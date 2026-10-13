#!/usr/bin/env python3
"""Improve digital-business-card.html (2026-10-13). Idempotent.

Why: GSC Page indexing 2026-10-13 moved this page to "Crawled - currently not
indexed" (live URL Inspection: "URL is not on Google", last crawl 2026-08-22).
Technically clean (self-canonical, no noindex, bare slug 301s, linked from 70
pages, <=11% 8-gram overlap with any other page), so the problem is value:
the page repeated the homepage pitch and carried an unverified third-party
market-size statistic (rule 1: never state numbers we have not verified).

What: (1) delete the market-size paragraph; (2) new section "What the other
person sees when you share your card" (receiver mechanics; links to the vCard
and VCF explainers); (3) new section "What to check before you choose a
digital business card", built only on seo/facts.py, naming no competitor and
stating our limits (free = one card with a credit); (4) a by-profession hub of
internal links to pages that exist; (5) two FAQs, visible + FAQPage JSON-LD;
(6) visible "Last updated", WebPage dateModified and sitemap lastmod -> today.
No prices printed in new text, so a reprice cannot leave it stale.

Run from repo root: python3 seo/improve_dbc_hub_2026_10_13.py
"""
import json, os, re

DATE, HUMAN = "2026-10-13", "13 October 2026"
F = "digital-business-card.html"
s = open(F, encoding="utf-8").read()
changed = []

# 1. unverified statistic
STAT = re.compile(r'\n<p>Industry analysts expect the digital business card market.*?</p>', re.S)
if STAT.search(s):
    s = STAT.sub("", s, count=1); changed.append("stat-removed")
assert "Allied" not in s

# 2-4. sections, inserted before "Who uses digital business cards?"
MARK = "<!-- DBC-HUB-2026-10 -->"
ANCHOR = ('<section class="section" style="background:var(--slate-50);">\n  <div class="container lp-prose">\n'
          '    <div class="section-head" style="margin-bottom:32px;"><h2>Who uses digital business cards?</h2>')

PROFS = [
    ("small business owners", "digital-business-card-for-small-business.html"),
    ("business owners", "business-card-for-business-owners.html"),
    ("freelancers", "digital-business-card-for-freelancers.html"),
    ("consultants", "digital-business-card-for-consultants.html"),
    ("coaches", "digital-business-card-for-coaches.html"),
    ("realtors", "digital-business-card-for-realtors.html"),
    ("mortgage brokers", "digital-business-card-for-mortgage-brokers.html"),
    ("insurance agents", "digital-business-card-for-insurance-agents.html"),
    ("accountants", "digital-business-card-for-accountants.html"),
    ("bookkeepers", "digital-business-card-for-bookkeepers.html"),
    ("lawyers", "digital-business-card-for-lawyers.html"),
    ("notaries", "digital-business-card-for-notaries.html"),
    ("therapists", "digital-business-card-for-therapists.html"),
    ("dentists", "digital-business-card-for-dentists.html"),
    ("chiropractors", "digital-business-card-for-chiropractors.html"),
    ("personal trainers", "digital-business-card-for-personal-trainers.html"),
    ("tutors", "digital-business-card-for-tutors.html"),
    ("photographers", "digital-business-card-for-photographers.html"),
    ("salons", "digital-business-card-for-salons.html"),
    ("event planners", "digital-business-card-for-event-planners.html"),
    ("contractors", "digital-business-card-for-contractors.html"),
    ("electricians", "digital-business-card-for-electricians.html"),
    ("plumbers", "digital-business-card-for-plumbers.html"),
    ("landscapers", "digital-business-card-for-landscapers.html"),
    ("cleaners", "digital-business-card-for-cleaners.html"),
    ("recruiters", "digital-business-card-for-recruiters.html"),
    ("sales teams", "digital-business-card-for-sales-teams.html"),
    ("teams", "digital-business-cards-for-teams.html"),
    ("events and conferences", "digital-business-card-for-events.html"),
]
for _, href in PROFS:
    assert os.path.exists(href), href

def sec(bg, h2, body):
    style = ' style="background:var(--slate-50);"' if bg else ""
    return ('<section class="section"%s>\n  <div class="container lp-prose">\n'
            '    <div class="section-head" style="margin-bottom:32px;"><h2>%s</h2></div>\n%s\n  </div>\n</section>\n\n'
            % (style, h2, body))

RECEIVER = sec(False, "What the other person sees when you share your card", (
    "<p><b>They open a web page, not an app.</b> Scanning your QR code or tapping your link opens your card "
    "in the phone's browser. Nothing is installed and nobody is asked to sign up, on iPhone or Android.</p>\n"
    "<p><b>They tap Save contact.</b> The card hands their phone a contact file (a vCard, the <code>.vcf</code> "
    "format every contacts app reads), and your name, title, company, phone, email, photo and links land in "
    "their contacts in one step. If you want the detail, see <a href=\"vcard-qr-code.html\">how a vCard QR code "
    "works</a> and <a href=\"open-vcf-file.html\">how to open a VCF file</a>.</p>\n"
    "<p><b>The link keeps working after you change.</b> The QR code points at your card's address, not at a "
    "frozen copy of your details, so the next person who scans the same code sees your current number and "
    "title. A contact someone has already saved to their phone is their copy; opening your card again shows "
    "them the new version.</p>"))

