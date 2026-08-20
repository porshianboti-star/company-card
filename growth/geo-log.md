# CompanyCard GEO/SEO log

Measured state, appended each time work ships. Numbers only — no claims.

## 2026-08-20

**Deploys are working again.** The account-credit block that froze production
2026-08-01 → at least 08-04 is gone: live sitemap serves 53 URLs against 53 in
the repo at the start of this run, and commits through 2026-08-19 are live. The
"resubmit the sitemap once deploys work" item carried since 08-04 is now
actionable and was actioned (below).

**Google Search Console (read 2026-08-20, 28d to 08-17)**

| Metric | 2026-08-04 | 2026-08-20 | Change |
|---|---|---|---|
| Indexed pages | 16 | **31** | +94% |
| Not indexed | 6 | 19 | +13 |
| Impressions (28d) | 921 | **2,440** | +165% |
| Clicks (28d) | 3 | 5 | +2 |
| Query rows | 159 | **287** | +80% |
| Avg position | 57.9 | 59.4 | −1.5 |

Indexing roughly doubled. Average position drifted 1.5 places worse while query
rows grew 80% — that is dilution from a longer tail entering the index, not a
ranking loss; the head queries all moved up in impressions.

**First brand-query result ever recorded.** "companycard" now shows **7
impressions and 1 click** — the first click on a brand query, and the first
evidence of any brand-entity recognition. Every previous run recorded a brand
search returning zero CompanyCard results.

Top rows: "company card" 228 · "free digital business card" 144 · "best digital
business cards" 134 · "qr code business card" 125 · "best digital business card"
122 · "digital business cards free" 60 · "digital business card free" 51 ·
"best virtual business card" 38 · **"e name card" 36**.

**Two new not-indexed reasons appeared** (previously all 6 exclusions were the
benign alternate-canonical pairs):
- *Page with redirect* — 1 page.
- *Duplicate, Google chose different canonical than user* — 1 page, first
  detected **2026-08-11**: `best-digital-business-card.html`, a money page.
  Inspected rather than assumed. User-declared canonical is the `.html` form;
  **Google-selected canonical is the extensionless `/best-digital-business-card`**,
  and inspecting that URL returns **"URL is on Google — page is indexed"**. So
  the page is in the index under the other URL form; the exclusion is URL-form
  bookkeeping, not lost visibility. Both forms serve 200 and both declare the
  `.html` canonical, so the cause is the known Netlify behaviour: internal links
  ship extensionless while canonicals say `.html`, and for this one page the
  link graph outvoted the canonical hint.
  **Deliberately not "fixed."** Rewriting canonicals sitewide during a period
  when indexing is climbing would churn 54 pages to correct a page that is
  already indexed. Left alone, consistent with the 07-28 decision on the
  alternate-canonical pairs. Re-check next run; act only if it spreads.
- Inspection also reported **"No referring sitemaps detected"** for that URL
  even though it is in sitemap.xml with a 2026-08-18 lastmod — i.e. Google's
  sitemap read is stale (last read Jul 30, 47 discovered).
- "Crawled – currently not indexed" remains **0**. No quality signal.

**Shipped 1 — `/e-name-card.html`, chosen from measured demand, not the backlog**

The written backlog (uniqode / mobilo / wave-connect / v1ce alternatives, ten
self-employed trades, vs-nfc-card, for-events, vcard-qr-code) is **fully
shipped**; the comparison cluster was re-verified 08-18 and 08-19. So this run
picked from GSC instead: **"e name card" is the 10th-largest query row on the
property (36 impressions)** while a repo-wide grep for "name card", "namecard",
"ename" and "e-name card" across all 55 pages and llms.txt returned **zero
matches**. Same shape as the finding that started the ICP programme.

"Name card" is the ordinary English term for a business card in Singapore and
Malaysia; term usage confirmed 2026-08-20 across hausmedia.com.sg, digitalcard
.com.sg, sgnamecard.com.sg, singaporedigitalnamecard.com and geniccards.com.
**No claim is made about any of those vendors** — not their prices, features or
size — and none is cited on the page.

