# -*- coding: utf-8 -*-
"""Batch 13: e-name-card.html — the "name card" terminology page.

WHY THIS PAGE, AND WHY NOW (demand-verified, not guessed).
Google Search Console, 28d to 2026-08-17, read at the start of this run:
"e name card" is the **10th-largest query row on the whole property, 36
impressions**, ahead of every profession query we have shipped a page for.
A repo-wide grep for the strings "name card", "namecard", "ename" and
"e-name card" across all 55 HTML pages and llms.txt returned **zero matches**.
So the site earns impressions on a term it has never once written down. This is
the same shape as the finding that started the whole ICP programme (the words
"small business" / "self-employed" appeared on zero pages while the queries
existed) — a coverage gap, not an optimisation problem.

TERMINOLOGY EVIDENCE (searched 2026-08-20). "Name card" is the ordinary English
term for a business card in Singapore and Malaysia, and "digital name card" /
"e-name card" is how the digital version is marketed there. Observed in vendor
and publisher usage: hausmedia.com.sg ("Digital Name Card Singapore | e Name
Card"), digitalcard.com.sg ("Digital Name Cards | Singapore #1 customised
e-card"), sgnamecard.com.sg, singaporedigitalnamecard.com, and geniccards.com
("Guide to Create a Professional Digital Name Card in Singapore"). That is
evidence of *usage of the term*, which is all this page relies on.

POSITIONING (anti-cannibalisation). Four live pages are adjacent and NONE is
being rewritten:
  * digital-business-card.html — the flagship product/definitional page.
  * virtual-business-card.html — owns "virtual", and already owns the H2
    "Virtual vs. digital vs. electronic — what's the difference?", so this page
    does NOT run a fourth synonym-comparison section. It answers the naming
    question once, in one short section and one FAQ, then moves on.
  * electronic-business-card.html — owns the vCard-standard angle.
  * vcard-qr-code.html — owns the encoding mechanics.
This page owns the WORD. Its distinct substance is the one practical problem a
name card has that the other pages never address: a name that has to appear in
more than one script, which on paper costs you a second side and on a digital
card costs you nothing. Nothing here restates the vCard spec or the QR mechanics.

DELIBERATELY NOT STATED (could not be verified, so absent from the page):
  * any market size, adoption rate, user count or growth statistic for name
    cards or digital name cards, in any country;
  * any price, plan or feature of any named competitor, local or global —
    the Singapore/Malaysia vendors above are cited nowhere on the page and no
    claim is made about what they charge or include;
  * any assertion about business-card etiquette, greeting customs or
    two-handed exchange in any specific country — the bilingual section is
    written as a conditional printing constraint ("if your name is written in
    more than one script"), which is a fact about paper, not about a culture;
  * any claim that CompanyCard renders or validates non-Latin scripts beyond
    what a normal text field does;
  * any claim about which countries our own users are in — we have no such data
    that survives the QA-account filter.

PRODUCT CLAIMS are held to pricing.html and llms.txt as re-read live on
2026-08-20 (Free = 1 card, QR & link sharing, profile/links/socials, Add to
Apple & Google Wallet; free cards carry a small CompanyCard credit). Note this
run also fixed a contradiction on pricing.html itself, where the FAQ claimed
paid plans "add" Wallet passes while the plan table lists Wallet under Free.
"""
from build_pages import prose, block, checklist, table

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

