# -*- coding: utf-8 -*-
"""Batch 23: hihello-pricing.html — a pricing explainer for a competitor.

WHY THIS PAGE (GSC, 28 days to 2026-09-20, read 2026-09-23).
HiHello is one of the two largest competitor clusters on the property, and
three of its rows are pure price intent with no page of ours aimed at them:
"hihello pricing" 6 @ 67.3, "hi hello pricing" 3 @ 54.3 (plus "hello-hello
pricing" 2 on 09-19). `grep -il "hihello pricing" *.html` returned nothing.
The three existing HiHello pages (alternative, vs Blinq, vs Popl) are
comparisons; none answers "what will HiHello bill me" on its own terms.

WHAT MAKES IT CITABLE: the billing toggle. hihello.com/pricing renders with
"Billed yearly — up to 25% off" switched ON, so the first figures a reader
(or a scraper) sees are yearly rates. The monthly rates live in the page's
own JS: `var MONTHLY = { 'Professional': { amt: '$8', note: 'billed
monthly' }, 'Business': { amt: '$6', note: 'billed monthly' } }`. And the
"up to 25%" is exactly 25% on Professional ($8 -> $6) but 16.7% on Business
($6 -> $5) — "Savings vary by plan", as HiHello's own FAQ says. Its FAQ also
says Business "start[s] at five users at $5 per user per month" without the
word yearly. Every bill on this page is computed from those printed rates.

VERIFIED 2026-09-23 by curl of https://www.hihello.com/pricing (200, 119,744
bytes): Personal free forever, 1 user, 4 cards, 5 card & badge scans/mo,
Apple & Google wallet; Professional 1 user, $6/mo, "$72 billed yearly",
16 cards, 20 scans/mo, "Unlimited scans add-on available" (no add-on price
printed); Business "5-100 users", $5 per user/month, "$60 per user/year",
unlimited cards and scans; Enterprise 101+ users, Custom. FAQ: "Base pricing
covers your first five seats"; Professional "is an individual plan";
"cancel at any time ... access continues through the end of your current
billing period"; SOC 2 Type II. CompanyCard figures from our pricing.html
the same day: Pro data-monthly 7.99 / data-annual 5.99; Business 12 / 10;
billing not live yet (paid plans are a preview).
"""
from build_pages import prose, table, block, checklist  # noqa: F401

VERIFIED = "23 September 2026"

REL = [
  ("HiHello alternative", "hihello-alternative.html"),
  ("HiHello vs Blinq", "hihello-vs-blinq.html"),
  ("HiHello vs Popl", "hihello-vs-popl.html"),
  ("How much a digital business card costs", "digital-business-card-cost.html"),
  ("Free plans compared", "free-digital-business-card-comparison.html"),
]

