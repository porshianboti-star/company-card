#!/usr/bin/env python3
"""
Correction of two WRONG third-party claims on small-business-toolkit-2027.html.

Both were introduced (or left standing) by seo/refresh_toolkit_sep2026.py on
2026-09-03, which recorded each vendor as "UNCHANGED". The prices it read were
real; the QUALIFIERS attached to them were not. A price-diff cannot catch this,
because the number on our page still appears on the vendor's page.

RE-VERIFIED 2026-09-08 against each vendor's own live pricing page:

  calendly.com/pricing  -- WRONG ON OUR PAGE.
      The pricing table defaults to the "Billed yearly" toggle, so the $10 that
      renders next to Standard is the ANNUAL rate, not the monthly one. The
      page's own embedded price data is unambiguous:

          "featuresLeadIn":"Everything in Free, and:"        <- Standard
          "USD":{"monthly":"$12","annual":"$10","annualSavingsPercentage":17}

      and 12 x (1 - 0.17) = 9.96 ~= 10, which is consistent. Teams is
      monthly $20 / annual $16.
      Our page said "the Standard plan is $10 per seat per month billed
      monthly" -- wrong qualifier, and it understates the monthly price by $2.
      The 09-03 script compounded this by deriving a phantom "annual ~$8.40"
      (a 16% discount applied to a number that was already the annual rate).
      Free tier re-confirmed: "Always free", "One event type",
      "One calendar connection".

  bitwarden.com/pricing/  -- WRONG ON OUR PAGE.
      The Personal panel lists "Share vault items with one other user" inside
      the PREMIUM feature list ("Enjoy premium features ... Share vault items
      with one other user"). The free tier is described only as "Just getting
      started? Get basic password management today. Always free." Bitwarden's
      sharing comparison says the same: "Premium -- Share items with one other
      existing Bitwarden user by creating a Free organization."
      Our page put that sharing capability in the FREE column.
      Price re-confirmed: Premium "$1.65 per month / Billed annually at $19.80".

Re-verified and UNCHANGED (no edit needed), same date, same method:

  trello.com/pricing    "Free for up to 10 collaborators per Workspace";
                        "Up to 10 boards per Workspace"; Standard "$5 USD
                        Per user/month if billed annually ($6 billed monthly)".
  waveapps.com/pricing  "STARTER Plan ... $0"; "Auto-import bank transactions"
                        appears only under "Everything in Starter, plus...";
                        Pro "$19 USD/month Billed monthly" ($190 USD/year).
                        A "$19 -> $9.50 first 3 months" promo is running; we
                        quote the list price, which is what renews.
  zoho.com/us/invoice/pricing/
                        "$0 ... forever-free"; "Add up to two users. Create a
                        maximum of three projects. Send up to 500 invoices per
                        year."; "if a user is inactive for over 180 days, their
                        associated data will be deleted in the subsequent 20
                        days"; no paid tier inside Zoho Invoice -- "Looking for
                        an advanced solution ... Explore Zoho Billing".

NOT re-fetched today (canva.com and hubspot.com both 403 / JS-gate curl): the
Canva and HubSpot rows are untouched and keep the 2026-09-03 reading. The
table's "verified Sep 2026" stamp stays literally true for every row.

Idempotent: re-running makes no further changes.
"""
import pathlib, sys

PAGE = pathlib.Path(__file__).resolve().parent.parent / "small-business-toolkit-2027.html"

SUBS = [
    # --- Calendly: prose ---
    ("When you need multiple event types, the Standard plan is $10 per seat per month billed monthly.",
     "When you need multiple event types, the Standard plan is $12 per seat per month billed monthly, "
     "or $10 per seat per month if you pay for the year up front."),

    # --- Calendly: comparison table ---
    ("<tr><td>Calendly</td><td>Scheduling</td><td>Free; one event type</td>"
     "<td>Standard $10/seat/mo</td></tr>",
     "<tr><td>Calendly</td><td>Scheduling</td><td>Free; one event type</td>"
     "<td>Standard $12/seat/mo ($10 annual)</td></tr>"),

    # --- Bitwarden: prose ---
    ("'s basic password management is always free, and the free tier includes sharing with one "
     "other user — enough for a two-person business to share the bank login and the social "
     "accounts safely. Premium is $1.65 per month billed annually, which is likely the smallest "
     "line item in your entire 2027 budget.",
     "'s basic password management is always free. Sharing a vault item with one other person "
     "— enough for a two-person business to share the bank login and the social accounts "
     "safely — is listed under Premium, not the free tier. Premium is $1.65 per month "
     "billed annually ($19.80 for the year), which is likely the smallest line item in your "
     "entire 2027 budget."),

    # --- Bitwarden: comparison table ---
    ("<tr><td>Bitwarden</td><td>Passwords</td><td>Free; share with one other user</td>"
     "<td>Premium $1.65/mo (annual)</td></tr>",
     "<tr><td>Bitwarden</td><td>Passwords</td><td>Free; basic password management</td>"
     "<td>Premium $1.65/mo billed annually ($19.80/yr); adds sharing with one other user</td></tr>"),

    # --- date stamp: this page only (add_freshness.py still hardcodes 2026-08-02
    #     and would roll every page BACKWARD, so it is deliberately not run) ---
    ('"dateModified": "2026-09-03"', '"dateModified": "2026-09-08"'),
]

def main():
    s = PAGE.read_text(encoding="utf-8")
    orig = s
    missing = []
    for old, new in SUBS:
        if old in s:
            s = s.replace(old, new)
        elif new not in s:
            missing.append(old[:70])
    if missing:
        print("ABORT - these anchors matched neither the old nor the new text:")
        for m in missing:
            print("   ", m)
        return 1
    if s != orig:
        PAGE.write_text(s, encoding="utf-8")
        print(f"patched {PAGE.name}")
    else:
        print(f"{PAGE.name} already correct (idempotent no-op)")
    return 0

sys.exit(main())