CHECKLIST = sec(True, "What to check before you choose a digital business card", (
    "<p>Most digital business card apps look alike on a landing page. These are the questions that decide "
    "whether one fits a small business or a self-employed professional, with CompanyCard's own answers.</p>\n"
    "<p><b>Does the receiver need an app?</b> They should not. A CompanyCard opens in any browser with a "
    "one-tap Save contact button.</p>\n"
    "<p><b>What does the free plan actually include?</b> Ours is one card with a QR code, a sharing link, an "
    "Apple and Google Wallet pass and unlimited edits, with no scan cap and no credit card. The limits: it is "
    "one card, and it carries a small clickable CompanyCard credit under the card. Pro removes the credit and "
    "adds lead capture, analytics and custom branding.</p>\n"
    "<p><b>Is the price published, and is there a seat minimum?</b> Our prices are on the "
    "<a href=\"pricing.html\">pricing page</a>, flat per plan, and the Business plan has no seat minimum, so a "
    "two-person business pays for two cards.</p>\n"
    "<p><b>Can you leave without losing your contacts?</b> Contacts people save from your card are vCards in "
    "their own phones, so they stay where they are whatever you do with your account.</p>"))

links = " · ".join('<a href="%s">%s</a>' % (h, n) for n, h in PROFS)
HUB = sec(False, "Digital business cards by profession", (
    "<p>The basics above apply to everyone. These pages cover what a card needs to do in a specific line of "
    "work, from booking links for coaches to emergency call-outs for plumbers:</p>\n<p>" + links + "</p>"))

if MARK not in s:
    assert s.count(ANCHOR) == 1, s.count(ANCHOR)
    s = s.replace(ANCHOR, MARK + "\n" + RECEIVER + CHECKLIST + HUB + ANCHOR, 1)
    changed.append("sections")

# 5. FAQs
NEW_FAQS = [
    ("What does the other person see when I share my digital business card?",
     "They see your card as a web page in their phone's browser, with no app to install and no sign-up. "
     "A Save contact button adds your name, title, company, phone, email, photo and links to their contacts "
     "as a vCard, on iPhone or Android."),
    ("What should I check before choosing a digital business card?",
     "Check that the receiver needs no app, what the free plan includes and what it limits, whether the "
     "price is published and whether teams have a seat minimum. CompanyCard's free plan is one card with a "
     "QR code, sharing link, Apple and Google Wallet pass and a small CompanyCard credit; prices are on the "
     "pricing page and the Business plan has no seat minimum."),
]
esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
LAST = re.search(r'(What happens if I change jobs or get promoted\?</summary><p>.*?</p></details>)', s, re.S).group(1)
tpl = re.search(r'(<details[^>]*><summary>)What happens if I change jobs', s).group(1)
add = ""
for q, a in NEW_FAQS:
    if "<summary>%s</summary>" % esc(q) not in s:
        add += "\n" + tpl + esc(q) + "</summary><p>" + esc(a) + "</p></details>"
if add:
    s = s.replace(LAST, LAST + add, 1); changed.append("faq-visible")

m = re.search(r'<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"FAQPage".*?)</script>', s, re.S)
data = json.loads(m.group(1))
names = {q["name"] for q in data["mainEntity"]}
for q, a in NEW_FAQS:
    if q not in names:
        data["mainEntity"].append({"@type": "Question", "name": q,
                                   "acceptedAnswer": {"@type": "Answer", "text": a}})
        changed.append("faq-schema")
s = s.replace(m.group(1), json.dumps(data, ensure_ascii=False, separators=(",", ":")), 1)

# 6. dates
s2 = re.sub(r'Last updated: [0-9]+ \w+ 2026', "Last updated: " + HUMAN, s, count=1)
fm = re.search(r'FRESH:BEGIN.*?FRESH:END', s2, re.S)
fb = re.sub(r'"dateModified":"[^"]+"', '"dateModified":"%s"' % DATE, fm.group(0))
s2 = s2.replace(fm.group(0), fb, 1)
if s2 != s:
    s = s2; changed.append("dates")
open(F, "w", encoding="utf-8").write(s)

sm = open("sitemap.xml", encoding="utf-8").read()
sm2 = re.sub(r'(<loc>https://company-card.com/digital-business-card.html</loc><lastmod>)[^<]+', r'\g<1>' + DATE, sm, count=1)
if sm2 != sm:
    open("sitemap.xml", "w", encoding="utf-8").write(sm2); changed.append("sitemap")
print("changed:", ", ".join(changed) or "nothing (already applied)")
