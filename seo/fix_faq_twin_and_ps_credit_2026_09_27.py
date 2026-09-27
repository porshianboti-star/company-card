#!/usr/bin/env python3
"""Fix round 1, 2026-09-27 — two verifier findings, both on existing pages.

1. email-signature-generator.html — the hand-built clause "its free plan carries
   no watermark" about the sister product stopped being true on 2026-09-27:
   ProSignature's free plan now carries a small clickable 'Created with
   ProSignature' line under the signature and Pro removes it (ProSignature repo
   commits e838c58 and 13824dd, owner directive of the same day). Replace the
   clause, link the phrase to ProSignature's own explainer page (HTTP 200 on
   2026-09-27), and bump the page's dateModified + sitemap <lastmod>.

2. digital-business-card.html — the FAQPage Question 'What is a digital business
   card?' existed only in the JSON-LD. Add the <details class="lp-faq"> twin
   whose <p> is byte-identical to the JSON-LD answer (copied out of the JSON-LD
   at run time, never retyped), as the first FAQ item.

Idempotent: every step is a no-op once its result is in place.
Run from repo root:
  python3 seo/fix_faq_twin_and_ps_credit_2026_09_27.py
  python3 seo/sync_faq_schema.py      # must exit 0
  python3 seo/build_llms_full.py
"""
import json, re, sys

DATE = "2026-09-27"
PS_EXPLAINER = "https://prosignature.co/email-signature-no-watermark"

OLD_CLAUSE = "is built for exactly that, and its free plan carries no watermark.</p>"
NEW_CLAUSE = ("is built for exactly that, and its free plan is free forever — the signature "
              "carries one small clickable "
              f"<a href=\"{PS_EXPLAINER}\" rel=\"noopener\">'Created with ProSignature'</a> line, "
              "which Pro removes.</p>")

def read(f):  return open(f, encoding="utf-8").read()
def write(f, s): open(f, "w", encoding="utf-8").write(s)

def replace_once(h, old, new, f):
    n = h.count(old)
    assert n == 1, f"{f}: expected exactly one occurrence of {old[:60]!r}, found {n}"
    return h.replace(old, new, 1)

# ---- 1. email-signature-generator.html --------------------------------------
f = "email-signature-generator.html"
h = read(f)
if NEW_CLAUSE in h:
    print(f"  {f}: clause already fixed")
else:
    h = replace_once(h, OLD_CLAUSE, NEW_CLAUSE, f)
    assert h.count('"dateModified":"') == 1, f"{f}: expected one dateModified"
    h = re.sub(r'"dateModified":"\d{4}-\d{2}-\d{2}"', f'"dateModified":"{DATE}"', h)
    write(f, h)
    print(f"  {f}: clause replaced, dateModified -> {DATE}")

sm = read("sitemap.xml")
pat = re.compile(r"(<url><loc>https://company-card\.com/email-signature-generator\.html</loc><lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)")
assert pat.search(sm), "sitemap: no <url> for email-signature-generator.html"
sm2 = pat.sub(rf"\g<1>{DATE}\g<2>", sm)
if sm2 != sm:
    write("sitemap.xml", sm2); print(f"  sitemap.xml: lastmod -> {DATE}")
else:
    print("  sitemap.xml: lastmod already current")

# ---- 2. digital-business-card.html ------------------------------------------
f = "digital-business-card.html"
h = read(f)
Q = "What is a digital business card?"
ld = [b for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S) if '"FAQPage"' in b]
assert len(ld) == 1, f"{f}: expected one FAQPage block, found {len(ld)}"
answers = {q["name"].strip(): q["acceptedAnswer"]["text"] for q in json.loads(ld[0])["mainEntity"]}
assert Q in answers, f"{f}: JSON-LD has no question {Q!r}"
twin = f'<details class="lp-faq"><summary>{Q}</summary><p>{answers[Q]}</p></details>\n'
if twin in h:
    print(f"  {f}: visible twin already present")
else:
    anchor = '<details class="lp-faq"><summary>Is a digital business card free?</summary>'
    h = replace_once(h, anchor, twin + anchor, f)
    write(f, h)
    print(f"  {f}: visible lp-faq twin inserted as first FAQ item")

# Owner directive: a certain former-employer brand name must never appear on any surface.
for f in ("email-signature-generator.html", "digital-business-card.html", "sitemap.xml"):
    assert ("wise" + "stamp") not in read(f).lower(), f"forbidden brand name in {f}"
print("done")
