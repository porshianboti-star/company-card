'use strict';
/* CompanyCard — connector server
   Real Google Workspace + Microsoft 365 directory sync over OAuth 2.0,
   plus a /api/provision endpoint. Pairs with the static front-end:
   set apiBase in app/config.js to this server's URL.
   Requires Node >= 18 (uses the built-in global fetch). */

const express = require('express');
const session = require('express-session');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

/* --- minimal .env loader so `node server.js` works without extra deps --- */
(function loadEnv() {
  try {
    const p = path.join(__dirname, '.env');
    if (!fs.existsSync(p)) return;
    fs.readFileSync(p, 'utf8').split('\n').forEach((line) => {
      const m = line.match(/^\s*([A-Za-z0-9_]+)\s*=\s*(.*?)\s*$/);
      if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
    });
  } catch (e) { /* ignore */ }
})();

const PORT = process.env.PORT || 4000;
const BASE_URL = process.env.BASE_URL || ('http://localhost:' + PORT);
const FRONTEND_ORIGIN = process.env.FRONTEND_ORIGIN || 'http://localhost:5500';
const SESSION_SECRET = process.env.SESSION_SECRET || 'dev-secret-change-me';
const COOKIE_SECURE = String(process.env.COOKIE_SECURE || 'false') === 'true';
const COOKIE_SAMESITE = process.env.COOKIE_SAMESITE || 'lax';

const PROVIDERS = {
  google: {
    authUrl: 'https://accounts.google.com/o/oauth2/v2/auth',
    tokenUrl: 'https://oauth2.googleapis.com/token',
    clientId: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    scope: 'openid email https://www.googleapis.com/auth/admin.directory.user.readonly',
    extraAuth: { access_type: 'offline', prompt: 'consent' }
  },
  microsoft: {
    authUrl: `https://login.microsoftonline.com/${process.env.MS_TENANT || 'common'}/oauth2/v2.0/authorize`,
    tokenUrl: `https://login.microsoftonline.com/${process.env.MS_TENANT || 'common'}/oauth2/v2.0/token`,
    clientId: process.env.MS_CLIENT_ID,
    clientSecret: process.env.MS_CLIENT_SECRET,
    scope: 'openid email offline_access https://graph.microsoft.com/User.Read.All',
    extraAuth: {}
  }
};
const redirectUri = (provider) => `${BASE_URL}/auth/${provider}/callback`;

const app = express();
app.use(express.json({ limit: '1mb' }));
app.use(cors({ origin: FRONTEND_ORIGIN, credentials: true }));
app.set('trust proxy', 1);
app.use(session({
  name: 'cc.sid',
  secret: SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: { httpOnly: true, secure: COOKIE_SECURE, sameSite: COOKIE_SAMESITE, maxAge: 1000 * 60 * 60 * 8 }
}));

/* Health / which providers are configured */
app.get('/healthz', (req, res) => {
  res.json({ ok: true, configured: Object.keys(PROVIDERS).filter((p) => PROVIDERS[p].clientId) });
});

/* 1) Begin OAuth — redirect the user to the provider's consent screen */
app.get('/auth/:provider', (req, res) => {
  const p = PROVIDERS[req.params.provider];
  if (!p) return res.status(404).send('Unknown provider');
  if (!p.clientId) return res.status(500).send('Provider not configured — set client id/secret in .env');
  const state = crypto.randomBytes(16).toString('hex');
  req.session.oauthState = state;
  const params = new URLSearchParams(Object.assign({
    client_id: p.clientId,
    redirect_uri: redirectUri(req.params.provider),
    response_type: 'code',
    scope: p.scope,
    state
  }, p.extraAuth));
  res.redirect(p.authUrl + '?' + params.toString());
});

/* 2) OAuth callback — exchange the code for an access token, then close the popup */
app.get('/auth/:provider/callback', async (req, res) => {
  const provider = req.params.provider;
  const p = PROVIDERS[provider];
  if (!p) return res.status(404).send('Unknown provider');
  if (!req.query.code) return res.status(400).send('Missing code');
  if (req.query.state !== req.session.oauthState) return res.status(400).send('State mismatch');
  try {
    const body = new URLSearchParams({
      code: req.query.code,
      client_id: p.clientId,
      client_secret: p.clientSecret,
      redirect_uri: redirectUri(provider),
      grant_type: 'authorization_code'
    });
    if (provider === 'microsoft') body.set('scope', p.scope);
    const tok = await fetchJSON(p.tokenUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body.toString()
    });
    req.session.tokens = req.session.tokens || {};
    req.session.tokens[provider] = { access_token: tok.access_token, refresh_token: tok.refresh_token, obtained: Date.now() };
    res.set('Content-Type', 'text/html').send(popupCloser(provider));
  } catch (e) {
    res.status(500).send('OAuth token exchange failed: ' + e.message);
  }
});

