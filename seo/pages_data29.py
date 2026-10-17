# -*- coding: utf-8 -*-
"""Batch 32: digital-business-card-for-property-managers.html — a positive profession page.

Why this page: every backlog profession page already exists, and the
comparison re-verify is next due ~2026-11-01. Independent property managers
and small letting / property-management firms are small-business owners whose
work runs on being reachable by three groups at once — owners, tenants and
the contractors who fix things — which is the ICP; no page served them.
Property managers appear only as *clients* on the cleaners, contractors,
electricians and landscapers pages, so this page is written from the
manager's side (owners, tenants, vendors) and does not compete with those.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page. No prices are printed. No legal, licensing
or tenancy-law claim is made: the page tells managers to show whatever
licence or registration details their own jurisdiction expects, without
saying what that is.

Product claims are limited to what pricing.html and features.html state today
(2026-10-17): free = one card, QR and link sharing, profile/links/socials,
Apple and Google Wallet pass, unlimited edits, no credit card, and the card
carries a small CompanyCard credit. Pro adds unlimited links and files, custom
branding and themes, lead capture and analytics, and removes the credit.
Business adds central admin, brand and template lock, CRM sync, no seat minimum.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-property-managers.html"

WHY = [
    "A property manager is the one contact three different groups need at short notice: the "
    "owners whose properties you look after, the tenants who live in them, and the contractors "
    "you send to fix things. Each of them needs a different link from you — a portal, a "
    "maintenance request form, an emergency number — and each of them loses the paper card.",
    "A digital card puts all of those on one page. A tenant scans the QR code on the welcome "
    "pack or the noticeboard and saves you to their phone in one tap; an owner gets the same "
    "link in an email; a contractor has your direct number before they reach the door.",
    "Managers' details change more than most: a new office number, a new portal or booking "
    "link, a new emergency line, a property added to the portfolio. A printed card in every "
    "welcome pack is wrong the day that happens. A live card is edited once, and every QR code "
    "and link you have already handed out shows the new details.",
]

INCLUDE = [
    ("Who you manage for and where.",
     "“Residential lettings and block management in the north of the city” tells an owner in "
     "a second whether you cover their property."),
    ("Your business name and logo, or your own name if you work independently.",
     "With your website, so an owner can check who you are before they call."),
    ("A tenant link and an emergency line.",
     "Your maintenance request form or tenant portal, and the number to call out of hours, "
     "labelled so nobody uses the wrong one."),
    ("An owner link.",
     "A booking link for a valuation or first meeting, or the owner portal you already use."),
    ("Any licence or registration details you are expected to show.",
     "Whatever your jurisdiction or professional body asks for — CompanyCard does not check "
     "or supply these, so add them exactly as you show them elsewhere."),
    ("A direct number and an email address.",
     "For the contractors and owners who need you rather than a form."),
]

ROWS = [
    ["New tenant moves in",
     "QR code in the welcome pack or on the move-in checklist",
     "Your emergency line and the maintenance request link"],
    ["Owner enquiry or valuation",
     "The card link in your reply email",
     "Who you are, what you manage and a way to book a meeting"],
    ["Viewing or property inspection",
     "QR code on your phone, saved in one tap",
     "Your direct number in their contacts for next time"],
    ["Contractor sent to a job",
     "The card link in the job message",
     "Who sent them and how to reach you on site"],
    ["Communal noticeboard or entrance",
     "Printed QR code on a notice",
     "The current contact details, even after they change"],
]

FAQS = [
    ("What should a property manager's digital business card include?",
     "Who you manage for and where, your business name and logo or your own name, a tenant link "
     "such as a maintenance request form or portal, an emergency number labelled as such, a "
     "booking link for owners, any licence or registration details you are expected to show, and "
     "a direct number and email."),
    ("Can tenants and owners see different links on one card?",
     "They see the same card, so label each link for who it is for — for example “Tenants: report "
     "a repair” and “Owners: book a valuation”. On the free plan you add your profile, links and "
     "socials; Pro adds unlimited links and files."),
    ("What happens to the QR codes I have already handed out when my number changes?",
     "Nothing needs reprinting. The QR code and link point to your live card, so you edit the "
     "card once and every welcome pack, notice and email you have already sent shows the new "
     "details."),
    ("Do tenants need an app to open my card?",
     "No. The card opens in any browser from a QR code or a link, and saving you to their "
     "contacts is one tap. Only you need an account."),
    ("Is it free for an independent property manager?",
     "Yes. The free plan includes " + FREE_SPEC + " Lead capture, analytics, custom branding "
     "and unlimited links and files are part of Pro."),
]

REL = [("For realtors", "digital-business-card-for-realtors.html"),
       ("For contractors", "digital-business-card-for-contractors.html"),
       ("For cleaners", "digital-business-card-for-cleaners.html"),
       ("For small business", "digital-business-card-for-small-business.html")]

MANAGERS = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Property Managers",
    "title": "Digital Business Card for Property Managers — Owners & Tenants | CompanyCard",
    "meta": ("A digital business card for property managers — one QR code and link for owners, "
             "tenants and contractors, with your emergency line and repair link, and details that "
             "stay current. Free to start, no app needed."),
    "h1": 'Digital business card for <span class="gradient-text">property managers</span>',
    "lead": ("Owners, tenants and contractors all need to reach you, often in a hurry. Give them "
             "one card they can scan from a welcome pack or a noticeboard, that saves you in a "
             "tap and stays right when your numbers change."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "One card for every owner, tenant and contractor.",
    "cta_p": "Free forever, no credit card, and the link keeps working when your details change.",
    "sections": [
        prose("Why a property manager's contact details matter more than most", WHY),
        block("What a property manager's card should carry", checklist(INCLUDE), tint=True),
        block("Where a property manager's card gets opened",
              table(["Where it is seen", "How it is shared", "What the other person needs first"],
                    ROWS,
                    note="Every row opens the same live card, so one edit reaches all of them.")),
        prose("Free, Pro or Business for property managers", [
            "An independent manager can start on the free plan: one card with a QR code and "
            "sharing link, profile, links and socials, and an Apple or Google Wallet pass, with "
            "no credit card. The free card carries a small CompanyCard credit.",
            "Pro is for when the card should collect as well as share: lead capture, so a "
            "landlord looking for a manager can send their details from your card, analytics on "
            "views and saves, unlimited links and files, custom branding and themes, and no "
            "credit. A firm can put every manager on the same branded card on the Business plan, "
            "which has no seat minimum and adds central admin, brand and template lock and CRM "
            "sync. See <a href=\"pricing.html\">pricing</a> for the current rates.",
        ]),
        block("Setting up your card in ten minutes", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, business name, "
            "direct number and the areas and property types you manage.",
            "Add your tenant link and emergency number, an owner booking link, and any licence "
            "or registration details you are expected to show — label each link for who it is for.",
            "Print the QR code in your welcome packs and on communal notices.",
            "Paste the card link into your email signature, add the card to Apple or Google "
            "Wallet, and send the link to your owners and regular contractors.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES29 = [MANAGERS]
PAGES = PAGES29
