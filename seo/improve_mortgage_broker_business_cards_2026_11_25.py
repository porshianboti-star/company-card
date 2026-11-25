#!/usr/bin/env python3
"""Improve digital-business-card-for-mortgage-brokers.html for "mortgage broker business cards" (2026-11-25). Idempotent.

Why: GSC 28 days to 11-23 shows "mortgage broker business cards" 9 impressions
@ 31.2, "mortgage broker business card" 6 @ 22.8, "mortgage business cards"
6 @ 38.7, "mortgage agent business card" 4 @ 30.0, "mortgage loan officer
business cards" 1 @ 33.0 (26 impressions, the baseline for the next read). The
title says "Digital Business Card for Mortgage Brokers & Loan Officers" and
never "mortgage broker business cards", and the page never covers the printed
card a broker still hands out. Page content untouched since 2026-08-02.

What: same shape as seo/improve_accountant_business_cards_2026_11_21.py.
(1) title / og / twitter / WebPage name -> "Mortgage Broker Business Cards:
Digital Business Card for Mortgage Brokers & Loan Officers" (keeps the old
title; H1 unchanged); description leads with mortgage broker business cards;
(2) one new section "Mortgage broker business cards, printed and digital"
before "Setting up a mortgage broker's card", with a by-format table; (3) two
FAQs, visible + FAQPage JSON-LD, then sync_faq_schema.py; (4) dateModified +
sitemap lastmod; llms.txt.

Facts: plan facts from seo/facts.py only (Free = one card, small clickable
CompanyCard credit, QR + link, unlimited edits; Pro $4.99 / $3.99 yearly adds
custom branding, lead capture, analytics, removes the credit). CompanyCard
does not print cards. New text does NOT mention the Wallet pass (owner decision
pending since 2026-10-29). No new regulatory rule: the page's existing
regulator section is linked, not extended, and every licence / disclosure
statement stays a "check your regulator" pointer. No rate, no statistic, no
competitor.
"""
import json
import re

DATE = "2026-11-25"
F = "digital-business-card-for-mortgage-brokers.html"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "Digital Business Card for Mortgage Brokers &amp; Loan Officers | CompanyCard"
NEW_T = "Mortgage Broker Business Cards: Digital Business Card for Mortgage Brokers &amp; Loan Officers | CompanyCard"
if NEW_T not in s and OLD_T in s:
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
# JSON-LD name may use a raw "&"
OLD_TJ = "Digital Business Card for Mortgage Brokers & Loan Officers | CompanyCard"
NEW_TJ = "Mortgage Broker Business Cards: Digital Business Card for Mortgage Brokers & Loan Officers | CompanyCard"
if NEW_TJ not in s and OLD_TJ in s:
    s = s.replace(OLD_TJ, NEW_TJ)
    changed.append("title-json")

OLD_D = "A digital business card for mortgage brokers and loan officers"
NEW_D = "Mortgage broker business cards that stay current: a digital business card for mortgage brokers and loan officers"
if NEW_D not in s:
    n = s.count(OLD_D)
    assert n >= 1, "description start not found"
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

MARK = "<!-- MORTGAGE-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Setting up a mortgage broker\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Mortgage broker business cards, printed and digital</h2></div>'
    "<p>Most mortgage brokers and loan officers still carry printed business cards: a stack on the "
    "estate agent's counter, a few handed out at a first-time-buyer evening, one clipped to a "
    "decision-in-principle letter. The trouble is what is printed on them. The firm or network you sit "
    "under, your application link, the borrowers you are taking and the hours you answer all change, "
    "and a box of cards does not. A CompanyCard gives every printed mortgage broker business card a QR "
    "code that opens your live digital card, so the paper can stay short and the details that change "
    "live in one place you can edit. CompanyCard does not print cards; you add the QR code from your "
    "card to whatever you have printed.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Where it goes</th><th>What to put on it</th></tr></thead><tbody>"
    "<tr><td><b>Printed mortgage broker business card</b></td><td>Your name, the firm, the licence or "
    "registration details your regulator expects on marketing, a direct mobile and the QR code. Leave "
    "the borrowers you take, your hours and the application link to the digital card the code opens.</td></tr>"
    "<tr><td><b>Leaflet or card holder on an estate agent's counter</b></td><td>The same QR code, so a "
    "buyer who picks one up after a viewing lands on your current card and can book a first call "
    "from the car.</td></tr>"
    "<tr><td><b>Link texted by a referring agent or accountant</b></td><td>The full card: the situations "
    "you handle, your fee position, a booking link, a document upload link and the direct line for "
    "agents.</td></tr>"
    "<tr><td><b>Email signature and client letters</b></td><td>The card link under your name on every "
    "progress update, and the QR code in the footer of letters, so each forwarded message carries "
    "your current details.</td></tr>"
    "</tbody></table>"
    "<p>A printed card is marketing material, so what has to appear on it (licence numbers, the firm's "
    "legal name, a status line) is set by your own regulator; see "
    "<a href=\"#mortgage-rules\">regulator rules on licence numbers, rates and marketing</a> above and "
    "ask your compliance officer before printing. One card is all a sole broker needs, and the free "
    "plan covers it; it carries a small CompanyCard credit under the card. Pro is $4.99 a month, or "
    "$3.99 a month billed yearly, adds custom branding, lead capture and analytics, and removes the "
    "credit. A brokerage with several advisers can give each person a card; see "
    "<a href=\"pricing.html\">pricing</a> or the <a href=\"qr-code-business-card.html\">QR code business "
    "card</a> guide.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

