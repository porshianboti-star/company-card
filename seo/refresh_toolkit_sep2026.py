#!/usr/bin/env python3
"""
Re-verification of the NON-CARD vendors cited on small-business-toolkit-2027.html,
and the September 2026 date restamp for that page.

The 2026-09-01 run re-verified the eight digital-business-card vendors and left a
standing note: the toolkit page also cites Zoho Invoice, Calendly, Wave Accounting
and Trello, which were NOT re-fetched that day, so the page kept an August 2026
stamp while the rest of the site moved to September. This script closes that gap.

VERIFIED 2026-09-03, each against the vendor's own live pricing page:

  calendly.com/pricing        Free = "One event type"; Standard $10/seat/mo
                              (annual ~$8.40). UNCHANGED.
  waveapps.com/pricing        Starter $0; "Auto-import bank transactions" is a
                              Pro-only feature; Pro $19 USD/mo ($190/yr).
                              UNCHANGED. (A $9.50-for-3-months promo is running;
                              the page states the $19 list price, which is what
                              we quote.)
  zoho.com/invoice/pricing/   Free; 500 invoices/yr; "Add up to two users";
                              "If you're inactive for more than 180 days, your
                              associated data will be deleted within the next 20
                              days."; no paid tier inside Zoho Invoice — Zoho
                              points to Zoho Billing. UNCHANGED.
  trello.com/pricing          "Free for up to 10 collaborators per Workspace";
                              "Up to 10 boards per Workspace"; Standard $5/user/mo
                              annual ($6 monthly). UNCHANGED.
  bitwarden.com/pricing/      Basic password management "Always free"; free tier
                              includes sharing with one other user; Premium $1.65/mo
                              billed annually ($19.80/yr). UNCHANGED.
  canva.com/pricing/          "Canva Free is available to anyone"; Pro US$120/year
                              for one person; footnote confirms "Free includes a
                              shared allowance across Standard and Premium AI only".
                              UNCHANGED. (403s to curl; read in a real browser.)
  hubspot.com/pricing/crm     "Free for up to 2 users. No credit card required.";
                              "You can add 1,000 contacts, and your free access has
                              no time limit."; Starter list price $20/mo/seat.
                              CHANGED ONLY IN DEGREE: the promotional rate is still
                              displayed and is now an explicit $7/mo/seat headline
                              ("Save up to 65% on Starter"). We name it.

  blinq.me/pricing            Re-read today because it sits in the same table:
                              two free cards, "Free forever", Premium $9.99/mo
                              ($7.33 annual), Business $6.99/user ($4.99 annual),
                              "you choose how many cards to start with (minimum of
                              five)". Free plan card lists "Add to Google or Apple
                              Wallet". UNCHANGED — inline stamp moved to 3 Sept.

Every figure on the page therefore still matched. The only substantive edit is the
HubSpot sentence, which now names the promo rate instead of gesturing at it.

Idempotent: re-running makes no further changes.
"""
import re, sys, pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "small-business-toolkit-2027.html"

SUBS = [
    # 1. Method note (visible prose)
    ("checked against the vendor's live pricing page in August 2026.",
     "checked against the vendor's live pricing page in September 2026."),

    # 2. Meta description / og / twitter / WebPage JSON-LD (4 copies, curly apostrophe)
    ("verified against the vendor’s live pricing page, August 2026.",
     "verified against the vendor’s live pricing page, September 2026."),

    # 3. HubSpot prose — name the promotional rate rather than gesturing at it
    ("HubSpot's Starter tier lists at $20/month per seat, though the page was "
     "showing a discounted promotional rate in August 2026 — budget against "
     "the list price.",
     "HubSpot's Starter tier lists at $20/month per seat, though in September 2026 "
     "the page was headlining a promotional rate of $7/month per seat — budget "
     "against the list price, because promotions expire and list prices are what "
     "renew."),

    # 4. Table header
    ("<th>Free tier (verified Aug 2026)</th>",
     "<th>Free tier (verified Sep 2026)</th>"),

    # 5. HubSpot table cell
    ("Starter lists at $20/mo/seat (promo rate seen Aug 2026)",
     "Starter lists at $20/mo/seat ($7 promo rate seen Sep 2026)"),

    # 6. Closing FAQ answer — appears twice: visible <p> and FAQPage JSON-LD.
    ("this article's figures were checked in August 2026.",
     "this article's figures were checked in September 2026."),

    # 7. Blinq inline stamp — re-read today
    ("(checked 1 September 2026)", "(checked 3 September 2026)"),
]


def main():
    s = PAGE.read_text(encoding="utf-8")
    before = s
    total = 0
    for old, new in SUBS:
        n = s.count(old)
        if n == 0 and s.count(new) == 0:
            print(f"  !! NOT FOUND and not already applied: {old[:70]!r}")
            return 1
        if n:
            s = s.replace(old, new)
            total += n
            print(f"  {n}x  {old[:64]!r}")
    if s == before:
        print("No changes (already applied).")
        return 0
    PAGE.write_text(s, encoding="utf-8")
    print(f"\nsmall-business-toolkit-2027.html: {total} replacement(s) written.")

    leftover = re.findall(r"Aug(?:ust)? 2026", s)
    if leftover:
        print(f"  !! {len(leftover)} August-2026 token(s) still on the page")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
