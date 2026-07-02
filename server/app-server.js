/* CompanyCard — self-hosted app server (no external services, zero dependencies).
   ---------------------------------------------------------------------------
   Run:   node server/app-server.js        (then open http://localhost:8787)

   What it does:
     • Serves the whole website + app (static files from the project folder)
     • REST API for accounts, login, invites and cards
     • Data lives in server/data.json on THIS computer
     • Passwords are stored ONLY as scrypt hashes (salted) — never plain text
     • Sessions via httpOnly cookie
     • Tenant isolation enforced on every endpoint:
         admin    → sees all cards/people of their own company only
         employee → sees only their own card
         anonymous→ only published cards (QR / share links)                 */
"use strict";

const http = require("http");
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const PORT = process.env.PORT || 8787;
const ROOT = path.join(__dirname, "..");            // project folder (the website)
const DATA_FILE = path.join(__dirname, "data.json");
const SESSION_DAYS = 14;
const INVITE_DAYS = 14;

/* ---------------- storage ---------------- */
let db = { companies: [], users: [], cards: [], invites: [], sessions: {} };
try { db = Object.assign(db, JSON.parse(fs.readFileSync(DATA_FILE, "utf8"))); } catch (e) { /* first run */ }

let saveTimer = null;
function flush() {
  try {
    const tmp = DATA_FILE + ".tmp";
    fs.writeFileSync(tmp, JSON.stringify(db, null, 2));
    fs.renameSync(tmp, DATA_FILE);                   // atomic swap — no corrupt files
  } catch (e) { console.error("Could not save data.json:", e.message); }
}
function persist() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(flush, 50);
}
/* always flush on shutdown so nothing is lost */
["SIGINT", "SIGTERM"].forEach(sig => process.on(sig, () => { flush(); process.exit(0); }));
process.on("exit", flush);
const uid = () => crypto.randomUUID();

/* ---------------- passwords (scrypt, salted) ---------------- */
function hashPassword(pw) {
  const salt = crypto.randomBytes(16).toString("hex");
  const hash = crypto.scryptSync(pw, salt, 64).toString("hex");
  return salt + ":" + hash;
}
function checkPassword(pw, stored) {
  const parts = String(stored).split(":");
  if (parts.length !== 2) return false;
  const test = crypto.scryptSync(pw, parts[0], 64);
  const ref = Buffer.from(parts[1], "hex");
  return test.length === ref.length && crypto.timingSafeEqual(test, ref);
}

/* ---------------- login throttle (5 fails -> 15 min lock) ---------------- */
const fails = new Map();
function throttled(key) {
  const f = fails.get(key);
  return !!(f && f.count >= 5 && Date.now() - f.at < 15 * 60 * 1000);
}
function noteFail(key) {
  const f = fails.get(key) || { count: 0, at: 0 };
  f.count = Date.now() - f.at > 15 * 60 * 1000 ? 1 : f.count + 1;
  f.at = Date.now();
  fails.set(key, f);
}

/* ---------------- sessions ---------------- */
function createSession(userId) {
  const token = crypto.randomBytes(32).toString("hex");
  db.sessions[token] = { userId, exp: Date.now() + SESSION_DAYS * 864e5 };
  persist();
  return token;
}
function sessionUser(req) {
  const m = /(?:^|;\s*)ccsid=([a-f0-9]{64})/.exec(req.headers.cookie || "");
  if (!m) return null;
  const s = db.sessions[m[1]];
  if (!s || s.exp < Date.now()) { if (s) { delete db.sessions[m[1]]; persist(); } return null; }
  return db.users.find(u => u.id === s.userId) || null;
}
function clearSession(req) {
  const m = /(?:^|;\s*)ccsid=([a-f0-9]{64})/.exec(req.headers.cookie || "");
  if (m && db.sessions[m[1]]) { delete db.sessions[m[1]]; persist(); }
}

/* ---------------- helpers ---------------- */
function json(res, code, obj, extraHeaders) {
  const h = Object.assign({ "Content-Type": "application/json; charset=utf-8" }, extraHeaders || {});
  res.writeHead(code, h);
  res.end(JSON.stringify(obj));
}
function readBody(req) {
  return new Promise((resolve, reject) => {
    let b = "";
    req.on("data", c => { b += c; if (b.length > 1e6) { reject(new Error("too big")); req.destroy(); } });
    req.on("end", () => { try { resolve(b ? JSON.parse(b) : {}); } catch (e) { reject(e); } });
  });
}
const norm = e => String(e || "").trim().toLowerCase();
function publicUser(u) {
  const c = db.companies.find(x => x.id === u.companyId);
  return { id: u.id, email: u.email, fullName: u.fullName, role: u.role,
           companyId: u.companyId, companyName: c ? c.name : "" };
}
function cookieFor(token) {
  return "ccsid=" + token + "; Path=/; HttpOnly; SameSite=Lax; Max-Age=" + SESSION_DAYS * 86400;
}

