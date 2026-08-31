# -*- coding: utf-8 -*-
"""Batch 17: business-card-for-business-owners.html

WHY THIS PAGE (demand-verified from GSC, not guessed).
Google Search Console read 2026-08-31. 28-day window to 08-28: 3.23K
impressions, 1 click, avg position 60.6. The 3-month query table (406 rows)
contains a coherent cluster that NO page on the site targets, and on which we
rank near the bottom of the visible results:

    co owner on business card ............  9 impressions, position 73.3
    business card for owner of company ...  7 impressions, position 89.7
    business cards for multiple employees  1 impression,  position 69.0
    business card for employees ..........  1 impression,  position 64.0
    business card without a business .....  1 impression,  position 76.0
    entrepreneur card ....................  1 impression,  position 60.0
                                           --
                                           20 impressions

For scale: batch 14 was justified by a 12-impression head row and batch 13 by
a 35-impression row. 20 sits between them, and unlike either it is a cluster
we can answer completely with ZERO competitor facts and zero product claims
beyond our own published pricing page — the lowest-risk page shipped this year.

It is also the most on-ICP intent in the whole table. The standing goal names
"small business owners and self-employed professionals". A person typing
"business card for owner of company" IS that person, at the exact moment they
are deciding what goes on the card.

ANTI-CANNIBALISATION. Checked against every adjacent live page:
  * digital-business-card-for-small-business.html — who we are for and why a
    small business wants a digital card. Product page. Does not discuss titles.
  * digital-business-card-for-freelancers.html — the self-employed pitch.
  * digital-business-cards-for-teams.html — the admin/branding story for a
    company rolling cards out to staff.
  * how-to-make-a-digital-business-card.html — the mechanics of building one.
None of them answers "what job title do I put on it", "how do two co-owners
handle this", or "what can I put on a card if the business isn't registered".
Grepped the repo: the strings "co-owner", "sole trader" and "what title"
appear on ZERO of the 61 pages. The gap is total.

INTEGRITY NOTES for anyone re-running or editing this file:
  * No competitor is named anywhere on this page, so nothing here can go stale
    the way a pricing figure does. There is deliberately nothing to re-verify
    about another vendor.
  * No statistics, no survey results, no "most business owners..." claims. Every
    assertion is either a definition, a plainly-stated trade-off, or a fact
    about our own product taken from pricing.html.
  * NO LEGAL ADVICE. The page repeatedly defers to the reader's own companies
    registry and local trading-name rules rather than stating what any
    jurisdiction requires. "Director" is described as a role that is commonly
    filed with a registry, with an instruction to check — not as a rule.
  * Product claims are held to pricing.html as read 2026-08-31: Free = ONE card,
    QR and link sharing, profile/links/socials, Apple and Google Wallet,
    unlimited edits, no credit card, and the card carries a small CompanyCard
    credit. Pro $7.99/mo ($5.99 billed annually). Business $12/user/mo, no seat
    minimum. Billing is not live — paid plans are a preview and nothing is
    charged. The one-card limit is stated in the co-owners section where it is
    an actual disadvantage, not buried.
"""

from build_pages import (block, cards3, checklist, prose, steps_howto, table)

SLUG = "business-card-for-business-owners.html"

# ---------------------------------------------------------------- sections

S_ANSWER = prose("The short answer", [
    "If you own the business, put the name you trade under, <b>one</b> role, one "
    "phone number you actually answer, one email address you actually read, and "
    "one link. If the business is registered, <b>Owner</b>, <b>Founder</b>, "
    "<b>Director</b> and <b>Principal</b> all read correctly. If you are "
    "self-employed with nothing registered, put the work itself — Plumber, "
    "Bookkeeper, Photographer — because that is the word the other person will "
    "search for when they go looking for your card three weeks later.",
    "The title question feels bigger than it is. Nobody has ever failed to get "
    "hired because their card said Owner instead of Founder. What does lose you "
    "the job is a card with two phone numbers on it and no clue which one rings.",
])

