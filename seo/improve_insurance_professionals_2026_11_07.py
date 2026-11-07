#!/usr/bin/env python3
"""Improve digital-business-card-for-insurance-agents.html for the "insurance professionals" queries (2026-11-07). Idempotent.

Why: GSC (28 days to early November) shows "insurance professionals digital
business cards" 9 @ 26.4, "digital business cards for insurance professionals"
7 @ 46.9 and "insurance sales digital business cards" 4 @ 40.5 (20 impressions,
0 clicks). The page is written for one agent; the title says "Agents & Brokers"
and never "insurance professionals" or covers an agency that wants a card for
every producer and account manager.

What: (1) title / og / twitter -> "Digital Business Cards for Insurance Agents,
Brokers & Insurance Professionals" (keeps every word the current title ranks
for; H1 unchanged); description names agencies and sales teams; (2) one new
section, "Cards for insurance professionals across an agency", anchored before
"Setting up an insurance agent's card", with a by-role table (producer / agent,
account manager or CSR, agency principal, printed cards); (3) two FAQs, visible
first, FAQPage JSON-LD Questions appended, then sync_faq_schema.py byte-matches;
(4) dateModified + sitemap lastmod -> 2026-11-07; llms.txt line updated.

Facts: every plan fact and price is from seo/facts.py (Free = one card with a
small clickable CompanyCard credit; Pro $4.99 / $3.99 yearly adds custom
branding, lead capture and analytics and removes the credit; Business $4.99 /
$3.99 per user, no seat minimum, central admin dashboard, brand and template
lock, bought by contacting us). The new text does NOT repeat the "Apple and
Google Wallet pass" claim (owner decision pending since 2026-10-29). No
statistic, no new licensing or regulatory rule (the page's existing regulator
section is left as is), no competitor (owner directive 2026-09-23).

Run from repo root: python3 seo/improve_insurance_professionals_2026_11_07.py
"""
import json
import re

DATE = "2026-11-07"
F = "digital-business-card-for-insurance-agents.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title + description ----------
OLD_T = "Digital Business Card for Insurance Agents &amp; Brokers | CompanyCard"
NEW_T = "Digital Business Cards for Insurance Agents, Brokers &amp; Insurance Professionals | CompanyCard"
if OLD_T in s:
    n = s.count(OLD_T)
    s = s.replace(OLD_T, NEW_T)
    changed.append("title x%d" % n)
OLD_D = ("A digital business card for insurance agents and brokers — carry your licence details, make quoting "
         "one tap, and update your card without reprinting a thing.")
NEW_D = ("Digital business cards for insurance agents, brokers and insurance professionals — carry your licence "
         "details, make quoting one tap, give every producer and account manager in an agency a card, and "
         "update it without reprinting a thing.")
if OLD_D in s:
    n = s.count(OLD_D)
    s = s.replace(OLD_D, NEW_D)
    changed.append("description x%d" % n)

# ---------- 2. agency section ----------
MARK = "<!-- INSURANCE-PROFESSIONALS-2026-11 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);"><div class="container">'
          '<div class="section-head" style="margin-bottom:32px;"><h2>Setting up an insurance agent\'s card</h2></div>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Cards for insurance professionals across an agency</h2></div>'
    "<p>Insurance sales is rarely one person. A client may get a quote from a producer, have their "
    "renewal handled by an account manager and call the agency principal when something goes wrong. "
    "Each of them can have their own CompanyCard, built on the same design, so the client always knows "
    "who they are dealing with and how to reach the agency.</p>"
    "<table class=\"lp-table\"><thead><tr><th>Role</th><th>What the card puts first</th></tr></thead><tbody>"
    "<tr><td><b>Producer or agent</b></td><td>Name, role, the lines they write, the licence details "
    "they already show, and a one-tap way to ask for a quote or book a review call.</td></tr>"
    "<tr><td><b>Account manager or service rep</b></td><td>A direct line and email for changes, "
    "certificates and renewals, so service requests reach the right person instead of the main "
    "switchboard.</td></tr>"
    "<tr><td><b>Agency principal or owner</b></td><td>The agency&rsquo;s name, website and main "
    "number, and the person to contact when a client wants to escalate.</td></tr>"
    "<tr><td><b>Printed cards and closing folders</b></td><td>Print the QR code from each person&rsquo;s "
    "CompanyCard. A client who scans it saves the details as they are today, so the print stays useful "
    "after a phone number, a title or a carrier changes.</td></tr>"
    "</tbody></table>"
    "<p>A single independent agent only needs one card, and the free plan covers it; it carries a small "
    "CompanyCard credit under the card. Pro is $4.99 a month, or $3.99 a month billed yearly, and adds "
    "custom branding, lead capture so a prospect can leave their name and email from your card, and "
    "analytics, and removes the credit. For an agency, Business is priced per user with no seat minimum, "
    "so an agency of three pays for three; it adds a central admin dashboard and brand and template lock, "
    "and is set up by <a href=\"contact.html\">talking to us</a>. See <a href=\"pricing.html\">pricing</a>.</p>"
    "</div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "setting-up anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# ---------- 3. FAQs (visible, then JSON-LD Questions appended) ----------
NEW_FAQS = [
    ("Can an insurance agency give every producer and account manager a digital business card?",
     "Yes. Each person gets their own card with their own direct line, email and booking or quote link, "
     "on one shared design. The Business plan is priced per user with no seat minimum, at $4.99 per user a "
     "month or $3.99 per user a month billed yearly, and adds a central admin dashboard and brand and "
     "template lock so every card in the agency stays consistent. Business is set up by contacting us. "
     "A single independent agent only needs one card, and the free plan covers it."),
    ("What should an insurance sales professional put on a digital business card?",
     "Your name and role, the agency's name, the lines you write, the licence details you already show "
     "on your other materials, a phone number and email, and one clear next step such as requesting a "
     "quote or booking a review call. On a CompanyCard those details open from a link or a QR code, and "
     "every one of them can be edited later without handing out a new card."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions from insurance agents</h2>"
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
OLD_L = "- Digital business card for insurance agents: https://company-card.com/" + F
NEW_L = ("- Digital business cards for insurance agents, brokers & insurance professionals (licence details, "
         "one-tap quotes, a card for every producer and account manager in an agency, QR code for printed "
         "cards): https://company-card.com/" + F)
if OLD_L in ll:
    open("llms.txt", "w", encoding="utf-8").write(ll.replace(OLD_L, NEW_L, 1))
    changed.append("llms")

print("changed:", ", ".join(changed) or "nothing (already applied)")
