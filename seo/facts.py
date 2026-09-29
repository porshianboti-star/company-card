#!/usr/bin/env python3
"""The one voice: every CompanyCard product fact, stated once.

Every figure here was read from pricing.html (the visible plan cards, the
Pricing FAQ and the OFFERS JSON-LD) on VERIFIED_DATE. Prices changed on
2026-09-29 (owner decision; seo/reprice_2026_09_29.py): Pro $4.99 monthly /
$3.99 yearly, Business $4.99 / $3.99 per user. Business is "Everything in Pro,
plus ...", so its per-seat price must never be below Pro's (the first version
of the change had Pro at $5.99 / $4.99, above Business; fixed the same day). add_verified_facts.py
prints these constants into pages, build_llms_full.py prints them into
llms-full.txt, and the FAQ answers hand-edited on the same day quote the same
sentences — so an assistant that reads two of our pages cannot find two
numbers. Change a fact here and re-run both scripts; never edit a printed copy.

Sources for the two non-pricing facts:
- "no scan cap": free-digital-business-card-comparison.html (visible + FAQ).
- the credit is a link under the card: app/card-view.js (card page button
  "Make your own CompanyCard" → company-card.com/app/builder.html) and
  app/product.js (embed credit "Made with CompanyCard" → company-card.com).
  Two surfaces, two labels, so the pages describe it as a clickable credit
  rather than quoting one label.
"""

VERIFIED_DATE = "2026-09-29"
VERIFIED_HUMAN = "29 September 2026"

PLANS = [
    # name, monthly, yearly, seats, includes/limits
    ("Free", "$0", "$0", "1 person",
     "One digital business card, QR code and sharing link, profile, links and "
     "socials, Apple and Google Wallet pass, unlimited edits, no scan cap, no "
     "credit card. Carries a small clickable CompanyCard credit under the card."),
    ("Pro", "$4.99", "$3.99 a month ($47.88 a year)", "1 person",
     "Everything in Free, plus unlimited links and files, custom branding and "
     "themes, lead capture and analytics. Removes the CompanyCard credit."),
    ("Business", "$4.99 per user", "$3.99 per user", "No seat minimum",
     "Everything in Pro, plus central admin dashboard, brand and template "
     "lock, CRM sync and team analytics, SSO and priority support. Bought by "
     "contacting us (“Talk to us about teams”), not self-serve."),
    ("Enterprise", "Custom", "Custom", "Custom",
     "Everything in Business, plus SCIM provisioning and SAML, audit logs and "
     "data residency, a dedicated success manager, SLA and invoicing."),
]

def _usd(s):
    import re as _re
    return float(_re.search(r"\$([\d.]+)", s).group(1))


_P = {p[0]: p for p in PLANS}
# Business is "Everything in Pro, plus ..." with no seat minimum: one person can
# buy one seat. Its per-seat price must never be below Pro on either term.
assert _usd(_P["Business"][1]) >= _usd(_P["Pro"][1]), "plan ladder: Business monthly per seat below Pro"
assert _usd(_P["Business"][2]) >= _usd(_P["Pro"][2]), "plan ladder: Business yearly per seat below Pro"

# No billing-status sentence is printed next to prices. Until 2026-09-29 a
# BILLING_NOTE constant here added a "billing not yet live, plans in preview,
# no charge" caveat to every facts paragraph, the pricing-table note and
# llms-full.txt; the owner had it removed on 2026-09-29
# (seo/remove_billing_preview_note_2026_09_29.py). Do not re-add one.

# The compact, quotable paragraph. Identical on every page that carries it.
FACTS_PARAGRAPH = (
    f"<b>CompanyCard facts, verified {VERIFIED_HUMAN} from our "
    f"<a href=\"pricing.html\">pricing page</a> (prices in US dollars):</b> "
    "the free plan is $0 forever and includes one digital business card, a QR "
    "code and sharing link, your profile, links and socials, an Apple and "
    "Google Wallet pass and unlimited edits, with no scan cap and no credit "
    "card; free cards carry a small clickable CompanyCard credit under the "
    "card. Pro is $4.99 a month, or $3.99 a month billed yearly ($47.88 a "
    "year), and removes the credit while adding custom branding, unlimited "
    "links and files, lead capture and analytics. Business is $4.99 per user a "
    "month, or $3.99 per user a month billed yearly, with no seat minimum. "
    "The person receiving a card needs no app — it opens in any browser "
    "with a one-tap Save contact button."
)

