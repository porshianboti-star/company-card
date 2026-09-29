# -*- coding: utf-8 -*-
"""Batch 26 wiring — digital-business-card-for-therapists.html.

FOOTER. Profession links live only in the long "Solutions" footer variant
(20 files); anchor-insert after the "For Lawyers" <li>, never a
whole-footer replace.

SITEMAP after the lawyers entry; LLMS.TXT after the lawyers line.

FRESHNESS. NOT seo/add_freshness.py (hardcoded 2026-08-02, rolls dates back).
Only the new page is stamped (published = modified = today); no existing page's
content changes, so no other date moves.

Idempotent. Run from repo root: python3 seo/wire_batch26.py
"""
import os
import re
import json

DATE = "2026-09-29"
BASE = "https://company-card.com/"
SLUG = "digital-business-card-for-therapists.html"
ACC = "digital-business-card-for-lawyers.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. footer ----------
ANCHOR = '<li><a href="%s">For Lawyers</a></li>' % ACC
NEW_LI = '<li><a href="%s">For Therapists</a></li>' % SLUG
touched = 0
for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
    h = open(fn, encoding="utf-8").read()
    if NEW_LI in h or ANCHOR not in h:
        continue
    assert h.count(ANCHOR) == 1, (fn, h.count(ANCHOR))
    open(fn, "w", encoding="utf-8").write(h.replace(ANCHOR, ANCHOR + NEW_LI, 1))
    touched += 1
print("footer link added to %d files" % touched)

# ---------- 3. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    r = re.compile(r'(<url><loc>' + re.escape(BASE + ACC) + r'</loc><lastmod>)([^<]*)(</lastmod>'
                   r'<changefreq>[^<]*</changefreq><priority>[^<]*</priority></url>)')
    m = r.search(sm)
    assert m and len(r.findall(sm)) == 1
    new_acc = m.group(0)
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    sm = sm[:m.start()] + new_acc + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")

# ---------- 4. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()
ACC_LINE = ("- Digital business card for lawyers & small law firms (practice areas, jurisdictions, "
            "first consultations for referred clients): " + BASE + ACC)
LINE = ("- Digital business card for therapists in private practice (what you work with, where "
        "you are licensed, fees, openings, first calls from referrals): " + BASE + SLUG)
if LINE not in ll:
    assert ll.count(ACC_LINE) == 1
    ll = ll.replace(ACC_LINE, ACC_LINE + "\n" + LINE, 1)
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt entry added")

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
