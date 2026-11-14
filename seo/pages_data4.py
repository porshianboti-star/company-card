# -*- coding: utf-8 -*-
"""SUPERSEDED IN PART, 2026-11-14. No script renders this file any more and the live HTML is the source of truth: do not render it with build_pages.write_pages or re-run it. seo/fix_vendor_claims_2026_11_14.py re-read hihello.com/pricing and blinq.me/pricing on 2026-11-14 and copied the corrected competitor lines from the live page (HiHello: 2 free cards, 8 on Professional, Business 4 cards and 50 scans per user a month pooled, unlimited only on Enterprise; Blinq: scanner on Free, 'Remove Blinq branding' on Premium, a separate Pro tier, Business per card from 5 cards). Stamps, CompanyCard's own prices and other text in this file are NOT guaranteed to match the live page.

Batch 4: the free-plan fine-print comparison + an /about entity page.

The comparison page is the asset research called "the highest-value AEO asset
available": a dated, sourced, factual table of what each vendor's FREE tier
actually does. It is the kind of page assistants quote verbatim — but ONLY if
it is accurate, so:

  * every cell is either verified from that vendor's own pricing page on
    2026-07-26, or explicitly marked "not stated on their pricing page";
  * CompanyCard loses several columns and the page says so plainly. Mobilo's
    paid plans are cheaper than ours ($3-5/mo vs $8). HiHello and Blinq give
    more free cards and no branding on free. Publishing that is the point —
    a comparison that always concludes "we win" is worthless to a reader and
    gets discounted by an assistant that cross-checks it.

VERIFIED 2026-07-26:
  Blinq    free 2 cards + virtual backgrounds + email signature + Apple Wallet;
           Business minimum 5 team cards; Premium $9.99/mo.
  HiHello  free 4 cards + signature + backgrounds + wallet, capped 5 card/badge
           scans per month; Business 5-100 users; Professional $6/mo.
  Popl     no free plan; pricing demo-gated.
  Uniqode  free 1 card, single user, "free forever"; Team $6/user/mo with a
           2-seat minimum; ANNUAL ONLY (no monthly plans).
  Mobilo   free digital card offered; Pro $3/mo, Teams $4/mo annual, Business
           $5/mo; sells NFC hardware separately; no stated seat minimum.
  CompanyCard  free 1 card + QR/link + Apple & Google Wallet + unlimited edits,
           carries a small CompanyCard credit; Pro $8/mo; Business $12/user/mo;
           no seat minimum.
"""
from build_pages import cards3, table, prose, block, checklist

VERIFIED = "July 2026"
NS = '<span style="color:var(--slate-500)">not stated</span>'