PAGE = {
 "slug": "hihello-pricing.html",
 "crumb": "HiHello Pricing",
 "title": "HiHello Pricing (2026): Monthly vs Yearly Rates and What You Actually Pay | CompanyCard",
 "meta": ("HiHello pricing read off hihello.com on " + VERIFIED + ": Personal free, Professional "
          "$8 a month or $72 a year, Business $6 or $5 per user with a five-user floor. Annual "
          "bills worked out for 1 to 100 users."),
 "og": ("HiHello's pricing page opens on its yearly rates. Here are the monthly ones too, and "
        "the yearly bill at every team size."),
 "h1": "HiHello pricing, monthly and yearly",
 "lead": ("HiHello publishes every price it charges, which is more than most of this category "
          "does. The catch is that its pricing page loads with the yearly switch already on. "
          "This page lists both sets of rates as printed on hihello.com on " + VERIFIED
          + ", then turns them into the bill you would actually receive."),
 "cta_btn": "Create your free card",
 "cta2": ("See CompanyCard pricing", "pricing.html"),
 "cta_h": "Comparing bills? Ours is on the page too",
 "cta_p": ("CompanyCard has a free card, a $7.99 Pro plan and a team plan you can buy for one "
           "seat. Start free and decide later."),
 "related": REL,
 "faqs": [
   ("How much does HiHello cost per month?",
    "As printed on hihello.com on " + VERIFIED + ": Personal is free. Professional is $8 a "
    "month if you pay month to month, or $6 a month if you pay $72 for the year. Business is $6 "
    "per user a month billed monthly, or $5 per user a month as $60 per user for the year, and "
    "it starts at five users. Enterprise, for 101 users or more, has no published price."),
   ("Why does HiHello's pricing page show $6 and $5?",
    "Because the page loads with its \"Billed yearly\" switch turned on. Those are the yearly "
    "rates, spread across twelve months. Switch it off and Professional reads $8 and Business "
    "reads $6 per user, both marked \"billed monthly\". Both sets are genuine prices; quote the "
    "one that matches how you intend to pay."),
   ("How much do you save with HiHello's annual billing?",
    "HiHello says \"up to 25%\" and \"Savings vary by plan\". Worked out from its own rates, "
    "Professional saves exactly 25% ($96 a year monthly against $72 yearly), while Business "
    "saves about 17% ($72 per user a year monthly against $60 yearly). The 25% applies to the "
    "individual plan only."),
   ("What is the cheapest way to get HiHello for a team?",
    "For five to a hundred people, Business billed yearly: $60 per user a year, so $300 for "
    "five users, $720 for twelve and $3,000 for fifty. Below five users you still pay for five, "
    "because HiHello's FAQ says base pricing covers the first five seats. A team of two or three "
    "can instead buy separate Professional plans, but HiHello describes Professional as an "
    "individual plan, so there is no shared admin dashboard."),
   ("Is HiHello free?",
    "The Personal plan is, with no end date: one user, four digital business cards, Apple and "
    "Google wallet passes, a personal email signature, virtual backgrounds and five card and "
    "badge scans a month. It is one of the larger free plans in the category. The limit most "
    "people meet first is the scan allowance, not the card count."),
   ("Can I cancel HiHello at any time?",
    "HiHello's FAQ says you can cancel from account settings at any time and keep access until "
    "the end of the period you have paid for. On a yearly plan that means the $72 or the per-user "
    "$60 is already spent; the saving from annual billing is a commitment, not a discount you "
    "can walk away from mid-year."),
   ("Is CompanyCard cheaper than HiHello?",
    "Mostly not. CompanyCard Pro is $7.99 a month or $5.99 billed yearly — a cent under HiHello "
    "Professional on each term, but for one card where HiHello gives sixteen. Our Business plan "
    "is $12 per user monthly or $10 yearly, twice HiHello's rate, and our free plan is one card "
    "with a small CompanyCard credit. What we offer that HiHello does not is a team plan below "
    "five seats, and on price that only beats HiHello's five-seat floor for one or two users: "
    "two CompanyCard seats are $240 a year against HiHello's $300. Our billing is not live yet; "
    "paid plans are currently a preview."),
 ],
}

