# -*- coding: utf-8 -*-
"""Batch 33: digital-business-card-for-interior-designers.html — a positive profession page.

Why this page: every backlog profession and feature page already exists, the
comparison re-verify is next due ~2026-11-01, and GSC (28 days to 10/17) shows
no un-served query gap — the one candidate, "digital business card for field
sales" (18 impressions @ 53), is already served by the sales-teams page, whose
title names field sales reps, so a new page would only cannibalise it.
Interior designers are self-employed professionals and small studios (the
ICP) whose work is sold on a portfolio and on referrals from realtors,
contractors and suppliers; no page served them and none of the existing trade
pages mention them, so there is nothing to cannibalise. Coverage page, not
query-driven.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page. No prices are printed. No claim is made
about design-industry accreditation: the page tells designers to show
whatever membership or certification they already show elsewhere.

Product claims are limited to what pricing.html / features.html / facts.py
state today (2026-10-19): free = one card, QR and link sharing, profile, links
and socials, Apple and Google Wallet pass, unlimited edits, no credit card,
and the card carries a small CompanyCard credit. Pro adds unlimited links and
files, custom branding and themes, lead capture and analytics, and removes
the credit. Business adds central admin, brand and template lock, CRM sync,
no seat minimum.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-interior-designers.html"

WHY = [
    "An interior designer is hired on two things: what your work looks like, and who vouched "
    "for you. A paper card carries neither. It has your name and a number, and the person "
    "holding it still has to go and find your portfolio before they can decide whether to call.",
    "A digital card puts the portfolio one tap away. A homeowner scans the QR code at the end of "
    "a consultation and lands on your card with your project photos, your Instagram or Pinterest "
    "and your website, then saves your number without typing it. A realtor or contractor who "
    "refers you can forward the link in a message instead of describing you from memory.",
    "The details designers hand out also change: a new studio address, a new showroom, a new "
    "booking link, a portfolio that has three better projects than it had last spring. A printed "
    "card is out of date the day that happens. A live card is edited once, and every QR code "
    "and link you have already given out shows the current version.",
]

INCLUDE = [
    ("What you design and for whom.",
     "“Residential interiors and kitchen renovations in the Bay Area” or “Commercial fit-outs "
     "for cafés and boutiques” tells a prospect in one line whether you are the right call."),
    ("Your studio name and logo, or your own name if you work alone.",
     "With your website, so a referral can check your work before they get in touch."),
    ("Your portfolio and social links.",
     "The project gallery on your site, your Instagram, Pinterest or Houzz, and anywhere else "
     "your work is photographed. On the free plan the card holds your profile, links and "
     "socials; Pro adds unlimited links and files, so a PDF lookbook can sit on the card too."),
    ("A consultation booking link.",
     "The scheduling link you already use for a first meeting or a site visit."),
    ("Any membership or certification you already show elsewhere.",
     "Whatever your professional association or jurisdiction expects — CompanyCard does not "
     "check or supply these, so add them exactly as they appear on your website."),
    ("A direct number and an email address.",
     "For the contractor on site who needs you now, not a form."),
]

ROWS = [
    ["End of a first consultation",
     "QR code on your phone, scanned before you leave",
     "Your portfolio, then your number saved in one tap"],
    ["Referral from a realtor, architect or contractor",
     "The card link forwarded in their message",
     "Who you are and what you have built, before they decide to call"],
    ["Showroom, trade fair or home show",
     "QR code on your stand or saved to Apple or Google Wallet",
     "A way to save you without typing while the stand is busy"],
    ["Supplier and trade reps",
     "The card link in your email signature",
     "Your studio address, direct number and where to send samples"],
    ["Finished project, handover day",
     "The card link in the handover email",
     "A link they can pass to the neighbour who admired the kitchen"],
]

FAQS = [
    ("What should an interior designer's digital business card include?",
     "What you design and for whom, your studio name and logo or your own name, your website "
     "and portfolio, your Instagram, Pinterest or Houzz, a consultation booking link, any "
     "membership or certification you already show elsewhere, and a direct number and email."),
    ("Can I put my portfolio on the card?",
     "Yes. On the free plan the card carries your profile, links and socials, so your portfolio "
     "page and your project galleries are one tap away. Pro adds unlimited links and files, so a "
     "PDF lookbook or a project sheet can sit on the card as well."),
    ("What happens to the cards I have already handed out when my studio moves?",
     "Nothing needs reprinting. The QR code and link point to your live card, so you edit the "
     "address once and every card, brochure and email you have already sent shows the new "
     "details."),
    ("Do clients need an app to open my card?",
     "No. The card opens in any browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("Is it free for a self-employed interior designer?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For photographers", "digital-business-card-for-photographers.html"),
       ("For realtors", "digital-business-card-for-realtors.html"),
       ("For contractors", "digital-business-card-for-contractors.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html")]

DESIGNERS = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Interior Designers",
    "title": "Digital Business Card for Interior Designers — Portfolio in One Tap | CompanyCard",
    "meta": ("A digital business card for interior designers — your portfolio, Instagram and "
             "booking link one tap from a QR code, saved to a client's phone without typing, and "
             "always current when your studio or work changes. Free to start, no app needed."),
    "h1": 'Digital business card for <span class="gradient-text">interior designers</span>',
    "lead": ("Clients hire the work they can see and the name a friend passed on. Give both of "
             "them one card that opens on your portfolio, saves you in a tap and stays current "
             "when your studio or your best projects change."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Your portfolio, one scan away.",
    "cta_p": "Free forever, no credit card, and the link keeps working when your details change.",
    "sections": [
        prose("Why a designer's card has to carry the portfolio", WHY),
        block("What an interior designer's card should carry", checklist(INCLUDE), tint=True),
        block("Where a designer's card gets opened",
              table(["Where it is seen", "How it is shared", "What the other person needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free, Pro or Business for interior designers", [
            "A self-employed designer can start on the free plan: one card with a QR code and "
            "sharing link, profile, links and socials, and an Apple or Google Wallet pass, with "
            "no credit card. The free card carries a small CompanyCard credit.",
            "Pro is for when the card should collect as well as show: lead capture, so a "
            "homeowner can send their details from your card after a home show, analytics on "
            "views and saves, unlimited links and files for a lookbook, custom branding and "
            "themes so the card matches the studio, and no credit. A studio can put every "
            "designer on the same branded card on the Business plan, which has no seat minimum "
            "and adds central admin, brand and template lock and CRM sync. See "
            "<a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, studio name, "
            "direct number and the kind of work you take on and where.",
            "Add your portfolio, Instagram, Pinterest or Houzz and your consultation booking "
            "link, plus any membership or certification you already show on your website.",
            "Print the QR code on your proposals, your showroom stand and the back of your "
            "existing cards.",
            "Paste the card link into your email signature, add the card to Apple or Google "
            "Wallet, and send the link to the realtors and contractors who refer you.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES30 = [DESIGNERS]
PAGES = PAGES30
