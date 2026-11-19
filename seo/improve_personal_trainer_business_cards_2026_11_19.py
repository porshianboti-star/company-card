#!/usr/bin/env python3
"""Improve digital-business-card-for-personal-trainers.html for the "personal trainer business cards" queries (2026-11-19). Idempotent.

Why: the 2026-11-13 GSC read (28 days to 11-10) showed "personal trainer
business cards" 20 impressions @ 55.1 landing on this page, which had not been
touched since 2026-08-02. The title says "Digital Business Card for Personal
Trainers & Coaches" and never "personal trainer business cards", and the page
never covers the printed card, sticker or flyer a trainer still uses. GSC
performance could not be re-read on 2026-11-19 (the browser pane declined the
page), so the 11-13 figure is the baseline.

What: same shape as seo/improve_notary_business_cards_2026_11_11.py.
(1) title / og / twitter / WebPage name -> "Personal Trainer Business Cards:
Digital Business Card for Personal Trainers & Coaches" (keeps every word of
the old title; H1 unchanged); description names printed personal trainer
business cards; (2) one new section, "Personal trainer business cards, printed
and digital", anchored before "Setting up a personal trainer's card", with a
by-format table (printed card, water-bottle sticker / noticeboard flyer, link
sent to a clinic or client, email signature); (3) two FAQs, visible first,
FAQPage JSON-LD Questions appended, then sync_faq_schema.py byte-matches;
(4) dateModified + sitemap lastmod -> 2026-11-19; llms.txt line.

Facts: plan facts from seo/facts.py only (Free = one card with a small
clickable CompanyCard credit, QR code and link, unlimited edits; Pro $4.99 /
$3.99 yearly removes the credit and adds custom branding, lead capture and
analytics). CompanyCard does not print cards and the text says so. The new
text does NOT mention the Apple/Google Wallet pass (owner decision pending
since 2026-10-29). No statistic, no new gym / certification / health-claim
rule (the page's existing rules section is pointed to, not extended), no
competitor (owner directive 2026-09-23). Sample details stay fictional.

Run from repo root: python3 seo/improve_personal_trainer_business_cards_2026_11_19.py
"""
import json
import re

DATE = "2026-11-19"
F = "digital-business-card-for-personal-trainers.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Personal Trainers &amp; Coaches | CompanyCard"
NEW_T = "Personal Trainer Business Cards: Digital Business Card for Personal Trainers &amp; Coaches | CompanyCard"
if NEW_T not in s and OLD_T in s:  # NEW_T contains OLD_T
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
OLD_D_START = "A digital business card for personal trainers "
NEW_D_START = ("Personal trainer business cards that stay current: a digital business card for personal "
               "trainers, with a QR code for your printed cards ")
if NEW_D_START not in s:
    n = s.count(OLD_D_START)
    assert n >= 1, "description start not found"
    s = s.replace(OLD_D_START, NEW_D_START)
    changed.append("description x%d" % n)

# ---------- 2. printed + digital section ----------
MARK = "<!-- PT-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container">'
          '<div class="section-head" style="margin-bottom:32px;"><h2>Setting up a personal trainer\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Personal trainer business cards, printed and digital</h2></div>'
    "<p>Plenty of personal trainers still keep printed business cards: a stack at the gym&rsquo;s front "
    "desk, a few at a physio&rsquo;s reception, one tucked into a new client&rsquo;s welcome pack. The "
    "weak point is what is printed on them. Your open slots, your prices, the gym you train at and "
    "your packages all change, and a box of cards does not. A CompanyCard gives every printed card a "
    "QR code that opens your live digital card, so the paper can stay short and the details that change "
    "live in one place you can edit. CompanyCard does not print cards; you add the QR code from your "
    "card to whatever you have printed.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Where it goes</th><th>What to put on it</th></tr></thead><tbody>"
    "<tr><td><b>Printed personal trainer business card</b></td><td>Your name, the title your certifying "
    "body grants, one line on who you train, the number clients text and the QR code. Leave prices, "
    "open slots and the gym address to the digital card the code opens.</td></tr>"
    "<tr><td><b>Sticker on a water bottle or a noticeboard flyer</b></td><td>The same QR code with one "
    "line such as &ldquo;Scan to book a free consultation&rdquo;, so a member can save your details "
    "between sets without stopping you mid-session.</td></tr>"
    "<tr><td><b>Link sent to a clinic or a client&rsquo;s friend</b></td><td>The full card: where you "
    "train, specialisms, open slots, packages, the booking link, a referral email, and your "
    "certification, insurance and first aid status, which is what a physio checks before sending a "
    "patient.</td></tr>"
    "<tr><td><b>Email signature</b></td><td>The card link under your name on every programme, invoice "
    "and check-in email, so each reply carries your current details.</td></tr>"
    "</tbody></table>"
    "<p>Before you hand anything out on the gym floor, check your gym&rsquo;s agreement and your "
    "certifying body&rsquo;s wording (see <a href=\"#trainer-rules\">gym rules, certifying bodies and "
    "health claims</a> below). One card is all a solo trainer needs, and the free plan covers it; it "
    "carries a small CompanyCard credit under the card. Pro is $4.99 a month, or $3.99 a month billed "
    "yearly, adds custom branding, lead capture and analytics, and removes the credit. See "
    "<a href=\"pricing.html\">pricing</a> or the <a href=\"qr-code-business-card.html\">QR code business "
    "card</a> guide.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# the in-page link target for the existing rules heading
if 'id="trainer-rules"' not in s:
    s, n = re.subn(r"<h2>(Gym rules, certifying bodies and health claims on a trainer)",
                   r'<h2 id="trainer-rules">\1', s)
    assert n == 1, "rules heading not found once"
    changed.append("anchor-id")

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("What should a personal trainer business card say?",
     "Your name, the title your certifying body grants, one line on who you train, the number clients "
     "text and a QR code. Details that change, such as open slots, prices, packages and the gym you "
     "train at, are better kept on the digital card the QR code opens, so a card printed today is still "
     "right after you move gyms. Check your gym's rules before you hand cards to members on the floor."),
    ("Do personal trainers still need printed business cards if they have a digital one?",
     "Many still leave them at a gym's front desk or a physio's reception. The two work together: have a "
     "short card printed with the QR code from your CompanyCard on it, and the code opens your current "
     "slots, packages and booking link. When those change you edit the digital card once and every "
     "printed card already handed out shows the update. CompanyCard does not print cards."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions from personal trainers</h2>"
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
OLD_L = "- Digital business card for personal trainers: https://company-card.com/" + F
NEW_L = ("- Personal trainer business cards: digital business card for personal trainers & coaches (open "
         "slots, booking link, clinic referrals, QR code for printed personal trainer business cards): "
         "https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
