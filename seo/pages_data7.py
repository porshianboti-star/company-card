# -*- coding: utf-8 -*-
"""Batch 7: rewrite popl-alternative.html — its thesis had gone stale.

WHY THIS REWRITE: the page was written when Popl read as an NFC-hardware
company ("built around NFC tags and cards you purchase per person"). Verified
2026-07-27 on popl.co and popl.co/pages/pricing, that is no longer accurate:

  * popl.co now leads with "Your AI GTM platform for in-person events" and
    "#1 Ranked Market Leader" in event lead capture. Its headline products are
    Event Lead Capture, Universal Badge Scanner, List Enrichment, Event
    Intelligence and Calendar Booking, with integrations to Salesforce,
    HubSpot and Marketo. Digital business cards are a SECONDARY offering.
  * Its pricing page publishes no prices and no free plan: "we quote pricing
    over a meeting instead of publishing it on our website."

The old page also still carried the email-signature / virtual-background
"included per seat" framing that was removed from blinq-alternative.html for
being a non-differentiator. Both are fixed here.

The honest current axis is not hardware-vs-software. It is:
enterprise event-marketing platform with demo-gated pricing
    vs
self-serve digital business card for small businesses with published pricing.
"""
from build_pages import cards3, table, prose, block, checklist, steps_howto

VERIFIED = "July 2026"
FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

POPL = {
 "slug": "popl-alternative.html",
 "crumb": "Popl Alternative",
 "title": "Popl Alternative for Small Business (2026) — Published Pricing | CompanyCard",
 "meta": ("Looking for a Popl alternative? Popl now positions itself as an enterprise event "
          "lead-capture platform and doesn't publish pricing. CompanyCard is a self-serve digital "
          "business card with a free plan and published rates."),
 "og": ("Popl alternative for small businesses — a self-serve digital business card with a free "
        "plan and published pricing, not a demo-gated enterprise platform."),
 "h1": 'A <span class="gradient-text">Popl alternative</span> you can just sign up for',
 "lead": ("Popl has moved upmarket — it now presents itself as an AI platform for event lead "
          "capture, and you book a demo to get a price. If you just want a professional digital "
          "business card you can start using today, that's a different product."),
 "cta_btn": "Create your free card",
 "cta2": ("See our pricing", "pricing.html"),
 "cta_h": "Sign up, don't book a call",
 "cta_p": "Free forever for one card, and every rate is on the pricing page.",
 "sections": [],
 "faqs": [
   ("What is the best Popl alternative?",
    "It depends what you were using Popl for. If you need enterprise event lead capture with badge "
    "scanning and CRM enrichment, that is now Popl's core product and a digital business card tool "
    "is not a replacement. If what you actually want is a professional digital business card you "
    "can set up yourself, CompanyCard is self-serve with published pricing and a free plan that "
    "includes " + FREE_SPEC),
   ("Does Popl have a free plan?",
    "Not as of " + VERIFIED + ". Popl's pricing page lists no free tier and no prices — it states "
    "that pricing is quoted in a meeting rather than published on the site. CompanyCard's free plan "
    "is available immediately with no credit card and no call."),
   ("Why doesn't Popl publish its pricing?",
    "Popl says it prefers to quote pricing over a meeting to make sure the product fits. That is a "
    "reasonable enterprise sales model, but it does mean you cannot compare costs on a Tuesday "
    "evening without talking to someone — which is usually the point at which a small business "
    "starts looking elsewhere."),
   ("Is Popl still a digital business card?",
    "It still offers digital business cards, but as of " + VERIFIED + " they are a secondary "
    "offering: popl.co leads with \"Your AI GTM platform for in-person events\" and its headline "
    "products are event lead capture, badge scanning, list enrichment and event intelligence. If "
    "your need is one card for yourself or a small team, you are no longer the main audience."),
   ("Do I need to buy NFC hardware?",
    "Not with CompanyCard — sharing is QR code, link, Apple or Google Wallet pass and email "
    "signature, so there is nothing to buy, ship or replace. If you already own an NFC tag that "
    "accepts a custom URL, you can point it at your CompanyCard link and a tap will open your card."),
   ("What does CompanyCard cost?",
    "Free for one card. Pro is $8 a month and removes the CompanyCard credit while adding custom "
    "branding, unlimited links, lead capture and analytics. Business is $12 per user per month for "
    "admin controls, brand lock, CRM sync and SSO, with no seat minimum. All of it is on the "
    "pricing page."),
 ],
 "related": [("Best digital business cards compared", "best-digital-business-card.html"),
             ("Free plans compared", "free-digital-business-card-comparison.html"),
             ("For small business", "digital-business-card-for-small-business.html"),
             ("Pricing", "pricing.html")],
}

