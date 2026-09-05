# -*- coding: utf-8 -*-
"""Batch 18: popl-vs-uniqode.html — the second vendor-vs-vendor page.

WHY THIS PAGE (demand-verified, and a total coverage gap).

Google Search Console read 2026-09-05 (28d: 3,750 impressions / 2 clicks / 388
query rows / avg position 60.5; 3-month: 4,980 impressions / 6 clicks / 472
rows). Filtering the 3-month query table on " vs " returns exactly four rows —
the whole of the vendor-vs-vendor demand this property can currently see:

    hihello vs blinq ..................... 71   (batch 15 owns this)
    blinq vs hihello ...................... 3   (same page)
    popl vs beaconstac .................... 2
    beaconstac vs popl .................... 2

"popl vs beaconstac" is therefore the ONLY head-to-head pair on the property
that we do not already answer, and it appears in BOTH orderings, which is the
signature of a real two-sided comparison intent rather than a stray long tail.

The impression count is small, but the coverage gap is total and measurable:
a repo-wide grep before writing this page found the string "beaconstac" on
**zero of 62 HTML files, zero times in llms.txt, and zero times in seo/**.
We publish a uniqode-alternative.html and it never once mentions the name the
searcher is actually typing. Batch 15 established that a vs page materialises
impressions from nothing (hihello-vs-blinq went 0 -> 71 in three months and is
now the 9th largest row on the property), so the pair with visible demand and
no page is the right next unit of work.

THE LOAD-BEARING FACT, AND WHY IT IS SAFE.
Beaconstac renamed itself Uniqode. Verified first-party 2026-09-05:

    curl -sIL https://www.beaconstac.com/
    HTTP/2 301
    location: https://www.uniqode.com
    HTTP/2 200

That is a redirect on the vendor's own domain, not a claim in an article, and
it is the single most useful thing this page can tell somebody searching for
"Popl vs Beaconstac". It also ages well: a 301 is a durable statement.

VENDOR FACTS — BOTH RE-FETCHED 2026-09-05, the day this page was written.
Read off each vendor's own live pages today; nothing is restated from the
2026-09-01 or 2026-09-03 runs without re-checking. Quoted strings were grepped
out of the fetched HTML, per the standing rule that quotations go stale while
their numbers stay right.

  * popl.co — title "Popl | Your AI GTM Platform for Event Lead Capture",
    h1 "Your AI GTM platform for in-person events". CONFIRMS the string
    batch 18 (2026-09-01) verified; still exact.
  * popl.co/pages/pricing — title "Popl Pricing | Event Lead Capture, Badge
    Scanner & Enrichment Plans", h1 "Simple pricing for teams of all sizes",
    section head "Turn events into your best growth channel". NO rates and NO
    tiers are published; the call to action is "Request Pricing". The word
    "Free" occurs ZERO times in the page text (checked by regex, not by eye).
    The single plan card lists: "Plans include unlimited events & conferences",
    "AI-native Universal Badge Scanner", "Verified contact & company data
    enrichment", "Event campaigns & qualifying questions", "Self-serve CRM &
    calendar integrations", "SOC 2 Type 2 enterprise-grade security",
    "Dedicated CSM onboarding & support", "Digital business cards for your
    team". Integrations named: Salesforce, HubSpot, Marketo.
  * uniqode.com/pricing — "No, we do not offer monthly plans, and it is not
    possible to change your subscription from an annual to a monthly plan."
    "You can create your first digital business card with Uniqode for free.
    For additional seats, upgrade to the Team plan at $6 per user per month."
    "Digital business cards created on the Free plan will remain free forever
    with essential features, while cards made on Team and Business+ plans will
    stay accessible as long as your account subscription is active."
    Business+ is custom-priced ("advanced security, control, and flexibility").
    "We offer a 30-day money-back guarantee". "All our plans are billed in USD".

OUR OWN figures are held to pricing.html as re-read today: Free $0 forever
(1 digital business card, QR & link sharing, profile/links/socials, Add to
Apple & Google Wallet), Pro $7.99/mo, Business $12/user/month whose call to
action is "Talk to us about teams", Enterprise custom. The annual toggle is
labelled "Save up to 25%" (Pro $5.99/mo, Business $10/user/mo per llms.txt).
pricing.html also states "Billing is not live yet — paid plans are currently a
preview, so nothing is charged", and that sentence is reproduced on this page
rather than hidden.

WHAT THIS PAGE CONCEDES, DELIBERATELY.
Uniqode's Team plan at $6 per user per month is HALF our $12 Business rate.
The page says so in the table and again in prose, before the closing section.
Our three checkable edges against THIS pair are narrow and are the only ones
claimed: (1) we bill monthly and Uniqode states plainly that it does not;
(2) we publish self-serve rates and Popl publishes none; (3) our free plan is
one working card rather than a trial. Wallet-on-free is NOT claimed as an edge
(dead since batch 15) and email signatures / virtual backgrounds are not
mentioned as differentiators at all. No seat-minimum claim is made against
Uniqode either: its pricing page states no minimum, so asserting one would be
inventing a fact, and the 2026-09-01 generator note that "its Team plan starts
at two seats" was NOT re-verifiable today and is not carried over.

ANTI-CANNIBALISATION. popl-alternative.html and uniqode-alternative.html argue
our case against one vendor each; this page answers "which of those two", and
CompanyCard does not appear until after the question has been answered — the
batch 15 template, which is the only vs page on the site that has earned
impressions.
"""
from build_pages import prose, table, block, faq_html, cta  # noqa: F401

