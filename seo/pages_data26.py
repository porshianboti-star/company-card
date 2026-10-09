# -*- coding: utf-8 -*-
"""Batch 28: digital-business-card-for-plumbers.html — a positive profession page.

Why this page: the standing backlog asks for more self-employed trade pages, and
plumbing is the largest one-van trade with no page of its own (contractors and
electricians exist; "your plumber" and "a one-van plumber" already appear as
examples on the contractors and small-business pages). Written for the
emergency-callout and repeat-customer reality of the trade, so it does not
duplicate the electricians page.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

Product claims are limited to what pricing.html and features.html state today
(2026-10-09): free = one card, QR and link sharing, profile/links/socials,
Apple and Google Wallet pass, unlimited edits, no scan cap, no credit card, and
the card carries a small CompanyCard credit. Pro adds unlimited links and files,
custom branding and themes, lead capture and analytics, and removes the credit.
No prices are printed, so a reprice cannot leave it stale. Nothing is claimed
about licensing rules in any country: the page tells the reader to show what
their own licence or registration body requires.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-plumbers.html"

WHY = [
    "Plumbing work is hired in two moods. One is the leak at eleven at night, when the "
    "homeowner searches, scrolls a neighbourhood group or digs out the magnet on the fridge "
    "and rings the first number that looks real. The other is the planned job — a bathroom "
    "refit, a boiler or water-heater swap — where they compare two or three quotes and pick "
    "the one they trust. Your card has to work for both: one tap to call in the first case, "
    "enough proof to win the quote in the second.",
    "Most of a plumber's next work comes from the last customer. The tenant passes your "
    "number to the landlord, the landlord to the letting agent, the homeowner to the "
    "neighbour whose kitchen is flooding. Whatever they forward has to open on any phone, "
    "with nothing to install, and save you into contacts in one tap so you are still there "
    "the next time something drips.",
    "And the details move. A personal mobile becomes a business line, an apprentice becomes "
    "a second van, you add gas or drainage work, the service area grows. Whatever is "
    "painted on the van or printed on a stack of cards is wrong the day one of those "
    "changes. A QR code that opens a live card is not: you edit the card once and every "
    "code already on the van, the invoices and the fridge magnets shows the new version.",
]

INCLUDE = [
    ("A tap-to-call number that you actually answer.",
     "Say whether it takes texts and WhatsApp, and whether you take emergency callouts and "
     "when."),
    ("The work you take, in the customer's words.",
     "“Leaks, blocked drains, water heaters, bathroom refits” is something a homeowner can "
     "match to the problem in front of them; “plumbing solutions” is not."),
    ("Where you go.",
     "The towns or postcodes you cover, because a stranger's first question is whether you "
     "come out to them."),
    ("Your licence, registration and insurance.",
     "Show whatever your licensing or registration body requires on advertising, with the "
     "number written out so a customer or landlord can check it."),
    ("Links to your finished work and your reviews.",
     "A link to photos of a tiled shower or a tidy boiler cupboard says more than a logo, "
     "and a link to the reviews you already have saves the customer a search."),
    ("A way to ask for a quote.",
     "A booking link, a quote form or an email address, for the planned jobs that are "
     "compared before anyone calls."),
]

ROWS = [
    ["Van, trailer or yard sign",
     "QR code next to the number",
     "Tap to call, and to save you for later"],
    ["Quotes, invoices and job sheets",
     "QR code or link in the footer",
     "Your licence details and a way to book the next job"],
    ["Fridge magnet or sticker left after a job",
     "QR code on the magnet",
     "The current number, months or years later"],
    ["Neighbourhood group or a message from a past customer",
     "The card link, forwarded",
     "What you do, where you go, and one tap to call"],
    ["Landlords and letting agents",
     "Link in an email or text",
     "Registration and insurance details, and a contact for tenants"],
]

FAQS = [
    ("What should a plumber's digital business card include?",
     "A tap-to-call number and whether you take emergency callouts, the kinds of work you "
     "take, the area you cover, your licence or registration and insurance details as your "
     "licensing body requires, links to finished jobs and reviews, and a way to ask for a quote."),
    ("How do I use a digital business card on the van?",
     "Put the card's QR code on the van next to your number. A customer points their phone "
     "camera at it, the card opens in the browser and they can call or save you in one "
     "tap. The same code works on quotes, invoices, job sheets and fridge magnets."),
    ("What happens to the QR codes on the van if my number changes?",
     "Nothing needs reprinting. The code opens your live card, so you edit the number once "
     "and every code already on the van, the paperwork and the magnets shows the new one."),
    ("Do my customers need an app?",
     "No. The card opens in any browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("Is it free for a one-van plumber?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For contractors & builders", "digital-business-card-for-contractors.html"),
       ("For electricians", "digital-business-card-for-electricians.html"),
       ("For small business", "digital-business-card-for-small-business.html"),
       ("QR code business card", "qr-code-business-card.html")]

PLUMBERS = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Plumbers",
    "title": "Digital Business Card for Plumbers — QR for the Van & Invoices | CompanyCard",
    "meta": ("A digital business card for plumbers — one tap to call from the QR code on your "
             "van, your licence and insurance shown up front, and a number you can change "
             "without repainting. Free to start, no app needed."),
    "h1": 'Digital business card for <span class="gradient-text">plumbers</span>',
    "lead": ("Plumbing is hired in a hurry or after three quotes. Give customers one card that "
             "calls you in a tap at eleven at night, shows your licence and finished work when "
             "they are comparing, and stays current on every van, invoice and fridge magnet."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Put a card on the van that never goes out of date.",
    "cta_p": "Free forever, no credit card, and the QR code keeps working when your details change.",
    "sections": [
        prose("How plumbing work actually arrives", WHY),
        block("What a plumber's card should carry", checklist(INCLUDE), tint=True),
        block("Where a plumber's card gets opened",
              table(["Where it is seen", "How it is shared", "What the customer needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free or Pro for a plumbing business", [
            "A one-van plumber can run the whole thing on the free plan: one card with a QR "
            "code and sharing link, profile, links and socials, and an Apple or Google Wallet "
            "pass so the code is on your lock screen when a customer asks for your number. "
            "There is no cap on scans and no credit card. The free card carries a small "
            "CompanyCard credit.",
            "Pro is for when the card starts doing sales work: lead capture, so someone who "
            "scans the van can leave their details for a quote, analytics on views and saves, "
            "unlimited links and files for a price list or photos of past jobs, custom "
            "branding and themes, and no credit. A firm with several vans can put every "
            "plumber on the same branded card on the Business plan. See "
            "<a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, business "
            "name, the number you answer and whether you take emergency callouts.",
            "List the work you take and the area you cover, then add your licence, "
            "registration and insurance details as your licensing body requires.",
            "Add links to photos of finished jobs and to your reviews, and a way to ask for a quote.",
            "Put the card's QR code on the van, your invoices and your magnets, and add the "
            "card to Apple or Google Wallet for the jobs where someone asks in person.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES26 = [PLUMBERS]
PAGES = PAGES26
