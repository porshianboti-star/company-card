#!/usr/bin/env python3
"""2026-09-19: hihello-vs-popl.html was rewritten (see pages_data20.py docstring)
after GSC listed it "Crawled - currently not indexed". build_pages20.py
re-renders the page WITHOUT the freshness block, so this script puts it back
with datePublished preserved (2026-09-13) and dateModified = today, and moves
the page's sitemap lastmod. Do NOT run add_freshness.py — it rolls every date
on the site back to its hardcoded 2026-08-02. Idempotent. Run from repo root.
"""
import json, re

BASE = "https://company-card.com/"
SLUG = "hihello-vs-popl.html"
PUBLISHED = "2026-09-13"
DATE = "2026-09-19"
MARK, ENDMARK = "<!-- FRESH:BEGIN -->", "<!-- FRESH:END -->"
DISAMBIG = ("A digital business card app for sharing your contact details by QR code, link or "
            "wallet pass. Not a corporate credit card, company expense card or spend-management "
            "service.")

h = open(SLUG, encoding="utf-8").read()
if MARK in h:
    old = re.search(re.escape(MARK) + r".*?" + re.escape(ENDMARK), h, re.S).group(0)
    PUBLISHED = re.search(r'"datePublished":"([^"]+)"', old).group(1)
    h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK) + r"\n?", "", h, count=1, flags=re.S)
title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", h, re.S).group(1)).strip()
node = {"@context": "https://schema.org", "@type": "WebPage", "name": title,
        "url": BASE + SLUG, "datePublished": PUBLISHED, "dateModified": DATE,
        "isPartOf": {"@type": "WebSite", "name": "CompanyCard", "url": BASE},
        "publisher": {"@type": "Organization", "name": "CompanyCard",
                      "disambiguatingDescription": DISAMBIG, "url": BASE},
        "inLanguage": "en"}
blk = (MARK + '\n<script type="application/ld+json">'
       + json.dumps(node, ensure_ascii=False, separators=(",", ":"))
       + "</script>\n" + ENDMARK + "\n")
i = h.find("</head>")
assert i != -1
h = h[:i] + blk + h[i:]
open(SLUG, "w", encoding="utf-8").write(h)
print("stamped %s: published=%s modified=%s" % (SLUG, PUBLISHED, DATE))

sm = open("sitemap.xml", encoding="utf-8").read()
lm = re.compile(r'(<loc>' + re.escape(BASE + SLUG) + r'</loc>\s*<lastmod>)([^<]*)(</lastmod>)')
assert len(lm.findall(sm)) == 1, "sitemap entry not uniquely found"
sm2, n = lm.subn(lambda m: m.group(1) + DATE + m.group(3), sm)
open("sitemap.xml", "w", encoding="utf-8").write(sm2)
print("sitemap lastmod -> %s (%d entry)" % (DATE, n))
