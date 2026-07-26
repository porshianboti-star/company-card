# -*- coding: utf-8 -*-
"""Batch 3: the two highest-opportunity clusters research flagged as unowned,
plus four more professions.

- Apple/Google Wallet: "most winnable feature cluster — incumbents are tiny
  players, CompanyCard already ships the feature, and there is no page for it."
  Wallet is on our FREE plan (verified on our own /pricing), which is the fact
  worth leading with.
- How-to: informational queries are disproportionately what AI assistants cite,
  and HowTo schema is infrastructure the site already uses.
- Professions: coaches, insurance agents, salon/barber, accountants — the
  self-employed trades the big platforms cover only in blog posts.

Facts about rivals stay out of these pages unless verified; product claims are
limited to what our own /pricing page states.
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

VERIFIED = "July 2026"
FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

REL_CORE = [("For small business", "digital-business-card-for-small-business.html"),
            ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
            ("Free digital business card", "free-digital-business-card.html"),
            ("QR code business card", "qr-code-business-card.html")]

# ------------------------------------------------------------------- wallet
WALLET = {
 "slug": "digital-business-card-apple-wallet.html",
 "crumb": "Digital Business Card for Apple & Google Wallet",
 "title": "Digital Business Card in Apple Wallet & Google Wallet (Free) | CompanyCard",
 "meta": ("Add your digital business card to Apple Wallet and Google Wallet — included on "
          "CompanyCard's free plan. Open it without unlocking an app, and share it by QR even "
          "with no signal."),
 "og": ("Put your digital business card in Apple Wallet or Google Wallet — included free with "
        "CompanyCard."),
 "h1": 'Your business card in <span class="gradient-text">Apple &amp; Google Wallet</span>',
 "lead": ("A wallet pass is the fastest way to get your card on screen — two taps from a locked "
          "phone, no app to open and no signal required. CompanyCard includes the Apple and Google "
          "Wallet pass on the free plan."),
 "cta_btn": "Create your free card",
 "cta2": ("See what's in the free plan", "free-digital-business-card.html"),
 "cta_h": "Keep your card where your phone already looks",
 "cta_p": "Free forever — wallet pass included, no credit card.",
 "howto_name": "How to add your digital business card to Apple Wallet or Google Wallet",
 "howto": [
   "Create your CompanyCard and fill in your details, links and logo.",
   "Open your own card page on the phone you want the pass on.",
   "Tap Add to Apple Wallet, or Add to Google Wallet on Android.",
   "Confirm, and the pass is saved — double-tap the side button (iPhone) or open Wallet to show your QR code.",
 ],
 "sections": [],
 "faqs": [
   ("Can I add a digital business card to Apple Wallet?",
    "Yes. Open your CompanyCard on your iPhone and tap Add to Apple Wallet. The pass is saved "
    "alongside your boarding passes and tickets, so you can bring up your QR code by double-tapping "
    "the side button without unlocking into an app."),
   ("Does it work with Google Wallet on Android?",
    "Yes. The same card offers Add to Google Wallet on Android, and the pass behaves the same way — "
    "open Wallet and your QR code is there."),
   ("Is the wallet pass included on the free plan?",
    "Yes. CompanyCard's free plan includes " + FREE_SPEC),
   ("Does the wallet pass work without internet?",
    "The pass itself lives on your phone, so you can display your QR code with no signal. The person "
    "scanning it needs a connection to load your card page — so at a venue with poor reception, it "
    "helps that they can still save the scan and open it later."),
   ("Does the pass update when I change my details?",
    "Your card page updates immediately, so anyone who scans the QR always sees current details. If a "
    "pass on your own phone looks out of date, remove and re-add it to refresh the stored copy."),
   ("Do I need an app for any of this?",
    "No. Apple Wallet and Google Wallet are already on the phone, and the person receiving your card "
    "just opens a browser page — there is no CompanyCard app to install on either side."),
 ],
 "related": REL_CORE,
}

WALLET["sections"] = [
  block("Why a wallet pass beats hunting for an app", cards3([
    ("Two taps from a locked phone",
     "Double-tap the side button and your QR is on screen. No unlocking, no searching for an icon, "
     "no waiting for a page to load."),
    ("It works with no signal",
     "Trade shows and basements are where sharing usually fails. The pass is stored on the device, "
     "so your code still displays."),
    ("It sits where people already look",
     "Next to the boarding pass and the coffee card — which means it is still there in three months, "
     "unlike an app they installed once."),
  ])),
  prose("What the pass actually does", [
    "The wallet pass is a shortcut to your card, not a copy of it. It stores your QR code and name "
    "on the phone so you can display them instantly; when someone scans, they load your live card "
    "page with whatever details are current.",
    "That split is the useful part. You can change your number, your role or your links a year from "
    "now and the pass in your pocket still points at the right place — nothing to re-download and "
    "nothing to reprint.",
  ]),
  block("Adding it, step by step", steps_howto([
    "Create your <a href=\"app/builder.html\">CompanyCard</a> and fill in your details, links and logo.",
    "Open your own card page on the phone you want the pass on.",
    "Tap <b>Add to Apple Wallet</b>, or <b>Add to Google Wallet</b> on Android.",
    "Confirm — then double-tap the side button (iPhone) or open Wallet to show your <a href=\"qr-code-business-card.html\">QR code</a>.",
  ]), tint=True),
]

# ------------------------------------------------------------------- how-to
HOWTO = {
 "slug": "how-to-make-a-digital-business-card.html",
 "crumb": "How to Make a Digital Business Card",
 "title": "How to Make a Digital Business Card (Free, iPhone & Android) | CompanyCard",
 "meta": ("How to make a digital business card for free in about five minutes — what to put on it, "
          "how to share it by QR, link or wallet, and how to set it up on iPhone and Android."),
 "og": ("A step-by-step guide to making a free digital business card and sharing it by QR, link or "
        "wallet pass."),
 "h1": 'How to make a <span class="gradient-text">digital business card</span>',
 "lead": ("It takes about five minutes and costs nothing. Here is exactly what to do, what to put on "
          "the card, and how to share it so the other person actually saves you."),
 "cta_btn": "Make yours free",
 "cta2": ("See the free plan", "free-digital-business-card.html"),
 "cta_h": "Five minutes, no credit card",
 "cta_p": "Build it, share it by QR, and edit it whenever things change.",
 "howto_name": "How to make a digital business card",
 "howto": [
   "Pick where your card will live — you need a permanent link and QR code you control.",
   "Add your identity: name, role, business name, photo or logo, and brand colour.",
   "Add only the contact routes you actually answer, plus one clear next step like a booking link.",
   "Add your links: website or portfolio, the socials that matter for your work, and a payment handle if relevant.",
   "Test it on someone else's phone — scan the QR and check that saving your contact takes one tap.",
   "Put the QR and link everywhere: email signature, social bios, invoices, and anything you print.",
 ],
 "sections": [],
 "faqs": [
   ("How do I make a digital business card for free?",
    "Create it on a platform that gives you a permanent link and QR code, add your details, photo or "
    "logo and links, then share it by QR, link or wallet pass. With CompanyCard the free plan "
    "includes " + FREE_SPEC),
   ("How do I make a digital business card on iPhone?",
    "Build the card in your browser, then open it on your iPhone and tap Add to Apple Wallet. You can "
    "then display your QR code by double-tapping the side button, without unlocking into an app."),
   ("How do I make one on Android?",
    "The process is the same in any mobile browser, and on Android you can tap Add to Google Wallet "
    "to keep the pass on your phone for instant access."),
   ("What should I put on a digital business card?",
    "Your name, role and business, a photo or logo, one or two contact routes you actually answer, "
    "the links that prove your work, and one clear next step such as a booking link. Resist adding "
    "everything — the card is a door, not a website."),
   ("Do I need a website first?",
    "No. Many freelancers and small businesses use their card link as their web presence, holding "
    "services, contact details, socials and a booking link in one page they can edit themselves."),
   ("How do people save my card?",
    "They scan your QR code or open your link in any phone browser, then tap once to save you as a "
    "contact. There is nothing for them to install."),
 ],
 "related": [("For small business", "digital-business-card-for-small-business.html"),
             ("Apple & Google Wallet", "digital-business-card-apple-wallet.html"),
             ("Digital vs paper", "digital-business-card-vs-paper.html"),
             ("Free digital business card", "free-digital-business-card.html")],
}

HOWTO["sections"] = [
  prose("Before you start: the one decision that matters", [
    "Almost every regret with digital business cards comes from the same place — the link changed. "
    "If your card lives on a URL you do not control, then every printed QR code, email signature and "
    "social bio you updated becomes wrong the day you move.",
    "So the first question is not which design you like. It is: <b>is this link permanent, and can I "
    "take my captured contacts with me?</b> Answer that and the rest is a five-minute form.",
  ]),
  block("The six steps", steps_howto([
    "<b>Pick where the card lives.</b> You need a permanent link and QR code you control.",
    "<b>Add your identity.</b> Name, role, business, photo or logo, and one brand colour.",
    "<b>Add contact routes you answer.</b> Two is usually plenty — plus one clear next step such as a booking link.",
    "<b>Add your links.</b> Website or portfolio, the socials that matter for your work, a payment handle if relevant.",
    "<b>Test on someone else's phone.</b> Scan the QR; saving your contact should take one tap.",
    "<b>Put it everywhere.</b> <a href=\"email-signature-generator.html\">Email signature</a>, social bios, invoices, and anything you print.",
  ]), tint=True),
  block("What to include — and what to leave off", checklist([
    ("Include: name, role and business.", "The three things someone needs to place you tomorrow."),
    ("Include: one clear next step.", "Book a call, see the work, get a quote. One, not five."),
    ("Include: a photo or logo.", "Recognition is most of what a card is for."),
    ("Leave off: every phone number you own.", "Give the one you answer."),
    ("Leave off: six social icons.", "Two that show your work beat six that show a pulse."),
    ("Leave off: a paragraph about yourself.", "Link to it instead — the card is the door."),
  ])),
  prose("How to share it so it actually lands", [
    "Showing a QR code works best in person: hold up your phone, let them scan with the normal camera "
    "app, and they land on your card without installing anything. A wallet pass makes this faster "
    "still, because you can bring the code up from a locked screen.",
    "Away from people, the link does the work. Put it in your email signature, your social bios, your "
    "invoices and quotes, and on anything physical you print. Because the QR is permanent, a sticker "
    "or a van decal stays correct even after your details change.",
  ]),
]

# --------------------------------------------------------------- professions
def profession(slug, crumb, title, meta, h1_html, lead, why, include_items, faqs):
    return {
     "slug": slug, "crumb": crumb, "title": title, "meta": meta, "og": meta,
     "h1": h1_html, "lead": lead,
     "cta_btn": "Create your free card",
     "cta2": ("What's in the free plan", "free-digital-business-card.html"),
     "cta_h": "A card that keeps up with the work",
     "cta_p": "Free forever, no credit card, and your link never changes.",
     "sections": [
        prose("Why it matters in this line of work", why),
        block("What to put on it", checklist(include_items), tint=True),
        block("Setting it up", steps_howto([
          "Open the <a href=\"app/builder.html\">builder</a> and add your name, role and business.",
          "Add the contact routes clients actually use, plus your booking or enquiry link.",
          "Add your logo and brand colour so it looks like you, not a template.",
          "Share it by <a href=\"qr-code-business-card.html\">QR code</a>, link or wallet pass — no app needed at the other end.",
        ])),
     ],
     "faqs": faqs, "related": REL_CORE,
    }

COACH = profession(
 "digital-business-card-for-coaches.html", "Digital Business Card for Coaches",
 "Digital Business Card for Coaches & Therapists | CompanyCard",
 "A digital business card for coaches, therapists and practitioners — share your approach, link to "
 "booking, and keep your details private-but-reachable. Free plan available.",
 'Digital business card for <span class="gradient-text">coaches &amp; therapists</span>',
 "Clients choose a coach or therapist on trust and fit. Your card should convey both, then make "
 "booking the easiest thing on the page.",
 ["This work is bought after someone reads a few lines and decides you sound like the right person. "
  "That makes the card less about credentials in a list and more about a clear sentence on who you "
  "help and what changes.",
  "It is also a practical way to keep boundaries. You can give clients a booking link and a "
  "professional contact route without handing out a personal mobile number, and change either "
  "without telling everyone.",
  "If you hold accreditations, the card is a sensible place for them — visible to anyone deciding "
  "whether to enquire, without a paragraph of explanation."],
 [("A line on who you help.", "\"ADHD coaching for adults\" is more useful than \"Certified Coach\"."),
  ("Your booking link, prominently.", "The single most valuable element on the page."),
  ("Accreditations you hold.", "Quiet credibility for the person deciding to enquire."),
  ("A professional contact route.", "Keeps your personal number private."),
  ("Whether you work online, in person, or both.", "Filters mismatched enquiries before they arrive.")],
 [("What should a coach's digital business card include?",
   "A one-line statement of who you help and with what, your booking link, any accreditations you "
   "hold, a professional contact route and whether you work online or in person. Lead with the "
   "outcome, not the certification."),
  ("Can I take bookings from it?",
   "Yes — add your scheduling link and a prospective client can book directly from the card instead "
   "of emailing to arrange a time."),
  ("Can I keep my personal number private?",
   "Yes. Put only the contact routes you want used on the card — a work email, a booking link or a "
   "business number. You can change them later without reissuing anything."),
  ("Is it free?", "Yes. The free plan includes " + FREE_SPEC)])

INSURANCE = profession(
 "digital-business-card-for-insurance-agents.html", "Digital Business Card for Insurance Agents",
 "Digital Business Card for Insurance Agents & Brokers | CompanyCard",
 "A digital business card for insurance agents and brokers — carry your licence details, make "
 "quoting one tap, and update your card without reprinting a thing.",
 'Digital business card for <span class="gradient-text">insurance agents</span>',
 "Insurance is sold in the gap between \"I should sort that out\" and actually doing it. A card that "
 "puts a quote request one tap away closes that gap.",
 ["Agents and brokers meet people who are interested but not yet ready. The card's job is to survive "
  "that delay — to still be in the phone, with a working number and a quote link, weeks after the "
  "conversation.",
  "It also carries the compliance furniture neatly. Licence numbers and the lines of business you're "
  "authorised for can sit on the card as fields, so they travel with every share rather than living "
  "on a printed card you've run out of.",
  "Because agents change agencies, territories and product lines, an editable card avoids the "
  "familiar problem of a drawer full of business cards with the wrong number on them. Follow your "
  "own state or regulator's rules on what must be disclosed."],
 [("Licence number and licensed states or lines.", "Add as fields so they appear on every share."),
  ("A quote-request link.", "The one action you want, made obvious."),
  ("Agency name and logo.", "Shows who you represent alongside your own name."),
  ("A direct line people will actually reach.", "Insurance questions arrive at odd hours."),
  ("The lines you write.", "Auto, home, commercial, life — saves mismatched enquiries.")],
 [("What should an insurance agent's digital business card include?",
   "Your name and agency, your licence number and the states or lines you're licensed for, a direct "
   "contact route and a quote-request link. Follow your regulator's rules on what must be disclosed "
   "in communications."),
  ("Can I display my licence number?",
   "Yes — add it as a field on the card so it appears every time you share, rather than only on "
   "printed cards you might run out of."),
  ("What happens if I change agency or territory?",
   "You edit the card and every link and QR code already shared reflects it — no reprint, and no "
   "stale numbers circulating."),
  ("Is it free to start?", "Yes. The free plan includes " + FREE_SPEC)])

SALON = profession(
 "digital-business-card-for-salons.html", "Digital Business Card for Salons & Barbers",
 "Digital Business Card for Salons, Barbers & Stylists | CompanyCard",
 "A digital business card for salons, barbers and stylists — a QR at the chair for rebooking, a link "
 "to your work, and prices you can change without reprinting.",
 'Digital business card for <span class="gradient-text">salons &amp; barbers</span>',
 "The best moment to get rebooked is while the client is still in the chair, happy with the result. "
 "A QR code at the mirror turns that moment into an appointment.",
 ["Salon and barbering work is repeat business, and repeat business depends on the client being able "
  "to find you again — not the shop, you. A card with your booking link puts that in their phone "
  "before they leave.",
  "It is also where your portfolio belongs. Instagram is how clients choose a stylist, so the card "
  "should open it, alongside the price list and the booking page.",
  "Prices and hours change, and reprinting cards each time is a small recurring cost that never "
  "quite feels worth it. Edit the card instead — the QR on the mirror, the window and the receipt "
  "keeps working."],
 [("Your booking link, front and centre.", "Rebooking while they're still delighted is the whole game."),
  ("Instagram or a photo gallery.", "How clients actually decide on a stylist."),
  ("Services and price range.", "Sets expectations and filters the wrong enquiries."),
  ("Which chair or shop you're at.", "Especially if you rent a chair or move around."),
  ("Opening hours.", "Editable, so holiday changes don't need a new print run.")],
 [("How do salons and barbers use a digital business card?",
   "The usual setup is a QR code at the mirror, on the window and on receipts. A client scans it, "
   "sees your work and prices, and books their next appointment — and your details are saved in "
   "their phone for next time."),
  ("Can clients book from the card?",
   "Yes — add your booking link and it becomes the main action on the page, so rebooking happens "
   "before the client leaves."),
  ("What if I move chairs or change prices?",
   "Edit the card. Every QR already printed on a mirror card, window or receipt shows the new "
   "details, so moving shop doesn't invalidate anything."),
  ("Is it really free?", "Yes. The free plan includes " + FREE_SPEC)])

ACCOUNTANT = profession(
 "digital-business-card-for-accountants.html", "Digital Business Card for Accountants",
 "Digital Business Card for Accountants & Bookkeepers | CompanyCard",
 "A digital business card for accountants and bookkeepers — carry your qualifications, make the "
 "first consultation easy to book, and keep details current through every filing season.",
 'Digital business card for <span class="gradient-text">accountants &amp; bookkeepers</span>',
 "Accounting work is referred more than it is advertised. Your card needs to survive being passed "
 "from one client to their business partner — which a link does and a paper card rarely does.",
 ["Most accounting clients arrive by referral, and a referral is someone forwarding your details. A "
  "link forwards cleanly in a message or an email, opens on any phone, and puts your qualifications "
  "and booking page in front of a stranger who was told you're good.",
  "Qualifications matter here more than in most trades — CPA, ACCA, CA, enrolled agent, whichever "
  "applies — and the card is a good place for them to be visible before a first call.",
  "The seasonal rhythm is the other reason to go digital. Deadlines, service lines and capacity "
  "change through the year; the card can say \"taking new clients\" in one month and not the next, "
  "without anything being reprinted."],
 [("Your qualification, after your name.", "CPA, ACCA, CA or equivalent — it does real work here."),
  ("What you actually do.", "Tax returns, bookkeeping, payroll, advisory — clients search by task."),
  ("Who you work with.", "Sole traders, limited companies, contractors — saves mismatched enquiries."),
  ("A consultation booking link.", "The natural first step for a new client."),
  ("Whether you're taking new clients.", "Editable, so it's honest in February and in July.")],
 [("What should an accountant's digital business card include?",
   "Your name with your qualification, the services you offer, the kind of clients you work with, a "
   "consultation booking link and current contact details. Saying whether you're currently taking "
   "new clients saves everyone time."),
  ("Is it good for referrals?",
   "That's its main advantage. A link forwards cleanly in a message or email and opens on any phone, "
   "so when a client recommends you their contact sees your qualifications and can book immediately."),
  ("Can I update it during filing season?",
   "Yes — edit it as often as you like. You can change capacity, services or deadlines and every "
   "link and QR already shared updates."),
  ("Is there a free plan?", "Yes. It includes " + FREE_SPEC)])

PAGES3 = [WALLET, HOWTO, COACH, INSURANCE, SALON, ACCOUNTANT]
