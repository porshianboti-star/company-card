# -*- coding: utf-8 -*-
"""Batch 31: digital-business-card-for-financial-advisors.html — a positive profession page.

Why this page: every backlog profession page already exists (batch 30 was the
digital-business-card hub fix). Independent financial advisors and planners are
self-employed professionals whose business runs on referrals and a first
meeting, which is the ICP; no page served them. GSC (28 days to 2026-10-12)
shows only adjacent queries ("digital business cards for insurance
professionals" 7 @ 51.1, "digital business cards for loan officers" 1 @ 54),
which the insurance-agents and mortgage-brokers pages serve — so this page is
written around referrals, introductions and annual reviews, not loans or
policies, to avoid cannibalising them.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

No compliance, regulatory or archiving claim is made: the page tells advisors
to have the card's wording approved by whoever reviews their marketing, and
says nothing about what any regulator requires. No prices are printed.

Product claims are limited to what pricing.html and features.html state today
(2026-10-15): free = one card, QR and link sharing, profile/links/socials,
Apple and Google Wallet pass, unlimited edits, no credit card, and the card
carries a small CompanyCard credit. Pro adds unlimited links and files, custom
branding and themes, lead capture and analytics, and removes the credit.
Business adds central admin, brand and template lock, CRM sync, no seat minimum.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-financial-advisors.html"

WHY = [
    "An independent financial advisor's next client usually arrives through someone else: a "
    "happy client who mentions you to a colleague, an accountant or solicitor who refers a "
    "client, a friend who passes your name on at a dinner. Each of those introductions starts "
    "with your contact details being handed on by a person who is not you.",
    "Paper does that job badly. The card a client took at their first meeting is in a drawer "
    "two years later, and the referral partner who promised to pass your details on has to "
    "dig out an old email. A link they can forward in a message, or a QR code that saves you "
    "into contacts in one tap, travels with the introduction.",
    "Advisors' details also change: you move to a new network or firm, add a qualification, "
    "change your booking link or the areas you focus on. A printed card is wrong the day that "
    "happens. A live card is edited once, and every link and QR code you have already shared "
    "shows the new details.",
]

INCLUDE = [
    ("The people you help and what you help them with.",
     "“Retirement planning for business owners and their families” tells a referred prospect "
     "in a second whether you are the right advisor; a generic “wealth solutions” does not."),
    ("Your firm, or your own name if you are independent.",
     "With the logo and website, so a prospect can check who you are before the first call."),
    ("Your qualifications and the details you are expected to show.",
     "Designations, firm or registration details and any wording your firm or compliance "
     "reviewer asks for. Have the card approved the same way as the rest of your marketing."),
    ("A booking link for an introductory meeting.",
     "It turns “you should talk to my advisor” into a time in the diary."),
    ("A direct number and an email address.",
     "Clients phone when something changes in their life, so make the direct line easy to find."),
    ("Your professional profiles and website.",
     "A link to your LinkedIn profile and your firm page, which is where a referred prospect "
     "looks next anyway."),
]

ROWS = [
    ["A client recommends you to a friend",
     "The card link, forwarded by message",
     "Who you help and a way to book a first call"],
    ["An accountant or solicitor refers a client",
     "The card link in their email to the client",
     "Your firm, qualifications and direct number"],
    ["First meeting or annual review",
     "QR code on your phone, saved in one tap",
     "Your direct number in their contacts for next time"],
    ["Seminar, workshop or networking event",
     "QR code on a slide, a badge or a table card",
     "Save you in one tap without queuing for a card"],
    ["Emails to clients and prospects",
     "Link or QR in the email signature",
     "Your booking link and website, one click away"],
]

FAQS = [
    ("What should a financial advisor's digital business card include?",
     "Who you help and what you help them with, your firm name and logo or your own name if you "
     "are independent, your qualifications and any details your firm or compliance reviewer asks "
     "you to show, a booking link for an introductory meeting, a direct number and email, and a "
     "link to your LinkedIn profile and website."),
    ("Does CompanyCard check my card's wording for compliance?",
     "No. CompanyCard is the card and the sharing; it does not review what you write. Treat the "
     "card like the rest of your marketing and have its wording approved by whoever reviews your "
     "materials. Because the card is live, a change they ask for is one edit, and every link and "
     "QR code you have already shared shows it."),
    ("How does a digital business card help with referrals?",
     "A client or referral partner can forward your card link in a message or an email, and the "
     "person they introduce opens it in any browser and saves you to their contacts in one tap. "
     "On Pro, lead capture lets that person send their own name and details back from your card."),
    ("Do my clients need an app to open my card?",
     "No. The card opens in any browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("Is it free for an independent financial advisor?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For insurance agents", "digital-business-card-for-insurance-agents.html"),
       ("For mortgage brokers", "digital-business-card-for-mortgage-brokers.html"),
       ("For accountants", "digital-business-card-for-accountants.html"),
       ("For consultants", "digital-business-card-for-consultants.html")]

ADVISORS = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Financial Advisors",
    "title": "Digital Business Card for Financial Advisors — Referrals & Clients | CompanyCard",
    "meta": ("A digital business card for financial advisors and planners — clients and referral "
             "partners forward one link, prospects save you in one tap and book a first meeting. "
             "Free to start, no app needed."),
    "h1": 'Digital business card for <span class="gradient-text">financial advisors</span>',
    "lead": ("Most advisors grow through introductions — a client, an accountant or a friend "
             "passing your name on. Give them one card they can forward, that saves you in a tap "
             "and stays current when your firm or details change."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "One card for every client and every introduction.",
    "cta_p": "Free forever, no credit card, and the link keeps working when your details change.",
    "sections": [
        prose("Why an advisor's details are handed on by someone else", WHY),
        block("What a financial advisor's card should carry", checklist(INCLUDE), tint=True),
        block("Where an advisor's card gets opened",
              table(["Where it is seen", "How it is shared", "What the other person needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free, Pro or Business for financial advisors", [
            "An independent advisor can start on the free plan: one card with a QR code and "
            "sharing link, profile, links and socials, and an Apple or Google Wallet pass, with "
            "no credit card. The free card carries a small CompanyCard credit.",
            "Pro is for when the card should collect as well as share: lead capture, so a "
            "referred prospect can send their details back from your card, analytics on views "
            "and saves, unlimited links and files, custom branding and themes, and no credit. "
            "A practice can put every advisor on the same branded card on the Business plan, "
            "which has no seat minimum and adds central admin, brand and template lock and CRM "
            "sync. See <a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, firm or "
            "business name, direct number and who you help.",
            "Add your qualifications and any details your firm asks you to show, a booking link "
            "for an introductory meeting, and links to your website and LinkedIn profile.",
            "Have the wording approved the way you approve the rest of your marketing.",
            "Paste the card link into your email signature, add the card to Apple or Google "
            "Wallet, and send the link to the people who refer clients to you.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES28 = [ADVISORS]
PAGES = PAGES28
