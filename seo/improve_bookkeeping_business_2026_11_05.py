#!/usr/bin/env python3
"""Improve digital-business-card-for-bookkeepers.html for the "bookkeeping business card" queries (2026-11-05). Idempotent.

Why: GSC (28 days to early November) shows the bookkeeper cluster closest to
page 2 of any profession page: "bookkeeping business card" 24 @ 25.2,
"bookkeeper business card" 19 @ 26.0, "bookkeeper business cards" 17 @ 27.2,
"bookkeeping business cards" 1 @ 34.0 (61 impressions, 0 clicks). The page is
written for the bookkeeper as a person; the searcher who types "bookkeeping
business card" is often setting up cards for the business itself (a sole
practice with its own name, or a small practice with staff), and may still
want printed cards. The title never says "bookkeeping" or "business card(s)"
for a practice.

What: (1) title / og / twitter -> "Digital Business Card for Bookkeepers &
Bookkeeping Businesses" (keeps every word the current title ranks for; H1
unchanged); meta / og / twitter description names the practice and printed
cards; (2) one new section, "Business cards for a bookkeeping business",
anchored before "Setting it up", with a by-practice table (sole practitioner
under their own name, sole practitioner with a trading name, small practice
with staff, printed cards); (3) two FAQs, visible first, FAQPage JSON-LD
Questions appended, then sync_faq_schema.py byte-matches; (4) dateModified +
sitemap lastmod -> 2026-11-05; llms.txt line updated.

Facts: every plan fact and price is from seo/facts.py (Free = one card, QR code
and sharing link, profile, links and socials, unlimited edits, no credit card,
small clickable CompanyCard credit; Pro $4.99 / $3.99 yearly adds custom
branding, lead capture and analytics and removes the credit; Business $4.99 /
$3.99 per user, no seat minimum, bought by contacting us). The new text does NOT
repeat the "Apple and Google Wallet pass" claim (owner decision pending since
2026-10-29). No statistic, no regulatory rule, no competitor (owner directive
2026-09-23).

Run from repo root: python3 seo/improve_bookkeeping_business_2026_11_05.py
"""
import json
import re

DATE = "2026-11-05"
F = "digital-business-card-for-bookkeepers.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Bookkeepers | CompanyCard"
NEW_T = "Digital Business Card for Bookkeepers &amp; Bookkeeping Businesses | CompanyCard"
if OLD_T in s:
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
OLD_D = ("A digital business card for bookkeepers — show the software you work in, your monthly services "
         "and catch-up work, and let referred clients book a discovery call. Free to start.")
NEW_D = ("A digital business card for bookkeepers and bookkeeping businesses — the software you work in, "
         "your monthly services and catch-up work, a discovery-call link, one card per person in a "
         "practice, and a QR code for printed cards. Free to start.")
if OLD_D in s:
    n = s.count(OLD_D)
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

# ---------- 2. practice section ----------
MARK = "<!-- BOOKKEEPING-BUSINESS-2026-11 -->"
ANCHOR = ('<section class="section"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Setting it up</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Business cards for a bookkeeping business</h2></div>'
    "<p>A bookkeeping business card is usually the same card as a bookkeeper&rsquo;s, organised around "
    "the practice rather than the person: the business name first, then who to contact, then what the "
    "practice does each month. How you set it up depends on how the business is run.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Your practice</th><th>How to set up the card</th></tr></thead><tbody>"
    "<tr><td><b>Sole practitioner under your own name</b></td><td>One card, your name as the headline, "
    "&ldquo;Bookkeeper&rdquo; as the title, then software, monthly services and the discovery-call link. "
    "The free plan covers it.</td></tr>"
    "<tr><td><b>Sole practitioner with a trading name</b></td><td>Still one card. Put the business name "
    "on the card alongside your own, and a link to the practice website if you have one. Pro adds custom "
    "branding and themes if you want the card in your practice colours and removes the CompanyCard credit "
    "under the card.</td></tr>"
    "<tr><td><b>Small practice with staff</b></td><td>One card per person, each with their own direct "
    "line and booking link, on one shared design. Business is priced per user with no seat minimum, so "
    "a practice of two pays for two; it adds a central admin dashboard and brand and template lock, and "
    "is set up by <a href=\"contact.html\">talking to us</a>.</td></tr>"
    "<tr><td><b>You still want printed cards</b></td><td>Print the QR code from your CompanyCard on the "
    "back. A client who scans it saves your details as they are today, so a printed card stays useful "
    "after you add payroll, change a package price or move to a new number.</td></tr>"
    "</tbody></table>"
    "<p>In every row the card opens in the browser of the person receiving it, with a one-tap save "
    "contact button and no app or account needed. On Pro, lead capture lets a prospective client leave "
    "their name and email from your card, and analytics shows how often it was opened. Pro is $4.99 a "
    "month, or $3.99 a month billed yearly. See <a href=\"pricing.html\">pricing</a>.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("What should a bookkeeping business card say?",
     "The business name and the person to contact, \"Bookkeeper\" or the title you use, the accounting "
     "software you work in, the monthly services you offer, whether you take catch-up work, a phone number "
     "and email, and a link to book a discovery call. On a CompanyCard those details open from a link or a "
     "QR code, and every one of them can be edited later without handing out a new card."),
    ("Can a bookkeeping practice with staff give everyone a card?",
     "Yes. Each person gets their own card with their own direct line and booking link. The Business plan "
     "is priced per user with no seat minimum, at $4.99 per user a month or $3.99 per user a month billed "
     "yearly, and adds a central admin dashboard and brand and template lock so every card in the practice "
     "uses the same design. Business is set up by contacting us. A sole practitioner only needs one card, "
     "and the free plan covers it."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions</h2>"
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
OLD_L = ("- Digital business card for bookkeepers (monthly bookkeeping, catch-up work, remote clients referred "
         "by accountants): https://company-card.com/" + F)
NEW_L = ("- Digital business card for bookkeepers & bookkeeping businesses (monthly bookkeeping, catch-up work, "
         "remote clients referred by accountants; one card per person in a practice, QR code for printed "
         "cards): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
