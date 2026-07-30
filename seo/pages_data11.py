# -*- coding: utf-8 -*-
"""Batch 11: dentists, chiropractors, event planners.

Drafted 2026-07-30 via a drafting+adversarial-verification workflow: each draft
was independently checked twice against the honesty rules before assembly, and
the checkers caught soft implied statistics ("Most couples check Instagram...",
"Dozens of couples photograph your QR code...", "Many practices are cash-based")
which were rewritten as conditionals or mechanisms before anything was rendered.

Same discipline as batches 8/10: trade-specific substance (how the trade is
hired, what a prospect checks, the one load-bearing field), product claims held
to /pricing, no competitor claims, and licensing/board rules never stated as
universal fact ("check your dental board / chiropractic board / local
requirements"). The event-planners page deliberately targets the PROFESSION and
cross-links digital-business-card-for-events.html (attending events), which
covers the other intent.

Content below is byte-exact from the verified drafts (assembled
programmatically; see growth/geo-log.md 2026-07-30).
"""
from build_pages import prose, block, checklist, steps_howto

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

REL = [("For small business", "digital-business-card-for-small-business.html"),
       ("For freelancers & self-employed", "digital-business-card-for-freelancers.html"),
       ("Free digital business card", "free-digital-business-card.html"),
       ("QR code business card", "qr-code-business-card.html")]


def profession(d, related=None):
    return {
     "slug": d["slug"], "crumb": d["crumb"], "title": d["title"], "meta": d["meta"],
     "og": d["meta"],
     "h1": 'Digital business card for <span class="gradient-text">' + d["h1_span"] + '</span>',
     "lead": d["lead"],
     "cta_btn": "Create your free card",
     "cta2": ("What's in the free plan", "free-digital-business-card.html"),
     "cta_h": "A card that keeps up with the work",
     "cta_p": "Free forever, no credit card, and your link never changes.",
     "sections": [
        prose("Why it matters in this line of work", d["why"]),
        block("What to put on it", checklist([tuple(i) for i in d["include_items"]]), tint=True),
        block("Setting it up", steps_howto([
          "Open the <a href=\"app/builder.html\">builder</a> and add your name, practice and role.",
          "Add the contact routes clients actually use, plus your booking or enquiry link.",
          "Add your logo and brand colour so it looks like you, not a template.",
          "Share it by <a href=\"qr-code-business-card.html\">QR code</a>, link or wallet pass — no app needed at the other end.",
        ])),
     ],
     "faqs": [tuple(f) for f in d["faqs"]] + [("Is it free to start?", "Yes. The free plan includes " + FREE_SPEC)],
     "related": related or REL,
    }