/* 3) Directory — fetch users from the connected provider, normalized */
app.get('/api/directory', async (req, res) => {
  const provider = req.query.provider;
  const p = PROVIDERS[provider];
  if (!p) return res.status(404).json({ error: 'unknown provider' });
  const tk = req.session.tokens && req.session.tokens[provider];
  if (!tk) return res.status(401).json({ error: 'not connected' });
  try {
    let users;
    if (provider === 'google') {
      const d = await fetchJSON(
        'https://admin.googleapis.com/admin/directory/v1/users?customer=my_customer&maxResults=200&orderBy=email',
        { headers: { Authorization: 'Bearer ' + tk.access_token } }
      );
      users = normalizeGoogle(d.users || []);
    } else {
      const d = await fetchJSON(
        "https://graph.microsoft.com/v1.0/users?$select=displayName,jobTitle,mail,userPrincipalName,department,mobilePhone&$top=200",
        { headers: { Authorization: 'Bearer ' + tk.access_token } }
      );
      users = normalizeMicrosoft(d.value || []);
    }
    res.json({ provider, count: users.length, users });
  } catch (e) {
    res.status(502).json({ error: 'directory fetch failed', detail: e.message });
  }
});

/* 4) Provision — persist the team (demo: writes data/teams.json; swap for your DB) */
app.post('/api/provision', (req, res) => {
  try {
    const dir = path.join(__dirname, 'data');
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);
    const file = path.join(dir, 'teams.json');
    const all = fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : [];
    const rec = {
      id: crypto.randomBytes(8).toString('hex'),
      at: Date.now(),
      company: req.body.company || {},
      status: req.body.status || 'invited',
      members: req.body.members || []
    };
    all.push(rec);
    fs.writeFileSync(file, JSON.stringify(all, null, 2));
    res.json({ ok: true, id: rec.id, provisioned: rec.members.length });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/me', (req, res) => {
  res.json({ connected: Object.keys((req.session && req.session.tokens) || {}) });
});

/* ---------- normalizers: provider shape -> { name,title,email,phone,dept } ---------- */
function normalizeGoogle(users) {
  return users.map((u, i) => {
    const org = (u.organizations && u.organizations[0]) || {};
    const phone = (u.phones && u.phones[0]) || {};
    return {
      id: u.id || ('g' + i),
      name: (u.name && u.name.fullName) || u.primaryEmail,
      title: org.title || '',
      email: u.primaryEmail || '',
      phone: phone.value || '',
      dept: org.department || ''
    };
  });
}
function normalizeMicrosoft(value) {
  return value.map((u, i) => ({
    id: u.id || ('m' + i),
    name: u.displayName || u.userPrincipalName,
    title: u.jobTitle || '',
    email: u.mail || u.userPrincipalName || '',
    phone: u.mobilePhone || '',
    dept: u.department || ''
  }));
}

async function fetchJSON(url, opts) {
  const r = await fetch(url, opts);
  const text = await r.text();
  let j; try { j = JSON.parse(text); } catch (e) { j = { raw: text }; }
  if (!r.ok) throw new Error((j.error && (j.error.message || j.error_description || j.error)) || ('HTTP ' + r.status));
  return j;
}

function popupCloser(provider) {
  return '<!doctype html><meta charset="utf-8"><body style="font-family:system-ui,sans-serif;text-align:center;padding:48px;color:#0B0A1F">' +
    '<h3>Connected ✓</h3><p>You can close this window.</p>' +
    '<script>try{window.opener&&window.opener.postMessage({type:"cc-auth",provider:' + JSON.stringify(provider) + '},' + JSON.stringify(FRONTEND_ORIGIN) + ');}catch(e){}setTimeout(function(){window.close();},300);</script></body>';
}

app.listen(PORT, () => console.log('CompanyCard connectors listening on ' + BASE_URL + '  (frontend origin: ' + FRONTEND_ORIGIN + ')'));
