#!/usr/bin/env python3
"""Monthly competitor re-verification pass — August 2026.

Every competitor figure carried on the site was re-read from that vendor's own
pricing page on 2026-08-04 before any stamp was moved from July to August.
Sources fetched this pass:

  blinq.me/pricing        Free = 2 cards, "Add to Google or Apple Wallet",
                          personal email signature, virtual backgrounds.
                          Premium $9.99/mo ($7.33/mo annual). Business $6.99/mo
                          per card ($4.99 annual), "A minimum payment equal to
                          5 Team Cards is required for all Blinq Business
                          subscriptions".
  hihello.com/pricing     Personal free = 4 cards, "5 card & badge scans /mo",
                          email signature, virtual backgrounds, Apple+Google
                          Wallet. Professional $6/mo ($72/yr), 16 cards, 20
                          scans/mo. Business $5/user/mo ($60/user/yr), "5-100
                          users". Enterprise custom, 101+.
  uniqode.com/pricing     "We currently only offer annual subscription plans."
                          "You can create your first digital business card with
                          Uniqode for free. For additional seats, upgrade to the
                          Team plan at $6 per user per month." Free-plan cards
                          "will remain free forever with essential features".
                          30-day money-back guarantee.
  mobilocard.com/pricing-2  Pro $3/mo; Teams $4/mo billed annually; Business
                          $5/mo billed annually. Free digital business card.
                          NFC hardware sold separately, not required.
  wavecnct.com/pages/pricing  Free = digital card, personal email signature,
                          unlimited sharing/contacts, wallet, lead capture form.
                          Pro $7/mo (removes Wave branding). Teams $5/user/mo,
                          "3 minimum seats". NFC sold separately, not required.
  v1ce.co/pricing         No free plan; 30-day trial then a single tier,
                          £49/mo headline, "£49.99/mo after trial". Smart card
                          from £75 one-time, "No subscription required".
  popl.co + popl.co/pages/pricing  No free plan, no published prices — "Popl
                          pricing is customized for your exact needs". Homepage
                          H1 still "Your AI GTM platform for in-person events".

CORRECTION SHIPPED THIS PASS — Uniqode's "2-seat minimum".
Pages claimed Uniqode's Team plan "requires at least two seats". That figure is
NOT published on uniqode.com/pricing as of 2026-08-04 (checked for "2 seats",
"two seats", "seat minimum", "minimum of N" — zero matches). It may still be
true, but we cannot verify it, so it comes off every page. What IS verifiable
and still differentiating: Uniqode sells annual subscriptions only, and our own
no-seat-minimum is a fact about us. Second instance of the rule that competitor
facts go stale and must be re-fetched, not restated.

DELIBERATELY NOT STATED (could not verify today):
  - Whether Blinq's or HiHello's free cards carry a vendor branding line
    (neither pricing page lists one either way) -> "None listed", not "None".
  - Wave Connect's free card count (page says "digital business card", no
    number) -> "count not stated".
  - Whether V1CE's £49.99 subscription can be bought without a card.

Run from repo root: python3 seo/refresh_verified_aug2026.py
Then: python3 seo/sync_faq_schema.py && python3 seo/add_freshness.py
"""
import sys

EDITS = []


def edit(fn, old, new, n=1):
    EDITS.append((fn, old, new, n))


# ---------------------------------------------------------------- comparison
F = "free-digital-business-card-comparison.html"

# Blinq: Google Wallet is on the free plan too, and no scan cap is listed.
edit(F,
     '<tr><td><b>Blinq</b></td><td>2</td><td>Apple Wallet</td>'
     '<td><span style="color:var(--slate-500)">not stated</span></td>'
     '<td>None listed</td><td>5 team cards</td><td>$9.99/mo Premium</td></tr>',
     '<tr><td><b>Blinq</b></td><td>2</td><td>Apple &amp; Google</td>'
     '<td>None listed</td>'
     '<td>None listed</td><td>5 team cards</td><td>$9.99/mo Premium</td></tr>')

# Uniqode: drop the unverifiable 2-seat minimum, keep the verified annual-only.
edit(F,
     '<td>2 seats, annual only</td><td>$6/user/mo (annual)</td>',
     '<td>Annual billing only; seat minimum '
     '<span style="color:var(--slate-500)">not stated</span></td>'
     '<td>$6/user/mo (annual)</td>')

# New vendor row: Wave Connect (verified today, and it carries a real 3-seat floor).
edit(F,
     '<tr><td><b>Popl</b></td><td>No free plan</td>',
     '<tr><td><b>Wave Connect</b></td>'
     '<td>Card included; count <span style="color:var(--slate-500)">not stated</span></td>'
     '<td>Yes</td><td>None listed</td><td>Yes — Pro removes it</td>'
     '<td>3 seats (Teams)</td><td>$7/mo Pro</td></tr>'
     '<tr><td><b>Popl</b></td><td>No free plan</td>')

