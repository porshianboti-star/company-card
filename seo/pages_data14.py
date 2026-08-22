# -*- coding: utf-8 -*-
"""Batch 14: digital-business-card-cost.html — the cross-vendor cost page.

WHY THIS PAGE, AND WHY NOW (demand-verified, not guessed).
Google Search Console, 28d to 2026-08-19, read at the start of this run
(2,300 impressions / 1 click / 257 query rows / avg position 61). A cost-and-
price intent cluster is clearly present in the query rows and NO page on the
site owns it:
    digital business card cost .......... 12
    digital business card comparison ..... 7
    digital business card platform ....... 7
    compare digital business cards ....... 6
    digital business card options ........ 6
    which digital business card is best .. 11
A repo-wide check of all 55 pages found exactly two titles containing
"pricing"/"cost": pricing.html (our own price list) and popl-alternative.html.
Nothing answers the actual question people type, which is what the category
costs, not what we charge.

POSITIONING (anti-cannibalisation). Three live pages are adjacent and NONE is
being rewritten:
  * pricing.html — our own plans only. Says nothing about anyone else.
  * free-digital-business-card-comparison.html — the FREE-tier fine print
    (card counts, scan caps, branding). It deliberately stops at $0.
  * best-digital-business-card.html — the ranked feature/spec matrix.
This page owns the PAID side and, specifically, the gap between the headline
number and what you actually pay: annual-only billing, seat minimums, hardware
sold separately, and pricing that is not published at all. That axis appears
on none of the three.

VENDOR FACTS — ALL RE-FETCHED 2026-08-22, the day this page was written.
Every figure below was read off the vendor's own live pricing page today; the
page carries a "verified 22 August 2026" stamp and nothing is restated from an
earlier run.
  * blinq.me/pricing — Free "$0 / Free forever", "Two free digital business
    cards". Premium "$9.99 / month", "$7.33 / month" billed annually, "up to
    five cards". Business "$6.99 / month" per user billed monthly, "$4.99 /
    month" billed annually, "A minimum payment equal to 5 Team Cards is
    required", "charged per card, per month". Enterprise "Custom".
  * hihello.com/pricing — Personal "$Free Forever", 4 cards, "5 card & badge
    scans/month". Professional "$6 per month" / "$72 billed yearly", 1 user,
    16 cards. Business "$5 per user/month" / "$60 per user/year", "5-100
    users". Enterprise "Custom", "101+ users".
  * uniqode.com/pricing — "We do not offer monthly plans, and it is not
    possible to change your subscription from an annual to a monthly plan."
    "You can create your first digital business card with Uniqode for free.
    For additional seats, upgrade to the Team plan at $6 per user per month."
    Business+ = custom pricing.
  * mobilocard.com/pricing-2 — Pro "$3 /month"; Teams "$4 /month Billed
    Annually"; Business "$5 /month Billed Annually"; the plan table lists Team
    Members as "1 / Unlimited / Unlimited" across those three. Cards sold
    separately, list "$19.99" / "$39.00" / "$59.00" / "$139.00", currently
    discounted.
  * wavecnct.com/pricing — Free "$ 0"; Pro "$ 7 / month"; Teams "$ 5 / user /
    month" with "3 minimum seats"; Enterprise "Contact Sales".
  * v1ce.co/pricing — Smart Card "From £75 one-time"; Client Capture OS
    headline card "£49/mo", with the body of the same page stating "The UK
    list price is £49.99 per month (GBP)" and "£49.99 /mo after the trial.
    Cancel before day 31." plus a "30-day free trial". The page is quoted at
    £49.99 because that is the figure it gives as the list price, and it is
    what llms.txt already states — the £49 card is a rounded headline.
  * popl.co/pages/pricing — no price anywhere on the page; the calls to action
    are "Request Pricing" and "Book a Demo".
OUR OWN figures are held to pricing.html and llms.txt as re-read today: Free
$0 (1 card, carries a small CompanyCard credit), Pro $7.99/mo or $5.99/mo
billed annually, Business $12/user/mo or $10/user/mo billed annually, no seat
minimum, and team plans are not self-serve ("Talk to us about teams").

DELIBERATELY NOT STATED (could not be verified, so absent from the page):
  * any claim that Popl has no free plan — its pricing page publishes no plan
    information at all, so the page says only that the pricing is not
    published and is obtained by request;
  * any market size, average spend, adoption statistic or "most companies pay
    X" figure for the category;
  * any currency conversion of V1CE's GBP prices into USD — the page quotes
    the currency the vendor quotes;
  * any claim about what a vendor's undiscounted hardware price "usually" is,
    beyond the list prices printed on the page today;
  * any claim about discounts, promotions or trial terms we have not read
    today, and no assertion that today's promotional hardware prices will
    still be available later;
  * any per-user reading of Mobilo's Teams/Business prices — Mobilo prints
    them as "/month" and lists team members as "Unlimited", so the page
    reports exactly that rather than inferring a per-seat rate;
  * any claim that our own paid plans are cheaper than the alternatives, which
    for several of them they are not, and the page says so.
"""
from build_pages import prose, block, checklist, table

