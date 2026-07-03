/* CompanyCard — authentication & multi-tenant data layer.
   ------------------------------------------------------------------
   Works in one of three modes, picked automatically:

     "local"    — DEFAULT. Talks to the built-in server (server/app-server.js)
                  over /api. Accounts, hashed passwords and cards are stored
                  on your own machine (server/data.json). Start it with:
                      node server/app-server.js
     "supabase" — if supabaseUrl/supabaseAnonKey are set in config.js
                  (optional cloud alternative, see supabase-setup.sql).
     "demo"     — when the site is opened as plain files (file://).
                  No real accounts; the old localStorage demo behaviour.

   Security model (enforced by the server, not by this file):
     admin    → sees every card/profile of their own company
     employee → sees only their own card
     tenants  → fully isolated from each other                       */
(function () {
  "use strict";

  var cfg = window.CC_CONFIG || {};
  var MODE =
    (cfg.supabaseUrl && cfg.supabaseAnonKey && window.supabase) ? "supabase" :
    (/^https?:$/.test(location.protocol)) ? "local" : "demo";

  var sb = MODE === "supabase" ? window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey) : null;

  var A = (window.CCAuth = {
    mode: MODE,
    enabled: MODE !== "demo",
    client: sb,
    session: null,
    profile: null,
    company: null
  });

  /* ---------- tiny fetch helper (local mode) ---------- */
  function call(method, path, body) {
    return fetch(path, {
      method: method,
      headers: body ? { "Content-Type": "application/json" } : undefined,
      body: body ? JSON.stringify(body) : undefined,
      credentials: "same-origin"
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok) return { error: { message: (j && j.error) || ("Request failed (" + r.status + ")") } };
        return { data: j };
      });
    }).catch(function () {
      return { error: { message: "Can’t reach the CompanyCard server. Is it running? (node server/app-server.js)" } };
    });
  }

  function profileFromLocal(u) {
    return { id: u.id, company_id: u.companyId, role: u.role, full_name: u.fullName,
             email: u.email, companies: { name: u.companyName } };
  }

  /* ---------- session & profile ---------- */
  A.init = function () {
    if (MODE === "demo") return Promise.resolve(null);
    if (MODE === "local") {
      return call("GET", "/api/me").then(function (r) {
        if (r.error || !r.data.user) return null;
        A.session = { user: { id: r.data.user.id } };
        A.profile = profileFromLocal(r.data.user);
        A.company = A.profile.companies;
        return A.profile;
      });
    }
    return sb.auth.getSession().then(function (r) {
      A.session = (r.data && r.data.session) || null;
      if (!A.session) return null;
      return sb.from("profiles").select("id, company_id, role, full_name, email, companies(name)")
        .eq("id", A.session.user.id).single()
        .then(function (p) {
          if (p.error || !p.data) return null;
          A.profile = p.data;
          A.company = p.data.companies || null;
          return A.profile;
        });
    });
  };

  function here() { return location.pathname.split("/").pop() || "dashboard.html"; }
  function goLogin() { location.replace("login.html?next=" + encodeURIComponent(here())); }

  /* guard("admin") — admins only. guard("any") — any signed-in user. */
  A.guard = function (need) {
    if (MODE === "demo") return Promise.resolve(null);
    return A.init().then(function (p) {
      if (!p) { goLogin(); return null; }
      if (need === "admin" && p.role !== "admin") { location.replace("employee.html"); return null; }
      return p;
    });
  };

  /* ---------- auth actions (all return { error } / { data:{session} }) ---------- */
  function trackSignup(r) {
    if (!r || !r.error) { try { window.CCTrack && CCTrack("signup"); } catch (e) {} }
    return r;
  }
  A.signupAdmin = function (fullName, companyName, email, password) {
    if (MODE === "local")
      return call("POST", "/api/signup",
        { fullName: fullName, companyName: companyName, email: email, password: password })
        .then(function (r) { return r.error ? r : { data: { session: true } }; }).then(trackSignup);
    return sb.auth.signUp({ email: email, password: password,
      options: { data: { full_name: fullName, company_name: companyName } } }).then(trackSignup);
  };

  A.signupInvited = function (fullName, email, password, token) {
    if (MODE === "local")
      return call("POST", "/api/signup-invite",
        { fullName: fullName, email: email, password: password, token: token })
        .then(function (r) { return r.error ? r : { data: { session: true } }; }).then(trackSignup);
    return sb.auth.signUp({ email: email, password: password,
      options: { data: { full_name: fullName, invite_token: token } } }).then(trackSignup);
  };

  A.login = function (email, password) {
    if (MODE === "local")
      return call("POST", "/api/login", { email: email, password: password });
    return sb.auth.signInWithPassword({ email: email, password: password });
  };

  A.logout = function () {
    var done = function () { location.href = "login.html"; };
    if (MODE === "local") { call("POST", "/api/logout").then(done, done); return; }
    if (MODE === "supabase") { sb.auth.signOut().then(done, done); return; }
    done();
  };

  A.inviteInfo = function (token) {
    if (MODE === "local")
      return call("GET", "/api/invite/" + encodeURIComponent(token)).then(function (r) {
        if (r.error) return null;
        return { company_name: r.data.companyName, email: r.data.email, role: r.data.role };
      });
    return sb.rpc("invite_info", { p_token: token }).then(function (r) {
      return (r.data && r.data[0]) || null;
    });
  };

  A.homeFor = function (role) { return role === "admin" ? "dashboard.html" : "employee.html"; };

  /* ---------- invites (admin) ---------- */
  A.createInvite = function (email, role) {
    var base = location.href.replace(/[^/]*(\?.*)?$/, "");
    if (MODE === "local")
      return call("POST", "/api/invites", { email: email, role: role || "employee" })
        .then(function (r) {
          if (r.error) throw new Error(r.error.message);
          return base + "signup.html?invite=" + r.data.token;
        });
    return A.init().then(function (p) {
      if (!p || p.role !== "admin") throw new Error("Admins only");
      return sb.from("invites")
        .insert({ company_id: p.company_id, email: email || null, role: role || "employee", created_by: p.id })
        .select("token").single();
    }).then(function (r) {
      if (r.error) throw r.error;
      return base + "signup.html?invite=" + r.data.token;
    });
  };

  /* ---------- cards ---------- */
  A.pushCard = function (card) {
    if (!A.enabled || !A.session) return Promise.resolve(null);
    if (MODE === "local")
      return call("PUT", "/api/cards/" + encodeURIComponent(card.id),
        { data: card, isPublic: card.isPublic !== false });
    return sb.from("cards").upsert({
      company_id: A.profile.company_id, owner_id: A.session.user.id,
      slug: card.id, is_public: card.isPublic !== false, data: card
    }, { onConflict: "slug" });
  };

  A.deleteCard = function (cardId) {
    if (!A.enabled || !A.session) return Promise.resolve(null);
    if (MODE === "local") return call("DELETE", "/api/cards/" + encodeURIComponent(cardId));
    return sb.from("cards").delete().eq("slug", cardId);
  };

  A.myCards = function () {
    if (MODE === "local")
      return call("GET", "/api/cards").then(function (r) {
        if (r.error) return { error: r.error, data: null };
        return { data: r.data.cards.map(function (c) { return { slug: c.slug, data: c.data, updated_at: c.updatedAt }; }) };
      });
    return sb.from("cards").select("slug, data, updated_at")
      .eq("owner_id", A.session.user.id).order("updated_at", { ascending: false });
  };

  /* Mark the current user's plan (called when the fake payment completes). */
  A.setPlan = function (plan) {
    if (MODE !== "supabase" || !A.session) return Promise.resolve(null);
    return sb.from("profiles").update({ plan: plan || "pro" }).eq("id", A.session.user.id);
  };

  /* Every card + owner of my company (admin only — server enforces). */
  A.companyCards = function () {
    if (MODE === "local") return call("GET", "/api/cards").then(function (r) {
      return r.error ? { error: r.error, data: null } : { data: r.data.cards };
    });
    return sb.from("cards")
      .select("slug, data, updated_at, owner_id, profiles:owner_id (full_name, email, role)")
      .order("updated_at", { ascending: false });
  };

  A.companyPeople = function () {
    if (MODE === "local") return call("GET", "/api/people").then(function (r) {
      return r.error ? { error: r.error, data: null } : { data: r.data.people };
    });
    return sb.from("profiles").select("id, full_name, email, role, created_at")
      .order("created_at", { ascending: true });
  };

  /* Public card by slug (anonymous visitors — QR / share link). */
  A.publicCard = function (slug) {
    if (MODE === "local")
      return call("GET", "/api/public/" + encodeURIComponent(slug)).then(function (r) {
        return r.error ? { error: r.error, data: null } : { data: { data: r.data.data } };
      });
    return sb.from("cards").select("data").eq("slug", slug).eq("is_public", true).single();
  };

  /* ---------- keep local demo storage in sync ---------- */
  A.syncLocal = function () {
    if (!A.enabled || !A.session || !window.CC) return Promise.resolve();
    return A.myCards().then(function (r) {
      if (r.error || !r.data) return;
      r.data.forEach(function (row) { if (row.data && row.data.id) window.CC.save(row.data); });
    });
  };

  document.addEventListener("DOMContentLoaded", function () {
    if (!A.enabled || !window.CC) return;
    var save = window.CC.save, remove = window.CC.remove;
    window.CC.save = function (card) { save(card); A.pushCard(card); };
    window.CC.remove = function (id) { remove(id); A.deleteCard(id); };
    A.init().then(function (p) { if (p) A.syncLocal(); });
  });

  /* ---------- sign-out buttons ---------- */
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("[data-signout]");
    if (el) { e.preventDefault(); A.logout(); }
  });
})();