if 'id="mortgage-rules"' not in s:
    s, n = re.subn(r"<h2>(Regulator rules on licence numbers, rates and marketing for mortgage brokers)",
                   r'<h2 id="mortgage-rules">\1', s)
    assert n == 1, "regulator heading not found once"
    changed.append("anchor-id")

NEW_FAQS = [
    ("What should a mortgage broker business card say?",
     "Your name, your firm, the licence or registration details your regulator expects on marketing, a "
     "direct mobile and a QR code. Details that change, such as the borrowers you are taking, the hours "
     "you answer, your application link and the network you sit under, are better kept on the digital "
     "card the QR code opens, so a card printed today is still right after you change firms. Leave "
     "rates off, and check your regulator's disclosure rules before printing."),
    ("Do mortgage brokers still need printed business cards if they have a digital one?",
     "Many still leave them on estate agents' counters and hand them out at first-time-buyer evenings. "
     "The two work together: have a short card printed with the QR code from your CompanyCard on it, "
     "and the code opens your current firm details, the borrowers you help and your booking link. When "
     "those change you edit the digital card once and every printed card already handed out shows the "
     "update. CompanyCard does not print cards."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions from mortgage brokers</h2>"
i = s.find(FAQ_H2)
assert i != -1, "FAQ section not found"
j = s.find("</section>", i)
assert s[j - len("</details></div>"):j] == "</details></div>", "unexpected FAQ section ending: " + s[j-60:j]
for q, a in NEW_FAQS:
    if f"<summary>{esc(q)}</summary>" in s:
        continue
    blk = f'<details class="lp-faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
    s = s[:j - len("</div>")] + blk + s[j - len("</div>"):]
    j = s.find("</section>", i)
    changed.append("faq")

ld = re.search(r'<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"FAQPage".*?)</script>', s, re.S)
assert ld, "FAQPage JSON-LD not found"
data = json.loads(ld.group(1))
names = {q["name"] for q in data["mainEntity"]}
for q, a in NEW_FAQS:
    if q not in names:
        data["mainEntity"].append({"@type": "Question", "name": q,
                                   "acceptedAnswer": {"@type": "Answer", "text": a}})
        changed.append("faq-schema")
s = s.replace(ld.group(1), json.dumps(data, ensure_ascii=False, separators=(",", ":")), 1)

m = re.search(r'("dateModified":")(\d{4}-\d{2}-\d{2})(")', s)
assert m and s.count('"dateModified"') == 1, "WebPage dateModified not found once"
if m.group(2) != DATE:
    s = s[:m.start(2)] + DATE + s[m.end(2):]
    changed.append("dateModified")

open(F, "w", encoding="utf-8").write(s)

sm = open("sitemap.xml", encoding="utf-8").read()
pat = re.compile(r'(<loc>https://company-card\.com/' + re.escape(F) + r'</loc><lastmod>)(\d{4}-\d{2}-\d{2})')
mm = pat.search(sm)
assert mm, "sitemap entry not found"
if mm.group(2) != DATE:
    sm = pat.sub(r'\g<1>' + DATE, sm, count=1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    changed.append("sitemap-lastmod")

ll = open("llms.txt", encoding="utf-8").read()
OLD_L = "- Digital business card for mortgage brokers & loan officers: https://company-card.com/" + F
NEW_L = ("- Mortgage broker business cards: digital business card for mortgage brokers & loan officers "
         "(licence details, borrowers you help, fee position, referring estate agents, QR code for printed "
         "mortgage broker business cards): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