DENTISTS_DRAFT = {'slug': 'digital-business-card-for-dentists.html',
 'crumb': 'Digital Business Card for Dentists',
 'title': 'Digital Business Card for Dentists | CompanyCard',
 'meta': 'A digital business card for dentists and dental practices: QR code, sharing link and '
         'Wallet pass, with your booking link and new-patient status always current.',
 'h1_span': 'dentists',
 'lead': 'Dentistry is local and referred: a patient recommends you, a GP mentions your name, '
         'a general dentist sends a case to a specialist. Your card has to survive that '
         "hand-off — and still show whether you're taking new patients when it's finally "
         'opened.',
 'why': ['New patients arrive by recommendation: a GP suggests a local practice, a hygienist '
         'mentions a dentist by name, a general dentist hands a patient the details of an '
         'orthodontist or oral surgeon. In those hand-offs, the person passing your card on '
         "isn't the patient — so its real job is to travel: open cleanly from a message, name "
         'the practice unmistakably, and put the booking link one tap away for whoever finally '
         'uses it.',
         'Before a new patient calls, they check three things: where the practice is, whether '
         'you are actually taking new patients, and what insurance or payment options you '
         'accept. A paper card answers none of them reliably. A digital card can carry the '
         'practice address, your current new-patient status and the plans you work with — and '
         'because every shared QR code and link opens the live version, that status is never a '
         'year out of date.',
         "If you are a specialist, the card's audience is other dentists. An orthodontist or "
         'periodontist lives on referrals from general practices, which means the goal is to '
         "be saved in every referring dentist's phone — a shared link and Wallet pass do that "
         'better than a card in a drawer. And when an associate joins, hours change, or you '
         'reopen the book to new patients, the QR on your referral slips and front desk keeps '
         'pointing at the current version.'],
 'include_items': [['The practice, front and centre.',
                    'Practice name, address and a link to directions — patients choose a '
                    'dentist they can actually get to.'],
                   ["Whether you're accepting new patients.",
                    "State it plainly and update it the day it changes; it's the first thing a "
                    'prospective patient wants settled.'],
                   ['Your booking link.',
                    'Online booking or a tap-to-call number — the card should end in an '
                    'appointment, not a note to ring later.'],
                   ['Insurance and payment options.',
                    'List the plans and schemes you accept so patients can rule themselves in '
                    'before they call.'],
                   ['What you do, specifically.',
                    'General dentistry, orthodontics, implants, oral surgery — referring '
                    'dentists and patients both need to know what to send you.'],
                   ['A referral route for professionals.',
                    'Specialists: add a direct line or referral email so a general dentist can '
                    'send a case without joining the patient queue.']],
 'faqs': [["What should a dentist's digital business card include?",
           'The practice name and address, whether you are accepting new patients, a booking '
           'link or direct phone number, the insurance and payment plans you accept, your '
           'services or specialty, and a link to your practice website. If you display '
           "qualifications or specialist titles, check your dental board's advertising rules "
           'first — what you may state varies by jurisdiction.'],
          ['How do dental specialists use digital business cards for referrals?',
           "For an orthodontist, oral surgeon, periodontist or endodontist, the card's main "
           'audience is referring general dentists. Share it so each practice can save your '
           'details to their phones and keep it behind the front desk. Because the shared link '
           'and QR always open your current details, the referral route stays correct when '
           'your team, address or availability changes — no reprinting or re-sending.'],
          ["Do patients need an app to open a dentist's digital business card?",
           'No. A CompanyCard digital business card opens as a normal web page when a patient '
           'scans the QR code or taps the link — nothing to install. That matters at a front '
           'desk or community event, where you get one scan and no patience for downloads. The '
           "card itself can also live in your own Apple or Google Wallet, so it's ready to "
           'show without hunting for paper.'],
          ['Can I change my details after the QR code is printed on referral slips?',
           'Yes. The QR code and link point to the card, not to a snapshot of it, so edits '
           'show up everywhere the code already exists. Close the book to new patients, change '
           'your hours, add an associate or update your insurance list, and referral slips, '
           'appointment cards and the front desk sign all show the current version. Edits are '
           'unlimited.']]}

