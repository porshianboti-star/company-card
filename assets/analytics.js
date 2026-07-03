/* CompanyCard — lightweight product analytics.
   Sends anonymous funnel events to Supabase (insert-only; nobody can read
   raw events through the public key — stats come via an aggregate RPC).
   Events: create_card_click, share_save_click, signup, checkout_click, pro_paid */
(function () {
  "use strict";
  var URL = "https://ohobtgbyrlczfdztzvqi.supabase.co/rest/v1/events";
  var KEY = "sb_publishable_H3hDKJRE0oOH7dkg7496Rw_trmUMPW9";

  function sid() {
    try {
      var s = localStorage.getItem("cc_sid");
      if (!s) { s = Math.random().toString(36).slice(2) + Date.now().toString(36); localStorage.setItem("cc_sid", s); }
      return s;
    } catch (e) { return "anon"; }
  }

  var sent = {}; /* de-dupe identical events within one page view */
  window.CCTrack = function (ev) {
    try {
      if (sent[ev]) return; sent[ev] = 1;
      setTimeout(function () { delete sent[ev]; }, 4000);
      fetch(URL, {
        method: "POST",
        headers: { apikey: KEY, "Content-Type": "application/json", Prefer: "return=minimal" },
        body: JSON.stringify({
          event: ev,
          session_id: sid(),
          user_id: (window.CCAuth && CCAuth.profile && CCAuth.profile.id) || null,
          path: location.pathname
        }),
        keepalive: true
      }).catch(function () {});
    } catch (e) {}
  };

  /* ---- automatic click tracking ---- */
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("a,button");
    if (!el) return;
    var href = (el.getAttribute && el.getAttribute("href")) || "";
    if (/builder(\.html)?$/.test(href.split("?")[0])) CCTrack("create_card_click");
    else if (/checkout/.test(href)) CCTrack("checkout_click");
    if (el.id === "btn-share" || el.id === "btn-save") CCTrack("share_save_click");
    else if (/^(share card|save|save contact|share)$/i.test((el.textContent || "").trim())) CCTrack("share_save_click");
  }, true);

  /* checkout page view = entered payment (covers JS-driven navigation too) */
  if (/checkout\.html$/.test(location.pathname) || /\/checkout$/.test(location.pathname)) CCTrack("checkout_click");

  /* ---- fake-payment success → pro account ---- */
  var tries = 0;
  var t = setInterval(function () {
    tries++;
    if (window.CC && CC.setPro && !CC.setPro.__tracked) {
      var orig = CC.setPro;
      CC.setPro = function (plan) { CCTrack("pro_paid"); return orig(plan); };
      CC.setPro.__tracked = true;
      clearInterval(t);
    }
    if (tries > 15) clearInterval(t);
  }, 400);
})();
