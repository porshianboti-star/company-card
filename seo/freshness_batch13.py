# -*- coding: utf-8 -*-
"""Batch 13 freshness — targeted, NOT the sitewide add_freshness.py sweep.

WHY NOT `python3 seo/add_freshness.py`. Running it unmodified would do three
things this pass, two of them dishonest:

  1. Set `dateModified` to DATE on all 55 pages. This run's only sitewide edit
     is one added footer link. The 2026-08-04 pass set the precedent that a
     boilerplate-nav change does not earn a modification stamp ("bumped only for
     the 12 pages actually changed, not sitewide"), and that is followed here.
  2. Rewrite every `<lastmod>` in sitemap.xml to a single DATE, destroying the
     per-page lastmod values set by the 2026-08-18 and 2026-08-19 competitor
     re-verification passes, which are accurate.
  3. Bump `datePublished` to DATE for the 21 slugs in its NEW_TODAY set. Those
     pages were published across batches 1-3, 10 and 11 in JULY, and already
     carry an inaccurate `datePublished` of 2026-08-02 from a previous run of
     this script. Their true publication dates are not recoverable from the
     repo, so this pass leaves them untouched rather than moving them further
     from the truth. Flagged for the log; not silently "fixed".

So only the two pages whose CONTENT actually changed today are stamped:
  * e-name-card.html — new this run; datePublished == dateModified == today.
  * pricing.html — the FAQ answer "Paid plans add things like custom branding,
    Apple & Google Wallet passes, ..." was replaced. It contradicted the plan
    table directly above it (which lists "Add to Apple & Google Wallet" under
    Free), the Free offer in this page's own AggregateOffer schema, and
    llms.txt — and it contradicted them on precisely the claim that is one of
    our three checkable differentiators. Both copies (visible <p> and the
    FAQPage JSON-LD) were replaced together.

Idempotent: re-running rewrites the same marker-bounded block.
Run from repo root: python3 seo/freshness_batch13.py
"""
import re, json, os

MARK, ENDMARK = "<!-- FRESH:BEGIN -->", "<!-- FRESH:END -->"
DATE = "2026-08-20"
BASE = "https://company-card.com/"

# The publisher node carries the category-collision disambiguation added sitewide
# (CompanyCard is not a corporate credit card). add_freshness.py does NOT emit it and
# would silently strip it from any page it rewrites — all 54 pages currently have it,
# so it is reproduced here verbatim rather than dropped.
DISAMBIG = ("A digital business card app for sharing your contact details by QR code, link or "
            "wallet pass. Not a corporate credit card, company expense card or spend-management "
            "service.")
PUBLISHER = {"@type": "Organization", "name": "CompanyCard",
             "disambiguatingDescription": DISAMBIG, "url": BASE}

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# slug -> datePublished ("" means keep whatever is already stamped)
TARGETS = {
    "e-name-card.html": DATE,       # genuinely new today
    "pricing.html": "2026-07-05",   # long-standing page, real content edit today
}

for f, published in TARGETS.items():
    h = open(f, encoding="utf-8").read()
    if MARK in h and ENDMARK in h:
        h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)

    m = re.search(r"<title>(.*?)</title>", h, re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else "CompanyCard"

    node = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "url": BASE + f,
        "datePublished": published,
        "dateModified": DATE,
        "isPartOf": {"@type": "WebSite", "name": "CompanyCard", "url": BASE},
        "publisher": PUBLISHER,
        "inLanguage": "en",
    }
    block = (MARK + '\n<script type="application/ld+json">'
             + json.dumps(node, ensure_ascii=False, separators=(",", ":"))
             + "</script>\n" + ENDMARK + "\n")

    i = h.find("</head>")
    assert i != -1, f"no </head> in {f}"
    h = h[:i] + block + h[i:]
    open(f, "w", encoding="utf-8").write(h)
    print(f"stamped {f}: published={published} modified={DATE}")

# sitemap lastmod for exactly those two URLs — every other entry is left alone
sm = open("sitemap.xml", encoding="utf-8").read()
for f in TARGETS:
    pat = re.compile(r"(<loc>" + re.escape(BASE + f) + r"</loc><lastmod>)[^<]+(</lastmod>)")
    sm, n = pat.subn(r"\g<1>" + DATE + r"\g<2>", sm)
    assert n == 1, (f, n)
    print(f"sitemap lastmod {f} -> {DATE}")
open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("done")