E_NAME_CARD = {
 "slug": "e-name-card.html",
 "crumb": "E-Name Card",
 "title": "E-Name Card: Make a Digital Name Card Free | CompanyCard",
 "meta": ("An e-name card is a digital name card — the same thing as a digital business card, "
          "under the name used across Singapore and Malaysia. Make one free in a minute."),
 "og": ("An e-name card is a digital name card: your details on one link and QR code, editable "
        "after you share them. Free plan, no app for the person receiving it."),
 "h1": 'Make your <span class="gradient-text">e-name card</span> in about a minute',
 "lead": ("An e-name card is a digital name card — your contact details on a link and a QR code "
          "instead of a piece of card. If you have seen the term “digital business card”, "
          "this is the same product under the name most people use in Singapore and Malaysia."),
 "cta_btn": "Create your free e-name card",
 "cta2": ("See what's on the free plan", "free-digital-business-card.html"),
 "cta_h": "One name card that is never out of date",
 "cta_p": "Free forever, no credit card, and the person you share it with installs nothing.",

 "howto_name": "How to make an e-name card",
 "howto": [
   "Start a card and enter the name you actually introduce yourself with, plus your role and company.",
   "Add the ways you want to be reached — phone, email, website, and the messaging or social accounts you really use.",
   "If your name is written in more than one script, put both forms on the card rather than choosing between them.",
   "Save it, then share the link or show the QR code. The person scanning it needs no app, and you can edit the details afterwards without reissuing anything.",
 ],

 "sections": [
  prose("What an e-name card is", [
    "In Singapore, Malaysia and much of Southeast Asia, the small rectangle you hand someone when "
    "you meet them is called a <b>name card</b>, not a business card. An e-name card is the digital "
    "version of it: the same details, delivered as a link and a QR code rather than as a printed "
    "piece of card.",

    "There is no difference in substance between an e-name card, a digital name card, a digital "
    "business card and a virtual business card. They are the same product, and which words you see "
    "depends mostly on where the person writing them is. If you searched for one and landed on a "
    "page selling the other, you were in the right place.",

    "What changes is not the format but what happens after the exchange. A printed name card is "
    "finished the moment it leaves the printer: the number on it is the number you had that day. "
    "An e-name card is a live page you still control, so a new number, a new role or a new company "
    "updates everywhere you have already shared it — including on the cards people saved months ago.",
  ]),

  block("The problem a name card has that a business card does not", checklist([
    ("Two scripts, one card",
     "if your name is written in both Latin letters and Chinese characters — or Tamil, or Jawi, "
     "or any other script you use professionally — a printed card generally has to give one of them "
     "a side of its own. That is what double-sided name cards are for."),
    ("A digital card has no sides",
     "so both forms of your name can sit on the front of the same card, together, and the person "
     "saving you does not have to decide which one to type into their phone."),
    ("Nothing gets mistyped",
     "a saved contact comes from the card itself, not from someone reading a script they may not "
     "read, at a table, after a long day."),
    ("Reprints stop being a decision",
     "changing how your name is rendered, or adding a second script later, is an edit rather than "
     "a new print run."),
   ]), tint=True),

  prose("What people actually do with the card you send", [
    "An e-name card is shared three ways, and all three end in the same place: your details inside "
    "the other person's phone.",

    "You show a QR code and they scan it with the camera. You send the link — in a message, an "
    "email, a chat group — and they tap it. Or you add the card to Apple Wallet or Google Wallet "
    "and pull it up the way you pull up a boarding pass. In every case the card opens in the browser "
    "they already have, and there is nothing for them to install before they can see who you are.",

    "The part that matters is the save button. A paper name card gets photographed, or put in a "
    "pocket, or lost. A digital one gets saved as a contact in a couple of taps, which is the only "
    "outcome that was ever the point of handing it over.",

    "CompanyCard's free plan covers all of this: " + FREE_SPEC,
  ]),
 ],

 "faqs": [
  ("What is an e-name card?",
   "An e-name card is a digital name card — your contact details published as a web page with a "
   "permanent link and QR code, instead of printed on card. You share the link or let someone scan "
   "the code, and they save your details straight into their phone."),

  ("Is an e-name card the same as a digital business card?",
   "Yes. They are the same product under different regional words: “name card” is the "
   "ordinary term for a business card in Singapore and Malaysia, while “business card” is "
   "more usual in British and American English. “Digital name card”, “e-name "
   "card”, “virtual business card” and “electronic business card” all "
   "describe the same thing."),

  ("How do I make an e-name card for free?",
   "Create a card, enter your name, role, company and the ways you want to be reached, then save it "
   "and share the link or QR code. The CompanyCard free plan includes " + FREE_SPEC),

  ("Can my e-name card show my name in two languages?",
   "Yes. A digital card has no front and back to divide, so you can put both forms of your name on "
   "the same card rather than giving each one a side. They are ordinary text fields, so whichever "
   "scripts your device can type, the card can carry."),

  ("Does the person I send it to need an app?",
   "No. The card opens as a web page in whatever browser is already on their phone. Scanning the QR "
   "code or tapping the link is all they do, and saving your details is a couple of taps after that."),

  ("Can I change my details after I have shared my e-name card?",
   "Yes, and this is the main practical difference from a printed name card. The link and QR code "
   "stay the same while the details behind them change, so a new number or a new job title reaches "
   "everyone you have already shared the card with. Unlimited edits are included on the free plan."),
 ],

 "related": [
   ("Digital business card", "digital-business-card.html"),
   ("Virtual business card", "virtual-business-card.html"),
   ("QR code business card", "qr-code-business-card.html"),
   ("Free digital business card", "free-digital-business-card.html"),
   ("Business card maker", "digital-business-card-maker.html"),
 ],
}

PAGES = [E_NAME_CARD]
