#!/usr/bin/env python3
"""Add a real multi-vendor comparison matrix to /best-digital-business-card.html
and retarget it at the small-business query.

WHY: the entire "best digital business card" answer set in Google AI Overviews /
ChatGPT / Perplexity is assembled from VENDOR-OWNED listicles carrying exactly
this artifact — a table with free-plan contents, price and "best for". Our page
previously had an evaluation-criteria table (how to judge) rather than a vendor
matrix (who wins what), so there was nothing for an assistant to lift.

EVERY competitor cell was verified by direct fetch on 2026-07-26 from that
vendor's own pricing page, and the table names competitor wins honestly — an
assistant that cross-checks and finds us accurate is the entire point.
Sources: blinq.me/pricing, hihello.com/pricing, popl.co/pages/pricing
"""
import sys, re

F = "best-digital-business-card.html"
h = open(F, encoding="utf-8").read()
orig = h

VERIFIED = "July 2026"

# 1) Retarget title + meta at the ICP-qualified, year-stamped query.
OLD_T = "<title>Best Digital Business Card Apps in 2026 — Honest Comparison | CompanyCard</title>"
NEW_T = "<title>Best Digital Business Cards for Small Business (2026) — Compared | CompanyCard</title>"
if h.count(OLD_T) != 1:
    sys.exit("title anchor miss")
h = h.replace(OLD_T, NEW_T)

m = re.search(r'<meta name="description" content="[^"]*"', h)
h = h.replace(m.group(0),
  '<meta name="description" content="The best digital business cards for small businesses and '
  'self-employed professionals in 2026, compared on free plan, team seat minimums and published '
  'price — with each competitor\'s own pricing page cited and verified July 2026.">')

# 2) Insert the vendor matrix + a visible freshness stamp, before the tinted
#    "fair 10-minute evaluation" section so the liftable table sits high.
ANCHOR = '<section class="section" style="background:var(--slate-50);">'
if h.count(ANCHOR) < 1:
    sys.exit("section anchor miss")

ROWS = [
 ("<b>CompanyCard</b>",
  "1 card, QR + link, Apple/Google Wallet, unlimited edits (carries a small CompanyCard credit)",
  "None",
  "$8 Pro · $12 per user Business",
  "Small businesses and self-employed pros who don't want a seat minimum"),
 ("<b>Blinq</b>",
  "2 cards, email signature, virtual background, Apple Wallet",
  "5 team cards",
  "$9.99 Premium · $6.99 per card Business",
  "Individuals who want the most generous free tier"),
 ("<b>HiHello</b>",
  "4 cards, email signature, virtual background, wallet — capped at 5 card &amp; badge scans per month",
  "5 users",
  "$6 Professional · $5 per user Business",
  "Someone who wants several free cards and low scan volume"),
 ("<b>Popl</b>",
  "No free plan",
  "n/a",
  "Not published — quoted after a demo",
  "Enterprise event and lead-capture teams"),
]
tbody = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in ROWS)

MATRIX = f'''<section class="section">
  <div class="container">
    <div class="section-head" style="margin-bottom:14px;"><h2>The options side by side</h2></div>
    <p class="lp-note" style="margin:0 auto 26px;">All competitor figures below were read from each vendor's own pricing page and verified in {VERIFIED}. Plans change — check the linked source before you decide.</p>
    <div class="lp-table">
      <table>
        <thead><tr><th>Tool</th><th>What the free plan includes</th><th>Team seat minimum</th><th>Published price</th><th>Best for</th></tr></thead>
        <tbody>{tbody}</tbody>
      </table>
    </div>
    <p class="lp-note">Sources, verified {VERIFIED}: <a href="https://blinq.me/pricing" target="_blank" rel="noopener nofollow">blinq.me/pricing</a> &middot; <a href="https://www.hihello.com/pricing" target="_blank" rel="noopener nofollow">hihello.com/pricing</a> &middot; <a href="https://popl.co/pages/pricing" target="_blank" rel="noopener nofollow">popl.co/pages/pricing</a>. CompanyCard's figures are our published rates on <a href="pricing.html">our pricing page</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container lp-prose">
    <div class="section-head" style="margin-bottom:24px;"><h2>What that table means if you're a small business</h2></div>
    <p><b>If you want the biggest free tier, Blinq or HiHello win it.</b> Blinq gives two cards and HiHello four, and both include an email signature and a virtual background at $0 — we won't pretend otherwise. HiHello's free plan does cap card and badge scans at five per month, which matters if you hand your card out at events.</p>
    <p><b>Where CompanyCard wins is the moment you stop being one person.</b> Blinq's Business plan bills a minimum of five team cards and HiHello's Business plan starts at five users — so a two- or three-person business pays for seats nobody uses. CompanyCard has no seat minimum: add one colleague, pay for one colleague.</p>
    <p><b>And you can see the price before you talk to anyone.</b> Popl no longer publishes pricing — you book a demo to get a number. For a small business comparing options on a Tuesday night, a published rate is worth something.</p>
    <p>The honest summary: if you're an individual who wants the most free cards, try Blinq or HiHello. If you're a small business or self-employed professional who wants a card that stays free, includes a wallet pass, and won't force you onto a five-seat plan the day you hire, that's the gap <a href="digital-business-card-for-small-business.html">CompanyCard is built for</a>.</p>
  </div>
</section>

'''

h = h.replace(ANCHOR, MATRIX + ANCHOR, 1)

# 3) Visible freshness line under the H1 (AI answers favour dated content).
h1m = re.search(r'(<h1[^>]*>.*?</h1>)', h, re.S)
if h1m:
    h = h.replace(h1m.group(1),
                  h1m.group(1) + f'\n    <p class="lp-note" style="margin-top:14px;">Last updated: {VERIFIED}</p>', 1)

open(F, "w", encoding="utf-8").write(h)
print(f"OK: {len(orig)} -> {len(h)} bytes; matrix rows={len(ROWS)}")