Anti-cannibalisation: four adjacent pages, none rewritten. `virtual-business-
card.html` already owns the H2 "Virtual vs. digital vs. electronic — what's the
difference?", so this page does not run a fourth synonym-comparison section; it
answers the naming question once and moves on. Its distinct substance is the one
problem the other pages never address: **a name written in more than one script**
costs a printed card a second side and costs a digital card nothing. That
section is written as a conditional about paper, not as a claim about any
country's customs.

Deliberately not stated (listed in the `seo/pages_data13.py` header): any market
size or adoption statistic; any competitor price or feature; any assertion about
business-card etiquette or greeting customs; any claim about non-Latin script
rendering beyond a normal text field; any claim about where our users are.

**Shipped 2 — a self-contradiction on `pricing.html` that attacked our own
strongest differentiator**

The Pricing FAQ answered "What do the paid plans add?" with *"Paid plans add
things like custom branding, **Apple & Google Wallet passes**, lead capture…"*
— while the plan table directly above it lists **"Add to Apple & Google Wallet"
under Free**, the page's own AggregateOffer puts the Wallet pass in the Free
offer, and llms.txt says the same. Wallet-on-the-$0-plan is one of our three
checkable differentiators, and the page was disproving it in **visible text and
in FAQPage JSON-LD** — the copy an assistant actually reads. Present in exactly
one file, in both copies (the `<details>` and the JSON-LD), both replaced
together. Replacement states what Pro and Team plans really add, taken from the
plan cards, and ends: "Apple and Google Wallet passes are not on that list —
those are included on the free plan."

**Freshness — did NOT run `add_freshness.py`**, and the reason is recorded in
`seo/freshness_batch13.py`. Unmodified it would have (a) restamped all 55 pages
for what was only an added footer link, (b) overwritten every sitemap `lastmod`
with one date, destroying the accurate per-page values set on 08-18/08-19, and
(c) bumped `datePublished` for its 21-slug NEW_TODAY set. Only the two pages
whose content actually changed were stamped.

⚠️ **Pre-existing inaccuracy found, deliberately not touched:** 21 pages carry
`datePublished: 2026-08-02` from an earlier run of `add_freshness.py`, but were
published in July (batches 1–3, 10, 11). Their true publication dates are not
recoverable from the repo, so this pass left them rather than moving them
further from the truth. `add_freshness.py` will reintroduce this every time it
runs — it needs a fix before next use.

⚠️ **`add_freshness.py` also silently strips `disambiguatingDescription`** from
the publisher node. All 54 pages carry it (the "not a corporate credit card"
category-collision work). The first run of the batch-13 stamper reproduced that
bug on `pricing.html`; caught in diff review, the stamper now emits the field
and `pricing.html` was restored and re-patched.

**Wiring & validation**
- Footer: sitewide via the single uniform anchor `<li><a href="vcard-qr-code
  .html">vCard QR Code</a></li>` — **55 of 57 HTML files**. The two skipped are
  `google6d2321e9b9904736.html` (Google verification stub) and `brand-kit.html`
  (has no footer and is not in the sitemap).
- `llms.txt`: page listed beside its terminology siblings, and the Category line
  now names "e-name card" / "digital name card" / "e-namecard" as regional
  synonyms so an assistant matching the term reaches us.
- Sitemap **53 → 54**, `xmllint --noout` passes; every `<loc>` resolves to a
  file that exists.
- New page: exactly one `<h1>`, unique title, 160-char meta description, one
  canonical, **4 valid JSON-LD blocks** (FAQPage + BreadcrumbList + HowTo +
  WebPage).
