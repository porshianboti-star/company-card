# -*- coding: utf-8 -*-
"""Batch 35: digital-business-card-for-handymen.html — a positive profession page.

Why this page: every backlog profession and feature page already exists and
the comparison re-verify is next due ~2026-11-01. GSC (28 days to 10/23) shows
no un-served query gap that a positive page can honestly fill: the vCard
cluster (business vcard 42 @ 46, qr code vcard format 16 @ 42) is already
served by vcard-qr-code.html, open-vcf-file.html and electronic-business-
card.html; "digital business card for field sales" (29 @ 50.7) stays with the
sales-teams page per the 10-19 decision; "most secure digital business card"
(22 @ 45.8) waits on owner-stated security facts. Handymen are the
archetypal self-employed small business (one person, one van, hired on
word of mouth and repeat work); no page served them and the word does not
appear on any existing trade page (contractors, electricians, plumbers,
landscapers, cleaners), so there is nothing to cannibalise. Coverage page,
not query-driven.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page. No prices are printed. No licensing or
insurance rule is asserted: handyman licensing differs by state, county and
city, and some jobs are reserved for licensed electricians or plumbers, so
the page tells the reader to show whatever their own rules require.

Product claims are limited to what pricing.html / features.html / facts.py
state today (2026-10-25): free = one card, QR and link sharing, profile, links
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

SLUG = "digital-business-card-for-handymen.html"

WHY = [
    "A handyman gets hired the moment something breaks. The homeowner is not researching; they "
    "are looking for the number of someone they trust, and the fastest way to be that someone is "
    "to already be saved in their phone. A paper card goes in a drawer. A card that was saved to "
    "their contacts in one tap comes up when they type the first three letters of your name.",
    "The second way a handyman gets hired is a neighbour asking “who did your fence?” The answer "
    "used to be a half-remembered name. With a digital card it is a link forwarded in the same "
    "message, opening on your services, your photos and a tap-to-call button, with no app for "
    "the person receiving it.",
    "And a handyman's details change more than most: a new number, a new service area after a "
    "move, drywall and tiling added to the list, a new insurance certificate. A printed card is "
    "wrong the week that happens. A digital card is edited once, and every QR code on the van, "
    "the invoices and the door hangers you have already handed out shows the current version.",
]

INCLUDE = [
    ("The jobs you take and the ones you do not.",
     "“Repairs, assembly, painting, drywall, fixtures and small carpentry — no roofing or gas” "
     "answers the first question a homeowner has, and saves the calls you would turn down."),
    ("Your service area.",
     "The towns or neighbourhoods you cover, so a forwarded card does not bring enquiries from "
     "an hour away."),
    ("Tap to call and tap to text.",
     "Most handyman jobs start with a photo of the problem sent by text. Make the number one tap "
     "and say which you prefer."),
    ("Photos of finished work.",
     "On the free plan the card carries your profile, links and socials, so link your Google "
     "Business Profile gallery, Facebook page or Instagram. Pro adds unlimited links and files, "
     "so a before-and-after sheet can sit on the card itself."),
    ("Where your reviews live.",
     "A link to your Google reviews, Nextdoor or whichever page your customers already use. "
     "CompanyCard does not host or verify reviews — link to the ones you have."),
    ("Insurance and licensing, as your own rules require.",
     "Handyman licensing differs by state, county and city, and some work is reserved for "
     "licensed electricians or plumbers. Show whatever your jurisdiction and your insurer "
     "expect, exactly as you show it on your quotes — CompanyCard does not check or supply it."),
]

ROWS = [
    ["End of a job, at the door",
     "QR code on your phone, or the link sent with the invoice",
     "Your number saved before you have driven off, for the next thing that breaks"],
    ["Neighbour asking who did the work",
     "Your customer forwards the card link in a message",
     "What you do, your area and your photos, before they decide to text you"],
    ["Van, truck or trailer",
     "QR code on the rear door, big enough to scan from the pavement",
     "A way to save you while you are up a ladder, without flagging you down"],
    ["Door hangers, flyers and local noticeboards",
     "The QR code printed once, never reprinted",
     "Current services and a number that still works when the flyer is six months old"],
    ["Property managers and landlords",
     "The card link in your email signature and quotes",
     "Your insurance details and a direct line for the tenant's emergency"],
]

FAQS = [
    ("What should a handyman's digital business card include?",
     "The jobs you take and the ones you do not, your service area, tap-to-call and tap-to-text "
     "numbers, photos of finished work, a link to where your reviews live, and whatever "
     "insurance or licensing information your own state, county, city and insurer expect you to "
     "show."),
    ("Do my customers need an app to open the card?",
     "No. The card opens in any phone browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("What happens to the QR code on my van when I change my number or add a service?",
     "Nothing needs repainting or reprinting. The QR code and the link point to your live card, "
     "so you edit the number or the service list once and every van sticker, invoice and door "
     "hanger you have already given out shows the new details."),
    ("Can I show photos of my work on the card?",
     "Yes. On the free plan the card carries your profile, links and socials, so your Google "
     "Business Profile gallery, Facebook page or Instagram are one tap away. Pro adds unlimited "
     "links and files, so a before-and-after sheet can sit on the card itself."),
    ("Is it free for a self-employed handyman?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For contractors", "digital-business-card-for-contractors.html"),
       ("For plumbers", "digital-business-card-for-plumbers.html"),
       ("For electricians", "digital-business-card-for-electricians.html"),
       ("For landscapers", "digital-business-card-for-landscapers.html")]

HANDYMEN = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Handymen",
    "title": "Digital Business Card for Handymen — Saved in One Tap | CompanyCard",
    "meta": ("A digital business card for handymen and home repair pros — a QR code for the van and "
             "the invoice, tap to call or text, photos of your work, and details you can change "
             "without reprinting a thing. Free to start, no app for your customers."),
    "h1": 'Digital business card for <span class="gradient-text">handymen</span>',
    "lead": ("The next job comes from the last customer, or their neighbour. Give them one card "
             "that saves your number in a tap, forwards in a message and stays current when your "
             "services, area or number change."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Be the number they already have.",
    "cta_p": "Free forever, no credit card, and the QR code on your van keeps working when your details change.",
    "sections": [
        prose("How a handyman gets the next job, and what the card has to do", WHY),
        block("What a handyman's card should carry", checklist(INCLUDE), tint=True),
        block("Van, invoice, door hanger: where a handyman's card gets opened",
              table(["Where it is seen", "How it is shared", "What the other person needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free, Pro or Business for handymen", [
            "A self-employed handyman can start on the free plan: one card with a QR code and "
            "sharing link, profile, links and socials, and an Apple or Google Wallet pass, with "
            "no credit card. The free card carries a small CompanyCard credit.",
            "Pro is for when the card should collect as well as show: lead capture, so a "
            "homeowner can send you their address and the job from your card, analytics on "
            "views and saves, unlimited links and files for a before-and-after sheet or your "
            "insurance certificate, custom branding so the card matches the van, and no credit. "
            "A handyman business with a few people on the road can put everyone on the same "
            "branded card on the Business plan, which has no seat minimum and adds central "
            "admin, brand and template lock and CRM sync. See "
            "<a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name or business "
            "name, your number, the jobs you take and the area you cover.",
            "Add links to your Google Business Profile, Facebook page or Instagram, and whatever "
            "insurance or licensing information your own rules require.",
            "Print the QR code on the van, your invoices and quotes, and any door hangers or "
            "flyers you already use.",
            "Paste the card link into your email signature and your text-message replies, and "
            "add the card to Apple or Google Wallet so it is one swipe away at the door.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES31 = [HANDYMEN]
PAGES = PAGES31
