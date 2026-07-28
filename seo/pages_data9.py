# -*- coding: utf-8 -*-
"""Batch 9: the last two competitor-alternative pages.

VERIFIED 2026-07-28 from each vendor's own pricing page:

  Wave Connect (wavecnct.com/pages/pricing)
    Free $0: digital business card, personal email signature, unlimited
    sharing, unlimited contacts, Apple/Google Wallet, QR + email + SMS
    sharing, LEAD CAPTURE FORM. Free cards DO carry Wave branding (Pro
    advertises "Remove Wave branding").
    Pro $7/mo (no seat minimum). Teams $5/user/mo with a 3-SEAT MINIMUM.
    Enterprise custom. Sells NFC products but does not require them.

  V1CE (v1ce.co/pages/pricing)
    NO free plan — 30-day trial. Single tier £49.99/month, which bundles a
    premium NFC card (free shipping, lifetime replacements) with "Client
    Capture OS" (CRM, automated follow-ups, booking, agreements, payments)
    and a "Scout AI" assistant. Explicitly no tiers or add-ons.

HONESTY NOTE, and it matters: Wave Connect beats CompanyCard on several
published axes — its free tier includes a lead capture form and email
signature (we gate lead capture behind Pro), and both Pro ($7 vs $8) and Teams
($5 vs $12 per user) are cheaper. The only published edge we have is the seat
floor: Wave Teams needs 3 seats, we need none. The page says exactly that and
does not manufacture more. A comparison page that loses honestly is still worth
publishing — it captures the query and it is the behaviour that earns citation.
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

# ------------------------------------------------------------- Wave Connect
WAVE = {
 "slug": "wave-connect-alternative.html",
 "crumb": "Wave Connect Alternative",
 "title": "Wave Connect Alternative — Honest Comparison (2026) | CompanyCard",
 "meta": ("A genuinely honest Wave Connect comparison: Wave's free tier and paid prices beat ours "
          "on several counts. The one place CompanyCard wins is the team seat floor. Verified "
          "July 2026."),
 "og": ("An honest Wave Connect comparison — including the columns where Wave beats CompanyCard."),
 "h1": 'Wave Connect <span class="gradient-text">alternative</span>, honestly compared',
 "lead": ("We'll save you the sales pitch: on published prices and free-tier features, Wave Connect "
          "beats us in several places. There is one specific case where CompanyCard is the better "
          "buy, and this page is mostly about telling you which one you're in."),
 "cta_btn": "Try CompanyCard free",
 "cta2": ("See the full comparison", "free-digital-business-card-comparison.html"),
 "cta_h": "Pick the one that fits, not the one that pitched",
 "cta_p": "Our free plan takes two minutes to test. So does theirs.",
 "sections": [],
 "faqs": [
   ("Is CompanyCard better than Wave Connect?",
    "Not across the board, and it would be dishonest to claim so. As of " + VERIFIED + " Wave "
    "Connect's free plan includes a lead capture form and a personal email signature, and its paid "
    "plans are cheaper — $7 a month against our $8, and $5 per user against our $12. The one "
    "published place CompanyCard wins is the team floor: Wave's Teams plan requires three seats, "
    "and we have no seat minimum. If your team is one or two people, that difference is the whole "
    "decision."),
   ("What does Wave Connect's free plan include?",
    "As of " + VERIFIED + ", Wave's free tier lists a digital business card, a personal email "
    "signature, unlimited sharing, unlimited contacts, Apple and Google Wallet, QR, email and SMS "
    "sharing, and a lead capture form. Free cards carry Wave branding — its Pro plan advertises "
    "removing it. Check wavecnct.com for current terms."),
   ("Do both put branding on the free card?",
    "Yes. Wave's Pro plan lists \"Remove Wave branding\" as a paid feature, and CompanyCard's free "
    "cards carry a small CompanyCard credit that Pro removes. Neither free tier is unbranded, so "
    "that is not a reason to pick one over the other."),
   ("When is CompanyCard the better choice?",
    "When your team is smaller than three people and you want them on a proper team plan with "
    "locked branding and central admin. Wave's Teams plan starts at three seats; CompanyCard has no "
    "seat minimum, so a two-person business can buy exactly two."),
   ("When should I just use Wave Connect?",
    "If you are a single user who wants lead capture on a free plan, or price is your deciding "
    "factor at any team size of three or more. On the published numbers those are Wave's, and we "
    "would rather you chose correctly than churned in a month."),
   ("What does CompanyCard's free plan include?",
    "It includes " + FREE_SPEC),
 ],
 "related": REL,
}
WAVE["sections"] = [
  prose("The honest version", [
    "Most \"alternative\" pages are written by the alternative. This one is too, so here is the "
    "part those pages usually leave out: on the published numbers as of " + VERIFIED + ", Wave "
    "Connect is cheaper than CompanyCard and its free tier does more.",
    "Wave's free plan lists a lead capture form and a personal email signature. We gate lead "
    "capture behind Pro. Its Pro is $7 a month to our $8, and its Teams plan is $5 per user to our "
    "$12. Those are real differences and we are not going to explain them away.",
    "There is one published place we win, and it is narrow but decisive for the people it affects: "
    "<b>Wave's Teams plan requires a minimum of three seats. CompanyCard has no seat minimum.</b> "
    "If you are a two-person business that wants locked branding and a shared dashboard, you cannot "
    "buy Wave Teams at the size you actually are.",
  ]),
  block("Side by side, published figures", table(
    ["", "Wave Connect (verified " + VERIFIED + ")", "CompanyCard"],
    [["<b>Free plan</b>", "Card, email signature, wallet, unlimited contacts, lead capture form",
      "Card, QR + link, wallet, unlimited edits"],
     ["<b>Branding on free</b>", "Yes — Pro removes it", "Yes — Pro removes it"],
     ["<b>Individual paid</b>", "$7/mo Pro", "$8/mo Pro"],
     ["<b>Team paid</b>", "$5/user/mo", "$12/user/mo"],
     ["<b>Team seat minimum</b>", "<b>3 seats</b>", "<b>None</b>"],
     ["<b>NFC hardware</b>", "Sold, not required", "None sold"]],
    note='Read from <a href="https://www.wavecnct.com/pages/pricing" target="_blank" rel="noopener nofollow">wavecnct.com/pages/pricing</a> in '
         + VERIFIED + '. Wave wins most of these columns. Terms change — check before deciding.')),
  block("Which one you are", cards3([
    ("A team of one or two",
     "CompanyCard. Wave Teams needs three seats, so you either overpay for a seat you don't use or "
     "stay on individual plans without shared branding."),
    ("A single user wanting lead capture free",
     "Wave. Their free tier includes a lead capture form; ours doesn't."),
    ("A team of three or more, price-led",
     "Wave, on the published per-user numbers. Run the total for your actual headcount."),
  ])),
]

# ------------------------------------------------------------------- V1CE
V1CE = {
 "slug": "v1ce-alternative.html",
 "crumb": "V1CE Alternative",
 "title": "V1CE Alternative — Free Digital Business Card, No £49.99/mo | CompanyCard",
 "meta": ("A V1CE alternative for people who want a digital business card, not a £49.99/month "
          "hardware-and-CRM subscription. Free plan, no card to receive, no trial countdown."),
 "og": ("V1CE alternative — a free digital business card instead of a £49.99/month bundled "
        "hardware and CRM subscription."),
 "h1": 'A <span class="gradient-text">V1CE alternative</span> that starts at nothing',
 "lead": ("V1CE bundles a premium NFC card with a full client-capture CRM for a single £49.99 a "
          "month, and has no free plan. If what you want is the card part, that's a lot of product "
          "to buy for it."),
 "cta_btn": "Create your free card",
 "cta2": ("Compare free plans", "free-digital-business-card-comparison.html"),
 "cta_h": "Start free, add tools when you need them",
 "cta_p": "No trial countdown, no hardware to receive, no £49.99 a month.",
 "sections": [],
 "faqs": [
   ("Does V1CE have a free plan?",
    "No. As of " + VERIFIED + " V1CE offers a 30-day free trial and then a single tier at £49.99 "
    "per month. It is explicit that there are no other tiers or add-ons. CompanyCard has a free "
    "plan with no time limit and no credit card."),
   ("What is included in V1CE's £49.99 a month?",
    "A premium NFC smart business card with free shipping and lifetime replacements, plus its "
    "Client Capture OS — CRM, automated follow-ups, booking, agreements and payments — and a Scout "
    "AI networking assistant. It is a bundle, not just a card, which is why the price sits where it "
    "does. Check v1ce.co for current terms."),
   ("Is CompanyCard cheaper than V1CE?",
    "Substantially, but they are not the same purchase. CompanyCard is free for one card, $8 a "
    "month for Pro and $12 per user for Business — a digital business card product. V1CE at £49.99 "
    "a month bundles hardware and a full client-capture CRM. If you need the CRM and the physical "
    "card, compare it against what you would otherwise pay for those separately."),
   ("When is V1CE the better choice?",
    "If you want a premium physical NFC card and a CRM with follow-ups, booking and payments in one "
    "subscription, and £49.99 a month is proportionate to the deals you close. For a lot of "
    "consultants and salespeople it will be. A free digital business card is not a substitute for a "
    "CRM."),
   ("Can I use my V1CE card with CompanyCard?",
    "If your NFC card lets you write a custom URL, you can point it at your CompanyCard link and a "
    "tap will open your card. CompanyCard does not sell hardware, so anything you already own keeps "
    "working alongside QR and link sharing."),
 ],
 "related": REL,
}
V1CE["sections"] = [
  prose("Two very different purchases", [
    "V1CE is not really a competitor to a digital business card — it is a bundle. As of " + VERIFIED +
    ", £49.99 a month gets you a premium NFC card with lifetime replacements plus a full client "
    "capture system: CRM, automated follow-ups, booking, agreements, payments and an AI assistant. "
    "There is one tier and no free plan, just a 30-day trial.",
    "That is a coherent product for someone whose job is closing deals in person, and if it "
    "replaces a CRM you already pay for, the maths can work comfortably.",
    "It is a lot to buy if what you actually wanted was a good digital business card. That is the "
    "gap CompanyCard fills: free for one card, $8 a month if you want custom branding and the "
    "credit removed, $12 per user for a team with admin controls — and no hardware to receive or "
    "replace.",
  ]),
  block("Side by side", table(
    ["", "V1CE (verified " + VERIFIED + ")", "CompanyCard"],
    [["<b>Free plan</b>", "None — 30-day trial", "Yes, no time limit, no credit card"],
     ["<b>Price</b>", "£49.99/month, single tier", "Free · $8/mo Pro · $12/user/mo Business"],
     ["<b>What you get</b>", "NFC card + CRM, follow-ups, booking, payments, AI assistant",
      "Digital business card, QR/link/wallet, branding, team admin"],
     ["<b>Hardware</b>", "Premium NFC card included, lifetime replacements", "None — nothing to ship or replace"],
     ["<b>Best for</b>", "In-person closers who want card + CRM in one bill",
      "Small businesses and self-employed who want the card"]],
    note='Read from <a href="https://v1ce.co/pages/pricing" target="_blank" rel="noopener nofollow">v1ce.co/pages/pricing</a> in '
         + VERIFIED + '. Terms change — check before deciding.')),
  block("Before you switch, ask", checklist([
    ("Do you actually use the CRM half?", "If yes, V1CE's price is buying two things and may be fair."),
    ("Do you want a physical card?", "V1CE includes one; CompanyCard sells no hardware at all."),
    ("How many people?", "V1CE is a single per-person subscription; team pricing changes the maths."),
    ("Would a free card do for now?", "You can test that in two minutes without a trial countdown."),
  ]), tint=True),
]

PAGES9 = [WAVE, V1CE]
