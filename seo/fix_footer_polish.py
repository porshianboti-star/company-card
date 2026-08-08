#!/usr/bin/env python3
"""Footer polish pass — QA sweep findings 2026-08-08.

1. Privacy Policy was ORPHANED (zero inbound links, absent from sitemap)
   while every page runs GA4 — add a footer link on every page + sitemap entry.
2. footer-social on index/features/business/pricing had 3 dead href="#"
   icons (X/LinkedIn/Instagram placeholders) — REMOVED until real profiles
   exist (no fake affordances).
3. Two adjacent footer links both labeled "Email Signature Generator"
   (one external to prosignature.co, one internal) — external relabeled.
4. privacy-policy.html added to sitemap.xml with its true lastmod.

Idempotent. Anchor-insertion only (10 footer variants — never rebuild whole
footers). Run from repo root: python3 seo/fix_footer_polish.py
"""
import glob, re, sys

PRIV_LINK = ' &middot; <a href="privacy-policy.html">Privacy Policy</a>'
ANCHOR = 'www.company-card.com</span>'
EXT_OLD = '<a href="https://prosignature.co/" rel="noopener">Email Signature Generator</a>'
EXT_NEW = '<a href="https://prosignature.co/" rel="noopener">ProSignature — Email Signatures</a>'
SOCIAL_RE = re.compile(r'\s*<div class="footer-social">(?:(?!</div>).)*</div>', re.S)

stats = {'priv': 0, 'social': 0, 'relabel': 0, 'skipped': []}
for f in sorted(glob.glob('*.html')):
    src = open(f, encoding='utf-8').read()
    orig = src
    if f != 'privacy-policy.html' and 'privacy-policy.html' not in src:
        n = src.count(ANCHOR)
        if n == 0:
            stats['skipped'].append(f)
        else:
            # insert once, at the footer-bottom occurrence (last occurrence is the footer)
            i = src.rfind(ANCHOR)
            src = src[:i + len(ANCHOR)] + PRIV_LINK + src[i + len(ANCHOR):]
            stats['priv'] += 1
    if 'footer-social' in src:
        src, k = SOCIAL_RE.subn('', src)
        stats['social'] += k
    if EXT_OLD in src:
        src = src.replace(EXT_OLD, EXT_NEW)
        stats['relabel'] += 1
    if src != orig:
        assert src.count('<style') == orig.count('<style'), f
        open(f, 'w', encoding='utf-8').write(src)

# sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
if 'privacy-policy' not in sm:
    entry = ('  <url>\n    <loc>https://company-card.com/privacy-policy.html</loc>\n'
             '    <lastmod>2026-07-05</lastmod>\n  </url>\n')
    sm = sm.replace('</urlset>', entry + '</urlset>')
    open('sitemap.xml', 'w', encoding='utf-8').write(sm)
    print('sitemap: privacy-policy added')

print(stats)
