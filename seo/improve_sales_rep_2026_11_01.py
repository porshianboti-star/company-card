#!/usr/bin/env python3
"""Improve digital-business-card-for-sales-teams.html for the single-rep queries (2026-11-01). Idempotent.

Why: GSC (28 days to 2026-10-30) shows "sales rep business card" 23 @ 53.4 and
"sales representative business card" 22 @ 66.5 (47 impressions, all landing on
this page at 59.8), plus "digital business card for field sales" 40 @ 49.0.
The page is written for a sales manager rolling cards out to a team; the one
rep who sets up their own card (the only rep at a small company, a territory or
manufacturer's rep, a new hire whose employer still prints paper) is covered by
a single FAQ. The title names teams and field reps but never the singular
"sales rep" / "sales representative".

What: (1) title / og / twitter -> "Digital Business Card for Sales Reps, Field
Sales & Sales Teams" (keeps every word the current title ranks for; H1 unchanged);
meta description names the single rep; (2) one new section, "A digital business
card for one sales rep", anchored before "Setting up a sales team", with a
by-role table (inside sales / SDR, field or territory rep, account executive,
manufacturer's or distributor's rep); (3) two FAQs, visible first, the FAQPage
JSON-LD Questions appended here, then sync_faq_schema.py byte-matches;
(4) dateModified + sitemap lastmod -> 2026-11-01; llms.txt line updated.

Facts: every plan fact and price is taken from seo/facts.py (verified from
pricing.html: Free = one card, QR code and sharing link, profile, links and
socials, unlimited edits, no credit card, small clickable CompanyCard credit;
Pro $4.99 / $3.99 yearly adds lead capture, analytics, unlimited links and
files, custom branding and removes the credit; Business $4.99 / $3.99 per user,
no seat minimum, bought by contacting us). The new text does NOT repeat the
"Apple and Google Wallet pass" claim (owner decision pending since 2026-10-29).
No statistic, no competitor (owner directive 2026-09-23).

Run from repo root: python3 seo/improve_sales_rep_2026_11_01.py
"""
import json
import re

DATE = "2026-11-01"
F = "digital-business-card-for-sales-teams.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Sales Teams &amp; Field Sales Reps | CompanyCard"
NEW_T = "Digital Business Card for Sales Reps, Field Sales &amp; Sales Teams | CompanyCard"
if OLD_T in s:
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
OLD_D = ("A digital business card for sales teams and field sales reps — prospects save you in one tap, "
         "leave their details back on your card, and every rep stays on brand from one admin dashboard. "
         "No seat minimum. Free to start.")
NEW_D = ("A digital business card for a sales rep or a whole sales team — what a sales representative’s "
         "card should carry, prospects save you in one tap and leave their details back, and every rep "
         "stays on brand from one dashboard. No seat minimum. Free for one rep.")
if OLD_D in s:
    n = s.count(OLD_D)
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

# ---------- 2. single-rep section ----------
MARK = "<!-- SALES-REP-2026-11 -->"
ANCHOR = ('<section class="section"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Setting up a sales team</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>A digital business card for one sales rep</h2></div>'
    "<p>Not every sales representative is handed a card by an admin. You may be the only rep at a small "
    "company, a territory or manufacturer&rsquo;s rep covering a region on your own, or a new hire whose "
    "employer still prints paper. In all of those cases the card you hand over is yours to set up, and "
    "CompanyCard does not need a team account for that: the free plan is one card for one person, with no "
    "credit card.</p>"
    "<p>What a sales rep&rsquo;s business card should carry depends on how you sell. The table is a starting "
    "point; every row fits on one CompanyCard, and each item is a field you can change later without "
    "handing out a new card.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Sales role</th><th>What goes on the card</th></tr></thead><tbody>"
    "<tr><td><b>Inside sales or SDR</b></td><td>Name, title, direct line and work email, a calendar link "
    "for the discovery call, and the one product page you qualify against.</td></tr>"
    "<tr><td><b>Field or territory rep</b></td><td>Name, title and territory on one line, the direct mobile "
    "a prospect can reach on a site visit, a link to the product sheet or price list, and the QR code on "
    "a clipboard, a sample case or the back of your phone.</td></tr>"
    "<tr><td><b>Account executive</b></td><td>Name, title, direct line, a calendar link for demos, and a "
    "link to a demo video or case study rather than a brochure.</td></tr>"
    "<tr><td><b>Manufacturer&rsquo;s or distributor&rsquo;s rep</b></td><td>Name, the lines or brands you "
    "carry, the region you cover, direct mobile, and a link to the catalogue or order form.</td></tr>"
    "</tbody></table>"
    "<p>If you still carry paper cards, put the QR code from your CompanyCard on them. The prospect who "
    "scans it saves the contact as it is today, so a card printed before your title or number changed "
    "keeps working. On the free plan the prospect saves your details in one tap. If you want the "
    "exchange to run both ways &mdash; the prospect leaving their name, company and email from your card "
    "&mdash; that is lead capture, part of Pro at $4.99 a month, or $3.99 a month billed yearly, together "
    "with view-and-save analytics, unlimited links and files for the product sheet, custom branding, and "
    "no CompanyCard credit under the card. Business is the plan for when there is a team to manage, not "
    "a requirement for one rep. See <a href=\"pricing.html\">pricing</a>.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("What should a sales rep put on a business card?",
     "Name, title and territory on one line, a direct mobile and a work email, a calendar link for the "
     "follow-up, and one link to what you sell. On a CompanyCard the same details open from a link or a "
     "QR code and the prospect saves them to their phone in one tap; on Pro the card can also collect the "
     "prospect's details back. If you still carry paper cards, print the QR code on them so the saved "
     "contact stays current after your title or number changes."),
    ("Can a sales representative use CompanyCard without a company account?",
     "Yes. The free plan is one card for one person, with no credit card: a QR code and sharing link, "
     "your profile, links and socials, and unlimited edits, with a small CompanyCard credit under the "
     "card. Pro, at $4.99 a month or $3.99 a month billed yearly, adds lead capture and analytics and "
     "removes the credit. If your company later wants every rep on one locked design, Business is "
     "priced per user with no seat minimum, so the cards already in use are not wasted."),
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
OLD_L = ("- Digital business card for sales teams & field sales reps (prospect saves the rep in one tap, lead "
         "capture on Pro and Business, brand and template lock, CRM sync and no seat minimum on Business): "
         "https://company-card.com/" + F)
NEW_L = ("- Digital business card for sales reps, field sales & sales teams (what a single sales representative's "
         "card should carry, free for one rep; prospect saves the rep in one tap, lead capture on Pro and "
         "Business, brand and template lock, CRM sync and no seat minimum on Business): "
         "https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
