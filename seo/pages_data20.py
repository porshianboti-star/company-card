# -*- coding: utf-8 -*-
"""Batch 22: hihello-vs-popl.html — the fourth vendor-vs-vendor page.

WHY THIS PAGE (the two largest competitor clusters on the property, paired).

Google Search Console, read 2026-09-13 from the in-app browser, 28 days,
394 query rows. Every row naming a competitor, grouped by vendor:

  HiHello   hihello vs blinq 52 + hihello alternative 40 (pos 28.4, the best
            non-brand position on the property) + hihello pricing 5 +
            hihello alternatives 3                              = 100
  Popl      popl alternative 47 (pos 40.2) + popl alternatives 12 + popl
            competitors 11 + best popl alternatives 2026 1       =  71
  Blinq     blinq alternative 8 + is blinq free 3 + six one-impression
            pricing rows                                        =  17
  Uniqode / Wave / V1CE                                          <= 7 each

HiHello and Popl are the two vendors searchers already reach this site for,
and no page put them side by side. "hihello vs popl" reads 0 impressions by
construction — GSC only records a pair once a page ranks for it; "hihello vs
blinq" read 0 before batch 15 and is 52 today, which is the control.

First-party evidence, checked the same day: BOTH vendors publish a page for
the pair — popl.co/pages/popl-vs-hihello (HTTP 200, title "Popl vs HiHello:
Event Lead Capture Platform Comparison", h1 "Teams choose Popl over HiHello
for better team functionality") and hihello.com/vs/popl (HTTP 200, title and
h1 "HiHello vs Popl"). A repo-wide grep for "hihello-vs-popl" and
"popl-vs-hihello" returned zero hits in *.html and llms.txt.

VENDOR FACTS — BOTH RE-FETCHED 2026-09-13, the day this page was written.

  * hihello.com/pricing — title "Pricing for Digital Business Card
    Subscription - HiHello", h1 "Pricing plans for everyone". The page has a
    "Billed yearly up to 25% off" switch that is ON by default. Read with the
    switch on (curl) AND off (clicked in the in-app browser):
      Personal      "1 user Free Forever" — "4 free digital business cards",
                    "Personal email signature", "Virtual backgrounds", "5 card
                    & badge scans /mo", "Add to Apple & Google wallet", "QR,
                    widgets, email, & SMS sharing".
      Professional  switch on:  "$6 per month $72 billed yearly"
                    switch off: "$8 per month billed monthly"
                    "1 user", "16 digital business cards", "20 card & badge
                    scans /mo", "Unlimited scans add-on available", "Contact
                    enrichment", "Card analytics", "Full card customization".
      Business      switch on:  "$5 per user/month $60 per user/year"
                    switch off: "$6 per user/month billed monthly"
                    "5-100 users", "Unlimited digital business cards",
                    "Unlimited card & badge scans", "Event lead capture",
                    "SSO & directory sync".
      Enterprise    "101+ users", "Custom".
    !! The $6 and $5 figures every earlier page on this site quotes are the
    YEARLY-billed rates. The monthly-billed rates are $8 and $6. The page's
    own JavaScript carries them (MONTHLY = {Professional: '$8', Business:
    '$6'}, note 'billed monthly') and the click confirmed the render. Same
    shape as the Calendly finding of 2026-09-08: the number is on the vendor's
    page, the billing term under it was not read. Corrected sitewide in the
    same commit as this page (seo/fix_hihello_billing_2026_09_13.py).
  * popl.co — title "Popl | Your AI GTM Platform for Event Lead Capture", h1
    "Your AI GTM platform for in-person events". Homepage FAQ: "Can I try Popl
    for free? Yes, Popl offers free trials and personalized demos. Free trials
    are designed for individuals to explore and experience the benefits of
    Popl Teams before committing to setting up a team." and "How does pricing
    work for Popl? Popl offers flexible pricing for both teams and
    individuals. Contact us for a custom quote".
  * popl.co/pages/pricing — title "Popl Pricing | Event Lead Capture, Badge
    Scanner & Enrichment Plans", h1 "Simple pricing for teams of all sizes".
    NO rates and NO tiers; "Request Pricing" x2, "Book a Demo". Plan card:
    "Plans include unlimited events & conferences", "AI-native Universal
    Badge Scanner", "Verified contact & company data enrichment", "Event
    campaigns & qualifying questions", "Self-serve CRM & calendar
    integrations", "SOC 2 Type 2 enterprise-grade security", "Dedicated CSM
    onboarding & support", "Digital business cards for your team". Pricing
    FAQ, new to this site's record: "Does Popl charge per seat or per license?
    No. Popl's pricing is all-inclusive — you won't be charged extra per user,
    per seat, or per license. Your plan covers your whole team, no matter how
    much it grows over time." "Popl for Individuals" block for "solo
    entrepreneurs and professionals" links https://poplco.app.link/pricing,
    which answered HTTP 307 to https://popl.co/pages/download-popl today. The
    word "free" appears once, in the footer link "Get the free mobile app".
    The dollar figures on the page are case-study outcomes, not prices.

OUR OWN figures from pricing.html as re-read today: Free $0 forever (1
digital business card, QR & link sharing, profile/links/socials, Add to Apple
& Google Wallet); Pro $7.99/mo, $5.99/mo billed yearly ($71.88 a year in the
page's own offer data); Business $12/user/mo, $10 billed yearly, "Talk to us
about teams"; "Billing is not live yet — paid plans are currently a preview,
so nothing is charged".

WHAT THIS PAGE CONCEDES, DELIBERATELY. HiHello's free plan is four cards to
our one, and ours carries a credit. HiHello Business is $6 per user billed
monthly ($5 yearly) against our $12 ($10 yearly). HiHello Professional and
our Pro are within a cent of each other on either billing term ($8 vs $7.99
monthly; $6 vs $5.99 yearly) and HiHello's includes sixteen cards to our one.
Popl is the better product for event lead capture, full stop. The checkable
edges claimed are only: a published price where Popl has none; no seat
minimum where HiHello Business is sold for 5-100 users (worth $24 vs $30 for
two people on monthly billing, gone at five). NOT claimed: a scan-cap edge —
HiHello's free plan caps its scanner at 5 a month, but our free plan has no
scanner at all (lead capture is a Pro feature, as hihello-alternative.html
already states), so five is more than zero. Wallet, signatures and
backgrounds are NOT claimed either — HiHello's free plan lists all three.

REWRITTEN 2026-09-19 — WHY. Google Search Console, read 2026-09-19 (indexing
report dated 9/14/26), listed this page under "Crawled - currently not
indexed" — the first page on the property ever to be crawled and declined.
An 8-word-shingle comparison against blinq-vs-popl.html measured Jaccard
0.214, and 1,044 of the page's 2,075 words sat in runs also present on that
page: the Popl facts, the three Popl FAQ answers and the CompanyCard column
had been reused verbatim. That is the same 0.13-0.26 band the 21 profession
pages were in before Google's decline forced the 2026-09-14 rewrite
(aa95ee2). Every vendor figure below was RE-FETCHED 2026-09-19 (hihello.com
/pricing: same plans and rates, MONTHLY JS object still Professional '$8'
and Business '$6' 'billed monthly'; popl.co and popl.co/pages/pricing: still
no rate, "Request Pricing" / "Book a Demo", the per-seat FAQ unchanged, the
"Popl for Individuals" link still HTTP 307 to popl.co/pages/download-popl;
two sentences new to our record on the pricing page: "Talk to our sales
team and we'll provide you with a quote" and "To learn more about pricing,
book a demo with us for a custom quote"). Our pricing.html re-read the same
day: unchanged. The page is now organised by buyer (one person free / one
person paid / two to four / five and up / an events team) rather than by
the vendor-then-vendor template, the table is a bill-by-headcount table
computed from the published rates, and the FAQ asks different questions.
Target after the rewrite: shingle Jaccard against every other vs page under
0.03, measured in the same session.
"""
from build_pages import prose, table, block, faq_html, cta, checklist  # noqa: F401

