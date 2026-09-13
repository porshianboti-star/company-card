/* CompanyCard mini-builder (round 69, 2026-09-13).
   Two pages were titled "Free Maker" / "Free Generator" and contained no maker
   (0 inputs, 0 QR). This drops a working one in: six fields, a live card
   preview, a scannable vCard QR, .vcf + PNG download, and a handoff into the
   full builder with the fields pre-filled. No signup, nothing stored.

   Rules carried over from the product code:
   - vCard values are escaped per RFC 2426 (D-073): backslash, newlines, ';' and ','
     — otherwise a two-line tagline or a "Robert \"Bob\" Chen" truncates the file.
   - Everything typed goes into the DOM through textContent, never innerHTML.
   - QR capacity (D-085): the vCard is kept short and we warn instead of
     rendering an unscannable 177-module square. */
(function () {
  var root = document.getElementById('cc-mini'); if (!root) return;
  var qrLib = window.QRCode;

  function vesc(v) {
    return String(v == null ? '' : v).replace(/\\/g, '\\\\').replace(/\r\n|\r|\n/g, '\\n').replace(/;/g, '\\;').replace(/,/g, '\\,');
  }
  function vcard(c) {
    var L = ['BEGIN:VCARD', 'VERSION:3.0', 'FN:' + vesc(c.name)];
    var p = (c.name || '').trim().split(/\s+/);
    L.push('N:' + vesc(p.slice(1).join(' ')) + ';' + vesc(p[0] || '') + ';;;');
    if (c.company) L.push('ORG:' + vesc(c.company));
    if (c.title) L.push('TITLE:' + vesc(c.title));
    if (c.phone) L.push('TEL;TYPE=CELL:' + vesc(c.phone));
    if (c.email) L.push('EMAIL;TYPE=INTERNET:' + vesc(c.email));
    if (c.website) L.push('URL:' + vesc(normUrl(c.website)));
    L.push('END:VCARD');
    return L.join('\r\n');
  }
  function normUrl(u) { u = (u || '').trim(); if (!u) return ''; return /^https?:\/\//i.test(u) ? u : 'https://' + u; }
  function initials(name) { var p = (name || '').trim().split(/\s+/).filter(Boolean); return ((p[0] || '')[0] || '') + ((p[1] || '')[0] || ''); }

  var F = ['name', 'title', 'company', 'phone', 'email', 'website'];
  var LABEL = { name: 'Full name', title: 'Job title', company: 'Company', phone: 'Phone', email: 'Email', website: 'Website' };
  var PH = { name: 'Jordan Diaz', title: 'Head of Sales', company: 'Northwind Studio', phone: '+1 555 0100', email: 'jordan@northwind.studio', website: 'northwind.studio' };
  var AC = { name: 'name', title: 'organization-title', company: 'organization', phone: 'tel', email: 'email', website: 'url' };

  root.innerHTML =
    '<div class="ccm-grid">' +
      '<form class="ccm-form" autocomplete="on" novalidate>' +
        F.map(function (k) {
          return '<label class="ccm-f"><span>' + LABEL[k] + '</span><input id="ccm-' + k + '" name="' + k + '" type="' +
            (k === 'email' ? 'email' : k === 'phone' ? 'tel' : k === 'website' ? 'url' : 'text') +
            '" placeholder="' + PH[k] + '" autocomplete="' + AC[k] + '"' + (k === 'name' ? ' required' : '') + '></label>';
        }).join('') +
        '<p class="ccm-note">Nothing is uploaded or saved until you choose to continue. The QR carries the card itself, so it works even before you sign up.</p>' +
      '</form>' +
      '<div class="ccm-out">' +
        '<div class="ccm-card" aria-live="polite">' +
          '<div class="ccm-top"><div class="ccm-avatar" id="ccm-av">JD</div><div><div class="ccm-name" id="ccm-pname">Jordan Diaz</div><div class="ccm-role" id="ccm-prole">Head of Sales · Northwind Studio</div></div></div>' +
          '<ul class="ccm-rows"><li id="ccm-pphone">+1 555 0100</li><li id="ccm-pemail">jordan@northwind.studio</li><li id="ccm-pweb">northwind.studio</li></ul>' +
          '<div class="ccm-qrwrap"><div id="ccm-qr" class="ccm-qr" role="img" aria-label="QR code of this business card"></div><div class="ccm-scan">Scan to save this contact</div></div>' +
        '</div>' +
        '<div class="ccm-actions">' +
          '<button type="button" class="btn btn-primary" id="ccm-continue">Save it as a real card — free</button>' +
          '<button type="button" class="btn btn-ghost" id="ccm-png">Download QR (PNG)</button>' +
          '<button type="button" class="btn btn-ghost" id="ccm-vcf">Download .vcf</button>' +
        '</div>' +
        '<p class="ccm-note" id="ccm-msg"></p>' +
      '</div>' +
    '</div>';

  var $ = function (id) { return document.getElementById(id); };
  var qr = null, used = false, t;
  function vals() { var o = {}; F.forEach(function (k) { o[k] = ($('ccm-' + k).value || '').trim(); }); return o; }
  function shown(c) { var o = {}; F.forEach(function (k) { o[k] = c[k] || PH[k]; }); return o; }

  function render() {
    var c = vals(), s = shown(c);
    $('ccm-av').textContent = initials(s.name).toUpperCase() || 'JD';
    $('ccm-pname').textContent = s.name;
    $('ccm-prole').textContent = [s.title, s.company].filter(Boolean).join(' · ');
    $('ccm-pphone').textContent = s.phone; $('ccm-pemail').textContent = s.email; $('ccm-pweb').textContent = s.website;
    var text = vcard(s), box = $('ccm-qr'), msg = $('ccm-msg');
    if (!qrLib) { msg.textContent = 'The QR library did not load — the card preview still works, and the .vcf download too.'; return; }
    if (text.length > 900) { box.textContent = ''; msg.textContent = 'That is too much text for a scannable QR — shorten a field or two.'; return; }
    msg.textContent = '';
    if (!qr) { box.textContent = ''; qr = new qrLib(box, { text: text, width: 148, height: 148, correctLevel: qrLib.CorrectLevel.M }); }
    else qr.makeCode(text);
    if (!used && F.some(function (k) { return c[k]; })) { used = true; track('mini_builder_used'); }
  }
  function track(name, extra) { try { if (typeof gtag === 'function') gtag('event', name, Object.assign({ page_path: location.pathname }, extra || {})); } catch (e) {} }
  function download(blob, filename) {
    var url = URL.createObjectURL(blob), a = document.createElement('a');
    a.href = url; a.download = filename; document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  }
  function safeName(c) { return ((c.name || 'card').trim() || 'card').replace(/[^\w.-]+/g, '_').slice(0, 60); }

  F.forEach(function (k) { $('ccm-' + k).addEventListener('input', function () { clearTimeout(t); t = setTimeout(render, 120); }); });
  $('ccm-vcf').addEventListener('click', function () {
    var c = shown(vals()); download(new Blob([vcard(c)], { type: 'text/vcard;charset=utf-8' }), safeName(c) + '.vcf'); track('mini_builder_download', { kind: 'vcf' });
  });
  $('ccm-png').addEventListener('click', function () {
    var cv = $('ccm-qr').querySelector('canvas'), img = $('ccm-qr').querySelector('img');
    if (cv) { cv.toBlob(function (b) { if (b) download(b, safeName(shown(vals())) + '-qr.png'); }); }
    else if (img && img.src) { var a = document.createElement('a'); a.href = img.src; a.download = safeName(shown(vals())) + '-qr.png'; document.body.appendChild(a); a.click(); document.body.removeChild(a); }
    else { $('ccm-msg').textContent = 'Type at least a name first.'; return; }
    track('mini_builder_download', { kind: 'png' });
  });
  $('ccm-continue').addEventListener('click', function () {
    var c = vals(); track('mini_builder_continue');
    var q = new URLSearchParams(); F.forEach(function (k) { if (c[k]) q.set(k, c[k]); });
    location.href = 'app/builder.html' + (q.toString() ? '?prefill=1&' + q.toString() : '');
  });
  render();
})();
