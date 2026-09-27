# -*- coding: utf-8 -*-
"""Batch 23 wiring — sitewide footer (+ template), sitemap, llms.txt, _redirects,
freshness stamp, for embed-digital-business-card-on-your-website.html.

Same shape as wire_batch20.py. FOOTER: anchor-insert after "How to Make One"
(the other how-to in Compare & Tools) where that <li> exists (15 pages), else
after "Digital vs Paper Cards" (the rest + template), else after "How Much It
Costs". brand-kit.html and the Google verification stub have no anchor and are
left alone. SITEMAP: right after how-to-make-a-digital-business-card.html,
lastmod set BY HAND to 2026-09-27 (seo/add_freshness.py is NOT run — its DATE
is 2026-08-02 and rolls dates backward). LLMS.TXT: one line under "## Guides"
after the how-to-make line. _REDIRECTS: one `/slug  /slug.html  301!` line in
alphabetical position. FRESHNESS: the new page only.

Idempotent. Run from repo root: python3 seo/wire_batch21.py
"""
import os, re, json

DATE = "2026-09-27"
BASE = "https://company-card.com/"
SLUG = "embed-digital-business-card-on-your-website.html"
BARE = "/" + SLUG[:-5]

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------- 1. sitewide footer link (+ the template) ----------
ANCHORS = [
    '<li><a href="how-to-make-a-digital-business-card.html">How to Make One</a></li>',
    '<li><a href="digital-business-card-vs-paper.html">Digital vs Paper Cards</a></li>',
    '<li><a href="digital-business-card-cost.html">How Much It Costs</a></li>',
]
NEW_LI = '<li><a href="%s">Add to Your Website</a></li>' % SLUG

targets = sorted(f for f in os.listdir(".") if f.endswith(".html")) + ["seo/_tpl_footer.txt"]
touched = skipped = present = 0
for fn in targets:
    h = open(fn, encoding="utf-8").read()
    if NEW_LI in h:
        present += 1
        continue
    for anchor in ANCHORS:
        if anchor in h:
            assert h.count(anchor) == 1, (fn, anchor, h.count(anchor))
            h = h.replace(anchor, anchor + NEW_LI, 1)
            open(fn, "w", encoding="utf-8").write(h)
            touched += 1
            break
    else:
        skipped += 1
        print("  no footer anchor, left alone: " + fn)
print("footer link added to %d files (%d already had it, %d have no anchor)" % (touched, present, skipped))

# ---------- 2. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
if BASE + SLUG not in sm:
    after_re = re.compile(
        r'<url><loc>' + re.escape(BASE + "how-to-make-a-digital-business-card.html")
        + r'</loc><lastmod>[^<]*</lastmod><changefreq>[^<]*</changefreq>'
        r'<priority>[^<]*</priority></url>')
    m = after_re.search(sm)
    assert m and len(after_re.findall(sm)) == 1, "how-to-make sitemap entry not uniquely found"
    entry = ("\n<url><loc>" + BASE + SLUG + "</loc><lastmod>" + DATE +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    sm = sm[:m.end()] + entry + sm[m.end():]
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap entry added")
else:
    print("sitemap entry already present")

# ---------- 3. llms.txt ----------
ll = open("llms.txt", encoding="utf-8").read()
LINE = ("- How to add a digital business card to your website — two copy-paste snippets from the "
        "app's Share → \"Add to your website\" panel: a Save-my-contact button (one SVG image linking "
        "to the card) or the card page in a lazy-loaded 360×600 iframe with a \"Made with "
        "CompanyCard\" credit line under it. Works in any HTML/embed block (Wix, Squarespace, "
        "WordPress, Webflow, Shopify, hand-coded sites, Linktree-style bios, email signatures); free "
        "plan included. The card's details travel inside the share link, so an edited card needs the "
        "snippet copied again: " + BASE + SLUG)
if LINE not in ll:
    anchor_start = "- How to make a digital business card: "
    i = ll.find(anchor_start)
    assert i != -1 and ll.count(anchor_start) == 1, "llms.txt how-to-make anchor not uniquely found"
    j = ll.find("\n", i)
    assert j != -1
    ll = ll[:j + 1] + LINE + "\n" + ll[j + 1:]
    open("llms.txt", "w", encoding="utf-8").write(ll)
    print("llms.txt: page listed under Guides")
else:
    print("llms.txt entry already present")

# ---------- 4. _redirects ----------
rd = open("_redirects", encoding="utf-8").read()
RULE = "%s  /%s  301!" % (BARE, SLUG)
if RULE not in rd:
    lines = rd.split("\n")
    idx = [k for k, l in enumerate(lines) if re.match(r"^/[a-z0-9-]+  /[a-z0-9-]+\.html  301!$", l)]
    assert idx, "no slug redirect rules found"
    pos = None
    for k in idx:
        if lines[k].split()[0] > BARE:
            pos = k
            break
    if pos is None:
        pos = idx[-1] + 1
    lines.insert(pos, RULE)
    open("_redirects", "w", encoding="utf-8").write("\n".join(lines))
    print("_redirects: rule added before line %d" % (pos + 1))
else:
    print("_redirects rule already present")

# ---------- 5. freshness stamp, new page only ----------
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
        h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)
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
print("done")
