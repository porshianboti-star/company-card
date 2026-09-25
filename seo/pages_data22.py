# -*- coding: utf-8 -*-
"""Batch 24: digital-business-card-for-bookkeepers.html — a positive profession page.

Picked from Search Console (28 days to 2026-09-22): "bookkeeping business card"
10 impressions + "bookkeeper business card" 5, all served by the accountants page
at an average position of 38.1. That page is written around a CPA's practice
(licence numbers, tax deadlines, referral partners such as solicitors). A
bookkeeper's work is different and this page is built on those differences:
monthly recurring work rather than a filing season, clients who are mostly
remote, the accounting software a bookkeeper works in as the deciding
credential, and accountants as the main referral source.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

Product claims are limited to what pricing.html states today (2026-09-25): free
plan = one card, QR and link sharing, profile/links/socials, Apple and Google
Wallet pass, unlimited updates, free forever, no credit card, and the card
carries a small CompanyCard credit; Pro ($7.99/mo) adds lead capture and
analytics, unlimited links and files, and removes the credit. Paid billing is a
preview. No file-upload claim for the free plan: the "secure upload" line tells
the bookkeeper to link to the portal they already use.

No invented credentials rules. Software certifications are described as things
bookkeepers commonly list, and registration/licensing is "check the rules where
you work" — requirements differ by country and state.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-bookkeepers.html"

WHY = [
    "A bookkeeper is hired for the months that follow, not for one job. The client is "
    "choosing who will see their bank feeds every week, so the decision is made slowly and "
    "usually on someone else's word: the accountant who does their year-end, another owner in "
    "the same trade, a business group where someone asked who does their books. By the time "
    "they contact you they have normally been sent your details by someone else, which means "
    "your card is read second-hand, often on a phone, often weeks after it was shared.",
    "Much of the work is remote. You may never meet a client in person: the introduction is a "
    "forwarded link, the first meeting is a video call and the rest happens inside the "
    "accounting software. A paper card has nowhere to go in that sequence. A link does — it "
    "sits in the email introduction, in your email signature, on the video call, and in the "
    "client's contacts once they save it.",
    "The details a prospective client checks are specific to bookkeeping: which software you "
    "work in, whether you take on catch-up work for a year of unreconciled accounts, whether "
    "you run payroll or only the books, and what a month of your time costs. Those change more "
    "often than a name and phone number do, and a card you can edit keeps every copy you have "
    "already handed out current.",
]

INCLUDE = [
    ("The software you work in.",
     "QuickBooks, Xero, Sage, FreshBooks — owners usually already use one and look for a "
     "bookkeeper who knows it. If you hold a vendor certification, name it."),
    ("What you do each month.",
     "Reconciliations, bills and invoicing, payroll, sales tax or VAT returns, month-end "
     "reports. Say where your work stops and the accountant's starts."),
    ("Whether you take catch-up and clean-up work.",
     "Owners who are behind search for exactly this; say whether you take it on and how far "
     "back you will go."),
    ("Who you work with.",
     "A trade or client type — contractors, online shops, cafés, landlords, charities — makes "
     "the right owner recognise themselves."),
    ("How you price.",
     "A monthly package, a starting price or “fixed monthly fee after a free review” "
     "all answer the question before it is asked."),
    ("A booking link for a discovery call.",
     "If new clients start with a short call, put the booking link one tap away."),
    ("A link to the secure portal you already use.",
     "For sending statements and receipts. Point to your practice or accounting software's own "
     "upload route rather than asking for documents by email."),
]

ROWS = [
    ["Introduced by an accountant",
     "The accountant forwards your link in an email to their client",
     "Your software, what you do each month and a booking link"],
    ["Referred by another owner",
     "Pasted into a text or a trade group chat",
     "The client types you work with and how you price"],
    ["Owner searching for help catching up",
     "Found your card link in a directory profile or social bio",
     "That you take catch-up work and how far back"],
    ["Local business networking",
     "Scans the QR code on your phone or name badge",
     "Save-contact button, then the discovery-call link"],
    ["Existing client, a year on",
     "Opens the contact they saved when they signed up",
     "Your current number, portal link and hours"],
]

FAQS = [
    ("What should a bookkeeper put on a digital business card?",
     "Your name and business, the accounting software you work in and any certification you "
     "hold for it, the monthly services you provide, whether you take catch-up work, the client "
     "types you specialise in, how you price, a link to book a discovery call and a link to the "
     "secure portal clients use to send documents."),
    ("How is a bookkeeper's card different from an accountant's?",
     "An accountant's card is organised around qualifications and the filing calendar. A "
     "bookkeeper's is organised around ongoing monthly work: which software you use, what you "
     "reconcile and run each month, and where your work hands over to the client's accountant. "
     "Our <a href=\"digital-business-card-for-accountants.html\">accountants page</a> covers "
     "the accountant's side."),
    ("Can I share it with clients I never meet in person?",
     "Yes. The card is a link, so it goes in an email introduction, a message, your email "
     "signature or the chat of a video call. The person who receives it opens it in their "
     "browser and saves your details with one tap — they do not need an app or an account."),
    ("Should I list my prices on the card?",
     "That is your decision. Showing a starting monthly price, or saying that fees "
     "are fixed after a free review, filters out enquiries that were never going to "
     "fit. Because the card is editable, a price change reaches every copy you have shared."),
    ("Do I need to show a registration or licence number?",
     "It depends where you work. Some countries and states regulate bookkeeping services or "
     "require registration for certain work, such as payroll or tax filings; many do not. "
     "Check the rules that apply to you, and if you hold a registration, adding it to the card "
     "is quick."),
    ("Is it free?", "Yes. The free plan includes " + FREE_SPEC),
]

REL = [("For accountants", "digital-business-card-for-accountants.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
       ("For small business", "digital-business-card-for-small-business.html"),
       ("Free digital business card", "free-digital-business-card.html")]

BOOKKEEPER = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Bookkeepers",
    "title": "Digital Business Card for Bookkeepers | CompanyCard",
    "meta": ("A digital business card for bookkeepers — show the software you work in, your "
             "monthly services and catch-up work, and let referred clients book a discovery "
             "call. Free to start."),
    "h1": 'Digital business card for <span class="gradient-text">bookkeepers</span>',
    "lead": ("Bookkeeping clients arrive through an accountant's email or another owner's "
             "recommendation, and most of them you will only ever meet on a call. Your card "
             "should be a link that answers their first questions wherever it is forwarded."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Your books are tidy. Make your card match.",
    "cta_p": "Free forever, no credit card, and the link never changes when your details do.",
    "sections": [
        prose("How bookkeepers get clients, and where the card is read", WHY),
        block("What a prospective client looks for on a bookkeeper's card",
              checklist(INCLUDE), tint=True),
        block("Where your card gets opened",
              table(["How the client finds you", "How the card reaches them",
                     "What they need to see first"], ROWS,
                    note="The same link works in every row, and edits reach all of them.")),
        prose("What changes, and why an editable card suits bookkeeping", [
            "A bookkeeping practice changes in small steps: you add payroll, drop a software "
            "platform, start or stop taking catch-up work, move a monthly package price, or "
            "close to new clients for a busy quarter. Each change makes a printed card slightly "
            "wrong. With CompanyCard you edit the card once and every link, QR code and saved "
            "copy shows the update.",
            "If you have one card to run, the free plan covers it: one card with QR and link "
            "sharing, your profile, links and socials, and an Apple or Google Wallet pass. The "
            "free card carries a small CompanyCard credit. Pro removes that credit and adds "
            "lead capture and analytics, so you can see how often the card an accountant "
            "forwarded was actually opened. See <a href=\"pricing.html\">pricing</a> for the "
            "full plan list.",
        ]),
        block("Setting it up", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, business name "
            "and “Bookkeeper” or the title you use.",
            "Add the software you work in, your monthly services and whether you take catch-up "
            "work.",
            "Add a discovery-call booking link and the link to the portal clients use for "
            "documents.",
            "Put the link in your email signature and send it to the accountants who refer to "
            "you, so they can forward it without retyping anything.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES22 = [BOOKKEEPER]
PAGES = PAGES22
