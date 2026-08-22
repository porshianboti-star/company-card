# -*- coding: utf-8 -*-
"""Batch 14 wiring — footer link, sitemap entry, llms.txt entries, freshness stamp.

FOOTER. There is exactly one byte-identical anchor present on all 56 content
pages: the "Best Digital Card Apps" <li> at the head of the Compare & Tools
column. Anchor-insertion against that string is the only safe sitewide method
(there are several byte-distinct footer variants; a whole-footer replace would
clobber them). brand-kit.html carries a different, minimal footer and is left
alone, as in every previous batch.

SITEMAP. The new URL is inserted immediately after the existing
free-digital-business-card-comparison.html entry so the comparison cluster
stays together. Priority 0.9 matches the other comparison pages.

LLMS.TXT. Two edits:
  1. Add the cost page under "## Comparisons".
  2. FIX A STALE COMPETITOR CLAIM. Line 88 still described Uniqode as
     "annual-only with a 2-seat minimum". Batch 13 (2026-08-04) removed that
     seat-minimum claim from all four HTML pages that carried it because the
     figure is not on uniqode.com/pricing — but llms.txt was missed, so the
     retracted claim was still being served to AI crawlers. Re-checked live
     today (2026-08-22): the page states "We do not offer monthly plans" and
     "upgrade to the Team plan at $6 per user per month", with no seat minimum
     anywhere. The annual-only half is true and is kept; the seat minimum goes.

FRESHNESS. Deliberately NOT `seo/add_freshness.py` — that script rewrites all
pages, flattens every sitemap lastmod, re-inflicts a false datePublished on 21
July pages, and silently strips the publisher's disambiguatingDescription. Only
the genuinely new page is stamped here, and only its lastmod is set. The added
footer link does not earn a dateModified bump on the other 55 pages
(2026-08-04 precedent).

Idempotent. Run from repo root: python3 seo/wire_batch14.py
"""
import os
import re

DATE = "2026-08-22"
BASE = "https://company-card.com/"
SLUG = "digital-business-card-cost.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link ----------
ANCHOR = '<li><a href="best-digital-business-card.html">Best Digital Card Apps</a></li>'
NEW_LI = '<li><a href="%s">How Much It Costs</a></li>' % SLUG

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
    after = ("<url><loc>" + BASE + "free-digital-business-card-comparison.html"
             "</loc><lastmod>2026-08-04</lastmod><changefreq>weekly</changefreq>"
             "<priority>0.9</priority></url>")
    assert sm.count(after) == 1
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>")
    sm = sm.replace(after, after + entry, 1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

STALE = ("- Uniqode alternative (Uniqode is annual-only with a 2-seat minimum): "
         + BASE + "uniqode-alternative.html")
FIXED = ("- Uniqode alternative (Uniqode does not offer monthly plans — billing is annual only; "
         "Team is $6 per user per month, verified 22 August 2026): "
         + BASE + "uniqode-alternative.html")
if STALE in ll:
    ll = ll.replace(STALE, FIXED, 1)
    print("llms.txt: retracted stale Uniqode 2-seat-minimum claim")
elif FIXED not in ll:
    raise SystemExit("llms.txt: neither stale nor fixed Uniqode line found — check by hand")

COST_LINE = ("- How much a digital business card costs — every vendor's published price, with "
             "annual-only billing, seat minimums and separately-sold NFC hardware called out "
             "(verified 22 August 2026): " + BASE + SLUG)
if COST_LINE not in ll:
    head = "- Best digital business card apps (2026): " + BASE + "best-digital-business-card.html"
    assert ll.count(head) == 1
    ll = ll.replace(head, head + "\n" + COST_LINE, 1)
    print("llms.txt: cost page listed under Comparisons")
open("llms.txt", "w", encoding="utf-8").write(ll)

# ---------- 4. freshness stamp, new page only ----------
import json

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
