/* CompanyCard — front-end configuration.
   ----------------------------------------------------------------
   Leave apiBase EMPTY to use the built-in demo (simulated Google /
   Microsoft directories — works with no server).

   To use REAL Google Workspace / Microsoft 365 sync, deploy the
   connector server in /server and put its URL here, e.g.
   apiBase: "https://connectors.company-card.com"
   (see /server/README.md for the full setup).                      */
window.CC_CONFIG = {
  /* --- User accounts (Supabase) ---------------------------------
     Create a free project at https://supabase.com, run the SQL in
     /supabase-setup.sql, then paste the two values from
     Project Settings → API. While these are empty the app runs in
     the local demo mode with no real accounts.                    */
  supabaseUrl: "https://ohobtgbyrlczfdztzvqi.supabase.co",
  supabaseAnonKey: "sb_publishable_H3hDKJRE0oOH7dkg7496Rw_trmUMPW9",

  /* --- Real directory import (Google Workspace / Microsoft 365) ------
     Public OAuth Client IDs (safe to expose — no secret). An admin signs
     in and consents, then real users are pulled from the directory.
     Leave empty and the connect buttons show one-time setup steps.
     See SETUP-DIRECTORY.md.                                            */
  googleClientId: "662555521030-bglsdji31m4p9ruhuq2hqgf13u9qsoau.apps.googleusercontent.com",
  msClientId: "",

  apiBase: "",
  providers: { google: true, microsoft: true, csv: true }
};