CHIROPRACTORS_DRAFT = {'slug': 'digital-business-card-for-chiropractors.html',
 'crumb': 'Digital Business Card for Chiropractors',
 'title': 'Digital Business Card for Chiropractors | CompanyCard',
 'meta': 'A digital business card for chiropractors: QR code, link and wallet pass carrying '
         'your booking link, what you treat and fees — editable forever, no app needed.',
 'h1_span': 'chiropractors',
 'lead': 'Chiropractic work arrives by word of mouth — a patient whose back got better tells a '
         'friend, a trainer sends a client across the road. Your card has to survive that '
         'forward and reassure a stranger in pain enough to book a first visit.',
 'why': ['Chiropractors get hired three ways: a patient whose pain got better tells a friend, '
         'a trainer or massage therapist sends someone across, or a stranger searches for help '
         "nearby. In every case the introduction happens on someone else's phone. Your card's "
         'real job is to forward well — open cleanly in a message from a patient to their '
         'friend with a bad back, and look credible to someone who has never met you.',
         'A prospect with a sore neck checks specific things before booking: do you treat '
         'their problem, what happens at a first visit, what techniques you use, and what it '
         'costs. If your practice is cash-based or sells treatment packages, saying so upfront '
         'filters better than any slogan. Put what you treat in plain words — back, neck, '
         'sports injuries, pregnancy-related pain — alongside your qualifications, so a '
         'cautious stranger can decide in one scroll.',
         'The referral that matters often lands months after you handed anything over. Your '
         "card sits in a past patient's phone, on a gym noticeboard as a QR code, in a "
         "physio's contacts — and every one of those copies shows whatever your card says "
         'today. Change your fees, add a technique, move clinics or open Saturday hours, and '
         'the link a patient forwarded last winter still books into the right diary.'],
 'include_items': [['Your new-patient booking link.',
                    'The one field that earns its place — a forwarded card should turn into a '
                    'booked first visit without a phone call.'],
                   ['What you treat.',
                    'Back pain, neck pain, sports injuries, pregnancy-related pain — name the '
                    'problems, not just the discipline.'],
                   ['Techniques you use.',
                    'Adjustment, mobilisation, soft tissue work — a line each in plain '
                    'language, so nobody arrives expecting something else.'],
                   ['How you charge.',
                    'Cash-based, packages, or insurance accepted — stating your model upfront '
                    'saves awkward first-visit conversations.'],
                   ['Qualifications and registration.',
                    'Your degree and board or association registration reassure a stranger — '
                    "check your chiropractic board's rules on how to present them."],
                   ['What a first visit involves.',
                    'How long it takes, what you assess, and whether treatment starts on day '
                    'one — the question every nervous first-timer has.']],
 'faqs': [['What should a chiropractor put on a digital business card?',
           'Your name and clinic, the problems you treat (back, neck, sports injuries, '
           'pregnancy-related pain), the techniques you use, your qualifications and '
           'registration, how you charge, and a direct link to book a new-patient appointment. '
           'If your chiropractic board has rules on how credentials or titles appear in '
           'advertising, follow those. The booking link matters most — a forwarded card should '
           'end in a booked visit, not a phone-tag exchange.'],
          ['How do chiropractors get referrals from gyms and personal trainers?',
           'Make yourself easy to pass on. Give trainers, massage therapists and physios '
           'something they can forward in a message rather than a paper card that stays in a '
           'drawer: a link or QR code that opens your profile with what you treat and a '
           'booking link. When a client mentions a bad back, the referral happens in ten '
           'seconds on the gym floor, and the card they forward is always current.'],
          ["Do patients need an app to open a chiropractor's digital business card?",
           "No. A CompanyCard opens in the phone's browser from a QR scan or a shared link — "
           'the patient installs nothing and creates no account. You can also keep your own '
           'card as a pass in Apple Wallet or Google Wallet, so the QR code is ready at the '
           'front desk, at the gym, or anywhere a conversation turns into a referral.'],
          ['Can patients book an appointment directly from a digital business card?',
           'Yes, if you put your booking link on it. The card itself is not a scheduler — it '
           "links to whatever system you already use, so tapping 'book a first visit' opens "
           'your live calendar. Because the card is editable forever, switching booking '
           'systems later does not break anything: every QR code and link you have ever shared '
           'simply points at the updated card.']]}

