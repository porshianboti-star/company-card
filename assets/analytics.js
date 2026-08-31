/* CompanyCard — lightweight product analytics.
   Sends anonymous funnel events to Supabase (insert-only; nobody can read
   raw events through the public key — stats come via an aggregate RPC).
   Events: card_view, create_card_click, builder_save_draft, card_share_open,
   card_save_contact, signup, checkout_click, pro_paid.
   `share_save_click` was retired 2026-08-11 — it conflated the owner saving a
   draft with the recipient saving a contact, so historical rows of that event
   cannot be split and should not be read as a viral signal. */
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

  /* One definition of "a recipient is looking at a shared card", used by both
     card_view and card_save_contact so the two ends of the loop can never
     drift apart again. The card travels in the URL (hash for the encoded card,
     ?id= for a stored one), so an owner opening the bare page is excluded.
     Function declaration, not a var — the click listener below is registered
     before this point in source order and must still be able to call it. */
  function _viewingSharedCard() {
    if (!/\/app\/(card|mobile)(\.html)?$/.test(location.pathname)) return false;
    try {
      return (location.hash && location.hash.length > 1) ||
             !!new URLSearchParams(location.search).get("id");
    } catch (e) { return false; }
  }

  /* ---- automatic click tracking ---- */
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("a,button");
    if (!el) return;
    var href = (el.getAttribute && el.getAttribute("href")) || "";
    if (/builder(\.html)?$/.test(href.split("?")[0])) CCTrack("create_card_click");
    else if (/checkout/.test(href)) CCTrack("checkout_click");
    /* Until 2026-08-11 every one of these fired a single `share_save_click`,
       including a text match on /^(share card|save|save contact|share)$/i. That
       collapsed the card OWNER saving their own draft together with the
       RECIPIENT saving the contact — opposite ends of the loop — into one
       number, which made the viral coefficient uncomputable rather than merely
       unknown. The text branch is gone: it matched any button reading "Save"
       anywhere on the site. */
    if (el.id === "btn-save" || el.id === "btn-save2") CCTrack("builder_save_draft");
    else if (el.id === "btn-share" || el.id === "btn-share2") CCTrack("card_share_open");
    /* CC:SAVE-ATTRIBUTION v1 (2026-08-31) — card_save_contact was measuring the
       wrong people, in both directions.

       FALSE NEGATIVE: the recipient's Save button on a shared card is rendered
       by CC.renderCard as `<button class="cc-save" data-save>` with NO id, and
       this branch only ever matched ids. The one event that means "a stranger
       put our user in their phone" — the whole viral loop — could not fire.

       FALSE POSITIVE: both ids it did match are the ACCOUNT OWNER acting on
       their own data. `dl-vcf` is the "Save contact" button inside the
       builder's own share modal; `save` is the button in the mobile lead
       editor (the fields around it are Tags and "Where you met, follow-ups…"),
       i.e. our user filing a lead they collected. Counting either as a viral
       signal is the same owner/recipient conflation that retiring
       share_save_click was meant to end — and it biased the number in the
       flattering direction, since every row it could ever produce came from
       our own users.

       So: attribute by WHO is looking, not by which id was clicked. A shared
       card is one whose card travels in the URL — the same test card_view uses
       below, which correctly excludes an owner opening the bare page. */
    else if (el.matches && el.matches("[data-save]")) CCTrack(_viewingSharedCard() ? "card_save_contact" : "owner_save_own_vcard");
    else if (el.id === "dl-vcf" || el.id === "vcf") CCTrack("owner_save_own_vcard");
    else if (el.id === "save") CCTrack("lead_saved");
  }, true);

  /* A shared card being viewed is step one of the only growth loop that does not
     depend on domain authority (D-031) — and it fired nothing at all until
     2026-08-11, so the loop was measured from its second step onward. Only count
     a real recipient view: the viewer renders from location.hash or ?id=, so an
     owner opening the bare page is correctly excluded. */
  if (_viewingSharedCard()) CCTrack("card_view");

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
