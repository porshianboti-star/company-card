# CompanyCard GEO/SEO log

Measured state, appended each time work ships. Numbers only — no claims.

## 2026-07-30 (later)

**Shipped batch 11** (drafting + adversarial-verification workflow; 2 checkers
per draft caught soft implied statistics pre-render): dentists, chiropractors,
event-planners. Sitemap 47 -> 50, all live 200. Event-planners page targets the
profession; cross-links the events-attendance page to avoid cannibalisation.

**Measured (GSC, read directly this session):**
- Indexed 16 / not-indexed 6 (all benign "alternate page with proper canonical");
  "Crawled - currently not indexed" = 0 — still no quality penalty.
- Performance 28d: 636 impressions, 4 clicks, CTR 0.6%, avg position 55.3,
  115 query rows. Impressions exist on target queries: "free digital business
  card" 23, "qr code business card" 27, "digital business cards free" 12,
  "hihello vs blinq" 9, "what is a virtual business card" 15.
- Sitemap RESUBMITTED in GSC: re-read same day, discovered pages 24 -> 47
  (before batch 11; will pick up 50 next read).
- Manual indexing REQUESTED for best-digital-business-card.html (was "URL
  unknown to Google" — the money page had never been crawled) and
  free-digital-business-card-comparison.html (same state).

**Measured (SERP + mention sweep, 6 queries + 8 mention searches, workflow):**
- CompanyCard ABSENT from all 6 target SERPs, including the brand query
  "CompanyCard digital business card" (zero brand-entity recognition).
- Third-party mentions of company-card.com anywhere: 0 (Reddit, G2, Trustpilot,
  Product Hunt, listicles, directories — nothing).
- Who wins these SERPs: vendor-owned listicles (Uniqode, Mobilo, Wave, V1CE,
  Blinq, HiHello, Krofile, DBC) + aggregators (G2 holds 2 slots on
  "wave connect alternative"; Slashdot, CB Insights). Only quasi-independent
  media: Small Business Trends.
- Conclusion unchanged and now better-evidenced: on-site coverage is compounding
  (impressions exist, position ~55) but entry into AI answers and top-10 SERPs
  runs through third-party surfaces (G2 etc.) that DO NOT EXIST for us yet.

## 2026-07-30

- Sitemap URLs: 43 -> 47 (xmllint clean). Pages: +4.
- Shipped batch 10: four self-employed-trade profession pages —
  `/digital-business-card-for-notaries`, `/-tutors`, `/-cleaners`,
  `/-landscapers`. Each written with trade-specific substance (how they get
  hired, the one load-bearing field), not noun-swaps: notary = commission
  no./expiry/E&O/RON; tutor = subjects + safeguarding check + forwards through
  parent group chats; cleaner = insurance + service split + QR on flyer/van;
  landscaper = photo portfolio + QR on truck/yard sign + seasonal edits.
- Product claims held to /pricing: free = 1 card + QR/link + wallet + unlimited
  edits, carries small CompanyCard credit; Pro $8; Business $12/user, no seat
  min. Did NOT claim lead-capture-on-free (that's gated behind Pro; Wave beats
  us there). No invented licensing/insurance/regulatory rules — pages say
  "check your own regulator / commissioning authority".
- Wired: index.html footer Solutions column (homepage body links), llms.txt
  "Pages by profession", sitemap.xml. add_freshness DATE bumped 07-26 -> 07-30
  (restamps dateModified sitewide + sitemap lastmod; footer changed on all
  pages this run, so the restamp is honest). sync_faq_schema: 0 mismatches.
- Validation: each new page = exactly one h1, unique title/meta/canonical, 3
  valid JSON-LD blocks (FAQPage + BreadcrumbList + WebPage).
- OFF-SITE STILL BLOCKED: Organization.sameAs = [] — no G2/Capterra/Product
  Hunt/AlternativeTo/Trustpilot/social profiles exist yet. Only the user can
  create them; remains the single biggest GEO blocker.

## 2026-07-28 (later)

- Pages 43 -> 45, sitemap 40 -> 42
- Added wave-connect-alternative and v1ce-alternative, completing the
  competitor set (Blinq, HiHello, Popl, Linq, Uniqode, Mobilo, Wave, V1CE)
- NOTE the Wave page concludes AGAINST us on most published columns: Wave's
  free tier includes lead capture + email signature, Pro is $7 vs our $8 and
  Teams $5/user vs our $12. Our only published edge is the seat floor (Wave
  Teams requires 3 seats, we require none). Published anyway — it captures the
  query and conceding accurately is the behaviour that earns citation.
- V1CE verified: no free plan, single tier GBP49.99/mo bundling NFC card + CRM

## 2026-07-28

**Site**
- Pages: 20 → 43
- Sitemap URLs: 17 → 40
- ICP phrase coverage ("small business" / "self-employed"): 0 pages → sitewide
- FAQPage schema byte-matching visible text: all pages (verified)
- Entity: Organization + WebSite + SoftwareApplication + WebPage on every page;
  AggregateOffer on /pricing

**Google Search Console**
- Indexed: 11 → 16
- Not indexed: 6, ALL "Alternate page with proper canonical tag"
  (duplicate `/foo` vs `/foo.html` forms — Google consolidating correctly)
- **"Crawled – currently not indexed": 0 affected pages** (drilldown verified)
  → no quality or authority penalty on the site
- Sitemap last read 2026-07-26, resubmitted after each batch

**Off-site — the binding constraint**
- G2: not created
- Capterra / Product Hunt / AlternativeTo / Trustpilot: not created
- Social profiles: none
- `Organization.sameAs`: `[]` (empty — nothing to populate it with)

**Integrity actions this pass**
- Removed false claim that Blinq lacks email signature + virtual background
  (Blinq ships both free — verified blinq.me/pricing)
- Rewrote /popl-alternative: Popl has repositioned to an AI event-lead-capture
  platform with demo-gated pricing; the "NFC hardware company" thesis was stale
- Removed unverifiable homepage social proof (50k+ / 7M+ / 4.9★ / 100+ and three
  named testimonials) at the user's explicit direction — no reviews exist on any
  platform to support a star rating

**Next measurable checkpoints**
- 3–10 days: new pages move from "unknown to Google" to indexed
- 2–4 weeks: first impressions on long-tail ICP queries
- Blocked until a G2 profile exists: `sameAs`, AggregateRating, third-party corroboration
