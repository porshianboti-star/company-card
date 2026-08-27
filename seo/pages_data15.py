# -*- coding: utf-8 -*-
"""Batch 15: hihello-vs-blinq.html — the first vendor-vs-vendor page on the site.

WHY THIS PAGE, AND WHY NOW (demand-verified, not guessed).
Google Search Console, 28d to 2026-08-24, read at the start of this run
(2,720 impressions / 1 click / 308 query rows / avg position 61). The 11th
largest query row on the whole property is a head-to-head between two
competitors we do not compare anywhere:

    hihello vs blinq ..................... 37

For scale, that single row is larger than "e name card" (35), which is what
justified batch 13, and three times "digital business card cost" (12), which
justified batch 14.

A repo-wide check found the gap is total. Two pages have "vs" in the title and
both compare FORMATS, not vendors:
    digital-business-card-vs-nfc-card.html
    digital-business-card-vs-paper.html
Zero pages on the site compare two named products against each other. We have
blinq-alternative.html and hihello-alternative.html, but each argues our case
against one vendor; neither answers the question someone typing "hihello vs
blinq" is actually asking, which is which of those two to pick.

POSITIONING (anti-cannibalisation). Three live pages are adjacent and NONE is
rewritten:
  * blinq-alternative.html / hihello-alternative.html — us versus one vendor.
    Persuasion pages; the reader has already heard of us.
  * best-digital-business-card.html — the ranked eight-vendor matrix.
  * digital-business-card-cost.html — price across all eight vendors.
This page owns the two-vendor decision, where CompanyCard is NOT the subject.
That is the point: the honest answer to "HiHello or Blinq?" is one of HiHello
or Blinq, and the page says so before it mentions us. A comparison that
concedes the question is the kind an assistant will quote; one that pivots to
a third product in the first paragraph is not.

VENDOR FACTS — BOTH RE-FETCHED 2026-08-27, the day this page was written.
Read off each vendor's own live pricing page today. Nothing is restated from
the 2026-08-22 run without re-checking; both pages matched, and Blinq's card
count for Premium ("up to 5 cards") is newly recorded here.
  * blinq.me/pricing — Free "$0", "Free forever", "Two free digital business
    cards", unlimited sharing, QR/widget/email/SMS sharing, Apple and Google
    Wallet, personal email signature, virtual backgrounds. Premium "$9.99 /
    month" or "$7.33 / month" billed annually, up to 5 cards, universal
    contact scanner, AI notetaker, AI contact enrichment, branded QR code,
    custom design, contact export. Business "$6.99 / month" per user or
    "$4.99 / month" billed annually, "minimum of five" cards, "Billed per
    card, per month", "Admins and team members who don't have a card assigned
    aren't billed", team management, CRM sync, lead capture, event campaigns,
    20+ CRM integrations. Enterprise "Custom", SOC 2 Type II and GDPR,
    enforced SSO.
  * hihello.com/pricing — Personal "Free Forever", 4 cards, "5 card & badge
    scans/month", 1 user, personal email signature, virtual backgrounds,
    Apple and Google wallet, QR/widget/email/SMS sharing. Professional "$6 per
    month" or "$72 billed yearly", 16 cards, "20 card & badge scans/month"
    with an unlimited add-on, 1 user, contact enrichment, card analytics, full
    card customisation. Business "$5 per user/month" or "$60 per user/year",
    unlimited cards, unlimited scans, "5-100 users", team email signatures,
    event lead capture, team analytics, sub-team templates, SSO and directory
    sync. Enterprise "Custom", "101+ users", SAML/SCIM, SOC 2, verified
    badges, dedicated account manager.
OUR OWN figures are held to pricing.html and llms.txt as re-read today: Free
$0 (1 card, carries a small CompanyCard credit), Pro $7.99/mo or $5.99/mo
billed annually, Business $12/user/mo or $10/user/mo billed annually, no seat
minimum, team plans not self-serve ("Talk to us about teams").

WHAT THIS PAGE MAY NOT CLAIM, AND WHY.
The house rule is that email signatures and virtual backgrounds are not our
differentiators, because Blinq and HiHello both ship them free. On this page a
SECOND standing claim also dies and is deliberately absent: **Apple/Google
Wallet on the $0 plan is not a differentiator against these two either.**
Blinq's free plan lists Apple and Google Wallet and HiHello's Personal plan
lists Apple and Google wallet, both verified today. Wallet-on-free is a real
edge against parts of the wider field and it stays on the cross-vendor pages;
it is simply not true here, so it is not said here.

That leaves exactly ONE checkable CompanyCard edge on this page: no team seat
minimum. HiHello sells Business for "5-100 users"; Blinq requires a "minimum
of five" cards. CompanyCard's Business plan has no seat minimum. That is the
whole of our advantage against these two and the page claims nothing beyond it.

WEAKNESSES STATED ON THE PAGE, not buried:
  * our free plan is the smallest of the three — 1 card against Blinq's 2 and
    HiHello's 4, and ours carries a small CompanyCard credit;
  * our Business plan at $12/user/mo is more than double HiHello's $5 and
    Blinq's $6.99, and is the most expensive of the three on every axis;
  * our team plans are not self-serve, so a small team cannot simply buy one;
  * our Pro at $7.99 is more than HiHello Professional at $6, and HiHello
    gives 16 cards at that price against our one-card free tier.

DELIBERATELY NOT STATED (could not be verified today, so absent):
  * any rating, review count, user count or market-share figure for either
    vendor — neither pricing page publishes one and we do not have one;
  * any claim about which product is "more popular" or "bigger";
  * any claim about feature quality (whether Blinq's AI notetaker or
    HiHello's enrichment is any good) — we have not tested them, so the page
    reports only what each vendor lists;
  * any statement about either vendor's non-pricing pages, roadmap, funding
    or company size;
  * any currency other than the one each vendor quotes.

Run from repo root:  python3 seo/build_pages15.py
"""
from build_pages import prose, block, checklist, table