PAGE["sections"] = [
  block("HiHello's four plans, both billing terms", table(
    ["Plan", "Who it is for", "Billed monthly", "Billed yearly", "What the price buys"],
    [
      ["<b>Personal</b>", "1 user", "$0", "$0",
       "4 cards, 5 card &amp; badge scans a month, Apple &amp; Google wallet"],
      ["<b>Professional</b>", "1 user", "$8 a month ($96 a year)", "$72 a year ($6 a month)",
       "16 cards, 20 scans a month, contact enrichment, card analytics"],
      ["<b>Business</b>", "5 to 100 users", "$6 per user a month ($72 a year)",
       "$60 per user a year ($5 a month)",
       "Unlimited cards and scans, event lead capture, team analytics, SSO"],
      ["<b>Enterprise</b>", "101+ users", "Not published", "Not published",
       "Custom quote; SAML/SCIM, dedicated account manager"],
    ],
    note=("Read from hihello.com/pricing on " + VERIFIED + ". The monthly column comes from the "
          "same page with the \"Billed yearly\" switch turned off; HiHello's page script labels "
          "those two figures \"billed monthly\". Annual totals are our arithmetic.")),
    tint=True),
  prose("The switch that changes every number", [
    "Open HiHello's pricing page and the first price under Professional is $6. Under it, in "
    "smaller type, is \"$72 billed yearly\". That $6 is not a monthly plan; it is a yearly plan "
    "divided by twelve. The month-to-month price is $8, and you only see it after you turn the "
    "\"Billed yearly — up to 25% off\" switch off. Business behaves the same way: $5 with the "
    "switch on, $6 with it off.",
    "None of this is hidden, and plenty of vendors default to annual. It matters because the $6 "
    "and $5 figures travel. Review sites, AI answers and comparison tables pick up whatever the "
    "page shows first, and a monthly $6 Professional plan does not exist. If a price for "
    "HiHello comes without the words \"yearly\" or \"monthly\" next to it, assume it is the "
    "yearly one.",
    "The \"up to 25%\" is also worth reading closely. It is exactly right for Professional: $8 "
    "down to $6 is a quarter off. On Business the step is $6 to $5, which is a sixth — roughly "
    "17%. HiHello's own FAQ is careful about this and says savings vary by plan; the banner "
    "simply quotes the best case.",
  ]),
  block("What HiHello would bill you in a year", table(
    ["Your size", "Plan you would be on", "Paying monthly", "Paying yearly"],
    [
      ["Just you, free", "Personal", "$0", "$0"],
      ["Just you, paid", "Professional", "$96", "$72"],
      ["2 people", "2 × Professional (no shared admin)", "$192", "$144"],
      ["3 people", "3 × Professional, or Business at its 5-seat floor",
       "$288, or $360 for Business", "$216, or $300 for Business"],
      ["5 people", "Business", "$360", "$300"],
      ["12 people", "Business", "$864", "$720"],
      ["50 people", "Business", "$3,600", "$3,000"],
      ["100 people", "Business (its ceiling)", "$7,200", "$6,000"],
      ["101 or more", "Enterprise", "Quote", "Quote"],
    ],
    note=("Computed from the rates in the first table. Taxes excluded. The five-seat floor for "
          "Business comes from HiHello's FAQ: \"Base pricing covers your first five seats\".")),
    tint=False),
  prose("Where the extra cost usually shows up", [
    "<b>Scans, before cards.</b> Four free cards is generous, and most individuals never use "
    "sixteen. The allowance that runs out is scanning: five card and badge scans a month on "
    "Personal, twenty on Professional. The pricing page offers an \"Unlimited scans add-on\" for "
    "Professional but, on " + VERIFIED + ", does not print what the add-on costs. If you collect "
    "a lot of paper cards at events, ask for that price before you choose a plan, or price "
    "Business, where scans are unlimited.",
    "<b>The gap between one and five.</b> Professional cannot be shared — HiHello says so in "
    "its FAQ — and Business bills from five seats. A three-person firm therefore chooses between "
    "three unconnected individual plans and paying for two empty seats. At yearly rates the "
    "difference is $216 against $300, so the empty seats cost $84 a year for the admin "
    "dashboard, templates and shared analytics.",
    "<b>Committing to the year.</b> The saving on annual billing is real, but HiHello's FAQ says "
    "cancelling keeps your access to the end of the paid period, so a yearly plan is paid for in "
    "full whether you use all of it or not. For a new team, one or two months on monthly "
    "billing is a cheap way to find out whether everyone actually uses their card.",
  ]),
  block("How CompanyCard's prices sit next to HiHello's", table(
    ["", "HiHello", "CompanyCard"],
    [
      ["Free plan", "4 cards", "1 card with a small CompanyCard credit"],
      ["One person, paid", "$8 monthly / $6 yearly, 16 cards",
       "$7.99 monthly / $5.99 yearly, 1 card"],
      ["Per user on the team plan", "$6 monthly / $5 yearly", "$12 monthly / $10 yearly"],
      ["Smallest team you can buy", "5 users", "1 user"],
      ["2 users on the team plan, per year", "$300 (billed as 5)", "$240"],
      ["3 users on the team plan, per year", "$300 (billed as 5)", "$360"],
      ["5 users on the team plan, per year", "$300", "$600"],
    ],
    note=("CompanyCard figures from our pricing page, " + VERIFIED + ". Both yearly. Our "
          "billing is not live yet: paid plans are a preview and nothing is charged today.")),
    tint=True),
  prose("Reading that table honestly", [
    "HiHello is the better-priced product for almost everyone. Its free plan holds four cards "
    "to our one. Its Professional plan costs one cent more than our Pro on either billing term "
    "and gives sixteen cards to our one. Its Business rate is half of ours.",
    "The narrow exception is a team smaller than five that wants shared branding and an admin "
    "view. Two people on CompanyCard Business cost $240 a year against HiHello's $300 floor. "
    "At three the order flips: $360 against $300, so HiHello is cheaper even though you are "
    "paying it for five people, and on a monthly bill it is $36 against $30. For a team of "
    "three or four, what we offer is not a lower bill; it is being billed for the people you "
    "have.",
    "If you are one person choosing on price alone, take HiHello's free plan. It is a good one.",
  ]),
  block("Before you pay HiHello, check these", checklist([
    ("Which switch position you are reading.",
     "$6 and $5 are yearly. $8 and $6 are monthly."),
    ("How many scans you need a month.",
     "5 free, 20 on Professional; the unlimited add-on has no printed price."),
    ("Your real headcount.",
     "Business bills from five seats and stops at a hundred."),
    ("Whether you will stay a year.",
     "Annual billing is paid through to the end of the term."),
    ("Whether you need an individual or a team plan.",
     "Professional is one person and cannot be shared."),
  ]), tint=False),
]

PAGES = [PAGE]
