/* CompanyCard extension — popup. Everything here is local: the card comes from
   chrome.storage.local, the QR is drawn in-page, the vCard is built in-page. */
(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };
  var state = { cards: [], card: null, url: "" };

  function msg(text, isErr) {
    var el = $("msg");
    el.textContent = text || "";
    el.className = "msg" + (isErr ? " err" : "");
    if (text) setTimeout(function () { if (el.textContent === text) el.textContent = ""; }, 2600);
  }

  function openTab(url) { chrome.tabs.create({ url: url }); window.close(); }

  function drawQr(url) {
    var box = $("qr");
    box.textContent = "";
    if (typeof QRCode === "undefined") return false;
    try {
      new QRCode(box, {
        text: url, width: 168, height: 168,
        colorDark: "#0B0A1F", colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.M
      });
      return true;
    } catch (e) { box.textContent = ""; return false; }
  }

  function render(card) {
    state.card = card;
    var full = CC.shareUrl(card);
    var lite = CC.shareUrl(card, true);
    /* A photo is inlined as a data URI, so any card carrying one is far past QR
       capacity and the code has to fall back to the photo-stripped link. That
       fallback used to be assigned to `url` and then used for the copy field and
       "Open card" as well — so every card with a photo handed out a link that
       dropped it, and the recipient saw grey initials instead of a face. It hit
       100% of photo-bearing cards and needed no unusual input at all. The notice
       that should have explained it was an empty stub.

       app/dashboard.html:119-122 already had this right: the LINK is always the
       full card, only the QR degrades, and it says so. Same shape here now. */
    state.url = full;
    var qrIsLite = false;
    if (full.length <= 900 && drawQr(full)) { qrIsLite = false; }
    else if (drawQr(lite)) { qrIsLite = true; }
    else { drawQr(full); }
    var note = $("qrnote");
    if (note) note.hidden = !(qrIsLite && (card.photo || card.cover));

    $("name").textContent = card.name || "Untitled card";
    var bits = [card.title, card.company].filter(Boolean);
    $("sub").textContent = bits.join(" · ");
    $("link").value = url;
  }

  function boot(res) {
    if (!res || !res.ok || !res.cards.length) {
      $("empty").hidden = false;
      return;
    }
    state.cards = res.cards;
    $("tool").hidden = false;

    var active = res.cards.filter(function (c) { return c.id === res.activeId; })[0] || res.cards[0];

    if (res.cards.length > 1) {
      var pick = $("pick");
      pick.hidden = false;
      res.cards.forEach(function (c) {
        var o = document.createElement("option");
        o.value = c.id;
        o.textContent = c.name || "Untitled card";
        if (c.id === active.id) o.selected = true;
        pick.appendChild(o);
      });
      pick.addEventListener("change", function () {
        var c = state.cards.filter(function (x) { return x.id === pick.value; })[0];
        if (!c) return;
        chrome.runtime.sendMessage({ type: "setActive", id: c.id }, function () { void chrome.runtime.lastError; });
        render(c);
      });
    }
    render(active);
  }

  async function copy(text, html) {
    if (html && window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
      await navigator.clipboard.write([new ClipboardItem({
        "text/html": new Blob([html], { type: "text/html" }),
        "text/plain": new Blob([text], { type: "text/plain" })
      })]);
      return;
    }
    await navigator.clipboard.writeText(text);
  }

  /* Tag traffic the extension sends to the site. The Chrome Web Store listing
     ranks #1 for "digital business card" (measured 2026-08-09), so this is the
     one channel we know is working — and until now its visits arrived untagged
     and were indistinguishable from direct traffic in GA4. */
  function siteUrl(path, source) {
    return CC.SITE + path + "?utm_source=chrome_extension&utm_medium=popup&utm_campaign=" + source;
  }

  document.addEventListener("DOMContentLoaded", function () {
    $("openSite").addEventListener("click", function (e) {
      e.preventDefault(); openTab(siteUrl("/app/dashboard.html", "open_dashboard"));
    });
    $("makeCard").addEventListener("click", function () { openTab(siteUrl("/app/builder.html", "empty_state_create")); });
    $("openCard").addEventListener("click", function () { if (state.url) openTab(state.url); });

    $("copyLink").addEventListener("click", function () {
      copy(state.url).then(function () { msg("Link copied"); })
        .catch(function () { msg("Could not copy", true); });
    });

    $("copySig").addEventListener("click", function () {
      if (!state.card) return;
      var html = CC.signature(state.card);
      var plain = [state.card.name, [state.card.title, state.card.company].filter(Boolean).join(" · "), state.url]
        .filter(Boolean).join("\n");
      copy(plain, html).then(function () { msg("Signature copied — paste it in Gmail"); })
        .catch(function () { msg("Could not copy", true); });
    });

    $("vcf").addEventListener("click", function () {
      if (!state.card) return;
      var blob = new Blob([CC.vcard(state.card)], { type: "text/vcard;charset=utf-8" });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = (state.card.name || "contact").replace(/\s+/g, "_") + ".vcf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
      msg("Contact file saved");
    });

    chrome.runtime.sendMessage({ type: "status" }, function (res) {
      void chrome.runtime.lastError;
      boot(res);
    });
  });
})();