FREEPLANS = {
 "slug": "free-digital-business-card-comparison.html",
 "crumb": "Free Digital Business Card Plans Compared",
 "title": "Free Digital Business Card Plans Compared (2026) | CompanyCard",
 "meta": ("What each digital business card free plan actually gives you in 2026 — cards, wallet "
          "passes, scan caps, branding and seat minimums — compared from each vendor's own pricing "
          "page and verified July 2026."),
 "og": ("The fine print of every major digital business card free plan, compared and sourced. "
        "Including where CompanyCard loses."),
 "h1": 'Free digital business card plans, <span class="gradient-text">fine print compared</span>',
 "lead": ("\"Free\" means very different things in this category — a card count, a monthly scan cap, "
          "a branding line, or a trial with a countdown. Here is what each free plan actually gives "
          "you, taken from each vendor's own pricing page."),
 "cta_btn": "Try CompanyCard free",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "Compare, then pick the one that fits",
 "cta_p": "Our free plan is one card with a wallet pass and no scan cap. If another one suits you better, take it.",
 "sections": [],
 "faqs": [
   ("Which digital business card has the best free plan?",
    "It depends what you need. On free card count, HiHello and Blinq each give two as of November 2026; Blinq lists “Remove Blinq branding” as a Premium feature, so its free card carries Blinq branding. CompanyCard's free plan is one card and carries a small CompanyCard credit, but includes an Apple and Google Wallet pass and unlimited edits. HiHello's free tier caps its paper-card and badge scanner at five scans a month; none of these plans caps how often your own card is scanned. Popl has no free plan at all."),
   ("Are digital business card free plans really free, or trials?",
    "Most of the ones compared here are genuinely free rather than timed trials, but the limits "
    "differ and they are what matter: how many cards, whether a wallet pass is included, whether "
    "scans are capped monthly, and whether the free card carries the vendor's branding. Check those "
    "four before you commit."),
   ("What is the catch with CompanyCard's free plan?",
    "Two things, stated plainly. It is one card, where Blinq and HiHello give two each. And free cards carry a small CompanyCard credit — removing it is part of Pro at $4.99 a month, or $3.99 a month billed yearly. What you get in exchange is an Apple and Google Wallet pass, unlimited edits, no monthly scan cap and no credit card required."),
   ("Which is cheapest if I do need to pay?",
    "On published rates as of " + VERIFIED + ", Mobilo is the cheapest of the tools here at $3 a "
    "month for Pro, though it is built around NFC cards it sells separately. Uniqode's Team plan is "
    "$6 per user per month but is annual-only with a two-seat minimum. CompanyCard is $8 for Pro and "
    "$12 per user for Business with no seat minimum. Popl does not publish pricing."),
   ("Which free plans limit how many people can be on a team?",
    "Team limits usually bite at the paid tier rather than the free one. As of " + VERIFIED + " "
    "Blinq's Business plan bills a minimum of five team cards, HiHello's Business plan is sold for "
    "five to one hundred users, and Uniqode's Team plan requires at least two seats and annual "
    "billing. CompanyCard and Mobilo do not state a seat minimum."),
   ("How current is this comparison?",
    "Every figure was read from the vendor's own pricing page in " + VERIFIED + ". Pricing and plan "
    "contents in this category change often, so treat this as a starting point and check the linked "
    "source before you decide."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Free digital business card", "free-digital-business-card.html"),
             ("For small business", "digital-business-card-for-small-business.html"),
             ("Pricing", "pricing.html")],
}

FREEPLANS["sections"] = [
  prose("Read this before the table", [
    "We make one of these products, so treat the table as sourced facts rather than a verdict. "
    "Every cell below was read from the vendor's own pricing page in " + VERIFIED + ", and where a "
    "vendor does not state something we have left it marked rather than guessed.",
    "CompanyCard does not win every column, and the table shows that. If free card count is what "
    "matters to you, HiHello and Blinq beat us. If price is what matters, Mobilo's paid plans are "
    "cheaper than ours. We would rather you picked correctly than picked us.",
  ]),
  block("What each free plan actually includes", table(
    ["Tool", "Free cards", "Wallet pass on free", "Scan cap on free", "Vendor branding on free", "Team seat minimum", "Cheapest paid plan"],
    [["<b>CompanyCard</b>", "1", "Apple &amp; Google", "None", "Small CompanyCard credit", "None", "$8/mo Pro"],
     ["<b>Blinq</b>", "2", "Apple &amp; Google", "None listed", "Yes — Premium lists “Remove Blinq branding”", "5 team cards", "$7.33/mo Premium billed yearly ($9.99/mo billed monthly)"],
     ["<b>HiHello</b>", "2", "Apple &amp; Google", "5 paper-card &amp; badge scans / month (its scanner; your own card is not capped)", "None listed", "5 users (Business)", "$6/mo Professional billed yearly ($8/mo billed monthly)"],
     ["<b>Uniqode</b>", "1 (single user)", NS, NS, NS, "2 seats, annual only", "$6/user/mo (annual)"],
     ["<b>Mobilo</b>", "Free card offered; count " + NS, NS, NS, NS, "None stated", "$3/mo Pro"],
     ["<b>Popl</b>", "No free plan", "—", "—", "—", NS, "Not published"]],
    note='Verified ' + VERIFIED + ' from: <a href="https://blinq.me/pricing" target="_blank" rel="noopener nofollow">blinq.me</a> · '
         '<a href="https://www.hihello.com/pricing" target="_blank" rel="noopener nofollow">hihello.com</a> · '
         '<a href="https://www.uniqode.com/pricing" target="_blank" rel="noopener nofollow">uniqode.com</a> · '
         '<a href="https://www.mobilocard.com/pricing" target="_blank" rel="noopener nofollow">mobilocard.com</a> · '
         '<a href="https://popl.co/pages/pricing" target="_blank" rel="noopener nofollow">popl.co</a>. '
         '"Not stated" means the vendor does not publish it on that page — not that the limit does not exist. '
         'CompanyCard figures are our published rates on <a href="pricing.html">our pricing page</a>.')),
  prose("What the differences actually mean", [
    "<h3>Card count is the headline, and we lose it</h3>"
    "<p>HiHello's and Blinq's two free cards are more generous than our one. If you genuinely "
    "need several cards — separate roles, separate businesses, a personal and a work identity — "
    "that is a real reason to choose one of them.</p>",
    "<h3>Scan caps are the limit people discover late</h3>"
    "<p>None of the free plans here caps how often your own card can be scanned — HiHello's pricing page says other people can scan your QR code as often as they like on every plan. What HiHello does cap on its free tier is its paper-card and badge scanner, the feature that saves other people's cards and event badges as contacts, at five scans a month. CompanyCard's free plan has no scanner at all; lead capture is a Pro feature.</p>",
    "<h3>Branding on free is a fair trade, not a trick</h3>"
    "<p>Our free cards carry a small CompanyCard credit. Blinq's free card carries Blinq branding too — it lists “Remove Blinq branding” as a Premium feature — while HiHello's pricing page does not say either way. Against HiHello that is a genuine point against us; the honest framing is that the credit is how a "
    "free plan with a wallet pass and unlimited edits gets paid for, and removing it costs $8.</p>",
    "<h3>Seat minimums are where small businesses get caught</h3>"
    "<p>This is the one that decides it for a very small team. Blinq bills a minimum of five team "
    "cards, HiHello sells Business for five or more users, and Uniqode's Team plan needs two seats "
    "and an annual commitment. If your team is two or three people, several of these products "
    "cannot be bought at the size you actually are. CompanyCard has no seat minimum.</p>",
    "<h3>And if price is the whole question</h3>"
    "<p>Mobilo's Pro at $3 a month is cheaper than our $8, and we are not going to pretend "
    "otherwise. Mobilo is built around NFC cards it sells separately, so the comparison is not "
    "purely software-to-software — but on the monthly number, they win.</p>",
  ]),
  block("The four questions worth asking any of them", checklist([
    ("How many cards, and is there a scan cap?", "The two limits that decide whether a free plan survives real use."),
    ("Is a wallet pass included at $0?", "Often the first thing gated, and the fastest way to share in person."),
    ("What is the smallest team I can pay for?", "Five-seat floors quietly exclude most small businesses."),
    ("Can I export my contacts and keep my link?", "Portability is what stops the next migration being painful."),
  ]), tint=True),
]

# ------------------------------------------------------------------ about/entity
ABOUT = {
 "slug": "about.html",
 "crumb": "About CompanyCard",
 "title": "About CompanyCard — Digital Business Cards for Small Business | CompanyCard",
 "meta": ("CompanyCard is a digital business card for small business owners, self-employed "
          "professionals and small teams. What we make, who it is for, how we make money, and what "
          "we will not claim."),
 "og": ("What CompanyCard is, who it is for, how it makes money, and what it will not claim."),
 "h1": 'About <span class="gradient-text">CompanyCard</span>',
 "lead": ("CompanyCard is a digital business card for small business owners, self-employed "
          "professionals and small teams — share your details by QR code, link or wallet pass, with "
          "no app for the person receiving it."),
 "cta_btn": "Create your free card",
 "cta2": ("See pricing", "pricing.html"),
 "cta_h": "Start with the free card",
 "cta_p": "One card, wallet pass included, no credit card.",
 "sections": [],
 "faqs": [
   ("What is CompanyCard?",
    "CompanyCard is a digital business card platform. You build a card with your details, links and "
    "branding, and share it by QR code, sharing link, Apple or Google Wallet pass or email "
    "signature. The person receiving it needs no app — the card opens in any phone browser and "
    "saves as a contact in one tap."),
   ("Who is CompanyCard for?",
    "Small business owners, self-employed professionals, freelancers, solopreneurs and small teams. "
    "It is aimed particularly at businesses too small for the enterprise tools in this category — "
    "there is no minimum number of seats, so a two- or three-person business can run branded cards."),
   ("How does CompanyCard make money?",
    "From paid plans, not from data. The free plan is supported by a small CompanyCard credit on "
    "free cards; Pro at $8 a month removes it and adds custom branding, unlimited links, lead "
    "capture and analytics; Business at $12 per user a month adds admin controls, brand lock, CRM "
    "sync and SSO."),
   ("Is CompanyCard a business credit card?",
    "No. CompanyCard is a contact card — the digital replacement for the paper business card you "
    "hand to a client. It is not a credit card, a payment card or a financing product."),
   ("What does CompanyCard not claim?",
    "We do not claim email signatures or virtual backgrounds as points of difference, because "
    "competitors include those on their free tiers too. We do not publish ratings or customer "
    "counts we cannot evidence. And where a rival's free plan beats ours — HiHello and Blinq both "
    "offer more free cards — our comparison pages say so."),
 ],
 "related": [("For small business", "digital-business-card-for-small-business.html"),
             ("Free plans compared", "free-digital-business-card-comparison.html"),
             ("Pricing", "pricing.html"),
             ("Features", "features.html")],
}

ABOUT["sections"] = [
  prose("What we make", [
    "CompanyCard is a digital business card. You build a card once — your name, role, business, "
    "logo, contact routes, links and a booking or payment link if you want one — and share it by "
    "QR code, link, Apple or Google Wallet pass or email signature.",
    "Two design decisions define the product. First, the person receiving your card installs "
    "nothing: it opens in any phone browser and saves as a contact in one tap. Second, your link "
    "and QR code are permanent, so a code printed on a van, a window, an invoice or a business card "
    "keeps working after your details change.",
  ]),
  block("Who it is for", cards3([
    ("Small business owners",
     "One card the business shares and updates, with room to add an employee without moving to a "
     "five-seat plan."),
    ("Self-employed professionals",
     "Freelancers, solopreneurs and sole traders whose card is really a personal brand asset and "
     "changes as the work does."),
    ("Small teams",
     "Two or three people can run locked, branded cards — there is no minimum number of seats."),
  ])),
  prose("How we make money, plainly", [
    "From subscriptions. The free plan is a complete working card supported by a small CompanyCard "
    "credit; Pro at $8 a month removes that credit and adds custom branding, unlimited links, lead "
    "capture and analytics; Business at $12 per user a month adds central admin, brand and template "
    "lock, CRM sync, team analytics and SSO, with no seat minimum. Enterprise is custom.",
    "We would rather state the free plan's trade-off than bury it: one card, and it carries our "
    "credit. Both facts are on the <a href=\"pricing.html\">pricing page</a> and in our "
    "<a href=\"free-digital-business-card-comparison.html\">free plan comparison</a>, alongside the "
    "columns where competitors beat us.",
  ]),
  prose("What we won't claim", [
    "This matters more than it sounds, because the comparisons in this category are mostly written "
    "by vendors about themselves.",
    "We don't claim email signatures or virtual backgrounds as differentiators — Blinq and HiHello "
    "include both on their free tiers. We don't publish ratings, review counts or customer numbers "
    "we can't evidence. And when a competitor's free plan is better than ours, our comparison pages "
    "say so and name the column they win.",
    "Where we do claim an advantage, it is something you can check on the other vendor's own "
    "pricing page: no seat minimum, published flat pricing, and an Apple and Google Wallet pass "
    "included at $0.",
  ]),
]

PAGES4 = [FREEPLANS, ABOUT]