# Plain-text twin of FACTS_PARAGRAPH for llms-full.txt (no markup).
FACTS_PLAIN = (
    f"CompanyCard facts, verified {VERIFIED_HUMAN} from "
    "https://company-card.com/pricing.html (prices in US dollars): "
    "the free plan is $0 forever and includes one digital business card, a QR "
    "code and sharing link, your profile, links and socials, an Apple and "
    "Google Wallet pass and unlimited edits, with no scan cap and no credit "
    "card; free cards carry a small clickable CompanyCard credit under the "
    "card. Pro is $4.99 a month, or $3.99 a month billed yearly ($47.88 a "
    "year), and removes the credit while adding custom branding, unlimited "
    "links and files, lead capture and analytics. Business is $4.99 per user a "
    "month, or $3.99 per user a month billed yearly, with no seat minimum. "
    "The person receiving a card needs no app — it opens in any browser "
    "with a one-tap Save contact button."
)

# Page-specific quotable openers (first paragraph under the H1). Same numbers.
LEAD_PRICING = (
    "CompanyCard is free for one digital business card — $0 forever, no "
    "credit card, with a small clickable CompanyCard credit under the card. Pro "
    "is $4.99 a month, or $3.99 a month billed yearly ($47.88 a year), and "
    "removes the credit. Business is $4.99 per user a month, or $3.99 per user a "
    "month billed yearly, with no seat minimum. Prices in US dollars, verified "
    f"{VERIFIED_HUMAN}."
)
LEAD_QR = (
    "A QR code business card is a QR code that opens your live digital business "
    "card, so whoever scans it sees your details and saves them in one tap. With "
    "CompanyCard the QR code, sharing link and Apple and Google Wallet pass are "
    "included on the free plan ($0 forever, one card, with a small clickable "
    "CompanyCard credit under the card); a branded QR code with your logo and "
    "colours is part of Pro at $4.99 a month, or $3.99 a month billed yearly."
)
LEAD_DBC = (
    "A digital business card is an online profile that replaces the paper card: "
    "you share a link or QR code and your full contact details, photo and links "
    "land in the other person’s phone with a one-tap save — no app on "
    "their side. CompanyCard’s free plan is $0 forever for one card, with a "
    "QR code, sharing link and Apple and Google Wallet pass, and a small "
    "clickable CompanyCard credit under the card; Pro at $4.99 a month, or "
    "$3.99 a month billed yearly, removes it."
)

UPDATED_LINE = (
    f"<p style=\"margin:14px auto 0;color:var(--slate-500);font-size:.88rem;"
    f"text-align:center\">Last updated: {VERIFIED_HUMAN}</p>"
)


def facts_table_html():
    rows = "".join(
        f"<tr><td><b>{n}</b></td><td>{m}</td><td>{y}</td><td>{s}</td><td>{d}</td></tr>"
        for n, m, y, s, d in PLANS
    )
    return (
        '<style>.cc-facts{max-width:960px;margin:0 auto;overflow-x:auto}'
        '.cc-facts table{width:100%;border-collapse:collapse;background:#fff;'
        'border:1px solid var(--slate-200);border-radius:14px;overflow:hidden}'
        '.cc-facts th,.cc-facts td{padding:12px 14px;text-align:left;vertical-align:top;'
        'border-bottom:1px solid var(--slate-200);font-size:.95rem;line-height:1.5}'
        '.cc-facts th{background:var(--slate-50);font-weight:700;color:var(--ink)}'
        '.cc-facts td{color:var(--slate-600)}.cc-facts tr:last-child td{border-bottom:none}'
        '.cc-facts-note{max-width:960px;margin:14px auto 0;color:var(--slate-500);font-size:.88rem;text-align:center}</style>'
        '<div class="cc-facts"><table>'
        '<thead><tr><th>Plan</th><th>Billed monthly</th><th>Billed yearly</th>'
        '<th>Seats</th><th>What it includes, and its limits</th></tr></thead>'
        f'<tbody>{rows}</tbody></table></div>'
        f'<p class="cc-facts-note">Figures read from the plan cards on this page on '
        f'{VERIFIED_HUMAN}; the SoftwareApplication offers in this page’s structured data carry the same numbers.</p>'
    )


def facts_table_plain():
    out = []
    for n, m, y, s, d in PLANS:
        out.append(f"- {n}: {m} billed monthly; {y} billed yearly; seats: {s}. {d}")
    return "\n".join(out)
