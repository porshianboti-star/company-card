# -*- coding: utf-8 -*-
"""Monthly competitor re-verification — November 2026.

All six sources cited on best-digital-business-card.html and
free-digital-business-card-comparison.html were re-read on 2026-11-01
(wavecnct.com and mobilocard.com in a real browser with the billing toggle
flipped; hihello.com in a real browser; blinq.me, popl.co, uniqode.com fetched):

  blinq.me/pricing        UNCHANGED. Free 2 cards + signature + backgrounds +
                          Wallet; Premium $9.99 / $7.33 yearly (5 cards);
                          Business $6.99 / $4.99 yearly; FAQ "(minimum of five)".
  hihello.com/pricing     CHANGED. Personal (free) is now "2 digital business
                          cards" (was 4); Professional is "8 digital business
                          cards" (was 16). Prices unchanged: Professional $6
                          yearly / $8 monthly; Business $5 / $6 per user,
                          "5-100 users", "five-seat minimum". The scan cap is
                          on HiHello's paper-card/badge scanner ("Scan 5 paper
                          business cards or badges a month"); the page states
                          "Other people can scan your own HiHello QR code as
                          often as they like, on every plan."
  wavecnct.com/pricing    UNCHANGED. Pro $9 monthly / $7 "billed annually";
                          Teams $7 / $5 "Per user/month (min 3)"; "Remove Wave
                          Connect branding" on Pro; free plan lists digital card,
                          unlimited sharing, Google or Apple Wallet, lead capture
                          form.
  popl.co/pages/pricing   UNCHANGED. "Request Pricing" / "Book a Demo"; no
                          dollar figure; no free plan on the page.
  uniqode.com/pricing     UNCHANGED. "create your first digital business card
                          with Uniqode for free"; Team $6 per user per month;
                          "No, we do not offer monthly plans".
  mobilocard.com/pricing-2 UNCHANGED. Pro "$3 /month", "Start for Free"; the only
                          seat wording is "* Requires 100 seats or more" on two
                          enterprise features.

So this run (a) corrects HiHello's card counts everywhere the site states them
(the two comparison pages, hihello-alternative, hihello-vs-blinq,
hihello-vs-popl, digital-business-card-cost, llms.txt), (b) rewords the scan
cap so it is no longer presented as a cap on how often a HiHello card can be
scanned — it is a cap on HiHello's paper-card/badge scanner — and (c) bumps the
verification stamps on the sentences that were re-checked. CompanyCard's own
figures were re-read from pricing.html / seo/facts.py today (Pro $4.99 / $3.99
yearly; Business $4.99 / $3.99 per user, no seat minimum) and are unchanged.
The free-plan "Apple and Google Wallet pass" claim is NOT touched here — it is
the owner's open decision (see growth/geo-log.md 2026-10-29).

Idempotent after one run (every edit asserts its old text on the first pass).
Run from repo root: python3 seo/refresh_verified_nov2026.py
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

TODAY_LONG, TODAY_ISO, TODAY_DMY = "1 November 2026", "2026-11-01", "1 November 2026"

# (file, old, new, min_count)
EDITS = [
 # ---- best-digital-business-card.html ----
 ("best-digital-business-card.html",
  "Blinq or HiHello if you want the most free cards (two and four respectively, both with signature, background and wallet)",
  "Blinq or HiHello if you want the most free cards (two each, both with signature, background and wallet)", 1),
 ("best-digital-business-card.html",
  "<td>4 cards, email signature, virtual background, wallet — capped at 5 card &amp; badge scans per month</td>",
  "<td>2 cards, email signature, virtual background, wallet — its paper-card &amp; badge scanner is capped at 5 scans per month</td>", 1),
 ("best-digital-business-card.html",
  "Someone who wants several free cards and low scan volume",
  "Someone who wants two free cards and scans few paper cards or badges", 1),
 ("best-digital-business-card.html",
  "Blinq gives two cards and HiHello four, and both include an email signature and a virtual background at $0 — we won't pretend otherwise. HiHello's free plan does cap card and badge scans at five per month, which matters if you hand your card out at events.",
  "Blinq and HiHello each give two cards, and both include an email signature and a virtual background at $0 — we won't pretend otherwise. HiHello's free plan does cap its paper-card and badge scanner — the feature that saves other people's cards as contacts — at five scans per month; scans of your own HiHello card are not limited.", 1),
 # ---- free-digital-business-card-comparison.html ----
 ("free-digital-business-card-comparison.html",
  "<tr><td><b>HiHello</b></td><td>4</td><td>Apple &amp; Google</td><td>5 card &amp; badge scans / month</td>",
  "<tr><td><b>HiHello</b></td><td>2</td><td>Apple &amp; Google</td><td>5 paper-card &amp; badge scans / month (its scanner; your own card is not capped)</td>", 1),
 ("free-digital-business-card-comparison.html",
  "HiHello's four free cards and Blinq's two are more generous than our one.",
  "HiHello's and Blinq's two free cards are more generous than our one.", 1),
 ("free-digital-business-card-comparison.html",
  "A monthly cap on how often your card can be scanned matters enormously if you work events, a counter or a shop floor, and not at all if you share your card a few times a month. HiHello's free tier caps card and badge scans at five per month; ours has no monthly cap.",
  "None of the free plans here caps how often your own card can be scanned — HiHello's pricing page says other people can scan your QR code as often as they like on every plan. What HiHello does cap on its free tier is its paper-card and badge scanner, the feature that saves other people's cards and event badges as contacts, at five scans a month. CompanyCard's free plan has no scanner at all; lead capture is a Pro feature.", 1),
 ("free-digital-business-card-comparison.html",
  "It depends what you need. On free card count, HiHello leads with four and Blinq gives two, both without a listed branding line — as of October 2026. CompanyCard's free plan is one card and carries a small CompanyCard credit, but includes an Apple and Google Wallet pass with no monthly cap on how often it is scanned, where HiHello's free tier caps card and badge scans at five per month. Popl has no free plan at all.",
  "It depends what you need. On free card count, HiHello and Blinq each give two, both without a listed branding line — as of November 2026. CompanyCard's free plan is one card and carries a small CompanyCard credit, but includes an Apple and Google Wallet pass and unlimited edits. HiHello's free tier caps its paper-card and badge scanner at five scans a month; none of these plans caps how often your own card is scanned. Popl has no free plan at all.", 2),
 # ---- hihello-alternative.html ----
 ("hihello-alternative.html",
  "HiHello's four-card free tier wins for individuals — compared honestly, verified September 2026.",
  "HiHello's two-card free tier wins for individuals — compared honestly, verified November 2026.", 1),
 ("hihello-alternative.html", "where HiHello's free plan gives you four cards.", "where HiHello's free plan gives you two cards.", 2),
 ("hihello-alternative.html", "As of September 2026 it gives four cards, an email signature", "As of November 2026 it gives two cards, an email signature", 1),
 ("hihello-alternative.html", "four cards as of September 2026, including", "two cards as of November 2026, including", 2),
 ("hihello-alternative.html", "four free cards to our one", "two free cards to our one", 1),
 ("hihello-alternative.html", "as of September 2026 HiHello's Personal plan is free and includes four cards", "as of November 2026 HiHello's Personal plan is free and includes two cards", 2),
 ("hihello-alternative.html", "<td>4 cards<", "<td>2 cards<", 1),
 ("hihello-alternative.html", "as of September 2026 HiHello's Business plan is sold for 5-100 users", "as of November 2026 HiHello's Business plan is sold for 5-100 users", 2),
 # ---- hihello-vs-blinq.html ----
 ("hihello-vs-blinq.html",
  "verified 13 September 2026. HiHello&#x27;s free plan gives 4 cards but caps scans; Blinq&#x27;s gives 2 with unlimited sharing. HiHello is cheaper on both paid tiers.",
  "verified 1 November 2026. HiHello&#x27;s free plan gives 2 cards, the same as Blinq&#x27;s, but caps its paper-card scanner. HiHello is cheaper on both paid tiers.", 1),
 ("hihello-vs-blinq.html",
  "Four cards free against two, and sixteen at $8 a month ($6 billed yearly) against five at $9.99 ($7.33 billed yearly). If you run more than one role, side business or language and want a separate card for each, this is the single biggest gap between the two products.",
  "Two cards free on each, then eight at $8 a month ($6 billed yearly) against five at $9.99 ($7.33 billed yearly). If you run more than one role, side business or language and want a separate card for each, the paid tiers are where the two products differ.", 1),
 ("hihello-vs-blinq.html",
  "Its free plan gives you four cards against Blinq's two, and its first paid tier is $8 a month billed monthly — $6 a month if you pay $72 for the year — for sixteen cards, against",
  "Its free plan gives you two cards, the same as Blinq's, and its first paid tier is $8 a month billed monthly — $6 a month if you pay $72 for the year — for eight cards, against", 1),
 ("hihello-vs-blinq.html", "$8/mo billed monthly, or $6/mo billed yearly (16 cards)", "$8/mo billed monthly, or $6/mo billed yearly (8 cards)", 1),
 ("hihello-vs-blinq.html", "16 cards, 1 user", "8 cards, 1 user", 1),
 ("hihello-vs-blinq.html", "4 cards, 5 scans/mo", "2 cards, 5 scans/mo", 1),
 ("hihello-vs-blinq.html", "“Free Forever” — 4 digital business cards, 1 user", "“Free Forever” — 2 digital business cards, 1 user", 1),
 ("hihello-vs-blinq.html", "against HiHello's 4 and Blinq's 2; Pro at", "against HiHello's 2 and Blinq's 2; Pro at", 2),
 ("hihello-vs-blinq.html", "for one card instead of sixteen", "for one card instead of eight", 3),
 ("hihello-vs-blinq.html", "HiHello Professional includes sixteen cards to our one", "HiHello Professional includes eight cards to our one", 1),
 ("hihello-vs-blinq.html",
  "HiHello's Personal plan is free forever with 4 cards, 1 user and 5 card and badge scans a month. Professional is $8 a month billed monthly, or $72 a year ($6 a month) billed yearly, for 16 cards and 20 scans a month.",
  "HiHello's Personal plan is free forever with 2 cards, 1 user and 5 paper-card and badge scans a month. Professional is $8 a month billed monthly, or $72 a year ($6 a month) billed yearly, for 8 cards and 20 scans a month.", 2),
 ("hihello-vs-blinq.html", "Verified 13 September 2026 on hihello.com/pricing.", "Verified 1 November 2026 on hihello.com/pricing.", 2),
 ("hihello-vs-blinq.html", "Verified 13 September 2026 on blinq.me/pricing.", "Verified 1 November 2026 on blinq.me/pricing.", 2),
 ("hihello-vs-blinq.html", "Verified 13 September 2026 on each vendor's own pricing page.", "Verified 1 November 2026 on each vendor's own pricing page.", 2),
 ("hihello-vs-blinq.html",
  "HiHello's free plan gives 4 digital business cards but caps you at “5 card & badge scans /mo”. Blinq's gives 2 cards with unlimited sharing and no published monthly cap, but keeps its contact scanner in the paid Premium tier. If you hand cards out, HiHello gives you more.",
  "HiHello's free plan gives 2 digital business cards but caps its paper-card and badge scanner at 5 scans a month. Blinq's gives 2 cards with unlimited sharing and no published monthly cap, but keeps its contact scanner in the paid Premium tier. On free card count the two are level.", 2),
 ("hihello-vs-blinq.html",
  "On published prices HiHello is cheaper for one person and gives more cards: 4 free against Blinq's 2, and 16 cards at $8 a month",
  "On published prices HiHello is cheaper for one person and gives more paid cards: 2 free on each, and 8 cards at $8 a month", 2),
 ("hihello-vs-blinq.html",
  "HiHello's free plan is generous about <b>having</b> cards and stingy about <b>scanning</b> them: four cards, but “5 card &amp; badge scans /mo”.",
  "HiHello's free plan matches Blinq on <b>having</b> cards and is stingy about <b>scanning</b> other people's: two cards, but “Scan 5 paper business cards or badges a month”.", 1),
 ("hihello-vs-blinq.html", "<b>HiHello wins on card count</b> Two cards free on each", "<b>HiHello wins on paid card count</b> Two cards free on each", 1),
 ("hihello-vs-blinq.html", "“5 card &amp; badge scans /mo”", "“Scan 5 paper business cards or badges a month”", 1),
 ("hihello-vs-blinq.html", "Enterprise is custom pricing for 101+ users.", "Enterprise is custom pricing for 100+ users.", 2),
 ("hihello-vs-blinq.html", "101+ users", "100+ users", 1),
 # ---- hihello-vs-popl.html ----
 ("hihello-vs-popl.html", "$72 a year if you pay up front, sixteen cards,", "$72 a year if you pay up front, eight cards,", 1),
 ("hihello-vs-popl.html", "includes four cards, wallet passes for Apple and Google", "includes two cards, wallet passes for Apple and Google", 1),
 ("hihello-vs-popl.html", "(Professional, 16 cards)", "(Professional, 8 cards)", 1),
 ("hihello-vs-popl.html", "take HiHello's four free cards", "take HiHello's two free cards", 1),
 ("hihello-vs-popl.html", "$0 — Personal, 4 cards, 5 scans a month", "$0 — Personal, 2 cards, 5 scans a month", 1),
 ("hihello-vs-popl.html", "HiHello: four, on a plan it labels", "HiHello: two, on a plan it labels", 2),
 ("hihello-vs-popl.html", "All three read on 19 September 2026.", "All three read on 1 November 2026.", 2),
 # ---- digital-business-card-cost.html ----
 ("digital-business-card-cost.html",
  "HiHello's is four cards but caps you at five card and badge scans a month",
  "HiHello's is two cards but caps its paper-card and badge scanner at five scans a month", 2),
 # ---- llms.txt ----
 ("llms.txt", "(free 4 cards vs 2; Professional", "(free 2 cards each; Professional", 1),
 ("llms.txt", "sixteen cards to our one", "eight cards to our one", 1),
 ("llms.txt", "Blinq's free plan includes two cards and HiHello's four.", "Blinq's free plan includes two cards and HiHello's two.", 1),
 ("llms.txt", "capped at 5 card and badge scans per month as of September 2026", "capped at 5 paper-card and badge scans per month as of November 2026", 1),
 ("llms.txt", "Verified 1 September 2026: https://company-card.com/hihello-vs-blinq.html", "Verified 1 November 2026: https://company-card.com/hihello-vs-blinq.html", 1),
]

touched = set()
cache = {}
def load(f):
    if f not in cache:
        cache[f] = open(f, encoding="utf-8").read()
    return cache[f]

already = all(load(f).count(new) >= n and old not in load(f) for f, old, new, n in EDITS)
if already:
    print("edits already applied (idempotent re-run)")
else:
    for f, old, new, n in EDITS:
        t = load(f)
        c = t.count(old)
        if c == 0 and t.count(new) >= n:
            print("%-45s already applied" % f); continue
        if c < n:
            sys.exit("FAIL %s: expected >=%d of %r, found %d" % (f, n, old[:70], c))
        cache[f] = t.replace(old, new)
        touched.add(f)
        print("%-45s x%d  %s" % (f, c, old[:60].replace("\n", " ")))

# month stamps on the two comparison pages (every source re-read today)
for f in ["best-digital-business-card.html", "free-digital-business-card-comparison.html"]:
    t = load(f)
    t = t.replace("Last updated: 1 October 2026", "Last updated: " + TODAY_LONG)
    t, n = re.subn(r"(?<![0-9] )October 2026", "November 2026", t)
    if "Last updated: " + TODAY_LONG not in t:
        sys.exit("FAIL: no Last-updated stamp in " + f)
    if re.search(r"(?<![0-9] )October 2026", t):
        sys.exit("FAIL: bare October stamp left in " + f)
    cache[f] = t; touched.add(f)
    print(f, "month stamps bumped:", n)

PAGES = [f for f in cache if f.endswith(".html")]
for f in PAGES:
    t = cache[f]
    t2 = re.sub(r'"dateModified":\s*"2026-\d\d-\d\d"', '"dateModified":"%s"' % TODAY_ISO, t)
    if t2 != t:
        cache[f] = t2; touched.add(f)

for f in cache:
    open(f, "w", encoding="utf-8").write(cache[f])

s = orig = open("sitemap.xml", encoding="utf-8").read()
for f in PAGES:
    s = re.sub(r"(<loc>https://company-card\.com/%s</loc><lastmod>)[0-9-]+" % re.escape(f),
               r"\g<1>" + TODAY_ISO, s)
if s != orig:
    open("sitemap.xml", "w", encoding="utf-8").write(s)
print("sitemap lastmod updated for", len(PAGES), "pages" if s != orig else "(unchanged)")

# guard: no stale HiHello card counts left anywhere on the site
bad = []
for f in sorted(os.listdir(".")):
    if f.endswith(".html") or f == "llms.txt":
        t = open(f, encoding="utf-8").read()
        for pat in [r"HiHello[^.<]{0,80}\b(four|sixteen|16) cards", r"\b(four|4|sixteen|16) (free )?cards[^.<]{0,60}HiHello"]:
            for m in re.finditer(pat, t):
                bad.append((f, m.group(0)[:100]))
if bad:
    for b in bad: print("STALE:", b)
    sys.exit("FAIL: stale HiHello card counts remain")
print("OK: no stale HiHello card counts; touched", sorted(touched))
