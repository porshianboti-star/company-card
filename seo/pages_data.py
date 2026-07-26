# -*- coding: utf-8 -*-
"""Page content for CompanyCard's ICP (small business / self-employed) pages.

COMPETITOR FACTS BELOW WERE VERIFIED BY DIRECT FETCH ON 2026-07-26 from each
vendor's own pricing page. Re-verify before editing; if a rival changes, change
the copy. Never state a competitor limitation we haven't checked — assistants
cross-check vendor pricing pages, and one contradicted claim discredits the
whole domain (that is exactly the bug this pass fixed on /blinq-alternative).

  Blinq   free: 2 cards, virtual backgrounds, personal email signature, Apple
          Wallet. Business plan bills a MINIMUM of 5 team cards.
  HiHello free: 4 cards, email signature, virtual backgrounds, wallet — but
          capped at 5 card & badge scans per month. Business = 5-100 users.
  Popl    no free plan; pricing is demo-gated (not published).
  CompanyCard free: 1 card, QR + link, profile/links/socials, Apple & Google
          Wallet, unlimited edits, carries a small CompanyCard credit
          (removing it is Pro, $8/mo). Business $12/user/mo. No seat minimum.
"""

VERIFIED = "July 2026"

FREE_SPEC = (
    "one digital business card, a QR code and sharing link, your profile, links and "
    "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
    "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro."
)

_RELATED_CORE = [
    ("Free digital business card", "free-digital-business-card.html"),
    ("Digital business card", "digital-business-card.html"),
    ("QR code business card", "qr-code-business-card.html"),
    ("Pricing", "pricing.html"),
]

# ---------------------------------------------------------------- flagship ICP
SMALL_BUSINESS = {
 "slug": "digital-business-card-for-small-business.html",
 "crumb": "Digital Business Card for Small Business",
 "title": "Digital Business Card for Small Business (Free Plan) | CompanyCard",
 "meta": ("CompanyCard is a free digital business card for small business owners — share by "
          "QR code, link or Apple/Google Wallet, no app for your customer, and no seat "
          "minimum when you add your first employee."),
 "og": ("A free digital business card built for small businesses: QR, link and wallet sharing, "
        "no app for the recipient, and no 5-seat minimum when you grow."),
 "h1": 'Digital business card for <span class="gradient-text">small business</span>',
 "lead": ("CompanyCard is a digital business card for small business owners: share your details "
          "by QR code, link or wallet, keep them current forever, and add a colleague without "
          "being forced onto a five-seat plan. Free to start."),
 "cta_btn": "Create your free card",
 "cta2": ("See pricing", "pricing.html"),
 "cta_h": "Look established from the first handshake",
 "cta_p": "Build your card in a couple of minutes. Free forever, no credit card.",
 "howto_name": "How to make a digital business card for your small business",
 "howto": [
   "Open the CompanyCard builder and enter your name, business name and role.",
   "Add the ways customers actually reach you — phone, email, website, WhatsApp, booking link and socials.",
   "Add your logo and brand colour so the card looks like your business, not a template.",
   "Share it: show the QR code, send the link, or add the pass to Apple or Google Wallet.",
 ],
 "sections": [],   # filled below
 "faqs": [
   ("Is there a free digital business card for small business?",
    "Yes. CompanyCard's free plan includes " + FREE_SPEC + " It is not a trial — there is no "
    "time limit and no credit card required."),
   ("Does my customer need an app to receive my card?",
    "No. They scan your QR code or open your link in any phone browser and save your contact "
    "in one tap. Nothing to install, on any phone."),
   ("What happens when I hire my first employee?",
    "You add them and keep going — CompanyCard has no seat minimum. This is worth checking "
    "elsewhere: as of " + VERIFIED + ", Blinq's Business plan bills a minimum of five team "
    "cards and HiHello's Business plan starts at five users, so a two- or three-person "
    "business pays for seats it does not use."),
   ("Do I have to reprint anything when my details change?",
    "No, and that is the main reason small businesses switch. You edit the card once and "
    "every QR code and link you have already shared shows the new details — including codes "
    "already printed on a van, a window or a flyer. Your link and QR code never change."),
   ("Is a digital business card professional enough for a small business?",
    "It reads as more prepared, not less. Handing over a scannable code that saves your "
    "details instantly — with your logo and brand colour — looks deliberate, and it removes "
    "the moment where someone loses your paper card in a pocket."),
   ("Can I use it without a website?",
    "Yes. Many small businesses use their CompanyCard link as their web presence: it holds "
    "your services, contact details, socials, booking link and payment handle in one page you "
    "can update yourself."),
 ],
 "related": [("Free digital business card", "free-digital-business-card.html"),
             ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
             ("Best digital business card apps", "best-digital-business-card.html"),
             ("Pricing", "pricing.html")],
}

