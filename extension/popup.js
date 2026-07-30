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
    /* Long payloads (a photo is inlined) blow past QR capacity — the site does
       the same fallback to the photo-stripped link. */
    var url = full.length <= 900 && drawQr(full) ? full : (drawQr(lite) ? lite : full);
    if (url === lite && full.length > 900) { /* photo dropped from the QR link */ }
    state.url = url;

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

  document.addEventListener("DOMContentLoaded", function () {
    $("openSite").addEventListener("click", function (e) {
      e.preventDefault(); openTab(CC.SITE + "/app/dashboard.html");
    });
    $("makeCard").addEventListener("click", function () { openTab(CC.SITE + "/app/builder.html"); });
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
