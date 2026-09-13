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
"""
from build_pages import prose, table, block, faq_html, cta  # noqa: F401

VERIFIED = "13 September 2026"

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
 "meta": ("HiHello vs Popl on what each vendor publishes: HiHello lists a free plan and every "
          "price (with a yearly toggle that hides the monthly rate); Popl lists no price at all. "
          "Which fits one person, a small team or an events team. Both re-checked " + VERIFIED + "."),
 "og": ("HiHello publishes every price; Popl publishes none. A head-to-head on free plans, "
        "billing terms and what each product is really built for."),
 "h1": "HiHello vs Popl",
 "lead": ("The two digital business card vendors people compare most often on this site, put side "
          "by side on what each one publishes and what each is built for — not on marketing. One "
          "lists a free plan and every price; the other lists none. Both were re-read on "
          + VERIFIED + "."),
 "cta_btn": "Create your free card",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "If you want a published price and no seat minimum",
 "cta_p": ("One card, priced in public, free to start, no five-user floor. "
           "That is the narrow gap CompanyCard fills between these two."),
 "related": REL,
 "faqs": [
   ("HiHello or Popl — which should I pick?",
    "For one person or a small business, HiHello: as of " + VERIFIED + " it publishes a free plan "
    "with four cards, a Professional plan at $8 a month billed monthly or $6 a month billed yearly, "
    "and a Business plan at $6 per user a month billed monthly or $5 billed yearly, all purchasable "
    "online. For a team whose job is capturing leads at trade shows and conferences, Popl: its "
    "pricing page sells unlimited events, an AI-native universal badge scanner, contact and company "
    "data enrichment and CRM sync, and says its plan is not charged per user, per seat or per "
    "license — and you get the price on a call, because it does not publish one."),
   ("How much does HiHello cost?",
    "As of " + VERIFIED + " HiHello publishes four plans. Personal is free forever with 4 cards, 1 "
    "user and 5 card and badge scans a month. Professional is $8 a month billed monthly, or $72 a "
    "year — $6 a month — billed yearly, for 1 user, 16 cards and 20 scans a month. Business is $6 "
    "per user a month billed monthly, or $60 per user a year — $5 a month — billed yearly, with "
    "unlimited cards and scans, and is sold for 5 to 100 users. Enterprise is custom for 101+ "
    "users. The pricing page's \"Billed yearly\" switch is on by default, so the first numbers you "
    "see are the yearly rates. Check hihello.com/pricing before deciding."),
   ("How much does Popl cost?",
    "Popl does not say. As of " + VERIFIED + " its pricing page publishes no rates and no tiers; "
    "it is headed \"Simple pricing for teams of all sizes\" and the calls to action are \"Request "
    "Pricing\" and \"Book a Demo\". The homepage FAQ says \"Popl offers flexible pricing for both "
    "teams and individuals. Contact us for a custom quote\". The pricing FAQ does say how the price "
    "is structured: \"you won't be charged extra per user, per seat, or per license\". The \"Popl "
    "for Individuals\" link on the pricing page redirects to a page for downloading the Popl app, "
    "so the individual price is not on the web either."),
   ("Does Popl have a free plan?",
    "Not a free plan. As of " + VERIFIED + " Popl's homepage FAQ says \"Popl offers free trials "
    "and personalized demos\" and that the trials are \"designed for individuals to explore and "
    "experience the benefits of Popl Teams before committing to setting up a team\". The pricing "
    "page lists no free tier; the only use of the word \"free\" on it is the footer link \"Get the "
    "free mobile app\". HiHello's Personal plan, by contrast, is \"Free Forever\" with four cards."),
   ("Is HiHello's free plan really free?",
    "Yes, with one published limit that matters. As of " + VERIFIED + " HiHello's Personal plan "
    "is \"Free Forever\" and includes 4 digital business cards, a personal email signature, virtual "
    "backgrounds, Apple and Google Wallet passes and sharing by QR code, widget, email and SMS — "
    "but it caps you at \"5 card & badge scans /mo\". Handing your card out is unlimited; scanning "
    "other people's paper cards into your phone is metered. Professional raises that to 20 a "
    "month, and only Business, sold for 5 to 100 users, makes it unlimited."),
   ("Where does CompanyCard fit, and where does it lose?",
    "It loses to HiHello on the free plan (four cards against our one, which carries a small "
    "CompanyCard credit), on the team rate ($6 per user billed monthly against our $12), and on "
    "cards per paid plan — HiHello Professional and our Pro are within a cent of each other on "
    "either billing term, $8 against $7.99 monthly and $6 against $5.99 yearly, and HiHello's "
    "includes sixteen cards to our one. It loses to Popl on event lead capture outright. What it "
    "has against this pair is narrow and checkable: we publish a price where Popl publishes none; "
    "we have no seat minimum where HiHello Business is sold for 5 to 100 users, which only matters "
    "for a team of two to four. HiHello's free plan caps its card scanner at five a month, but "
    "that is not an edge for us: our free plan has no scanner at all — lead capture is a Pro "
    "feature. Our pricing page also states that billing is not live yet — paid plans are "
    "currently a preview, so nothing is charged."),
 ],
}

PAGE["sections"] = [
  prose("The short answer", [
    "These are the two vendors people arrive at this site comparing, and they have ended up "
    "selling to different buyers. That settles most of the choice before you look at a feature.",
    "<b>Choose HiHello if you are one person or a small business.</b> As of " + VERIFIED + " "
    "hihello.com/pricing lists a Personal plan that is \"Free Forever\" with four cards, "
    "Professional at $8 a month billed monthly or $6 a month billed yearly, and Business at $6 per "
    "user a month billed monthly or $5 billed yearly, every one of them purchasable online. It is "
    "the vendor in this pair that still sells a card to an individual with a price on the page.",
    "<b>Choose Popl if your job is events.</b> popl.co leads with \"Your AI GTM platform for "
    "in-person events\", and its pricing page sells unlimited events and conferences, an AI-native "
    "universal badge scanner, verified contact and company data enrichment, event campaigns with "
    "qualifying questions and CRM sync. Digital business cards are on the list — \"Digital business "
    "cards for your team\" — as one line item in an event-marketing platform. You will book a call "
    "to find out the price.",
    "<b>Read HiHello's price with the toggle in mind.</b> Its pricing page opens with a \"Billed "
    "yearly up to 25% off\" switch turned on, so the numbers you see first — $6 and $5 — are the "
    "yearly rates. Switch it off and Professional reads \"$8 per month billed monthly\" and Business "
    "\"$6 per user/month billed monthly\". Most comparisons, including earlier versions of ours, "
    "quote the yearly figure as if it were the monthly price.",
  ]),
  block("Side by side", table(
    ["What to check", "HiHello", "Popl", "CompanyCard"],
    [
      ["<b>Published price</b>",
       "Yes — Personal free, Professional <b>$8/mo</b> monthly or <b>$6/mo</b> yearly, Business <b>$6/user/mo</b> monthly or <b>$5</b> yearly, Enterprise custom",
       "None. Calls to action are “Request Pricing” and “Book a Demo”",
       "Yes — Free, Pro $7.99/mo or $5.99 yearly, Business $12/user/mo or $10 yearly"],
      ["<b>Free plan</b>",
       "Yes — “Free Forever”, 4 cards, email signature, virtual backgrounds, Apple and Google Wallet — capped at “5 card &amp; badge scans /mo”",
       "No free plan listed. Homepage FAQ: “Popl offers free trials and personalized demos”",
       "1 card, QR &amp; link sharing, Apple and Google Wallet, no card scanner (lead capture is a Pro feature) — carries a small CompanyCard credit"],
      ["<b>Cards on the individual paid plan</b>",
       "Professional: 16 cards, 20 scans a month",
       "Not published",
       "Pro builds on the one free card: unlimited links and files, custom branding, lead capture and analytics"],
      ["<b>Smallest team bill</b>",
       "Business is sold for “5-100 users” — five users, so <b>$30/mo</b> billed monthly or $25/mo billed yearly",
       "Not published",
       "No seat minimum: one user is $12/mo, two are $24/mo"],
      ["<b>How team billing works</b>",
       "Per user, monthly or yearly",
       "Not per user: “you won't be charged extra per user, per seat, or per license”; the rate itself is not published",
       "Per user, monthly or yearly; the Business plan is “Talk to us about teams”"],
      ["<b>What it is built around</b>",
       "A card for individuals, with lead capture and directory sync for teams",
       "Event lead capture and badge scanning at conferences",
       "One card for a small business or self-employed person"],
      ["<b>How you start</b>",
       "Sign up free; upgrade online",
       "Request pricing, then a call; individuals are sent to the app download",
       "Sign up free; teams talk to us"],
    ],
    note=("Read from hihello.com/pricing (with the “Billed yearly” switch on and off), popl.co and "
          "popl.co/pages/pricing on " + VERIFIED + "; the “Popl for Individuals” link was followed "
          "the same day and redirected to popl.co/pages/download-popl. Vendor terms change — check "
          "both before deciding. CompanyCard figures are our own published rates on our "
          "<a href=\"pricing.html\">pricing page</a>, where yearly billing is labelled "
          "“Save up to 25%”."),
  ), tint=True),
  prose("Where each one genuinely wins", [
    "<b>HiHello wins on the free plan and on price transparency.</b> Four free cards, forever, with "
    "Apple and Google Wallet, a personal email signature and virtual backgrounds all on the $0 tier, "
    "and every paid price on the page. If you want to know what you will pay before you sign up, "
    "HiHello tells you and Popl does not.",
    "<b>HiHello's Professional is a lot of card for the money.</b> Sixteen cards, contact "
    "enrichment, card analytics and full customisation for $8 a month, or $6 if you pay for the "
    "year. If you run more than one role, side business or language and want a separate card for "
    "each, no plan on this page comes close.",
    "<b>Popl wins on events, and it is not close.</b> If you staff a booth, what decides your "
    "quarter is how fast a scanned badge becomes an enriched, deduplicated record in your CRM. That "
    "is the product Popl now builds, with a dedicated CSM and SOC 2 Type 2 on the plan card. And its "
    "pricing FAQ makes one structural promise HiHello's per-user model cannot: the plan is not "
    "charged per seat. A digital business card is not a substitute for any of that, and we would "
    "rather say so than win the click.",
    "<b>The thing neither publishes is a team price for two people.</b> Popl publishes no price at "
    "all. HiHello publishes one, but sells Business for 5 to 100 users, so a two-person business "
    "is on two Professional plans without shared branding or admin control. That is the gap a "
    "third option has to fit into, and it is a small one.",
  ]),
  prose("Where CompanyCard fits — and where it does not", [
    "We are the third option in that last paragraph, and it is worth being precise about how "
    "small the advantage is.",
    "<b>Where we lose.</b> HiHello's free plan is four cards; ours is one, and it carries a small "
    "CompanyCard credit that Pro removes. HiHello Business is $6 per user billed monthly against "
    "our $12, and at five people or more it is simply cheaper. HiHello Professional and our Pro are "
    "within a cent of each other on either billing term — $8 against $7.99 monthly, $6 against "
    "$5.99 yearly — and HiHello's includes sixteen cards, contact enrichment and card analytics "
    "where ours includes one card. Popl is the better product for trade shows, full stop. Our "
    "Business plan is not self-serve either — the pricing page says “Talk to us about teams” — and "
    "it states plainly that billing is not live yet: paid plans are currently a preview, so nothing "
    "is charged.",
    "<b>Where we hold up.</b> Two things, both checkable on the pricing pages linked above. We "
    "publish a price, where Popl publishes none. We have no seat minimum, where HiHello Business "
    "starts at five users — which matters for a business of two to four that wants team features "
    "($24 for two against a $30 five-user floor on monthly billing) and stops mattering at five. "
    "HiHello's five-scans-a-month cap on its free plan is not a point for us: our free plan has no "
    "card scanner at all, because lead capture is a Pro feature.",
    "If you are a sole trader or a business of two who wants one good card this afternoon, with the "
    "price on the page and no five-user floor, that is the case. If you want four free cards or "
    "sixteen paid ones, take HiHello. If you are staffing booths, go and book the Popl demo.",
  ]),
]

PAGES = [PAGE]