/* ---------------- API ---------------- */
async function api(req, res, url) {
  const p = url.pathname.replace(/\/+$/, "");
  const send = (code, obj, h) => json(res, code, obj, h);

  if (p === "/api/health") return send(200, { ok: true, mode: "local" });

  /* ---- signup: founder -> new company, becomes admin ---- */
  if (p === "/api/signup" && req.method === "POST") {
    const b = await readBody(req);
    const email = norm(b.email);
    if (!b.fullName || !b.companyName || !email || !b.password || String(b.password).length < 8)
      return send(400, { error: "Fill in every field — password needs 8+ characters." });
    if (db.users.some(u => u.email === email))
      return send(409, { error: "An account with this email already exists. Try signing in." });
    const company = { id: uid(), name: String(b.companyName).trim(), createdAt: Date.now() };
    const user = { id: uid(), email, fullName: String(b.fullName).trim(), role: "admin",
                   companyId: company.id, pass: hashPassword(String(b.password)), createdAt: Date.now() };
    db.companies.push(company); db.users.push(user); persist();
    return send(200, { user: publicUser(user) }, { "Set-Cookie": cookieFor(createSession(user.id)) });
  }

  /* ---- signup via invite -> employee joins that company ---- */
  if (p === "/api/signup-invite" && req.method === "POST") {
    const b = await readBody(req);
    const email = norm(b.email);
    const inv = db.invites.find(i => i.token === b.token && !i.acceptedAt && i.exp > Date.now());
    if (!inv) return send(400, { error: "Invite link is invalid or has expired. Ask your admin for a new one." });
    if (!b.fullName || !email || !b.password || String(b.password).length < 8)
      return send(400, { error: "Fill in every field — password needs 8+ characters." });
    if (inv.email && norm(inv.email) !== email)
      return send(400, { error: "This invite was issued for " + inv.email + "." });
    if (db.users.some(u => u.email === email))
      return send(409, { error: "An account with this email already exists. Try signing in." });
    const user = { id: uid(), email, fullName: String(b.fullName).trim(), role: inv.role || "employee",
                   companyId: inv.companyId, pass: hashPassword(String(b.password)), createdAt: Date.now() };
    db.users.push(user);
    inv.acceptedAt = Date.now(); inv.acceptedBy = user.id; persist();
    return send(200, { user: publicUser(user) }, { "Set-Cookie": cookieFor(createSession(user.id)) });
  }

  /* ---- login ---- */
  if (p === "/api/login" && req.method === "POST") {
    const b = await readBody(req);
    const email = norm(b.email);
    const key = email + "|" + (req.socket.remoteAddress || "");
    if (throttled(key)) return send(429, { error: "Too many attempts. Try again in 15 minutes." });
    const user = db.users.find(u => u.email === email);
    if (!user || !checkPassword(String(b.password || ""), user.pass)) {
      noteFail(key);
      return send(401, { error: "Wrong email or password." });
    }
    fails.delete(key);
    return send(200, { user: publicUser(user) }, { "Set-Cookie": cookieFor(createSession(user.id)) });
  }

  if (p === "/api/logout" && req.method === "POST") {
    clearSession(req);
    return send(200, { ok: true }, { "Set-Cookie": "ccsid=; Path=/; HttpOnly; Max-Age=0" });
  }

  /* ---- who am I ---- */
  if (p === "/api/me") {
    const u = sessionUser(req);
    return u ? send(200, { user: publicUser(u) }) : send(401, { error: "Not signed in" });
  }

  /* ---- public card (anonymous — QR / share link) ---- */
  let m = p.match(/^\/api\/public\/([\w-]+)$/);
  if (m) {
    const c = db.cards.find(x => x.slug === m[1] && x.isPublic);
    return c ? send(200, { data: c.data }) : send(404, { error: "Card not found" });
  }

  /* ---- invite info for the signup page (by token only) ---- */
  m = p.match(/^\/api\/invite\/([\w-]+)$/);
  if (m) {
    const inv = db.invites.find(i => i.token === m[1] && !i.acceptedAt && i.exp > Date.now());
    if (!inv) return send(404, { error: "Invalid invite" });
    const c = db.companies.find(x => x.id === inv.companyId);
    return send(200, { companyName: c ? c.name : "", email: inv.email || "", role: inv.role });
  }

  /* ---------- everything below needs a signed-in user ---------- */
  const user = sessionUser(req);
  if (!user) return send(401, { error: "Not signed in" });

  /* ---- invites (admin only) ---- */
  if (p === "/api/invites" && req.method === "POST") {
    if (user.role !== "admin") return send(403, { error: "Admins only" });
    const b = await readBody(req);
    const inv = { id: uid(), token: uid(), companyId: user.companyId, email: norm(b.email) || "",
                  role: b.role === "admin" ? "admin" : "employee", createdBy: user.id,
                  exp: Date.now() + INVITE_DAYS * 864e5, createdAt: Date.now() };
    db.invites.push(inv); persist();
    return send(200, { token: inv.token });
  }

  /* ---- people of my company (admin only) ---- */
  if (p === "/api/people") {
    if (user.role !== "admin") return send(403, { error: "Admins only" });
    return send(200, {
      people: db.users.filter(u => u.companyId === user.companyId)
        .map(u => ({ id: u.id, fullName: u.fullName, email: u.email, role: u.role, createdAt: u.createdAt }))
    });
  }

  /* ---- cards ---- */
  if (p === "/api/cards" && req.method === "GET") {
    if (user.role !== "admin") {
      const mine = db.cards.filter(c => c.ownerId === user.id);
      return send(200, { cards: mine.map(c => ({ slug: c.slug, data: c.data, updatedAt: c.updatedAt })) });
    }
    const all = db.cards.filter(c => c.companyId === user.companyId).map(c => {
      const o = db.users.find(u => u.id === c.ownerId);
      return { slug: c.slug, data: c.data, updatedAt: c.updatedAt,
               owner: o ? { id: o.id, fullName: o.fullName, email: o.email, role: o.role } : null };
    });
    return send(200, { cards: all });
  }

  m = p.match(/^\/api\/cards\/([\w-]+)$/);
  if (m && req.method === "PUT") {
    const b = await readBody(req);
    if (!b.data || typeof b.data !== "object") return send(400, { error: "Missing card data" });
    let card = db.cards.find(c => c.slug === m[1]);
    if (card && card.ownerId !== user.id && !(user.role === "admin" && card.companyId === user.companyId))
      return send(403, { error: "Not your card" });
    if (!card) {
      card = { id: uid(), slug: m[1], ownerId: user.id, companyId: user.companyId, createdAt: Date.now() };
      db.cards.push(card);
    }
    card.data = b.data;
    card.isPublic = b.isPublic !== false;
    card.updatedAt = Date.now();
    persist();
    return send(200, { ok: true });
  }
  if (m && req.method === "DELETE") {
    const card = db.cards.find(c => c.slug === m[1]);
    if (!card) return send(404, { error: "Not found" });
    const allowed = card.ownerId === user.id || (user.role === "admin" && card.companyId === user.companyId);
    if (!allowed) return send(403, { error: "Not your card" });
    db.cards = db.cards.filter(c => c !== card); persist();
    return send(200, { ok: true });
  }

  return send(404, { error: "Unknown API endpoint" });
}

