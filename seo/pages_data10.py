# -*- coding: utf-8 -*-
"""Batch 10: four more self-employed trades — notary, tutor, cleaner, landscaper.

Same discipline as batch 8: each page must earn its place with trade-specific
substance, not a swapped noun. What is genuinely different per trade is how they
get hired, what a prospect must see before they call, and which one field on the
card is load-bearing.

Product claims limited to what /pricing states: free plan = one card, QR + link,
Apple/Google Wallet pass, unlimited edits, free forever no credit card, carries a
small CompanyCard credit; Pro $8/mo removes the credit; Business $12/user, no seat
minimum. No lead-capture-on-free claim (that is gated behind Pro). No invented
licensing, insurance or regulatory requirements — where rules vary the page says
"check your own regulator / commissioning authority".
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

REL = [("For small business", "digital-business-card-for-small-business.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
       ("Free digital business card", "free-digital-business-card.html"),
       ("QR code business card", "qr-code-business-card.html")]


def profession(slug, crumb, title, meta, h1, lead, why, include_items, faqs, related=None):
    return {
     "slug": slug, "crumb": crumb, "title": title, "meta": meta, "og": meta,
     "h1": h1, "lead": lead,
     "cta_btn": "Create your free card",
     "cta2": ("What's in the free plan", "free-digital-business-card.html"),
     "cta_h": "A card that keeps up with the work",
     "cta_p": "Free forever, no credit card, and your link never changes.",
     "sections": [
        prose("Why it matters in this line of work", why),
        block("What to put on it", checklist(include_items), tint=True),
        block("Setting it up", steps_howto([
          "Open the <a href=\"app/builder.html\">builder</a> and add your name, trade and business.",
          "Add the contact routes clients actually use, plus your booking or quote link.",
          "Add your logo and brand colour so it looks like you, not a template.",
          "Share it by <a href=\"qr-code-business-card.html\">QR code</a>, link or wallet pass — no app needed at the other end.",
        ])),
     ],
     "faqs": faqs, "related": related or REL,
    }


# ------------------------------------------------------------------- Notary
NOTARY = profession(
 "digital-business-card-for-notaries.html", "Digital Business Card for Notaries",
 "Digital Business Card for Notaries & Signing Agents | CompanyCard",
 "A digital business card for notaries and mobile signing agents — carry your commission "
 "details, take same-day signings with one tap, and stay in every title company's contacts.",
 'Digital business card for <span class="gradient-text">notaries</span> &amp; signing agents',
 "Signing work is same-day and referral-fed. Your card has to reach a title company fast, show "
 "your commission at a glance, and still be current when your expiry date rolls over.",
 ["A mobile notary's business is almost entirely repeat and referral — title companies, escrow "
  "officers, real estate agents, attorneys and signing services who book you again when you were "
  "easy to reach last time. The card's real job is to <i>get saved</i> in their phone so the next "
  "same-day request goes to you and not the next name on a list.",
  "The detail that carries the card is your commission. A stranger booking a signing wants to see "
  "your commission number, jurisdiction and expiry, whether you carry E&amp;O insurance, and "
  "whether you handle loan signings or remote online notarization at all. Putting those on the card "
  "means they travel with every share instead of turning into a back-and-forth email.",
  "Commissions expire and coverage changes. A printed card with last year's expiry date quietly "
  "works against you; an editable card shows the current commission everywhere you have already "
  "shared it. Requirements for what a notary may display vary by jurisdiction — follow your own "
  "commissioning authority's rules."],
 [("Your commission number, jurisdiction and expiry.", "The first thing a booker checks; keep the expiry current."),
  ("Whether you carry E&amp;O insurance.", "Many signing services require it — state the amount."),
  ("Loan signings and RON, if you do them.", "Signing agents and remote online notarization are separate asks; say which you cover."),
  ("A direct line and your service radius.", "Same-day signings go to whoever answers and is close enough."),
  ("Your availability.", "Evenings and weekends are much of a mobile notary's value — spell it out."),
  ("A booking or request link.", "Turns a text at 8am into a confirmed 11am signing.")],
 [("What should a notary's digital business card include?",
   "Your commission number, jurisdiction and expiry date, whether you carry E&amp;O insurance and "
   "for how much, whether you handle loan signings and remote online notarization, your service "
   "radius, availability and a direct booking route. Follow your own commissioning authority's "
   "rules on what a notary may display."),
  ("Why does a digital card suit mobile signing work?",
   "Because the work is same-day and comes from people who booked you before. A link opens cleanly "
   "in a text, shows your commission and coverage to a title company that has never met you, and "
   "still works when your commission expiry or insurance has changed since you last shared it."),
  ("Can I show that I handle loan signings or RON?",
   "Yes — add them as fields on the card and edit them whenever your credentials change. Because a "
   "signing agent and a remote online notary are different asks, stating which you cover saves both "
   "of you a wasted call."),
  ("Is it free to start?", "Yes. The free plan includes " + FREE_SPEC)])

# --------------------------------------------------------------------- Tutor
TUTOR = profession(
 "digital-business-card-for-tutors.html", "Digital Business Card for Tutors",
 "Digital Business Card for Tutors & Private Teachers | CompanyCard",
 "A digital business card for tutors — one link that forwards through parent group chats, shows "
 "your subjects and safeguarding checks, and lets a parent book a trial lesson.",
 'Digital business card for <span class="gradient-text">tutors</span>',
 "Tutoring spreads through parents talking to parents. Your card has to survive being forwarded "
 "into a class WhatsApp group and still make a stranger comfortable booking their child in.",
 ["A tutor's best marketing channel is a parent recommending you to another parent, usually by "
  "pasting a link into a group chat. That means the card has to <i>forward well</i>: open cleanly "
  "in a message, and answer a parent's first questions before they have to ask them.",
  "Those questions are specific. Which subjects and levels, in-person or online, and — the one that "
  "decides whether a parent relaxes — whether you hold a background or safeguarding check. Putting "
  "your DBS or equivalent, your qualifications and a couple of results on the card does the "
  "reassuring for you, in a way a paper card handed over at the school gate never could.",
  "Your availability and rates change each term, and a link keeps up. The same card you shared in "
  "September shows this term's slots and prices, so a parent who saved you months ago sees what is "
  "actually open now rather than a number that has moved on."],
 [("Subjects and levels, precisely.", "GCSE maths, SAT prep, primary reading — parents search by exactly this."),
  ("In-person, online, or both.", "And your area if you travel; it filters mismatched enquiries."),
  ("Your background or safeguarding check.", "A DBS or equivalent is the detail that makes a parent comfortable — display whatever your region uses."),
  ("Qualifications and a little proof.", "Grades achieved, a testimonial, exam-board experience."),
  ("A booking link for a trial lesson.", "The one action worth making obvious."),
  ("Rates and current availability.", "Saved once, edited each term — no reprinting.")],
 [("What should a tutor's digital business card include?",
   "The subjects and levels you teach, whether you tutor in person or online, your qualifications, "
   "a background or safeguarding check if you hold one, a couple of results or a testimonial, your "
   "rates and a link to book a trial lesson. Display whatever safeguarding credential your region "
   "uses."),
  ("Why is a digital card good for getting tutoring referrals?",
   "Because most tutoring referrals happen when one parent pastes your details into a group chat. A "
   "link forwards cleanly, opens without an app, and shows your subjects, checks and booking option "
   "to a parent who has never met you — so the recommendation does the introducing for you."),
  ("Can a parent book a lesson from the card?",
   "Yes. Add your scheduling or contact link and it becomes the main action on the card, so a "
   "parent can book a trial while they are still looking at your subjects and results."),
  ("What if my availability changes each term?",
   "Edit the card. Every link and QR code you have already shared shows this term's slots and "
   "rates, so a parent who saved you last term sees what is actually open now."),
  ("Is it really free?", "Yes. The free plan includes " + FREE_SPEC)])

# ------------------------------------------------------------------- Cleaner
CLEANER = profession(
 "digital-business-card-for-cleaners.html", "Digital Business Card for Cleaners",
 "Digital Business Card for Cleaners & Cleaning Businesses | CompanyCard",
 "A digital business card for cleaners — a QR for the door hanger and van, insurance and services "
 "shown up front, and a quote link that turns a flyer into a booking.",
 'Digital business card for <span class="gradient-text">cleaners</span>',
 "Cleaning is won locally and kept by trust. A card that shows you are insured, lists exactly what "
 "you clean, and books a quote in one tap does more work than any flyer.",
 ["Cleaning businesses grow on recurring clients and neighbourhood referrals, and most first "
  "contact is a quote request. The card's job is to turn a flyer, a door hanger or a van sighting "
  "into that request without friction — someone scans a QR, sees what you do and taps to ask for a "
  "price, all before they have talked themselves out of it.",
  "What a prospective client wants to see first is reassurance: that you are insured, what exactly "
  "you clean, and whether you bring your own supplies. Domestic, end-of-tenancy, deep clean and "
  "office work are different jobs — spelling them out means the enquiries you get are the ones you "
  "actually want.",
  "The reprint problem hits cleaners hard, because your number ends up on flyers, door hangers, the "
  "van and every invoice. Change it and all of that is dead. A permanent QR code that points at an "
  "editable card fixes it — you update the details once and everything already out there keeps "
  "working."],
 [("Proof you're insured.", "Public liability reassures a stranger letting you into their home — state it plainly."),
  ("Exactly what you clean.", "Domestic, end-of-tenancy, deep clean, offices — different jobs, different clients."),
  ("A quote or booking link.", "The one action that turns a flyer into a paying job."),
  ("Your area and availability.", "Regular weekly slots, one-offs, short notice — say which you take."),
  ("Whether supplies are included.", "A common first question; answering it saves a call."),
  ("Before-and-after photos.", "End-of-tenancy and deep cleans photograph well and sell themselves.")],
 [("What should a cleaner's digital business card include?",
   "Whether you are insured, exactly what you clean (domestic, end-of-tenancy, deep clean, office), "
   "whether supplies are included, your area and availability, a quote or booking link and a couple "
   "of before-and-after photos. Those answer a new client's first questions before they call."),
  ("How do I use it on flyers, door hangers and the van?",
   "Print the QR code on all of them. Someone scans it, sees your services and insurance, and taps "
   "to request a quote — and you are saved in their phone for the next time they or a neighbour "
   "needs a clean."),
  ("What if my phone number or prices change?",
   "You edit the card and every QR already printed keeps working with the new details. That is the "
   "main reason to put a code on the van and the flyers rather than a bare number."),
  ("Do customers need an app to see it?",
   "No. They scan with the normal phone camera and the card opens in the browser. Requesting a "
   "quote or saving your number is one tap, nothing to install."),
  ("Is it free to start?", "Yes. The free plan includes " + FREE_SPEC)])

# ----------------------------------------------------------------- Landscaper
LANDSCAPER = profession(
 "digital-business-card-for-landscapers.html", "Digital Business Card for Landscapers",
 "Digital Business Card for Landscapers & Gardeners | CompanyCard",
 "A digital business card for landscapers and gardeners — a QR on the truck and yard sign, a "
 "photo portfolio that sells the work, and a quote link neighbours can tap while you're on site.",
 'Digital business card for <span class="gradient-text">landscapers</span> &amp; gardeners',
 "Landscaping sells itself when the work is visible. A card with a QR on the truck and a portfolio "
 "of finished jobs turns the neighbour watching you work into your next quote.",
 ["Landscaping and garden work are advertised in public by definition — you are on someone's front "
  "lawn where the whole street can see the result. The card's job is to catch that: a QR on the "
  "truck, the trailer or a yard sign that a neighbour can scan while you are still working, landing "
  "them on your portfolio and a quote link.",
  "For this trade the load-bearing element is photos. Nobody hires a landscaper from a description; "
  "they hire from a before-and-after of a garden like theirs. A link carries a portfolio a paper "
  "card never could — lawns, planting, patios, tree work, whatever you want more of.",
  "The work is also seasonal, and your card should move with it. Leaf clearance in autumn, "
  "maintenance contracts in spring, hardscaping when the ground is dry — an editable card lets the "
  "same QR on the truck advertise what you actually want to be booked for this month."],
 [("A photo portfolio of finished jobs.", "The single thing that sells landscaping — show gardens like the ones you want more of."),
  ("Exactly what you offer.", "Lawn care, planting, patios and hardscaping, tree work, maintenance — be specific."),
  ("Proof you're insured, and any certifications.", "Reassures a homeowner before machinery turns up — display what you hold."),
  ("A quote link, front and centre.", "So a neighbour can ask for a price while you're on site."),
  ("Your area and seasonal availability.", "Say what you're taking on this season and how far you travel."),
  ("Whether you do one-offs or contracts.", "Weekly maintenance and one-off jobs attract different clients.")],
 [("What should a landscaper's digital business card include?",
   "A photo portfolio of finished work, exactly what you offer (lawn care, planting, patios and "
   "hardscaping, tree work, maintenance), proof you are insured and any certifications, your area, "
   "seasonal availability and a quote link. Photos of gardens like the client's do more than any "
   "description."),
  ("How do I use it on the truck and on jobs?",
   "Put the QR code on the truck, the trailer and a yard sign at each job. A neighbour who likes "
   "what they see scans it, browses your portfolio and taps to request a quote — while you are "
   "still on site and the work is in front of them."),
  ("Why does a photo portfolio matter so much for landscaping?",
   "Because people hire from before-and-afters, not descriptions. A digital card links to a full "
   "gallery a paper card cannot carry, so a prospect can see a garden like their own before they "
   "ever call."),
  ("What if my services change with the season?",
   "Edit the card. The same QR on your truck can advertise leaf clearance in autumn and maintenance "
   "contracts in spring, and every code already out there shows the current version."),
  ("Is it really free?", "Yes. The free plan includes " + FREE_SPEC)])

PAGES10 = [NOTARY, TUTOR, CLEANER, LANDSCAPER]
