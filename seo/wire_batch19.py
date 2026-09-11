# -*- coding: utf-8 -*-
"""Batch 21 wiring — sitewide footer, sitemap, llms.txt, freshness stamps.

Same shape as wire_batch18.py (batch 19), for blinq-vs-popl.html.

FOOTER. Anchor-insert after the "Popl vs Uniqode" <li> so the vs-cluster
stays contiguous (HiHello vs Blinq -> Popl vs Uniqode -> Blinq vs Popl), with
the batch-18 anchors as fallbacks. Never a whole-footer replace: the site has
15 byte-distinct footer variants. brand-kit.html (minimal footer) and the
Google verification stub (no footer) are left alone as in every batch.
seo/_tpl_footer.txt was one link behind the live footer (missing Popl vs
Uniqode) when this batch started; it was brought level in the same commit
BEFORE the page was rendered, so blinq-vs-popl.html shipped with the full
footer and the check "footer links equal to about.html" passed.

SITEMAP. Inserted immediately after popl-vs-uniqode.html. Priority 0.9 /
weekly, matching the other comparison pages.

LLMS.TXT. One line under "## Comparisons", after the Popl vs Uniqode line,
stating the page's conclusions (Blinq publishes every price and Popl none;
Popl's individual link goes to an app download; Blinq Business starts at five
cards; where CompanyCard loses) rather than merely that the page exists.

FRESHNESS. NOT seo/add_freshness.py — its DATE is still 2026-08-02 and would
roll dateModified backward sitewide. Only the two files that changed:
  * blinq-vs-popl.html — new page, published and modified 2026-09-11.
  * popl-vs-uniqode.html — its claim that the word "free" does not appear on
    Popl's pricing page was corrected (it appears once, in the footer link
    "Get the free mobile app") in visible FAQ, FAQPage JSON-LD and the table
    cell, so its dateModified and sitemap lastmod move.

Idempotent. Run from repo root: python3 seo/wire_batch19.py
"""
import os
import re
import json

DATE = "2026-09-11"
BASE = "https://company-card.com/"
SLUG = "blinq-vs-popl.html"
ALSO_TOUCHED = "popl-vs-uniqode.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link ----------
ANCHORS = [
    '<li><a href="popl-vs-uniqode.html">Popl vs Uniqode</a></li>',
    '<li><a href="hihello-vs-blinq.html">HiHello vs Blinq</a></li>',
    '<li><a href="popl-alternative.html">Popl Alternative</a></li>',
]
NEW_LI = '<li><a href="%s">Blinq vs Popl</a></li>' % SLUG

touched = skipped = 0
for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
    h = open(fn, encoding="utf-8").read()
    if NEW_LI in h:
        continue
    for anchor in ANCHORS:
        if anchor in h:
            assert h.count(anchor) == 1, (fn, anchor, h.count(anchor))
            h = h.replace(anchor, anchor + NEW_LI, 1)
            open(fn, "w", encoding="utf-8").write(h)
            touched += 1
            break
    else:
        skipped += 1
print("footer link added to %d pages (%d have no matching footer anchor)" % (touched, skipped))

# ---------- 2. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    after_re = re.compile(
        r'<url><loc>' + re.escape(BASE + "popl-vs-uniqode.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "popl-vs-uniqode sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# popl-vs-uniqode.html genuinely changed this commit -> move its lastmod
uq_re = re.compile(
    r'(<url><loc>' + re.escape(BASE + ALSO_TOUCHED) + r'</loc><lastmod>)([^<]*)(</lastmod>)')
m = uq_re.search(sm)
assert m and len(uq_re.findall(sm)) == 1, "popl-vs-uniqode lastmod entry not uniquely found"
if m.group(2) != DATE:
    sm = uq_re.sub(lambda x: x.group(1) + DATE + x.group(3), sm, count=1)
    print("sitemap lastmod for %s: %s -> %s" % (ALSO_TOUCHED, m.group(2), DATE))
else:
    print("sitemap lastmod for %s already %s" % (ALSO_TOUCHED, DATE))
open("sitemap.xml", "w", encoding="utf-8").write(sm)

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

LINE = ("- Blinq vs Popl — a head-to-head between two competitors, not a CompanyCard pitch. Blinq "
        "publishes every price (Free with two cards; Premium $9.99/mo or $7.33/mo annual, up to five "
        "cards; Business $6.99/user/mo or $4.99 annual, billed per card with a minimum of five cards "
        "to start, so the smallest Business bill is $34.95/mo). Popl publishes no rates and no tiers "
        "— its pricing page's calls to action are \"Request Pricing\" and \"Book a Demo\", its "
        "homepage FAQ offers \"free trials and personalized demos\" rather than a free plan, and "
        "its \"Popl for Individuals\" link redirects to an app-download page — and it sells itself "
        "as an AI platform for in-person event lead capture. Verdict on the page: Blinq for an "
        "individual or small business, Popl for an events team. CompanyCard loses to Blinq on the "
        "free plan (2 cards, no credit vs our 1 with a credit) and on the per-seat team rate ($6.99 "
        "vs our $12); its checkable edges are a published price where Popl has none, no seat minimum "
        "(which matters only for one or two people), and Pro at $7.99 vs Blinq Premium at $9.99 with "
        "fewer features. Verified 11 September 2026: " + BASE + SLUG)

if LINE not in ll:
    anchor_start = "- Popl vs Uniqode (formerly Beaconstac) — a head-to-head"
    i = ll.find(anchor_start)
    assert i != -1 and ll.count(anchor_start) == 1, "llms.txt Popl vs Uniqode anchor not uniquely found"
    j = ll.find("\n", i)
    assert j != -1
    ll = ll[:j + 1] + LINE + "\n" + ll[j + 1:]
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt: page listed under Comparisons")
else:
    print("llms.txt entry already present")

# ---------- 4. freshness stamps, changed files only ----------
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
        h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)
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


stamp(SLUG, DATE, DATE)              # new page
stamp(ALSO_TOUCHED, DATE, DATE)      # datePublished preserved from its existing block
print("done")
