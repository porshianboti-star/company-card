# -*- coding: utf-8 -*-
"""Batch 8: five more self-employed trades + the events cluster.

Resumed after correcting an earlier misread: the GSC drilldown on 2026-07-28
showed "Crawled - currently not indexed" = 0 affected pages, so there is no
quality/authority penalty and expansion is not contraindicated. The only
exclusions are benign duplicate-URL canonicals.

Each page must earn its place with trade-specific substance — the failure mode
for a batch like this is ten pages that differ only in the noun. What is
genuinely different per trade: how they get hired, what a prospect needs to see
before calling, and which detail on the card is load-bearing.

Product claims limited to what our own /pricing states. No invented statistics,
licensing requirements or regulatory claims — where rules vary, the page says
"check your own regulator".
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


MORTGAGE = profession(
 "digital-business-card-for-mortgage-brokers.html", "Digital Business Card for Mortgage Brokers",
 "Digital Business Card for Mortgage Brokers & Loan Officers | CompanyCard",
 "A digital business card for mortgage brokers and loan officers — carry your licence "
 "details, make applications one tap away, and stay in the phone of every agent who refers you.",
 'Digital business card for <span class="gradient-text">mortgage brokers</span>',
 "Mortgage work arrives by referral and moves fast. Your card has to survive being forwarded "
 "from an estate agent to a buyer, and still be reachable six months later when they're ready.",
 ["Brokers and loan officers get most of their business through people who are not their "
  "clients — estate agents, solicitors, accountants, past borrowers. That means the card's real "
  "job is to <i>forward well</i>: open cleanly in a message, show your credentials to a stranger, "
  "and make starting an application obvious.",
  "The timing problem is the other half. Someone meets you months before they buy. A paper card "
  "does not survive that gap; a saved contact with a working link does — and if your rates, "
  "lenders or phone number changed in between, the link still shows the current version.",
  "Licensing details belong on it. Registration or licence numbers are commonly required in "
  "broker communications, and putting them on the card means they travel with every share. "
  "Follow your own regulator's rules on exactly what must be displayed."],
 [("Your licence or registration number.", "Add it as a field so it appears on every share."),
  ("An application or enquiry link.", "The one action worth making obvious."),
  ("What you actually arrange.", "First-time buyers, buy-to-let, remortgage, commercial — clients search by situation."),
  ("A direct line.", "Referrals go cold fast; make reaching you one tap."),
  ("Your firm and any network you sit under.", "Reassures a stranger who was handed your details."),
  ("A calendar link for a first chat.", "Turns a referral into a booked call before it cools.")],
 [("What should a mortgage broker's digital business card include?",
   "Your name and firm, your licence or registration number if your regulator requires it in "
   "communications, the kinds of lending you arrange, a direct contact route and a link to start "
   "an application or book a first call. Check your own regulator's rules on required disclosures."),
  ("Why does a digital card suit mortgage work?",
   "Because most of your business is forwarded by someone else and often acted on months later. A "
   "link opens cleanly in a message, shows your credentials to someone who has never met you, and "
   "still works when your number, firm or product range has changed since."),
  ("Can I show which lenders or products I cover?",
   "Yes — add them as fields or links on the card, and edit them whenever your panel changes "
   "without reprinting anything."),
  ("Is it free to start?", "Yes. The free plan includes " + FREE_SPEC)])

TRAINER = profession(
 "digital-business-card-for-personal-trainers.html", "Digital Business Card for Personal Trainers",
 "Digital Business Card for Personal Trainers & Coaches | CompanyCard",
 "A digital business card for personal trainers — share it on the gym floor by QR, link to your "
 "results and packages, and let people book a session without an awkward exchange.",
 'Digital business card for <span class="gradient-text">personal trainers</span>',
 "The best time to get someone to book is thirty seconds after they ask what you charge — on the "
 "gym floor, with no pen and nowhere to put a paper card.",
 ["Personal training is sold in short, unplanned conversations in a place where nobody is carrying "
  "a wallet. A QR code on your phone solves the mechanics: they scan, your packages and results are "
  "on their screen, and you are saved in their contacts before the conversation ends.",
  "It also carries the proof. Prospective clients want to see people like them who got results, and "
  "a link does that where a card cannot — before-and-afters, a class timetable, a testimonial page, "
  "your Instagram.",
  "And your offer changes constantly: new packages, seasonal pricing, a block of classes, a gym "
  "move. An editable card means the QR on your water bottle, your car and the gym noticeboard keeps "
  "showing what you are actually selling this month."],
 [("A booking link, front and centre.", "The whole point — capture them while they're motivated."),
  ("Your packages and price range.", "Filters out the conversation you'd rather not have twice."),
  ("Proof: results, testimonials or Instagram.", "Prospects want to see people like them."),
  ("Your specialisms.", "Strength, pre/post-natal, rehab, over-50s — people search by need."),
  ("Where you train.", "Gym, outdoors, at-home, online — saves mismatched enquiries."),
  ("Qualifications and insurance.", "Quiet reassurance, especially for rehab or pre/post-natal work.")],
 [("How do personal trainers use a digital business card?",
   "Most keep the QR code on their phone and show it when someone asks about training. The person "
   "scans it, sees packages, results and a booking link, and saves the contact — no paper card and "
   "no typing a number into a phone mid-conversation."),
  ("Can clients book a session from it?",
   "Yes. Add your booking or scheduling link and it becomes the main action on the card, so an "
   "interested person can book while they are still standing in front of you."),
  ("What if my packages or prices change?",
   "Edit the card. Every QR you have already shared — on a noticeboard, a water bottle, a car "
   "sticker — shows the new version, so seasonal pricing does not mean reprinting."),
  ("Is it really free?", "Yes. The free plan includes " + FREE_SPEC)])

ELECTRICIAN = profession(
 "digital-business-card-for-electricians.html", "Digital Business Card for Electricians",
 "Digital Business Card for Electricians & Sparkies | CompanyCard",
 "A digital business card for electricians — show your certifications before you're asked, take "
 "callouts with one tap, and change your number without re-signwriting the van.",
 'Digital business card for <span class="gradient-text">electricians</span>',
 "Electrical work is hired on trust and urgency. A card that shows your certifications and calls "
 "you in one tap does more than any amount of design.",
 ["Homeowners hiring an electrician are checking two things: are you qualified, and can you come "
  "out. A digital card answers both in the same screen — certifications and registrations visible "
  "without asking, and a tap-to-call number at the top.",
  "The reprint problem is severe in the trades. Your details are on the van, the board outside a "
  "job, the quote, the invoice and the certificate you leave behind. Changing a phone number "
  "normally invalidates all of it. A permanent QR code does not — you edit the card instead.",
  "It is also where the work you have done belongs: consumer unit upgrades, EV charger installs, "
  "rewires, testing and inspection. Photos and a service list stop the enquiries you do not want "
  "and win the ones you do."],
 [("Tap-to-call, above everything else.", "Electrical enquiries are phone calls, often urgent."),
  ("Your certifications and registrations.", "Homeowners look for them; display whatever your scheme requires."),
  ("The work you take.", "Rewires, EV chargers, consumer units, testing — be specific."),
  ("Emergency availability.", "If you do callouts, say so; if you don't, say that too."),
  ("Photos of finished work.", "Boards and installs photograph well and build trust fast."),
  ("Your service area.", "Saves both of you a call that was never going to work.")],
 [("What should an electrician's digital business card include?",
   "A tap-to-call number, your certifications and scheme registration, the kinds of electrical work "
   "you take, your service area and whether you do emergency callouts. Photos of finished work "
   "help more than a logo. Display whatever your registration scheme requires."),
  ("How do I use it on the van and on jobs?",
   "Put the QR code on the van, on job boards and on your quotes, invoices and certificates. A "
   "homeowner scans it, sees your credentials and taps once to call — and you are saved in their "
   "phone for the next job."),
  ("What if my number or service area changes?",
   "You edit the card and every QR already printed keeps working with the new details. That is the "
   "main reason to put a code on the van rather than a number."),
  ("Do customers need an app?",
   "No. They scan with the normal camera app and the card opens in the browser. Saving your number "
   "is one tap.")])

EVENTS = {
 "slug": "digital-business-card-for-events.html",
 "crumb": "Digital Business Card for Events",
 "title": "Digital Business Cards for Events, Conferences & Networking | CompanyCard",
 "meta": ("Use a digital business card at events and conferences — share by QR from a lanyard or "
          "phone, get saved instantly, and follow up with people who actually remember you.",),
 "og": "Digital business cards for events and conferences — share by QR, get saved instantly.",
 "h1": 'Digital business cards for <span class="gradient-text">events &amp; conferences</span>',
 "lead": ("Conferences are where paper cards go to die — collected politely, pocketed, and binned at "
          "the airport. A code someone scans puts you in the phone instead of the bin."),
 "cta_btn": "Create your free card",
 "cta2": ("Compare the options", "best-digital-business-card.html"),
 "cta_h": "Get saved, not collected",
 "cta_p": "Free forever — and a wallet pass so your code opens without unlocking an app.",
 "howto_name": "How to use a digital business card at an event",
 "howto": [
   "Add your card to Apple or Google Wallet before you travel, so the QR opens from a locked phone.",
   "Put the QR on your lanyard insert or phone case as a backup for when a queue forms.",
   "When you meet someone, show the code and let them scan — they save you in one tap.",
   "Add a note in your phone the same evening while you still remember the conversation.",
 ],
 "sections": [],
 "faqs": [
   ("Are digital business cards good for conferences?",
    "They are better than paper for the part that matters — being saved rather than collected. A "
    "scan puts your details straight into the other person's phone with your links attached, so "
    "your follow-up email is not the first time they see who you are."),
   ("What if the venue wifi is bad?",
    "Keep your card in Apple or Google Wallet before you travel. The pass and your QR code are "
    "stored on your phone, so the code displays with no signal. The person scanning does need a "
    "connection to load your card, so if reception is poor let them scan and open it later."),
   ("How do I share my card without holding up a queue?",
    "Two tricks: keep the wallet pass ready so the code is two taps from a locked screen, and print "
    "the same QR on your lanyard insert so people can scan it while you are still talking to "
    "someone else."),
   ("Should I still bring paper cards to an event?",
    "A few, for people who expect one — some industries and cultures still do. Treat them as a "
    "courtesy and the digital card as the one that actually gets saved. Printing the QR on the "
    "paper card gives you both."),
   ("How do I follow up afterwards?",
    "Because they saved you as a contact with your links attached, your follow-up lands with "
    "context already in place. Add a one-line note about the conversation the same evening — that, "
    "not the card, is what makes the follow-up work."),
 ],
 "related": [("Apple & Google Wallet", "digital-business-card-apple-wallet.html"),
             ("QR code business card", "qr-code-business-card.html"),
             ("For small business", "digital-business-card-for-small-business.html"),
             ("Digital vs paper", "digital-business-card-vs-paper.html")],
}
EVENTS["meta"] = EVENTS["meta"][0] if isinstance(EVENTS["meta"], tuple) else EVENTS["meta"]

EVENTS["sections"] = [
  prose("Why paper fails specifically at events", [
    "Nothing is wrong with a paper card until you are the eleventh person to hand one over. By the "
    "end of a conference someone has a stack of rectangles with no memory attached to any of them, "
    "and the ones that get followed up are the ones already in the phone.",
    "A scanned card skips that entirely. Your details land in their contacts with your links "
    "attached, at the moment they are actually interested — which is also the moment they are most "
    "likely to tap through and look at your work.",
  ]),
  block("What actually goes wrong, and the fix", table(
    ["The moment", "What goes wrong with paper", "What to do instead"],
    [["<b>Busy stand, queue forming</b>", "You fumble for a card, they pocket it unread",
      "QR on your lanyard insert — they scan while you keep talking"],
     ["<b>Bad reception in a hall</b>", "n/a — but your app-based card won't load either",
      "Wallet pass: the code is stored on your phone and displays offline"],
     ["<b>You ran out on day two</b>", "Nothing to give", "Nothing to run out of"],
     ["<b>Follow-up a week later</b>", "They don't remember which card was you",
      "They saved you with your links, so your name has context"],
     ["<b>Your title changed after the event</b>", "Every card you handed out is now wrong",
      "Edit the card; everything already shared updates"]])),
  block("Before you travel", checklist([
    ("Add the card to Apple or Google Wallet.", "So the QR opens from a locked phone, offline."),
    ("Print the QR on your lanyard insert.", "Lets people scan you while you're mid-conversation."),
    ("Put one clear next step on the card.", "A booking link beats a phone number at an event."),
    ("Check it on someone else's phone first.", "Count the taps to save you. More than three is friction."),
    ("Bring a few paper cards anyway.", "For the people who expect one — print the same QR on them."),
  ]), tint=True),
]

PAGES8 = [MORTGAGE, TRAINER, ELECTRICIAN, EVENTS]