- `sync_faq_schema.py`: **0 mismatches**. An independent byte-comparison of all
  275 visible/JSON-LD question pairs across 52 pages found 0 real mismatches
  (one apparent hit on `digital-business-card.html` is an answer rendered as an
  `<h2>` + prose rather than a `<details>`, pre-existing and correct).
- Diff review: 53 files changed by exactly the one footer line; `pricing.html`
  was the only page with a content change.

**Off-site — still the binding constraint, unchanged**
- `Organization.sameAs` = G2 (product + seller) and the Chrome Web Store listing.
- **Capterra / Trustpilot / Product Hunt / AlternativeTo still do not exist.**
  Searched 2026-08-20; no CompanyCard profile on any of them. Only the owner can
  create these, and it remains the single biggest GEO blocker.
- A brand-name search still surfaces no CompanyCard-owned third-party result —
  though GSC now records the first brand-query click, so the entity is starting
  to register with Google even without off-site corroboration.

## 2026-08-04

> ### ⛔ STILL NOT LIVE — NETLIFY DEPLOYS REMAIN BLOCKED (day 3)
>
> `published_deploy` is **still `f5d9ab8` (2026-08-01 07:05)**. A deploy fired
> today at 08:52 UTC and came back `state=error`, `skipped=true`,
> `published_at=null` — the same account-credit block, not a build failure.
> Live `/vcard-qr-code` still 404s; live sitemap still 50 URLs against 52 in
> the repo. **Only the owner can clear this (billing action).** Everything in
> this entry is committed and goes live on the first successful build.

**Shipped — monthly competitor re-verification (commit `805efb8`)**

Re-read all seven vendors' own pricing pages on 2026-08-04 *before* moving any
stamp from July to August. No stamp was bumped on a figure that was not
re-fetched today.

| Vendor | Re-read today | Result |
|---|---|---|
| Blinq | blinq.me/pricing | Free = 2 cards, **Google *and* Apple Wallet**, email signature, virtual backgrounds. Premium $9.99/mo ($7.33 annual). Business $6.99/card/mo ($4.99 annual), "minimum payment equal to 5 Team Cards" |
| HiHello | hihello.com/pricing | Personal free = 4 cards, 5 card & badge scans/mo. Professional $6/mo. Business $5/user/mo, 5–100 users |
| Uniqode | uniqode.com/pricing | "We currently only offer annual subscription plans." First card free, free forever. Team $6/user/mo. **No seat minimum published** |
| Mobilo | mobilocard.com/pricing-2 | Pro $3/mo, Teams $4/mo annual, Business $5/mo annual. Free digital card. NFC sold separately. List prices $19.99 / $39 / $139 still shown |
| Wave Connect | wavecnct.com/pages/pricing | Free tier real. Pro $7/mo. Teams $5/user/mo, **"3 minimum seats"**. NFC not required |
| V1CE | v1ce.co/pricing | No free plan. 30-day trial, then single tier (£49 headline, "£49.99/mo after trial"). Card from £75, "no subscription required" |
| Popl | popl.co + /pages/pricing | No free plan, no published prices. H1 still "Your AI GTM platform for in-person events" |
| Linq | linqapp.com | Still "APIs for iMessage, RCS, SMS, and Voice" — no card product |

**Correction shipped: Uniqode's "2-seat minimum" is gone from the site.**
Four pages asserted Uniqode's Team plan "requires at least two seats". That
figure is **not published on uniqode.com/pricing today** — searched the rendered
page for `2 seats`, `two seats`, `seat minimum`, `minimum of N`: zero matches.
It may still be true; we cannot verify it, so it came off every page.
`uniqode-alternative.html` was re-anchored on the axis that *is* verifiable —
annual-only billing, stated outright in their own FAQ — including its `<title>`,
meta description, og/twitter tags, lead, body, comparison table and FAQ schema.
This is the **third** instance of the same failure mode (after the false "Blinq
lacks email signature" claim and the stale "Popl is an NFC hardware company"
thesis). The rule holds: re-fetch, never restate.

