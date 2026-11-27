#!/usr/bin/env python3
"""Improve digital-business-cards-for-teams.html for the team / employee business-card cluster (2026-11-27). Idempotent.

Why: GSC 28 days to 11-25, Page filter = this URL, 14 query rows, 108
impressions, 0 clicks: "digital business cards for teams" 31 @ 52.9, "team
company cards" 18 @ 15.8, "team business cards" 10 @ 24.7, "business cards for
large teams" 9 @ 25.7, "business cards many employees" 8 @ 26.0, "business
cards for multiple employees" 5 @ 40.0, "business cards for all employees"
4 @ 24.8, "business card(s) for employees" 4 @ 39.5 + 3 @ 42.0. The page never
says "team business cards", gives no price for a team of a given size (only the
5-person pointer) and never covers the printed card employees still carry.
Page content untouched since 2026-09-29.

What: (1) title / og / WebPage name -> "Team Business Cards: Digital Business
Cards for Teams & Employees" (H1 + breadcrumb unchanged); description leads
with team business cards; (2) one new section "Team business cards for every
employee, from two people to a large team" before "Why teams switch together",
with a by-team-size table; (3) two FAQs, visible + FAQPage JSON-LD, then
sync_faq_schema.py; (4) dateModified + sitemap lastmod on this URL; llms.txt.

Facts: plan facts from seo/facts.py only (Free = one card per person with a
small clickable CompanyCard credit; Business $4.99 per user monthly / $3.99
per user a month billed yearly, no seat minimum, central admin dashboard,
brand and template lock, CRM sync, team analytics, SSO, bought by contacting
us, not self-serve; Enterprise custom: SCIM, SAML, audit logs, data
residency, invoicing). Every figure in the table is seats x list price.
CompanyCard does not print cards. No Wallet text (owner decision pending
since 2026-10-29). No statistic, no competitor, no volume discount claimed.
"""
import json
import re

DATE = "2026-11-27"
F = "digital-business-cards-for-teams.html"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "Digital Business Cards for Teams — One Brand, Every Employee | CompanyCard"
NEW_T = "Team Business Cards: Digital Business Cards for Teams &amp; Employees | CompanyCard"
NEW_TJ = "Team Business Cards: Digital Business Cards for Teams & Employees | CompanyCard"
if OLD_T in s:
    # <title> and og:title take the HTML-escaped form; the JSON-LD name takes the raw "&"
    for pat, new in ((r'(<title>)' + re.escape(OLD_T), NEW_T),
                     (r'(<meta property="og:title" content=")' + re.escape(OLD_T), NEW_T),
                     (r'("@type":"WebPage","name":")' + re.escape(OLD_T), NEW_TJ)):
        s, n = re.subn(pat, lambda m, new=new: m.group(1) + new, s)
        assert n == 1, "title target not found once: " + pat[:40]
    assert OLD_T not in s, "an old title copy is left"
    changed.append("title x3")

OLD_D = "Roll out digital business cards across your company:"
NEW_D = "Team business cards for every employee, from 2 people to a large team. Roll out digital business cards across your company:"
if NEW_D not in s:
    n = s.count(OLD_D)
    assert n == 2, "description start expected twice, found %d" % n
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

TD = 'style="padding:12px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--slate-200);font-size:.98rem;line-height:1.55;color:var(--slate-700);"'
TH = 'style="padding:12px 14px;text-align:left;border-bottom:1px solid var(--slate-200);background:var(--slate-50);font-weight:700;color:var(--ink);"'


def row(a, b, c):
    return f"<tr><td {TD}><b>{a}</b></td><td {TD}>{b}</td><td {TD}>{c}</td></tr>"


