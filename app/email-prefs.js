/* CompanyCard — Email preferences (Settings), 2026-09-29.
   Fills any <section data-email-prefs> on the page for a signed-in Supabase
   user: one checkbox bound to profiles.marketing_opt_in. Writes go through
   CCAuth.setMarketingOptIn -> RPC set_marketing_opt_in, which stamps server
   time and records the change in public.marketing_consent_log.
   The section stays hidden when there is no cloud account (demo/local mode). */
(function () {
  "use strict";

  function init() {
    var box = document.querySelector("[data-email-prefs]");
    if (!box || !window.CCAuth || CCAuth.mode !== "supabase") return;
    var cb = box.querySelector("input[type=checkbox]");
    var status = box.querySelector("[data-email-prefs-status]");
    if (!cb) return;

    function say(msg) { if (status) status.textContent = msg || ""; }

    var ready = CCAuth.session ? Promise.resolve(CCAuth.profile) : CCAuth.init();
    ready.then(function () { return CCAuth.marketingOptIn(); }).then(function (on) {
      if (on === null) return;           /* not signed in, or the read failed */
      cb.checked = on;
      box.hidden = false;
    });

    cb.addEventListener("change", function () {
      var want = cb.checked;
      cb.disabled = true; say("Saving…");
      CCAuth.setMarketingOptIn(want).then(function (now) {
        cb.disabled = false;
        if (now === null) { cb.checked = !want; say("Couldn’t save. Try again."); return; }
        cb.checked = now;
        say(now ? "Saved. You’ll get tips and offers by email." : "Saved. You won’t get tips or offers by email.");
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
