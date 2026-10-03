#!/usr/bin/env python3
"""Improve digital-business-card-for-realtors.html (2026-10-03). Idempotent.

Why: GSC (3 months to 2026-09-29) — the page draws ~99 impressions at avg
position 74 on "digital business card(s) for realtors" and "digital business
cards for real estate agents" (77). The title already names real estate agents;
the H1 did not, and the page never said what a card does at the open house
beyond "scan the QR", or how a team gets matching cards.

What: (1) H1 names realtors AND real estate agents; (2) one new section,
"Open houses, showings and team cards", built only on facts from seo/facts.py
(lead capture is Pro; Wallet pass is on Free; Business has no seat minimum,
brand and template lock, central admin); (3) two FAQs, visible and in the
FAQPage JSON-LD (sync_faq_schema.py then byte-matches them). No prices are
printed here, so a reprice cannot leave this page stale.

Run from repo root: python3 seo/improve_realtors_2026_10_03.py
"""
import json, re

F = "digital-business-card-for-realtors.html"
s = open(F, encoding="utf-8").read()

OLD_H1 = 'Digital business card for <span class="gradient-text">realtors</span></h1>'
NEW_H1 = ('Digital business card for <span class="gradient-text">realtors &amp; real estate '
          'agents</span></h1>')

SECTION_MARK = "<!-- REALTORS-OPENHOUSE-2026-10 -->"
SECTION = (
    SECTION_MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Open houses, showings and team cards</h2></div>'
    "<p>At an open house the free card does one direction of the exchange: a visitor scans your "
    "QR code and saves your number, listings link and brokerage in one tap, with no app to "
    "install. Add the card to Apple Wallet or Google Wallet as well, which the free plan "
    "includes, and the code is on your lock screen when a visitor asks for your number on the "
    "way out.</p>"
    "<p>The other direction is the sign-in sheet. On Pro, lead capture lets a visitor send their "
    "own name and contact details back from your card, and they are saved in your account "
    "instead of on a clipboard you have to decipher on Monday. Pro also adds analytics and "
    "removes the small CompanyCard credit under the card. If you only need to be saved into "
    "phones, the free plan is enough.</p>"
    "<p>For a team or a small brokerage, the Business plan has no seat minimum, so a two-agent "
    "team pays for two cards. It adds a central admin dashboard and brand and template lock, so "
    "every agent's card carries the same brokerage name and logo, and when the office number "
    "changes it is changed once for everyone. See <a href=\"pricing.html\">pricing</a> for the "
    "current rates.</p></div></section>\n"
)
ANCHOR = '<section class="section" style="background:var(--slate-50);"><div class="container lp-prose"><div class="section-head" style="margin-bottom:24px;"><h2>What changes in a realtor\'s career'

NEW_FAQS = [
    ("Can open-house visitors leave their details on my card?",
     "Yes, on Pro. Lead capture lets a visitor send their name and contact details back from your "
     "card, and they are saved in your account, which replaces the paper sign-in sheet. On the "
     "free plan visitors can save your details in one tap, but the card does not collect theirs."),
    ("Can a real estate team give every agent a matching card?",
     "Yes. The Business plan has no seat minimum, so a two-agent team pays for two cards. It adds "
     "a central admin dashboard and brand and template lock, so every agent's card shows the same "
     "brokerage name and logo, and a change to the office details is made once for the whole team."),
]

changed = []
if OLD_H1 in s:
    s = s.replace(OLD_H1, NEW_H1, 1); changed.append("h1")
assert NEW_H1 in s, "H1 not found"

if SECTION_MARK not in s:
    assert s.count(ANCHOR) == 1, "section anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1); changed.append("section")

def faq_html(q, a):
    esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<details class="lp-faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'

FAQ_END = "</details></div></section>"
faq_sec = re.search(r'<h2>Frequently asked questions from realtors</h2></div>.*?</details></div></section>', s, re.S)
assert faq_sec, "FAQ section not found"
for q, a in NEW_FAQS:
    if f"<summary>{q}</summary>" not in s:
        block = faq_sec.group(0)
        new_block = block[: -len("</div></section>")] + faq_html(q, a) + "</div></section>"
        s = s.replace(block, new_block, 1)
        faq_sec = re.search(r'<h2>Frequently asked questions from realtors</h2></div>.*?</details></div></section>', s, re.S)
        changed.append("faq-visible")

m = re.search(r'<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"FAQPage".*?)</script>', s, re.S)
assert m, "FAQPage JSON-LD not found"
data = json.loads(m.group(1))
names = {q["name"] for q in data["mainEntity"]}
for q, a in NEW_FAQS:
    if q not in names:
        data["mainEntity"].append({"@type": "Question", "name": q,
                                   "acceptedAnswer": {"@type": "Answer", "text": a}})
        changed.append("faq-schema")
new_ld = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
s = s.replace(m.group(1), new_ld, 1)

open(F, "w", encoding="utf-8").write(s)
print("changed:", ", ".join(changed) or "nothing (already applied)")
