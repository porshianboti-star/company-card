# -*- coding: utf-8 -*-
"""Batch 25: digital-business-card-for-lawyers.html — a positive profession page.

Picked from Search Console (28 days to 2026-09-24): "best digital business cards
for law firms 2025" appeared with no page on the site written for lawyers. Solo
practitioners and small firms are squarely the small-business / self-employed
ICP, and no existing profession page overlaps (the nearest, notaries, is about
mobile signing work, not legal advice).

Built on what differs for lawyers: clients arrive by referral and read the card
second-hand; the practice areas and jurisdictions a lawyer can take on are the
deciding details; the first contact must not become a channel for confidential
case facts before a conflict check; and lawyer marketing is regulated.

Owner directive 2026-09-23: positive pages about CompanyCard only — no
competitor is named on this page.

Product claims are limited to what pricing.html states today (2026-09-27): free
plan = one card, QR and link sharing, profile/links/socials, Apple and Google
Wallet pass, unlimited updates, free forever, no credit card, and the card
carries a small CompanyCard credit; Pro ($7.99/mo) adds lead capture and
analytics, unlimited links and files, and removes the credit. Paid billing is a
preview.

No invented professional-conduct rules. Advertising, "specialist" wording and
disclaimers are described only as things regulators commonly address, and the
reader is told to check their own bar or law society's rules — they differ by
jurisdiction. Nothing on the page is legal or ethics advice.
"""
from build_pages import table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited updates — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

SLUG = "digital-business-card-for-lawyers.html"

WHY = [
    "Most people hire a lawyer once or twice in their lives, and they rarely start by "
    "searching cold. They ask someone they trust — an accountant, another lawyer who does not "
    "take their kind of matter, a friend who went through the same thing — and they are sent a "
    "name. What arrives is usually a forwarded link or a contact passed on in a message, read "
    "on a phone at a stressful moment. Your card is judged second-hand, before you have spoken.",
    "The question the reader is trying to answer is narrow: does this lawyer handle my kind of "
    "matter, where I am? Practice areas, the jurisdictions you are admitted in and whether you "
    "take on new clients at all are the details that decide it. A card that answers those "
    "first saves both of you a call that was never going to fit.",
    "Referrals between lawyers work the same way. When you pass on a matter you cannot take, "
    "the most useful thing you can send is a link the client can open, save and act on — and "
    "that is also what you want other lawyers to send about you.",
]

INCLUDE = [
    ("Your practice areas, in plain words.",
     "“Family law — divorce, custody, prenuptial agreements” is read faster than a "
     "list of legal terms. Say what you do not take on, too."),
    ("Where you are admitted to practise.",
     "The states, provinces or countries you can act in. Many matters are decided by this "
     "alone."),
    ("Your firm, office address and hours.",
     "Include whether you meet clients in person, by video or both."),
    ("How a first consultation works.",
     "Whether it is free or paid, how long it is, and a booking link if you use one."),
    ("A way to reach the right person.",
     "A direct line, an intake email or your assistant's number — whichever you want a new "
     "enquiry to go to."),
    ("A short line about what not to send yet.",
     "Something like “Please don't send case details until we have spoken” "
     "protects the reader and you until a conflict check is done."),
    ("Any wording your regulator requires.",
     "Some jurisdictions expect a disclaimer or specific language on lawyer marketing. The "
     "card's text is yours to edit, so add what applies."),
]

ROWS = [
    ["Referred by an accountant or adviser",
     "The adviser forwards your link in an email",
     "Your practice areas and where you practise"],
    ["Referred by another lawyer",
     "Your link is passed on because they cannot take the matter",
     "That you take this type of matter and how to book a first call"],
    ["Met at a business or community event",
     "Scans the QR code on your phone",
     "Save-contact button, then your firm and practice areas"],
    ["Prospective client comparing options",
     "Opens the link from your website or directory profile",
     "How a first consultation works and what it costs"],
    ["Existing client, months later",
     "Opens the contact they saved at the start",
     "Your current direct line, office address and hours"],
]

