# -*- coding: utf-8 -*-
"""Batch 21: blinq-vs-popl.html — the third vendor-vs-vendor page.

WHY THIS PAGE (the pair both vendors publish a page for, and we do not).

The scheduled task's backlog has been exhausted since 2026-08-20; pages are now
picked from evidence. This run the Google Search Console read could not be
taken (the Chrome extension reported no connected browser for the whole
session), so the pick rests on two first-party signals read 2026-09-11 rather
than on the query table:

  * blinq.me/pricing's own footer links a "Blinq vs Popl" page, and popl.co
    publishes /pages/popl-vs-blinq. When BOTH vendors in a pair spend a page
    on the comparison, the pair has demand — vendors do not build vs pages for
    searches nobody makes.
  * Every page in the result set for the query is either vendor-owned (Popl's,
    Blinq's blog) or a listicle/affiliate site; the G2 compare page is the only
    third-party source. That is the same category structure the 2026-07-26
    research recorded, and the same gap batch 15 (hihello-vs-blinq, 0 -> 71
    impressions in three months from a standing start) filled.

Before writing, a repo-wide grep for "blinq-vs-popl" and "popl-vs-blinq"
returned zero hits in *.html and llms.txt: blinq-alternative.html names Popl
in its meta description and popl-alternative.html never names Blinq at all.
The pair was uncovered.

VENDOR FACTS — BOTH RE-FETCHED 2026-09-11, the day this page was written.
Every string below was read out of the fetched HTML today (curl with a browser
user agent; Popl's individual-pricing deep link followed with -IL). Nothing is
restated from the 2026-09-01 or 2026-09-05 runs without re-checking, per the
standing rule that quoted strings go stale while their numbers stay right.

  * blinq.me/pricing — title "Digital Business Card and Lead Capture Pricing |
    Blinq", h1 "Free to start and built to scale". Monthly/Annual toggle.
      Free      "$0 Free forever" — "Two free digital business cards",
                "Unlimited sharing", "Unlimited contact creation", "QR code,
                widget, email & SMS sharing", "Add to Google or Apple Wallet",
                "Personal email signature", "Virtual backgrounds".
      Premium   "$9.99 / month Billed monthly"; "$7.33 / month Billed
                annually". "Create up to five cards", "Universal contact
                scanner", "AI notetaker", "AI contact enrichment", "Branded QR
                code", "Custom card colours & design", "Export contacts".
      Business  "$6.99 / month Billed monthly, per user"; "$4.99 / month
                Billed annually, per user". The billing FAQ on the same page
                says: "Blinq Business is billed per card, per month, for the
                team cards in your account. When you sign up you choose how
                many cards to start with (minimum of five) and you're charged
                for those cards straight away." and "Admins and team members
                who don't have a card assigned aren't billed, so you only pay
                for people who have a card." Both wordings are on the page
                today; the page reproduces both rather than picking one.
      Enterprise "Custom", "Book a demo".
    Footer of that page lists "Blinq vs Popl", "Blinq vs HiHello", "Blinq vs
    Uniqode", "Blinq vs Dot".
  * popl.co — title "Popl | Your AI GTM Platform for Event Lead Capture", h1
    "Your AI GTM platform for in-person events" (still exact vs 09-01/09-05).
    Homepage FAQ: "Can I try Popl for free? Yes, Popl offers free trials and
    personalized demos. Free trials are designed for individuals to explore
    and experience the benefits of Popl Teams before committing to setting up
    a team." and "How does pricing work for Popl? Popl offers flexible pricing
    for both teams and individuals. Contact us for a custom quote".
  * popl.co/pages/pricing — title "Popl Pricing | Event Lead Capture, Badge
    Scanner & Enrichment Plans", h1 "Simple pricing for teams of all sizes".
    NO rates and NO tiers; calls to action "Request Pricing" (x2) and "Book a
    Demo". Single plan card: "Plans include unlimited events & conferences",
    "AI-native Universal Badge Scanner", "Verified contact & company data
    enrichment", "Event campaigns & qualifying questions", "Self-serve CRM &
    calendar integrations", "SOC 2 Type 2 enterprise-grade security",
    "Dedicated CSM onboarding & support", "Digital business cards for your
    team". The only dollar figures on the page are case-study outcomes
    ("$6M in Qualified Pipeline Generated" etc.), not prices.
    NEW SINCE 09-05: a block "Only need Popl for yourself? (not a team) We
    offer a simple digital business card app designed perfectly for solo
    entrepreneurs and professionals. Popl for Individuals" whose link is
    https://poplco.app.link/pricing — which answers HTTP 307 to
    https://popl.co/pages/download-popl, a page titled "Download the Popl App
    | Event Lead Capture + CRM Sync". So the individual price is not on the
    web either; the path to it is an app install.
    The word "free" appears on the pricing page exactly once, in the footer
    link "Get the free mobile app". (batch 18's popl-vs-uniqode page said it
    appeared zero times; corrected in the same commit as this page.)

OUR OWN figures are held to pricing.html as re-read today: Free $0 forever
(1 digital business card, QR & link sharing, profile/links/socials, Add to
Apple & Google Wallet), Pro $7.99/mo, Business $12/user/month whose call to
action is "Talk to us about teams", Enterprise custom. Annual toggle "Save up
to 25%" (Pro $5.99/mo, Business $10/user/mo per llms.txt). pricing.html also
states "Billing is not live yet — paid plans are currently a preview, so
nothing is charged", reproduced on this page rather than hidden.

WHAT THIS PAGE CONCEDES, DELIBERATELY.
Blinq's free plan is two cards with no vendor credit; ours is one card with a
CompanyCard credit. Blinq's per-seat Business rate ($6.99, $4.99 annual) is
far below our $12, and Blinq Premium bundles a contact scanner, AI notetaker
and enrichment that our Pro does not list. Popl is the better product for
trade-show lead capture, full stop. Our checkable edges against THIS pair are
narrow and are the only ones claimed: (1) we publish a price where Popl
publishes none; (2) we have no seat minimum where Blinq Business starts at
five cards — and the page does the arithmetic showing that edge is gone by
three people ($36 vs Blinq's $34.95 floor); (3) our individual paid tier is
$2 cheaper than Blinq Premium ($7.99 vs $9.99), with the feature gap stated.
Wallet-on-free, email signatures and virtual backgrounds are NOT claimed as
edges — Blinq's free plan lists all three, and the page says so.

ANTI-CANNIBALISATION. blinq-alternative.html and popl-alternative.html argue
our case against one vendor each; this page answers "which of those two", and
CompanyCard does not appear until after the question has been answered — the
batch 15 template, the only vs shape on the site that has earned impressions.
"""
from build_pages import prose, table, block, faq_html, cta  # noqa: F401

