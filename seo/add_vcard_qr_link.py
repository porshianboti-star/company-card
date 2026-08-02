#!/usr/bin/env python3
"""Wire vcard-qr-code.html into the sitewide footer (batch 12, 2026-08-02).

The footer exists in ~10 byte-distinct variants across the site, so this patches
by a stable ANCHOR string rather than by replacing a whole footer block. The
anchor is the existing "QR Code Business Card" list item, which is present in 54
of the 56 root HTML files (the exceptions are brand-kit.html and the Google
Search Console verification stub, neither of which carries the standard footer).
The new link is placed immediately after it, which is also where it belongs
topically.

Idempotent: files that already contain the new link are skipped.

Run from the repo root:  python3 seo/add_vcard_qr_link.py
"""
import os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ANCHOR = '<li><a href="qr-code-business-card.html">QR Code Business Card</a></li>'
NEW = '<li><a href="vcard-qr-code.html">vCard QR Code</a></li>'

targets = sorted(glob.glob(os.path.join(ROOT, "*.html")))
targets.append(os.path.join(HERE, "_tpl_footer.txt"))

patched, skipped, missing = [], [], []
for path in targets:
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if NEW in html:
        skipped.append(os.path.basename(path))
        continue
    if ANCHOR not in html:
        missing.append(os.path.basename(path))
        continue
    html = html.replace(ANCHOR, ANCHOR + NEW)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    patched.append(os.path.basename(path))

print(f"patched {len(patched)} files")
print(f"already had the link: {len(skipped)}")
print(f"no footer anchor (expected: brand-kit, gsc stub): {missing}")
