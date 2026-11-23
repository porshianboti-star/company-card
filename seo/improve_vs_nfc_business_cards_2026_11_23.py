#!/usr/bin/env python3
"""Improve digital-business-card-vs-nfc-card.html for the "vs NFC business cards" cluster (2026-11-23). Idempotent.

Why: GSC 28 days to 11-21 shows "digital business card vs nfc" 22 impressions
@ 31.0, "digital business cards vs nfc business cards" 14 @ 38.3 and "nfc vs
digital business cards" 12 @ 34.4 (48 impressions, all on this page). The
title says "NFC Card" and the page never uses the phrase "NFC business card"
the searcher types, and it does not say which one to use in which situation.
Page untouched since 2026-08-02.

What: same shape as seo/improve_accountant_business_cards_2026_11_21.py.
(1) title / og / twitter / WebPage name -> "Digital Business Card vs NFC
Business Card: Which Do You Actually Need? (2026)" (H1 and breadcrumb
unchanged); description names NFC business cards; (2) one new section "NFC
business card or digital business card: which to use where" before "Deciding
in one minute", with a by-situation table; (3) two FAQs, visible + FAQPage
JSON-LD, then sync_faq_schema.py; (4) dateModified + sitemap lastmod; llms.txt.

Facts: plan facts from seo/facts.py only (Free = one card, QR code + link,
unlimited edits, small clickable CompanyCard credit). CompanyCard does not sell
NFC hardware (already stated on the page). New text does NOT mention the
Wallet pass (owner decision pending since 2026-10-29). No vendor is named, no
price of any hardware is added, no phone model or statistic is asserted. The
"what happens when details change" answer is conditional on what the tag
stores (a link to a page you can edit vs contact details written on the chip).
"""
import json
import re

DATE = "2026-11-23"
F = "digital-business-card-vs-nfc-card.html"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "Digital Business Card vs NFC Card: Which Do You Actually Need? (2026) | CompanyCard"
NEW_T = "Digital Business Card vs NFC Business Card: Which Do You Actually Need? (2026) | CompanyCard"
if NEW_T not in s:
    n = s.count(OLD_T)
    assert n == 4, "expected title in 4 places, found %d" % n
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)

OLD_D = "Digital business card vs NFC card compared"
NEW_D = "Digital business cards vs NFC business cards compared"
if NEW_D not in s:
    n = s.count(OLD_D)
    assert n == 1, "description start not found once"
    s = s.replace(OLD_D, NEW_D)
    changed.append("description")

MARK = "<!-- VS-NFC-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container">'
          '<div class="section-head" style="margin-bottom:32px;"><h2>Deciding in one minute</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>NFC business card or digital business card: which to use where</h2></div>'
    "<p>Because an NFC business card usually opens a digital business card, most of the choice comes down "
    "to the moment you are sharing in. A tap only works when the other person is standing next to you; a "
    "QR code or a link also works when they are not. The table below goes through the common situations "
    "for a small business or a self-employed professional.</p>"
    '<div class="lp-table"><table><thead><tr><th>Situation</th><th>What works</th></tr></thead><tbody>'
    "<tr><td><b>Meeting one person face to face</b></td><td>Either. Tap an NFC business card if you own one, "
    "or show the QR code of your digital business card on your phone screen.</td></tr>"
    "<tr><td><b>Trade-show stand or shop counter</b></td><td>Both. A tap for the person in front of you, "
    "and a printed QR code on the stand for people who walk past or whose phone does not respond to the tap.</td></tr>"
    "<tr><td><b>Van, sign, window, flyer or invoice</b></td><td>QR code. Nobody can tap a van, and a code "
    "is read from a distance.</td></tr>"
    "<tr><td><b>Email, text message, LinkedIn or a video call</b></td><td>The link to your digital business "
    "card. An NFC card cannot be sent.</td></tr>"
    "<tr><td><b>A new person joins the business</b></td><td>A digital business card can be made the same "
    "day. An NFC business card has to be ordered and delivered first.</td></tr>"
    "<tr><td><b>Your phone number or job title changes</b></td><td>Edit the digital business card once. "
    "An NFC card that points at that card's link then opens the updated details as well.</td></tr>"
    "</tbody></table></div>"
    "<p>So the two are not rivals: the digital business card is the part that holds your details, and an "
    "NFC business card is one optional way to open it. CompanyCard makes the digital part and does not "
    "sell NFC hardware. The free plan covers one card with a QR code and a sharing link and unlimited "
    "edits, and carries a small CompanyCard credit under the card; see <a href=\"pricing.html\">pricing</a> "
    "or the <a href=\"qr-code-business-card.html\">QR code business card</a> guide.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "deciding anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

NEW_FAQS = [
    ("Is an NFC business card better than a digital business card?",
     "They do different jobs. A digital business card is the page that holds your details, shared by QR "
     "code or link, and it reaches people in person, by email and from a sign. An NFC business card is a "
     "physical card that opens a page like that when it is tapped against a phone, so it only helps when "
     "you are standing next to someone. Most small businesses start with the digital business card and "
     "add an NFC card later only if they want something to hand over or tap."),
    ("What happens to an NFC business card when my details change?",
     "It depends on what the card stores. If the NFC business card holds a link to a digital business card "
     "that you can edit, you change the details once on that card and the next tap opens the updated "
     "version. If your contact details were written directly onto the chip, the card has to be rewritten "
     "or replaced. A CompanyCard link stays the same when you edit your card, and edits are unlimited on "
     "every plan."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions</h2>"
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
OLD_L = "- Digital business card vs NFC card: https://company-card.com/" + F
NEW_L = ("- Digital business card vs NFC business card (the NFC card is a way to open a digital card; which to "
         "use face to face, on a stand, on a sign, by email; what happens when details change): "
         "https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
