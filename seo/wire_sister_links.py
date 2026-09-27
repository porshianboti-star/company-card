# -*- coding: utf-8 -*-
"""Sister-product links in every footer (+ the template). Idempotent.

WHY. CompanyCard, ProSignature (prosignature.co) and MeetingBrand
(meetingbrand.com) are the owner's three products. Before this script, 15
pages carried a ProSignature link in the "Compare & Tools" footer column
(family A), 48 pages plus seo/_tpl_footer.txt carried the standard footer
without it (family B), and meetingbrand.com appeared nowhere in the repo.

WHAT. Every footer ends up with, in this order, inside "Compare & Tools":
    ... <li>ProSignature — Email Signatures</li>
        <li>MeetingBrand — Branded Meeting Backgrounds</li>
        <li>Email Signature Generator</li> ...
  * family A: the MeetingBrand <li> is inserted right after the existing
    ProSignature <li>;
  * family B (+ template): both <li>s are inserted right before the "Email
    Signature Generator" <li>, which is exactly where family A already has
    them, so the two families converge on one footer shape.
Never a whole-footer replace (the site has byte-distinct footer variants).
brand-kit.html (minimal footer) and the Google verification stub (no footer)
have no anchor and are left alone, as in every wire_batch*.py.

Run from repo root: python3 seo/wire_sister_links.py
"""
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

PS_LI = '<li><a href="https://prosignature.co/" rel="noopener">ProSignature — Email Signatures</a></li>'
MB_LI = '<li><a href="https://meetingbrand.com/" rel="noopener">MeetingBrand — Branded Meeting Backgrounds</a></li>'
ESG_LI = '<li><a href="email-signature-generator.html">Email Signature Generator</a></li>'

targets = sorted(f for f in os.listdir(".") if f.endswith(".html")) + ["seo/_tpl_footer.txt"]
fam_a = fam_b = already = no_anchor = 0
for fn in targets:
    h = open(fn, encoding="utf-8").read()
    if MB_LI in h:
        already += 1
        continue
    if PS_LI + ESG_LI in h:                       # family A
        assert h.count(PS_LI + ESG_LI) == 1, fn
        h = h.replace(PS_LI + ESG_LI, PS_LI + MB_LI + ESG_LI, 1)
        fam_a += 1
    elif ESG_LI in h:                             # family B (+ template)
        assert h.count(ESG_LI) == 1, (fn, h.count(ESG_LI))
        assert PS_LI not in h, ("ProSignature li present but not adjacent to the anchor", fn)
        h = h.replace(ESG_LI, PS_LI + MB_LI + ESG_LI, 1)
        fam_b += 1
    else:
        no_anchor += 1
        print("  no footer anchor, left alone: " + fn)
        continue
    open(fn, "w", encoding="utf-8").write(h)

print("family A (MeetingBrand added after ProSignature): %d" % fam_a)
print("family B (ProSignature + MeetingBrand added):      %d" % fam_b)
print("already wired: %d   no anchor: %d   total targets: %d" % (already, no_anchor, len(targets)))
