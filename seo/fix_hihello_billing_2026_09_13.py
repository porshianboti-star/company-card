# -*- coding: utf-8 -*-
"""2026-09-13 — HiHello's $6 / $5 are YEARLY-billed rates; monthly is $8 / $6.

WHAT WAS WRONG. hihello.com/pricing opens with a "Billed yearly up to 25% off"
switch turned ON. With it on, the page renders "Professional … $6 per month
$72 billed yearly" and "Business … $5 per user/month $60 per user/year". With
it off (clicked in the in-app browser on 2026-09-13; the page's own JS also
carries MONTHLY = {Professional: '$8', Business: '$6'}, note 'billed monthly')
it renders "Professional … $8 per month billed monthly" and "Business … $6 per
user/month billed monthly".

Every page on this site quoted $6 and $5 as HiHello's monthly prices, and
hihello-vs-blinq.html compared them to Blinq's MONTHLY-billed $9.99 and $6.99
and concluded "HiHello wins on price, at every tier". Like for like:
  individual  monthly $8 vs $9.99 (HiHello cheaper)   yearly $6 vs $7.33 (HiHello cheaper)
  team        monthly $6 vs $6.99 (HiHello cheaper)   yearly $5 vs $4.99 (Blinq cheaper by a cent)
So HiHello is cheaper for one person either way; the team tier is a near tie
that the billing term decides. Also affected: "HiHello and Blinq are both
cheaper than CompanyCard at every paid tier" — HiHello Professional ($8 / $6)
and CompanyCard Pro ($7.99 / $5.99) are within a cent of each other on either
term, so that sentence is replaced with the precise one. The "$24 vs $25"
seat-floor arithmetic mixed our monthly rate with HiHello's yearly one; it is
now $24 vs $30 monthly (or $20 vs $25 yearly).

Tenth member of the stale-claim family, same shape as the Calendly finding of
2026-09-08 (the number is on the vendor's page; the billing term under it
was not read). Rule restated: READ THE BILLING TOGGLE.

Also fixed while here: llms.txt said our free plan "has no monthly scan cap"
against HiHello's 5 — our free plan has no scanner at all (lead capture is a
Pro feature, as hihello-alternative.html states), so that was a misleading
edge; and seo/pages_data2.py's CompanyCard cell still said "$8 Pro" (the live
page says $7.99), a latent rebuild regression.

Every replacement asserts its exact expected count in each file, so a drift
in any target string fails loudly instead of silently skipping. Idempotent:
a second run finds zero targets and exits 0 with "already applied".
Run from repo root: python3 seo/fix_hihello_billing_2026_09_13.py
"""
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

HH_TEAM = ("HiHello $6 per user a month billed monthly, or $5 billed yearly")

