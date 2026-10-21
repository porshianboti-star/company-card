# -*- coding: utf-8 -*-
"""Remove unverified security and performance claims from business.html (2026-10-21).

business.html asserted "SOC 2 Type II & GDPR compliant", "encryption ... at rest",
"the certifications procurement asks for", a SOC 2 badge and three stat tiles
("3x more contacts captured", "100% brand-consistent", "5 min company-wide
rollout"). None of these is in seo/facts.py, pricing.html or the privacy
policy, and growth/off-site-listing-kit.md records that we hold no verified
facts about CompanyCard's security posture. Rule 1 of the GEO loop: never
invent facts.

Replaced with what is published elsewhere on the site:
- privacy-policy.html: encryption in transit (HTTPS), secured access-controlled
  storage, passwords stored only as secured hashes, delete cards or account at
  any time, access/correction/export/deletion rights.
- facts.py / pricing.html: SSO on Business; SCIM, SAML, audit logs and data
  residency on Enterprise; no seat minimum; brand and template lock.

Idempotent. Run from repo root: python3 seo/fix_business_unverified_claims_2026_10_21.py
"""
import os
import re

DATE = "2026-10-21"
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
FN = "business.html"
h = open(FN, encoding="utf-8").read()
TICK = ('<span class="tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>')

REPL = [
    # meta + og descriptions
    ("Central admin, SSO, CRM sync, analytics and enterprise security. CompanyCard for Teams.",
     "Central admin, brand lock, SSO, CRM sync and analytics, with no seat minimum. CompanyCard for Teams."),
    # stat tiles
    ('<div class="stat reveal"><div class="num gradient-text">3×</div><div class="lbl">More contacts captured</div></div>',
     '<div class="stat reveal"><div class="num gradient-text">0</div><div class="lbl">Seat minimum</div></div>'),
    ('<div class="stat reveal"><div class="num gradient-text">100%</div><div class="lbl">Brand-consistent cards</div></div>',
     '<div class="stat reveal"><div class="num gradient-text">1</div><div class="lbl">Locked brand template for everyone</div></div>'),
    ('<div class="stat reveal"><div class="num gradient-text">5&nbsp;min</div><div class="lbl">Company-wide rollout</div></div>',
     '<div class="stat reveal"><div class="num gradient-text">Live</div><div class="lbl">Edits reach every card already shared</div></div>'),
    ('<div class="stat reveal"><div class="num gradient-text">SOC&nbsp;2</div><div class="lbl">Enterprise security</div></div>',
     '<div class="stat reveal"><div class="num gradient-text">SSO</div><div class="lbl">On the Business plan</div></div>'),
    # security section
    ('<span class="eyebrow"><span class="dot"></span> Security &amp; compliance</span>',
     '<span class="eyebrow"><span class="dot"></span> Security &amp; your data</span>'),
    ("<h2>Enterprise-grade by default.</h2>",
     "<h2>What we protect, and how.</h2>"),
    ("<p class=\"lead\">Your people's data is protected with the controls your security team expects — and the certifications procurement asks for.</p>",
     "<p class=\"lead\">Everything below is stated in our <a href=\"privacy-policy.html\">privacy policy</a> "
     "or on the <a href=\"pricing.html\">pricing page</a>. We do not list certifications we have not published.</p>"),
    (TICK + " SOC 2 Type II &amp; GDPR compliant</li>",
     TICK + " Encryption in transit (HTTPS) and secured, access-controlled storage; passwords kept only as secured hashes</li>"),
    (TICK + " Encryption in transit &amp; at rest</li>",
     TICK + " SSO on Business; SAML, SCIM provisioning, audit logs and data residency on Enterprise</li>"),
    (TICK + " Audit logs &amp; data residency options</li>",
     TICK + " Delete a card or the whole account at any time, and request access, correction or export of your data</li>"),
    ('<span class="save-tag" style="padding:10px;">SOC 2</span>',
     '<span class="save-tag" style="padding:10px;">HTTPS</span>'),
    ('<span class="save-tag" style="padding:10px;">GDPR</span>',
     '<span class="save-tag" style="padding:10px;">Audit logs</span>'),
]
n = 0
for old, new in REPL:
    c = h.count(old)
    if c == 0:
        assert new in h, ("missing anchor", old[:80])
        continue
    h = h.replace(old, new)
    n += c
assert not re.search(r"SOC\s*(&nbsp;)?\s*2|at rest|3×|certifications procurement", h), "residual claim"

# freshness: keep datePublished, bump dateModified
h = re.sub(r'("url":"https://company-card.com/business.html","datePublished":"[^"]+","dateModified":")[^"]+(")',
           r"\g<1>" + DATE + r"\2", h, count=1)
open(FN, "w", encoding="utf-8").write(h)

sm = open("sitemap.xml", encoding="utf-8").read()
sm = re.sub(r"(<loc>https://company-card.com/business.html</loc><lastmod>)[^<]+", r"\g<1>" + DATE, sm, count=1)
open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("replaced %d occurrences in %s; dateModified + sitemap lastmod = %s" % (n, FN, DATE))
