# -*- coding: utf-8 -*-
"""Batch 27 wiring — digital-business-card-for-sales-teams.html.

FOOTER. Anchor-insert after the "Cards for Teams" <li> in every footer that
has it (66 files on 2026-10-07); never a whole-footer replace.

SITEMAP after the teams entry; LLMS.TXT after the teams line under
"Pages by audience".

REDIRECTS. Round 69 policy: one URL per page, the bare form 301s to .html
with a forced rule. Added for the new page and for the therapists page, which
batch 26 missed (measured live 2026-10-07: /digital-business-card-for-therapists
answered 200, not 301).

FRESHNESS. NOT seo/add_freshness.py (hardcoded 2026-08-02, rolls dates back).
Only the new page is stamped (published = modified = today).

Idempotent. Run from repo root: python3 seo/wire_batch27.py
"""
import os
import re
import json

DATE = "2026-10-07"
BASE = "https://company-card.com/"
SLUG = "digital-business-card-for-sales-teams.html"
ACC = "digital-business-cards-for-teams.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. footer ----------
ANCHOR = '<li><a href="%s">Cards for Teams</a></li>' % ACC
NEW_LI = '<li><a href="%s">For Sales Teams</a></li>' % SLUG
touched = 0
for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
    h = open(fn, encoding="utf-8").read()
    if NEW_LI in h or ANCHOR not in h:
        continue
    assert h.count(ANCHOR) == 1, (fn, h.count(ANCHOR))
    open(fn, "w", encoding="utf-8").write(h.replace(ANCHOR, ANCHOR + NEW_LI, 1))
    touched += 1
print("footer link added to %d files" % touched)

# ---------- 2. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    r = re.compile(r'<url><loc>' + re.escape(BASE + ACC) + r'</loc>.*?</url>', re.S)
    found = r.findall(sm)
    assert len(found) == 1, found
    m = r.search(sm)
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()
ACC_LINE = "- Digital business cards for teams: " + BASE + ACC
LINE = ("- Digital business card for sales teams & field sales reps (prospect saves the rep in "
        "one tap, lead capture on Pro and Business, brand and template lock, CRM sync and no "
        "seat minimum on Business): " + BASE + SLUG)
if LINE not in ll:
    assert ll.count(ACC_LINE) == 1, ll.count(ACC_LINE)
    ll = ll.replace(ACC_LINE, ACC_LINE + "\n" + LINE, 1)
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt entry added")

# ---------- 4. _redirects ----------
rd = open("_redirects", encoding="utf-8").read()
added = []
for s in ("digital-business-card-for-therapists", "digital-business-card-for-sales-teams"):
    rule = "/%s  /%s.html  301!" % (s, s)
    if rule not in rd:
        if not rd.endswith("\n"):
            rd += "\n"
        rd += rule + "\n"
        added.append(s)
if added:
    open("_redirects", "w", encoding="utf-8").write(rd)
    print("redirect rules added: %s" % ", ".join(added))

# ---------- 5. freshness ----------
MARK, ENDMARK = "<!-- FRESH:BEGIN -->", "<!-- FRESH:END -->"
DISAMBIG = ("A digital business card app for sharing your contact details by QR code, link or "
            "wallet pass. Not a corporate credit card, company expense card or spend-management "
            "service.")
PUBLISHER = {"@type": "Organization", "name": "CompanyCard",
             "disambiguatingDescription": DISAMBIG, "url": BASE}


def stamp(slug, published, modified):
    h = open(slug, encoding="utf-8").read()
    if MARK in h:
        old = re.search(re.escape(MARK) + r".*?" + re.escape(ENDMARK), h, re.S).group(0)
        prev = re.search(r'"datePublished":"([^"]+)"', old)
        published = prev.group(1) if prev else published
        h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK) + r"\n?", "", h, count=1, flags=re.S)
    title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", h, re.S).group(1)).strip()
    node = {"@context": "https://schema.org", "@type": "WebPage", "name": title,
            "url": BASE + slug, "datePublished": published, "dateModified": modified,
            "isPartOf": {"@type": "WebSite", "name": "CompanyCard", "url": BASE},
            "publisher": PUBLISHER, "inLanguage": "en"}
    blk = (MARK + '\n<script type="application/ld+json">'
           + json.dumps(node, ensure_ascii=False, separators=(",", ":"))
           + "</script>\n" + ENDMARK + "\n")
    i = h.find("</head>")
    assert i != -1, slug
    open(slug, "w", encoding="utf-8").write(h[:i] + blk + h[i:])
    print("stamped %s: published=%s modified=%s" % (slug, published, modified))


stamp(SLUG, DATE, DATE)
print("done")
