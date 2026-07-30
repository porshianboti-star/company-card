/* CompanyCard extension — content script.
   Runs only on https://company-card.com/app/* (the signed-in user's own
   CompanyCard pages) and copies the cards that page already keeps in
   localStorage into the extension, so the toolbar popup can show them.
   Read-only: it never writes to the page and never contacts a server. */
(function () {
  "use strict";
  var KEY = "cc_cards_v1";

  function readCards() {
    try {
      var a = JSON.parse(localStorage.getItem(KEY));
      return Array.isArray(a) ? a : [];
    } catch (e) { return []; }
  }

  var lastSent = "";
  function sync() {
    var cards = readCards();
    if (!cards.length) return;
    var json = JSON.stringify(cards);
    if (json === lastSent) return;
    lastSent = json;
    try {
      chrome.runtime.sendMessage({ type: "syncCards", cards: cards }, function () {
        void chrome.runtime.lastError; // popup/worker may be closed — ignore
      });
    } catch (e) { /* extension context invalidated on reload */ }
  }

  sync();
  /* The page hydrates from the cloud shortly after load, and the builder saves
     while the user edits — re-check for a short while, then on every change. */
  var ticks = 0;
  var timer = setInterval(function () { sync(); if (++ticks >= 8) clearInterval(timer); }, 1500);
  window.addEventListener("storage", sync);
  window.addEventListener("focus", sync);
  window.addEventListener("beforeunload", sync);
})();