# (file, [(old, new, expected_count), ...])
EDITS = [
 ("hihello-vs-blinq.html", [
   ("its first paid tier is $6 a month for sixteen cards against Blinq's $9.99 for five. "
    "On published price alone HiHello wins at every tier.",
    "its first paid tier is $8 a month billed monthly — $6 a month if you pay $72 for the year — "
    "for sixteen cards, against Blinq's $9.99 (or $7.33 yearly) for five. On published price "
    "HiHello is cheaper for one person on either billing term; the team tiers are within a dollar "
    "of each other and the billing term decides it.", 1),
   ("and its $6 tier at twenty", "and its Professional tier at twenty", 1),
   ("Professional — “$6 per month” or “$72 billed yearly”",
    "Professional — “$8 per month billed monthly”, or “$6 per month” / “$72 billed yearly” with "
    "the page's “Billed yearly” switch on (it is on by default)", 1),
   ("<b>HiHello wins on price, at every tier</b> $6 a month against $9.99 for the first paid "
    "tier, and $5 per user against $6.99 for the team tier. Annual pricing narrows it — $7.33 for "
    "Blinq Premium against HiHello's $72 a year, which is $6 a month — but it does not close it. "
    "HiHello is the cheaper product on its published numbers.",
    "<b>HiHello wins on price for one person; the team tier is a near tie</b> Billed monthly, "
    "HiHello Professional is $8 against Blinq Premium at $9.99; billed yearly it is $6 against "
    "$7.33. For the team tier it is $6 per user against $6.99 billed monthly, but $5 against $4.99 "
    "billed yearly — a cent in Blinq's favour. HiHello is the cheaper product for an individual on "
    "its published numbers; for a team of five or more, the billing term decides it.", 1),
   ("and sixteen at $6 a month against five at $9.99.",
    "and sixteen at $8 a month ($6 billed yearly) against five at $9.99 ($7.33 billed yearly).", 1),
   ("<td>$6/mo (16 cards)</td><td>$9.99/mo (5 cards)</td><td>Pro $7.99/mo, or $5.99/mo billed "
    "annually — <b>more than HiHello</b></td>",
    "<td>$8/mo billed monthly, or $6/mo billed yearly (16 cards)</td><td>$9.99/mo, or $7.33/mo "
    "billed yearly (5 cards)</td><td>Pro $7.99/mo, or $5.99/mo billed yearly — <b>within a cent of "
    "HiHello on either term, for one card instead of sixteen</b></td>", 1),
   ("<td>$5/user/mo</td><td>$6.99/card/mo</td>",
    "<td>$6/user/mo billed monthly, or $5 billed yearly</td><td>$6.99/card/mo, or $4.99 billed "
    "yearly</td>", 1),
   ("HiHello and Blinq are both cheaper than CompanyCard at every paid tier, and both give a "
    "bigger free plan.",
    "HiHello and Blinq are both cheaper than CompanyCard on the team tier, HiHello Professional "
    "is within a cent of CompanyCard Pro on either billing term while including sixteen cards to "
    "our one, and both give a bigger free plan.", 1),
   ("Our per-user rate is $12 a month, which is more than double HiHello's $5 — so two people on "
    "CompanyCard Business pay $24 a month against a five-user HiHello Business floor of $25.",
    "Our per-user rate is $12 a month, double HiHello's $6 billed monthly — so two people on "
    "CompanyCard Business pay $24 a month against a five-user HiHello Business floor of $30 "
    "billed monthly, or $20 against $25 if both are billed yearly.", 1),
   # FAQ — visible + JSON-LD, hence 2 each
   ("On published prices HiHello is cheaper at every tier and gives more cards: 4 free against "
    "Blinq's 2, 16 cards at $6 a month against 5 at $9.99, and $5 per user against $6.99 for teams.",
    "On published prices HiHello is cheaper for one person and gives more cards: 4 free against "
    "Blinq's 2, and 16 cards at $8 a month ($6 billed yearly) against 5 at $9.99 ($7.33 billed "
    "yearly). The team tier is a near tie — $6 per user against $6.99 billed monthly, $5 against "
    "$4.99 billed yearly.", 2),
   ("Professional is $6 per month or $72 billed yearly for 16 cards and 20 scans a month. "
    "Business is $5 per user per month or $60 per user per year with unlimited cards and scans,",
    "Professional is $8 a month billed monthly, or $72 a year ($6 a month) billed yearly, for 16 "
    "cards and 20 scans a month. Business is $6 per user a month billed monthly, or $60 per user a "
    "year ($5 a month) billed yearly, with unlimited cards and scans,", 2),
   ("Pro at $7.99 a month against HiHello's $6, and Business at $12 per user against HiHello's $5 "
    "and Blinq's $6.99.",
    "Pro at $7.99 a month against HiHello's $8 billed monthly ($6 yearly) for one card instead of "
    "sixteen, and Business at $12 per user against HiHello's $6 ($5 yearly) and Blinq's $6.99.", 2),
 ]),
 ("seo/pages_data15.py", [
   ("its first paid tier is $6 a month for sixteen cards against Blinq's \"\n    \"$9.99 for five. "
    "On published price alone HiHello wins at every tier.",
    "its first paid tier is $8 a month billed monthly — $6 a month if you pay $72 for the year — \"\n"
    "    \"for sixteen cards, against Blinq's $9.99 (or $7.33 yearly) for five. On published price "
    "HiHello is cheaper for one person on either billing term; the team tiers are within a dollar "
    "of each other and the billing term decides it.", 1),
   ("and its $6 tier \"\n    \"at twenty", "and its Professional tier \"\n    \"at twenty", 1),
 ]),
 ("digital-business-card-cost.html", [
   ("$5 per user (HiHello, Wave Connect), $6 per user (Uniqode)",
    "$5 per user (Wave Connect), $5–$6 per user (HiHello, yearly or monthly billing), $6 per user "
    "(Uniqode)", 1),
   ("<td>Professional $6/mo, or $72 billed yearly</td><td>Business $5 per user/mo, or $60 per "
    "user/year</td>",
    "<td>Professional $8/mo billed monthly, or $72 a year ($6/mo) billed yearly</td><td>Business "
    "$6 per user/mo billed monthly, or $60 per user/year ($5/mo) billed yearly</td>", 1),
   ("HiHello's and Wave Connect's $5 per user a month are the lowest published rates.",
    "Wave Connect's $5 per user a month and HiHello's $5 per user a month billed yearly ($6 "
    "monthly) are the lowest published rates.", 2),
 ]),
 ("seo/pages_data14.py", [
   ("$5 per user (HiHello, Wave Connect), $6 per user (Uniqode)",
    "$5 per user (Wave Connect), $5–$6 per user (HiHello, yearly or monthly billing), $6 per user "
    "(Uniqode)", 1),
   ("\"Professional $6/mo, or $72 billed yearly\",",
    "\"Professional $8/mo billed monthly, or $72 a year ($6/mo) billed yearly\",", 1),
   ("\"Business $5 per user/mo, or $60 per user/year\",",
    "\"Business $6 per user/mo billed monthly, or $60 per user/year ($5/mo) billed yearly\",", 1),
 ]),
 ("best-digital-business-card.html", [
   ("<td>$6 Professional · $5 per user Business</td>",
    "<td>$6 Professional · $5 per user Business, billed yearly ($8 · $6 billed monthly)</td>", 1),
 ]),
 ("seo/add_vendor_matrix.py", [
   ("\"$6 Professional · $5 per user Business\",",
    "\"$6 Professional · $5 per user Business, billed yearly ($8 · $6 billed monthly)\",", 1),
 ]),
 ("free-digital-business-card-comparison.html", [
   ("<td>$6/mo Professional</td>",
    "<td>$6/mo Professional billed yearly ($8/mo billed monthly)</td>", 1),
 ]),
 ("seo/pages_data4.py", [
   ("\"$6/mo Professional\"]", "\"$6/mo Professional billed yearly ($8/mo billed monthly)\"]", 1),
 ]),
 ("hihello-alternative.html", [
   ("<td>$6 Professional · $5 per user Business</td>",
    "<td>$6 Professional · $5 per user Business, billed yearly ($8 · $6 billed monthly)</td>", 1),
 ]),
 ("seo/pages_data2.py", [
   ("\"$6 Professional · $5 per user Business\", \"$8 Pro · $12 per user Business\"]",
    "\"$6 Professional · $5 per user Business, billed yearly ($8 · $6 billed monthly)\", "
    "\"$7.99 Pro ($5.99/mo billed yearly) · $12 per user Business ($10 billed yearly)\"]", 1),
 ]),
 ("blinq-alternative.html", [
   ("<td>Professional $6/mo</td>", "<td>Professional $8/mo ($6/mo yearly)</td>", 1),
   ("<td>Business $5/user/mo, sold from 5 users</td>",
    "<td>Business $6/user/mo ($5 yearly), sold from 5 users</td>", 1),
 ]),
 ("llms.txt", [
   ("On published prices HiHello is cheaper at every tier (free 4 cards vs 2; $6/mo vs $9.99/mo; "
    "$5/user vs $6.99/card)",
    "On published prices HiHello is cheaper for one person (free 4 cards vs 2; Professional $8/mo "
    "vs Premium $9.99/mo billed monthly, $6 vs $7.33 yearly) and the team tier is a near tie "
    "(HiHello $6/user vs Blinq $6.99/card billed monthly; $5 vs $4.99 yearly)", 1),
   ("CompanyCard's free plan includes a Wallet pass and has no monthly scan cap (HiHello's free "
    "tier caps card and badge scans at 5 per month as of September 2026).",
    "CompanyCard's free plan includes a Wallet pass but no card scanner — lead capture is a Pro "
    "feature (HiHello's free tier includes its scanner, capped at 5 card and badge scans per "
    "month as of September 2026).", 1),
 ]),
]

# pages_data2.py also lists the HiHello/Blinq team row through the same
# generator as blinq-alternative.html; patch it if the exact string is there.
EDITS.append(("seo/pages_data2.py", [
   ("\"Professional $6/mo\"", "\"Professional $8/mo ($6/mo yearly)\"", None),
   ("\"Business $5/user/mo, sold from 5 users\"",
    "\"Business $6/user/mo ($5 yearly), sold from 5 users\"", None),
]))

applied = already = 0
for fn, edits in EDITS:
    s = open(fn, encoding="utf-8").read()
    orig = s
    for old, new, n in edits:
        c = s.count(old)
        if c == 0:
            if s.count(new) >= 1:
                already += 1
                continue
            if n is None:
                continue
            sys.exit("%s: target not found: %r" % (fn, old[:80]))
        if n is not None and c != n:
            sys.exit("%s: expected %d occurrences, found %d: %r" % (fn, n, c, old[:80]))
        s = s.replace(old, new)
        applied += c
    if s != orig:
        open(fn, "w", encoding="utf-8").write(s)
        print("patched", fn)
print("applied %d replacement(s); %d already applied" % (applied, already))