VERIFIED = "verified 22 August 2026"

COST = {
 "slug": "digital-business-card-cost.html",
 "crumb": "Digital Business Card Cost",
 "title": "How Much Does a Digital Business Card Cost? (2026 Prices) | CompanyCard",
 "meta": ("Most digital business cards have a free plan. Paid personal plans run about $3–$10 a "
          "month and team plans about $4–$7 per user. Every vendor's published price, compared and "
          "dated."),
 "og": ("What a digital business card actually costs in 2026 — every published price from Blinq, "
        "HiHello, Mobilo, Uniqode, Wave, V1CE and CompanyCard, plus the billing terms that change "
        "the real number."),
 "h1": 'How much does a <span class="gradient-text">digital business card</span> cost?',
 "lead": ("For one person, usually nothing: every major digital business card except V1CE and Popl "
          "publishes a free plan, and a free plan is enough for most self-employed people. Paid "
          "personal plans run from $3 to about $10 a month, and team plans from about $4 to $7 per "
          "user a month. The prices below were read off each vendor's own pricing page on "
          "22 August 2026."),
 "cta_btn": "Start free — no credit card",
 "cta2": ("See CompanyCard's plans", "pricing.html"),
 "cta_h": "The cheapest way to find out is to make one",
 "cta_p": "The free plan is a real, working card. No credit card, and nothing expires.",

 "sections": [
  prose("The short answer", [
    "<b>$0 for one card, for most people.</b> Six of the eight products below publish a free plan "
    "that gives one person a working digital business card indefinitely. If you are self-employed "
    "and you need one card with your details on it, the honest answer is that you should not be "
    "paying anything.",

    "<b>About $3–$10 a month if you pay.</b> Paid personal plans start at $3 a month (Mobilo Pro) "
    "and top out around $9.99 a month (Blinq Premium). What you buy at that price is broadly the "
    "same everywhere: custom branding, removal of the vendor's own credit from your card, lead "
    "capture and analytics.",

    "<b>About $4–$7 per user a month for a team</b>, before minimums. Team tiers cluster tightly: "
    "$4 (Mobilo), $5 per user (HiHello, Wave Connect), $6 per user (Uniqode), $4.99–$6.99 per card "
    "(Blinq). CompanyCard's Business plan is $12 per user and is the most expensive team plan on "
    "this page — that is stated here rather than left out.",

    "<b>Hardware is a separate purchase.</b> An NFC card is a physical product with a one-off "
    "price, sold alongside a subscription rather than instead of one. It is not part of the "
    "monthly cost and no digital business card requires it.",
  ]),

  block("Every published price, " + VERIFIED, table(
    ["Product", "Free plan", "Personal paid", "Team paid", "The catch in the billing"],
    [
      ["<b>CompanyCard</b>",
       "Yes — 1 card, carries a small CompanyCard credit",
       "Pro $7.99/mo, or $5.99/mo billed annually",
       "Business $12/user/mo, or $10/user/mo billed annually",
       "No seat minimum, but team plans are not self-serve — the button says “Talk to us about teams”"],
      ["<b>Blinq</b>",
       "Yes — two free digital business cards",
       "Premium $9.99/mo, or $7.33/mo billed annually",
       "Business $6.99 per card/mo, or $4.99 billed annually",
       "“A minimum payment equal to 5 Team Cards is required”, and billing is per card rather than per person"],
      ["<b>HiHello</b>",
       "Yes — 4 cards, capped at 5 card &amp; badge scans a month",
       "Professional $6/mo, or $72 billed yearly",
       "Business $5 per user/mo, or $60 per user/year",
       "The Business plan is sold for 5–100 users; below five people you are on Professional"],
      ["<b>Mobilo</b>",
       "Yes",
       "Pro $3/mo — the cheapest paid plan here",
       "Teams $4/mo and Business $5/mo, both billed annually",
       "Team tiers are annual only; NFC cards are a separate purchase, listed at $19.99–$139"],
      ["<b>Uniqode</b>",
       "Yes — your first digital business card",
       "None — the first paid tier is the team plan",
       "Team $6 per user/mo",
       "“We do not offer monthly plans” — billing is annual only, and you cannot switch to monthly later"],
      ["<b>Wave Connect</b>",
       "Yes",
       "Pro $7/mo",
       "Teams $5 per user/mo",
       "“3 minimum seats” on Teams, so the smallest team bill is 3 × $5"],
      ["<b>V1CE</b>",
       "No — a 30-day free trial instead",
       "Client Capture OS £49.99/mo after the trial",
       "Not published separately",
       "Priced in pounds; the physical Smart Card is a separate purchase “From £75 one-time”"],
      ["<b>Popl</b>",
       "Not published",
       "Not published",
       "Not published",
       "The pricing page publishes no prices — the calls to action are “Request Pricing” and “Book a Demo”"],
    ],
    note=("Every figure read off the vendor's own pricing page on 22 August 2026: "
          "blinq.me/pricing, hihello.com/pricing, uniqode.com/pricing, mobilocard.com/pricing-2, "
          "wavecnct.com/pricing, v1ce.co/pricing, popl.co/pages/pricing. Prices change; if you are "
          "reading this much later, check the source before relying on it. Currencies are quoted as "
          "the vendor quotes them.")), tint=True),

  block("Four things that make the real price differ from the headline price", checklist([
    ("Annual-only billing",
     "Uniqode states plainly that it does not offer monthly plans and that you cannot move an "
     "annual subscription to monthly. Mobilo prints its Teams and Business prices as “billed "
     "annually”. A $6 monthly-looking number that can only be bought a year at a time is a "
     "commitment, not a subscription — and it is the single most common thing people miss when "
     "they compare these products on price alone."),
    ("Seat minimums",
     "Blinq's Business plan requires “a minimum payment equal to 5 Team Cards”. Wave Connect's "
     "Teams plan has “3 minimum seats”. HiHello sells its Business plan for 5–100 users. If you "
     "and one colleague want team features, the per-user price on the page is not the price you "
     "pay; the minimum is."),
    ("Hardware sold separately",
     "Mobilo lists NFC cards at $19.99 to $139 and V1CE lists its Smart Card “From £75 one-time”, "
     "each alongside a subscription rather than instead of one. No digital business card needs a "
     "physical card to work — a QR code and a link do the same job — so treat hardware as an "
     "optional accessory when you are comparing monthly costs."),
    ("Pricing that is not published at all",
     "Popl's pricing page carries no prices; you request them. Uniqode's Business+ and the "
     "Enterprise tiers at Blinq, HiHello and Wave Connect are all “Custom” or “Contact Sales”. "
     "Unpublished pricing is not automatically expensive, but you cannot compare it, and you "
     "cannot buy it in an afternoon."),
   ]), tint=False),

  prose("What we charge, and where we are the wrong answer", [
    "CompanyCard's free plan is $0 forever and includes one digital business card, a QR code and "
    "sharing link, your profile, links and socials, an Apple and Google Wallet pass, and unlimited "
    "edits. No credit card. Pro is $7.99 a month, or $5.99 a month billed annually. Business is "
    "$12 per user a month, or $10 per user a month billed annually, with no seat minimum.",

    "Three honest comparisons, because you can check all of them in the table above. "
    "<b>Our free plan is the smallest here:</b> one card, where HiHello gives four and Blinq gives "
    "two, and our free cards carry a small CompanyCard credit that theirs do not. "
    "<b>Mobilo's Pro plan is less than half our Pro price</b> — $3 against $7.99. "
    "<b>Our Business plan is the most expensive team plan on this page</b>, at roughly twice "
    "HiHello's or Wave Connect's per-user rate.",

    "What is genuinely ours: the Apple and Google Wallet pass is on the $0 plan rather than behind "
    "a paid tier; there is no seat minimum, so two people can be a team; and every price is "
    "published, monthly billing included, so you can compare us without talking to anyone. If what "
    "you need is the cheapest paid personal plan, that is Mobilo. If you need several free cards, "
    "that is HiHello. If you need an NFC card in your pocket, that is Mobilo or V1CE. We would "
    "rather you found that here than found it out later.",
  ]),
 ],

 "faqs": [
  ("How much does a digital business card cost?",
   "For one person, usually nothing — CompanyCard, Blinq, HiHello, Mobilo, Uniqode and Wave "
   "Connect all publish a free plan. Paid personal plans run from $3 a month (Mobilo Pro) to $9.99 "
   "a month (Blinq Premium), and team plans from about $4 to $7 per user a month. Prices verified "
   "22 August 2026 on each vendor's own pricing page."),

  ("Is there a genuinely free digital business card?",
   "Yes. Six of the eight products compared here publish a free plan that does not expire. The "
   "differences are in the limits: CompanyCard's free plan is one card and carries a small "
   "CompanyCard credit, Blinq's is two cards, and HiHello's is four cards but caps you at five "
   "card and badge scans a month. V1CE offers a 30-day trial rather than a free plan, and Popl "
   "publishes no pricing at all."),

  ("What is the cheapest digital business card?",
   "The cheapest paid personal plan on this page is Mobilo Pro at $3 a month, which is less than "
   "half what CompanyCard charges for Pro. For teams, Mobilo's Teams plan at $4 a month billed "
   "annually and HiHello's and Wave Connect's $5 per user a month are the lowest published rates. "
   "The cheapest option overall is a free plan, which is enough for most self-employed people."),

  ("Why are some digital business cards annual-only?",
   "Annual billing locks in revenue for the vendor and is usually presented as a discount. Uniqode "
   "states that it does not offer monthly plans and that an annual subscription cannot be switched "
   "to monthly. Mobilo prices its Teams and Business plans as billed annually. It matters when you "
   "compare: a plan advertised at $6 a month that can only be bought for a year costs $72 up "
   "front, not $6."),

  ("Do I have to buy an NFC card?",
   "No. A digital business card works through a QR code and a link, and the person receiving it "
   "needs no app and no special hardware. NFC cards are an optional physical accessory sold on top "
   "of a subscription — Mobilo lists them at $19.99 to $139 and V1CE lists its Smart Card from £75 "
   "one-time. Neither replaces the subscription."),

  ("How much does a digital business card cost for a small team?",
   "Between about $4 and $12 per person a month, but check the minimum before the rate. Blinq "
   "requires a minimum payment equal to five Team Cards, Wave Connect's Teams plan has a three-seat "
   "minimum, and HiHello sells its Business plan for 5–100 users, so a two-person team may not be "
   "able to buy the per-user price it sees. CompanyCard's Business plan is $12 per user a month "
   "with no seat minimum, which is the most expensive per-user rate here and the only one a "
   "two-person team can buy at face value."),

  ("Is a paid plan worth it if I am self-employed?",
   "Often not. The free plans cover the whole job — one card, a QR code, a sharing link, and "
   "details you can update after you have shared them. Paying gets you custom branding, removal of "
   "the vendor's credit from your card, extra cards, and lead capture with analytics. Those are "
   "worth money if you hand out your card at events and want to follow up; they are not worth "
   "money if you just need people to have your phone number."),
 ],

 "related": [
   ("CompanyCard pricing", "pricing.html"),
   ("Free plans compared", "free-digital-business-card-comparison.html"),
   ("Best digital business cards", "best-digital-business-card.html"),
   ("Digital card vs NFC card", "digital-business-card-vs-nfc-card.html"),
   ("Free digital business card", "free-digital-business-card.html"),
 ],
}

PAGES = [COST]
