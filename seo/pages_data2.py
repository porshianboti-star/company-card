# -*- coding: utf-8 -*-
"""Batch 2: competitor-alternative pages + profession pages.

VERIFIED BY DIRECT FETCH 2026-07-26:
  linqapp.com   — pivoted out of the category entirely. Headline is now
                  "APIs for iMessage, RCS, SMS, and Voice built for Agents".
                  Linq no longer sells digital business cards, which strands
                  its former card users. This is the highest-intent, lowest-
                  competition alternative query in the niche.
  hihello.com/pricing — free = 4 cards incl. email signature, virtual
                  background and wallet, BUT capped at 5 card & badge scans
                  per month. Professional $6/mo. Business $5/user/mo, 5-100
                  users (so a 2-4 person team cannot buy it).
  blinq.me/pricing — Business bills a minimum of 5 team cards.

Profession pages target audience-qualified queries that competitors only cover
in blog posts. Claims stay generic-true (what the card does) — no invented
customer counts, testimonials or industry statistics.
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

VERIFIED = "July 2026"
FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

# ------------------------------------------------------------ Linq alternative
LINQ = {
 "slug": "linq-alternative.html",
 "crumb": "Linq Alternative",
 "title": "Linq Alternative for Digital Business Cards (2026) | CompanyCard",
 "meta": ("Looking for a Linq alternative? Linq has moved on to messaging APIs. CompanyCard is a "
          "digital business card you can move to today — free plan, QR, link and wallet sharing, "
          "no app for the recipient."),
 "og": ("Linq now sells messaging APIs, not digital business cards. Here's how to move your card "
        "to CompanyCard — free plan, permanent link and QR."),
 "h1": 'Looking for a <span class="gradient-text">Linq alternative</span>?',
 "lead": ("Linq's website now sells messaging APIs for developers, not digital business cards. If "
          "you were using a Linq card, here's a straightforward place to move it — free, with a "
          "link and QR code that stay yours."),
 "cta_btn": "Create your free card",
 "cta2": ("Compare all the options", "best-digital-business-card.html"),
 "cta_h": "Move your card in about five minutes",
 "cta_p": "Rebuild it free, then update your link wherever you've shared it.",
 "howto_name": "How to move from Linq to CompanyCard",
 "howto": [
   "Open your existing Linq card and copy your details, links and photo while it still loads.",
   "Create a free CompanyCard and paste them in, adding your logo and brand colour.",
   "Update your link where you control it — email signature, social bios, and any printed QR code.",
   "If you own an NFC tag that lets you set a custom URL, point it at your new CompanyCard link.",
 ],
 "sections": [],
 "faqs": [
   ("Is Linq still doing digital business cards?",
    "As of " + VERIFIED + ", linqapp.com presents itself as a developer messaging platform — its "
    "headline is \"APIs for iMessage, RCS, SMS, and Voice built for Agents\" — not a digital "
    "business card product. If you rely on a Linq card, it is worth having somewhere else to go. "
    "Check Linq's own site for the current status of any card product you hold."),
   ("What is the best Linq alternative?",
    "For an individual or a small business, look for three things: a free plan you can genuinely "
    "use with clients, no app required for the person receiving the card, and a permanent link and "
    "QR code so you never repeat this migration. CompanyCard's free plan covers all three — it "
    "includes " + FREE_SPEC),
   ("Can I keep my NFC tag if I switch?",
    "Usually yes. If your tag or card lets you write a custom URL, you can point it at your "
    "CompanyCard link and a tap will open your new card. Everyone else can reach you by QR code or "
    "link with no hardware at all."),
   ("How do I move my details across?",
    "Copy your details, links and photo from your existing card, paste them into the CompanyCard "
    "builder, then update your link in the places you control — email signature, social bios and "
    "any printed QR. It takes about five minutes."),
   ("Will I have to migrate again later?",
    "Nobody can promise what another company does next, so the honest answer is: choose on "
    "portability. With CompanyCard your link and QR code are permanent, and you can export the "
    "contacts you capture, so you are never locked to us by your own data."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Blinq & HiHello alternative", "blinq-alternative.html"),
             ("Popl alternative", "popl-alternative.html"),
             ("Free digital business card", "free-digital-business-card.html")],
}

# --------------------------------------------------------- HiHello alternative
HIHELLO = {
 "slug": "hihello-alternative.html",
 "crumb": "HiHello Alternative",
 "title": "HiHello Alternative for Small Business & Teams (2026) | CompanyCard",
 "meta": ("A HiHello alternative for small businesses: no 5-user minimum on team plans, no monthly "
          "scan cap on the free card, and published flat pricing. Compared and verified July 2026."),
 "og": ("HiHello alternative for small teams — no 5-user Business minimum, no free-tier scan cap, "
        "published pricing."),
 "h1": 'A <span class="gradient-text">HiHello alternative</span> built for small teams',
 "lead": ("HiHello has a genuinely generous free tier. Where it gets awkward is the two ends: a "
          "monthly scan cap on free, and a Business plan that starts at five users. CompanyCard "
          "has neither."),
 "cta_btn": "Create your free card",
 "cta2": ("See the full comparison", "best-digital-business-card.html"),
 "cta_h": "No minimum, no scan cap",
 "cta_p": "Start free, add a colleague when you actually have one.",
 "sections": [],
 "faqs": [
   ("Is CompanyCard a good HiHello alternative?",
    "It depends which limit is bothering you. HiHello's free plan is generous on card count — four "
    "cards as of " + VERIFIED + ", including an email signature and virtual background. But that "
    "free tier caps card and badge scans at five per month, and its Business plan starts at five "
    "users. CompanyCard has no monthly scan cap on the free card and no seat minimum on team "
    "plans, which is what matters if you hand your card out often or your team is two people."),
   ("Does HiHello have a free plan?",
    "Yes — as of " + VERIFIED + " HiHello's Personal plan is free and includes four cards, a "
    "personal email signature, virtual backgrounds and wallet support, with card and badge scans "
    "capped at five per month. We would rather point you at their pricing page than characterise "
    "it second-hand: check hihello.com/pricing for the current terms."),
   ("What does CompanyCard cost?",
    "Free forever for one card. Pro is $8 per month and removes the CompanyCard credit while adding "
    "unlimited links, custom branding, lead capture and analytics. Business is $12 per user per "
    "month for admin controls, brand lock, CRM sync and SSO — with no minimum number of seats."),
   ("Can a two-person business get a team plan?",
    "With CompanyCard, yes — there is no seat minimum. This is the specific gap worth checking "
    "elsewhere: as of " + VERIFIED + " HiHello's Business plan is sold for 5-100 users and Blinq's "
    "Business plan bills a minimum of five team cards, so very small teams are structurally "
    "excluded from both."),
   ("Do I lose anything by switching?",
    "Be aware of the trade-off rather than surprised by it: CompanyCard's free plan is one card and "
    "carries a small CompanyCard credit, where HiHello's free plan gives you four cards without "
    "one. If free card count is what you optimise for, HiHello wins that column and we will not "
    "pretend otherwise."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Blinq alternative", "blinq-alternative.html"),
             ("For small business", "digital-business-card-for-small-business.html"),
             ("Pricing", "pricing.html")],
}

LINQ["sections"] = [
  prose("What happened to Linq", [
    "If you are searching for a Linq alternative, you probably already found the reason: "
    "linqapp.com now leads with \"APIs for iMessage, RCS, SMS, and Voice built for Agents\". It "
    "is a developer messaging company. The digital business card is no longer the product on the "
    "front door.",
    "That leaves anyone holding a Linq card in an uncomfortable position — your card is the link "
    "you have printed on things and pasted into your email signature, and it now depends on a "
    "product line that is no longer the company's focus. Check Linq's own site for the current "
    "status of anything you hold; this page is simply somewhere to land if you decide to move.",
  ]),
  block("What to look for when you move", cards3([
    ("A link that is permanent",
     "The whole cost of switching is updating your link everywhere. Pick a card whose URL and QR "
     "code never change, so you only pay that cost once."),
    ("A free plan that actually works",
     "You should be able to run a real card, shared with real clients, at $0 — not a countdown "
     "trial that strands you again in fourteen days."),
    ("Your data on the way out",
     "Being able to export the contacts you capture is what stops the next migration being "
     "painful. Portability is the feature that protects you."),
  ])),
  block("Moving across, step by step", steps_howto([
    "Open your existing card and copy your details, links and photo while it still loads.",
    "Create a <a href=\"app/builder.html\">free CompanyCard</a> and paste them in, adding your logo and brand colour.",
    "Update your link where you control it — email signature, social bios, and any printed <a href=\"qr-code-business-card.html\">QR code</a>.",
    "If you own an NFC tag that accepts a custom URL, point it at your new CompanyCard link.",
  ]), tint=True),
]

HIHELLO["sections"] = [
  prose("Where HiHello is strong — and where it isn't", [
    "HiHello makes a good product and its free tier is one of the most generous in the category. "
    "As of " + VERIFIED + " it gives four cards, an email signature, virtual backgrounds and "
    "wallet support at $0. If free card count is your deciding factor, it wins that column.",
    "Two limits push people to look elsewhere. The free plan caps card and badge scans at five per "
    "month, which is easy to hit if you hand your card out at events or on a counter. And the "
    "Business plan is sold for five to one hundred users — so if your team is you and two others, "
    "you cannot buy it at the size you actually are.",
    "CompanyCard is aimed squarely at that second gap: no seat minimum, and no monthly cap on how "
    "often your free card gets scanned.",
  ]),
  block("The differences that decide it", table(
    ["What to check", "HiHello (verified " + VERIFIED + ")", "CompanyCard"],
    [["<b>Free plan card count</b>", "4 cards", "1 card"],
     ["<b>Scan cap on free</b>", "5 card &amp; badge scans per month", "No monthly scan cap"],
     ["<b>Team plan minimum</b>", "Business sold for 5-100 users", "No seat minimum"],
     ["<b>Published pricing</b>", "$6 Professional · $5 per user Business", "$8 Pro · $12 per user Business"],
     ["<b>Branding on free card</b>", "No HiHello credit", "Carries a small CompanyCard credit"]],
    note='Read from <a href="https://www.hihello.com/pricing" target="_blank" rel="noopener nofollow">hihello.com/pricing</a> in '
         + VERIFIED + '. Plans change — check before deciding. CompanyCard figures are our published rates.')),
]

# --------------------------------------------------------------- profession pages
def profession(slug, crumb, title, meta, h1_html, lead, why_paras, include_items, faqs, related):
    return {
     "slug": slug, "crumb": crumb, "title": title, "meta": meta, "og": meta,
     "h1": h1_html, "lead": lead,
     "cta_btn": "Create your free card",
     "cta2": ("What's in the free plan", "free-digital-business-card.html"),
     "cta_h": "Get a card that keeps up with the work",
     "cta_p": "Free forever, no credit card, and your link never changes.",
     "sections": [
        prose("Why it matters in this line of work", why_paras),
        block("What to put on it", checklist(include_items), tint=True),
        block("Setting it up", steps_howto([
          "Open the <a href=\"app/builder.html\">builder</a> and add your name, role and business.",
          "Add the contact routes clients actually use, plus your booking or enquiry link.",
          "Add your logo and brand colour so it looks like you, not a template.",
          "Share it by <a href=\"qr-code-business-card.html\">QR code</a>, link or wallet pass — no app needed at the other end.",
        ])),
     ],
     "faqs": faqs, "related": related,
    }

REL_PROF = [("For small business", "digital-business-card-for-small-business.html"),
            ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
            ("Free digital business card", "free-digital-business-card.html"),
            ("QR code business card", "qr-code-business-card.html")]

REALTOR = profession(
 "digital-business-card-for-realtors.html", "Digital Business Card for Realtors",
 "Digital Business Card for Realtors & Real Estate Agents | CompanyCard",
 "A digital business card for realtors and real estate agents — share by QR at viewings and open "
 "houses, link straight to your listings, and update your details without reprinting anything.",
 'Digital business card for <span class="gradient-text">realtors</span>',
 "At an open house you get one moment to be saved into someone's phone. A QR code they can scan "
 "from across the room does that better than a card that ends up in a coat pocket.",
 ["Real estate runs on being reachable at the exact moment someone decides to act. A digital card "
  "puts your number, your listings and a way to book a viewing one tap away, and it works from a "
  "window display, a yard sign or a phone screen.",
  "It also solves the reprint problem. Agents change brokerages, phone numbers and headshots more "
  "often than most professions — and every one of those changes normally invalidates a box of "
  "printed cards. Here you edit the card and the codes you have already put on signs keep working.",
  "If your state or board requires a licence number in your advertising and communications, you can "
  "add it as a field on the card so it travels with every share. Check your own board's rules for "
  "what must be displayed."],
 [("A photo people recognise.", "Real estate is personal — the headshot is doing work here."),
  ("Brokerage name and logo.", "Shows who you hang your licence with, alongside your own name."),
  ("Licence number if your board requires it.", "Add it as a field so it appears on every share."),
  ("A direct line, not a switchboard.", "Buyers act fast; make calling or texting you one tap."),
  ("A link to live listings.", "The one thing a prospect actually wants to look at next."),
  ("A booking link for viewings.", "Turns interest into a diary entry before it cools.")],
 [("What should a realtor's digital business card include?",
   "Your name, photo, brokerage and logo, a direct phone number, a link to your current listings "
   "and a way to book a viewing — plus your licence number if your board requires it in "
   "communications. Keep it to what a buyer needs in the ten seconds after they meet you."),
  ("How do I use it at an open house?",
   "Display the QR code — on a sign, a tablet or your phone — and let visitors scan it. Their "
   "phone opens your card in the browser and saves your details in one tap, with no app to "
   "install and no sign-in sheet to decipher later."),
  ("What happens when I change brokerage?",
   "You edit the card. Every QR code and link you have already handed out, printed on a sign or "
   "put in your email signature updates to the new details automatically — no reprint."),
  ("Is it free for a single agent?",
   "Yes. The free plan includes " + FREE_SPEC)],
 REL_PROF)

CONSULTANT = profession(
 "digital-business-card-for-consultants.html", "Digital Business Card for Consultants",
 "Digital Business Card for Consultants & Coaches | CompanyCard",
 "A digital business card for consultants and coaches — lead with your positioning, link to your "
 "work and let prospects book you from the same page. Free plan, no app for the recipient.",
 'Digital business card for <span class="gradient-text">consultants &amp; coaches</span>',
 "You are selling judgement, so your card has one job: make it easy to believe you and easy to "
 "book you. One link does both.",
 ["Consulting and coaching are bought on credibility. The card that works is not the one that "
  "lists a job title — it is the one that says in a line what you help people do, then puts the "
  "proof and the calendar link right underneath.",
  "Because independent practices change shape constantly — new niche, new rates, new company name "
  "— an editable card matters more here than almost anywhere. Everything you handed out last year "
  "should point at what you do now.",
  "It is also the natural home for the things you would otherwise have to email: a one-page "
  "overview of your services, a case study, and the booking link that turns a conversation into "
  "a scheduled call."],
 [("A one-line positioning statement.", "\"Ops consultant for scaling e-commerce teams\" beats \"Consultant\"."),
  ("A link to proof.", "Case studies, results or a short portfolio — whatever earns the reply."),
  ("A booking link.", "Let a warm prospect put time in your diary while they are still warm."),
  ("LinkedIn, if that is where your credibility lives.", "For most B2B practices it is."),
  ("A clean, restrained design.", "Understatement reads as senior. Resist adding everything.")],
 [("What makes a good consultant's business card?",
   "A one-line statement of what you help clients do, a link to proof of that, and a way to book "
   "you — in that order. Contact details matter, but they are not what converts a conversation "
   "into a project."),
  ("Can I add a Calendly or booking link?",
   "Yes. You can add any booking or calendar link to the card, so a prospect can schedule a call "
   "directly instead of emailing to arrange one."),
  ("Is the free plan enough for a solo consultant?",
   "For many, yes. The free plan includes " + FREE_SPEC + " Pro adds custom branding, unlimited "
   "links and lead capture if you want the card to look fully white-labelled."),
  ("What if I change my niche or rates?",
   "You edit the card and every link and QR code you have already shared reflects it. Independent "
   "practices change direction often; the card should not need reprinting when they do.")],
 REL_PROF)

CONTRACTOR = profession(
 "digital-business-card-for-contractors.html", "Digital Business Card for Contractors",
 "Digital Business Card for Contractors & Tradespeople | CompanyCard",
 "A digital business card for contractors, builders and tradespeople — a QR code for your van and "
 "quotes, a tap to call, and details you can change without reprinting a thing.",
 'Digital business card for <span class="gradient-text">contractors &amp; trades</span>',
 "Put the QR code on the van, the quote and the job sign. When someone wants the work done, they "
 "scan it and you are in their phone — no fumbling for a pen.",
 ["Trade work is won on being the one who is easy to reach when something breaks. A digital card "
  "makes calling you a single tap, and it puts your work photos and reviews right next to the "
  "phone number.",
  "The reprint problem is sharper here than anywhere. Van livery, yard signs, quote templates and "
  "invoice footers all carry your details — and all of them are expensive to change. Put a "
  "permanent QR code on them instead and edit the card when your number, service area or "
  "certifications change.",
  "If you hold licences, insurance or trade certifications, the card is a sensible place to keep "
  "them visible, so a homeowner can see them before they ask."],
 [("A tap-to-call number, front and centre.", "Most trade enquiries start as a phone call."),
  ("What you actually do, in plain words.", "\"Emergency plumbing, Leeds and north\" — not \"quality solutions\"."),
  ("Photos of finished work.", "The fastest trust signal there is in the trades."),
  ("Licences, insurance and certifications.", "Add the ones you hold so homeowners see them up front."),
  ("A link to reviews.", "Where your existing customers already vouched for you."),
  ("Your service area.", "Saves both of you a call that was never going to work.")],
 [("How do contractors use a digital business card?",
   "The common setup is a QR code on the van, on yard signs and on quotes and invoices. A "
   "homeowner scans it, sees your work, licences and reviews, and taps once to call you — and "
   "your details are saved in their phone for the next job."),
  ("What if my phone number or service area changes?",
   "You edit the card. Every QR code already printed on your van, signs or paperwork keeps working "
   "and shows the new details — which is the whole reason to use a code rather than printed text."),
  ("Can I show my licence and insurance details?",
   "Yes — add them as fields on the card so they are visible before a customer has to ask. Display "
   "whatever your local licensing rules require."),
  ("Do my customers need an app?",
   "No. They scan the code with the normal camera app and your card opens in the browser. Saving "
   "your number is one tap. Nothing to install.")],
 REL_PROF)

PHOTOGRAPHER = profession(
 "digital-business-card-for-photographers.html", "Digital Business Card for Photographers",
 "Digital Business Card for Photographers | CompanyCard",
 "A digital business card for photographers — link straight to your portfolio and Instagram, take "
 "enquiries, and share it by QR at shoots and weddings. Free plan available.",
 'Digital business card for <span class="gradient-text">photographers</span>',
 "Your card should look as considered as your work — and it should open your portfolio, not "
 "describe it.",
 ["Photography is bought with the eyes. The job of the card is to get someone from \"who shot "
  "this?\" to looking at your gallery in one tap, which a link does and a printed card does not.",
  "It is also how you get booked at the moment of maximum enthusiasm. At a wedding or an event, "
  "guests who liked what they saw can scan a code, see the portfolio and land on your enquiry "
  "form before the evening is over.",
  "Keep the card itself light and typographic. Let the portfolio carry the images — the card is "
  "the door, not the gallery."],
 [("A link to the portfolio, above everything.", "It is the only thing that decides the booking."),
  ("Instagram, prominently.", "Still where most photography clients browse and verify."),
  ("An enquiry or booking link.", "Catch interest while the shoot is still fresh."),
  ("Your studio mark or wordmark.", "Cleanly placed — restraint reads as taste here."),
  ("The kind of work you take.", "Weddings, portraits, product — saves mismatched enquiries.")],
 [("What should a photographer's digital business card include?",
   "A link to your portfolio, a prominent Instagram link, an enquiry or booking link, your studio "
   "mark and a line on the kind of work you take. Keep the card light and let the portfolio carry "
   "the images."),
  ("How do I share it at a wedding or event?",
   "Show the QR code on your phone, a small print or a card at the table. Guests scan it with "
   "their camera app, land on your portfolio and can enquire — no app, and nothing for you to "
   "carry a box of."),
  ("Can I match it to my brand?",
   "Yes. You can set your brand colour and add your logo or wordmark. Pro adds fuller custom "
   "branding and removes the CompanyCard credit if you want it completely white-labelled."),
  ("Is it really free?",
   "Yes. The free plan includes " + FREE_SPEC)],
 REL_PROF)

PAGES2 = [LINQ, HIHELLO, REALTOR, CONSULTANT, CONTRACTOR, PHOTOGRAPHER]