VERIFIED = "5 September 2026"

REL = [
  ("Popl alternative", "popl-alternative.html"),
  ("Uniqode alternative", "uniqode-alternative.html"),
  ("HiHello vs Blinq", "hihello-vs-blinq.html"),
  ("Best digital business cards compared", "best-digital-business-card.html"),
  ("How much a digital business card costs", "digital-business-card-cost.html"),
]

PAGE = {
 "slug": "popl-vs-uniqode.html",
 "crumb": "Popl vs Uniqode",
 "title": "Popl vs Uniqode (formerly Beaconstac): Which One in 2026? | CompanyCard",
 "meta": ("Popl vs Uniqode, the company that used to be Beaconstac. What each one "
          "publishes, what each is actually built for, and which fits a small business. "
          "Both vendors re-checked " + VERIFIED + "."),
 "og": ("Beaconstac is now Uniqode. A head-to-head with Popl on published pricing, "
        "billing terms and what each product is really for."),
 "h1": "Popl vs Uniqode (formerly Beaconstac)",
 "lead": ("If you searched for Beaconstac, you are looking for Uniqode — the company "
          "renamed, and beaconstac.com now redirects to uniqode.com. Here is how it compares "
          "with Popl on what each vendor actually publishes, and which job each one is built "
          "for. Both were re-read on " + VERIFIED + "."),
 "cta_btn": "Create your free card",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "If neither of those is the shape you wanted",
 "cta_p": ("A single card, priced in public, billed by the month, free to start. "
           "That is the gap CompanyCard fills between these two."),
 "related": REL,
 "faqs": [
   ("Is Beaconstac the same company as Uniqode?",
    "Yes. Beaconstac rebranded to Uniqode, and the old domain now points at the new one: as of "
    + VERIFIED + ", https://www.beaconstac.com/ returns an HTTP 301 redirect to "
    "https://www.uniqode.com. So a search for \"Popl vs Beaconstac\" is a search for Popl vs "
    "Uniqode, and any Beaconstac review or price you find from before the rename describes the "
    "same product under its old name."),
   ("Popl or Uniqode — which should I pick?",
    "It depends on the job, and for most small businesses neither is aimed at you. Pick Popl if "
    "your work is capturing leads at trade shows and conferences: as of " + VERIFIED + " its own "
    "pricing page sells unlimited events, an AI-native universal badge scanner, contact and "
    "company data enrichment, and native Salesforce, HubSpot and Marketo sync. Pick Uniqode if "
    "you want a digital business card you can price and buy yourself today, especially alongside "
    "a QR-code programme, and you are willing to commit for a year."),
   ("How much does Popl cost?",
    "Popl does not say. As of " + VERIFIED + " its pricing page publishes no rates and no tiers "
    "— the page is headed \"Simple pricing for teams of all sizes\" and the only call to "
    "action is \"Request Pricing\". The word \"free\" does not appear on it at all, so there is "
    "no free plan to compare against. You will find out the number on a call."),
   ("How much does Uniqode cost, and does it bill monthly?",
    "As of " + VERIFIED + " Uniqode's first digital business card is free, additional seats are "
    "on the Team plan at $6 per user per month, and Business+ is custom-priced. Billing is annual "
    "only: Uniqode states \"No, we do not offer monthly plans, and it is not possible to change "
    "your subscription from an annual to a monthly plan.\" It offers a 30-day money-back "
    "guarantee. Check uniqode.com/pricing before deciding — terms change."),
   ("What happens to a Uniqode card if I stop paying?",
    "Uniqode draws the line at the free plan. Its pricing page states that \"Digital business "
    "cards created on the Free plan will remain free forever with essential features, while cards "
    "made on Team and Business+ plans will stay accessible as long as your account subscription "
    "is active\" (read " + VERIFIED + "). In other words the free card survives; a paid card is "
    "tied to an active subscription."),
   ("Where does CompanyCard fit, and where does it lose?",
    "It loses on the headline team price: Uniqode's Team plan is $6 per user per month against "
    "our $12 Business, so for a team that is happy to pay annually Uniqode is cheaper and we will "
    "not pretend otherwise. What we have against this pair is narrow and checkable — we "
    "bill monthly where Uniqode states it does not offer monthly plans, we publish our rates "
    "where Popl publishes none, and our free plan is one working card rather than a trial. Note "
    "our free card carries a small CompanyCard credit, and our pricing page states that billing "
    "is not live yet — paid plans are currently a preview, so nothing is charged."),
 ],
}