POPL["sections"] = [
  prose("What changed at Popl", [
    "If you last looked at Popl a couple of years ago, you probably remember it as a digital "
    "business card brand known for NFC products. That is not how it presents itself now.",
    "As of " + VERIFIED + ", popl.co leads with <b>\"Your AI GTM platform for in-person events\"</b> "
    "and describes itself as the market leader in event lead capture. Its headline products are "
    "event lead capture, a universal badge scanner, list enrichment, event intelligence and "
    "calendar booking, with Salesforce, HubSpot and Marketo integrations. Digital business cards "
    "are still offered, but as a secondary part of the platform.",
    "That is a legitimate and probably sensible move for them — enterprise event marketing is a "
    "bigger budget than individual business cards. It just means that if you are a small business "
    "wanting one good card, you are no longer the customer the product is designed around.",
  ]),
  block("The practical differences", cards3([
    ("You can see the price",
     "Popl's pricing page publishes no rates and no free tier — it quotes over a meeting. "
     "CompanyCard's rates are published: free, $8 Pro, $12 per user Business."),
    ("You can start without a call",
     "Sign up, build the card, share it. No demo booking, no discovery call, no waiting for a "
     "quote to come back."),
    ("Sized for small businesses",
     "No seat minimum, and a free plan that is a complete working card rather than a trial."),
  ])),
  block("Side by side", table(
    ["What to check", "Popl (verified " + VERIFIED + ")", "CompanyCard"],
    [["<b>Free plan</b>", "None listed", "1 card, wallet pass, unlimited edits"],
     ["<b>Published pricing</b>", "No — quoted after a demo", "Yes — $8 Pro, $12 per user Business"],
     ["<b>How you start</b>", "Book a demo", "Sign up and build the card"],
     ["<b>Primary focus</b>", "Enterprise event lead capture and GTM", "Digital business cards for small businesses"],
     ["<b>Team seat minimum</b>", "Not published", "None"]],
    note='Read from <a href="https://popl.co" target="_blank" rel="noopener nofollow">popl.co</a> and '
         '<a href="https://popl.co/pages/pricing" target="_blank" rel="noopener nofollow">popl.co/pages/pricing</a> in '
         + VERIFIED + '. Popl is repositioning; check their site for current details. CompanyCard figures are our '
         'published rates on <a href="pricing.html">our pricing page</a>.')),
  prose("When Popl is still the right answer", [
    "We would rather point you correctly than win the click. If your job is running trade-show "
    "booths — scanning badges, enriching lead lists, pushing them into Salesforce the same day — "
    "that is what Popl is now built for, and a digital business card tool is not a substitute for "
    "it. Book the demo.",
    "CompanyCard is the right answer for the other case: you are a small business or a "
    "self-employed professional, you want a card that looks established and is easy to share, and "
    "you would like to set it up yourself this afternoon without a sales call. If you already own "
    "an NFC tag from a previous setup and it accepts a custom URL, point it at your CompanyCard "
    "link — the tap keeps working, and everyone else scans a QR or opens the link.",
  ]),
  block("Moving your card across", steps_howto([
    "Copy your details, links and photo from your existing card.",
    "Create a <a href=\"app/builder.html\">free CompanyCard</a> and paste them in, adding your logo and brand colour.",
    "Update your link where you control it — email signature, social bios, and any printed <a href=\"qr-code-business-card.html\">QR code</a>.",
    "If you own an NFC tag that accepts a custom URL, point it at your new CompanyCard link.",
  ]), tint=True),
]

PAGES7 = [POPL]
