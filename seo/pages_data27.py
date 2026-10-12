# -*- coding: utf-8 -*-
"""Batch 29: digital-business-card-for-recruiters.html — a positive profession page.

Why this page: GSC (28 days to 2026-10-10) shows recruiting queries with no page
serving them — "digital business cards for recruiters" 1 @ 45, "best digital
business card for recruiting and hr teams at hiring events" 1 @ 9. Independent
and agency recruiters are self-employed or small-firm professionals who hand out
contact details all day (candidates, hiring managers, career fairs), which is
the ICP. Written around the two-sided nature of recruiting (candidates AND
clients) so it does not duplicate the sales-teams or events pages.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

Product claims are limited to what pricing.html and features.html state today
(2026-10-12): free = one card, QR and link sharing, profile/links/socials,
Apple and Google Wallet pass, unlimited edits, no scan cap, no credit card, and
the card carries a small CompanyCard credit. Pro adds unlimited links and files,
custom branding and themes, lead capture and analytics, and removes the credit.
Business adds central admin, brand and template lock, CRM sync, no seat minimum.
No ATS integration is claimed. No prices are printed.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-recruiters.html"

WHY = [
    "A recruiter's contact details travel to two audiences at once. Candidates need to know "
    "who you are, which roles or sectors you place, and how to send a CV. Hiring managers and "
    "clients need to know what you specialise in and why they should take your call. Most "
    "recruiters hand the same details to both, dozens of times a week, on calls, in messages "
    "and across a table at a career fair.",
    "Much of that handover happens where paper does badly. A candidate on a video interview "
    "cannot take a card from you; a graduate at a busy fair stand takes ten cards and loses "
    "nine; a hiring manager forwards your details to a colleague by message. A link or a QR "
    "code that opens in any browser and saves you into contacts in one tap works in all three.",
    "Recruiters also move: desks change, agencies rebrand, an independent recruiter changes "
    "the sectors they cover or their booking link. A printed card is wrong the day that "
    "happens. A live card is edited once, and every QR code and link you have already shared "
    "shows the new details.",
]

INCLUDE = [
    ("The roles and sectors you place.",
     "“Finance and accounting roles in the Midlands” lets a candidate and a client both see "
     "in a second whether you are the right recruiter; “talent solutions” does not."),
    ("A direct number and the hours you take calls.",
     "Candidates often call on a lunch break, so say when you are reachable."),
    ("Where to send a CV.",
     "An email address or a link to your application or jobs page, so a candidate does not "
     "have to ask."),
    ("A booking link for a first call.",
     "For candidates and hiring managers alike, a scheduling link turns “let's talk” into a "
     "time in the diary."),
    ("Your agency, or your own name if you work independently.",
     "With the logo and website, so a client can check who you are before they reply."),
    ("Your professional profiles.",
     "A link to your LinkedIn profile and to current openings, which is where most candidates "
     "will look next anyway."),
]

ROWS = [
    ["Career fair or campus event",
     "QR code on the stand, a badge or a phone screen",
     "Save you in one tap, and where to send a CV"],
    ["Video interview or screening call",
     "Card link pasted in the chat",
     "Your direct number and booking link"],
    ["Email to a hiring manager",
     "Link or QR in the email signature",
     "Your specialism and agency, at a glance"],
    ["Candidate forwards you to a friend",
     "The card link, forwarded",
     "What roles you place and how to reach you"],
    ["Networking event or client meeting",
     "Card added to Apple or Google Wallet",
     "A code on your lock screen instead of a card in a pocket"],
]

FAQS = [
    ("What should a recruiter's digital business card include?",
     "The roles and sectors you place, a direct number and the hours you take calls, where "
     "to send a CV, a booking link for a first call, your agency name and logo or your own "
     "name if you work independently, and a link to your LinkedIn profile and current openings."),
    ("How do recruiters use a digital business card at a career fair?",
     "Show the card's QR code on the stand, a badge or your phone. A candidate points their "
     "camera at it, the card opens in the browser and they can save you in one tap and see "
     "where to send a CV. On Pro, lead capture lets them send their own name and details back "
     "from your card."),
    ("Do candidates need an app to open my card?",
     "No. The card opens in any browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("Can a recruitment agency give every recruiter a matching card?",
     "Yes. The Business plan has no seat minimum, so a three-person agency pays for three "
     "cards. It adds a central admin dashboard, brand and template lock so every recruiter's "
     "card shows the same agency name and logo, and CRM sync."),
    ("Is it free for an independent recruiter?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For sales teams", "digital-business-card-for-sales-teams.html"),
       ("For events & conferences", "digital-business-card-for-events.html"),
       ("For consultants", "digital-business-card-for-consultants.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html")]

RECRUITERS = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Recruiters",
    "title": "Digital Business Card for Recruiters — Career Fairs & Candidates | CompanyCard",
    "meta": ("A digital business card for recruiters — candidates save you in one tap from a "
             "QR code at a career fair or a link on a call, and see your sectors and where to "
             "send a CV. Free to start, no app needed."),
    "h1": 'Digital business card for <span class="gradient-text">recruiters</span>',
    "lead": ("Recruiters hand their details to candidates and clients all day — on calls, by "
             "message and at career fairs. Give both one card that saves you in a tap, says what "
             "you place, and stays current when your desk or agency changes."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "One card for every candidate and every client.",
    "cta_p": "Free forever, no credit card, and the link keeps working when your details change.",
    "sections": [
        prose("Why recruiters hand out their details differently", WHY),
        block("What a recruiter's card should carry", checklist(INCLUDE), tint=True),
        block("Where a recruiter's card gets opened",
              table(["Where it is seen", "How it is shared", "What the other person needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free, Pro or Business for recruiters", [
            "An independent recruiter can start on the free plan: one card with a QR code and "
            "sharing link, profile, links and socials, and an Apple or Google Wallet pass. "
            "There is no cap on scans and no credit card. The free card carries a small "
            "CompanyCard credit.",
            "Pro is for when the card should collect as well as share: lead capture, so a "
            "candidate who scans your code at a fair can send their details back to you, "
            "analytics on views and saves, unlimited links and files, custom branding and "
            "themes, and no credit. An agency can put every recruiter on the same branded "
            "card on the Business plan, which has no seat minimum and adds central admin, "
            "brand and template lock and CRM sync. See <a href=\"pricing.html\">pricing</a> "
            "for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, agency or "
            "business name, direct number and the roles and sectors you place.",
            "Add where to send a CV, a booking link for a first call and a link to your "
            "LinkedIn profile and current openings.",
            "Paste the card link into your email signature and interview invitations.",
            "Add the card to Apple or Google Wallet and print the QR code for your fair stand "
            "or badge.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES27 = [RECRUITERS]
PAGES = PAGES27
