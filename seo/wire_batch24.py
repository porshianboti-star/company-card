# -*- coding: utf-8 -*-
"""Batch 24 wiring — digital-business-card-for-bookkeepers.html.

FOOTER. The profession links live only in the long "Solutions" footer variant
(20 files incl. index.html and pricing.html); seo/_tpl_footer.txt and the
footers on generated landing pages carry no profession links at all, which is
how every earlier profession page was wired too. Anchor-insert after the
"For Accountants" <li>; never a whole-footer replace.

CROSS-LINK. The accountants page gets a "For bookkeepers" link in its
Related row (insert-only). Its generator (pages_data3.py REL_CORE) is shared by
many pages and the live accountants page has been hand-extended since, so the
generator is not touched; a rebuild of pages_data3 would drop this link.

SITEMAP after the accountants entry; LLMS.TXT after the accountants line.

FRESHNESS. NOT seo/add_freshness.py (hardcoded 2026-08-02, rolls dates back).
The new page gets a FRESH block (published = modified = today); the
accountants page's dateModified moves because its content changed.

Idempotent. Run from repo root: python3 seo/wire_batch24.py
"""
import os
import re
import json

DATE = "2026-09-25"
BASE = "https://company-card.com/"
SLUG = "digital-business-card-for-bookkeepers.html"
ACC = "digital-business-card-for-accountants.html"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. footer ----------
ANCHOR = '<li><a href="%s">For Accountants</a></li>' % ACC
NEW_LI = '<li><a href="%s">For Bookkeepers</a></li>' % SLUG
touched = 0
for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
    h = open(fn, encoding="utf-8").read()
    if NEW_LI in h or ANCHOR not in h:
        continue
    assert h.count(ANCHOR) == 1, (fn, h.count(ANCHOR))
    open(fn, "w", encoding="utf-8").write(h.replace(ANCHOR, ANCHOR + NEW_LI, 1))
    touched += 1
print("footer link added to %d files" % touched)

# ---------- 2. accountants Related row ----------
h = open(ACC, encoding="utf-8").read()
REL_OLD = 'Related: <a href="digital-business-card-for-small-business.html">For small business</a>'
REL_NEW = ('Related: <a href="%s">For bookkeepers</a> &middot; '
           '<a href="digital-business-card-for-small-business.html">For small business</a>' % SLUG)
if REL_NEW not in h:
    assert h.count(REL_OLD) == 1, h.count(REL_OLD)
    open(ACC, "w", encoding="utf-8").write(h.replace(REL_OLD, REL_NEW, 1))
    print("accountants: related link added")

# ---------- 3. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    r = re.compile(r'(<url><loc>' + re.escape(BASE + ACC) + r'</loc><lastmod>)([^<]*)(</lastmod>'
                   r'<changefreq>[^<]*</changefreq><priority>[^<]*</priority></url>)')
    m = r.search(sm)
    assert m and len(r.findall(sm)) == 1
    new_acc = m.group(1) + DATE + m.group(3)
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    sm = sm[:m.start()] + new_acc + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")

# ---------- 4. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()
ACC_LINE = "- Digital business card for accountants & bookkeepers: " + BASE + ACC
LINE = ("- Digital business card for bookkeepers (monthly bookkeeping, catch-up work, "
        "remote clients referred by accountants): " + BASE + SLUG)
if LINE not in ll:
    assert ll.count(ACC_LINE) == 1
    ll = ll.replace(ACC_LINE, ACC_LINE + "\n" + LINE, 1)
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt entry added")

# ---------- 5. freshness ----------
MARK, ENDMARK = "<!-- FRESH:BEGIN -->", "<!-- FRESH:END -->"
DISAMBIG = ("A digital business card app for sharing your contact details by QR code, link or "
            "wallet pass. Not a corporate credit card, company expense card or spend-management "
            "service.")
PUBLISHER = {"@type": "Organization", "name": "CompanyCard",
             "disambiguatingDescription": DISAMBIG, "url": BASE}


def stamp(slug, published, modified):
    h = open(slug, encoding="utf-8").read()
    if MARK in h:
        old = re.search(re.escape(MARK) + r".*?" + re.escape(ENDMARK), h, re.S).group(0)
        prev = re.search(r'"datePublished":"([^"]+)"', old)
        published = prev.group(1) if prev else published
        h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK) + r"\n?", "", h, count=1, flags=re.S)
    title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", h, re.S).group(1)).strip()
    node = {"@context": "https://schema.org", "@type": "WebPage", "name": title,
            "url": BASE + slug, "datePublished": published, "dateModified": modified,
            "isPartOf": {"@type": "WebSite", "name": "CompanyCard", "url": BASE},
            "publisher": PUBLISHER, "inLanguage": "en"}
    blk = (MARK + '\n<script type="application/ld+json">'
           + json.dumps(node, ensure_ascii=False, separators=(",", ":"))
           + "</script>\n" + ENDMARK + "\n")
    i = h.find("</head>")
    assert i != -1, slug
    open(slug, "w", encoding="utf-8").write(h[:i] + blk + h[i:])
    print("stamped %s: published=%s modified=%s" % (slug, published, modified))


stamp(SLUG, DATE, DATE)
stamp(ACC, DATE, DATE)
print("done")