edit(F, 'Verified July 2026 from:', 'Verified August 2026 from:')
edit(F, 'https://www.mobilocard.com/pricing"', 'https://www.mobilocard.com/pricing-2"')
edit(F,
     ' · <a href="https://popl.co/pages/pricing"',
     ' · <a href="https://www.wavecnct.com/pages/pricing" target="_blank" '
     'rel="noopener nofollow">wavecnct.com</a>'
     ' · <a href="https://popl.co/pages/pricing"')

edit(F,
     "Blinq bills a minimum of five team cards, HiHello sells Business for five "
     "or more users, and Uniqode's Team plan needs two seats and an annual "
     "commitment.",
     "Blinq bills a minimum of five team cards, HiHello sells Business for five "
     "or more users, and Wave Connect's Teams plan starts at three seats. "
     "Uniqode does not publish a seat minimum, but it sells annual "
     "subscriptions only, so the commitment there is a year rather than a month.")

edit(F,
     'both without a branding line — as of July 2026.',
     'both without a listed branding line — as of August 2026.', n=-1)

edit(F,
     "On published rates as of July 2026, Mobilo is the cheapest of the tools "
     "here at $3 a month for Pro, though it is built around NFC cards it sells "
     "separately. Uniqode's Team plan is $6 per user per month but is "
     "annual-only with a two-seat minimum.",
     "On published rates as of August 2026, Mobilo is the cheapest of the tools "
     "here at $3 a month for Pro, though it is built around NFC cards it sells "
     "separately. Wave Connect's Pro is $7 a month. Uniqode's Team plan is $6 "
     "per user per month but is annual-only — it states plainly that it does "
     "not offer monthly plans.", n=-1)

edit(F,
     "As of July 2026 Blinq's Business plan bills a minimum of five team cards, "
     "HiHello's Business plan is sold for five to one hundred users, and "
     "Uniqode's Team plan requires at least two seats and annual billing. "
     "CompanyCard and Mobilo do not state a seat minimum.",
     "As of August 2026 Blinq's Business plan bills a minimum of five team "
     "cards, HiHello's Business plan is sold for five to one hundred users, and "
     "Wave Connect's Teams plan starts at three seats. Uniqode publishes no "
     "seat minimum but sells annual subscriptions only. CompanyCard and Mobilo "
     "do not state a seat minimum.", n=-1)

edit(F, "pricing page in July 2026", "pricing page in August 2026", n=-1)

# --------------------------------------------------------------- best-of page
B = "best-digital-business-card.html"
edit(B, 'Last updated: July 2026', 'Last updated: August 2026')
edit(B, 'verified in July 2026', 'verified in August 2026')
edit(B, 'Sources, verified July 2026:', 'Sources, verified August 2026:')
edit(B,
     '<td>2 cards, email signature, virtual background, Apple Wallet</td>',
     '<td>2 cards, email signature, virtual background, Apple &amp; Google Wallet</td>')

# ------------------------------------------------------- uniqode-alternative
U = "uniqode-alternative.html"
edit(U,
     'Uniqode Alternative — No Annual Lock-In or Seat Minimum | CompanyCard',
     'Uniqode Alternative — Monthly Billing, No Annual Lock-In | CompanyCard',
     n=-1)  # <title>, og:title, twitter:title, JSON-LD
edit(U,
     'A Uniqode alternative for small teams: monthly billing rather than '
     'annual-only, and no two-seat minimum. Compared from Uniqode&#x27;s own '
     'pricing page, verified July 2026.',
     'A Uniqode alternative for small teams: monthly billing rather than '
     'Uniqode&#x27;s annual-only subscriptions, and no seat minimum on our '
     'side. Compared from Uniqode&#x27;s own pricing page, verified August 2026.')
edit(U,
     'Uniqode alternative — monthly billing instead of annual-only, and no '
     '2-seat minimum.',
     'Uniqode alternative — monthly billing instead of annual-only, and no '
     'seat minimum on our side.',
     n=2)  # og:description, twitter:description
edit(U,
     "Uniqode's paid plans are annual-only and start at two seats. If you'd "
     "rather pay monthly, or you're a single person who doesn't need a second "
     "seat, that's the gap CompanyCard fills.",
     "Uniqode sells annual subscriptions only — it states plainly that it does "
     "not offer monthly plans. If you'd rather pay month to month, or test "
     "something before committing a year of budget, that's the gap CompanyCard "
     "fills.")
edit(U,
     "one card for a single user, free forever as of July 2026",
     "your first card, free forever, as of August 2026")
