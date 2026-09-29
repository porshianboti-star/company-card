# -*- coding: utf-8 -*-
"""Batch 26: digital-business-card-for-therapists.html — a positive profession page.

Therapists, counsellors and psychologists in private practice are self-employed
by definition and squarely the small-business / self-employed ICP. No existing
page is written for them (therapists appear only as referrers on the
chiropractors page; coaches is a different, unregulated trade).

Built on what differs for a private-practice therapist: people often choose a
therapist privately and slowly, from a doctor's referral, a directory listing
or a friend's recommendation; the deciding details are what you work with,
where you are licensed, session format, fees and insurance, and whether you
have openings; and the card is a public page, so it must never become a channel
for clinical information.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor or directory is named on this page.

Product claims are limited to what pricing.html states today (2026-09-29): free
plan = one card, QR and link sharing, profile/links/socials, Apple and Google
Wallet pass, unlimited updates, free forever, no credit card, and the card
carries a small CompanyCard credit; Pro ($7.99/mo) adds lead capture and
analytics and removes the credit. Paid billing is a preview.

No compliance claims. CompanyCard is NOT described as HIPAA-compliant or as a
place for clinical records or messages; the page says so plainly. Rules on
professional titles and advertising are described only as things licensing
boards commonly address, and the reader is told to check their own board's
rules. Nothing on the page is clinical, legal or ethics advice.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-therapists.html"

WHY = [
    "Choosing a therapist is private and often slow. Someone is given your name by their "
    "doctor, finds you in a directory, or hears about you from a friend — and then they read "
    "about you, sometimes more than once, before they get in touch. Your card is part of that "
    "quiet reading, usually on a phone and often late in the evening.",
    "The questions they are trying to answer are practical: do you work with what I am "
    "dealing with, can you see me where I live, in person or online, what does it cost, do "
    "you take my insurance, and do you have space for new clients. A card that answers those "
    "plainly makes the first message easier to send.",
    "Referrers need the same thing. A doctor, a school counsellor or another therapist who "
    "cannot take a client wants one link they can pass on, which opens without an app and "
    "shows how to book a first call.",
]

INCLUDE = [
    ("Your name, credentials and license type.",
     "Written the way your licensing board expects them to appear."),
    ("Where you are licensed to practise.",
     "The states, provinces or countries you can see clients in, which matters most for "
     "online sessions."),
    ("What you work with, in plain words.",
     "“Anxiety, grief, couples and life transitions” is read faster than a list "
     "of methods. Name the ages or groups you see, too."),
    ("Session format, fees and insurance.",
     "In person, online or both; your fee or fee range; which insurance you accept or "
     "whether you provide receipts for reimbursement."),
    ("Whether you are taking new clients.",
     "A current line about openings or a waitlist saves people an unanswered message. "
     "Because the card is editable, you can change it the day it changes."),
    ("How to book a first call.",
     "A booking link, a phone number or a contact email for new enquiries — whichever you "
     "want first contact to go to."),
    ("A short safety and privacy line.",
     "Something like “Please don't share personal details here. If you are in "
     "crisis, call your local emergency number.” The card is a public page, not a "
     "private channel."),
]

ROWS = [
    ["Referred by a doctor or clinic",
     "The referrer passes on your link or prints the QR code",
     "What you work with, fees and insurance, how to book"],
    ["Referred by another therapist",
     "Your link is sent because they are full or it is not their area",
     "Whether you have openings and your license location"],
    ["Found in a directory or on your website",
     "Opens the link from your profile",
     "Session format and how a first call works"],
    ["Met at a workshop or community talk",
     "Scans the QR code on the last slide or a handout",
     "Save-contact button, then how to book"],
    ["Current client, between sessions",
     "Opens the contact they saved at the start",
     "Your current phone, office address and hours"],
]

FAQS = [
    ("What should a therapist put on a digital business card?",
     "Your name, credentials and license type, where you are licensed to practise, what you "
     "work with in plain words, whether you see clients in person or online, your fees and "
     "insurance, whether you are taking new clients, how to book a first call, and a short "
     "line asking people not to share personal details on the card."),
    ("Can clients send me private information through the card?",
     "They should not. A digital business card is a public contact page, not a secure "
     "messaging or records system, and CompanyCard does not describe itself as one. Use the "
     "card to point people to how you want first contact to happen, and if you use lead "
     "capture, collect contact details only."),
    ("Are there rules about how therapists advertise?",
     "Often, yes. Licensing boards and professional bodies commonly set rules on how titles "
     "and credentials are shown, on testimonials and on advertising claims, and they differ by "
     "profession and location. Check the rules that apply to you, and edit the card's text to "
     "match them."),
    ("Can a group practice give every clinician a card?",
     "Yes. Each clinician can have their own card with their own specialties, license "
     "details and booking link. For a practice that wants one locked design across everyone, "
     "see <a href=\"digital-business-cards-for-teams.html\">digital business cards for "
     "teams</a>."),
    ("Do the people I share it with need an app?",
     "No. The card opens in any browser from a link or a QR code, and the reader saves your "
     "details to their contacts with one tap."),
    ("Is it free?", "Yes. The free plan includes " + FREE_SPEC),
]

REL = [("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
       ("For coaches", "digital-business-card-for-coaches.html"),
       ("For chiropractors", "digital-business-card-for-chiropractors.html"),
       ("Free digital business card", "free-digital-business-card.html")]

THERAPIST = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Therapists",
    "title": "Digital Business Card for Therapists in Private Practice | CompanyCard",
    "meta": ("A digital business card for therapists, counsellors and psychologists in private "
             "practice — show what you work with, where you are licensed, fees and openings, "
             "and let referred clients book a first call. Free to start."),
    "h1": 'Digital business card for <span class="gradient-text">therapists</span>',
    "lead": ("People choose a therapist quietly, often from a referral, and read about you "
             "before they reach out. Give them one link that says what you work with, where you "
             "are licensed, what it costs and how to book a first call."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Make the first message easier to send.",
    "cta_p": "Free forever, no credit card, and the link never changes when your details do.",
    "sections": [
        prose("How clients find a therapist, and where the card is read", WHY),
        block("What a prospective client looks for on a therapist's card",
              checklist(INCLUDE), tint=True),
        block("Where your card gets opened",
              table(["How the client finds you", "How the card reaches them",
                     "What they need to see first"], ROWS,
                    note="The same link works in every row, and edits reach all of them.")),
        prose("What changes, and why an editable card suits a private practice", [
            "A practice changes in small steps: you open or close your caseload, start "
            "offering online sessions, get licensed in another state, change your fee, join an "
            "insurance panel or leave one, or move office. Each change makes a printed card "
            "slightly wrong, and a card that still says you have openings when you do not sends "
            "people a message that goes unanswered. With CompanyCard you edit the card once "
            "and every link, QR code and saved copy shows the update.",
            "If you have one card to run, the free plan covers it: one card with QR and link "
            "sharing, your profile, links and socials, and an Apple or Google Wallet pass. The "
            "free card carries a small CompanyCard credit. Pro removes that credit and adds "
            "lead capture and analytics, so you can see whether the link you gave a referrer is "
            "being opened. See <a href=\"pricing.html\">pricing</a> for the full plan list.",
            "One thing the card is not: a place for clinical information. It is a public page, "
            "so keep intake forms, notes and messages in the systems you already use for "
            "client records.",
        ]),
        block("Setting it up", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, credentials "
            "and practice name.",
            "Add what you work with in plain words, where you are licensed, your session format "
            "and your fees or insurance.",
            "Add a booking link or contact for first calls, a line about current openings, and "
            "a short line asking people not to share personal details on the card.",
            "Put the link in your email signature and directory profile, and send it to the "
            "doctors and colleagues who refer to you, so they can pass it on without retyping "
            "anything.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES24 = [THERAPIST]
PAGES = PAGES24