# --------------------------------------------------- freelance / self-employed
FREELANCE = {
 "slug": "digital-business-card-for-freelancers.html",
 "crumb": "Digital Business Card for Freelancers & Self-Employed",
 "title": "Digital Business Card for Freelancers & Self-Employed | CompanyCard",
 "meta": ("A free digital business card for freelancers, self-employed professionals and "
          "solopreneurs. Share by QR code or link, update it any time, and look established "
          "without a design budget."),
 "og": ("Free digital business card for freelancers, self-employed pros and solopreneurs — "
        "QR, link and wallet sharing, no app needed to receive it."),
 "h1": 'Digital business card for <span class="gradient-text">freelancers &amp; the self-employed</span>',
 "lead": ("You are the brand. A CompanyCard digital business card gives freelancers, "
          "self-employed professionals and solopreneurs one link that holds everything — "
          "work, contact details, booking and payment — and updates the moment your work does."),
 "cta_btn": "Create your free card",
 "cta2": ("What's in the free plan", "free-digital-business-card.html"),
 "cta_h": "One link that grows with your work",
 "cta_p": "Free forever, no credit card, and your link never changes.",
 "sections": [],
 "faqs": [
   ("Is this a business card or a business credit card?",
    "This is a digital business card — the contact card you share with clients, not a credit "
    "card or financing product. Searches for 'self-employed business card' return both, so to "
    "be explicit: CompanyCard replaces the paper card in your wallet, not the payment card."),
   ("What is the best digital business card for a freelancer?",
    "For most freelancers the deciding factors are: a free tier you can actually use with "
    "clients, no app required for the person receiving it, and a link that never changes when "
    "you rebrand or change your rates. CompanyCard's free plan covers all three — it includes "
    + FREE_SPEC),
   ("Does it work for solopreneurs and sole traders too?",
    "Yes — solopreneur, sole trader, freelancer and self-employed are different words for the "
    "same setup here: one person who is the whole business. The card is built for exactly that, "
    "and it scales without penalty if you ever bring someone on, because there is no seat minimum."),
   ("Can I put my portfolio, booking link and payment details on it?",
    "Yes. Alongside your contact details you can add your website or portfolio, a booking or "
    "calendar link, socials and a payment handle, so a prospect can look at your work and book "
    "you from the same page."),
   ("What happens to my card if I change what I do?",
    "You edit it — the link and QR code stay the same. Freelance work changes shape often, and "
    "that is precisely where paper cards and PDF one-pagers fail: everything you have already "
    "handed out keeps pointing at the new version."),
   ("How do I share it if I meet someone without my phone out?",
    "Your link works in an email signature, a proposal footer, a social bio or a printed QR "
    "code on an invoice or sticker. The QR is permanent, so anything you print stays valid."),
 ],
 "related": [("For small business", "digital-business-card-for-small-business.html"),
             ("Free digital business card", "free-digital-business-card.html"),
             ("Email signature generator", "email-signature-generator.html"),
             ("Digital vs paper", "digital-business-card-vs-paper.html")],
}

# ------------------------------------------------------------------ sections
# Built here (not inline above) so the copy sits next to the verified facts.
from build_pages import cards3, table, prose, block, checklist, steps_howto