FAQS = [
    ("What should a lawyer put on a digital business card?",
     "Your name and firm, your practice areas in plain words, the jurisdictions where you are "
     "admitted, your office address and hours, how a first consultation works, a direct way to "
     "reach you or your intake team, and any wording your regulator requires on lawyer "
     "marketing."),
    ("Is a digital business card allowed for lawyers?",
     "A card is a way of sharing your contact details, and lawyers use them the same way other "
     "professionals do. What you say on it may count as lawyer advertising where you practise, "
     "and rules on disclaimers, on calling yourself a specialist and on client testimonials "
     "differ between bars and law societies. Check the rules that apply to you before you "
     "publish, and edit the card's text to match them."),
    ("Should prospective clients send me case details through the card?",
     "It is safer not to invite that. Use the card to book a first call or reach your intake "
     "team, and ask people not to send details of their matter until you have spoken. If you "
     "use lead capture, collect contact details only."),
    ("Can a small firm give every lawyer a card?",
     "Yes. Each person can have their own card with their own practice areas and direct line. "
     "For a firm that wants one locked design across everyone, see "
     "<a href=\"digital-business-cards-for-teams.html\">digital business cards for teams</a>."),
    ("Do the people I share it with need an app?",
     "No. The card opens in any browser from a link or a QR code, and the reader saves your "
     "details to their contacts with one tap."),
    ("Is it free?", "Yes. The free plan includes " + FREE_SPEC),
]

REL = [("For small business", "digital-business-card-for-small-business.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
       ("For accountants", "digital-business-card-for-accountants.html"),
       ("Free digital business card", "free-digital-business-card.html")]

LAWYER = {
    "slug": SLUG,
    "crumb": "Digital Business Card for Lawyers",
    "title": "Digital Business Card for Lawyers & Small Law Firms | CompanyCard",
    "meta": ("A digital business card for lawyers and small law firms — show your practice "
             "areas and where you practise, let referred clients book a first consultation, "
             "and edit it any time. Free to start."),
    "h1": 'Digital business card for <span class="gradient-text">lawyers</span>',
    "lead": ("Legal clients usually arrive through someone else's recommendation, and your card "
             "is read before you have spoken. Make it a link that says what you handle, where "
             "you practise and how to book a first call."),
    "cta_btn": "Create your free card",
    "cta2": ("What's in the free plan", "free-digital-business-card.html"),
    "cta_h": "Make the referral easy to act on.",
    "cta_p": "Free forever, no credit card, and the link never changes when your details do.",
    "sections": [
        prose("How lawyers get clients, and where the card is read", WHY),
        block("What a prospective client looks for on a lawyer's card",
              checklist(INCLUDE), tint=True),
        block("Where your card gets opened",
              table(["How the client finds you", "How the card reaches them",
                     "What they need to see first"], ROWS,
                    note="The same link works in every row, and edits reach all of them.")),
        prose("What changes, and why an editable card suits a legal practice", [
            "A practice changes in small steps: you add a practice area, get admitted in "
            "another jurisdiction, move office, change your consultation fee, join or leave a "
            "firm, or close to new matters for a while. Each change makes a printed card "
            "slightly wrong, and a card that is wrong about where you can practise sends the "
            "wrong people to you. With CompanyCard you edit the card once and every link, QR "
            "code and saved copy shows the update.",
            "If you have one card to run, the free plan covers it: one card with QR and link "
            "sharing, your profile, links and socials, and an Apple or Google Wallet pass. The "
            "free card carries a small CompanyCard credit. Pro removes that credit and adds "
            "lead capture and analytics, so you can see whether the link you gave a referral "
            "partner is being opened. See <a href=\"pricing.html\">pricing</a> for the full "
            "plan list.",
        ]),
        block("Setting it up", steps_howto([
            "Open the <a href=\"app/builder.html\">builder</a> and add your name, firm and "
            "title.",
            "Add your practice areas in plain words and the jurisdictions where you are "
            "admitted.",
            "Add a booking link or intake contact for first consultations, a line asking people "
            "not to send case details yet, and any wording your regulator requires.",
            "Put the link in your email signature and send it to the accountants, advisers and "
            "lawyers who refer matters to you, so they can forward it without retyping "
            "anything.",
        ])),
    ],
    "faqs": FAQS,
    "related": REL,
}

PAGES23 = [LAWYER]
PAGES = PAGES23
