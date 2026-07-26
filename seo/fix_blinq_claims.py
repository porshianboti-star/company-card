#!/usr/bin/env python3
"""Correct factually wrong competitor claims on blinq-alternative.html.

VERIFIED 2026-07-26 from blinq.me/pricing: Blinq's FREE tier includes two cards,
virtual backgrounds, personal email signatures and Apple Wallet. The page
previously implied CompanyCard "adds" those over Blinq — false, and the biggest
GEO risk on the site (assistants cross-check vendor pricing pages).

Real, checkable differentiators used instead:
  - Blinq Business requires a minimum of 5 team cards; CompanyCard has no seat
    minimum, so a 2-4 person business can run a branded team.
  - CompanyCard publishes flat pricing ($8 Pro / $12 Business per user).
Run from repo root: python3 fix_blinq_claims.py
"""
import sys, os

F = "blinq-alternative.html"
h = open(F, encoding="utf-8").read()
orig = h

REPS = [
# 1. og:description — drop the false "included per seat" differentiator framing
('<meta property="og:description" content="A digital business card alternative to Blinq, HiHello and Popl — no hardware to buy, free to start, with email signatures and video backgrounds included per seat.">',
 '<meta property="og:description" content="A digital business card alternative to Blinq, HiHello and Popl — no hardware to buy, no team seat minimum, and flat published pricing.">'),

# 2. Feature card — replace the false uniqueness claim with the verified one
('<div class="card"><h3>More in every seat</h3><p>A card is only part of the job. CompanyCard bundles a matching email signature and a branded video-call background for every employee.</p></div>',
 '<div class="card"><h3>No team minimum</h3><p>Blinq\'s Business plan bills a minimum of five team cards. CompanyCard has no seat minimum, so a two- or three-person business can run branded cards without paying for empty seats.</p></div>'),

# 3. Body prose — state plainly that Blinq includes these, and where we differ
('<p>Blinq is a polished digital business card platform with a free tier and paid team plans, and — like most in the space — it also sells NFC accessories. CompanyCard covers the same core sharing (QR, link, wallet, no app for the receiver) and adds a matching <a href="email-signature-generator.html">email signature</a> and a <a href="virtual-background-for-video-calls.html">video-call background</a> per seat, managed with locked brand templates from one dashboard.</p>',
 '<p>Blinq is a polished digital business card platform and a genuinely strong free tier: as of July 2026 its free plan includes two cards, an <a href="email-signature-generator.html">email signature</a>, a <a href="virtual-background-for-video-calls.html">virtual background</a> and Apple Wallet — so those are not points of difference, and we won\'t pretend they are. CompanyCard covers the same core sharing (QR, link, wallet, no app for the receiver). Where the two genuinely diverge is team pricing: Blinq\'s Business plan carries a minimum of five team cards, while CompanyCard has no seat minimum and publishes flat per-user pricing, which matters if your "team" is you and two other people.</p>'),

# 4. Table rows — replace non-differentiating rows with verified comparisons
('<tr><td><b>Email signature</b></td><td>Every email quietly shares your card</td><td>Included, matched to the card, per seat</td></tr>',
 '<tr><td><b>Team seat minimum</b></td><td>Small teams get locked out by 5-seat floors</td><td>No minimum — brand two people if that\'s your team</td></tr>'),
('<tr><td><b>Video-call background</b></td><td>Your card works the room on Zoom/Meet</td><td>Branded background included per seat</td></tr>',
 '<tr><td><b>Pricing transparency</b></td><td>Hidden pricing means a sales call before a number</td><td>Published flat rates — $8 Pro, $12 per user Business</td></tr>'),
]

for old, new in REPS:
    if h.count(old) != 1:
        sys.exit(f"ANCHOR MISS ({h.count(old)}x): {old[:90]}")
    h = h.replace(old, new)

# 5+6. FAQ answer appears twice (visible <details> and FAQPage JSON-LD) and must
# stay identical in both — Google requires schema to mirror visible text.
OLD_A = ("Yes. CompanyCard covers the same core job as Blinq — a digital business card you share by QR, link or wallet with no app for the receiver — and adds a matching email signature and a branded video-call background for every seat, with locked brand templates and one team dashboard. There is no hardware to buy, and the free plan is a full working card.")
NEW_A = ("It depends on what you need. Blinq has a strong free tier — as of July 2026 it includes two cards, an email signature, a virtual background and Apple Wallet — so those are not reasons to switch. The clearest reason to choose CompanyCard is team size and price: Blinq's Business plan bills a minimum of five team cards, while CompanyCard has no seat minimum and publishes flat pricing, so a two- or three-person business can run locked, branded cards without paying for empty seats.")

n = h.count(OLD_A)
if n != 2:
    sys.exit(f"FAQ answer expected 2x (visible + JSON-LD), found {n}")
h = h.replace(OLD_A, NEW_A)

open(F, "w", encoding="utf-8").write(h)
print(f"Fixed {len(REPS)} blocks + FAQ answer (2 copies). {len(orig)} -> {len(h)} bytes")
