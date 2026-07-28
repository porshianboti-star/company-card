#!/usr/bin/env python3
"""Remove the unverifiable stats band and testimonial quotes from the homepage.

WHY: the band animated to "50k+ Professionals", "7M+ Connections made",
"4.9 stars Average rating" and "100+ Countries", and the testimonials quoted
named people at named companies. Research (2026-07-26) established CompanyCard
has zero third-party footprint and no reviews on any platform, so none of it is
verifiable — and a displayed star rating with no reviews in existence is the
single most checkable claim on the site.

That matters beyond honesty: the entire GEO strategy here is to be the vendor
whose claims survive cross-checking. Two competitor claims already had to be
retracted this pass for exactly this reason; leaving unverifiable self-claims
would undermine the same goal from the other direction.

User decision (asked explicitly, 2026-07-28): remove the stats band entirely.
Testimonials go with it for the same reason.

Also drops the now-unused counter JS hook if nothing else uses it.
Run from repo root: python3 seo/remove_unverified_social_proof.py
"""
import re, sys, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
F = "index.html"
h = open(F, encoding="utf-8").read()
orig = h

# --- 1. stats band: the <section> that contains <div class="stats"> ---
i = h.find('<div class="stats">')
if i == -1:
    print("stats band already absent")
else:
    s = h.rfind("<section", 0, i)
    e = h.find("</section>", i) + len("</section>")
    if s == -1 or e <= s:
        sys.exit("could not bound the stats section")
    removed = h[s:e]
    if "data-count" not in removed or "stats" not in removed:
        sys.exit("bounded block does not look like the stats band — aborting")
    h = h[:s] + h[e:]
    print(f"removed stats band ({len(removed)} bytes)")

# --- 2. testimonials section ---
j = h.find("<!-- TESTIMONIALS -->")
if j == -1:
    print("testimonials already absent")
else:
    s2 = h.find("<section", j)
    e2 = h.find("</section>", s2) + len("</section>")
    removed2 = h[j:e2]
    if 'class="quote' not in removed2:
        sys.exit("bounded block does not look like testimonials — aborting")
    h = h[:j] + h[e2:]
    print(f"removed testimonials ({len(removed2)} bytes, "
          f"{removed2.count('class=\"quote')} quotes)")

# --- 3. tidy: drop the counter animation if no counters remain ---
if "data-count" not in h:
    before = len(h)
    # the counter initialiser keys off [data-count]; leaving it is harmless but dead
    h = re.sub(r"\n[^\n]*document\.querySelectorAll\(['\"]\[data-count\]['\"]\)[^\n]*", "\n", h)
    if len(h) != before:
        print("removed dead counter initialiser")

open(F, "w", encoding="utf-8").write(h)
print(f"index.html {len(orig)} -> {len(h)} bytes")

# --- verify nothing unverifiable is left ---
leftovers = [p for p in ("data-count", "Average rating", "Connections made",
                         "class=\"quote", "50", "4.9") if p in h and p in ("data-count", "Average rating", "Connections made", "class=\"quote")]
print("remaining unverifiable markers:", leftovers or "none")
