#!/usr/bin/env python3
"""Improve vcard-qr-code.html for the "vCard format" queries (2026-11-14, rank plan
CC-5 as modified by the verifiers). Idempotent; every anchor is asserted.

Why: GSC (90 days to 2026-11-10) — "qr code vcard format" 35 impressions @ 33.1 (29 of
them US; 28d 29 @ 30.5), "vcard qr code format" 3 @ 39.3, "vcard format" 4 @ 75,
"vcard 3.0 format" 1 @ 38; all land on this page (90 impressions @ 31.3, 0 clicks).
The page explains the payload, but the word "format" is in neither the title nor a
heading, and it shows no example payload — the thing the plain-text "how to format a
vCard QR code" answers on that results page lead with. Expect a position change at
most, not clicks; the volume is tiny.

What:
  1. <title>, og:title, twitter:title, WebPage name -> "vCard QR Code Format: What's
     Encoded Inside | CompanyCard" (57 characters). H1 unchanged. The WebPage JSON-LD
     name gets a plain apostrophe; the three head tags keep the HTML-escaped one.
  2. description = og:description = twitter:description (152 characters).
  3. H2 "The anatomy of the payload" -> "The vCard QR code format, line by line".
  4. Under that H2, one example payload in a <pre>, labelled "Example (fictional
     details)": VERSION:3.0 with N then FN, a 555-01xx number (+1-202-555-0100) and
     example.com addresses. It states no rule beyond what the page already cites from
     RFC 2426 / RFC 6350.
  5. seo/pages_data12.py: same title, description and H2, plus a note that the
     example block lives in this script.
  6. dateModified + sitemap lastmod -> 2026-11-14 for this URL only. The "Sources,
     verified August 2026" line is NOT restamped (the RFC links were not re-opened).
     Does NOT run add_freshness.py.

Run from repo root: python3 seo/improve_vcard_format_2026_11_14.py
then python3 seo/build_llms_full.py.
"""
import py_compile
import re

DATE = "2026-11-14"
F = "vcard-qr-code.html"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "vCard QR Code: What&#x27;s Encoded Inside | CompanyCard"
NEW_T = "vCard QR Code Format: What&#x27;s Encoded Inside | CompanyCard"
NEW_PLAIN = NEW_T.replace("&#x27;", "'")
assert len(NEW_PLAIN) == 57
# <title>, og:title and twitter:title carry the HTML-escaped apostrophe. The WebPage JSON-LD name
# takes a plain one (repair 2026-11-14): JSON consumers do not HTML-unescape, so a "&#x27;" there is
# shown literally — it had been, under the old title too.
for old_name in ('"name":"' + OLD_T + '"', '"name":"' + NEW_T + '"'):
    if old_name in s:
        assert s.count(old_name) == 1, f"WebPage name occurrences: {s.count(old_name)}"
        s = s.replace(old_name, '"name":"' + NEW_PLAIN + '"')
        changed.append("jsonld-name")
if OLD_T in s:
    assert s.count(OLD_T) == 3, f"title occurrences: {s.count(OLD_T)}"  # title, og:title, twitter:title
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x3")
assert s.count(NEW_T) == 3, s.count(NEW_T)
assert s.count('"name":"' + NEW_PLAIN + '"') == 1

DESC = ("What a vCard QR code contains, line by line: the vCard format (3.0 or 4.0), why extra "
        "fields make the code harder to scan, and when a link works better.")
assert len(DESC) == 152, len(DESC)
# The value each tag held on 2026-11-13 (HEAD d2e37c7). Anything else means another edit (the
# every-2-days GEO loop, say) touched it since: stop rather than overwrite it unseen.
OLD_DESC = ("What a vCard QR code actually encodes: the .vcf payload, why extra fields make the code denser "
            "and harder to scan, and when a link works better.")
for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    m = re.search(r'<meta ' + re.escape(attr) + r' content="([^"]*)">', s)
    assert m and s.count(m.group(0)) == 1, f"{attr} not found/unique"
    assert m.group(1) in (OLD_DESC, DESC), f"{attr} changed since 2026-11-13: {m.group(1)[:80]!r}"
    if m.group(1) != DESC:
        s = s.replace(m.group(0), f'<meta {attr} content="{DESC}">', 1)
        changed.append(attr)

OLD_H2 = "<h2>The anatomy of the payload</h2>"
NEW_H2 = "<h2>The vCard QR code format, line by line</h2>"
if NEW_H2 not in s:
    assert s.count(OLD_H2) == 1, "H2 not unique"
    s = s.replace(OLD_H2, NEW_H2, 1)
    changed.append("h2")

