#!/usr/bin/env python3
"""Goal-aligned identity fix + canonical free-plan spec.

WHY: audited 2026-07-26 — "small business", "self-employed", "solopreneur" and
"sole trader" appeared ZERO times sitewide, while every ICP query is
audience-qualified ("digital business card for small business"). Google's AI
Mode fans a prompt out into persona sub-queries; a page that never names the
persona cannot match the sub-query that decides the answer.

Also states the free plan identically everywhere (card count + wallet + the
CompanyCard credit) so assistants that cross-check pages see one consistent
spec instead of inferring an unlimited-cards claim we never made.

Run from repo root: python3 fix_identity_and_free.py
"""
import sys

# One canonical sentence, reused verbatim in entity schema + llms.txt.
CANON = ("CompanyCard is a digital business card for small business owners, "
         "self-employed professionals and teams — share your details by QR code, "
         "link, Apple or Google Wallet with no app for the person receiving it. "
         "A free plan is available.")

changes = []

# ---------------- index.html ----------------
f = "index.html"
h = open(f, encoding="utf-8").read()
o = h

R = [
 # Title: lead with the ICP + the free offer (the two things the ICP types)
 # NB: the live <title> uses a bare "&", the <h1> uses "&amp;" — match each exactly.
 ("<title>CompanyCard — The digital business card for people & teams</title>",
  "<title>Free Digital Business Card for Small Business & Self-Employed | CompanyCard</title>"),

 # H1: keep the animated-span structure, name the buyer
 ('<h1 class="fx" style="--d:.15s; margin-top:22px;">The digital business card<br><span class="gtext-anim">for people &amp; teams.</span></h1>',
  '<h1 class="fx" style="--d:.15s; margin-top:22px;">The digital business card<br><span class="gtext-anim">for small business &amp; self-employed pros.</span></h1>'),

 # Organization description = the canonical sentence
 ('"description":"The digital business card for people and teams."',
  f'"description":"{CANON}"'),

 # SoftwareApplication description names the audience too
 ('"description":"Digital business card builder for people and teams: QR code, sharing link, wallet pass, email signature and virtual background — no app required for the receiver."',
  '"description":"Digital business card builder for small business owners, self-employed professionals and teams: QR code, sharing link, Apple and Google Wallet pass, email signature and virtual background — no app required for the person receiving the card. Free plan available; no seat minimum on team plans."'),
]
for old, new in R:
    if h.count(old) != 1:
        sys.exit(f"[index] anchor {h.count(old)}x: {old[:80]}")
    h = h.replace(old, new)

# Meta description: name the ICP and the free offer
import re
m = re.search(r'<meta name="description" content="([^"]+)"', h)
if not m:
    sys.exit("[index] no meta description")
h = h.replace(m.group(0),
 '<meta name="description" content="CompanyCard is a free digital business card for small business owners and '
 'self-employed professionals. Share by QR code, link or Apple/Google Wallet — no app for the recipient, '
 'no seat minimum for small teams.">')
open(f, "w", encoding="utf-8").write(h)
changes.append((f, len(o), len(h)))

# ---------------- free-digital-business-card.html ----------------
# State the card count + wallet + the credit line explicitly. The page said
# "unlimited edits" (true) but never the card count, so a model could infer
# unlimited CARDS. Being explicit is what makes the fact quotable.
f = "free-digital-business-card.html"
h = open(f, encoding="utf-8").read()
o = h
OLD = ("<p class=\"lead\">Everything you need to network like it's this decade — card, QR code, link and unlimited edits — free. No credit card, no 14-day countdown.</p>")
NEW = (OLD +
       "\n<p style=\"max-width:680px;margin:14px auto 0;\"><b>Exactly what free includes:</b> one digital business card, QR code and sharing link, "
       "your profile, links and socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no credit card. "
       "Cards on the free plan carry a small CompanyCard credit; removing it is part of Pro. There is no seat minimum if you "
       "later add a colleague.</p>")
if h.count(OLD) != 1:
    # fall back: insert after the lead paragraph
    sys.exit(f"[free] anchor {h.count(OLD)}x")
h = h.replace(OLD, NEW)
open(f, "w", encoding="utf-8").write(h)
changes.append((f, len(o), len(h)))

for f, a, b in changes:
    print(f"  {f}: {a} -> {b} bytes")
print("CANON:", CANON)