edit(U,
     "The friction people run into is commercial rather than functional. "
     "Uniqode states plainly that it does not offer monthly plans: paid "
     "subscriptions are annual, and its Team plan starts at two seats. If you "
     "are a sole trader, or a business that would rather test something for a "
     "month before committing a year of budget, that is the decision point.",
     "The friction people run into is commercial rather than functional. "
     "Uniqode states plainly that it does not offer monthly plans: paid "
     "subscriptions are annual, and a second card means moving to the Team "
     "plan at $6 per user per month. If you are a sole trader, or a business "
     "that would rather test something for a month before committing a year of "
     "budget, that is the decision point.")
edit(U,
     '<td><b>Team seat minimum</b></td><td>2 seats on Team</td><td>None</td>',
     '<td><b>Team seat minimum</b></td><td>Not published</td><td>None</td>')
edit(U,
     '<td>1 card, single user, free forever</td>',
     '<td>First card free, free forever</td>')
edit(U,
     "The two structural reasons are billing and seats. As of July 2026 "
     "Uniqode states it does not offer monthly plans — paid subscriptions are "
     "annual only — and its Team plan requires at least two seats. For a solo "
     "professional or a business that wants to pay month to month, that is a "
     "commitment decision before it is a product decision.",
     "Billing terms. As of August 2026 Uniqode states it does not offer "
     "monthly plans — paid subscriptions are annual only — and a second card "
     "means upgrading to its Team plan at $6 per user per month. For a solo "
     "professional or a business that wants to pay month to month, that is a "
     "commitment decision before it is a product decision.", n=-1)
edit(U,
     "Yes. As of July 2026 Uniqode lets you create one digital business card "
     "free, for a single user, and states cards created on the free plan "
     "remain free forever.",
     "Yes. As of August 2026 Uniqode lets you create your first digital "
     "business card free, and states cards created on the free plan remain "
     "free forever with essential features.", n=-1)

# ------------------------------------------- pages whose figures all re-verify
V = "v1ce-alternative.html"
edit(V, 'https://v1ce.co/pages/pricing', 'https://v1ce.co/pricing', n=-1)
edit(V, 'v1ce.co/pages/pricing', 'v1ce.co/pricing', n=-1)

for fn in [V, "wave-connect-alternative.html", "hihello-alternative.html",
           "popl-alternative.html", "best-virtual-business-card.html"]:
    edit(fn, "July 2026", "August 2026", n=-1)  # -1 = replace all


def main():
    from collections import defaultdict
    by_file = defaultdict(list)
    for fn, old, new, n in EDITS:
        by_file[fn].append((old, new, n))
    failures = []
    for fn, edits in by_file.items():
        h = open(fn, encoding="utf-8").read()
        orig = h
        for old, new, n in edits:
            found = h.count(old)
            if n == -1:
                if found == 0:
                    failures.append(f"{fn}: no match for {old[:70]!r}")
                    continue
                h = h.replace(old, new)
            else:
                if found != n:
                    failures.append(
                        f"{fn}: expected {n} match(es) for {old[:70]!r}, found {found}")
                    continue
                h = h.replace(old, new, n)
        if h != orig:
            open(fn, "w", encoding="utf-8").write(h)
            print(f"  patched {fn}")
    if failures:
        print("\nFAILED:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("\nAll replacements applied.")


# NOTE: run as two passes, in order — main() then main2(). Neither is
# idempotent (they assert on exact match counts), so this file is a record of
# what was changed, not a re-runnable migration.


# --------------------------------------------------------------- second pass
# Added after the first run surfaced more July stamps. Each vendor below was
# re-verified on 2026-08-04 in the same sweep documented above; linqapp.com was
# re-fetched this pass and still leads with "APIs for iMessage, RCS, SMS, and
# Voice built for Agents" — no digital business card product. Mobilo's list
# prices ($19.99 branded / $39 custom / $139 metal, discounted at the time of
# checking) were re-read from mobilocard.com and still match.
#
# Also fixes a stray ">" that was closing the meta description on
# best-digital-business-card.html and rendering as a visible ">" above the
# nav — the same typo class already fixed once on index.html.
EDITS2 = []


def edit2(fn, old, new, n=1):
    EDITS2.append((fn, old, new, n))


edit2("best-digital-business-card.html",
      "cited and verified July 2026.\">>",
      "cited and verified August 2026.\">")
edit2("free-digital-business-card-comparison.html",
      "own pricing page and verified July 2026.",
      "own pricing page and verified August 2026.")
for fn in ["blinq-alternative.html", "mobilo-alternative.html",
           "linq-alternative.html",
           "digital-business-card-for-small-business.html"]:
    edit2(fn, "July 2026", "August 2026", n=-1)


def main2():
    EDITS.clear()
    EDITS.extend(EDITS2)
    main()


if __name__ == "__main__":
    main()   # first pass
    main2()  # second pass
