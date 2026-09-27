#!/usr/bin/env python3
"""Generate llms-full.txt from facts that are already published — nothing new.

Evidence rule (same as the ProSignature site): llms-full.txt may only contain
(1) llms.txt verbatim, (2) the one-voice plan facts from seo/facts.py, which
were read from pricing.html, and (3) for every page in sitemap.xml, its
<title>, canonical URL, meta description and the visible FAQ questions and
answers extracted with the same regex sync_faq_schema.py uses. No sentence is
written here that a visitor cannot read on the live site. OpenAI publishes no
commitment to llms.txt, so this is a consistency artefact, not a ranking lever.

Run from repo root: python3 seo/build_llms_full.py
"""
import re, html as ht, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import VERIFIED_HUMAN, FACTS_PLAIN, facts_table_plain

def text(s):
    return re.sub(r"\s+", " ", ht.unescape(re.sub(r"<[^>]+>", "", s))).strip()

def visible_faqs(body):
    out = []
    for m in re.finditer(r'<details class="lp-faq"><summary>(.*?)</summary>(.*?)</details>', body, re.S):
        out.append((text(m.group(1)), text(m.group(2))))
    return out

sm = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>(https://company-card\.com/[^<]*)</loc>", sm)

parts = [open("llms.txt", encoding="utf-8").read().rstrip(), ""]
parts += [f"## Verified plan facts (read from https://company-card.com/pricing.html on {VERIFIED_HUMAN})",
          FACTS_PLAIN, "", facts_table_plain(), "",
          "## Page-by-page: title, description and the FAQ shown on each page",
          "Every answer below is the visible FAQ text of that page, byte-identical to its FAQPage structured data.", ""]

n_pages = n_faq = 0
for loc in locs:
    f = "index.html" if loc == "https://company-card.com/" else loc.split("company-card.com/")[1]
    if not os.path.exists(f):
        continue
    h = open(f, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", h, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    body = re.sub(r'<script type="application/ld\+json">.*?</script>', "", h, flags=re.S)
    faqs = visible_faqs(body)
    parts.append(f"### {text(title.group(1)) if title else f}")
    parts.append(f"URL: {loc}")
    if desc:
        parts.append(f"Description: {text(desc.group(1))}")
    for q, a in faqs:
        parts.append(f"Q: {q}")
        parts.append(f"A: {a}")
    parts.append("")
    n_pages += 1; n_faq += len(faqs)

out = "\n".join(parts).rstrip() + "\n"
# Owner directive: a certain former-employer brand name must never appear on any surface.
# Spelled in two halves so this guard itself never fails the repo-wide grep.
assert ("wise" + "stamp") not in out.lower(), "forbidden brand name in output"
open("llms-full.txt", "w", encoding="utf-8").write(out)
print(f"llms-full.txt: {n_pages} pages, {n_faq} Q&A, {len(out.encode())//1024} KB")
