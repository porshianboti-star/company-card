# -*- coding: utf-8 -*-
"""Batch 27: digital-business-card-for-sales-teams.html — a positive use-case page.

Why this page (GSC, 28 days to 2026-10-04): a small sales cluster reaches the
site with no page written for it — "digital business card for field sales" (3
impressions @ 57), "best digital business card for sales teams" (1 @ 59),
"best virtual business card tools for field sales professionals" (1 @ 65),
"best digital business card platforms for global field sales" (1 @ 58), "most
recommended digital business card app by sales professionals" (1 @ 62),
"business card for employees" (5 @ 50). The teams page is written for a whole
company's staff; this one is written for the people whose job is the handshake.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

Product claims are limited to what pricing.html and features.html state today
(2026-10-07): free = one card, QR and link sharing, profile/links/socials,
Apple and Google Wallet pass, unlimited edits, no scan cap, no credit card, and
the card carries a small CompanyCard credit. Pro adds unlimited links and files,
custom branding and themes, lead capture with view-and-save analytics, and
removes the credit. Business is "everything in Pro, plus" a central admin
dashboard, brand and template lock, CRM sync (features.html: "Export anywhere —
CRM, CSV or Zapier"), team analytics, SSO and priority support, priced per user
with no seat minimum and bought by contacting us. Enterprise adds SCIM/SAML,
audit logs, data residency and an SLA. No prices are printed on this page, so a
reprice cannot leave it stale. Nothing is claimed about offboarding, named CRM
integrations, badge scanning or NFC hardware.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-sales-teams.html"

WHY = [
    "A sales conversation ends with an exchange of details, and the paper version of that "
    "exchange leaks. The prospect pockets a card and types it into their phone later, or "
    "does not; the rep writes a name on the back of the prospect's card and loses the "
    "context by Friday. A digital business card closes both ends of the exchange on the "
    "spot: the prospect saves the rep in one tap, and on Pro and Business the prospect can "
    "send their own details back from the same card.",
    "Field sales adds a second problem: the details change. Territories are redrawn, a rep "
    "gets a new direct line, the product sheet is updated, someone moves from inside sales "
    "to the road. A printed card is wrong the day after any of those, and a box of five "
    "hundred is wrong for a year. A CompanyCard is edited once and every link, QR code and "
    "wallet pass that was ever shared shows the current version.",
    "The third problem is the brand. Twenty reps with twenty self-made cards look like twenty "
    "small companies. The Business plan locks the template and the brand, so every card in "
    "the team carries the same logo, colours and layout, and the admin changes the company "
    "address once for everyone.",
]

INCLUDE = [
    ("Name, title and territory.",
     "“Account executive, Pacific Northwest” tells a prospect in one line whether you are "
     "the right person to call back."),
    ("Direct mobile and a work email.",
     "The number a prospect can actually reach on a site visit, not a switchboard."),
    ("A calendar link.",
     "Booking a follow-up from the card removes the three-email dance about availability."),
    ("One link to what you sell.",
     "A product page, a demo video or a one-page PDF. On Pro the card carries files and "
     "unlimited links, so the brochure travels with the card instead of in a bag."),
    ("The company logo and colours, locked.",
     "On the Business plan the admin sets the template once and reps cannot drift from it."),
    ("Lead capture switched on.",
     "So the person you just met can leave their name, company and email before you are "
     "back in the car."),
]

ROWS = [
    ["Trade show or conference",
     "Badge or lanyard QR, phone lock screen, Wallet pass",
     "Save-contact button, then a way to leave their own details"],
    ["Site visit or walk-in",
     "QR on a clipboard, tablet or the back of the phone",
     "Direct mobile and the product link"],
    ["Video call or demo",
     "Link in the chat, QR on the closing slide or the video background",
     "Calendar link for the follow-up"],
    ["Follow-up email or LinkedIn message",
     "Link in the email signature or the message",
     "The same card, so the saved contact is already current"],
    ["Months later, when they are ready to buy",
     "The contact they saved at the first meeting",
     "Your current number and title, not the one from last year"],
]

FAQS = [
    ("Can a rep capture leads at a trade show with a digital business card?",
     "Yes, on Pro or Business. Lead capture lets the person who scans the card send their "
     "own name and contact details back, and they are saved in the rep's account. On the "
     "free plan the prospect can save the rep's details in one tap, but the card does not "
     "collect theirs."),
    ("Does the prospect need an app to open the card?",
     "No. The card opens in any browser from a link or a QR code, and the prospect saves "
     "the rep's details to their contacts with one tap. Only the rep needs an account."),
    ("Does a sales team need a minimum number of seats?",
     "No. The Business plan is priced per user with no seat minimum, so a two-rep team pays "
     "for two cards and a team of forty pays for forty. Business is bought by contacting us "
     "rather than self-serve; see <a href=\"pricing.html\">pricing</a> for the current rate."),
    ("Can captured leads go into our CRM?",
     "On the Business plan, yes. CRM sync is part of the plan, and captured contacts can "
     "also be exported as CSV or through Zapier. Team analytics show how each card is "
     "performing. Pro includes lead capture with view-and-save analytics but not CRM sync."),
    ("Can we stop reps from changing the design?",
     "Yes. Brand and template lock on the Business plan keeps every card on the same logo, "
     "colours and layout, and the admin edits shared details such as the company address "
     "once from a central dashboard. Reps still edit their own name, title and contact "
     "details."),
    ("Is it free for a single rep?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture and analytics are part of "
     "Pro, and team controls are part of Business."),
]

REL = [("Digital business cards for teams", "digital-business-cards-for-teams.html"),
       ("For consultants", "digital-business-card-for-consultants.html"),
       ("Digital business cards for events", "digital-business-card-for-events.html"),
       ("Free digital business card", "free-digital-business-card.html")]

SALES = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Sales Teams",
    "title": "Digital Business Card for Sales Teams & Field Sales Reps | CompanyCard",
    "meta": ("A digital business card for sales teams and field sales reps — prospects save "
             "you in one tap, leave their details back on your card, and every rep stays on "
             "brand from one admin dashboard. No seat minimum. Free to start."),
    "h1": 'Digital business card for <span class="gradient-text">sales teams &amp; field '
          'sales reps</span>',
    "lead": ("The handshake ends with an exchange of details. Give every rep one card that "
             "the prospect saves in a tap, that captures the prospect's details back, and that "
             "stays current and on brand when the territory, the title or the logo changes."),
    "cta_btn": "Create your free card",
    "cta2": ("Talk to us about teams", "pricing.html"),
    "cta_h": "Put the whole sales team on one card.",
    "cta_p": "One rep is free forever. A team pays per rep, with no seat minimum, and the "
             "brand is locked from one dashboard.",
    "sections": [
        prose("Why sales teams move the business card off paper", WHY),
        block("What a sales rep's card should carry", checklist(INCLUDE), tint=True),
        block("Where a rep's card gets opened",
              table(["Where you meet", "How the card is shared",
                     "What the prospect needs first"], ROWS,
                    note="The same link works in every row, and an edit reaches all of them "
                         "at once.")),
        prose("Running cards across a team", [
            "One rep can run a card alone on the free plan: one card with QR and link "
            "sharing, profile, links and socials, and an Apple or Google Wallet pass, with no "
            "cap on scans. The free card carries a small CompanyCard credit.",
            "Pro is the plan for a rep who wants the exchange to run both ways. It adds lead "
            "capture, so the prospect can leave their details from the card, view-and-save "
            "analytics, unlimited links and files for the product sheet and demo video, "
            "custom branding and themes, and it removes the credit.",
            "Business is everything in Pro for every rep, plus the things a sales manager "
            "needs: a central admin dashboard, brand and template lock, CRM sync with CSV and "
            "Zapier export, team analytics, SSO and priority support. It is priced per user "
            "with no seat minimum, so a small team is not asked to pay for empty seats, and "
            "it is set up by contacting us rather than self-serve. Larger organisations that "
            "need SCIM and SAML provisioning, audit logs, data residency or an SLA have an "
            "Enterprise plan. See <a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up a sales team", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and make the first card: "
            "name, title, territory, direct mobile, work email and a calendar link.",
            "Add one link to what you sell, and on Pro attach the product sheet or demo video "
            "as a file so it travels with the card.",
            "Switch on lead capture, then add the card to Apple or Google Wallet so the QR "
            "code is on the lock screen at the next show.",
            "For the team, contact us about Business: the admin sets the locked template and "
            "brand once, each rep gets a card on it, and captured leads sync to the CRM.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES25 = [SALES]
PAGES = PAGES25
