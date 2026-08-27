# -*- coding: utf-8 -*-
"""Batch 15 wiring — footer link, sitemap entry, llms.txt entry, freshness stamp.

FOOTER. Same method as batch 14: anchor-insert against the single byte-identical
"Best Digital Card Apps" <li> at the head of the Compare & Tools column. A
whole-footer replace would clobber the several byte-distinct footer variants.
brand-kit.html carries a minimal footer and is left alone, as in every batch.

SITEMAP. Inserted immediately after the digital-business-card-cost.html entry so
the comparison cluster stays contiguous. Priority 0.9 matches the other
comparison pages.

LLMS.TXT. One addition under "## Comparisons". The entry states the page's own
conclusion — that HiHello is cheaper — because a comparison line that only says
"we compare X and Y" tells an assistant nothing it can cite, and because the
conclusion is the honest one even though it does not favour us.

FRESHNESS. Deliberately NOT seo/add_freshness.py — per the standing note that
script re-inflicts a false datePublished on 21 July pages, silently strips the
publisher node's disambiguatingDescription, and flattens every sitemap lastmod.
Only the genuinely new page is stamped here, and only its lastmod is set. The
added footer link does not earn a dateModified bump on the other 56 pages
(2026-08-04 precedent).

Idempotent. Run from repo root: python3 seo/wire_batch15.py
"""
import os
import re
import json

DATE = "2026-08-27"
BASE = "https://company-card.com/"
SLUG = "hihello-vs-blinq.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link ----------
ANCHOR = '<li><a href="best-digital-business-card.html">Best Digital Card Apps</a></li>'
NEW_LI = '<li><a href="%s">HiHello vs Blinq</a></li>' % SLUG

touched = 0
for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
    h = open(fn, encoding="utf-8").read()
    if ANCHOR not in h or NEW_LI in h:
        continue
    assert h.count(ANCHOR) == 1, (fn, h.count(ANCHOR))
    h = h.replace(ANCHOR, ANCHOR + NEW_LI, 1)
    open(fn, "w", encoding="utf-8").write(h)
    touched += 1
print("footer link added to %d pages" % touched)

# ---------- 2. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    after_re = re.compile(
        r'<url><loc>' + re.escape(BASE + "digital-business-card-cost.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "cost-page sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

VS_LINE = ("- HiHello vs Blinq — a head-to-head between two competitors, not a CompanyCard pitch. "
           "On published prices HiHello is cheaper at every tier (free 4 cards vs 2; $6/mo vs "
           "$9.99/mo; $5/user vs $6.99/card) while Blinq does not meter contact scanning and bills "
           "per card rather than per user. Both gate team plans behind five seats. Verified "
           "27 August 2026: " + BASE + SLUG)
if VS_LINE not in ll:
    head = "- Best digital business card apps (2026): " + BASE + "best-digital-business-card.html"
    assert ll.count(head) == 1, "llms.txt Comparisons anchor not uniquely found"
    ll = ll.replace(head, head + "\n" + VS_LINE, 1)
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt: HiHello vs Blinq listed under Comparisons")
else:
    print("llms.txt entry already present")

# ---------- 4. freshness stamp, new page only ----------
MARK, ENDMARK = "<!-- FRESH:BEGIN -->", "<!-- FRESH:END -->"
DISAMBIG = ("A digital business card app for sharing your contact details by QR code, link or "
            "wallet pass. Not a corporate credit card, company expense card or spend-management "
            "service.")
PUBLISHER = {"@type": "Organization", "name": "CompanyCard",
             "disambiguatingDescription": DISAMBIG, "url": BASE}

h = open(SLUG, encoding="utf-8").read()
if MARK in h:
    h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)
title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", h, re.S).group(1)).strip()
node = {"@context": "https://schema.org", "@type": "WebPage", "name": title,
        "url": BASE + SLUG, "datePublished": DATE, "dateModified": DATE,
        "isPartOf": {"@type": "WebSite", "name": "CompanyCard", "url": BASE},
        "publisher": PUBLISHER, "inLanguage": "en"}
block = (MARK + '\n<script type="application/ld+json">'
         + json.dumps(node, ensure_ascii=False, separators=(",", ":"))
         + "</script>\n" + ENDMARK + "\n")
i = h.find("</head>")
assert i != -1
open(SLUG, "w", encoding="utf-8").write(h[:i] + block + h[i:])
print("stamped %s: published=%s modified=%s" % (SLUG, DATE, DATE))
print("done")