MARK = "<!-- TEAM-BUSINESS-CARDS-2026-11 -->"
ANCHOR = ('<section class="section">\n  <div class="container lp-prose">\n    <div class="section-head" '
          'style="margin-bottom:32px;"><h2>Why teams switch together</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Team business cards for every employee, from two people to a large team</h2></div>'
    "<p>Ordering business cards for a team used to mean one print run per person, and another every "
    "time someone joined, changed title or got a new number. Team business cards on CompanyCard work "
    "the other way round: the company keeps one template, each employee has a digital card built from "
    "it, and a change is an edit rather than a reprint. The Business plan is priced per user with no "
    "seat minimum, so the sums below are simply the number of employees multiplied by the list price: "
    "$3.99 per user a month billed yearly, or $4.99 per user billed monthly.</p>"
    '<div style="overflow-x:auto;margin:0 0 18px;"><table style="width:100%;border-collapse:collapse;background:#fff;'
    'border:1px solid var(--slate-200);">'
    f"<thead><tr><th {TH}>Team size</th><th {TH}>Business plan, list price</th><th {TH}>What matters at this size</th></tr></thead><tbody>"
    + row("2 to 5 employees",
          "2 people: $7.98 a month billed yearly, $9.98 billed monthly. 5 people: $19.95 or $24.95.",
          "There is no seat minimum, so a two-person company pays for two seats. If nobody needs a "
          "locked template yet, each person can start on their own free card, which carries a small "
          "CompanyCard credit.")
    + row("10 to 25 employees",
          "10 people: $39.90 a month billed yearly, $49.90 billed monthly. 25 people: $99.75 or $124.75.",
          "Brand and template lock starts to pay for itself: admins fix the logo, colours and layout, "
          "and employees change only their own details.")
    + row("50 to 100 employees",
          "50 people: $199.50 a month billed yearly, $249.50 billed monthly. 100 people: $399 or $499.",
          "The central admin dashboard, team analytics, CRM sync and SSO are part of Business, so "
          "cards for many employees are managed in one place.")
    + row("Large teams with IT requirements",
          "Enterprise, custom pricing.",
          "Adds SCIM provisioning and SAML, audit logs, data residency, a dedicated success manager, "
          "an SLA and invoicing.")
    + "</tbody></table></div>"
    "<p>Two limits to know before you plan a rollout. Team plans are not bought through a checkout: "
    "Business and Enterprise start with a conversation, through “Talk to us about teams” on the "
    "<a href=\"pricing.html\">pricing page</a>. And CompanyCard does not print cards. If your "
    "employees still hand out printed business cards, each person’s card has its own QR code that "
    "your printer can place on the paper card, so the printed card stays short and the details that "
    "change live on the digital one. The <a href=\"qr-code-business-card.html\">QR code business "
    "card</a> guide covers that, and a team of a few people can compare the options on our "
    "<a href=\"digital-business-card-for-small-business.html\">small business</a> page.</p>"
    "</div></section>\n\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "why-teams anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

NEW_FAQS = [
    ("How much do team business cards cost for 10, 50 or 100 employees?",
     "On CompanyCard’s Business plan the list price is $3.99 per user a month billed yearly, or $4.99 "
     "per user billed monthly, with no seat minimum. That is $39.90 a month billed yearly for 10 "
     "employees ($49.90 billed monthly), $199.50 for 50 ($249.50) and $399 for 100 ($499). Business is "
     "bought by contacting us rather than through a checkout, and Enterprise, for large teams that "
     "need SCIM, SAML or invoicing, is priced on request."),
    ("Can a team of two or three people get team business cards?",
     "Yes. The Business plan has no seat minimum, so a two-person team pays for two seats: $7.98 a "
     "month billed yearly, or $9.98 billed monthly. A very small team that does not need a locked "
     "company template or an admin dashboard can also have each person start with their own free "
     "card, which carries a small CompanyCard credit under the card."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions</h2>"
i = s.find(FAQ_H2)
assert i != -1 and s.count(FAQ_H2) == 1, "FAQ section not found once"
for q, a in NEW_FAQS:
    if f"<summary>{esc(q)}</summary>" in s:
        continue
    j = s.find("</section>", i)
    k = s.rfind("</details>", i, j)
    assert k != -1, "no FAQ item in the FAQ section"
    k += len("</details>")
    blk = f'\n<details class="lp-faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
    s = s[:k] + blk + s[k:]
    changed.append("faq")

ld = re.search(r'<script type="application/ld\+json">(\{"@context": ?"https://schema.org", ?"@type": ?"FAQPage".*?)</script>', s, re.S)
assert ld, "FAQPage JSON-LD not found"
data = json.loads(ld.group(1))
names = {q["name"] for q in data["mainEntity"]}
add = False
for q, a in NEW_FAQS:
    if q not in names:
        data["mainEntity"].append({"@type": "Question", "name": q,
                                   "acceptedAnswer": {"@type": "Answer", "text": a}})
        add = True
if add:
    s = s.replace(ld.group(1), json.dumps(data, ensure_ascii=False), 1)
    changed.append("faq-schema")

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
OLD_L = "- Digital business cards for teams: https://company-card.com/" + F
NEW_L = ("- Team business cards: digital business cards for teams and employees (one locked company "
         "template, a card per employee, Business plan list price by team size from 2 to 100 people with "
         "no seat minimum, Enterprise for large teams, QR code for printed employee cards): "
         "https://company-card.com/" + F)
if OLD_L in ll:
    assert ll.count(OLD_L) == 1
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
