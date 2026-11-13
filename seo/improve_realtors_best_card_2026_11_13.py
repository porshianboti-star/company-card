#!/usr/bin/env python3
"""Improve digital-business-card-for-realtors.html for the "best digital business card for realtors" queries (2026-11-13). Idempotent.

Why: GSC (28 days to 2026-11-10) shows 142 impressions @ 73.6 on "real*" queries,
all landing on this page: "best digital business card for realtors" 38 @ 53.4,
"best digital business card for real estate agents" 18 @ 51.4, "real estate
digital business card" 26 @ 81.5, "digital business card for realtors" 21 @
91.0. It is the largest profession cluster on the property, and the page never
answers the "which is best" question: it has no list of what a realtor should
check before picking a card.

What: (1) one new section, "How to choose the best digital business card for a
realtor", anchored before "Setting up a realtor's card": a criteria table (what
to check / why it matters in real estate / what CompanyCard does), stated with
our limits (free = one card with a small credit; lead capture is Pro; team
plans are bought by contacting us); (2) two FAQs, visible first, FAQPage
JSON-LD Questions appended, then sync_faq_schema.py byte-matches; (3)
description names the choosing checklist; (4) dateModified + sitemap lastmod ->
2026-11-13; llms.txt line. Title and H1 unchanged (they already carry every
query word except "best", and we do not call ourselves the best).

Facts: plan facts from seo/facts.py only (Free = one card, QR code and link,
unlimited edits, small clickable CompanyCard credit; Pro $4.99 / $3.99 yearly:
custom branding, lead capture, analytics, removes the credit; Business $4.99 /
$3.99 per user, no seat minimum, central admin, brand and template lock, bought
by contacting us). The new text does NOT mention the Apple/Google Wallet pass
(owner decision pending since 2026-10-29). No statistic, no new licensing rule
(the existing commission-rules section is pointed to), no competitor named
(owner directive 2026-09-23), no "we are the best" claim.

Run from repo root: python3 seo/improve_realtors_best_card_2026_11_13.py
"""
import json
import re

DATE = "2026-11-13"
F = "digital-business-card-for-realtors.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. description ----------
m = re.search(r'<meta name="description" content="(.*?)"', s)
OLD_D = m.group(1)
ADD_D = " Includes a checklist for choosing the best digital business card for a real estate agent."
if ADD_D.strip() not in s:
    assert OLD_D.endswith("without reprinting anything."), "unexpected description"
    n = s.count(OLD_D)
    s = s.replace(OLD_D, OLD_D + ADD_D)
    changed.append("description x%d" % n)

# ---------- 2. choosing section ----------
MARK = "<!-- REALTORS-BEST-CARD-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container">'
          '<div class="section-head" style="margin-bottom:32px;"><h2>Setting up a realtor\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2 id="best-card">How to choose the best digital business card for a realtor</h2></div>'
    "<p>The best digital business card for a real estate agent is the one that still works on a busy "
    "Saturday: a buyer at an open house can save your number in seconds, the card is correct the day "
    "after you change brokerage, and it shows what your state requires. Check any card, ours included, "
    "against these six points before you print a QR code on a yard sign.</p>"
    '<table class="lp-table"><thead><tr><th>What to check</th><th>Why it matters in real estate</th>'
    "<th>What CompanyCard does</th></tr></thead><tbody>"
    "<tr><td><b>Nothing to install for the person receiving it</b></td><td>Open-house visitors and "
    "sellers will not download an app to keep an agent&rsquo;s number.</td><td>The card opens in any "
    "phone browser with a one-tap Save contact button.</td></tr>"
    "<tr><td><b>A QR code that never changes</b></td><td>Yard-sign riders, flyers and mailers stay out "
    "for months, long after they are printed.</td><td>Every card has a QR code and a sharing link; you "
    "edit the card and the printed code keeps working.</td></tr>"
    "<tr><td><b>Edits without a fee or a reprint</b></td><td>Agents change brokerage, phone numbers, "
    "designations and service areas.</td><td>Unlimited edits on every plan, including the free one.</td></tr>"
    "<tr><td><b>Room for brokerage and licence details</b></td><td>Many state commissions set rules for "
    "what an agent&rsquo;s advertising must show.</td><td>You add your brokerage name and licence number "
    "as fields on the card; see the <a href=\"#commission-rules\">commission rules section</a> below and "
    "check your own state.</td></tr>"
    "<tr><td><b>A way for visitors to send their details back</b></td><td>It replaces the paper sign-in "
    "sheet at an open house.</td><td>Lead capture and analytics are on Pro, not on the free plan.</td></tr>"
    "<tr><td><b>Matching cards for a team</b></td><td>A team or brokerage wants one logo and one layout "
    "on every agent&rsquo;s card.</td><td>Business adds a central admin dashboard and brand and template "
    "lock, with no seat minimum. It is bought by contacting us, not self-serve.</td></tr>"
    "</tbody></table>"
    "<p>What it costs: one card is free and carries a small CompanyCard credit under the card. Pro is "
    "$4.99 a month, or $3.99 a month billed yearly, and removes the credit while adding custom branding, "
    "lead capture and analytics. Business is $4.99 per user a month, or $3.99 billed yearly. If you only "
    "need a link and a QR code for your sign riders, the free card is enough; if you run open houses "
    "every weekend, the sign-in feature on Pro is the part worth paying for. See "
    "<a href=\"pricing.html\">pricing</a>.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# in-page link target for the existing commission-rules heading
OLD_H = "<h2>Real estate commission rules on brokerage names, licence numbers and advertising</h2>"
NEW_H = '<h2 id="commission-rules">Real estate commission rules on brokerage names, licence numbers and advertising</h2>'
if OLD_H in s:
    assert s.count(OLD_H) == 1
    s = s.replace(OLD_H, NEW_H)
    changed.append("anchor-id")
assert 'id="commission-rules"' in s, "commission-rules anchor missing"

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("What is the best digital business card for realtors?",
     "The best one for a real estate agent is the one that passes six checks: the person receiving it "
     "needs no app, the QR code keeps working after you edit the card, edits are unlimited, there is room "
     "for your brokerage name and licence number, visitors can send their details back at an open house, "
     "and a team can have matching cards. CompanyCard covers the first four on its free plan, which is one "
     "card with a small CompanyCard credit under it. Lead capture is on Pro at $4.99 a month, or $3.99 a "
     "month billed yearly, and matching team cards are on Business."),
    ("Is a free digital business card enough for a real estate agent?",
     "For many solo agents, yes. The free CompanyCard plan is one card with a QR code and a sharing link, "
     "your listings link, brokerage and licence details, and unlimited edits, and the person scanning it "
     "needs no app. It carries a small CompanyCard credit under the card. Pro removes the credit and adds "
     "custom branding, lead capture for open-house sign-ins and analytics."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions from realtors</h2>"
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
OLD_L = "- Digital business card for realtors: https://company-card.com/" + F
NEW_L = ("- Digital business card for realtors & real estate agents (open houses, brokerage and licence "
         "details, a six-point checklist for choosing the best card for an agent): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