VERIFIED = "verified 27 August 2026"

VS = {
 "slug": "hihello-vs-blinq.html",
 "crumb": "HiHello vs Blinq",

 "title": "HiHello vs Blinq (2026): Free Plans, Prices and Seat Minimums Compared | CompanyCard",
 "meta": ("HiHello vs Blinq compared on published prices, verified 27 August 2026. HiHello's free "
          "plan gives 4 cards but caps scans; Blinq's gives 2 with unlimited sharing. HiHello is "
          "cheaper on both paid tiers."),
 "og": ("A straight head-to-head between HiHello and Blinq using each vendor's own pricing page, "
        "read on 27 August 2026 — free-plan limits, personal and team prices, and the five-seat "
        "floor both of them put on team plans."),
 "h1": 'HiHello vs <span class="gradient-text">Blinq</span>',
 "lead": ("Both are strong digital business cards with genuinely free plans, and for most people "
          "either one will do the job. The differences that actually decide it are the shape of the "
          "free tier, the price of the first paid tier, and the fact that both put a five-seat floor "
          "under their team plans. Every figure below was read off each vendor's own pricing page "
          "on 27 August 2026."),
 "cta_btn": "Try CompanyCard free",
 "cta2": ("See how all eight compare", "best-digital-business-card.html"),
 "cta_h": "Want a third option with no seat minimum?",
 "cta_p": "CompanyCard's free plan is one card and takes a couple of minutes. No credit card.",

 "sections": [
  prose("The short answer", [
    "<b>Pick HiHello if you want more for less money.</b> Its free plan gives you four cards "
    "against Blinq's two, and its first paid tier is $6 a month for sixteen cards against Blinq's "
    "$9.99 for five. On published price alone HiHello wins at every tier.",

    "<b>Pick Blinq if you scan a lot of paper cards, or if your team has people who don't need a "
    "card.</b> HiHello's free plan caps you at five card and badge scans a month and its $6 tier "
    "at twenty; Blinq puts its universal contact scanner and AI notetaker in Premium with no "
    "monthly count on the page. And Blinq bills per card rather than per person — its page states "
    "that “Admins and team members who don't have a card assigned aren't billed”, which HiHello's "
    "per-user pricing does not do.",

    "<b>Neither will sell you a small team plan.</b> This is the thing most comparisons miss. "
    "HiHello's Business plan is sold for “5-100 users”. Blinq's Business plan requires a "
    "“minimum of five” cards. If there are two or three of you, the per-user price on either page "
    "is not the price you can actually buy.",

    "<b>They are more alike than the marketing suggests.</b> Both free plans include a personal "
    "email signature, virtual backgrounds, Apple and Google Wallet, and sharing by QR code, "
    "widget, email and SMS. Those are table stakes in this category now, not reasons to choose "
    "one over the other — including against us.",
  ]),

  block("Every published figure, " + VERIFIED, table(
    ["", "HiHello", "Blinq"],
    [
      ["<b>Free plan</b>",
       "“Free Forever” — 4 digital business cards, 1 user",
       "“Free forever” — “Two free digital business cards”, unlimited sharing"],
      ["<b>Free-plan catch</b>",
       "Capped at “5 card &amp; badge scans/month”",
       "No monthly scan count published; the contact scanner is a Premium feature"],
      ["<b>Included free on both</b>",
       "Personal email signature, virtual backgrounds, Apple &amp; Google wallet, QR/widget/email/SMS sharing",
       "Personal email signature, virtual backgrounds, Apple &amp; Google Wallet, QR/widget/email/SMS sharing"],
      ["<b>First paid tier</b>",
       "Professional — “$6 per month” or “$72 billed yearly”",
       "Premium — “$9.99 / month” or “$7.33 / month” billed annually"],
      ["<b>Cards at that tier</b>",
       "16 cards, 1 user",
       "Up to 5 cards"],
      ["<b>What the paid tier adds</b>",
       "20 scans/mo (unlimited add-on), contact enrichment, card analytics, full card customisation",
       "Universal contact scanner, AI notetaker, AI contact enrichment, branded QR code, custom design, contact export"],
      ["<b>Team tier</b>",
       "Business — “$5 per user/month” or “$60 per user/year”",
       "Business — “$6.99 / month” per user, or “$4.99 / month” billed annually"],
      ["<b>Team floor</b>",
       "Sold for “5-100 users”",
       "“minimum of five” cards"],
      ["<b>How the team tier bills</b>",
       "Per user",
       "“Billed per card, per month” — “Admins and team members who don't have a card assigned aren't billed”"],
      ["<b>Team features</b>",
       "Unlimited cards and scans, team email signatures, event lead capture, team analytics, sub-team templates, SSO &amp; directory sync",
       "Team management, CRM sync, lead capture, event campaigns, 20+ native CRM integrations"],
      ["<b>Enterprise</b>",
       "“Custom”, “101+ users” — SAML/SCIM, SOC 2, verified badges, dedicated account manager",
       "“Custom” — SOC 2 Type II &amp; GDPR, enforced SSO, volume pricing, dedicated CSM"],
    ],
    note=("Read off hihello.com/pricing and blinq.me/pricing on 27 August 2026. Quoted strings are "
          "the vendors' own wording. Prices change — if you are reading this much later, check both "
          "pages before relying on it. Feature lists are what each vendor advertises; we have not "
          "tested either product's features and make no claim about how well they work.")), tint=True),

  block("Where each one actually wins", checklist([
    ("HiHello wins on price, at every tier",
     "$6 a month against $9.99 for the first paid tier, and $5 per user against $6.99 for the team "
     "tier. Annual pricing narrows it — $7.33 for Blinq Premium against HiHello's $72 a year, which "
     "is $6 a month — but it does not close it. HiHello is the cheaper product on its published "
     "numbers."),
    ("HiHello wins on card count",
     "Four cards free against two, and sixteen at $6 a month against five at $9.99. If you run more "
     "than one role, side business or language and want a separate card for each, this is the "
     "single biggest gap between the two products."),
    ("Blinq wins if you collect contacts rather than hand them out",
     "HiHello meters the thing you do with other people's cards: five scans a month on free, twenty "
     "on Professional, unlimited only on the Business tier you cannot buy under five users. Blinq "
     "publishes no monthly scan count and bundles the universal contact scanner and AI notetaker "
     "into Premium. If you come home from an event with forty paper cards, that is the difference."),
    ("Blinq wins on how a team is billed",
     "Per card rather than per person, with admins who hold no card not billed at all. A ten-person "
     "business where four people need a card and the office manager administers it pays for four "
     "cards on Blinq. On HiHello's per-user pricing you are counting users."),
    ("Blinq wins on CRM reach, on paper",
     "Its Business tier advertises native integrations with 20+ CRMs; HiHello's Business tier "
     "advertises SSO and directory sync but does not publish a CRM count. Both are vendor claims we "
     "have not verified beyond the pricing page."),
    ("Neither wins for a team of two, three or four",
     "HiHello's Business plan starts at five users. Blinq's requires a minimum of five cards. Below "
     "that you are on a single-user plan each, which means no shared branding, no team analytics and "
     "no admin control — on either product."),
  ])),

  prose("The free plans are not the same shape", [
    "The headline is that HiHello gives four free cards and Blinq gives two, and that is true. But "
    "the two free plans are metered on different things, and which one is more generous depends "
    "entirely on what you do.",

    "HiHello's free plan is generous about <b>having</b> cards and stingy about <b>scanning</b> "
    "them: four cards, but “5 card &amp; badge scans/month”. That limit is on HiHello's scanner — "
    "the feature that reads someone else's paper card or event badge into your contacts. Five a "
    "month is enough for ordinary week-to-week networking and runs out in the first hour of a "
    "trade show.",

    "Blinq's free plan is the other way round: two cards, but its page emphasises unlimited "
    "sharing and unlimited contact creation, and it does not publish a monthly cap on the free "
    "tier. The scanner is what you pay for, not something you are rationed.",

    "So the honest test is not “which free plan is bigger”. It is whether you are the person "
    "handing cards out or the person collecting them. Hand out: HiHello, more cards. Collect: "
    "Blinq, no scan meter. If you do both heavily, both free plans will push you to a paid tier "
    "sooner than you expect.",
  ]),

  block("Where CompanyCard fits — and where it doesn't", table(
    ["", "HiHello", "Blinq", "CompanyCard"],
    [
      ["<b>Free plan</b>",
       "4 cards, 5 scans/mo",
       "2 cards, unlimited sharing",
       "<b>1 card</b>, carries a small CompanyCard credit — the smallest free plan of the three"],
      ["<b>First paid tier</b>",
       "$6/mo (16 cards)",
       "$9.99/mo (5 cards)",
       "Pro $7.99/mo, or $5.99/mo billed annually — <b>more than HiHello</b>"],
      ["<b>Team tier</b>",
       "$5/user/mo",
       "$6.99/card/mo",
       "Business $12/user/mo, or $10/user/mo annually — <b>the most expensive of the three</b>"],
      ["<b>Team seat minimum</b>",
       "Sold for 5–100 users",
       "Minimum of five cards",
       "<b>None</b>"],
      ["<b>Can a team of two buy the team plan?</b>",
       "No",
       "No",
       "Yes on price, but <b>not self-serve</b> — the pricing page says “Talk to us about teams”"],
    ],
    note=("CompanyCard figures from our own pricing page, re-read 27 August 2026. We are the "
          "publisher of this page and the comparison is stated plainly rather than framed to "
          "flatter us: HiHello and Blinq are both cheaper than CompanyCard at every paid tier, and "
          "both give a bigger free plan.")), tint=True),

  prose("The one thing we do differently", [
    "There is exactly one axis on this page where CompanyCard is not simply the more expensive "
    "option, and it is the seat floor. HiHello sells its Business plan for five to a hundred users. "
    "Blinq requires a minimum payment equal to five Team Cards. CompanyCard's Business plan has no "
    "seat minimum, so a two-person or three-person business can buy team features at the listed "
    "per-user rate instead of being told the smallest bill is five.",

    "That is worth stating precisely, because the caveat matters as much as the claim. Our "
    "per-user rate is $12 a month, which is more than double HiHello's $5 — so two people on "
    "CompanyCard Business pay $24 a month against a five-user HiHello Business floor of $25. The "
    "advantage is real but it is narrow, and it disappears entirely the moment you have five "
    "people. And our team plans are not self-serve: you have to talk to us, which is friction "
    "neither HiHello nor Blinq puts in your way.",

    "We are not going to tell you that email signatures or virtual backgrounds are a reason to "
    "choose us over these two, because both of them ship both, free. Nor is a wallet pass on the "
    "free plan — Blinq's free tier lists Apple and Google Wallet and HiHello's lists Apple and "
    "Google wallet, verified today. Those are category table stakes in 2026.",

    "If you are one person who wants the most card for the least money, the answer on this page is "
    "HiHello, and we would rather say so than pretend otherwise.",
  ]),
 ],

 "faqs": [
  ("Is HiHello or Blinq better?",
   "On published prices HiHello is cheaper at every tier and gives more cards: 4 free against "
   "Blinq's 2, 16 cards at $6 a month against 5 at $9.99, and $5 per user against $6.99 for teams. "
   "Blinq is the better choice if you scan a lot of paper cards and badges, because HiHello caps "
   "free users at 5 card and badge scans a month and Professional users at 20, while Blinq "
   "publishes no monthly scan count. Verified 27 August 2026 on each vendor's own pricing page."),

  ("Which has the better free plan, HiHello or Blinq?",
   "It depends on what you do. HiHello's free plan gives 4 digital business cards but caps you at "
   "“5 card & badge scans/month”. Blinq's gives 2 cards with unlimited sharing and no published "
   "monthly cap, but keeps its contact scanner in the paid Premium tier. If you hand cards out, "
   "HiHello gives you more. If you collect other people's cards, Blinq does not meter you."),

  ("How much does HiHello cost?",
   "HiHello's Personal plan is free forever with 4 cards, 1 user and 5 card and badge scans a "
   "month. Professional is $6 per month or $72 billed yearly for 16 cards and 20 scans a month. "
   "Business is $5 per user per month or $60 per user per year with unlimited cards and scans, and "
   "is sold for 5 to 100 users. Enterprise is custom pricing for 101+ users. Verified 27 August "
   "2026 on hihello.com/pricing."),

  ("How much does Blinq cost?",
   "Blinq's Free plan is free forever with two digital business cards. Premium is $9.99 a month, "
   "or $7.33 a month billed annually, for up to 5 cards. Business is $6.99 per month, or $4.99 "
   "billed annually, with a minimum of five cards and billing per card rather than per user. "
   "Enterprise is custom. Verified 27 August 2026 on blinq.me/pricing."),

  ("Do HiHello and Blinq have a minimum number of users?",
   "Yes, both effectively require five. HiHello sells its Business plan for “5-100 users”. Blinq's "
   "Business plan requires a “minimum of five” cards. A team of two, three or four cannot buy the "
   "team tier on either product at the per-user price shown, and would be on single-user plans "
   "without shared branding, team analytics or admin control."),

  ("Does Blinq bill per user or per card?",
   "Per card. Blinq's pricing page states that Business is “Billed per card, per month” and that "
   "“Admins and team members who don't have a card assigned aren't billed”. HiHello bills per user. "
   "The difference matters if some people in your organisation administer the account or need "
   "access but do not need a card of their own — on Blinq those people are free."),

  ("Do HiHello and Blinq both include an email signature and virtual backgrounds free?",
   "Yes. Both vendors list a personal email signature and virtual backgrounds on their free plans, "
   "along with Apple and Google wallet passes and sharing by QR code, widget, email and SMS. These "
   "are table stakes in this category rather than points of difference between the two products — "
   "or between them and CompanyCard, which is why this page does not present them as a reason to "
   "choose any of the three."),

  ("How does CompanyCard compare to HiHello and Blinq?",
   "CompanyCard is more expensive than both and has a smaller free plan: 1 card carrying a small "
   "CompanyCard credit against HiHello's 4 and Blinq's 2, Pro at $7.99 a month against HiHello's "
   "$6, and Business at $12 per user against HiHello's $5 and Blinq's $6.99. The one axis where "
   "CompanyCard differs is the seat floor — it has no seat minimum on team plans, so a two-person "
   "or three-person business can buy team features that HiHello and Blinq both gate behind five "
   "seats. CompanyCard's team plans are not self-serve, though; the pricing page directs you to "
   "talk to us."),
 ],

 "related": [
   ("HiHello alternative", "hihello-alternative.html"),
   ("Blinq alternative", "blinq-alternative.html"),
   ("Best digital business cards", "best-digital-business-card.html"),
   ("What a digital business card costs", "digital-business-card-cost.html"),
   ("Free plans compared", "free-digital-business-card-comparison.html"),
 ],
}

PAGES = [VS]