VERIFIED = "19 September 2026"

REL = [
  ("HiHello alternative", "hihello-alternative.html"),
  ("Popl alternative", "popl-alternative.html"),
  ("HiHello vs Blinq", "hihello-vs-blinq.html"),
  ("Blinq vs Popl", "blinq-vs-popl.html"),
  ("How much a digital business card costs", "digital-business-card-cost.html"),
]

PAGE = {
 "slug": "hihello-vs-popl.html",
 "crumb": "HiHello vs Popl",
 "title": "HiHello vs Popl: Which Digital Business Card in 2026? | CompanyCard",
 "meta": ("HiHello vs Popl by headcount: what one person, a team of three, a team of five and an "
          "events team would actually pay, from the rates each vendor publishes (HiHello all of "
          "them, Popl none). Re-read " + VERIFIED + "."),
 "og": ("What you would pay HiHello or Popl at every team size, worked out from their own "
        "pricing pages — one publishes every rate, the other quotes by phone."),
 "h1": "HiHello vs Popl",
 "lead": ("Instead of a feature grid, this page works out what each vendor would bill you at "
          "your headcount, from the numbers on their own pricing pages as read on " + VERIFIED
          + ". HiHello prints every rate. Popl prints none, so its column says what you get "
          "before the quote."),
 "cta_btn": "Create your free card",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "A price you can read, from one user up",
 "cta_p": ("CompanyCard sells one card, priced on the page, free to start, with team plans "
           "that begin at a single seat. That is the whole pitch against this pair."),
 "related": REL,
 "faqs": [
   ("Is Popl cheaper than HiHello?",
    "Nobody outside Popl can tell you, because Popl does not publish a rate. As of " + VERIFIED
    + " popl.co/pages/pricing shows plan contents and two buttons, \"Request Pricing\" and "
    "\"Book a Demo\", and its FAQ says \"Talk to our sales team and we'll provide you with a "
    "quote\". HiHello prints every figure: Professional $8 a month billed monthly, Business $6 "
    "per user a month billed monthly, $6 and $5 respectively if you pay for the year. The only "
    "way to compare the two bills is to ask Popl for yours."),
   ("Which one suits a team of three?",
    "HiHello's team plan is labelled for \"5-100 users\", so as of " + VERIFIED + " three people "
    "are either on three separate Professional plans at $24 a month billed monthly, with no "
    "shared admin or template lock, or buying Business at its five-user floor for $30. Popl "
    "gives you a quote. CompanyCard Business has no seat minimum, so three people are $36 a "
    "month billed monthly or $30 billed yearly, with the admin dashboard and brand lock "
    "included; our pricing page adds that billing is not live yet and paid plans are a "
    "preview. Three users is the one headcount where our published team rate is competitive; "
    "at five HiHello is cheaper."),
   ("Why does HiHello show $6 in one place and $8 in another?",
    "Because its pricing page opens with the \"Billed yearly up to 25% off\" switch already "
    "on. As of " + VERIFIED + " the first Professional price you see is $6 a month, which is "
    "the yearly plan, $72 charged once. Turn the switch off and the same plan reads \"$8 per "
    "month billed monthly\". Business does the same thing: $5 per user a month with the switch "
    "on, $6 with it off. Both numbers are correct; they describe different billing terms."),
   ("Can one person buy Popl?",
    "Not from the website, as of " + VERIFIED + ". The pricing page has a \"Popl for "
    "Individuals\" panel for \"solo entrepreneurs and professionals\", but its link sends you "
    "to the page for downloading the Popl app rather than to a plan or a price, and the "
    "homepage FAQ describes the free trial as a way for individuals to \"experience the "
    "benefits of Popl Teams before committing to setting up a team\". An individual price for "
    "Popl is not published anywhere we could find."),
   ("How many cards come with each free option?",
    "HiHello: four, on a plan it labels \"Free Forever\", with Apple and Google Wallet, an "
    "email signature and virtual backgrounds included and card and badge scanning capped at "
    "five a month. Popl: none as a plan; what it offers is a free trial and a demo, and the "
    "only \"free\" on its pricing page is the footer's \"Get the free mobile app\". CompanyCard: "
    "one card with QR code, link and wallet pass, no scanner, and a small CompanyCard credit on "
    "it that the Pro plan removes. All three read on " + VERIFIED + "."),
   ("What would an events team actually get from Popl that HiHello lacks?",
    "As of " + VERIFIED + " Popl's plan card lists unlimited events and conferences, an "
    "AI-native universal badge scanner, verified contact and company data enrichment, event "
    "campaigns with qualifying questions, self-serve CRM and calendar integrations, SOC 2 Type 2 "
    "security and a dedicated customer success manager, with digital business cards as one line "
    "on that list. HiHello's Business plan lists event lead capture, unlimited scans and "
    "unlimited contact enrichment too, but the product is built around the card; Popl's is "
    "built around the booth. If badge scanning at conferences is the job, that is Popl's home "
    "ground, and CompanyCard does not compete there at all."),
 ],
}