VERIFIED = "11 September 2026"

REL = [
  ("Blinq alternative", "blinq-alternative.html"),
  ("Popl alternative", "popl-alternative.html"),
  ("HiHello vs Blinq", "hihello-vs-blinq.html"),
  ("Popl vs Uniqode", "popl-vs-uniqode.html"),
  ("How much a digital business card costs", "digital-business-card-cost.html"),
]

PAGE = {
 "slug": "blinq-vs-popl.html",
 "crumb": "Blinq vs Popl",
 "title": "Blinq vs Popl: Which Digital Business Card in 2026? | CompanyCard",
 "meta": ("Blinq vs Popl compared on what each vendor actually publishes: Blinq lists every "
          "price, Popl lists none. Which one fits a freelancer, a small team, or an events "
          "team. Both re-checked " + VERIFIED + "."),
 "og": ("Blinq publishes every price; Popl publishes none. A head-to-head on pricing, "
        "billing terms and what each product is really built for."),
 "h1": "Blinq vs Popl",
 "lead": ("Two of the best-known names in digital business cards, compared on what each one "
          "publishes and what each is built for — not on marketing. One lists every price on "
          "its site; the other has stopped listing any. Both were re-read on " + VERIFIED + "."),
 "cta_btn": "Create your free card",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "If you want a published price and no seat minimum",
 "cta_p": ("One card, priced in public, free to start, no five-card floor. "
           "That is the narrow gap CompanyCard fills between these two."),
 "related": REL,
 "faqs": [
   ("Blinq or Popl — which should I pick?",
    "For one person or a small business, Blinq: as of " + VERIFIED + " it publishes a free "
    "plan with two cards, a Premium plan at $9.99 a month, and a Business plan at $6.99 per user "
    "a month, and you can buy any of them online without talking to anyone. For a team whose job "
    "is capturing leads at trade shows and conferences, Popl: its pricing page sells unlimited "
    "events, an AI-native universal badge scanner, contact and company data enrichment, and "
    "Salesforce, HubSpot and Marketo sync — and you get the price on a call, because it does not "
    "publish one."),
   ("How much does Popl cost?",
    "Popl does not say. As of " + VERIFIED + " its pricing page publishes no rates and no "
    "tiers; it is headed \"Simple pricing for teams of all sizes\" and the calls to action are "
    "\"Request Pricing\" and \"Book a Demo\". The homepage FAQ says \"Popl offers flexible pricing "
    "for both teams and individuals. Contact us for a custom quote\". The \"Popl for Individuals\" "
    "link on the pricing page redirects to a page for downloading the Popl app, so the individual "
    "price is not on the web either. If a comparison you are reading quotes a Popl monthly price, "
    "check its date."),
   ("How much does Blinq cost?",
    "As of " + VERIFIED + " Blinq publishes four plans. Free is $0 forever with two digital "
    "business cards. Premium is $9.99 a month billed monthly or $7.33 a month billed annually, "
    "with up to five cards. Business is $6.99 a month billed monthly or $4.99 a month billed "
    "annually, per user, and Blinq's billing FAQ says it is billed per card with a minimum of "
    "five cards to start. Enterprise is custom. Check blinq.me/pricing before deciding — "
    "prices change."),
   ("Does Popl have a free plan?",
    "Not a free plan. As of " + VERIFIED + " Popl's homepage FAQ says \"Popl offers free trials "
    "and personalized demos\" and that the trials are \"designed for individuals to explore and "
    "experience the benefits of Popl Teams before committing to setting up a team\". The pricing "
    "page lists no free tier, and the only use of the word \"free\" on it is the footer link "
    "\"Get the free mobile app\". Blinq's free plan, by contrast, is a permanent plan with two "
    "cards."),
   ("Is Blinq's team plan really $6.99 a month?",
    "Per user, yes — but not from one user. As of " + VERIFIED + " Blinq's Business plan card "
    "says \"$6.99 / month Billed monthly, per user\", and the billing FAQ on the same page says "
    "\"When you sign up you choose how many cards to start with (minimum of five)\". So the "
    "smallest Business bill is five cards, $34.95 a month on monthly billing. The same FAQ says "
    "\"Admins and team members who don't have a card assigned aren't billed\", so you pay for "
    "people who have a card, not for every login."),
   ("Where does CompanyCard fit, and where does it lose?",
    "It loses to Blinq on the free plan (two cards and no vendor credit, against our one card "
    "with a small CompanyCard credit) and on the per-seat team rate ($6.99 against our $12), and "
    "it loses to Popl on event lead capture outright. What it has against this pair is narrow "
    "and checkable: we publish a price where Popl publishes none; we have no seat minimum where "
    "Blinq Business starts at five cards, which only matters for a team of one or two; and our "
    "Pro plan is $7.99 a month against Blinq Premium at $9.99, though Blinq Premium lists a "
    "contact scanner, AI notetaker and contact enrichment that Pro does not. Our pricing page "
    "also states that billing is not live yet — paid plans are currently a preview, so nothing "
    "is charged."),
 ],
}

