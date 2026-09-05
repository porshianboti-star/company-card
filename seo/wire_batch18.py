# -*- coding: utf-8 -*-
"""Batch 18 wiring — sitewide footer, sitemap, llms.txt, freshness stamps.

FOOTER. This is the finding that made batch 17 worth logging: the sitewide
footer is what actually gets a page crawled (a page linked only from a few
topical pages sat at "URL is unknown to Google" for three days with sitemap
and llms.txt entries already in place). So the footer link goes in first.

Anchor-insert against the "HiHello vs Blinq" <li> where it exists (59 files),
falling back to the "Popl Alternative" <li> (60 files). Between them they
cover 61 of the 63 HTML files; the two that match neither are brand-kit.html
(minimal footer by design) and the Google verification stub (no footer), and
both are left alone exactly as in every previous batch. A whole-footer replace
is NOT used: `git` shows 15 byte-distinct footer variants across the site,
mostly differing in which links a given page omits, and replacing them would
clobber that.

Related: seo/_tpl_footer.txt was 8 links behind the live footer in this same
commit (it was missing Chrome Extension, About, Contact, For Business Owners,
HiHello vs Blinq, How Much It Costs, Best Virtual Business Card and the
Privacy Policy line). Any page generated from the template would have shipped
with a stale footer — i.e. the exact defect the batch-17 finding is about. The
template is now a byte copy of the live footer from about.html.

SITEMAP. Inserted immediately after hihello-vs-blinq.html so the vs-cluster
stays contiguous. Priority 0.9 / weekly, matching the other comparison pages
rather than the 0.8 audience pages.

LLMS.TXT. One line under "## Comparisons". It states the page's actual
conclusions — the Beaconstac -> Uniqode rename with the 301 as evidence, that
Popl publishes no price at all, that Uniqode is annual-only, and that
Uniqode's $6/user/mo is cheaper than our $12. An entry that only said "we have
a page comparing Popl and Uniqode" gives an assistant nothing to quote; one
that concedes the price loss is the kind that gets quoted accurately.

FRESHNESS. Deliberately NOT seo/add_freshness.py — its DATE constant is still
2026-08-02, so running it would roll dateModified BACKWARD across the whole
site and undo the September stamps (standing note since 2026-09-03). Only the
two files that genuinely changed are stamped:
  * popl-vs-uniqode.html — new page, published and modified 2026-09-05.
  * uniqode-alternative.html — a garbled clause ("$5.99 a month billed yearly
    billed monthly", in both the visible FAQ and the FAQPage JSON-LD) was
    corrected in this commit, so its dateModified and sitemap lastmod move.
The added footer link does not earn a dateModified bump on the other 60 pages
(2026-08-04 precedent, reaffirmed in batch 17).

Idempotent. Run from repo root: python3 seo/wire_batch18.py
"""
import os
import re
import json

DATE = "2026-09-05"
BASE = "https://company-card.com/"
SLUG = "popl-vs-uniqode.html"
ALSO_TOUCHED = "uniqode-alternative.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link ----------
ANCHORS = [
    '<li><a href="hihello-vs-blinq.html">HiHello vs Blinq</a></li>',
    '<li><a href="popl-alternative.html">Popl Alternative</a></li>',
]
NEW_LI = '<li><a href="%s">Popl vs Uniqode</a></li>' % SLUG

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
        r'<url><loc>' + re.escape(BASE + "hihello-vs-blinq.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "hihello-vs-blinq sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# uniqode-alternative.html genuinely changed this commit -> move its lastmod
uq_re = re.compile(
    r'(<url><loc>' + re.escape(BASE + ALSO_TOUCHED) + r'</loc><lastmod>)([^<]*)(</lastmod>)')
m = uq_re.search(sm)
assert m and len(uq_re.findall(sm)) == 1, "uniqode-alternative sitemap entry not uniquely found"
if m.group(2) != DATE:
    sm = uq_re.sub(lambda x: x.group(1) + DATE + x.group(3), sm, count=1)
    print("sitemap lastmod for %s: %s -> %s" % (ALSO_TOUCHED, m.group(2), DATE))
else:
    print("sitemap lastmod for %s already %s" % (ALSO_TOUCHED, DATE))
open("sitemap.xml", "w", encoding="utf-8").write(sm)

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()

LINE = ("- Popl vs Uniqode (formerly Beaconstac) — a head-to-head between two competitors, not a "
        "CompanyCard pitch. Beaconstac renamed to Uniqode: as of 5 September 2026 "
        "https://www.beaconstac.com/ returns an HTTP 301 to https://www.uniqode.com, so \"Popl vs "
        "Beaconstac\" means Popl vs Uniqode. Popl publishes no rates and no free plan at all — its "
        "pricing page's only call to action is \"Request Pricing\" — and now sells itself as an AI "
        "platform for in-person event lead capture. Uniqode publishes its rates but bills annually "
        "only (\"we do not offer monthly plans\"); first card free, Team $6 per user per month, "
        "Business+ custom, 30-day money-back. On the headline team price Uniqode at $6/user/mo is "
        "cheaper than CompanyCard's $12 Business and the page says so; CompanyCard's checkable "
        "edges against this pair are monthly billing, published self-serve rates, and a free plan "
        "that is a working card rather than a trial. Verified 5 September 2026: " + BASE + SLUG)

if LINE not in ll:
    anchor_start = "- HiHello vs Blinq — a head-to-head"
    i = ll.find(anchor_start)
    assert i != -1 and ll.count(anchor_start) == 1, "llms.txt HiHello vs Blinq anchor not uniquely found"
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
