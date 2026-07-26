#!/usr/bin/env python3
"""Add machine-readable pricing (SoftwareApplication + Offer array) to pricing.html.

WHY: AI assistants answering "how much does X cost" quote prices, and a page
with only FAQPage/BreadcrumbList gives them nothing structured to quote. Every
figure below matches the visible pricing table verbatim — schema must reflect
visible content, and inconsistent numbers are exactly what stops a model
repeating yours.

audience = BusinessAudience naming the ICP, so the entity itself carries "small
business / self-employed" rather than relying on prose alone.
Idempotent: re-running replaces the block between the markers.

Run from repo root: python3 add_offer_schema.py
"""
import re, json, sys

F = "pricing.html"
MARK = "<!-- OFFERS:BEGIN -->"
ENDMARK = "<!-- OFFERS:END -->"

h = open(F, encoding="utf-8").read()
orig = h

# Remove a previous block if present (marker-bounded — never bound at </head>,
# which would swallow whatever sits between).
if MARK in h and ENDMARK in h:
    h = re.sub(re.escape(MARK) + r".*?" + re.escape(ENDMARK), "", h, count=1, flags=re.S)

BASE = "https://company-card.com/"

def offer(name, price, desc, unit=None):
    o = {
        "@type": "Offer",
        "name": name,
        "price": price,
        "priceCurrency": "USD",
        "description": desc,
        "url": BASE + "pricing.html",
        "availability": "https://schema.org/InStock",
    }
    if price != "0":
        o["priceSpecification"] = {
            "@type": "UnitPriceSpecification",
            "price": price,
            "priceCurrency": "USD",
            "billingIncrement": 1,
            "unitText": unit or "month",
        }
    return o

app = {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "CompanyCard",
  "applicationCategory": "BusinessApplication",
  "applicationSubCategory": "Digital business card",
  "operatingSystem": "Web, iOS, Android (browser-based — no app required for the recipient)",
  "url": BASE,
  "description": ("CompanyCard is a digital business card for small business owners, self-employed "
                  "professionals and teams — share your details by QR code, link, Apple or Google "
                  "Wallet with no app for the person receiving it. A free plan is available."),
  "audience": {
    "@type": "BusinessAudience",
    "name": "Small business owners, self-employed professionals, freelancers and small teams",
  },
  "featureList": [
    "QR code business card",
    "Permanent sharing link that never changes",
    "Apple Wallet and Google Wallet pass",
    "No app required for the person receiving the card",
    "Email signature",
    "Virtual background for video calls",
    "Team cards with locked branding and central admin",
    "No seat minimum on team plans",
  ],
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "USD",
    "lowPrice": "0",
    "highPrice": "12",
    "offerCount": 4,
    "offers": [
      offer("Free", "0",
            "One digital business card, QR code and sharing link, profile, links and socials, "
            "Apple and Google Wallet pass, unlimited edits. Free forever, no credit card. Free "
            "cards carry a small CompanyCard credit."),
      offer("Pro", "8",
            "Everything in Free, plus unlimited links and files, custom branding and themes, "
            "lead capture and analytics, and removal of the CompanyCard credit."),
      offer("Business", "12",
            "Everything in Pro, plus central admin dashboard, brand and template lock, CRM sync "
            "and team analytics, and SSO. Priced per user per month with no seat minimum.",
            unit="user per month"),
      {"@type": "Offer", "name": "Enterprise", "priceCurrency": "USD",
       "description": "Custom pricing. Everything in Business, plus SCIM provisioning and SAML, "
                      "audit logs and data residency, a dedicated success manager, SLA and invoicing.",
       "url": BASE + "pricing.html", "availability": "https://schema.org/InStock"},
    ],
  },
}

block = (MARK + "\n<script type=\"application/ld+json\">"
         + json.dumps(app, ensure_ascii=False, separators=(",", ":"))
         + "</script>\n" + ENDMARK + "\n")

idx = h.find("</head>")
if idx == -1:
    sys.exit("no </head>")
h = h[:idx] + block + h[idx:]
open(F, "w", encoding="utf-8").write(h)

# validate
types = [json.loads(b)["@type"] for b in
         re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)]
print(f"OK {len(orig)} -> {len(h)} bytes; schema now: {types}")
