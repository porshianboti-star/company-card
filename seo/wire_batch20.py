# -*- coding: utf-8 -*-
"""Batch 22 wiring — sitewide footer (+ template), sitemap, llms.txt, stamps.

Same shape as wire_batch19.py (batch 21), for hihello-vs-popl.html.

FOOTER. Anchor-insert after the "Blinq vs Popl" <li> so the vs-cluster stays
contiguous (HiHello vs Blinq -> Popl vs Uniqode -> Blinq vs Popl -> HiHello
vs Popl), with earlier vs anchors as fallbacks. Never a whole-footer replace:
the site has 15 byte-distinct footer variants. brand-kit.html (minimal
footer) and the Google verification stub (no footer) are left alone.
seo/_tpl_footer.txt IS PATCHED HERE TOO — it was one link behind the live
footer for the third run running (missing Blinq vs Popl) when this batch
started; it was levelled by hand before rendering, and from this batch on the
wiring script treats the template as one more page so it cannot fall behind.

SITEMAP. Inserted immediately after blinq-vs-popl.html. Priority 0.9 /
weekly, matching the other comparison pages.

LLMS.TXT. One line under "## Comparisons", after the Blinq vs Popl line,
stating the page's conclusions (HiHello publishes every price behind a
default-on yearly toggle; Popl publishes none and is not billed per seat;
where CompanyCard loses) rather than merely that the page exists.

FRESHNESS. NOT seo/add_freshness.py — its DATE is still 2026-08-02 and would
roll dateModified backward sitewide. Only the files whose CONTENT changed:
  * hihello-vs-popl.html — new page, published and modified 2026-09-13.
  * the six pages corrected by seo/fix_hihello_billing_2026_09_13.py
    (hihello-vs-blinq, digital-business-card-cost, best-digital-business-card,
    free-digital-business-card-comparison, hihello-alternative,
    blinq-alternative) — dateModified and sitemap lastmod move; datePublished
    is preserved from each page's existing block.
  * hihello-vs-blinq.html additionally has its visible "1 September 2026"
    verification stamps moved to 13 September 2026: BOTH vendors it cites
    (hihello.com/pricing, blinq.me/pricing) and our own pricing.html were
    re-fetched today. The other five corrected pages cite vendors that were
    NOT re-fetched today, so their stamps stay; only their HiHello cells
    changed, and those cells now carry the billing term.

Idempotent. Run from repo root: python3 seo/wire_batch20.py
"""
import os
import re
import json

DATE = "2026-09-13"
BASE = "https://company-card.com/"
SLUG = "hihello-vs-popl.html"
CORRECTED = [
    "hihello-vs-blinq.html",
    "digital-business-card-cost.html",
    "best-digital-business-card.html",
    "free-digital-business-card-comparison.html",
    "hihello-alternative.html",
    "blinq-alternative.html",
]
RESTAMP_VISIBLE = {"hihello-vs-blinq.html": ("1 September 2026", "13 September 2026")}

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link (+ the template) ----------
ANCHORS = [
    '<li><a href="blinq-vs-popl.html">Blinq vs Popl</a></li>',
    '<li><a href="popl-vs-uniqode.html">Popl vs Uniqode</a></li>',
    '<li><a href="hihello-vs-blinq.html">HiHello vs Blinq</a></li>',
]
NEW_LI = '<li><a href="%s">HiHello vs Popl</a></li>' % SLUG

targets = sorted(f for f in os.listdir(".") if f.endswith(".html")) + ["seo/_tpl_footer.txt"]
touched = skipped = 0
for fn in targets:
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
print("footer link added to %d files (%d have no matching footer anchor)" % (touched, skipped))

# ---------- 2. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    after_re = re.compile(
        r'<url><loc>' + re.escape(BASE + "blinq-vs-popl.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "blinq-vs-popl sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    print("sitemap entry added")
else:
    print("sitemap entry already present")

for slug in CORRECTED:
    lm_re = re.compile(
        r'(<url><loc>' + re.escape(BASE + slug) + r'</loc><lastmod>)([^<]*)(</lastmod>)')
    m = lm_re.search(sm)
    assert m and len(lm_re.findall(sm)) == 1, "%s lastmod entry not uniquely found" % slug
    if m.group(2) != DATE:
        sm = lm_re.sub(lambda x: x.group(1) + DATE + x.group(3), sm, count=1)
        print("sitemap lastmod for %s: %s -> %s" % (slug, m.group(2), DATE))
open("sitemap.xml", "w", encoding="utf-8").write(sm)

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

LINE = ("- HiHello vs Popl — a head-to-head between two competitors, not a CompanyCard pitch. HiHello "
        "publishes every price, but its pricing page opens with a \"Billed yearly\" switch turned on, "
        "so the $6 (Professional) and $5 per user (Business) most comparisons quote are yearly rates; "
        "billed monthly they are $8 and $6 per user. Its Personal plan is free forever with four cards, "
        "capped at 5 card and badge scans a month; Business is sold for 5–100 users. Popl publishes no "
        "rates and no tiers — its pricing page's calls to action are \"Request Pricing\" and \"Book a "
        "Demo\", its homepage FAQ offers \"free trials and personalized demos\" rather than a free "
        "plan, its \"Popl for Individuals\" link redirects to an app-download page, and its pricing "
        "FAQ says the plan is not charged per user, per seat or per license — and it sells itself as "
        "an AI platform for in-person event lead capture. Verdict on the page: HiHello for an "
        "individual or small business, Popl for an events team. CompanyCard loses to HiHello on the "
        "free plan (4 cards, no credit vs our 1 with a credit) and on the per-seat team rate ($6 "
        "monthly / $5 yearly vs our $12 / $10); HiHello Professional and CompanyCard Pro are within a "
        "cent of each other on either billing term ($8 vs $7.99 monthly, $6 vs $5.99 yearly) and "
        "HiHello's includes sixteen cards to our one; our checkable edges are a published price where "
        "Popl has none and no seat minimum where HiHello Business starts at five users. Verified 13 "
        "September 2026: " + BASE + SLUG)

if LINE not in ll:
    anchor_start = "- Blinq vs Popl — a head-to-head"
    i = ll.find(anchor_start)
    assert i != -1 and ll.count(anchor_start) == 1, "llms.txt Blinq vs Popl anchor not uniquely found"
    j = ll.find("\n", i)
    assert j != -1
    ll = ll[:j + 1] + LINE + "\n" + ll[j + 1:]
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt: page listed under Comparisons")
else:
    print("llms.txt entry already present")

# ---------- 4. visible verification stamps, one page ----------
for slug, (old, new) in RESTAMP_VISIBLE.items():
    h = open(slug, encoding="utf-8").read()
    n = h.count(old)
    if n:
        h = h.replace(old, new)
        open(slug, "w", encoding="utf-8").write(h)
        print("%s: %d visible stamp(s) %s -> %s" % (slug, n, old, new))
    else:
        print("%s: no '%s' stamps left" % (slug, old))

# ---------- 5. freshness stamps, changed files only ----------
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


stamp(SLUG, DATE, DATE)
for slug in CORRECTED:
    stamp(slug, DATE, DATE)   # datePublished preserved from each existing block
print("done")
