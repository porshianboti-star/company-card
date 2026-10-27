#!/usr/bin/env python3
"""Improve digital-business-card-for-lawyers.html for the firm-wide query (2026-10-27). Idempotent.

Why: GSC (28 days to 2026-10-25) shows "digital business cards law firm"
17 @ 69.8 and "digital business cards for legal teams" 1 @ 50. The page is
written for one lawyer and a referred client; the firm-wide case (every
partner, associate, paralegal and intake person with their own card on one
firm design) is covered by a single FAQ that links away to the teams page.
The title says "Small Law Firms" in the singular-card form and never the
plural "digital business cards".

What: (1) title / og / twitter / WebPage name -> "Digital Business Cards for
Lawyers & Law Firms"; meta description names the whole-firm case; (2) one new
section, "Digital business cards for a whole law firm", anchored before
"Setting it up"; (3) one FAQ on what it costs a firm, visible first, the
FAQPage JSON-LD Question appended here, then sync_faq_schema.py byte-matches;
(4) dateModified + sitemap lastmod -> 2026-10-27; llms.txt line updated.

Facts: every plan fact and price is taken from seo/facts.py (verified from
pricing.html, re-read 2026-10-27: Pro $4.99 / $3.99 yearly, Business $4.99 /
$3.99 per user, no seat minimum, bought by contacting us). The admin-dashboard
behaviour quoted is what business.html states. No bar or law-society rule is
asserted; the page keeps telling the reader to check their own regulator.
No competitor is named (owner directive 2026-09-23).

Run from repo root: python3 seo/improve_lawyers_firm_2026_10_27.py
"""
import json
import re

DATE = "2026-10-27"
F = "digital-business-card-for-lawyers.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Lawyers &amp; Small Law Firms | CompanyCard"
NEW_T = "Digital Business Cards for Lawyers &amp; Law Firms | CompanyCard"
if OLD_T in s:
    s = s.replace(OLD_T, NEW_T)
    changed.append("title")
OLD_D = ("A digital business card for lawyers and small law firms — show your practice areas and where you "
         "practise, let referred clients book a first consultation, and edit it any time. Free to start.")
NEW_D = ("Digital business cards for lawyers and law firms — practice areas, where you are admitted and how "
         "to book a first consultation, with one firm design for every lawyer and staff member. Free to start.")
if OLD_D in s:
    n = s.count(OLD_D)
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

# ---------- 2. whole-firm section ----------
MARK = "<!-- LAWYERS-FIRM-2026-10 -->"
ANCHOR = ('<section class="section"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Setting it up</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Digital business cards for a whole law firm</h2></div>'
    "<p>In a firm, the card a client receives is rarely the one the firm designed. A partner hands out "
    "last year&rsquo;s print run, an associate adds a practice area the firm does not market, a paralegal "
    "has no card at all, and the intake number differs from card to card. Clients notice, and a referral "
    "that lands on an out-of-date card is harder to act on.</p>"
    "<p>With CompanyCard every person at the firm gets their own card &mdash; partners, associates, of "
    "counsel, paralegals, legal assistants and the intake team &mdash; each with their own name, title, "
    "practice areas, admissions and direct line, on one firm design. The firm name, logo, office "
    "addresses and any wording your regulator expects on marketing are set once and appear on every "
    "card.</p>"
    "<table class=\"lp-table\"><thead><tr><th>At the firm</th><th>What goes on their card</th></tr></thead><tbody>"
    "<tr><td><b>Partners</b></td><td>Practice areas they lead, admissions, direct line, a booking link "
    "for first consultations if they take new matters.</td></tr>"
    "<tr><td><b>Associates and of counsel</b></td><td>Their own practice areas and admissions, a "
    "direct line or email, and the supervising team where that helps the client.</td></tr>"
    "<tr><td><b>Paralegals and legal assistants</b></td><td>Name, role and the matters or lawyers they "
    "support, so an existing client reaches the right person.</td></tr>"
    "<tr><td><b>Intake</b></td><td>The one number and email the firm wants new enquiries to use, and "
    "the line asking people not to send case details yet.</td></tr>"
    "</tbody></table>"
    "<p>The Business plan adds a central admin dashboard, brand and template lock so the firm design "
    "stays the same on every card, CRM sync and team analytics, with SSO and priority support. When "
    "someone joins, changes title or leaves, the card is updated or deactivated from the dashboard, and "
    "every link and QR code already shared shows the change. There is no seat minimum, so a two-lawyer "
    "practice pays for two people. Business is $4.99 per user a month, or $3.99 per user a month "
    "billed yearly, and is arranged by "
    "<a href=\"contact.html\">talking to us about teams</a> rather than self-serve. A solo practitioner "
    "does not need it: the free plan covers one card. See <a href=\"pricing.html\">pricing</a> and "
    "<a href=\"digital-business-cards-for-teams.html\">digital business cards for teams</a>.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-it-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# ---------- 3. FAQ (visible, then JSON-LD Question appended) ----------
NEW_FAQS = [
    ("How much do digital business cards cost for a law firm?",
     "A solo lawyer can use the free plan: one card, $0 forever, with a small CompanyCard credit under "
     "the card. Pro is $4.99 a month, or $3.99 a month billed yearly, and removes the credit. A firm "
     "that wants one locked design and a central admin dashboard uses Business at $4.99 per user a "
     "month, or $3.99 per user a month billed yearly, with no seat minimum, arranged by talking to us "
     "about teams. Prices are in US dollars."),
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
m = re.search(r'("url":"https://company-card\.com/' + re.escape(F) + r'"[^<]*?"dateModified":")(\d{4}-\d{2}-\d{2})(")', s)
assert m, "WebPage dateModified not found"
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
OLD_L = ("- Digital business card for lawyers & small law firms (practice areas, jurisdictions, first "
         "consultations for referred clients): https://company-card.com/" + F)
NEW_L = ("- Digital business cards for lawyers & law firms (practice areas, jurisdictions, first "
         "consultations for referred clients; one firm design for every lawyer, paralegal and intake "
         "person on Business, no seat minimum): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