S_TITLES = block(
    "Choosing your title when nobody assigns you one",
    table(
        ["Title", "How it reads", "Best when"],
        [
            ["<b>Owner</b>",
             "Plain and unambiguous. You are the business.",
             "Sole proprietors, single-owner limited companies, trades. Never wrong."],
            ["<b>Founder</b>",
             "The business is a thing that exists apart from you.",
             "You have built a brand, a product or an agency you intend to outlast you."],
            ["<b>Director</b>",
             "A formal role inside a registered company.",
             "You genuinely hold the position. In many countries it is filed with the "
             "companies registry — check yours before you print it."],
            ["<b>Principal</b>",
             "Senior and professional rather than commercial.",
             "Consultancies, design studios, practices where &ldquo;Owner&rdquo; sounds "
             "like you run a shop."],
            ["<b>Managing Director</b>",
             "You own it <em>and</em> you run it day to day.",
             "Common outside the United States; reads oddly inside it."],
            ["<b>CEO</b> / <b>President</b>",
             "There are layers of management beneath you.",
             "There actually are. On a one-person business it can read as inflated to "
             "the person holding the card."],
            ["<b>The trade itself</b>",
             "This is what I do.",
             "You are hired for a skill, not for owning something. Usually the strongest "
             "choice for self-employed trades."],
        ],
        note="One title, not three. &ldquo;Owner / Lead Consultant / Head of Delivery&rdquo; "
             "tells the reader you have no colleagues, which is the one thing the card was "
             "supposed to avoid saying."),
    tint=True)

S_TITLE_PROSE = prose("Two things worth getting right", [
    "<b>Do not claim a legal role you do not hold.</b> Director, in particular, is a "
    "position that is commonly registered with a national companies registry, and a "
    "card is a durable document. If you are unsure whether you hold it, check your "
    "own registrar rather than guessing — this page cannot tell you, and neither can "
    "anyone else who does not know how your business is set up.",
    "<b>Match the title to the room.</b> The same person can be Owner on a card handed "
    "to a homeowner and Principal on one handed to a procurement manager. On paper "
    "that means two print runs and a decision about which stack lives in which pocket. "
    "On a digital card it means editing one field, which is the practical reason "
    "owners tend to settle the question differently once the card stops being "
    "permanent.",
])

S_COOWNERS = block(
    "Two or more co-owners: three ways to handle it",
    cards3([
        ("One card each — the default",
         "Same design, same logo, same colours; each person's own name, direct number "
         "and email. The person you met can reach <em>you</em>, and neither of you "
         "loses a lead to the other's inbox. This is the right answer in almost every "
         "case."),
        ("One shared card with both names",
         "Looks equitable and fails at the moment of use. Whoever scans it does not "
         "remember which of you they spoke to, so they either guess or write to a "
         "shared address and wait. If you split the work by function, the card cannot "
         "route them to the right half."),
        ("A card with no person on it",
         "Business name, service, one number. This works for walk-in and call-out "
         "trades where the number is the business number and whoever picks up can "
         "help. It is a weak choice for anything sold on a relationship."),
    ]),
)

S_COOWNERS_PROSE = prose("The honest cost of one card each", [
    "On paper, one card each doubles the print run, and every time one of you changes "
    "a number you reprint both. That is the real reason co-owned businesses end up "
    "with a shared card they do not like.",
    "On a digital card the maths is different but not free, and it is worth saying "
    "plainly: <b>CompanyCard's free plan is one card per account.</b> Two co-owners "
    "means two free accounts — which works, costs nothing, and is genuinely how a lot "
    "of two-person businesses use it — or a paid plan if you want both cards managed "
    "in one place with the CompanyCard credit removed. Our team plan is $12 per user "
    "per month with no seat minimum, so a two-person business pays for two people "
    "rather than a five-seat floor. Billing is not live yet; paid plans are currently "
    "a preview and nothing is charged.",
])

