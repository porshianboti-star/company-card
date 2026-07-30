/* CompanyCard extension — card helpers.
   A trimmed copy of the parts of app/product.js the popup needs, so the
   extension can render a card completely offline (no remote code, no API). */
(function (global) {
  "use strict";
  var CC = {};

  CC.SITE = "https://company-card.com";

  CC.themes = {
    indigo: { solid: "#6366F1" },
    violet: { solid: "#8B5CF6" },
    teal:   { solid: "#0EA5E9" },
    rose:   { solid: "#F43F5E" },
    amber:  { solid: "#F59E0B" },
    green:  { solid: "#16A34A" },
    ink:    { solid: "#0B0A1F" }
  };
  CC.themeOf = function (card) {
    if (card && card.theme === "custom" && card.customColor) return { solid: card.customColor };
    return CC.themes[card && card.theme] || CC.themes.indigo;
  };

  CC.esc = function (s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  };
  CC.initials = function (name) {
    return (name || "").trim().split(/\s+/).slice(0, 2)
      .map(function (w) { return w[0] || ""; }).join("").toUpperCase() || "CC";
  };

  /* url-safe base64 of UTF-8 JSON — must stay byte-identical to app/product.js */
  CC.encode = function (card, lite) {
    var c = JSON.parse(JSON.stringify(card));
    if (lite) { delete c.photo; delete c.cover; }
    var b = btoa(unescape(encodeURIComponent(JSON.stringify(c))));
    return b.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  };
  CC.decode = function (s) {
    try {
      s = String(s).replace(/-/g, "+").replace(/_/g, "/");
      while (s.length % 4) s += "=";
      return JSON.parse(decodeURIComponent(escape(atob(s))));
    } catch (e) { return null; }
  };
  CC.shareUrl = function (card, lite) {
    return CC.SITE + "/app/card.html#c=" + CC.encode(card, lite);
  };

  function ensureUrl(v) { return /^https?:\/\//i.test(v) ? v : "https://" + v; }
  CC.href = function (f) {
    var v = (f.value || "").trim();
    switch (f.type) {
      case "phone": return "tel:" + v.replace(/[^\d+]/g, "");
      case "email": return "mailto:" + v;
      case "whatsapp": return "https://wa.me/" + v.replace(/\D/g, "");
      case "instagram": return /^https?:/i.test(v) ? v : "https://instagram.com/" + v.replace(/^@/, "");
      case "twitter": return /^https?:/i.test(v) ? v : "https://x.com/" + v.replace(/^@/, "");
      case "linkedin": return /^https?:/i.test(v) ? v : "https://linkedin.com/" + v.replace(/^\//, "");
      case "youtube": return /^https?:/i.test(v) ? v : "https://youtube.com/" + v.replace(/^\//, "");
      case "tiktok": return /^https?:/i.test(v) ? v : "https://tiktok.com/@" + v.replace(/^@/, "");
      case "facebook": return /^https?:/i.test(v) ? v : "https://facebook.com/" + v.replace(/^\//, "");
      case "address": return "https://maps.google.com/?q=" + encodeURIComponent(v);
      default: return ensureUrl(v);
    }
  };

  CC.field = function (card, type) {
    var f = (card.fields || []).filter(function (x) { return x.type === type && x.value; })[0];
    return f ? f.value : "";
  };

  CC.vcard = function (card) {
    var L = ["BEGIN:VCARD", "VERSION:3.0"];
    L.push("FN:" + (card.name || ""));
    var parts = (card.name || "").trim().split(/\s+/);
    L.push("N:" + (parts.slice(1).join(" ") || "") + ";" + (parts[0] || "") + ";;;");
    if (card.company) L.push("ORG:" + card.company);
    if (card.title) L.push("TITLE:" + card.title);
    (card.fields || []).forEach(function (f) {
      if (!f.value) return;
      if (f.type === "phone") L.push("TEL;TYPE=CELL:" + f.value);
      else if (f.type === "whatsapp") L.push("TEL;TYPE=WHATSAPP:" + f.value);
      else if (f.type === "email") L.push("EMAIL;TYPE=INTERNET:" + f.value);
      else if (f.type === "address") L.push("ADR;TYPE=WORK:;;" + f.value + ";;;;");
      else L.push("URL:" + CC.href(f));
    });
    if (card.tagline) L.push("NOTE:" + card.tagline);
    L.push("REV:" + new Date().toISOString());
    L.push("END:VCARD");
    return L.join("\r\n");
  };

  /* Table-based HTML signature — mirrors app/signature.html buildSig(). */
  CC.signature = function (card) {
    var esc = CC.esc;
    var color = (CC.themeOf(card) || {}).solid || "#6366F1";
    var url = CC.shareUrl(card, true);
    var phone = CC.field(card, "phone"), email = CC.field(card, "email"), site = CC.field(card, "website");
    var photoCell = /^https?:/.test(card.photo || "")
      ? '<img src="' + esc(card.photo) + '" width="64" height="64" alt="" style="border-radius:12px;display:block;">'
      : '<div style="width:64px;height:64px;border-radius:12px;background:' + color + ';color:#ffffff;font-family:Arial,sans-serif;font-size:24px;font-weight:bold;text-align:center;line-height:64px;">' + esc(CC.initials(card.name)) + '</div>';
    var rows = [];
    if (phone) rows.push(esc(phone));
    if (email) rows.push('<a href="mailto:' + esc(email) + '" style="color:#475569;text-decoration:none;">' + esc(email) + '</a>');
    if (site) rows.push('<a href="' + (/^https?:/.test(site) ? esc(site) : "https://" + esc(site)) + '" style="color:#475569;text-decoration:none;">' + esc(site.replace(/^https?:\/\//, "")) + '</a>');
    return '' +
'<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#334155;">' +
  '<tr>' +
    '<td style="padding-right:16px;vertical-align:top;">' + photoCell + '</td>' +
    '<td style="border-left:3px solid ' + color + ';padding-left:16px;vertical-align:top;">' +
      '<div style="font-size:16px;font-weight:bold;color:#111827;">' + esc(card.name) + '</div>' +
      '<div style="color:#64748B;padding:2px 0 6px;">' + esc(card.title || "") + (card.title && card.company ? " · " : "") + esc(card.company || "") + '</div>' +
      (rows.length ? '<div style="line-height:1.6;">' + rows.join("<br>") + "</div>" : "") +
      '<div style="padding-top:8px;"><a href="' + esc(url) + '" style="color:' + color + ';font-weight:bold;text-decoration:none;">Save my contact →</a></div>' +
    '</td>' +
  '</tr>' +
'</table>';
  };

  global.CC = CC;
})(typeof self !== "undefined" ? self : this);