EVENT_PLANNERS_DRAFT = {'slug': 'digital-business-card-for-event-planners.html',
 'crumb': 'Digital Business Card for Event Planners',
 'title': 'Digital Business Card for Event & Wedding Planners | CompanyCard',
 'meta': 'A digital business card for event and wedding planners: portfolio link, enquiry link '
         'and a QR code built for bridal fairs. Every edit updates every shared card.',
 'h1_span': 'event planners',
 'lead': 'Planners are hired once, on portfolio and trust, for a day that cannot be re-run. '
         'Your card travels — venue coordinator to couple, florist to client, past bride to '
         'engaged friend — and it has to show real events and an enquiry route wherever it '
         'lands.',
 'why': ['Planning work often arrives sideways. A venue coordinator mentions you to a couple, '
         'a florist or photographer passes your name along, a past client tells an engaged '
         'friend. The person holding your card is often not the one you gave it to, so its '
         'real job is to forward well: open cleanly from a link in a message, make sense to a '
         'stranger, and show what you plan and how to enquire.',
         'Hiring a planner is a one-shot purchase — nobody re-runs a wedding or a product '
         'launch. Before a prospect contacts you, they want proof it went well for someone '
         'else: real events you have planned, the types you take on, roughly where you work, '
         'and an easy next step. The portfolio link is the load-bearing field; the enquiry or '
         'consultation link is what turns a look into a conversation.',
         'Bridal and trade fairs are scan-heavy. Couples photograph your QR code throughout '
         'the day, and the decision often comes months later. A printed card is frozen at '
         'print day; a CompanyCard QR or link always opens the current version, so when your '
         'packages, portfolio or phone number change, everyone who scanned you at the spring '
         "fair still lands on this season's details. The same goes for vendors who saved your "
         'card years ago.'],
 'include_items': [['A portfolio of real events.',
                    'Link to a gallery or highlights page — planners are hired on what they '
                    'have actually delivered, not on promises.'],
                   ['The event types you take on.',
                    'Weddings, corporate events, private parties, launches — say it plainly so '
                    'venues and vendors know when to pass you along.'],
                   ['An enquiry or consultation link.',
                    'A booking form or a check-my-date link turns a scan at a fair into a '
                    'conversation instead of a lost brochure.'],
                   ['Your service area.',
                    'Venues and vendors refer locally — name the cities or regions you cover '
                    'and say whether you travel.'],
                   ['A direct contact route.',
                    'Events are coordinated by phone and message; list the number clients and '
                    'vendors should actually use on the day.'],
                   ['Your Instagram and socials.',
                    'Couples often look you up on Instagram before they ever email — put it '
                    'one tap away instead of making them search for you.']],
 'faqs': [["What should an event planner's digital business card include?",
           'Your name and business, the event types you plan — weddings, corporate, private '
           'parties — a portfolio link showing real events, your service area, a direct phone '
           'or WhatsApp route, your Instagram, and an enquiry or consultation link. If your '
           'market expects particular credentials or association memberships, add them, and '
           'check your own local requirements, since these vary by country.'],
          ['How do wedding planners use a QR code at bridal fairs?',
           'Put the code on your stand banner, brochures and phone lock screen so couples can '
           'scan instead of typing. The scan opens your live card with your portfolio and '
           'enquiry link — nothing for them to install. Because the code points to the current '
           'version of your card, you can update packages and photos after the fair, and '
           'everyone who scanned still sees the latest details months later when they decide.'],
          ['Do clients need an app to open a digital business card?',
           "No. A CompanyCard opens in the recipient's web browser from a QR scan or a shared "
           'link, so couples, corporate clients and vendors see your card without installing '
           'anything. You can also keep your own card as an Apple or Google Wallet pass, so it '
           'is ready to show at fairs, venue walkthroughs and vendor meetings.'],
          ['How do event planners get more referrals from venues and vendors?',
           'Make your card effortless to pass on. Florists, caterers, photographers and venue '
           'coordinators refer planners in messages, so give them a link that opens cleanly, '
           'states your event types and service area, and shows a real portfolio to a '
           'stranger. Because a digital card is always current, a vendor who saved it years '
           'ago still forwards working details, not an old number.']]}

REL_EP = [('Digital business cards for events & conferences', 'digital-business-card-for-events.html'),
 ('For small business', 'digital-business-card-for-small-business.html'),
 ('Free digital business card', 'free-digital-business-card.html'),
 ('QR code business card', 'qr-code-business-card.html')]

DENTISTS = profession(DENTISTS_DRAFT)
CHIROPRACTORS = profession(CHIROPRACTORS_DRAFT)
EVENT_PLANNERS = profession(EVENT_PLANNERS_DRAFT, related=REL_EP)

PAGES11 = [DENTISTS, CHIROPRACTORS, EVENT_PLANNERS]