S_NO_BUSINESS = prose("What to put on the card when the business isn't registered yet", [
    "Plenty of people start handing out cards before there is a company behind them, "
    "and that is fine. What matters is not claiming a legal status you do not have.",
    "<b>You can trade under your own name.</b> Put your name where a business name "
    "would go and the work underneath it. &ldquo;Sam Okafor — Bookkeeping&rdquo; is a "
    "complete, honest card, and it is easier to say on the phone than an invented "
    "trading name.",
    "<b>Leave off anything that asserts registration.</b> Ltd, LLC, Inc, GmbH, Pty, a "
    "company number, a registered office address — these are statements about legal "
    "status, not decoration. If they are not true today, they do not go on the card "
    "today.",
    "<b>Check a trading name before you commit it.</b> Name rules differ by country "
    "and sometimes by state or province, and a name that is free to use as a website "
    "is not automatically free to trade under. Check your own companies registry and "
    "your local trading-name rules first. If the name is still unsettled, that is the "
    "strongest possible argument for a card you can edit after you have handed it out "
    "rather than one you have already printed five hundred of.",
])

S_FIELDS = block(
    "The fields that actually get used",
    checklist([
        ("Your name.",
         "The one you introduce yourself with. Not the one on your passport, if they "
         "differ."),
        ("One role.",
         "See above. One."),
        ("One phone number.",
         "The one you answer. A card with a mobile and a landline makes the reader "
         "choose, and half of them choose wrong and give up."),
        ("One email address.",
         "Your own, not the info@ you read on Fridays — unless someone genuinely "
         "watches info@ all day."),
        ("One link.",
         "The page that proves you are real: a site, a booking page, a portfolio, a "
         "profile. One."),
        ("What you do, in plain words.",
         "If your business name does not say it, the card has to. &ldquo;Verity "
         "&amp; Co&rdquo; means nothing; &ldquo;Verity &amp; Co — Domestic "
         "Electricians&rdquo; means something."),
    ]),
    tint=True)

S_LEAVE_OFF = prose("What to leave off", [
    "A fax number. A second office address. Six social icons, five of which you have "
    "not posted to this year. A QR code that opens your homepage instead of saving "
    "your details — that is the most common mistake on a modern card, and it wastes "
    "the one thing a QR code is good at.",
    "Also leave off awards, memberships and certifications you cannot currently "
    "evidence. An owner's card is one of the few documents where a stranger will "
    "check.",
])

S_WHY_DIGITAL = prose("Why owners revisit their card more often than employees do", [
    "An employee's card changes when they change jobs. An owner's card changes when "
    "the service list changes, when the coverage area changes, when the number "
    "changes, when the business finally registers — and, more often than anyone "
    "admits, when they change their mind about the title.",
    "On paper each of those is a reprint, so most owners live with a card that is "
    "slightly wrong. A digital business card moves the cost: the QR code and the "
    "sharing link stay the same, and the details behind them are edited. Cards you "
    "handed out last year point at the corrected version.",
    "CompanyCard's free plan gives you one card with a QR code, a permanent sharing "
    "link, your profile, links and socials, an Apple or Google Wallet pass and "
    "unlimited edits, with no credit card. The honest limits: it is one card, and it "
    "carries a small CompanyCard credit. Removing the credit, along with custom "
    "branding, unlimited links and files, and lead capture, is what the $7.99 per "
    "month Pro plan is for ($5.99 per month billed annually).",
])

HOWTO = [
    "Decide your title first — one word or one short phrase, and one you would say "
    "out loud when introducing yourself.",
    "Choose the single phone number and single email address you will actually "
    "answer, and leave every other contact route off the card.",
    "Add the business name you trade under, plus a plain description of the work if "
    "the name does not make it obvious.",
    "Add one link that proves you are real — a site, a booking page or a portfolio.",
    "Give each co-owner their own card on the same design, rather than putting two "
    "names on one card.",
    "Share it as a QR code, a link or a wallet pass, and edit the details later "
    "without reprinting or resharing anything.",
]

S_HOWTO = block("How to build an owner's card in six decisions",
                steps_howto(HOWTO))