MARK = "<!-- VCARD-EXAMPLE-2026-11 -->"
PAYLOAD = "\n".join([
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:Okafor;Sam;;;",
    "FN:Sam Okafor",
    "ORG:Okafor Bookkeeping LLC",
    "TITLE:Owner",
    "TEL;TYPE=CELL:+1-202-555-0100",
    "EMAIL:sam@example.com",
    "URL:https://example.com",
    "END:VCARD",
])
EXAMPLE = (
    MARK + '<div style="max-width:640px;margin:0 auto 28px;">'
    '<p style="margin:0 0 8px;font-weight:600;">Example (fictional details)</p>'
    '<pre style="margin:0;padding:16px 18px;background:#fff;border:1px solid var(--slate-200,#e5e7eb);'
    'border-radius:12px;overflow-x:auto;font-size:14px;line-height:1.6;"><code>' + PAYLOAD +
    "</code></pre>"
    '<p style="margin:8px 0 0;font-size:14px;color:var(--slate-500,#64748b);">A vCard 3.0 payload as '
    "a QR code would carry it, one property per line. The name, company, number and addresses are "
    "placeholders, not a real person.</p></div>"
)
ANCHOR = NEW_H2 + '</div><ul class="checklist" style="max-width:640px;margin:0 auto;">'
if MARK not in s:
    assert s.count(ANCHOR) == 1, "H2 + checklist anchor not unique"
    s = s.replace(ANCHOR, NEW_H2 + "</div>" + EXAMPLE + '<ul class="checklist" style="max-width:640px;margin:0 auto;">', 1)
    changed.append("example")

m = re.search(r'("url":"https://company-card\.com/' + re.escape(F) +
              r'"[^<]*?"dateModified":")(\d{4}-\d{2}-\d{2})(")', s)
assert m, "WebPage dateModified not found"
if m.group(2) != DATE:
    s = s[:m.start(2)] + DATE + s[m.end(2):]
    changed.append("dateModified")
open(F, "w", encoding="utf-8").write(s)

sm = open("sitemap.xml", encoding="utf-8").read()
pat = re.compile(r'(<loc>https://company-card\.com/' + re.escape(F) + r'</loc><lastmod>)(\d{4}-\d{2}-\d{2})')
mm = pat.search(sm)
assert mm, "sitemap entry not found"
if mm.group(2) != DATE:
    sm = pat.sub(lambda x: x.group(1) + DATE, sm, count=1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    changed.append("sitemap-lastmod")

# ---------- generator ----------
G = "seo/pages_data12.py"
g = open(G, encoding="utf-8").read()
GEN = [
    ('"title": "vCard QR Code: What\'s Encoded Inside | CompanyCard",',
     '"title": "vCard QR Code Format: What\'s Encoded Inside | CompanyCard",'),
    (' "meta": ("What a vCard QR code actually encodes: the .vcf payload, why extra fields make the "\n'
     '          "code denser and harder to scan, and when a link works better."),',
     ' "meta": ("' + DESC + '"),'),
    (' "og": ("What a vCard QR code actually encodes: the .vcf payload, why extra fields make the "\n'
     '        "code denser and harder to scan, and when a link works better."),',
     ' "og": ("' + DESC + '"),'),
    ('block("The anatomy of the payload", checklist([',
     'block("The vCard QR code format, line by line", checklist(['),
]
for old, new in GEN:
    if new in g:
        continue
    assert g.count(old) == 1, f"{G}: anchor not unique: {old[:60]!r}"
    g = g.replace(old, new, 1)
    changed.append("generator")
NOTE = ("SUPERSEDED IN PART, 2026-11-14 (vcard-qr-code.html). Do not rebuild vcard-qr-code.html "
        "from this file: the live HTML and seo/improve_vcard_format_2026_11_14.py are its source of "
        "truth. A render from here lacks what later scripts added to the live page (the WebPage "
        "JSON-LD with its dates, and the example vCard payload block under 'The vCard QR code "
        "format, line by line'), and the improve script stops on such a render rather than "
        "patching it.\n\n")
NOTE_KEY = "SUPERSEDED IN PART, 2026-11-14 (vcard-qr-code.html)"
if NOTE_KEY not in g:
    k = g.find('"""')
    assert k != -1
    g = g[:k + 3] + NOTE + g[k + 3:]
    changed.append("generator-note")
else:
    i = g.find(NOTE_KEY)
    j = g.find("\n\n", i) + 2
    if g[i:j] != NOTE:
        g = g[:i] + NOTE + g[j:]
        changed.append("generator-note-updated")
open(G, "w", encoding="utf-8").write(g)
py_compile.compile(G, doraise=True)

print("changed:", ", ".join(changed) or "nothing (already applied)")
