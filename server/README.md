# CompanyCard — Connector server

Real **Google Workspace** & **Microsoft 365** directory sync (plus card provisioning) for CompanyCard Teams.

The static site works on its own with a built‑in **demo** (simulated directories). This server adds the **real** connections. When you set `apiBase` in `app/config.js` to this server's URL, the onboarding flow's *Connect* buttons use real OAuth + your live directory instead of the demo.

```
Browser (static site)  ──Connect──▶  this server  ──OAuth──▶  Google / Microsoft
        ▲                                  │
        └──────  normalized users  ◀───────┘   (GET /api/directory)
```

---

## 1. Run it

```bash
cd server
npm install
cp .env.example .env      # then fill in the values below
npm start                 # → http://localhost:4000
```

Requires **Node 18+** (uses the built‑in `fetch`). Health check: `GET /healthz`.

---

## 2. Google Workspace setup

1. **Google Cloud Console** → create/select a project.
2. **APIs & Services → Library →** enable **Admin SDK API**.
3. **APIs & Services → Credentials → Create credentials → OAuth client ID → Web application**.
4. **Authorised redirect URI:** `http://localhost:4000/auth/google/callback` (use your real `BASE_URL` in production).
5. Copy the **Client ID / Client secret** into `.env` (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`).
6. The person who connects must be a **Workspace admin** (scope `admin.directory.user.readonly` reads your org's users).

## 3. Microsoft 365 / Entra ID setup

1. **Azure Portal → Microsoft Entra ID → App registrations → New registration.**
2. **Redirect URI (Web):** `http://localhost:4000/auth/microsoft/callback`.
3. **Certificates & secrets →** create a **client secret**.
4. **API permissions → Add → Microsoft Graph → Delegated →** `User.Read.All` → **Grant admin consent**.
5. Copy **Application (client) ID**, the **secret value**, and your **Directory (tenant) ID** into `.env`
   (`MS_CLIENT_ID`, `MS_CLIENT_SECRET`, `MS_TENANT`). Use `common` for multi‑tenant.

---

## 4. Point the site at the server

In `app/config.js`:

```js
window.CC_CONFIG = { apiBase: "http://localhost:4000", providers: { google:true, microsoft:true, csv:true } };
```

Set `FRONTEND_ORIGIN` in `.env` to wherever the static site is served (e.g. `http://localhost:5500`). Now in the onboarding wizard, **Connect Google Workspace / Microsoft 365** opens the real consent screen, and the user list comes from your directory. CSV import is handled entirely in the browser and needs no server.

> Leave `apiBase` empty to fall back to the built‑in demo at any time.

---

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/auth/:provider` | Start OAuth (`google` \| `microsoft`) |
| GET | `/auth/:provider/callback` | Token exchange, closes the popup |
| GET | `/api/directory?provider=` | Normalized users `{ name, title, email, phone, dept }` |
| POST | `/api/provision` | Persist `{ company, members, status }` (demo writes `data/teams.json`) |
| GET | `/api/me` | Which providers the session is connected to |
| GET | `/healthz` | Status + configured providers |

## Production notes

- Serve over **HTTPS** and set `COOKIE_SECURE=true`, `COOKIE_SAMESITE=none` (cross‑site cookies for the popup → API calls).
- Store tokens in a real session store / database (the demo keeps them in memory and writes JSON). Use the `refresh_token` to keep directories in sync.
- Lock `FRONTEND_ORIGIN` to your exact site origin; never use `*` with credentials.
- Swap `/api/provision`'s file write for your database, and trigger the actual invite emails there.