FAQS = [
    ("What job title should I put on my business card if I own the business?",
     "Owner, Founder, Director and Principal all read correctly on an owner's card, "
     "and none of them is wrong. Pick Owner if you want the plainest option, Founder "
     "if the business is a brand you intend to outlast you, Principal for a "
     "professional practice, and Director only if you actually hold that role — in "
     "many countries it is filed with the companies registry, so check yours. If you "
     "are self-employed and hired for a skill, the trade itself — Plumber, Bookkeeper, "
     "Photographer — is usually stronger than any ownership title. Whichever you "
     "choose, put one title on the card, not three."),
    ("Can two co-owners share one business card?",
     "You can, but it usually costs you leads. Whoever scans a two-name card does not "
     "remember which of you they met, so they write to a shared address and wait, or "
     "they guess. The better pattern is one card each on the same design, with each "
     "person's own direct number and email. On paper that doubles the print run. On a "
     "digital card each owner needs their own card — CompanyCard's free plan is one "
     "card per account, so two co-owners means either two free accounts or a paid "
     "plan that manages both in one place."),
    ("What do I put on a business card if my business isn't registered yet?",
     "Trade under your own name: put your name where the business name would go and "
     "the work you do underneath it. Leave off anything that asserts a legal status "
     "you do not have — Ltd, LLC, Inc, a company number or a registered office "
     "address. If you are still choosing a trading name, check it against your own "
     "companies registry and your local trading-name rules before committing it to "
     "print, and consider a card you can edit after handing it out rather than one "
     "you have already printed."),
    ("Should the owner's card look different from the employees' cards?",
     "No. The design, logo and colours should be identical across everyone in the "
     "business, including you — that is what makes the card look like it belongs to "
     "a company rather than a person. The only things that should differ are the "
     "name, the role and the direct contact details. A visually distinct owner's card "
     "reads as a hierarchy nobody asked about."),
    ("Is CEO the right title for a one-person business?",
     "It is accurate in the narrow sense and it can still work against you. CEO "
     "signals that there are layers of management underneath, so on a business with "
     "no employees it can read as inflated to the person holding the card — "
     "particularly if they meet you doing the work yourself an hour later. Owner or "
     "Founder carries the same authority without the mismatch. If you deal mostly "
     "with large organisations where CEO is the expected counterpart title, that is a "
     "reasonable argument for using it."),
    ("Can I change the title on a digital business card after I've shared it?",
     "Yes. On CompanyCard the QR code and the sharing link are permanent and the "
     "details behind them are editable, so changing your title, phone number or "
     "business name updates the card everyone already has. Unlimited edits are "
     "included on the free plan. This is the practical difference from paper, where "
     "changing a title means reprinting and every card already in circulation stays "
     "wrong."),
]

PAGES = [{
    "slug": SLUG,
    "crumb": "Business Cards for Business Owners",
    "title": "What to Put on a Business Card When You Own the Company | CompanyCard",
    "meta": ("What job title to use when you own the business, how two co-owners should "
             "handle cards, and what to put on a card when the business isn't registered "
             "yet. A practical guide for small business owners and the self-employed."),
    "og": ("Owner, Founder, Director or Principal? How co-owners should split cards, and "
           "what you can put on a card before the business is registered."),
    "h1": "What to put on a business card when you own the company",
    "lead": ("Nobody hands an owner a job title — you pick it yourself, usually at the "
             "worst possible moment. Here is how to choose one that reads right, how two "
             "or more co-owners should handle it, and what belongs on the card when the "
             "business has no registered name yet."),
    "cta_btn": "Create your free card",
    "cta2": ("See what's on the free plan", "pricing.html"),
    "sections": [S_ANSWER, S_TITLES, S_TITLE_PROSE, S_COOWNERS, S_COOWNERS_PROSE,
                 S_NO_BUSINESS, S_FIELDS, S_LEAVE_OFF, S_HOWTO, S_WHY_DIGITAL],
    "howto": HOWTO,
    "howto_name": "How to make a business card when you own the business",
    "faqs": FAQS,
    "cta_h": "One card, edited whenever you change your mind",
    "cta_p": ("Free forever, one card, no credit card. Change your title, your number or "
              "your business name later without reprinting anything."),
    "related": [
        ("Digital business cards for small business", "digital-business-card-for-small-business.html"),
        ("For freelancers & the self-employed", "digital-business-card-for-freelancers.html"),
        ("Cards for teams", "digital-business-cards-for-teams.html"),
        ("Digital vs paper business cards", "digital-business-card-vs-paper.html"),
        ("Pricing", "pricing.html"),
    ],
}]
