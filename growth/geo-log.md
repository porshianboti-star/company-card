# CompanyCard GEO/SEO log

Measured state, appended each time work ships. Numbers only — no claims.

## 2026-08-02

> ### ⛔ NOTHING IN THIS ENTRY IS LIVE YET — NETLIFY DEPLOYS ARE BLOCKED
>
> **The site has not deployed since 2026-08-01 07:05 (commit `f5d9ab8`).** Every
> deploy since then fails before building with the Netlify error:
> **`Skipped due to account credit usage exceeded`**
>
> Confirmed by API against site `steady-cendol-c884c0`
> (`00bb5c43-f376-4091-9712-d007e2be7dfe`), three consecutive failures:
> `d1a0224` (14:19), `d2f273c8` (20:13), and a manual rebuild I triggered at
> 20:20 to check whether it was transient — it is not.
> `build_settings.stop_builds` is `false`, so builds are not paused manually;
> `published_deploy` is still `f5d9ab8`. Account is the Personal tier,
> billing email porshianboti@gmail.com.
>
> **Only the user can clear this** — it needs a billing/credit action on the
> Netlify account. I did not and will not attempt any payment or plan change.
> Everything below is committed and pushed to `main` and will go live on the
> first successful build with no further work.
>
> **Consequence for measurement:** the GSC and sitemap numbers recorded below
> describe the site as it stands at `f5d9ab8` (50 sitemap URLs live). The 51-URL
> sitemap, the `sameAs` values and `/vcard-qr-code` are in the repo only.

**THE OFF-SITE WALL CAME DOWN.** The G2 profile approved on 2026-08-02 is live
and publicly reachable, confirmed by loading both URLs this session:
- Product: https://www.g2.com/products/companycard/reviews — listed in G2's
  **Digital Business Card** category, 0 reviews, no rating.
- Seller: https://www.g2.com/sellers/companycard — 1 profile, 1 category.
It is **not yet indexed by Google**: a web search for "CompanyCard" restricted
to g2.com returns the category page and rival products but no CompanyCard
result. Expected for a profile hours old; worth re-checking next run.

**Wired it in — `Organization.sameAs` is no longer `[]`:**
- `index.html`: `Organization.sameAs` = [seller, product]; also added
  `sameAs` = [product] to the `SoftwareApplication` node.
- `llms.txt`: new "## Third-party profiles (for verification)" section. It
  states plainly that the profile has **no reviews and no rating**, and asks
  summarisers not to attribute one. Also records that Capterra / Product Hunt /
  AlternativeTo / Trustpilot still do not exist.
- `about.html`: a paragraph in "What we won't claim" naming the G2 listing, its
  go-live date and the fact that it carries no rating yet.

**Built (not yet live): `vcard-qr-code.html`** (the last unshipped item on the standing
backlog). Deliberately the *payload/encoding-mechanics* page, not a second
feature comparison — `qr-code-business-card.html` already owns the
"vCard QR vs. dynamic QR" feature table and its FAQ, and
`electronic-business-card.html` owns the definitional angle. This page covers
what is literally encoded in the `.vcf`, which properties the spec requires,
and why more fields raise the QR version and therefore the printed size needed
to scan. 4 JSON-LD blocks (FAQPage + BreadcrumbList + HowTo + WebPage), 6 FAQs
byte-matched, 1 h1, 55-char title, 144-char meta.

**Fact provenance for that page** — every technical claim fetched from a primary
source on 2026-08-02, listed in the header of `seo/pages_data12.py`: RFC 6350
(vCard 4.0; obsoletes 2425/2426/4770; VERSION+FN mandatory, VERSION immediately
after BEGIN:VCARD), RFC 2426 (vCard 3.0), Denso Wave (v1 = 21x21 modules,
v40 = 177x177, +4 modules per side per version; EC levels L/M/Q/H, M ~15%,
Q ~25%, raising EC adds Reed-Solomon data). **Deliberately NOT stated** because
they could not be verified: any minimum print size in mm, the version-40 byte
capacity (Denso Wave's capacity table would not load), the L and H percentages,
and what any specific phone does with a scanned vCard.

**Competitor re-verification (rule 2):**
- **Blinq re-fetched live 2026-08-02 — all four stamped claims still true.**
  Free = 2 cards + virtual backgrounds + email signature + Apple/Google Wallet;
  Premium $9.99/mo monthly ($7.33 annual); Business $6.99/card/mo monthly
  ($4.99 annual); FAQ still states a minimum payment equal to 5 Team Cards.
- HiHello / Mobilo / Uniqode / Wave Connect / V1CE were **NOT** re-verified this
  run — the verification workflow hit the session agent limit and 11 of 13
  agents died. Their "verified July 2026" stamps were therefore **left
  unchanged**, which is correct: bumping the stamp to August would assert a
  re-check that did not happen. **Next run must start with these five.**

**Measured (GSC, read directly this session):**
- Sitemap: **50 URLs live** (fetched from company-card.com, `xmllint` clean).
  The repo is at **51** — the extra URL is `/vcard-qr-code.html`, which cannot
  appear live until the deploy block above is cleared.
- Indexed **16**, not-indexed **6** — all still "Alternate page with proper
  canonical tag"; "Crawled - currently not indexed" = **0**. No quality penalty.
- Indexed count is **flat at 16 since 07-28** while the sitemap has grown to 51.
  The gap is crawl latency, not exclusion — nothing new is being *rejected*.
- Performance 28d: **809 impressions, 4 clicks, CTR 0.5%, avg position 57.2,
  139 query rows** (07-30: 636 / 4 / 0.6% / 55.3 / 115).
  Impressions +27%, query rows +24, clicks flat, average position drifted 1.9
  worse — consistent with more long-tail queries surfacing at depth.
- Top queries by impressions: "company card" **155** (brand term, now the
  largest single row), "qr code business card" 44 (was 27), "free digital
  business card" 38 (was 23), "e name card" 22, "digital business cards free"
  20, "vc background" 18, "what is a virtual business card" 16.

**Also fixed:** `index.html` line 7 had a stray second `>` closing the homepage
meta-description tag (`...small teams.">>`). Pre-existing; one character.

**Still blocked on the user:** Capterra, Product Hunt, AlternativeTo and
Trustpilot profiles do not exist, and G2 has 0 reviews. G2 Grid eligibility is
published at 10 approved reviews. Only the user can create accounts or ask real
customers for reviews; never seed fake ones.

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
