#!/usr/bin/env python3
"""Improve digital-business-card-for-accountants.html for "accountant business cards" (2026-11-21). Idempotent.

Why: GSC 28 days to 11-19 shows "accountant business cards" 10 impressions @ 21.5
(the nearest profession query to page 2 not yet worked). The page title says
"Digital Business Card for Accountants & Bookkeepers" and never "accountant
business cards", and the page never covers the printed card an accountant
still hands out. Page untouched since 2026-09-25.

What: same shape as seo/improve_personal_trainer_business_cards_2026_11_19.py.
(1) title / og / twitter / WebPage name -> "Accountant Business Cards: Digital
Business Card for Accountants & Bookkeepers" (keeps the old title; H1
unchanged); description leads with accountant business cards; (2) one new
section "Accountant business cards, printed and digital" before "Setting up an
accountant's card", with a by-format table; (3) two FAQs, visible + FAQPage
JSON-LD, then sync_faq_schema.py; (4) dateModified + sitemap lastmod; llms.txt.

Facts: plan facts from seo/facts.py only (Free = one card, small clickable
CompanyCard credit, QR + link, unlimited edits; Pro $4.99 / $3.99 yearly adds
custom branding, lead capture, analytics, removes the credit). CompanyCard
does not print cards. New text does NOT mention the Wallet pass (owner decision
pending since 2026-10-29). No new licensing rule: the page's existing
designation/permit paragraph is linked, not extended. No competitor.
"""
import json
import re

DATE = "2026-11-21"
F = "digital-business-card-for-accountants.html"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "Digital Business Card for Accountants &amp; Bookkeepers | CompanyCard"
NEW_T = "Accountant Business Cards: Digital Business Card for Accountants &amp; Bookkeepers | CompanyCard"
if NEW_T not in s and OLD_T in s:
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
# JSON-LD name may use a raw "&"
OLD_TJ = "Digital Business Card for Accountants & Bookkeepers | CompanyCard"
NEW_TJ = "Accountant Business Cards: Digital Business Card for Accountants & Bookkeepers | CompanyCard"
if NEW_TJ not in s and OLD_TJ in s:
    s = s.replace(OLD_TJ, NEW_TJ)
    changed.append("title-json")

OLD_D = "A digital business card for accountants and bookkeepers"
NEW_D = "Accountant business cards that stay current: a digital business card for accountants and bookkeepers"
if NEW_D not in s:
    n = s.count(OLD_D)
    assert n >= 1, "description start not found"
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

MARK = "<!-- ACCT-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Setting up an accountant\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Accountant business cards, printed and digital</h2></div>'
    "<p>Most accountants still carry printed business cards: a few in the wallet for the chamber "
    "breakfast, a stack on the reception desk, one clipped to an engagement letter. The trouble is "
    "what is printed on them. Your new-client status, your season hours, the client portal link and "
    "sometimes the firm name itself change during the year, and a box of cards does not. A CompanyCard "
    "gives every printed accountant business card a QR code that opens your live digital card, so the "
    "paper can stay short and the details that change live in one place you can edit. CompanyCard does "
    "not print cards; you add the QR code from your card to whatever you have printed.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Where it goes</th><th>What to put on it</th></tr></thead><tbody>"
    "<tr><td><b>Printed accountant business card</b></td><td>Your name with your designation, the firm, "
    "a direct number and the QR code. Leave services, new-client status, hours and the portal link to "
    "the digital card the code opens.</td></tr>"
    "<tr><td><b>Letterhead, engagement letters and invoices</b></td><td>The same QR code in the footer, "
    "so a client who wants to recommend you can pass on your current card instead of a photocopy.</td></tr>"
    "<tr><td><b>Link sent to a solicitor, broker or lender who refers</b></td><td>The full card: services "
    "by task, the clients you take, whether you are taking new clients this season, a consultation "
    "booking link and a secure document link.</td></tr>"
    "<tr><td><b>Email signature</b></td><td>The card link under your name on every year-end reminder and "
    "return you send, so each forwarded email carries your current details.</td></tr>"
    "</tbody></table>"
    "<p>What you may print after your name, and whether a permit or registration number belongs on "
    "marketing material, is set by your own board or professional body (see "
    "<a href=\"#accountant-rules\">what changes in an accounting practice</a> above). One card is all a "
    "sole practitioner needs, and the free plan covers it; it carries a small CompanyCard credit under "
    "the card. Pro is $4.99 a month, or $3.99 a month billed yearly, adds custom branding, lead capture "
    "and analytics, and removes the credit. A firm with several people can give each person a card; see "
    "<a href=\"pricing.html\">pricing</a> or the <a href=\"qr-code-business-card.html\">QR code business "
    "card</a> guide.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

if 'id="accountant-rules"' not in s:
    s, n = re.subn(r"<h2>(What changes in an accounting practice)", r'<h2 id="accountant-rules">\1', s)
    assert n == 1, "practice heading not found once"
    changed.append("anchor-id")

NEW_FAQS = [
    ("What should an accountant business card say?",
     "Your name with the designation you may use, your firm, a direct number and a QR code. Details that "
     "change, such as the services you offer this season, whether you are taking new clients, your "
     "filing-season hours and your client portal link, are better kept on the digital card the QR code "
     "opens, so a card printed today is still right after the April deadline. Check your board's rule on "
     "designations and permit numbers before printing."),
    ("Do accountants still need printed business cards if they have a digital one?",
     "Many still hand them out at networking breakfasts and leave them on the reception desk. The two "
     "work together: have a short card printed with the QR code from your CompanyCard on it, and the code "
     "opens your current new-client status, hours and booking link. When those change you edit the "
     "digital card once and every printed card already handed out shows the update. CompanyCard does not "
     "print cards."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Questions accountants and bookkeepers ask about digital business cards</h2>"
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
OLD_L = "- Digital business card for accountants & bookkeepers: https://company-card.com/" + F
NEW_L = ("- Accountant business cards: digital business card for accountants & bookkeepers (designation, "
         "services by task, new-client status, referral partners, QR code for printed accountant business "
         "cards): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
