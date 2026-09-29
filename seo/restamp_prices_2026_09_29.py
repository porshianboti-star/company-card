#!/usr/bin/env python3
"""Date stamps that sit next to OUR prices must say when those prices were read.

seo/reprice_2026_09_29.py rewrote the price bullets and the cost-page table rows
but left two stamps behind:

1. llms.txt: "## Pricing (published; read from https://company-card.com/pricing.html
   on 27 September 2026)". On 27 September the page showed other prices (Pro
   $7.99/$5.99, Business $12/$10), so the heading dated the new prices two days
   before they existed. The heading is now derived from seo/facts.py
   VERIFIED_HUMAN (the one voice every FACTS block already uses); any older date
   in that heading is replaced, so a later re-price only has to bump facts.py
   and re-run this script. build_llms_full.py copies llms.txt verbatim, so run
   it afterwards.

2. digital-business-card-cost.html: the vendor table is headed "verified
   1 September 2026", which stays true for the other vendors, but its
   CompanyCard row carries the 29 September prices. The row gets its own date
   note, and the source note under the table says which rows were re-read.

Idempotent (marker-guarded, anchors asserted to occur exactly once).
Run from repo root:
  python3 seo/restamp_prices_2026_09_29.py
  python3 seo/build_llms_full.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import VERIFIED_HUMAN

changed = []

# ---------------------------------------------------------------- 1. llms.txt
HEAD_RE = re.compile(r"^## Pricing \(published; read from https://company-card\.com/pricing\.html on ([^)]+)\)$", re.M)
p = "llms.txt"
s = open(p, encoding="utf-8").read()
hits = HEAD_RE.findall(s)
assert len(hits) == 1, f"{p}: pricing heading found {len(hits)} times"
new = HEAD_RE.sub(f"## Pricing (published; read from https://company-card.com/pricing.html on {VERIFIED_HUMAN})", s)
if new != s:
    open(p, "w", encoding="utf-8").write(new)
    changed.append(p)

# ---------------------------------------------------------------- 2. cost page
p = "digital-business-card-cost.html"
s = open(p, encoding="utf-8").read()
MARK = "<!--cc-row-date-->"
if MARK not in s:
    ROW_OLD = "<tr><td><b>CompanyCard</b></td><td>Yes — 1 card, carries a small CompanyCard credit</td><td>Pro $5.99/mo"
    ROW_NEW = (f"<tr><td><b>CompanyCard</b>{MARK}<br><small>our prices, read {VERIFIED_HUMAN}</small></td>"
               "<td>Yes — 1 card, carries a small CompanyCard credit</td><td>Pro $5.99/mo")
    NOTE_OLD = "v1ce.co/pricing, popl.co/pages/pricing. Prices change;"
    NOTE_NEW = (f"v1ce.co/pricing, popl.co/pages/pricing. CompanyCard's row (from our own pricing page) and Wave "
                f"Connect's billing periods were re-read on {VERIFIED_HUMAN}. Prices change;")
    for old in (ROW_OLD, NOTE_OLD):
        assert s.count(old) == 1, f"{p}: anchor found {s.count(old)} times: {old[:60]!r}"
    styles_before = re.findall(r"<style[^>]*>.*?</style>", s, re.S)
    n_script, n_head = s.count("<script"), s.count("</head>")
    s2 = s.replace(ROW_OLD, ROW_NEW).replace(NOTE_OLD, NOTE_NEW)
    assert re.findall(r"<style[^>]*>.*?</style>", s2, re.S) == styles_before
    assert s2.count("<script") == n_script and s2.count("</head>") == n_head
    open(p, "w", encoding="utf-8").write(s2)
    changed.append(p)

assert ("wise" + "stamp") not in open("llms.txt", encoding="utf-8").read().lower()
print("changed:", ", ".join(changed) if changed else "nothing (already stamped)")
