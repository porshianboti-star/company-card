#!/usr/bin/env python3
"""2026-09-15: digital-business-card-maker.html gets the mini-builder.

GSC 28d (read 2026-09-15): the page is the third-largest on the property
(579 impressions) at position 78.0 — the worst of any top-10 page — and its
title promised a maker it did not contain (0 inputs). Same defect the
2026-09-13 commit fixed on qr-code-business-card and virtual-business-card;
same shared assets/mini-builder.js, same #make section under the hero.
Every replacement asserts its exact count so a rerun cannot double-insert.
"""
import re, sys, pathlib

P = pathlib.Path(__file__).resolve().parent.parent
page = P / 'digital-business-card-maker.html'
src = (P / 'qr-code-business-card.html').read_text()
html = page.read_text()

if 'mini-builder.js' in html:
    print('already mounted'); sys.exit(0)

def rep(s, old, new, n=1):
    c = s.count(old)
    assert c == n, (old[:60], c)
    return s.replace(old, new)

# 1. the shared style block, lifted verbatim from the sibling page
m = re.search(r'<style>\n/\* mini-builder \(round 69\) \*/.*?</style>\n', src, re.S)
assert m
html = rep(html, '<!-- FRESH:END -->\n</head>', '<!-- FRESH:END -->\n' + m.group(0) + '</head>')

# 2. hero: CTA scrolls to the maker; lead says it is on this page
html = rep(html,
    '<p class="lead">Design your card in a live editor — templates, colours, photo, layout — and publish it as a link and QR code instead of a print order.</p>',
    '<p class="lead">Type your details below and watch the card and its QR code build as you go. Download it, or publish it as a live link and QR code instead of a print order.</p>')
html = rep(html,
    '''      <a href="app/builder.html" class="btn btn-primary btn-lg shine">Open the free maker</a>
      <a href="features.html" class="btn btn-ghost btn-lg">See all features</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>A maker built for sharing, not printing</h2>''',
    '''      <a href="#make" class="btn btn-primary btn-lg shine">Make my card free</a>
      <a href="features.html" class="btn btn-ghost btn-lg">See all features</a>
    </div>
  </div>
</section>
<section class="section" id="make">
  <div class="container">
    <h2 style="text-align:center;margin-bottom:8px">Make your digital business card now — free, no signup</h2>
    <p class="lead" style="text-align:center;max-width:640px;margin:0 auto 26px">Six fields, a live preview and a scannable QR code. Download the QR or the .vcf, or save it as a real CompanyCard with a permanent link, templates and brand colours.</p>
    <div id="cc-mini"></div>
  </div>
</section>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script src="assets/mini-builder.js" defer></script>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>A maker built for sharing, not printing</h2>''')

# 3. meta description: the on-page maker has no templates; the full builder does
old_desc = 'A business card maker for the digital age: design your card online with live preview, templates and brand colours. Free to use — QR code and link included.'
new_desc = 'Make a digital business card online, free: type your details, watch the live preview and QR code update, download it or save it as a real card with a permanent link. No signup to try.'
html = rep(html, old_desc, new_desc, 2)  # meta description + og:description

# 4. honest dateModified (add_freshness.py would roll it back to 08-02)
html = rep(html, '"dateModified":"2026-08-02"', '"dateModified":"2026-09-15"')
page.write_text(html)

sm = P / 'sitemap.xml'
s = sm.read_text()
s = rep(s, '<loc>https://company-card.com/digital-business-card-maker.html</loc><lastmod>2026-08-02</lastmod>',
           '<loc>https://company-card.com/digital-business-card-maker.html</loc><lastmod>2026-09-15</lastmod>')
sm.write_text(s)
print('ok')