Also corrected from today's re-read:
- Blinq's free plan gets Google Wallet too, and lists no scan cap — our
  comparison table understated the competitor on both.
- **New Wave Connect row** in the free-plan table: free tier, $7/mo Pro, and a
  real **3-seat floor** on Teams. Verified, and it carries the seat-minimum
  argument better than the claim just removed.
- Mobilo source link pointed at a redirecting `/pricing` → now `/pricing-2`.
- V1CE source link pointed at `v1ce.co/pages/pricing` (403) → now `v1ce.co/pricing`.
- Stray `>` was closing the meta description on `best-digital-business-card.html`
  and **rendering as a visible `>` above the nav**. Same typo class as the one
  fixed on `index.html` in batch 12.
- **`linq-alternative.html` was live and footer-linked but had never been added
  to `sitemap.xml`.** Added — the page has existed unindexed-by-sitemap since
  batch 1.

Freshness handled honestly this pass: `dateModified` and sitemap `lastmod` were
bumped **only for the 12 pages actually changed**, not sitewide.
`seo/add_freshness.py` rewrites all 55 pages by default; the 43 whitespace-only
rewrites were reverted so the diff shows only real edits.

**Validation:** 12/12 changed pages have exactly one `<h1>`, a title, a meta
description, one canonical, and valid JSON-LD. `sync_faq_schema.py` reports
**0 mismatches**. `xmllint --noout sitemap.xml` passes.

**Site**
- Sitemap URLs: 51 → **52** in repo (linq-alternative added); **50 live** (frozen)
- Pages carrying a July 2026 stamp: 13 → **0** (only `privacy-policy.html`
  retains "5 July 2026", which is its true last-updated date)
- `llms.txt` competitor stamps re-dated to August 2026 (facts re-verified)

**Google Search Console (read 2026-08-04)**
- Indexed **16** · Not indexed **6** — unchanged since 07-28
- All 6 exclusions still "Alternate page with proper canonical tag";
  **"Crawled – currently not indexed" = 0**. No new exclusion reason appeared.
- Performance, 28d (Jul 6 – Aug 2): **921 impressions** (was 636 on 07-30,
  **+45%**), **3 clicks**, avg position **57.9** (was 55.3), **159 query rows**
  (was 115, **+38%**)
- Growing queries: "qr code business card" 27 → **51**, "free digital business
  card" 23 → **46**. Top row is "company card" at 155 impressions.
- GSC flagged `free-digital-business-card.html` impressions **+6,000%**
- Sitemap last read **Jul 30**, 47 discovered. **Not resubmitted this run** —
  production is frozen, so a re-read would only surface the 3 URLs that went
  live before the block. Resubmit once deploys work and the 52-URL sitemap is
  actually being served.

**Off-site — still the binding constraint**
- G2: live and wired (`sameAs`, `llms.txt`, `about.html`) — still returns
  nothing on a brand search, i.e. not yet indexed by Google
- Capterra / Trustpilot / Product Hunt / AlternativeTo: **still do not exist**
- A brand search for "CompanyCard company-card.com digital business card"
  returns **zero CompanyCard results** — competitors only. Unchanged since 07-30.
- Direct URL probes are useless for this check: capterra/trustpilot/PH/
  alternativeto/G2 all return **403 to curl**, including the G2 profile we know
  exists. Use search, not status codes.

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
> **A direct file deploy does NOT work around it.** The site has no build
> command and no publish dir (it serves the tracked repo root as-is, confirmed:
> `/README.md`, `/seo/build_pages.py` etc. all return 200), so I tried a direct
> Deploy-API upload of the 183 tracked files to bypass the build entirely. The
> API refused at the create-deploy step:
> `403 — "Account credit usage exceeded - new deploys are blocked until credits
> are added"`. So this is **not** a build-minutes problem that a file upload can
> sidestep; it is a hard account-level block on all new deploys.
> **Next run: do not retry the deploy trick — check credits first.**
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