PAGE["sections"] = [
  prose("First, the name: Beaconstac is Uniqode", [
    "A lot of the searches for this comparison still use the old name. Beaconstac rebranded to "
    "Uniqode, and the rename is visible on the vendor's own infrastructure rather than only in "
    "press coverage: as of " + VERIFIED + ", <code>https://www.beaconstac.com/</code> answers with "
    "an HTTP 301 and sends you to <code>https://www.uniqode.com</code>.",
    "That matters for anything you read while researching. Reviews, prices and feature lists "
    "published under the Beaconstac name describe the same product line, but they predate the "
    "rename — and in this category prices move, so treat the numbers in them as historical "
    "and check <a href=\"https://www.uniqode.com/pricing\" target=\"_blank\" rel=\"nofollow noopener\">"
    "uniqode.com/pricing</a> for what is true today.",
  ]),
  prose("The short answer", [
    "These two are not really competing for the same buyer any more, which makes the choice "
    "easier than it looks.",
    "<b>Choose Popl if your job is events.</b> As of " + VERIFIED + " popl.co leads with \"Your AI "
    "GTM platform for in-person events\" and its pricing page sells unlimited events and "
    "conferences, an AI-native universal badge scanner, verified contact and company data "
    "enrichment, event campaigns with qualifying questions, and self-serve CRM and calendar "
    "integrations with native Salesforce, HubSpot and Marketo sync. Digital business cards are on "
    "the list — \"Digital business cards for your team\" — but they are one line item "
    "in an event-marketing platform. You will book a call to find out the price.",
    "<b>Choose Uniqode if you want to buy a card yourself, today.</b> It publishes its rates, the "
    "first card is free, and additional seats are $6 per user per month. The catch is commercial "
    "rather than functional: paid subscriptions are annual only.",
    "<b>If you are one person or a business of three, look again at both.</b> Popl will not quote "
    "you without a meeting, and Uniqode will not bill you monthly. Those are the two friction "
    "points that send people to a third option.",
  ]),
  block("Side by side", table(
    ["What to check", "Popl", "Uniqode (formerly Beaconstac)", "CompanyCard"],
    [
      ["<b>Published price</b>",
       "None. The pricing page's only call to action is “Request Pricing”",
       "Yes — Team <b>$6 per user per month</b>; Business+ custom",
       "Yes — Free, Pro $7.99/mo, Business $12/user/mo"],
      ["<b>Free plan</b>",
       "None published — the word “free” does not appear on the pricing page",
       "First card free, and free-plan cards “remain free forever with essential features”",
       "1 card, QR &amp; link sharing, Apple and Google Wallet — carries a small CompanyCard credit"],
      ["<b>Monthly billing</b>",
       "Not published",
       "<b>No</b> — “we do not offer monthly plans”; annual only",
       "Monthly or annual"],
      ["<b>How you start</b>",
       "Request pricing, then a call",
       "Sign up and buy online",
       "Sign up free; the Business plan is “Talk to us about teams”"],
      ["<b>What it is built around</b>",
       "Event lead capture and badge scanning at conferences",
       "QR codes at scale, with digital business cards alongside",
       "One card for a small business or self-employed person"],
      ["<b>If you stop paying</b>",
       "Not published",
       "Free-plan cards stay; paid cards last “as long as your account subscription is active”",
       "Free plan is the floor — there is nothing to stop paying for"],
      ["<b>Money back</b>",
       "Not published",
       "30-day money-back guarantee",
       "Free plan — you can try it without paying at all"],
    ],
    note=("Read from popl.co, popl.co/pages/pricing and uniqode.com/pricing on " + VERIFIED
          + "; the beaconstac.com redirect was checked the same day. Vendor terms change — "
            "check both before deciding. CompanyCard figures are our own published rates on our "
            "<a href=\"pricing.html\">pricing page</a>, where annual billing is labelled "
            "“Save up to 25%”."),
  ), tint=True),
  prose("Where each one genuinely wins", [
    "<b>Popl wins on events, and it is not close.</b> If you staff a booth, the thing that decides "
    "your quarter is how fast a scanned badge becomes an enriched, deduplicated record in "
    "Salesforce. That is the product Popl now builds. A digital business card tool is not a "
    "substitute for it, and we would rather say so than win the click.",
    "<b>Uniqode wins on price and on breadth.</b> $6 per user per month is half our Business rate, "
    "and if you already run QR codes for packaging, signage or campaigns, having the cards live in "
    "the same account is a real operational advantage rather than a feature-list one. The 30-day "
    "money-back guarantee takes some of the sting out of the annual commitment.",
    "<b>The thing neither publishes is a monthly, single-seat price.</b> Popl publishes no price at "
    "all; Uniqode publishes one but will not bill it monthly. If you want to spend $8 this month "
    "and decide again next month, that is the shape neither of them sells.",
  ]),
  prose("Where CompanyCard fits — and where it does not", [
    "We are the third option in that last paragraph, and it is worth being precise about how "
    "small the advantage is.",
    "<b>Where we lose.</b> On the headline team number Uniqode is cheaper: $6 per user per month "
    "against our $12 Business plan. If you have five people, are happy to pay for a year, and want "
    "the lowest published rate, Uniqode is the better buy and this page is not going to argue "
    "otherwise. Our free plan is also one card, and it carries a small CompanyCard credit — "
    "removing that is part of Pro. Our Business plan is not self-serve either; the pricing page "
    "says “Talk to us about teams”. And our own pricing page states plainly that "
    "billing is not live yet — paid plans are currently a preview, so nothing is charged.",
    "<b>Where we hold up.</b> Three things, all checkable on the three pricing pages linked above. "
    "We bill monthly, where Uniqode states it does not offer monthly plans. We publish our rates, "
    "where Popl publishes none and quotes over a meeting. And our free tier is a complete working "
    "card — QR code, sharing link, profile and socials, Apple and Google Wallet pass — "
    "rather than a trial that expires.",
    "If you are a sole trader or a business of two or three who wants one good card this "
    "afternoon, without a sales call and without committing a year of budget, that is the case. "
    "If you are staffing trade-show booths, go and book the Popl demo.",
  ]),
]

PAGES = [PAGE]
