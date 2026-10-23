#!/usr/bin/env python3
"""Improve business-card-for-business-owners.html (2026-10-23). Idempotent.

Why: GSC (28 days to 2026-10-21) shows the page is the closest thing the site
has to page 1 on a non-brand cluster — "what to put on business card as owner"
10 @ 12.6, "business card for owner of company" 8 @ 14.1 — with a long tail the
page does not answer in its own words: "sole proprietor title on business card"
2 @ 17.5, "proprietor designation on visiting card" 2 @ 32, "proprietor
business card" 2 @ 43.5, "co owner on business card" 2 @ 38.5, "business card
titles for owners" 1 @ 45, "how to put llc on business cards" 1 @ 50. The title
table lists Owner / Founder / Director / Principal / MD / CEO / the trade, but
never the words Sole Proprietor, Proprietor or Managing Member, and the page
says only that LLC/Ltd must not be claimed before registration — not where the
designator goes once the business IS registered.

What: (1) two rows added to the existing title table (Sole Proprietor /
Proprietor; Managing Member); (2) one new section, "Where LLC, Ltd or Inc goes
on the card", anchored before "Two or more co-owners"; (3) two FAQs, visible
first, then sync_faq_schema.py byte-matches the FAQPage JSON-LD; (4)
dateModified -> 2026-10-23 (the sitemap lastmod is bumped by the same script).
No prices are printed. No legal rule is asserted: naming requirements differ by
jurisdiction, and the page says to check your own registrar.

Run from repo root: python3 seo/improve_owners_titles_2026_10_23.py
"""
import re

DATE = "2026-10-23"
F = "business-card-for-business-owners.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. title table rows ----------
OWNER_ROW = ('<tr><td><b>Owner</b></td><td>Plain and unambiguous. You are the business.</td>'
             '<td>Sole proprietors, single-owner limited companies, trades. Never wrong.</td></tr>')
NEW_ROWS = (
    '<tr><td><b>Sole Proprietor</b> / <b>Proprietor</b></td>'
    '<td>A legal form, not a job. It says how the business is set up, not what you do.</td>'
    '<td>Where it is the customary designation on a visiting card, or when the reader is a bank or a '
    'supplier opening an account. For customers, Owner or the trade itself says the same thing in '
    'plainer words.</td></tr>'
    '<tr><td><b>Managing Member</b></td>'
    '<td>The owner who runs a US LLC, in the LLC&rsquo;s own vocabulary.</td>'
    '<td>Contracts, leases and bank paperwork, where who can sign matters. On a card handed to a '
    'customer it reads as jargon &mdash; use Owner there.</td></tr>'
)
if "<b>Sole Proprietor</b>" not in s:
    assert s.count(OWNER_ROW) == 1, "owner row not unique"
    s = s.replace(OWNER_ROW, OWNER_ROW + NEW_ROWS, 1)
    changed.append("table-rows")

# ---------- 2. LLC / Ltd section ----------
MARK = "<!-- OWNERS-LEGALFORM-2026-10 -->"
ANCHOR = ('<section class="section"><div class="container"><div class="section-head" '
          'style="margin-bottom:32px;"><h2>Two or more co-owners: three ways to handle it</h2>')
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>Where LLC, Ltd or Inc goes on the card</h2></div>'
    "<p>Once the business is registered, the designator belongs to the business name, not to you. "
    "Write the name once, as it is registered &mdash; &ldquo;Okafor Bookkeeping LLC&rdquo;, "
    "&ldquo;Okafor Bookkeeping Ltd&rdquo; &mdash; on the business-name line, and put a role next to "
    "your own name. &ldquo;Sam Okafor, Owner&rdquo; above &ldquo;Okafor Bookkeeping LLC&rdquo; reads "
    "correctly. &ldquo;Sam Okafor, LLC&rdquo; does not, because an LLC is a thing you own, not a "
    "title you hold.</p>"
    "<p>Whether the designator has to appear at all is a question for your own registrar. Some "
    "jurisdictions expect the registered name, suffix included, wherever the business presents "
    "itself; others let a registered company trade under a shorter name as long as the legal name is "
    "disclosed somewhere. This page cannot tell you which rule you are under, so check before you "
    "commit it to print or to the card.</p>"
    "<p>If you registered after you started handing out cards, this is the edit a digital card was "
    "made for. Change the business-name line once in the "
    "<a href=\"app/builder.html\">builder</a> and every QR code and link you have already given out "
    "shows the registered name, with no reprint.</p></div></section>\n"
)
if MARK not in s:
    assert s.count(ANCHOR) == 1, "co-owners anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1)
    changed.append("section")

# ---------- 3. FAQs (visible; sync_faq_schema.py then rewrites the JSON-LD) ----------
NEW_FAQS = [
    ("Should I put Sole Proprietor on my business card?",
     "Only where it is the customary designation on a visiting card, or when the card is for a bank "
     "or a supplier who needs to know how the business is set up. Sole Proprietor describes a legal "
     "form, not what you do, so for customers Owner or the trade itself — Plumber, Bookkeeper, "
     "Photographer — says the same thing in plainer words. Whichever you choose, use one title."),
    ("How do I put LLC on a business card?",
     "Attach it to the business name, not to your own name: “Sam Okafor, Owner” above "
     "“Okafor Bookkeeping LLC”. Write the registered name once, with the suffix, on the "
     "business-name line, and do not repeat it after your title. Whether the suffix must appear at "
     "all depends on your jurisdiction, so check your own registrar. On a digital card the name "
     "line is edited once and every card already shared shows the change."),
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

# ---------- 3b. FAQPage JSON-LD (questions appended; sync_faq_schema.py byte-matches answers) ----------
import json
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

print("changed:", ", ".join(changed) or "nothing (already applied)")
