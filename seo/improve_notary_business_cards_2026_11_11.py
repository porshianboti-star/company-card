#!/usr/bin/env python3
"""Improve digital-business-card-for-notaries.html for the "notary business card(s)" queries (2026-11-11). Idempotent.

Why: GSC (28 days to 2026-11-08) shows "notary business card" 16 @ 35.1,
"business cards notary" 16 @ 37.8 and "notary business cards" 7 @ 34.6; every
"notar*" impression (46 @ 35.4) lands on this page. The title says "Digital
Business Card for Notaries & Signing Agents" and never "notary business card",
and the page never covers the printed card a notary still hands out.

What: (1) title / og / twitter / WebPage name -> "Notary Business Cards: Digital
Business Card for Notaries & Signing Agents" (keeps every word the current
title ranks for; H1 unchanged); description names printed notary business
cards; (2) one new section, "Notary business cards, printed and digital",
anchored before "Setting up a notary's card", with a by-format table (printed
card, folder sticker, link sent to a booker, email signature); (3) two FAQs,
visible first, FAQPage JSON-LD Questions appended, then sync_faq_schema.py
byte-matches; (4) dateModified + sitemap lastmod -> 2026-11-11; llms.txt line.

Facts: plan facts from seo/facts.py only (Free = one card with a small
clickable CompanyCard credit; Pro $4.99 / $3.99 yearly removes it). The new
text does NOT mention the Apple/Google Wallet pass (owner decision pending
since 2026-10-29). No statistic, no new state rule (the page's existing "State
rules" section is pointed to, not extended), no competitor (owner directive
2026-09-23). The sample commission details stay fictional.

Run from repo root: python3 seo/improve_notary_business_cards_2026_11_11.py
"""
import json
import re

DATE = "2026-11-11"
F = "digital-business-card-for-notaries.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Notaries &amp; Signing Agents | CompanyCard"
NEW_T = "Notary Business Cards: Digital Business Card for Notaries &amp; Signing Agents | CompanyCard"
if NEW_T not in s and OLD_T in s:  # NEW_T contains OLD_T
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
OLD_D = ("A digital business card for notaries and mobile signing agents — carry your commission details, "
         "take same-day signings with one tap, and stay in every title company&#x27;s contacts.")
NEW_D = ("Notary business cards that stay current: a digital business card for notaries and mobile signing "
         "agents, with a QR code for your printed cards — carry your commission details, take same-day "
         "signings with one tap, and stay in every title company&#x27;s contacts.")
if NEW_D not in s and OLD_D in s:
    n = s.count(OLD_D)
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

# ---------- 2. printed + digital section ----------
MARK = "<!-- NOTARY-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container">'
          '<div class="section-head" style="margin-bottom:32px;"><h2>Setting up a notary\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Notary business cards, printed and digital</h2></div>'
    "<p>Most notaries still hand out printed business cards: at the signing table, in the closing folder, "
    "on a title company&rsquo;s front desk. The problem is what is printed on them. A commission expiry, "
    "an E&amp;O amount, a service area and a travel fee all change, and a box of cards does not. A "
    "CompanyCard gives every printed card a QR code that opens your live digital card, so the paper can "
    "stay short and the details that change live in one place you can edit.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Where it goes</th><th>What to put on it</th></tr></thead><tbody>"
    "<tr><td><b>Printed notary business card</b></td><td>Your name, Notary Public or Notary Public and "
    "Loan Signing Agent, your direct number and the QR code. Leave the details that expire, such as the "
    "commission date and E&amp;O amount, to the digital card the code opens.</td></tr>"
    "<tr><td><b>Sticker on the signing folder</b></td><td>The same QR code with one line such as "
    "&ldquo;Scan to save my details&rdquo;, so a borrower or escrow officer can keep your contact after "
    "the closing.</td></tr>"
    "<tr><td><b>Link sent to a booker</b></td><td>The full card: commission state, number and expiry, "
    "E&amp;O, RON status, counties, hours, languages and a booking link, which is what a vendor "
    "coordinator checks before adding you to a rotation.</td></tr>"
    "<tr><td><b>Email signature</b></td><td>The card link under your name on every confirmation and "
    "scan-back email, so each reply carries your current details.</td></tr>"
    "</tbody></table>"
    "<p>Whatever you print, check it against your state&rsquo;s advertising rules first (see "
    "<a href=\"#state-rules\">state rules on how a notary may advertise</a> below). One card is all a "
    "notary needs, and the free plan covers it; it carries a small CompanyCard credit under the card. "
    "Pro is $4.99 a month, or $3.99 a month billed yearly, adds custom branding, lead capture and "
    "analytics, and removes the credit. See <a href=\"pricing.html\">pricing</a> or the "
    "<a href=\"qr-code-business-card.html\">QR code business card</a> guide.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# the in-page link target for the existing state-rules heading
OLD_H = "<h2>State rules on how a notary may advertise</h2>"
NEW_H = '<h2 id="state-rules">State rules on how a notary may advertise</h2>'
if OLD_H in s:
    assert s.count(OLD_H) == 1
    s = s.replace(OLD_H, NEW_H)
    changed.append("anchor-id")

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("What should a notary business card say?",
     "Your name, Notary Public or Notary Public and Loan Signing Agent, your direct number and a QR code. "
     "Details that change, such as your commission expiry, E&O amount, service area and travel fee, are "
     "better kept on the digital card the QR code opens, so a card printed today is still right after "
     "a renewal. Check your state's notary advertising rules before you print anything."),
    ("Do notaries still need printed business cards if they have a digital one?",
     "Many still hand them out, at the signing table and in the closing folder. The two work together: "
     "print a short card with the QR code from your CompanyCard, and the code opens your current "
     "commission, coverage and booking details. When those change you edit the digital card once and "
     "every printed card already handed out shows the update."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions from notaries</h2>"
i = s.find(FAQ_H2)
assert i != -1, "FAQ section not found"
j = s.find("</section>", i)
assert s[j - len("</details></div>"):j] == "</details></div>", "unexpected FAQ section ending"
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

# ---------- 4. dateModified ----------
m = re.search(r'("dateModified":")(\d{4}-\d{2}-\d{2})(")', s)
assert m and s.count('"dateModified"') == 1, "WebPage dateModified not found once"
if m.group(2) != DATE:
    s = s[:m.start(2)] + DATE + s[m.end(2):]
    changed.append("dateModified")

open(F, "w", encoding="utf-8").write(s)

# ---------- 5. sitemap lastmod ----------
sm = open("sitemap.xml", encoding="utf-8").read()
pat = re.compile(r'(<loc>https://company-card\.com/' + re.escape(F) + r'</loc><lastmod>)(\d{4}-\d{2}-\d{2})')
mm = pat.search(sm)
assert mm, "sitemap entry not found"
if mm.group(2) != DATE:
    sm = pat.sub(r'\g<1>' + DATE, sm, count=1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    changed.append("sitemap-lastmod")

# ---------- 6. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()
OLD_L = "- Digital business card for notaries & mobile signing agents: https://company-card.com/" + F
NEW_L = ("- Notary business cards: digital business card for notaries & mobile signing agents (commission "
         "details, same-day bookings, QR code for printed notary business cards): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