PAGE["sections"] = [
  prose("Start from your headcount, not from the feature list", [
    "HiHello and Popl no longer sell to the same person. HiHello's pricing page still opens with "
    "a plan for \"1 user\" that costs nothing; Popl's opens with \"Simple pricing for teams of all "
    "sizes\" and no number under it. So the useful question is not which product is better but "
    "which of them will quote you at all, and for how much, at the size you are.",
    "<b>One person who wants a free card.</b> HiHello, without much argument. Its Personal plan "
    "is labelled \"Free Forever\" and includes four cards, wallet passes for Apple and Google, an "
    "email signature and virtual backgrounds. Popl offers a trial, not a plan. CompanyCard's free "
    "tier is one card with a small credit on it — honest, but fewer cards.",
    "<b>One person who will pay.</b> HiHello Professional: $8 a month billed monthly, $72 a "
    "year if you pay up front, sixteen cards, contact enrichment and analytics. CompanyCard Pro "
    "is $7.99 a month or $5.99 billed yearly for one card with unlimited links, custom branding, "
    "lead capture and the credit removed. Popl does not sell to an individual from its website "
    "at all — see the FAQ below.",
    "<b>Two, three or four people who want shared branding.</b> This is the awkward size. "
    "HiHello Business is sold for \"5-100 users\". Popl quotes. CompanyCard Business starts at "
    "one seat, $12 a month each, and it is the only one of the three that prints a team price a "
    "business of three can pay without a call or a fifth person.",
    "<b>Five people or more.</b> HiHello Business at $6 per user billed monthly, or $5 yearly, "
    "is half our $12 and it is self-serve. From five up, HiHello is the better-priced card "
    "platform of the three and we say so.",
    "<b>A team whose job is trade shows.</b> Popl, and the price is whatever the call produces. "
    "The plan card sells unlimited events, a universal badge scanner, data enrichment and CRM "
    "sync; the card is a line item. Neither HiHello nor CompanyCard is built around a booth.",
  ]),
  block("What each vendor would bill you, by team size", table(
    ["Headcount", "HiHello", "Popl", "CompanyCard"],
    [
      ["<b>1 person, free</b>",
       "$0 — Personal, 4 cards, 5 scans a month",
       "No free plan; a free trial and a demo",
       "$0 — 1 card, wallet pass, small CompanyCard credit"],
      ["<b>1 person, paid</b>",
       "<b>$8/mo</b> billed monthly · $72/yr billed yearly (Professional, 16 cards)",
       "Not sold online to individuals; the link goes to the app download",
       "<b>$7.99/mo</b> · $5.99/mo billed yearly ($71.88/yr) (Pro, 1 card)"],
      ["<b>3 people</b>",
       "3 × Professional = <b>$24/mo</b> with no shared admin, or Business at its 5-user floor, $30/mo",
       "Quote",
       "3 × Business = <b>$36/mo</b> · $30/mo billed yearly, admin dashboard and brand lock included"],
      ["<b>5 people</b>",
       "Business <b>$30/mo</b> billed monthly · $300/yr billed yearly",
       "Quote — “you won't be charged extra per user, per seat, or per license”",
       "<b>$60/mo</b> · $50/mo billed yearly"],
      ["<b>25 people</b>",
       "Business <b>$150/mo</b> · $1,500/yr",
       "Quote, same all-inclusive structure",
       "<b>$300/mo</b> · $250/mo billed yearly"],
      ["<b>Events team at a conference</b>",
       "Business includes event lead capture and unlimited badge scans",
       "The product: unlimited events, universal badge scanner, enrichment, CRM sync, SOC 2 Type 2, a dedicated CSM",
       "Not built for this; lead capture on Pro is a card feature, not a badge scanner"],
    ],
    note=("Arithmetic from hihello.com/pricing (switch on and off), popl.co/pages/pricing, popl.co "
          "and our own <a href=\"pricing.html\">pricing page</a>, all read on " + VERIFIED + ". "
          "HiHello's five-user figure assumes Business is bought at the bottom of its "
          "“5-100 users” range. CompanyCard's paid plans are a preview: the pricing page says "
          "billing is not live yet and nothing is charged. Rates move — reread both vendors "
          "before you buy."),
  ), tint=True),
  prose("The switch on HiHello's pricing page", [
    "Most comparisons of HiHello, ours included until September 2026, quoted $6 and $5 as its "
    "monthly prices. They are its yearly prices. The page loads with a control labelled \"Billed "
    "yearly up to 25% off\" already on, and the plan cards under it read \"$6 per month, $72 "
    "billed yearly\" and \"$5 per user/month, $60 per user/year\".",
    "Click the switch off and the cards re-render: Professional becomes \"$8 per month billed "
    "monthly\" and Business \"$6 per user/month billed monthly\". The page's own script carries "
    "both sets of figures, and we clicked it in a browser on " + VERIFIED + " to confirm the "
    "render matches. If you intend to pay month to month, the numbers that matter are $8 and $6.",
    "This is not a criticism of HiHello — a yearly default is common — but it is why some pages "
    "will tell you HiHello Business is $5 and others $6, and why our own earlier pages had to be "
    "corrected.",
  ]),
  prose("What Popl publishes instead of a price", [
    "Popl's pricing page is a real page with real content; it just contains no rate. As of "
    + VERIFIED + " it is headed \"Simple pricing for teams of all sizes\" and every button on "
    "it is \"Request Pricing\" or \"Book a Demo\". The dollar figures on the page belong to "
    "customer case studies — pipeline generated, revenue closed — not to plans.",
    "What it does tell you is the shape of the deal. Its FAQ answers \"Does Popl charge per "
    "seat or per license?\" with \"No. Popl's pricing is all-inclusive — you won't be charged "
    "extra per user, per seat, or per license. Your plan covers your whole team, no matter how "
    "much it grows over time.\" It also says \"Talk to our sales team and we'll provide you "
    "with a quote\" and \"To learn more about pricing, book a demo with us for a custom quote\". "
    "So the bill is a single negotiated number rather than a per-head one, which is genuinely "
    "different from HiHello and from us.",
    "The homepage frames the whole company as \"Your AI GTM platform for in-person events\" "
    "and answers \"Can I try Popl for free?\" with \"Yes, Popl offers free trials and "
    "personalized demos\". The trial is described as a way for individuals to try Popl Teams "
    "before setting one up — a path into a team purchase, not a free card.",
  ]),
  block("What we would tell a friend", checklist([
    ("You want a free card today:",
     "take HiHello's four free cards, or ours if one card with a wallet pass is enough and you "
     "do not mind the credit."),
    ("You are two to four people and want one brand on every card:",
     "CompanyCard is the only one of the three with a printed price at that size; HiHello needs "
     "five, Popl needs a call."),
    ("You are five or more:",
     "HiHello Business, $6 a user billed monthly, is half our rate and self-serve. Buy it."),
    ("You run a booth:",
     "book the Popl demo. Ask for the all-inclusive number and how it changes as the team grows."),
    ("You want to know the price before you sign up:",
     "HiHello or CompanyCard. Popl will not tell you on the page."),
  ]), tint=False),
]

PAGES = [PAGE]
