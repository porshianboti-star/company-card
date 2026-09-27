/* CompanyCard — public card page composition, shared by app/card.html (the
   card travels in the URL: #c= or ?id=) and app/c.html (the card lives in
   Supabase and is served at /c/<slug>). The card itself is drawn by
   CC.renderCard in product.js; this file owns everything around it — the
   "Scan to open" QR panel, the "Make your own CompanyCard" credit, the
   Save-contact handler and the GA4 signup_click — so the two pages cannot
   drift apart. Every href is root-absolute: c.html is served at /c/<slug>,
   where a relative "builder.html" would resolve to /c/builder.html. */
(function () {
  "use strict";

  var LOGO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 388 84" width="388" height="84" role="img" aria-label="CompanyCard" class="logo-lockup" style="height:30px;margin:0 auto 18px"><rect x="9" y="18" width="74" height="48" rx="9" stroke="#1A1814" stroke-width="2" fill="none"/><path d="M 57.19,26.81 A 13,13 0 1 0 57.19,45.19" stroke="#1A1814" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.3"/><path d="M 43.19,36.81 A 13,13 0 1 0 43.19,55.19" stroke="#1A1814" stroke-width="6" stroke-linecap="round" fill="none"/><text x="104" y="56.5" font-family="Marcellus, Georgia, serif" font-size="42" letter-spacing="1" fill="#1A1814">CompanyCard</text></svg>';
  var PLUS = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>';
  /* Absolute + tagged so the credit is the same crawlable link whether the card
     is opened from a share, embedded on someone else's site or served at
     /c/<slug>; _top so a click inside the 360x600 embed iframe opens the
     builder full-page rather than inside the frame. */
  var BUILDER = "https://company-card.com/app/builder.html?utm_source=shared_card";

  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function toast(m) {
    var t = document.getElementById("toast"); if (!t) return;
    t.textContent = m; t.classList.add("show"); clearTimeout(t._t);
    t._t = setTimeout(function () { t.classList.remove("show"); }, 2200);
  }

  var V = (window.CCView = {});
  V.toast = toast;

  /* Empty / not-public state. opts: { title, text, cta } */
  V.empty = function (view, opts) {
    opts = opts || {};
    view.innerHTML =
      '<div class="cc-shell" style="padding:40px 28px;text-align:center">' + LOGO +
      '<h2 style="margin-bottom:8px">' + esc(opts.title || "No card to show") + '</h2>' +
      '<p style="color:var(--slate-500);margin-bottom:22px">' + esc(opts.text || "This link doesn't contain a card yet.") + '</p>' +
      '<a class="btn btn-primary btn-lg" href="/app/builder.html">' + esc(opts.cta || "Create your free card") + '</a></div>';
  };

  /* The card. opts: { qrUrl, qrFallback, source, pageLocation } */
  V.show = function (view, card, opts) {
    opts = opts || {};
    var qrCard = card.showQR ? "" :
      '<div class="qr-card"><h3>Scan to open</h3><p>Point a camera here to share this card.</p>' +
      '<div class="qrbox" id="qr" style="margin-top:14px"></div></div>';
    view.innerHTML =
      '<div class="cc-shell" id="cc">' + CC.renderCard(card) + '</div>' +
      qrCard +
      '<div class="made"><a class="btn btn-ghost" href="' + BUILDER + '" target="_top">' + PLUS + ' Make your own CompanyCard</a></div>';

    var ccEl = document.getElementById("cc");
    ccEl.addEventListener("click", function (e) {
      if (e.target.closest("[data-save]")) { e.preventDefault(); CC.downloadVcard(card); toast("Contact downloaded"); }
    });

    /* A shared card is the one place we reach someone who is not looking for
       us — the product's only growth channel that owes nothing to domain
       authority. Reported as signup_click so it lands in the same funnel as
       the site's CTAs, with a source so the viral loop can be told apart:
       "shared_card" (card.html) or "public_card" (/c/<slug>). */
    var madeEl = view.querySelector(".made a");
    if (madeEl) {
      madeEl.addEventListener("click", function () {
        try {
          if (typeof gtag === "function") {
            gtag("event", "signup_click", { source: opts.source || "shared_card", page_location: opts.pageLocation || "/app/card" });
          }
        } catch (e) { /* never block the navigation on analytics */ }
      });
    }

    if (card.showQR) { CC.fillQR(ccEl, card); }
    else {
      var qel = document.getElementById("qr");
      if (!CC.qr(qel, opts.qrUrl || location.href, 168) && opts.qrFallback) CC.qr(qel, opts.qrFallback, 168);
    }
  };
})();
