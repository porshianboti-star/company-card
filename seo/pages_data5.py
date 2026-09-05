# -*- coding: utf-8 -*-
"""Batch 5: Uniqode + Mobilo alternatives, and digital vs NFC cards.

Three substantial pages rather than a long tail of near-identical ones —
"Crawled, currently not indexed" in GSC is a value signal, so thin variants
would make that worse, not better.

VERIFIED 2026-07-26 from each vendor's own pricing page:
  Uniqode  free = 1 digital business card, single user, "free forever"; Team
           $6/user/month with a 2-seat minimum; ANNUAL SUBSCRIPTIONS ONLY —
           "We do not offer monthly plans"; Business+ custom; 30-day
           money-back guarantee on paid plans.
  Mobilo   free digital card offered ("Completely Free"); Pro $3/mo, Teams
           $4/mo billed annually (unlimited team members), Business $5/mo;
           sells NFC hardware separately (branded card $19.99, custom $39,
           metal $139, discounted at time of check); no stated seat minimum.

Mobilo is CHEAPER than us on the monthly number and the page says so. The
honest angle is hardware-centric vs software-only, not price.
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

VERIFIED = "July 2026"
FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

REL = [("Best digital business cards compared", "best-digital-business-card.html"),
       ("Free plans compared", "free-digital-business-card-comparison.html"),
       ("For small business", "digital-business-card-for-small-business.html"),
       ("Pricing", "pricing.html")]

# ------------------------------------------------------------- Uniqode
UNIQODE = {
 "slug": "uniqode-alternative.html",
 "crumb": "Uniqode Alternative",
 "title": "Uniqode Alternative — No Annual Lock-In or Seat Minimum | CompanyCard",
 "meta": ("A Uniqode alternative for small teams: monthly billing rather than annual-only, and no "
          "two-seat minimum. Compared from Uniqode's own pricing page, verified July 2026."),
 "og": ("Uniqode alternative — monthly billing instead of annual-only, and no 2-seat minimum."),
 "h1": 'A <span class="gradient-text">Uniqode alternative</span> without the annual commitment',
 "lead": ("Uniqode's paid plans are annual-only and start at two seats. If you'd rather pay monthly, "
          "or you're a single person who doesn't need a second seat, that's the gap CompanyCard fills."),
 "cta_btn": "Create your free card",
 "cta2": ("See the full comparison", "best-digital-business-card.html"),
 "cta_h": "Pay monthly, for exactly the seats you use",
 "cta_p": "Start free — upgrade if and when it earns it.",
 "sections": [],
 "faqs": [
   ("Why look for a Uniqode alternative?",
    "The two structural reasons are billing and seats. As of " + VERIFIED + " Uniqode states it does "
    "not offer monthly plans — paid subscriptions are annual only — and its Team plan requires at "
    "least two seats. For a solo professional or a business that wants to pay month to month, that "
    "is a commitment decision before it is a product decision."),
   ("Does Uniqode have a free plan?",
    "Yes. As of " + VERIFIED + " Uniqode lets you create one digital business card free, for a "
    "single user, and states cards created on the free plan remain free forever. Check "
    "uniqode.com/pricing for current terms."),
   ("How is CompanyCard different?",
    "CompanyCard bills monthly, has no seat minimum, and publishes flat rates: free for one card, "
    "$7.99 a month for Pro ($5.99 billed yearly), $12 per user a month for Business. You can add one "
    "colleague and pay for "
    "one colleague, without an annual commitment."),
   ("Is CompanyCard cheaper than Uniqode?",
    "Not on the headline number for a team: Uniqode's Team plan is $6 per user per month against "
    "our $12 Business, though theirs is annual-only and ours is not. For a single person our Pro is "
    "$7.99 a month, or $5.99 a month billed yearly. Which is cheaper depends entirely on whether you "
    "want to commit for "
    "a year — compare on your own headcount and billing preference."),
   ("What do I get free with CompanyCard?",
    "The free plan includes " + FREE_SPEC),
 ],
 "related": REL,
}
UNIQODE["sections"] = [
  prose("Where Uniqode and CompanyCard actually differ", [
    "Uniqode is a capable platform with a broader QR-code product line, and its free tier — one card "
    "for a single user, free forever as of " + VERIFIED + " — is a reasonable starting point.",
    "The friction people run into is commercial rather than functional. Uniqode states plainly that "
    "it does not offer monthly plans: paid subscriptions are annual, and its Team plan starts at two "
    "seats. If you are a sole trader, or a business that would rather test something for a month "
    "before committing a year of budget, that is the decision point.",
    "CompanyCard bills monthly, has no seat minimum, and publishes its rates. That is the whole of "
    "the difference worth claiming — we are not going to invent feature gaps we have not verified.",
  ]),
  block("Side by side", table(
    ["What to check", "Uniqode (verified " + VERIFIED + ")", "CompanyCard"],
    [["<b>Billing terms</b>", "Annual subscriptions only", "Monthly or annual"],
     ["<b>Team seat minimum</b>", "2 seats on Team", "None"],
     ["<b>Free plan</b>", "1 card, single user, free forever", "1 card, wallet pass, unlimited edits"],
     ["<b>Published paid rate</b>", "$6/user/mo (annual) Team", "$7.99/mo Pro · $12/user/mo Business"],
     ["<b>Money-back</b>", "30-day guarantee on paid plans", "Free plan — try before paying at all"]],
    note='Read from <a href="https://www.uniqode.com/pricing" target="_blank" rel="noopener nofollow">uniqode.com/pricing</a> in '
         + VERIFIED + '. Terms change — check before deciding.')),
]

# ------------------------------------------------------------- Mobilo
MOBILO = {
 "slug": "mobilo-alternative.html",
 "crumb": "Mobilo Alternative",
 "title": "Mobilo Alternative — Software-Only, No NFC Card to Buy | CompanyCard",
 "meta": ("A Mobilo alternative with no NFC hardware: share by QR, link and Apple/Google Wallet. "
          "An honest comparison — Mobilo's paid plans are cheaper, and we say so."),
 "og": ("Mobilo alternative — pure software, no NFC card to buy, ship or replace."),
 "h1": 'A <span class="gradient-text">Mobilo alternative</span> with nothing to buy',
 "lead": ("Mobilo is built around NFC cards it sells you. CompanyCard is software only — QR, link "
          "and wallet. Worth saying up front: Mobilo's paid plans are cheaper than ours."),
 "cta_btn": "Create your free card",
 "cta2": ("Compare free plans", "free-digital-business-card-comparison.html"),
 "cta_h": "No card to order, ship or replace",
 "cta_p": "Share by QR, link and wallet pass — starting free.",
 "sections": [],
 "faqs": [
   ("Is CompanyCard cheaper than Mobilo?",
    "No, and we would rather say so. As of " + VERIFIED + " Mobilo lists Pro at $3 a month and Teams "
    "at $4 a month billed annually, against CompanyCard's $7.99 Pro and $12 per user Business. If the "
    "monthly number is your deciding factor, Mobilo wins it. The difference is what the products "
    "are: Mobilo is built around NFC cards it sells separately, CompanyCard is software only."),
   ("Do I need to buy an NFC card with Mobilo?",
    "Mobilo offers a free digital card and sells physical NFC cards separately — as of " + VERIFIED +
    " its site listed a branded NFC card at $19.99, a custom design at $39 and a metal card at $139, "
    "with discounts running at the time we checked. The hardware is optional, but it is central to "
    "the product. Check mobilocard.com for current pricing."),
   ("Why choose software-only?",
    "Because there is nothing to order for a new hire, nothing to reship when someone loses one, and "
    "nothing that stops working if you change the design. Sharing by QR code, link and wallet pass "
    "reaches every phone with no tap and no accessory. If you like the physical object, that is a "
    "genuine reason to prefer a hardware product instead."),
   ("What does CompanyCard include free?",
    "The free plan includes " + FREE_SPEC),
 ],
 "related": REL,
}
MOBILO["sections"] = [
  prose("The honest comparison", [
    "Mobilo makes a good product, offers a free digital card, and its paid plans are cheaper than "
    "ours — Pro at $3 a month and Teams at $4 billed annually as of " + VERIFIED + ", against our $7.99 "
    "and $12. If price is the deciding factor, that is your answer and you should take it.",
    "What you are choosing between is really two shapes of product. Mobilo is built around NFC cards "
    "it sells separately; the tap is the experience. CompanyCard has no hardware at all — sharing is "
    "QR code, link, Apple or Google Wallet pass and email signature.",
    "That matters most as a business grows. Every new hire on a hardware-centric setup is an order, "
    "a delivery and a replacement when it goes missing; on a software-only setup it is a seat. And "
    "an NFC tap needs the other person's phone to be close, unlocked and NFC-ready, where a QR code "
    "works across a room and a link works in an email.",
  ]),
  block("Two different shapes of product", cards3([
    ("Nothing to order or replace",
     "No cards to buy per person, ship to a new hire, or re-order when one is lost."),
    ("Reaches every phone",
     "QR and link work regardless of NFC support, and from across a table rather than on contact."),
    ("Honest trade-off",
     "You lose the physical object. Some people genuinely want something to hand over — if that is "
     "you, buy the hardware product."),
  ])),
]

# ------------------------------------------------------- digital vs NFC
VSNFC = {
 "slug": "digital-business-card-vs-nfc-card.html",
 "crumb": "Digital Business Card vs NFC Card",
 "title": "Digital Business Card vs NFC Card: Which Do You Actually Need? (2026) | CompanyCard",
 "meta": ("Digital business card vs NFC card compared — how each is shared, what they cost, who "
          "they reach, and when the hardware is genuinely worth buying."),
 "og": ("QR and link vs NFC tap: how digital business cards and NFC cards really differ, and when "
        "hardware is worth it."),
 "h1": 'Digital business card vs <span class="gradient-text">NFC card</span>',
 "lead": ("They are often sold as the same thing. They are not: one is software you share by QR or "
          "link, the other is a physical product you tap. Here is which one actually fits."),
 "cta_btn": "Try the software version free",
 "cta2": ("Compare the apps", "best-digital-business-card.html"),
 "cta_h": "Start with the free software card",
 "cta_p": "If you later want something to tap, an NFC tag can point at the same link.",
 "sections": [],
 "faqs": [
   ("What is the difference between a digital business card and an NFC card?",
    "A digital business card is software — a page with your details that you share by QR code, link "
    "or wallet pass. An NFC card is a physical card or tag containing a chip that opens a link when "
    "tapped against a phone. The NFC card is a way of delivering a digital card, not a different "
    "kind of card: most NFC products open exactly the same sort of page."),
   ("Do I need an NFC card, or is the app enough?",
    "For most people the software is enough, because QR codes and links reach every phone and work "
    "at a distance. NFC is worth buying if you want something physical to hand over, or you share "
    "your card constantly in person and like the tap. It is not required to have a digital card."),
   ("Does NFC work on every phone?",
    "Not reliably. An NFC tap needs the other person's phone to support it, have it enabled and be "
    "unlocked and held close. A QR code or link works on any phone with a camera or a browser, which "
    "is why most digital card platforms use those as the primary sharing method regardless of "
    "whether they also sell hardware."),
   ("Can I use an NFC card with CompanyCard?",
    "CompanyCard does not sell hardware, but if you own an NFC tag or card that lets you write a "
    "custom URL, you can point it at your CompanyCard link. A tap then opens your card, while "
    "everyone else reaches you by QR code or link with no hardware at all."),
   ("Which is cheaper?",
    "Software is generally cheaper because there is nothing to buy per person and nothing to replace. "
    "NFC cards are typically bought individually — vendors in this category list branded cards from "
    "around $20 up to well over $100 for metal versions — and each new employee needs their own."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Digital vs paper", "digital-business-card-vs-paper.html"),
             ("QR code business card", "qr-code-business-card.html"),
             ("For small business", "digital-business-card-for-small-business.html")],
}
VSNFC["sections"] = [
  prose("They are not two competing technologies", [
    "The most useful thing to understand first: an NFC card is a <i>delivery method</i> for a digital "
    "card, not an alternative to one. Tap an NFC business card and it opens a web page with someone's "
    "details — the same kind of page a QR code or a link would open.",
    "So the real question is not \"digital or NFC\". It is: <b>do I want to buy a physical object to "
    "open my card, in addition to the QR code and link I already have?</b>",
  ]),
  block("How they compare in practice", table(
    ["", "Software card (QR, link, wallet)", "NFC card or tag"],
    [["<b>How it's shared</b>", "Scan a code, open a link, show a wallet pass", "Tap the card against a phone"],
     ["<b>Who can receive it</b>", "Any phone with a camera or browser", "Phones with NFC on, unlocked and held close"],
     ["<b>Distance</b>", "Across a room, in an email, on a sign", "Physical contact"],
     ["<b>Cost per person</b>", "A seat, or free", "A card to buy per person, plus replacements"],
     ["<b>New hire</b>", "Add a seat", "Order, wait, ship"],
     ["<b>If you lose it</b>", "Nothing to lose", "Re-order"],
     ["<b>The appeal</b>", "Nothing to carry or replace", "A physical object to hand over"]],
    note="Hardware prices vary by vendor and change often — check the seller's own page. This "
         "comparison is about the two delivery methods, not any single product.")),
  prose("When the hardware is genuinely worth it", [
    "There are real cases for buying an NFC card, and it would be dishonest to pretend otherwise. If "
    "you work a trade-show booth and tap dozens of phones a day, the tap is faster than framing a QR "
    "code. If your work is client-facing in a setting where handing something over matters — "
    "hospitality, luxury retail, high-value sales — the object itself does work that a screen does not.",
    "For most small businesses and self-employed professionals, though, the software covers it. Your "
    "QR code goes on the van, the invoice, the window and your phone screen; your link goes in your "
    "email signature and your social bios; and there is nothing to re-order when you hire someone.",
    "And these are not exclusive. If you already own an NFC tag that accepts a custom URL, point it "
    "at your card link — the tap works for the people who like tapping, and everyone else scans.",
  ]),
  block("Deciding in one minute", checklist([
    ("Do people need to receive it at a distance?", "Signs, emails and shop windows rule out NFC on its own — you need a QR."),
    ("How often do you share in person?", "Dozens a day makes the tap worth buying; a few a week does not."),
    ("How often do you hire?", "Every new person on a hardware setup is an order and a delivery."),
    ("Do you want something to hand over?", "A legitimate reason to buy hardware — just know you're buying the object, not the card."),
  ]), tint=True),
]

PAGES5 = [UNIQODE, MOBILO, VSNFC]
