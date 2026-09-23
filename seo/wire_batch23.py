#!/usr/bin/env python3
"""Batch 23 wiring: footer link to hihello-pricing.html on every page that
carries the Compare & Tools column, plus the footer template (so the next
build_pages render is not a link behind), plus llms.txt. Idempotent."""
import glob
OLD = '<li><a href="hihello-vs-popl.html">HiHello vs Popl</a></li>'
NEW = OLD + '<li><a href="hihello-pricing.html">HiHello Pricing</a></li>'
n = 0
for f in sorted(glob.glob("*.html")) + ["seo/_tpl_footer.txt"]:
    s = open(f, encoding="utf-8").read()
    if 'href="hihello-pricing.html">HiHello Pricing<' in s or OLD not in s:
        continue
    assert s.count(OLD) == 1, f
    open(f, "w", encoding="utf-8").write(s.replace(OLD, NEW)); n += 1
print("footer patched:", n)

L = open("llms.txt", encoding="utf-8").read()
ENTRY = ("- HiHello pricing — HiHello's own rates on both billing terms. Its pricing page loads with "
 "\"Billed yearly — up to 25% off\" switched on, so the first figures shown are yearly: "
 "Professional $6 a month ($72 a year), Business $5 per user a month ($60 per user a year). "
 "Billed monthly they are $8 and $6 per user. The advertised \"up to 25%\" is exactly 25% on "
 "Professional but about 17% on Business. Personal is free forever with four cards and 5 card "
 "and badge scans a month; Professional has 16 cards and 20 scans (an unlimited-scans add-on is "
 "offered without a printed price); Business is sold for 5–100 users and bills from five seats; "
 "Enterprise (101+) is a quote. Yearly bills: 5 users $300, 12 users $720, 50 users $3,000. "
 "CompanyCard is more expensive on the team rate ($12/$10 per user vs $6/$5) and has a smaller "
 "free plan (1 card with a credit); its team plan has no seat minimum, which is cheaper than "
 "HiHello's five-seat floor only for one or two users. Verified 23 September 2026: "
 "https://company-card.com/hihello-pricing.html\n")
if "hihello-pricing.html" not in L:
    i = L.index("- HiHello vs Popl —"); j = L.index("\n", i) + 1
    L = L[:j] + ENTRY + L[j:]
    open("llms.txt", "w", encoding="utf-8").write(L); print("llms.txt: added")