/* ---------------- static files ---------------- */
const MIME = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript",
  ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg", ".webp": "image/webp", ".mp4": "video/mp4", ".webm": "video/webm",
  ".webmanifest": "application/manifest+json", ".ico": "image/x-icon", ".woff2": "font/woff2",
  ".md": "text/markdown", ".txt": "text/plain", ".xml": "application/xml" };

function serveStatic(req, res, url) {
  let file = decodeURIComponent(url.pathname);
  if (file === "/") file = "/index.html";
  const full = path.normalize(path.join(ROOT, file));
  if (!full.startsWith(ROOT)) { res.writeHead(403); return res.end("Forbidden"); }
  if (full.startsWith(path.join(ROOT, "server"))) { res.writeHead(403); return res.end("Forbidden"); } // never expose data.json
  fs.stat(full, (err, st) => {
    let target = full;
    if (!err && st.isDirectory()) target = path.join(full, "index.html");
    fs.readFile(target, (e2, buf) => {
      if (e2) { res.writeHead(404, { "Content-Type": "text/plain" }); return res.end("Not found"); }
      res.writeHead(200, {
        "Content-Type": MIME[path.extname(target).toLowerCase()] || "application/octet-stream",
        "X-Content-Type-Options": "nosniff"
      });
      res.end(buf);
    });
  });
}

/* ---------------- server ---------------- */
http.createServer((req, res) => {
  const url = new URL(req.url, "http://" + (req.headers.host || "localhost"));
  if (url.pathname.startsWith("/api/")) {
    Promise.resolve(api(req, res, url)).catch(e => json(res, 500, { error: "Server error: " + e.message }));
  } else {
    serveStatic(req, res, url);
  }
}).listen(PORT, () => {
  console.log("");
  console.log("  CompanyCard server is running");
  console.log("  Website:  http://localhost:" + PORT);
  console.log("  Sign up:  http://localhost:" + PORT + "/app/signup.html");
  console.log("  Data:     " + DATA_FILE);
  console.log("");
});
