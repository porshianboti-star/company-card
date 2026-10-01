# -*- coding: utf-8 -*-
"""Monthly competitor re-verification — October 2026 (the two comparison pages).

Every competitor source cited on best-digital-business-card.html and
free-digital-business-card-comparison.html was re-read on 2026-10-01 in a real
browser, with each billing toggle flipped both ways:

  blinq.me/pricing        Free 2 cards + signature + backgrounds + Wallet;
                          Premium $9.99/mo ($7.33 yearly); Business $6.99/card
                          ($4.99 yearly); billing FAQ "(minimum of five)".
  hihello.com/pricing     4 free cards, 5 card & badge scans /mo, wallet;
                          Professional $8 monthly / $6 yearly; Business 5-100
                          users $6 monthly / $5 yearly.
  wavecnct.com/pricing    Free card + Wallet + lead capture form; Pro $9 / $7
                          yearly; Teams $7 / $5 yearly, "3 minimum seats";
                          Pro lists "Remove Wave branding".
  popl.co/pages/pricing   "Request pricing" only; no free plan on the pricing
                          page or the homepage.
  uniqode.com/pricing     "create your first digital business card ... for
                          free"; Team $6 per user per month; cards FAQ "No, we
                          do not offer monthly plans".
  mobilocard.com/pricing-2  Pro $3/month "Start for Free"; no seat minimum
                          stated.

Every figure and every attributed wording on the two pages still matches, so
this run changes dates only. CompanyCard's own figures were re-read from the
live pricing.html the same day; its "verified 29 September 2026" stamp is the
pricing page's own and is shared by many pages, so it is left alone.

Other vendor pages keep their September stamp: their sources (Linq, V1CE and
the vendor-vs-vendor pages' extra quotes) were not all re-read today.

Idempotent. Run from repo root: python3 seo/refresh_verified_oct2026.py
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

PAGES = ["best-digital-business-card.html", "free-digital-business-card-comparison.html"]
TODAY_LONG, TODAY_ISO = "1 October 2026", "2026-10-01"

for f in PAGES:
    t = orig = open(f, encoding="utf-8").read()
    t = t.replace("Last updated: 29 September 2026", "Last updated: " + TODAY_LONG)
    # bare month stamps only — "29 September 2026" (CompanyCard facts) stays
    t, n = re.subn(r"(?<![0-9] )September 2026", "October 2026", t)
    t = re.sub(r'"dateModified":\s*"2026-09-\d\d"', '"dateModified":"%s"' % TODAY_ISO, t)
    if "Last updated: " + TODAY_LONG not in t:
        sys.exit("FAIL: no Last-updated stamp in " + f)
    if re.search(r"(?<![0-9] )September 2026", t):
        sys.exit("FAIL: bare September stamp left in " + f)
    if t != orig:
        open(f, "w", encoding="utf-8").write(t)
    print(f, "month stamps bumped:", n)

s = orig = open("sitemap.xml", encoding="utf-8").read()
for f in PAGES:
    s = re.sub(r"(<loc>https://company-card\.com/%s</loc><lastmod>)[0-9-]+" % re.escape(f),
               r"\g<1>" + TODAY_ISO, s)
if s != orig:
    open("sitemap.xml", "w", encoding="utf-8").write(s)
print("sitemap lastmod updated" if s != orig else "sitemap unchanged")
