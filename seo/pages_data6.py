# -*- coding: utf-8 -*-
"""Batch 6: own the "best virtual business card / best virtual card" cluster.

Audited 2026-07-26: "best virtual business card" and "best virtual card" appear
on ZERO pages, while "best digital business card" appears on 10. The site has
virtual-business-card.html (a what-is/how-to page) but nothing ranked at the
comparison intent for the *virtual* phrasing.

ANTI-CANNIBALISATION: this page must not duplicate best-digital-business-card
.html (a vendor matrix) or virtual-business-card.html (definitional/how-to).
Its distinct angle is the buyer's actual question behind "best virtual card" —
*which one makes me look professional* — so it is organised as criteria for a
card that reads as professional, with a shortlist by use case rather than a
second copy of the vendor matrix. It links to the matrix for the spec table.

Competitor facts verified 2026-07-26 from each vendor's own pricing page (see
pages_data.py / pages_data5.py headers). Nothing new is claimed here.
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

VERIFIED = "July 2026"
FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

BEST_VIRTUAL = {
 "slug": "best-virtual-business-card.html",
 "crumb": "Best Virtual Business Card",
 "title": "Best Virtual Business Card for Small Business & Professionals (2026) | CompanyCard",
 "meta": ("The best virtual business card for small business owners and self-employed "
          "professionals in 2026 — what makes one look professional, which to pick for your "
          "situation, and an honest look at the free plans. Verified July 2026."),
 "og": ("How to pick the best virtual business card if you want to look professional — criteria, "
        "a shortlist by use case, and honest notes on the free plans."),
 "h1": 'The best <span class="gradient-text">virtual business card</span> for working like a pro',
 "lead": ("If you searched for the best virtual card, you probably don't want a feature list — you "
          "want the one that makes you look established. Here are the criteria that actually "
          "decide that, and which option fits which situation."),
 "cta_btn": "Create your free card",
 "cta2": ("See the full spec comparison", "best-digital-business-card.html"),
 "cta_h": "Look the part from the first handshake",
 "cta_p": "Build a professional virtual card free — no credit card, no countdown.",
 "howto_name": "How to choose the best virtual business card",
 "howto": [
   "Decide whether the person receiving it needs an app — if they do, rule it out.",
   "Check the free plan's real limits: card count, monthly scan caps and whether a wallet pass is included.",
   "Check the smallest team you can pay for, because several plans bill a five-seat floor.",
   "Confirm the link and QR code are permanent so you never have to reprint or re-share.",
   "Make one, send it to a colleague's phone, and count the taps until your contact is saved.",
 ],
 "sections": [],
 "faqs": [
   ("What is the best virtual business card?",
    "For small business owners and self-employed professionals, the best virtual business card is "
    "the one with a free plan you can genuinely use with clients, no app required for the person "
    "receiving it, a permanent link and QR code, and no seat minimum if you later add someone. "
    "CompanyCard is built for exactly that case; its free plan includes " + FREE_SPEC),
   ("What is the best free virtual business card?",
    "On free card count, HiHello leads with four and Blinq gives two, both without a vendor "
    "branding line as of " + VERIFIED + " — we won't pretend otherwise. CompanyCard's free plan is "
    "one card carrying a small CompanyCard credit, but it includes an Apple and Google Wallet pass "
    "and has no monthly cap on scans, where HiHello's free tier caps card and badge scans at five "
    "per month. See our full free-plan comparison for the fine print."),
   ("What makes a virtual business card look professional?",
    "Four things, in order: your own logo and brand colour rather than a stock template; a photo "
    "that looks deliberate; only the contact routes you actually answer; and one clear next step "
    "such as a booking link. A cluttered card with six social icons and three phone numbers reads "
    "as less professional, not more."),
   ("Is a virtual business card better than a paper one for a small business?",
    "For most small businesses, yes — mainly because it never goes out of date. You change your "
    "number, prices or logo once and every QR code you've already printed on a van, a window or an "
    "invoice shows the new details. Some people still carry a few paper cards for occasions that "
    "call for handing something over."),
   ("Do I need to pay to look professional?",
    "Not to start. A free card with your own logo, brand colour and a booking link already looks "
    "established. Paying mainly buys removing the vendor's credit line, custom branding and "
    "analytics — worth it once the card is earning you work, not before."),
   ("Is 'virtual business card' the same as 'digital business card'?",
    "Yes — virtual, digital and electronic business card all describe the same thing: a shareable "
    "card that lives on a link rather than on paper. Vendors use the terms interchangeably, so "
    "search whichever phrase you like and compare the same way."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Free plans compared", "free-digital-business-card-comparison.html"),
             ("Virtual business card", "virtual-business-card.html"),
             ("For small business", "digital-business-card-for-small-business.html")],
}

BEST_VIRTUAL["sections"] = [
  prose("What people actually mean by \"best\"", [
    "Almost nobody searching for the best virtual business card is comparing feature matrices. The "
    "real question is usually one of three: <i>which one won't embarrass me in front of a client</i>, "
    "<i>which one is genuinely free</i>, or <i>which one won't cost me a fortune when I hire</i>.",
    "So this page is organised around those, not around a spec sheet. If you do want the "
    "side-by-side numbers — free plan contents, seat minimums and published prices across six "
    "vendors — that lives on our <a href=\"best-digital-business-card.html\">comparison page</a>, "
    "with each figure sourced from the vendor's own pricing page.",
  ]),
  block("The five criteria that actually decide it", checklist([
    ("Nothing to install at the other end.",
     "If the person receiving your card has to download an app, you will lose most of them at the "
     "counter. Scanning a QR into a browser should be the whole interaction."),
    ("A free plan you can use with real clients.",
     "Not a fourteen-day countdown. Check the card count, whether scans are capped monthly, and "
     "whether a wallet pass is included at $0."),
    ("A permanent link and QR code.",
     "This is the one people regret. If the URL can change, every printed code and email signature "
     "you have updated becomes wrong."),
    ("The smallest team you can actually buy.",
     "As of " + VERIFIED + ", Blinq's Business plan bills a minimum of five team cards and "
     "HiHello's starts at five users — so a two-person business pays for five."),
    ("Your branding, not the vendor's.",
     "Your logo and brand colour are what make it read as professional. Check what the free tier "
     "shows and what removing it costs."),
  ])),
  block("Which one fits your situation", table(
    ["If you are…", "What matters most", "Where to look"],
    [["<b>A one-person business who wants it to look established</b>",
      "Your own logo and colour, a booking link, and a card that stays free",
      "CompanyCard's free plan — wallet pass included, no scan cap"],
     ["<b>Someone who needs several separate cards</b>",
      "Free card count",
      "HiHello (4 free) or Blinq (2 free) beat us here as of " + VERIFIED],
     ["<b>A two or three person team</b>",
      "Being able to buy a team plan at your actual size",
      "CompanyCard — no seat minimum, where several rivals floor at five"],
     ["<b>Watching every pound or dollar</b>",
      "The monthly number",
      "Mobilo lists Pro at $3/mo, cheaper than our $8 — see our "
      "<a href=\"mobilo-alternative.html\">Mobilo comparison</a>"],
     ["<b>Handing cards out constantly in person</b>",
      "Speed of the share, and no monthly cap",
      "A wallet pass plus an uncapped free plan; consider NFC hardware only if you tap dozens a day"]],
    note="Competitor details verified " + VERIFIED + " from their own pricing pages and linked on our "
         "<a href=\"free-digital-business-card-comparison.html\">free plan comparison</a>. We make one of "
         "these products — the rows above name where others win.")),
  prose("Making yours look professional, whichever you pick", [
    "The platform matters less than what you put on the card. The cards that read as established "
    "share the same restraint: one logo, one brand colour, a photo that looks intentional, the two "
    "contact routes you actually answer, and a single clear next step.",
    "What makes a card look amateur is almost always addition — every phone number you have ever "
    "had, six social icons, a paragraph of biography. Link to the biography instead. The card is "
    "the door, not the room.",
    "If you want the specifics for your line of work, we have written them up for "
    "<a href=\"digital-business-card-for-realtors.html\">realtors</a>, "
    "<a href=\"digital-business-card-for-consultants.html\">consultants</a>, "
    "<a href=\"digital-business-card-for-contractors.html\">contractors</a>, "
    "<a href=\"digital-business-card-for-photographers.html\">photographers</a> and "
    "<a href=\"digital-business-card-for-small-business.html\">small businesses</a> generally.",
  ]),
  block("Test it in five minutes before you commit", steps_howto([
    "Make a card on the free plan — if the free tier can't produce something you'd share with a client, the paid tier won't fix it.",
    "Send it to a colleague's phone and count the taps until your contact is saved. More than three is friction you'll pay for at every meeting.",
    "Check what the card looks like with your logo and colour on it, not the demo's.",
    "Find the pricing page and work out the total for your <i>actual</i> headcount, including any seat minimum.",
  ]), tint=True),
]

PAGES6 = [BEST_VIRTUAL]