PAGE["sections"] = [
  prose("The short answer", [
    "These two started in the same place — a card you share by tap or QR — and have ended up "
    "selling to different buyers. That is the first thing to know, because it settles most of the "
    "choice before you look at a single feature.",
    "<b>Choose Blinq if you are one person or a small business.</b> As of " + VERIFIED + " "
    "blinq.me/pricing lists a Free plan (\"$0 Free forever\", two cards), Premium at $9.99 a month, "
    "and Business at $6.99 per user a month, every one of them purchasable online. It is the "
    "vendor in this pair that still behaves like a card product.",
    "<b>Choose Popl if your job is events.</b> popl.co now leads with \"Your AI GTM platform for "
    "in-person events\", and its pricing page sells unlimited events and conferences, an AI-native "
    "universal badge scanner, verified contact and company data enrichment, event campaigns with "
    "qualifying questions, and native Salesforce, HubSpot and Marketo sync. Digital business cards "
    "are on the list — \"Digital business cards for your team\" — as one line item in an "
    "event-marketing platform. You will book a call to find out the price.",
    "<b>If you want the individual Popl card, note where the link goes.</b> The pricing page has a "
    "\"Popl for Individuals\" block for \"solo entrepreneurs and professionals\"; as of "
    + VERIFIED + " its link redirects to a page for downloading the Popl app rather than to a "
    "price. The individual product exists; its price is not published on the web.",
  ]),
  block("Side by side", table(
    ["What to check", "Blinq", "Popl", "CompanyCard"],
    [
      ["<b>Published price</b>",
       "Yes — Free, Premium <b>$9.99/mo</b> ($7.33 annual), Business <b>$6.99/user/mo</b> ($4.99 annual), Enterprise custom",
       "None. Calls to action are “Request Pricing” and “Book a Demo”",
       "Yes — Free, Pro $7.99/mo, Business $12/user/mo"],
      ["<b>Free plan</b>",
       "Yes — “Two free digital business cards”, unlimited sharing, Google and Apple Wallet, personal email signature, virtual backgrounds",
       "No free plan listed. Homepage FAQ: “Popl offers free trials and personalized demos”",
       "1 card, QR &amp; link sharing, Apple and Google Wallet — carries a small CompanyCard credit"],
      ["<b>Cards on the individual paid plan</b>",
       "Premium: “Create up to five cards”",
       "Not published",
       "Pro builds on the one free card: unlimited links and files, custom branding, lead capture and analytics"],
      ["<b>Smallest team bill</b>",
       "Five cards — “minimum of five” — so <b>$34.95/mo</b> on monthly billing",
       "Not published",
       "No seat minimum: one user is $12/mo, two are $24/mo"],
      ["<b>How team billing works</b>",
       "Per card, per month; “Admins and team members who don't have a card assigned aren't billed”",
       "Not published",
       "Per user, monthly or annual; the Business plan is “Talk to us about teams”"],
      ["<b>Monthly billing</b>",
       "Yes — Monthly/Annual toggle on the pricing page",
       "Not published",
       "Monthly or annual"],
      ["<b>What it is built around</b>",
       "A card for individuals, with lead capture and CRM sync for teams",
       "Event lead capture and badge scanning at conferences",
       "One card for a small business or self-employed person"],
      ["<b>How you start</b>",
       "Sign up free; upgrade online",
       "Request pricing, then a call; individuals are sent to the app download",
       "Sign up free; teams talk to us"],
    ],
    note=("Read from blinq.me/pricing, popl.co and popl.co/pages/pricing on " + VERIFIED
          + "; the “Popl for Individuals” link was followed the same day and redirected to "
            "popl.co/pages/download-popl. Vendor terms change — check both before deciding. "
            "CompanyCard figures are our own published rates on our "
            "<a href=\"pricing.html\">pricing page</a>, where annual billing is labelled "
            "“Save up to 25%”."),
  ), tint=True),
  prose("Where each one genuinely wins", [
    "<b>Blinq wins on the free plan and on price transparency.</b> Two free cards, forever, with "
    "Google and Apple Wallet, a personal email signature and virtual backgrounds all on the $0 "
    "tier, and every paid price on the page with a monthly/annual toggle. If you want to know "
    "what you will pay before you sign up, Blinq tells you and Popl does not.",
    "<b>Blinq's Premium is also the richer individual plan.</b> $9.99 a month buys up to five cards, "
    "a universal contact scanner, an AI notetaker and AI contact enrichment. Those are sales tools, "
    "not card tools, and if you meet a lot of people they are worth the two dollars over cheaper "
    "single-card plans, ours included.",
    "<b>Popl wins on events, and it is not close.</b> If you staff a booth, what decides your "
    "quarter is how fast a scanned badge becomes an enriched, deduplicated record in Salesforce. "
    "That is the product Popl now builds, with a dedicated CSM and SOC 2 Type 2 on the plan card. "
    "A digital business card is not a substitute for it, and we would rather say so than win the "
    "click.",
    "<b>The thing neither publishes is a team price for two people.</b> Popl publishes no price at "
    "all. Blinq publishes one, but its billing FAQ starts Business at five cards, so a two-person "
    "business pays for five. That is the gap a third option has to fit into, and it is a small one.",
  ]),
  prose("Where CompanyCard fits — and where it does not", [
    "We are the third option in that last paragraph, and it is worth being precise about how "
    "small the advantage is.",
    "<b>Where we lose.</b> Blinq's free plan is two cards with no vendor credit; ours is one card, "
    "and it carries a small CompanyCard credit that Pro removes. Blinq Business is $6.99 per user "
    "against our $12, and at five people or more it is simply cheaper. Blinq Premium lists a "
    "contact scanner, AI notetaker and enrichment that our Pro does not. Popl is the better product "
    "for trade shows, full stop. Our Business plan is not self-serve either — the pricing page says "
    "“Talk to us about teams” — and it states plainly that billing is not live yet: paid plans are "
    "currently a preview, so nothing is charged.",
    "<b>Where we hold up.</b> Three things, all checkable on the pricing pages linked above. We "
    "publish a price, where Popl publishes none. We have no seat minimum, where Blinq Business "
    "starts at five cards — which matters for a business of one or two that wants the team plan "
    "($12 or $24 against $34.95) and stops mattering at three ($36 against $34.95). And our Pro "
    "plan is $7.99 a month against "
    "Blinq Premium at $9.99, for a plainer card without the sales tooling.",
    "If you are a sole trader or a business of two who wants one good card this afternoon, with "
    "the price on the page and no five-card floor, that is the case. If you want the fuller free "
    "plan, take Blinq. If you are staffing booths, go and book the Popl demo.",
  ]),
]

PAGES = [PAGE]
