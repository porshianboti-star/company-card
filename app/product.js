/* ============================================================
   CompanyCard — product engine (shared)
   Cards live in localStorage; sharing via an encoded link.
   Template system: divider shapes, icon styles, grid/row layout, light/dark.
   ============================================================ */
(function (global) {
  "use strict";
  var CC = {};

  /* ---------- Theme colours ---------- */
  CC.themes = {
    indigo: { grad: "linear-gradient(135deg,#6366F1,#8B5CF6,#A855F7)", solid: "#6366F1" },
    violet: { grad: "linear-gradient(135deg,#8B5CF6,#A855F7)", solid: "#8B5CF6" },
    teal:   { grad: "linear-gradient(135deg,#0EA5E9,#14B8A6)", solid: "#0EA5E9" },
    rose:   { grad: "linear-gradient(135deg,#F43F5E,#A855F7)", solid: "#F43F5E" },
    amber:  { grad: "linear-gradient(135deg,#F59E0B,#F43F5E)", solid: "#F59E0B" },
    green:  { grad: "linear-gradient(135deg,#22C55E,#16A34A)", solid: "#16A34A" },
    ink:    { grad: "linear-gradient(135deg,#334155,#0B0A1F)", solid: "#0B0A1F" }
  };
  CC.themeKeys = ["indigo", "violet", "teal", "rose", "amber", "green", "ink"];

  /* Extended palette for the "see more" gallery + custom picker */
  CC.palette = [
    "#6366F1", "#4F46E5", "#7C3AED", "#8B5CF6", "#A855F7", "#D946EF",
    "#EC4899", "#F43F5E", "#EF4444", "#F97316", "#F59E0B", "#EAB308",
    "#84CC16", "#22C55E", "#10B981", "#14B8A6", "#06B6D4", "#0EA5E9",
    "#3B82F6", "#2563EB", "#64748B", "#334155", "#0F172A", "#0B0A1F"
  ];
  /* lighten (amt>0) / darken (amt<0) a hex by amt in -1..1 — used to build a gradient from one colour */
  CC.shade = function (hex, amt) {
    var c = String(hex || "#6366F1").replace("#", "");
    if (c.length === 3) c = c[0] + c[0] + c[1] + c[1] + c[2] + c[2];
    var n = parseInt(c, 16); if (isNaN(n)) n = 0x6366F1;
    var r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255;
    var f = function (v) { return Math.max(0, Math.min(255, Math.round(v + (amt < 0 ? v * amt : (255 - v) * amt)))); };
    return "#" + [f(r), f(g), f(b)].map(function (v) { return ("0" + v.toString(16)).slice(-2); }).join("");
  };
  /* readable text colour (#fff or near-black) for a given background hex */
  CC.readableOn = function (hex) {
    var c = String(hex || "").replace("#", ""); if (c.length === 3) c = c[0] + c[0] + c[1] + c[1] + c[2] + c[2];
    var n = parseInt(c, 16); if (isNaN(n)) return "#fff";
    var r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255;
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255 > 0.62 ? "#0B0A1F" : "#fff";
  };

  /* Resolve a preset key OR a custom hex → { grad, solid } */
  CC._resolveColor = function (key, custom) {
    if (key === "custom" && custom) {
      var c = custom;
      return { grad: "linear-gradient(135deg," + CC.shade(c, .18) + "," + c + "," + CC.shade(c, -.24) + ")", solid: c };
    }
    return CC.themes[key] || CC.themes.indigo;
  };
  /* theme = the brand colour (name + icon accent) · bg = the card header background.
     Old cards have no `bg` → fall back to their theme so they look unchanged. */
  CC.themeOf = function (card) { return CC._resolveColor(card && card.theme, card && card.customColor); };
  CC.bgOf = function (card) { return CC._resolveColor((card && card.bg) || (card && card.theme) || "indigo", card && card.bgCustomColor); };

  CC.shapes = ["circle", "rounded", "square"];
  CC.shapeRadius = { circle: "50%", rounded: "26px", square: "16px" };

  /* ---------- Templates ----------
     divider: straight | wave | curve | slant | notch
     icons:   soft | round | outline
     links:   rows | grid
     avatar:  center | ring | left | banner
  */
  CC.templates = [
    { id: "minimal",  name: "Minimal",   dark: false, body: "#ffffff", divider: "straight", icons: "soft",    links: "rows", avatar: "center", accent: "theme", bg: "tpl-bg/minimal.jpg" },
    { id: "wave",     name: "Wave",      dark: false, body: "#ffffff", divider: "wave",     icons: "round",   links: "rows", avatar: "center", accent: "theme", bg: "tpl-bg/wave.jpg" },
    { id: "curve",    name: "Curve",     dark: false, body: "#ffffff", divider: "curve",    icons: "outline", links: "grid", avatar: "ring",   accent: "theme", bg: "tpl-bg/curve.jpg" },
    { id: "spotlight",name: "Spotlight", dark: false, body: "#ffffff", divider: "straight", icons: "round",   links: "grid", avatar: "ring",   accent: "theme", bg: "tpl-bg/spotlight.jpg" },
    { id: "corner",   name: "Corner",    dark: false, body: "#ffffff", divider: "slant",    icons: "round",   links: "grid", avatar: "left",   accent: "theme", bg: "tpl-bg/corner.jpg" },
    { id: "noir",     name: "Noir",      dark: true,  body: "#0b0a1f", divider: "straight", icons: "outline", links: "grid", avatar: "banner", accent: "#F5C542", bg: "tpl-bg/noir.jpg", logo: "tpl-bg/emblem-gold.png" },
    { id: "onyx",     name: "Onyx",      dark: true,  body: "#0e1117", divider: "slant",    icons: "round",   links: "grid", avatar: "banner", accent: "#84CC16", bg: "tpl-bg/onyx.jpg", logo: "tpl-bg/emblem-lime.png" }
  ];
  CC.tpl = function (id) { for (var i = 0; i < CC.templates.length; i++) if (CC.templates[i].id === id) return CC.templates[i]; return CC.templates[0]; };

  /* ---------- Icons ---------- */
  CC.ICONS = {
    phone:    { p: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/>' },
    email:    { p: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>' },
    website:  { p: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20Z"/>' },
    linkedin: { fill: true, p: '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14ZM8.3 18V10H5.7v8h2.6Zm-1.3-9.1a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM18.3 18v-4.4c0-2.4-1.3-3.5-3-3.5a2.6 2.6 0 0 0-2.3 1.3V10h-2.6v8h2.6v-4.2c0-1.1.2-2.2 1.6-2.2s1.4 1.3 1.4 2.3V18h2.3Z"/>' },
    instagram:{ p: '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>' },
    twitter:  { fill: true, p: '<path d="M18.9 2H22l-7.5 8.6L23 22h-6.8l-5.3-7-6.1 7H1.6l8-9.2L1 2h7l4.8 6.4L18.9 2Zm-1.2 18h1.9L7.4 4H5.4l12.3 16Z"/>' },
    whatsapp: { fill: true, p: '<path d="M12 2a10 10 0 0 0-8.7 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2Zm5.3 13.9c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1-.4-.1-.9-.3-1.6-.6-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 .9-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .5l-.4.6c-.1.2-.3.3-.1.6.1.3.6 1 1.3 1.6.9.8 1.6 1 1.9 1.2.2.1.4 0 .5-.1l.7-.8c.2-.2.4-.2.6-.1l1.7.8c.2.1.4.2.5.3.1.3.1.7-.1 1.3Z"/>' },
    calendar: { p: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>' },
    address:  { p: '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/>' },
    custom:   { p: '<circle cx="12" cy="12" r="9"/><path d="M8 12h8M12 8v8"/>' },
    youtube:  { p: '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3Z" fill="currentColor" stroke="none"/>' },
    facebook: { fill: true, p: '<path d="M14 9h3V5h-3a4 4 0 0 0-4 4v2H7v4h3v6h4v-6h3l1-4h-4V9a1 1 0 0 1 1-1Z"/>' },
    tiktok:   { fill: true, p: '<path d="M14 3c.3 2.3 1.7 3.9 4 4.2v3.1a7 7 0 0 1-4-1.3v5.6a5.6 5.6 0 1 1-5.6-5.6c.3 0 .6 0 .9.05v3.2a2.5 2.5 0 1 0 1.7 2.35V3H14Z"/>' },
    pinterest:{ fill: true, p: '<path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 .02-2.9l1.16-4.9s-.3-.6-.3-1.45c0-1.36.8-2.37 1.78-2.37.84 0 1.25.63 1.25 1.39 0 .85-.54 2.11-.82 3.28-.23.99.49 1.79 1.46 1.79 1.76 0 2.94-2.26 2.94-4.94 0-2.04-1.37-3.56-3.87-3.56a4.4 4.4 0 0 0-4.6 4.43c0 .88.26 1.5.67 1.98.19.22.21.31.14.57l-.2.8c-.07.26-.28.35-.52.25-1.06-.43-1.55-1.59-1.55-2.89 0-2.15 1.81-4.73 5.41-4.73 2.9 0 4.8 2.1 4.8 4.35 0 2.98-1.66 5.2-4.1 5.2-.82 0-1.6-.44-1.86-.95l-.5 2c-.18.69-.67 1.56-1 2.09A10 10 0 1 0 12 2Z"/>' },
    save:     { p: '<path d="M16 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="9.5" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/>' }
  };
  CC.icon = function (type) {
    var i = CC.ICONS[type] || CC.ICONS.custom;
    var attr = i.fill ? 'fill="currentColor"' : 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"';
    return '<svg viewBox="0 0 24 24" ' + attr + '>' + i.p + '</svg>';
  };

  /* ---------- Field types ---------- */
  CC.fieldTypes = {
    phone:    { label: "Phone", mode: "tel", ph: "+1 555 0100" },
    email:    { label: "Email", mode: "email", ph: "you@company.com" },
    website:  { label: "Website", mode: "url", ph: "company-card.com" },
    linkedin: { label: "LinkedIn", mode: "text", ph: "in/yourname" },
    instagram:{ label: "Instagram", mode: "text", ph: "@yourhandle" },
    twitter:  { label: "X / Twitter", mode: "text", ph: "@yourhandle" },
    whatsapp: { label: "WhatsApp", mode: "tel", ph: "+1 555 0100" },
    calendar: { label: "Book a call", mode: "url", ph: "calendly.com/you" },
    address:  { label: "Address", mode: "text", ph: "123 Main St, City" },
    youtube:  { label: "YouTube", mode: "url", ph: "youtube.com/@you" },
    facebook: { label: "Facebook", mode: "url", ph: "facebook.com/you" },
    tiktok:   { label: "TikTok", mode: "text", ph: "@you" },
    pinterest:{ label: "Pinterest", mode: "url", ph: "pinterest.com/you" },
    custom:   { label: "Custom link", mode: "url", ph: "link or text" }
  };
  CC.fieldTypeKeys = ["phone", "whatsapp", "email", "website", "linkedin", "instagram", "youtube", "twitter", "facebook", "tiktok", "pinterest", "calendar", "address", "custom"];
  CC.brandColors = {
    phone: "#22C55E", whatsapp: "#25D366", email: "#EA4335", website: "#0EA5E9",
    linkedin: "#0A66C2", instagram: "#E4405F", youtube: "#FF0000", twitter: "#1DA1F2",
    facebook: "#1877F2", tiktok: "#111111", pinterest: "#E60023", calendar: "#8B5CF6",
    address: "#EF4444", custom: "#64748B"
  };

  /* ---------- Icon design styles (user-pickable) ----------
     soft = tinted rounded square · solid = filled circle · outline = ring · plain = bare glyph.
     Values map to the ico-* CSS classes. Empty card.iconStyle → fall back to the template's. */
  CC.iconStyles = ["soft", "solid", "outline", "plain"];
  CC.iconStyleClass = { soft: "soft", solid: "round", outline: "outline", plain: "plain" };
  CC.iconStyleLabel = { soft: "Soft", solid: "Solid", outline: "Outline", plain: "Plain" };
  CC.tplToIconStyle = { soft: "soft", round: "solid", outline: "outline", plain: "plain" };

  /* ---------- Per-link display ----------
     "strip" = full row (icon + label + value) · "icon" = compact logo only.
     Sensible default per type: contact details as strips, socials as logos. */
  CC.defaultDisplay = {
    phone: "strip", whatsapp: "strip", email: "strip", website: "strip", address: "strip",
    calendar: "strip", custom: "strip",
    linkedin: "icon", instagram: "icon", twitter: "icon", facebook: "icon",
    youtube: "icon", tiktok: "icon", pinterest: "icon"
  };
  CC.fieldDisplay = function (f) {
    return (f && (f.display === "icon" || f.display === "strip")) ? f.display : (CC.defaultDisplay[f && f.type] || "strip");
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
      case "address": return "https://maps.google.com/?q=" + encodeURIComponent(v);
      default: return ensureUrl(v);
    }
  };

  /* ---------- Helpers ---------- */
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  CC.esc = esc;
  CC.initials = function (name) { return (name || "").trim().split(/\s+/).slice(0, 2).map(function (w) { return w[0] || ""; }).join("").toUpperCase() || "CC"; };
  CC.uid = function () { return "c" + Math.random().toString(36).slice(2, 9); };
  CC.blank = function () { return { id: CC.uid(), tpl: "minimal", name: "", title: "", company: "", tagline: "", theme: "indigo", customColor: "", photo: "", cover: "", bg: "", bgCustomColor: "", shape: "rounded", showQR: false, brandedQR: false, iconColor: "original", iconStyle: "", showSave: true, saveLabel: "", saveColor: "", fields: [] }; };

  /* ---------- Encode / decode (unicode + url-safe base64) ---------- */
  CC.encode = function (card, lite) {
    var c = JSON.parse(JSON.stringify(card));
    if (lite) { delete c.photo; delete c.cover; }
    var b = btoa(unescape(encodeURIComponent(JSON.stringify(c))));
    return b.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  };
  CC.decode = function (s) {
    try { s = s.replace(/-/g, "+").replace(/_/g, "/"); while (s.length % 4) s += "="; return JSON.parse(decodeURIComponent(escape(atob(s)))); }
    catch (e) { return null; }
  };
  CC.shareUrl = function (card, lite) { return location.href.replace(/[^/]*(\?.*)?$/, "") + "card.html#c=" + CC.encode(card, lite); };

  /* ---------- Storage ---------- */
  var KEY = "cc_cards_v1";
  CC.all = function () { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } };
  CC.get = function (id) { return CC.all().filter(function (c) { return c.id === id; })[0]; };
  CC.save = function (card) { var a = CC.all(), i = -1; a.forEach(function (c, k) { if (c.id === card.id) i = k; }); card.updated = Date.now(); if (i >= 0) a[i] = card; else a.unshift(card); localStorage.setItem(KEY, JSON.stringify(a)); };
  CC.remove = function (id) { localStorage.setItem(KEY, JSON.stringify(CC.all().filter(function (c) { return c.id !== id; }))); };

  /* ============================================================
     PLANS — free vs Pro. Account + upgrade live in localStorage.
     Build is always free; Pro features are gated at deploy (save/share).
     ============================================================ */
  CC.FREE_FIELD_LIMIT = 5;
  CC.FREE_CARD_LIMIT = 1;
  CC.PRICING = { currency: "$", monthly: 7.99, annual: 5.99, annualTotal: 71.88 }; /* annual = per-month, billed yearly */
  CC.PRO_FEATURES = {
    cover:       { label: "Cover image",        hint: "Add a branded banner photo." },
    iconStyle:   { label: "Premium icon styles", hint: "Solid, outline & plain icon designs." },
    brandColor:  { label: "Brand-colour icons",  hint: "Recolour every icon to your brand." },
    customColor: { label: "Custom colours",       hint: "Any hex colour + the full palette." },
    brandedQR:   { label: "Branded QR code",      hint: "Put your logo & colour in the QR." },
    fields:      { label: "Unlimited links",      hint: "More than " + 5 + " links on a card." },
    multiCard:   { label: "Multiple cards",       hint: "Create more than one card." }
  };

  /* Which Pro features a card uses right now (drives badges + the deploy paywall). */
  CC.cardProFeatures = function (card) {
    var used = [];
    if (!card) return used;
    if (card.cover) used.push("cover");
    if (card.iconStyle && card.iconStyle !== "soft") used.push("iconStyle");
    if (card.iconColor === "brand") used.push("brandColor");
    if (card.theme === "custom" || card.bg === "custom") used.push("customColor");
    if (card.brandedQR) used.push("brandedQR");
    var n = (card.fields || []).filter(function (f) { return (f.value || "").trim(); }).length;
    if (n > CC.FREE_FIELD_LIMIT) used.push("fields");
    return used;
  };
  CC.usesPro = function (card) { return CC.cardProFeatures(card).length > 0; };

  /* ---------- Account ---------- */
  var UKEY = "cc_user_v1";
  CC.user = function () { try { return JSON.parse(localStorage.getItem(UKEY)) || null; } catch (e) { return null; } };
  CC.saveUser = function (u) { localStorage.setItem(UKEY, JSON.stringify(u)); return u; };
  CC.isAuthed = function () { return !!CC.user(); };
  CC.isPro = function () { var u = CC.user(); return !!(u && u.pro); };
  CC.signup = function (email, name, via) {
    var u = CC.user() || {};
    u.email = email || u.email || ""; u.name = name || u.name || ""; u.via = via || u.via || "email";
    if (!u.since) u.since = Date.now(); if (typeof u.pro !== "boolean") u.pro = false;
    return CC.saveUser(u);
  };
  CC.setPro = function (plan) {
    var u = CC.user() || CC.signup("you@company-card.com");
    u.pro = true; u.plan = plan || "monthly"; u.proSince = Date.now();
    /* also record Pro on the account in the cloud, so it's queryable */
    try { if (window.CCAuth && CCAuth.setPlan) CCAuth.setPlan("pro"); } catch (e) {}
    return CC.saveUser(u);
  };
  CC.signOut = function () { localStorage.removeItem(UKEY); };

  /* ---------- Contacts (captured connections) ---------- */
  var CKEY = "cc_contacts_v1";
  CC.blankContact = function () { return { id: CC.uid(), name: "", title: "", company: "", email: "", phone: "", website: "", tags: [], note: "", source: "manual", met: Date.now() }; };
  CC.contacts = function () { try { return JSON.parse(localStorage.getItem(CKEY)) || []; } catch (e) { return []; } };
  CC.getContact = function (id) { return CC.contacts().filter(function (c) { return c.id === id; })[0]; };
  CC.saveContact = function (c) {
    var a = CC.contacts(), i = -1; if (!c.id) c.id = CC.uid(); if (!c.met) c.met = Date.now();
    a.forEach(function (x, k) { if (x.id === c.id) i = k; });
    if (i >= 0) a[i] = c; else a.unshift(c);
    localStorage.setItem(CKEY, JSON.stringify(a)); return c;
  };
  CC.removeContact = function (id) { localStorage.setItem(CKEY, JSON.stringify(CC.contacts().filter(function (c) { return c.id !== id; }))); };
  CC.contactVcard = function (c) {
    var L = ["BEGIN:VCARD", "VERSION:3.0", "FN:" + (c.name || "")];
    var p = (c.name || "").trim().split(/\s+/); L.push("N:" + (p.slice(1).join(" ") || "") + ";" + (p[0] || "") + ";;;");
    if (c.company) L.push("ORG:" + c.company); if (c.title) L.push("TITLE:" + c.title);
    if (c.phone) L.push("TEL;TYPE=CELL:" + c.phone); if (c.email) L.push("EMAIL;TYPE=INTERNET:" + c.email);
    if (c.website) L.push("URL:" + c.website); if (c.note) L.push("NOTE:" + c.note);
    L.push("REV:" + new Date().toISOString(), "END:VCARD"); return L.join("\r\n");
  };
  CC.downloadContact = function (c) {
    var blob = new Blob([CC.contactVcard(c)], { type: "text/vcard;charset=utf-8" });
    var url = URL.createObjectURL(blob), a = document.createElement("a");
    a.href = url; a.download = (c.name || "contact").replace(/\s+/g, "_") + ".vcf";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  };
  CC.seedContacts = function () {
    if (CC.contacts().length) return CC.contacts();
    var now = Date.now(), day = 864e5;
    var s = [
      { name: "Rachel Kim", title: "VP Sales", company: "Northwind", email: "rachel.kim@northwind.com", phone: "+1 555 0142", website: "", tags: ["Lead", "SaaS Expo"], note: "Met at SaaS Expo booth 14 — wants a pilot for 25 reps. Send pricing.", source: "scan", met: now - day },
      { name: "Diego Martín", title: "Account Executive", company: "Lumen", email: "diego@lumen.io", phone: "+1 555 0143", website: "", tags: ["Partner"], note: "Intro from Rachel. Follow up next week.", source: "qr", met: now - 3 * day },
      { name: "Amara Okafor", title: "Partnerships Lead", company: "Brightline", email: "amara@brightline.co", phone: "", website: "brightline.co", tags: ["Investor"], note: "", source: "scan", met: now - 8 * day },
      { name: "Tom Walsh", title: "Marketing Manager", company: "Cedar", email: "tom.walsh@cedar.com", phone: "+1 555 0145", website: "", tags: ["Lead"], note: "Asked for case studies.", source: "manual", met: now - 15 * day }
    ].map(function (c) { c.id = CC.uid(); return c; });
    localStorage.setItem(CKEY, JSON.stringify(s)); return s;
  };
  CC.ago = function (ts) {
    var s = Math.floor((Date.now() - ts) / 1000); if (s < 60) return "just now";
    var m = Math.floor(s / 60); if (m < 60) return m + "m ago";
    var h = Math.floor(m / 60); if (h < 24) return h + "h ago";
    var d = Math.floor(h / 24); if (d < 7) return d + "d ago";
    var w = Math.floor(d / 7); if (w < 5) return w + "w ago";
    return new Date(ts).toLocaleDateString();
  };

  /* ---------- vCard ---------- */
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
  CC.downloadVcard = function (card) {
    var blob = new Blob([CC.vcard(card)], { type: "text/vcard;charset=utf-8" });
    var url = URL.createObjectURL(blob), a = document.createElement("a");
    a.href = url; a.download = (card.name || "contact").replace(/\s+/g, "_") + ".vcf";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  };

  /* ---------- QR (qrcodejs from CDN). Returns false if it can't encode. ---------- */
  CC.qr = function (el, text, size, colorDark) {
    el.innerHTML = "";
    if (!global.QRCode) { el.innerHTML = '<div class="cc-qr-fallback">QR needs an internet connection</div>'; return false; }
    try { new global.QRCode(el, { text: text, width: size || 168, height: size || 168, colorDark: colorDark || "#0B0A1F", colorLight: "#ffffff", correctLevel: global.QRCode.CorrectLevel.M }); return true; }
    catch (e) { el.innerHTML = ""; return false; }
  };

  /* ---------- Divider shapes ---------- */
  CC.dividerSVG = function (kind) {
    var paths = {
      wave:  'M0,12 C20,24 34,2 50,11 C66,20 80,0 100,12 L100,22 L0,22 Z',
      curve: 'M0,22 C28,2 72,2 100,22 L100,22 L0,22 Z',
      slant: 'M0,22 L100,3 L100,22 Z'
    };
    if (!paths[kind]) return "";
    return '<svg class="cc-dsvg" viewBox="0 0 100 22" preserveAspectRatio="none"><path d="' + paths[kind] + '"/></svg>';
  };

  /* ---------- Card renderer ---------- */
  CC.renderCard = function (card) {
    var tpl = CC.tpl(card.tpl);
    var th = CC.themeOf(card);      /* brand colour → name + icon accent */
    var bg = CC.bgOf(card);         /* background colour → card header */
    var accent = tpl.accent === "theme" ? th.solid : tpl.accent;
    var icStyle = function (type) { return card.iconColor === "original" ? ' style="--ic:' + (CC.brandColors[type] || accent) + '"' : ""; };
    var fields = (card.fields || []).filter(function (f) { return (f.value || "").trim(); });
    var shapeR = CC.shapeRadius[card.shape] || CC.shapeRadius.rounded;
    /* header background priority: uploaded cover → chosen background colour → template image → fallback */
    var img = function (u) { return "background-image:url(" + u + ");background-size:cover;background-position:center"; };
    var coverStyle;
    if (card.cover) coverStyle = img(card.cover);
    else if (card.bg) coverStyle = "background:" + bg.grad;
    else if (tpl.bg) coverStyle = img(tpl.bg);
    else coverStyle = "background:" + (tpl.dark ? "linear-gradient(150deg,#2a2540,#0b0a1f)" : bg.grad);
    var avInner = card.photo ? '<img src="' + card.photo + '" alt="">' : '<span>' + CC.initials(card.name) + "</span>";
    var avStyle = "border-radius:" + shapeR + ";" + (card.photo ? "background:#fff" : "background:" + th.grad);
    var avatar = '<div class="cc-avatar" style="' + avStyle + '">' + avInner + "</div>";
    var divider = CC.dividerSVG(tpl.divider);
    divider = divider ? '<div class="cc-divider">' + divider + "</div>" : "";

    /* split links by their per-link display choice */
    var iconFields = fields.filter(function (f) { return CC.fieldDisplay(f) === "icon"; });
    var stripFields = fields.filter(function (f) { return CC.fieldDisplay(f) === "strip"; });

    /* logo group — labelled tiles on grid templates, compact actions otherwise */
    var iconBlock = "";
    if (iconFields.length) {
      if (tpl.links === "grid") {
        iconBlock = '<div class="cc-grid">' + iconFields.map(function (f) {
          return '<a class="cc-gi" href="' + CC.href(f) + '" target="_blank" rel="noopener">' +
            '<span class="cc-gi-ic"' + icStyle(f.type) + ">" + CC.icon(f.type) + "</span>" +
            '<span class="cc-gi-l">' + esc(f.label || CC.fieldTypes[f.type].label) + "</span></a>";
        }).join("") + "</div>";
      } else {
        iconBlock = '<div class="cc-actions">' + iconFields.map(function (f) {
          return '<a class="cc-act"' + icStyle(f.type) + ' href="' + CC.href(f) + '" target="_blank" rel="noopener" aria-label="' + esc(f.label || CC.fieldTypes[f.type].label) + '">' + CC.icon(f.type) + "</a>";
        }).join("") + "</div>";
      }
    }

    /* strip group — full rows with label + value */
    var stripBlock = stripFields.length ? '<div class="cc-fields">' + stripFields.map(function (f) {
      return '<a class="cc-row" href="' + CC.href(f) + '" target="_blank" rel="noopener">' +
        '<span class="cc-row-ic"' + icStyle(f.type) + ">" + CC.icon(f.type) + "</span>" +
        '<span class="cc-row-tx"><b>' + esc(f.label || CC.fieldTypes[f.type].label) + "</b><span>" + esc(f.value) + "</span></span>" +
        '<span class="cc-row-go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg></span></a>';
    }).join("") + "</div>" : "";

    var links = (iconBlock + stripBlock) || '<div class="cc-empty">Add links to see them here</div>';

    var qrBlock = card.showQR ? '<div class="cc-qrblock"><div class="cc-qrbox" data-qr></div><span class="cc-qrcap">Scan to connect</span></div>' : "";
    var titleLine = [card.title, card.company].filter(Boolean).map(esc).join(" · ") || "Title · Company";
    var saveOn = card.showSave !== false;
    var saveLabel = (card.saveLabel != null && String(card.saveLabel).trim() !== "") ? card.saveLabel : "Save contact";
    var saveStyle = card.saveColor ? ' style="background:' + card.saveColor + ';color:' + CC.readableOn(card.saveColor) + '"' : "";
    var saveBtn = saveOn ? '<button class="cc-save" type="button" data-save' + saveStyle + '>' + CC.icon("save") + " " + esc(saveLabel) + "</button>" : "";
    var ico = CC.iconStyleClass[card.iconStyle] || tpl.icons;
    var cls = "cc-card div-" + tpl.divider + " ico-" + ico + " lay-" + tpl.links + " av-" + tpl.avatar + (tpl.dark ? " is-dark" : "");
    var styleVars = "--cc-accent:" + accent + ";--cc-name:" + accent + ";--cc-body:" + tpl.body + ";";

    return '<div class="' + cls + '" style="' + styleVars + '">' +
        '<div class="cc-cover" style="' + coverStyle + '">' + (tpl.logo ? '<img class="cc-logo" src="' + tpl.logo + '" alt="">' : "") + (tpl.avatar === "banner" ? avatar : "") + "</div>" +
        divider +
        (tpl.avatar === "banner" ? "" : avatar) +
        '<div class="cc-id"><div class="cc-name">' + esc(card.name || "Your name") + "</div>" +
          '<div class="cc-title">' + titleLine + "</div>" +
          (card.tagline ? '<div class="cc-tag">' + esc(card.tagline) + "</div>" : "") +
        "</div>" +
        saveBtn +
        links + qrBlock +
      "</div>";
  };

  CC.fillQR = function (container, card) {
    if (!container || !card.showQR) return;
    var el = container.querySelector("[data-qr]");
    var col = card.brandedQR ? CC.themeOf(card).solid : "#0B0A1F";
    if (el) { if (!CC.qr(el, CC.shareUrl(card), 132, col)) CC.qr(el, CC.shareUrl(card, true), 132, col); }
  };

  /* ---------- Image cropper (drag + zoom in/out, square or wide) ---------- */
  CC.crop = function (file, opts, cb) {
    opts = opts || {};
    var aspect = opts.aspect || 1, outW = opts.out || 512, outH = Math.round(outW / aspect), bg = opts.bg || "#ffffff";
    var rd = new FileReader();
    rd.onload = function (e) { var img = new Image(); img.onload = function () { ui(img); }; img.src = e.target.result; };
    rd.readAsDataURL(file);

    function ui(img) {
      var VW = 320, VH = Math.round(VW / aspect);
      var modal = document.createElement("div");
      modal.className = "modal crop-modal";
      modal.innerHTML =
        '<div class="crop-box"><h3>' + (opts.title || "Crop image") + "</h3>" +
        '<div class="crop-stage" style="width:' + VW + "px;height:" + VH + 'px;background:' + bg + '">' +
          '<img class="crop-img" alt="" draggable="false"><div class="crop-ovl' + (opts.round ? " round" : "") + '"></div></div>' +
        '<div class="crop-zoom"><span>−</span><input type="range" min="0" max="100" value="0" class="crop-range" aria-label="Zoom"><span>+</span></div>' +
        '<div class="crop-actions"><button class="btn btn-ghost btn-block" data-cc type="button">Cancel</button><button class="btn btn-primary btn-block" data-ca type="button">Apply</button></div></div>';
      document.body.appendChild(modal);
      var stage = modal.querySelector(".crop-stage"), imgEl = modal.querySelector(".crop-img"), range = modal.querySelector(".crop-range");
      var fit = Math.min(VW / img.width, VH / img.height);   // whole image visible
      var cover = Math.max(VW / img.width, VH / img.height); // fills viewport
      var minS = fit, maxS = cover * 3.2;
      var scale = cover, tx = 0, ty = 0;
      function center() { tx = (VW - img.width * scale) / 2; ty = (VH - img.height * scale) / 2; }
      function clamp() {
        var w = img.width * scale, h = img.height * scale;
        tx = w <= VW ? (VW - w) / 2 : Math.min(0, Math.max(VW - w, tx));
        ty = h <= VH ? (VH - h) / 2 : Math.min(0, Math.max(VH - h, ty));
      }
      function draw() { imgEl.style.width = (img.width * scale) + "px"; imgEl.style.transform = "translate(" + tx + "px," + ty + "px)"; }
      center(); range.value = Math.round((scale - minS) / (maxS - minS) * 100); imgEl.src = img.src; draw();
      range.addEventListener("input", function () {
        var cx = VW / 2, cy = VH / 2, ox = (cx - tx) / scale, oy = (cy - ty) / scale;
        scale = minS + (parseFloat(range.value) / 100) * (maxS - minS);
        tx = cx - ox * scale; ty = cy - oy * scale; clamp(); draw();
      });
      var dragging = false, lx = 0, ly = 0;
      function pt(e) { var t = e.touches ? e.touches[0] : e; return { x: t.clientX, y: t.clientY }; }
      function down(e) { dragging = true; var p = pt(e); lx = p.x; ly = p.y; }
      function move(e) { if (!dragging) return; var p = pt(e); tx += p.x - lx; ty += p.y - ly; lx = p.x; ly = p.y; clamp(); draw(); if (e.cancelable) e.preventDefault(); }
      function up() { dragging = false; }
      stage.addEventListener("mousedown", down); window.addEventListener("mousemove", move); window.addEventListener("mouseup", up);
      stage.addEventListener("touchstart", down, { passive: true }); stage.addEventListener("touchmove", move, { passive: false }); stage.addEventListener("touchend", up);
      function close() { window.removeEventListener("mousemove", move); window.removeEventListener("mouseup", up); modal.remove(); }
      modal.querySelector("[data-cc]").addEventListener("click", close);
      modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
      modal.querySelector("[data-ca]").addEventListener("click", function () {
        var c = document.createElement("canvas"); c.width = outW; c.height = outH;
        var ctx = c.getContext("2d"); ctx.fillStyle = bg; ctx.fillRect(0, 0, outW, outH);
        ctx.drawImage(img, -tx / scale, -ty / scale, VW / scale, VH / scale, 0, 0, outW, outH);
        var url = c.toDataURL("image/jpeg", 0.85); close(); cb(url);
      });
    }
  };

  /* ============================================================
     TEAM ROLLOUT — company model, CSV import, directory connect, provisioning
     ============================================================ */
  var TKEY = "cc_team_v1";
  CC.blankTeam = function () {
    return { company: { name: "", domain: "", color: "indigo", template: "minimal", logo: "", lockBrand: true },
             members: [], source: "", connected: null, updated: 0 };
  };
  CC.team = function () { try { return JSON.parse(localStorage.getItem(TKEY)) || CC.blankTeam(); } catch (e) { return CC.blankTeam(); } };
  CC.saveTeam = function (t) { t.updated = Date.now(); localStorage.setItem(TKEY, JSON.stringify(t)); return t; };
  CC.resetTeam = function () { localStorage.removeItem(TKEY); };

  /* RFC-4180-ish CSV parser (quotes, commas, newlines) */
  CC.parseCSV = function (text) {
    var rows = [], row = [], cur = "", q = false, i, c;
    text = String(text).replace(/\r\n/g, "\n").replace(/\r/g, "\n");
    for (i = 0; i < text.length; i++) {
      c = text[i];
      if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
      else { if (c === '"') q = true; else if (c === ",") { row.push(cur); cur = ""; } else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; } else cur += c; }
    }
    if (cur.length || row.length) { row.push(cur); rows.push(row); }
    return rows.filter(function (r) { return r.some(function (x) { return (x || "").trim(); }); });
  };

  /* Guess column indexes from a header row */
  CC.guessMap = function (headers) {
    var H = headers.map(function (h) { return (h || "").toLowerCase().trim(); });
    var find = function (keys) { for (var k = 0; k < keys.length; k++) { for (var j = 0; j < H.length; j++) { if (H[j].indexOf(keys[k]) >= 0) return j; } } return -1; };
    return { name: find(["full name", "name", "employee"]), title: find(["title", "role", "position", "job"]),
             email: find(["email", "mail", "e-mail"]), phone: find(["phone", "mobile", "tel", "cell"]), dept: find(["department", "dept", "team", "division"]) };
  };
  CC.rowsToMembers = function (rows, map, hasHeader) {
    var out = [], start = hasHeader ? 1 : 0, g = function (r, idx) { return idx >= 0 && r[idx] != null ? String(r[idx]).trim() : ""; };
    for (var i = start; i < rows.length; i++) {
      var r = rows[i], name = g(r, map.name);
      if (!name) continue;
      out.push({ id: CC.uid(), name: name, title: g(r, map.title), email: g(r, map.email), phone: g(r, map.phone), dept: g(r, map.dept), pick: true });
    }
    return out;
  };
  CC.sampleCSV = function () {
    return "Full Name,Job Title,Email,Phone,Department\n" +
      "Rachel Kim,VP Sales,rachel.kim@northwind.com,+1 555 0142,Sales\n" +
      "Diego Martin,Account Executive,diego.martin@northwind.com,+1 555 0143,Sales\n" +
      "Amara Okafor,Partnerships Lead,amara.okafor@northwind.com,+1 555 0144,Partnerships\n" +
      "Marcus Bell,Solutions Engineer,marcus.bell@northwind.com,+1 555 0145,Engineering\n" +
      "Sofia Costa,Customer Success,sofia.costa@northwind.com,+1 555 0146,Success\n";
  };

  /* Simulated Google Workspace / Microsoft 365 directory */
  CC.sampleDirectory = function (provider, domain) {
    domain = domain || "northwind.com";
    var base = [
      ["Rachel Kim", "VP Sales", "rachel.kim", "Sales"],
      ["Diego Martín", "Account Executive", "diego.martin", "Sales"],
      ["Amara Okafor", "Partnerships Lead", "amara.okafor", "Partnerships"],
      ["Marcus Bell", "Solutions Engineer", "marcus.bell", "Engineering"],
      ["Sofia Costa", "Customer Success", "sofia.costa", "Success"],
      ["Tom Walsh", "Marketing Manager", "tom.walsh", "Marketing"],
      ["Priya Nair", "Talent Partner", "priya.nair", "People"],
      ["Liam O'Brien", "Finance Analyst", "liam.obrien", "Finance"],
      ["Hana Suzuki", "Product Designer", "hana.suzuki", "Product"],
      ["Noah Cohen", "Sales Development", "noah.cohen", "Sales"],
      ["Élodie Laurent", "Office Manager", "elodie.laurent", "Operations"],
      ["Sam Carter", "IT Administrator", "sam.carter", "IT"]
    ];
    return base.map(function (r, i) { return { id: "d" + i, name: r[0], title: r[1], email: r[2] + "@" + domain, phone: "", dept: r[3], pick: true }; });
  };

  /* Build a card for a member by merging the company brand template with the
     member's own data. company-scoped items apply to everyone; employee-scoped
     items come from the member. cover/photo: { scope:'company'|'employee', value }. */
  CC.memberCard = function (member, company) {
    company = company || {}; member = member || {};
    var c = CC.blank();
    c.name = member.name || ""; c.title = member.title || ""; c.company = company.name || "Company";
    c.theme = company.color || "indigo";
    if (company.customColor) c.customColor = company.customColor;
    if (company.bg) c.bg = company.bg;
    if (company.bgCustomColor) c.bgCustomColor = company.bgCustomColor;
    c.tpl = company.template || "minimal";
    if (company.shape) c.shape = company.shape;
    if (company.iconColor) c.iconColor = company.iconColor;
    if (company.iconStyle) c.iconStyle = company.iconStyle;
    if (company.showQR) c.showQR = true;
    if (company.saveLabel) c.saveLabel = company.saveLabel;
    if (company.saveColor) c.saveColor = company.saveColor;
    if (company.showSave === false) c.showSave = false;
    var cs = company.cover && company.cover.scope, ps = company.photo && company.photo.scope;
    c.cover = cs === "company" ? (company.cover.value || "") : (member.cover || "");
    c.photo = ps === "company" ? (company.photo.value || "") : (member.photo || "");
    c.fields = [];
    var links = company.links || [];
    if (!links.length) {
      /* legacy fallback: email/phone basics + company.socials */
      if (member.email) c.fields.push({ id: CC.uid(), type: "email", value: member.email });
      if (member.phone) c.fields.push({ id: CC.uid(), type: "phone", value: member.phone });
      (member.links || []).forEach(function (l) { if (l && l.value && String(l.value).trim()) c.fields.push({ id: CC.uid(), type: l.type, value: l.value }); });
      (company.socials || []).forEach(function (s) { if (s && s.value && String(s.value).trim()) c.fields.push({ id: CC.uid(), type: s.type, value: s.value }); });
      return c;
    }
    /* links-driven: every row in the designer, in order. company → fixed value;
       employee → email/phone from the member basics, other types from member.links. */
    links.forEach(function (l) {
      var v = "";
      if (l.scope === "company") v = l.value || "";
      else if (l.type === "email") v = member.email || "";
      else if (l.type === "phone") v = member.phone || "";
      else { var ml = (member.links || []).filter(function (x) { return x.type === l.type; })[0]; v = ml ? ml.value : ""; }
      if (v && String(v).trim()) c.fields.push({ id: CC.uid(), type: l.type || "custom", value: v, display: l.display });
    });
    return c;
  };
  /* Provision picked members into the team with a status + brand-locked card */
  CC.provision = function (team, members, status) {
    status = status || "invited";
    members.forEach(function (m) {
      team.members.push({ id: m.id || CC.uid(), name: m.name, title: m.title || "", email: m.email || "",
        phone: m.phone || "", dept: m.dept || "", links: m.links || [], photo: m.photo || "", cover: m.cover || "",
        status: status, added: Date.now(), card: CC.memberCard(m, team.company) });
    });
    return CC.saveTeam(team);
  };
  /* Re-build + save a single member's card after they personalise it */
  CC.refreshMember = function (team, member) {
    member.card = CC.memberCard(member, team.company);
    for (var i = 0; i < team.members.length; i++) { if (team.members[i].id === member.id) { team.members[i] = member; break; } }
    return CC.saveTeam(team);
  };

  /* ============================================================
     CONNECTOR API — real backend when app/config.js sets apiBase,
     otherwise the built-in simulation (sampleDirectory).
     ============================================================ */
  CC.config = global.CC_CONFIG || { apiBase: "", providers: { google: true, microsoft: true, csv: true } };
  CC.googleClientId = function () { return (CC.config.googleClientId || "").trim(); };
  CC.msClientId = function () { return (CC.config.msClientId || "").trim(); };
  CC.canConnect = function (p) { return p === "google" ? !!CC.googleClientId() : p === "microsoft" ? !!CC.msClientId() : true; };

  /* load an external script once, resolve when ready */
  CC._scripts = {};
  CC.loadScript = function (src) {
    if (CC._scripts[src]) return CC._scripts[src];
    CC._scripts[src] = new Promise(function (res, rej) {
      var s = document.createElement("script"); s.src = src; s.async = true;
      s.onload = function () { res(); }; s.onerror = function () { rej(new Error("Could not load " + src)); };
      document.head.appendChild(s);
    });
    return CC._scripts[src];
  };

  /* ---- REAL Google Workspace directory (client-side OAuth, no secret) ---- */
  CC.googleDirectory = function () {
    var cid = CC.googleClientId();
    if (!cid) return Promise.reject(new Error("SETUP_NEEDED"));
    return CC.loadScript("https://accounts.google.com/gsi/client").then(function () {
      return new Promise(function (resolve, reject) {
        var client = google.accounts.oauth2.initTokenClient({
          client_id: cid,
          scope: "https://www.googleapis.com/auth/admin.directory.user.readonly",
          callback: function (resp) {
            if (resp.error || !resp.access_token) { reject(new Error("Google sign-in was cancelled or denied.")); return; }
            var out = [], page = "";
            function grab() {
              var url = "https://admin.googleapis.com/admin/directory/v1/users?customer=my_customer&maxResults=200&orderBy=email" + (page ? "&pageToken=" + page : "");
              fetch(url, { headers: { Authorization: "Bearer " + resp.access_token } })
                .then(function (r) { if (r.status === 403) throw new Error("This Google account isn't a Workspace admin, or the Directory API isn't enabled."); if (!r.ok) throw new Error("Google Directory error " + r.status); return r.json(); })
                .then(function (d) {
                  (d.users || []).forEach(function (u, i) {
                    var org = (u.organizations && u.organizations[0]) || {};
                    out.push({ id: u.id || ("g" + out.length), name: (u.name && u.name.fullName) || u.primaryEmail,
                      title: org.title || "", email: u.primaryEmail || "", phone: (u.phones && u.phones[0] && u.phones[0].value) || "",
                      dept: org.department || "", pick: true });
                  });
                  if (d.nextPageToken) { page = d.nextPageToken; grab(); } else resolve(out);
                }).catch(reject);
            }
            grab();
          }
        });
        client.requestAccessToken();
      });
    });
  };

  /* ---- REAL Microsoft 365 / Entra directory (MSAL, public client, no secret) ---- */
  CC.microsoftDirectory = function () {
    var cid = CC.msClientId();
    if (!cid) return Promise.reject(new Error("SETUP_NEEDED"));
    var scopes = ["User.Read.All", "Directory.Read.All"];
    return CC.loadScript("https://alcdn.msauth.net/browser/2.38.3/js/msal-browser.min.js").then(function () {
      var pca = new msal.PublicClientApplication({ auth: { clientId: cid, authority: "https://login.microsoftonline.com/organizations", redirectUri: location.origin + location.pathname } });
      var init = pca.initialize ? pca.initialize() : Promise.resolve();
      return init.then(function () { return pca.loginPopup({ scopes: scopes }); }).then(function (login) {
        return pca.acquireTokenSilent({ account: login.account, scopes: scopes })
          .catch(function () { return pca.acquireTokenPopup({ scopes: scopes }); })
          .then(function (r) { return r.accessToken; });
      }).then(function (tok) {
        var out = [];
        function grab(url) {
          return fetch(url, { headers: { Authorization: "Bearer " + tok } })
            .then(function (r) { if (r.status === 403) throw new Error("This account lacks directory permission, or admin consent wasn't granted."); if (!r.ok) throw new Error("Microsoft Graph error " + r.status); return r.json(); })
            .then(function (d) {
              (d.value || []).forEach(function (u) {
                out.push({ id: u.id || ("m" + out.length), name: u.displayName || u.userPrincipalName,
                  title: u.jobTitle || "", email: u.mail || u.userPrincipalName || "", phone: u.mobilePhone || "",
                  dept: u.department || "", pick: true });
              });
              if (d["@odata.nextLink"]) return grab(d["@odata.nextLink"]);
              return out;
            });
        }
        return grab("https://graph.microsoft.com/v1.0/users?$select=displayName,jobTitle,mail,userPrincipalName,department,mobilePhone&$top=200");
      });
    });
  };
  CC.apiBase = function () { return (CC.config.apiBase || "").replace(/\/+$/, ""); };

  /* Open the provider's OAuth popup; resolves when it reports back (or closes). */
  CC.startAuth = function (provider) {
    var base = CC.apiBase();
    if (!base) return Promise.resolve(false);
    return new Promise(function (resolve, reject) {
      var w = window.open(base + "/auth/" + provider, "cc-auth", "width=520,height=660");
      if (!w) { reject(new Error("Popup blocked — allow popups and retry")); return; }
      function cleanup() { window.removeEventListener("message", onMsg); clearInterval(iv); }
      function onMsg(e) { if (e.data && e.data.type === "cc-auth" && e.data.provider === provider) { cleanup(); resolve(true); } }
      window.addEventListener("message", onMsg);
      var iv = setInterval(function () { if (w.closed) { cleanup(); resolve(true); } }, 700);
    });
  };

  /* Fetch the directory — REAL provider APIs via client-side OAuth (no fake data). */
  CC.fetchDirectory = function (provider, domain) {
    if (provider === "google") return CC.googleDirectory();
    if (provider === "microsoft") return CC.microsoftDirectory();
    var base = CC.apiBase();
    if (base) return fetch(base + "/api/directory?provider=" + encodeURIComponent(provider), { credentials: "include" })
      .then(function (r) { if (!r.ok) throw new Error("Directory " + r.status); return r.json(); })
      .then(function (d) { return (d.users || []).map(function (u, i) { return { id: u.id || ("d" + i), name: u.name, title: u.title || "", email: u.email || "", phone: u.phone || "", dept: u.dept || "", pick: true }; }); });
    return Promise.reject(new Error("Unsupported provider"));
  };

  /* Persist provisioning server-side when a backend is configured (no-op otherwise). */
  CC.provisionRemote = function (company, members, status) {
    var base = CC.apiBase();
    if (!base) return Promise.resolve({ ok: true, local: true });
    return fetch(base + "/api/provision", {
      method: "POST", credentials: "include", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ company: company, members: members, status: status })
    }).then(function (r) { return r.json(); }).catch(function () { return { ok: false }; });
  };

  global.CC = CC;
})(window);
