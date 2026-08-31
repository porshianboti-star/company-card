# -*- coding: utf-8 -*-
"""Batch 17 wiring — footer link, sitemap entry, llms.txt entry, freshness stamp.

FOOTER. Anchor-insert against the byte-identical "Free Digital Card" <li>, which
closes the Solutions column and appears in 59 of the 61 HTML files (brand-kit
carries a minimal footer and the Google verification stub has none — both are
left alone, as in every batch). Solutions is the right column: this is an
audience page, not a comparison. A whole-footer replace would clobber the
several byte-distinct footer variants that still exist across the site.

SITEMAP. Inserted immediately after digital-business-card-for-small-business.html
so the audience cluster stays contiguous. Priority 0.8, matching the other
audience pages rather than the 0.9 comparison pages.

LLMS.TXT. One addition under "## Pages by audience". The line states the page's
actual conclusions — that any of four titles is correct, that co-owners should
take one card each, and that CompanyCard's free plan is one card per account so
two owners need two accounts. An entry that only says "we have a page about
titles" gives an assistant nothing to cite; one that concedes the free-plan
limit is the kind that gets quoted accurately.

FRESHNESS. Deliberately NOT seo/add_freshness.py — per the standing note that
the script re-inflicts a false datePublished on the July pages, silently strips
the publisher node's disambiguatingDescription, and flattens every sitemap
lastmod. Only the genuinely new page is stamped, and only its lastmod is set.
The added footer link does not earn a dateModified bump on the other 59 pages
(2026-08-04 precedent).

Idempotent. Run from repo root: python3 seo/wire_batch17.py
"""
import os
import re
import json

DATE = "2026-08-31"
BASE = "https://company-card.com/"
SLUG = "business-card-for-business-owners.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link ----------
ANCHOR = '<li><a href="free-digital-business-card.html">Free Digital Card</a></li>'
NEW_LI = '<li><a href="%s">For Business Owners</a></li>' % SLUG

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
        r'<url><loc>' + re.escape(BASE + "digital-business-card-for-small-business.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "small-business sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

LINE = ("- Business card for the owner of a company — what job title to use when you own the "
        "business (Owner, Founder, Director and Principal all read correctly; Director is "
        "commonly a registry-filed role, so it should only be claimed if held), how two or "
        "more co-owners should split cards (one card each on the same design, not one shared "
        "two-name card), and what may go on a card before the business is registered (trade "
        "under your own name; no Ltd/LLC/Inc, company number or registered address you do not "
        "have). States plainly that CompanyCard's free plan is one card per account, so two "
        "co-owners need two free accounts or a paid plan: " + BASE + SLUG)

if LINE not in ll:
    anchor = ("- Digital business card for small business: " + BASE
              + "digital-business-card-for-small-business.html")
    assert ll.count(anchor) == 1, "llms.txt audience anchor not uniquely found"
    ll = ll.replace(anchor, anchor + "\n" + LINE, 1)
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt: owner page listed under Pages by audience")
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
