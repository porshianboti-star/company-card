#!/usr/bin/env python3
"""Improve digital-business-card-maker.html (2026-10-05). Idempotent.

Why: GSC (3 months to 2026-10-02), queries containing "maker": 398 impressions,
0 clicks. The largest cluster is the generic "business card maker online /
free online" wording (business card maker online 40 @ 84.8, business card
maker free online 30 @ 80.0, business card online maker 28 @ 83.9, online free
business card maker 26 @ 75.8, free online business card maker 25 @ 80.3,
online business card maker free 23 @ 81.4). The page's title, H1 and meta
never said "online business card maker" or "free business card maker".

What: (1) title/og/WebPage name lead with "Free Online Business Card Maker";
(2) H1 names the free online business card maker; (3) meta description leads
with the same words; (4) one section, "What the free online maker makes",
stating only what the page's own mini builder and seo/facts.py support (six
fields, live preview, QR, .vcf download, no signup to try; free plan = 1 card
with a small credit; Pro removes it); (5) two FAQs, visible and in FAQPage
JSON-LD. No prices printed. Page-only date stamp (add_freshness.py NOT run).

Run from repo root: python3 seo/improve_maker_2026_10_05.py
"""
import json, re

F = "digital-business-card-maker.html"
SM = "sitemap.xml"
DATE = "2026-10-05"
s = open(F, encoding="utf-8").read()
changed = []

OLD_T = "Digital Business Card Maker — Design Your Card Online Free | CompanyCard"
NEW_T = "Free Online Business Card Maker — Digital Card, QR &amp; Link | CompanyCard"
NEW_T_LD = "Free Online Business Card Maker — Digital Card, QR & Link | CompanyCard"
if OLD_T in s:
    s = s.replace(f"<title>{OLD_T}</title>", f"<title>{NEW_T}</title>")
    s = s.replace(f'"name":"{OLD_T}"', f'"name":"{NEW_T_LD}"')
    s = s.replace(OLD_T, NEW_T)  # og:title / twitter:title attributes
    changed.append("title")

OLD_D = ('content="Make a digital business card online, free: type your details, watch the live '
         'preview and QR code update, download it or save it as a real card with a permanent '
         'link. No signup to try."')
NEW_D = ('content="Free online business card maker: type your details, watch the live preview '
         'and QR code update, download the QR or .vcf, or save it as a digital card with a '
         'permanent link. No signup to try."')
if OLD_D in s:
    s = s.replace(OLD_D, NEW_D); changed.append("meta")

OLD_H1 = ('The business card maker where <span class="gradient-text">nothing goes to print.</span></h1>')
NEW_H1 = ('The free online business card maker where <span class="gradient-text">nothing goes '
          'to print.</span></h1>')
if OLD_H1 in s:
    s = s.replace(OLD_H1, NEW_H1, 1); changed.append("h1")
assert NEW_H1 in s, "H1 not found"

MARK = "<!-- MAKER-ONLINE-FREE-2026-10 -->"
SECTION = (
    MARK +
    '<section class="section"><div class="container lp-prose"><div class="section-head" '
    'style="margin-bottom:24px;"><h2>What the free online maker makes</h2></div>'
    "<p>This is an online business card maker, so there is nothing to install: it runs in the "
    "browser on this page. Fill in six fields and the card and its QR code are drawn as you type. "
    "You can try it without an account and download the QR code or a .vcf contact file straight "
    "away.</p>"
    "<p>What it makes is a digital card, not a print file. Save it as a CompanyCard and you get a "
    "permanent link, a scannable QR code and an Apple Wallet or Google Wallet pass, all on the "
    "free plan. The free plan is one card and it carries a small clickable CompanyCard credit "
    "under the card; Pro removes the credit and adds custom branding, lead capture and "
    "analytics. See <a href=\"pricing.html\">pricing</a> for the current rates.</p>"
    "<p>If you also want paper, print a plain card with your name and the downloaded QR code. "
    "The printed card then never goes out of date, because the details live behind the code and "
    "you can edit them as often as you like.</p></div></section>\n"
)
ANCHOR = ('<section class="section">\n  <div class="container lp-prose">\n    <div class="section-head" '
          'style="margin-bottom:32px;"><h2>From card makers to card platforms</h2>')
if MARK not in s:
    assert s.count(ANCHOR) == 1, "section anchor not unique"
    s = s.replace(ANCHOR, SECTION + ANCHOR, 1); changed.append("section")

NEW_FAQS = [
    ("Is this an online business card maker I can use without signing up?",
     "Yes. The maker runs in your browser on this page: fill in your details, watch the card and "
     "QR code update, and download the QR code or a .vcf file without an account. Saving it as a "
     "CompanyCard with a permanent link is free and needs a free account."),
    ("Can I print the business card I make here?",
     "The maker produces a digital card rather than a print file. To combine it with paper, "
     "download the QR code and print it on a simple card; anyone who scans it opens your digital "
     "card, which you can keep editing without reprinting."),
]

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

FAQ_RE = r'<h2>Frequently asked questions</h2></div>.*?</details>\n  </div>\n</section>'
for q, a in NEW_FAQS:
    if f"<summary>{esc(q)}</summary>" not in s:
        m = re.search(FAQ_RE, s, re.S)
        assert m, "FAQ section not found"
        block = m.group(0)
        new_block = block.replace("</details>\n  </div>\n</section>",
                                  f'</details>\n<details class="lp-faq"><summary>{esc(q)}</summary>'
                                  f"<p>{esc(a)}</p></details>\n  </div>\n</section>")
        s = s.replace(block, new_block, 1); changed.append("faq-visible")

m = re.search(r'<script type="application/ld\+json">(\{"@context": ?"https://schema.org", ?"@type": ?"FAQPage".*?)</script>', s, re.S)
assert m, "FAQPage JSON-LD not found"
data = json.loads(m.group(1))
names = {q["name"] for q in data["mainEntity"]}
for q, a in NEW_FAQS:
    if q not in names:
        data["mainEntity"].append({"@type": "Question", "name": q,
                                   "acceptedAnswer": {"@type": "Answer", "text": a}})
        changed.append("faq-schema")
s = s.replace(m.group(1), json.dumps(data, ensure_ascii=False), 1)

if changed:
    s = re.sub(r'"dateModified":"\d{4}-\d{2}-\d{2}"', f'"dateModified":"{DATE}"', s)
    sm = open(SM, encoding="utf-8").read()
    sm = re.sub(r'(<loc>https://company-card.com/digital-business-card-maker.html</loc><lastmod>)[\d-]+',
                rf"\g<1>{DATE}", sm)
    open(SM, "w", encoding="utf-8").write(sm)

open(F, "w", encoding="utf-8").write(s)
print("changed:", ", ".join(changed) or "nothing (already applied)")