SMALL_BUSINESS["sections"] = [
  block("What a small business actually needs from a business card", cards3([
    ("Details that are never out of date",
     "Change your number, add a service or move premises and every code you've already given "
     "out updates itself. Nothing to reprint."),
    ("Nothing for the customer to install",
     "They scan or tap, your card opens in the browser, one tap saves you to their contacts. "
     "No app, on any phone."),
    ("Room to grow, without a five-seat bill",
     "Add your first employee when you're ready. There's no seat minimum, so a two-person "
     "business isn't billed like a five-person one."),
  ])),

  prose("The small-business case for going digital", [
    "Most small businesses don't lose work because their card looked wrong. They lose it "
    "because the card ended up in a drawer, or because the number on it changed two years ago "
    "and the box of 500 is still sitting in the cupboard.",
    "A digital card removes both problems at once. The QR code on your van, your window or "
    "your invoice keeps working after you change your phone, your prices or your logo — you "
    "edit the card, not the print run. And because the person receiving it saves you in one "
    "tap, you end up in the phone rather than in the bin.",
    "It also does something paper can't: it carries the things small businesses actually get "
    "hired through — a booking link, a WhatsApp button, a payment handle, a link to reviews — "
    "in the same place as your phone number.",
  ]),

  block("Set it up in four steps", steps_howto([
    "Open the <a href=\"app/builder.html\">CompanyCard builder</a> and enter your name, business name and role.",
    "Add the ways customers actually reach you — phone, email, website, WhatsApp, booking link and socials.",
    "Add your logo and brand colour so the card looks like your business, not a template.",
    "Share it: show the <a href=\"qr-code-business-card.html\">QR code</a>, send the link, or add the pass to Apple or Google Wallet.",
  ]), tint=True),

  block("What you get on the free plan", checklist([
    ("One full digital business card.",
     "Your photo or logo, business name, role, contact details, links and socials."),
    ("QR code and sharing link.",
     "Both permanent — print the QR on anything and it keeps working."),
    ("Apple and Google Wallet pass.",
     "Included at $0. Your card sits in the customer's wallet next to their boarding passes."),
    ("Unlimited edits, forever.",
     "No time limit, no credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro."),
  ])),

  prose("How it compares if you're a two- or three-person business", [
    "The digital business card market is built around either individuals or companies with a "
    "real headcount, and small businesses fall in the gap. It's worth checking the small print "
    "before you commit, because the gap shows up in the bill.",
    table(["What to check", "Why it matters to a small business", "Where CompanyCard stands"], [
      ["<b>Team seat minimum</b>",
       "Several team plans bill a floor of five seats whether you use them or not",
       "No minimum — add one colleague and pay for one colleague"],
      ["<b>Is pricing published?</b>",
       "Hidden pricing means booking a sales call before you can compare",
       "Published: free, $8/mo Pro, $12 per user/mo Business"],
      ["<b>Wallet pass on the free tier</b>",
       "Wallet is often the feature that gets gated first",
       "Included on the free plan"],
      ["<b>Does the recipient need an app?</b>",
       "Any install step loses you customers at the counter",
       "No app — opens in any phone browser"],
    ], note="Competitor plan details change; check each vendor's own pricing page before deciding. "
            "Figures for CompanyCard are our published rates as of " + VERIFIED + "."),
  ]),
]

FREELANCE["sections"] = [
  prose("First, the disambiguation", [
    "<p>If you searched for a business card as a self-employed person, you may have landed on "
    "pages about business <i>credit</i> cards. This is not that. CompanyCard is a digital "
    "business card — the contact card you hand to a client, replacing the paper one in your "
    "wallet. No credit, no application, no financing.</p>",
  ]),

  block("Why one link beats a stack of cards", cards3([
    ("Your work changes — the link doesn't",
     "Rebrand, raise your rates, switch niches: you edit the card and everything you've already "
     "sent shows the new version. The URL and QR never change."),
    ("Everything a client needs in one place",
     "Portfolio, contact details, booking link, socials and a payment handle — so a prospect can "
     "see your work and book you without leaving the page."),
    ("Free is genuinely free",
     "No trial countdown and no credit card. Free cards carry a small CompanyCard credit; that's "
     "the only catch, and we'd rather say it than bury it."),
  ])),

  prose("Freelancer, self-employed, solopreneur, sole trader", [
    "These are four words for the same working reality: you are the business, so your business "
    "card is really a personal brand asset. That changes what it needs to do.",
    "A company card mostly needs to say who you work for. Yours needs to prove what you can do — "
    "which is why the useful version links straight to work samples and a way to book you, and "
    "why it has to be editable the week you change direction.",
    "It also needs to cost nothing while you're building. A card you can share with a client at "
    "$0, that doesn't expire and doesn't demand a card number up front, is the baseline — and "
    "it should still be there, unchanged, when you're charging three times as much.",
  ]),

  block("What to put on a freelancer's card", checklist([
    ("Name, discipline and a one-line positioning.",
     "\"Brand designer for early-stage founders\" beats \"Freelance Designer\"."),
    ("A link to actual work.",
     "Portfolio, showreel or a case study — the thing that decides whether you get the reply."),
    ("A way to book you.",
     "Calendar link or enquiry form, so interest converts before it cools."),
    ("How you get paid, if relevant.",
     "A payment handle saves an awkward email for trades, coaches and creators."),
    ("Only the socials that sell you.",
     "One or two that show your work. Leave the rest off."),
  ]), tint=True),
]

PAGES = [SMALL_BUSINESS, FREELANCE]
