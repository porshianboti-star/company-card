#!/usr/bin/env python3
"""Add a "Built for how you work" section to the homepage that links, in body
copy, to the audience and profession pages.

WHY THIS IS THE HIGHEST-VALUE REMAINING ON-SITE FIX:
GSC reports "Crawled - currently not indexed" on some URLs, and the 18 pages
added this pass were reachable ONLY from the sitewide footer — the weakest
internal-link position there is. The homepage is the most-crawled page on the
domain; body links from it are how discovery and weight actually flow. Before
this change: body links to the new pages = 0.

It also puts the ICP phrases in homepage body copy, which is what a persona
sub-query ("digital business card for a plumber") needs to match.

Idempotent, marker-bounded. Run from repo root.
"""
import sys, re

F = "index.html"
MARK = "<!-- AUDIENCE:BEGIN -->"
ENDMARK = "<!-- AUDIENCE:END -->"

h = open(F, encoding="utf-8").read()
orig = h

if MARK in h and ENDMARK in h:
    h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)

AUDIENCE = [
 ("Small business owners", "digital-business-card-for-small-business.html",
  "One card your whole business shares — and no five-seat minimum the day you hire."),
 ("Freelancers &amp; self-employed", "digital-business-card-for-freelancers.html",
  "You are the brand. One link for your work, your contact details and your booking page."),
 ("Realtors", "digital-business-card-for-realtors.html",
  "Scan it at the open house, link straight to your listings."),
 ("Consultants &amp; coaches", "digital-business-card-for-consultants.html",
  "Lead with what you help people do, then let them book you."),
 ("Contractors &amp; trades", "digital-business-card-for-contractors.html",
  "A QR on the van and the quote. Change your number without reprinting."),
 ("Photographers", "digital-business-card-for-photographers.html",
  "Open the portfolio, not a description of it."),
 ("Coaches &amp; therapists", "digital-business-card-for-coaches.html",
  "Booking front and centre, personal number kept private."),
 ("Insurance agents", "digital-business-card-for-insurance-agents.html",
  "Licence details on every share, quotes one tap away."),
 ("Salons &amp; barbers", "digital-business-card-for-salons.html",
  "Rebook them while they're still in the chair."),
 ("Accountants", "digital-business-card-for-accountants.html",
  "A link that forwards cleanly when a client refers you."),
]

cards = "".join(
  f'<a class="card reveal" href="{u}" style="display:block;text-decoration:none">'
  f'<h3 style="margin-bottom:6px">{t}</h3>'
  f'<p style="color:var(--slate-600)">{d}</p></a>'
  for t, u, d in AUDIENCE)

SECTION = f'''{MARK}
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow"><span class="dot"></span> Built for how you work</span>
      <h2>Made for small businesses and the self-employed.</h2>
      <p class="sub" style="max-width:720px;margin:10px auto 0">Most digital business card tools are built for enterprises with a headcount. CompanyCard is built for the people who <i>are</i> the business — and for teams too small to be forced onto a five-seat plan.</p>
    </div>
    <div class="grid grid-3" style="margin-top:26px">{cards}</div>
    <p class="lp-related" style="margin-top:26px;text-align:center">
      Comparing options? See <a href="best-digital-business-card.html">the best digital business cards for small business</a>,
      or <a href="free-digital-business-card-comparison.html">what each free plan actually includes</a>.
    </p>
  </div>
</section>
{ENDMARK}
'''

# Insert before the testimonials section so the audience block sits high on the page.
anchor = "<!-- TESTIMONIALS -->"
if h.count(anchor) != 1:
    sys.exit(f"anchor {h.count(anchor)}x — aborting rather than guessing a position")
h = h.replace(anchor, SECTION + "\n" + anchor, 1)

open(F, "w", encoding="utf-8").write(h)

body = h[:h.find("<footer")]
linked = sum(1 for _, u, _ in AUDIENCE if u in body)
print(f"OK {len(orig)} -> {len(h)} bytes; audience pages linked from homepage body: {linked}/{len(AUDIENCE)}")
