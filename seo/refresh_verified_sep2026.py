# -*- coding: utf-8 -*-
"""Monthly competitor re-verification — September 2026.

All eight card vendors were re-fetched from their own pricing pages on
2026-09-01 (blinq.me/pricing, hihello.com/pricing, uniqode.com/pricing,
mobilocard.com/pricing-2, wavecnct.com/pages/pricing, popl.co/pages/pricing,
v1ce.co/pricing, linqapp.com). Every PRICE and LIMIT asserted on the site still
matches. Two ATTRIBUTED WORDINGS had gone stale — the substance survived in both
cases, but the words we put in the vendor's mouth are no longer on their page:

  1. linq-alternative.html quoted Linq's headline as
     "APIs for iMessage, RCS, SMS, and Voice built for Agents".
     That string is GONE from linqapp.com. Today the <title> is "Communication
     APIs for Messaging and Voice | Linq" and the h1 is "Build robust messaging
     capabilities in minutes". The page's thesis (Linq left the digital business
     card category) is now stronger, not weaker: the phrase "business card" does
     not occur anywhere on linqapp.com's homepage. Quote replaced with today's
     wording in all three copies — visible prose, visible FAQ answer, and the
     FAQPage JSON-LD (the last two must stay byte-identical).

  2. small-business-toolkit-2027.html said Blinq's pricing page "states that a
     minimum payment equal to 5 Team Cards is required for all Business
     subscriptions". "Team Cards" and "minimum payment" no longer appear on
     blinq.me/pricing. Blinq rewrote the copy; the five-card floor is still real
     and now lives in their billing FAQ: "Blinq Business is billed per card, per
     month ... you choose how many cards to start with (minimum of five)".
     Sentence rewritten to match what the page says today.

This is the fifth instance of the stale-vendor-claim family, and the first two
where the FIGURE was right and only the QUOTATION was wrong. Re-verifying prices
alone would not have caught either one. Re-read quoted strings, not just numbers.

DATE STAMPS. Bumped to September 2026 only on pages whose every source was
re-read today (the card-vendor pages). Deliberately NOT bumped:
  * vcard-qr-code.html — its sources are RFC 6350/2426 and Denso Wave, not
    vendor pricing; not re-fetched today, so its August stamp stays honest.
  * small-business-toolkit-2027.html — it also cites Zoho Invoice, Calendly,
    Wave Accounting and Trello, which were NOT re-verified today. The corrected
    Blinq sentence carries its own inline "1 September 2026" instead. The page's
    non-card claims are flagged in growth/geo-log.md as next run's work.
  * the llms.txt line describing the toolkit page, for the same reason.

Idempotent. Run from repo root: python3 seo/refresh_verified_sep2026.py
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

# ---------------------------------------------------------------- content fixes

# --- 1. Linq: the quoted headline is stale in three places -------------------
# The FAQ answer exists twice (visible <p> and FAQPage JSON-LD) and the two must
# match byte for byte, so it is defined once and emitted with the right quoting.
LINQ_FAQ_OLD = ('As of {m} 2026, linqapp.com presents itself as a developer messaging '
                'platform — its headline is {q}APIs for iMessage, RCS, SMS, and Voice '
                'built for Agents{q} — not a digital business card product.')
LINQ_FAQ_NEW = ('As of September 2026, linqapp.com presents itself as a developer messaging '
                'platform — its homepage headline is {q}Build robust messaging '
                'capabilities in minutes{q} and the phrase {q}business card{q} does not '
                'appear on it — not a digital business card product.')

LINQ_PROSE_OLD = ('linqapp.com now leads with "APIs for iMessage, RCS, SMS, and Voice built '
                  'for Agents". It is a developer messaging company.')
LINQ_PROSE_NEW = ('linqapp.com now leads with "Build robust messaging capabilities in minutes" '
                  'and titles itself "Communication APIs for Messaging and Voice". It is a '
                  'developer messaging company, and the phrase "business card" does not appear '
                  'anywhere on its homepage.')

# --- 2. Blinq's five-card floor: right number, wrong attribution -------------
TOOLKIT_OLD = ('Blinq’s pricing page states that a minimum payment equal to 5 Team Cards '
               'is required for all Business subscriptions')
TOOLKIT_OLD_ALT = ("Blinq's pricing page states that a minimum payment equal to 5 Team Cards "
                   "is required for all Business subscriptions")
TOOLKIT_NEW = ("Blinq's pricing page states that Business is billed per card, per month, and "
               "that you start with a minimum of five cards (checked 1 September 2026)")

# ------------------------------------------------------------------ date stamps
# Only pages whose every cited source was re-read on 2026-09-01.
RESTAMP = [
    "best-digital-business-card.html",
    "best-virtual-business-card.html",
    "free-digital-business-card-comparison.html",
    "hihello-alternative.html",
    "uniqode-alternative.html",
    "wave-connect-alternative.html",
    "v1ce-alternative.html",
    "popl-alternative.html",
    "blinq-alternative.html",
    "mobilo-alternative.html",
    "linq-alternative.html",
    "digital-business-card-cost.html",
    "hihello-vs-blinq.html",
    "digital-business-card-for-small-business.html",
]
DATE_SUBS = [
    ("27 August 2026", "1 September 2026"),
    ("22 August 2026", "1 September 2026"),
    ("19 August 2026", "1 September 2026"),
    ("August 2026", "September 2026"),   # catch-all, after the dated forms
]

changed = {}


def bump_dates(text):
    for old, new in DATE_SUBS:
        text = text.replace(old, new)
    return text


# ---- Linq page --------------------------------------------------------------
f = "linq-alternative.html"
t = orig = open(f, encoding="utf-8").read()
n = 0
for month in ("August", "September"):          # idempotent: catch either stamp
    for qs, qr in ((r'\"', r'\"'), ('"', '"')):   # JSON-escaped and plain forms
        old = LINQ_FAQ_OLD.format(m=month, q=qs)
        if old in t:
            t = t.replace(old, LINQ_FAQ_NEW.format(q=qr))
            n += 1
if LINQ_PROSE_OLD in t:
    t = t.replace(LINQ_PROSE_OLD, LINQ_PROSE_NEW)
    n += 1
if n != 3 and "APIs for iMessage" in t:
    sys.exit("FAIL: expected 3 Linq quote replacements, made %d" % n)
t = bump_dates(t)
if t != orig:
    open(f, "w", encoding="utf-8").write(t)
    changed[f] = n

# ---- toolkit page: content fix only, no stamp bump --------------------------
f = "small-business-toolkit-2027.html"
t = orig = open(f, encoding="utf-8").read()
hits = 0
for old in (TOOLKIT_OLD, TOOLKIT_OLD_ALT):
    if old in t:
        hits += t.count(old)
        t = t.replace(old, TOOLKIT_NEW)
if hits == 0 and TOOLKIT_NEW not in t:
    sys.exit("FAIL: Blinq minimum-payment sentence not found in " + f)
if t != orig:
    open(f, "w", encoding="utf-8").write(t)
    changed[f] = hits

# ---- the same stale Blinq wording, on two more pages ------------------------
# "Team Cards" and "minimum payment" are both gone from blinq.me/pricing. Two of
# these five were set as DIRECT QUOTATIONS, which is the worst form for a claim
# to go stale in. Blinq's billing FAQ today reads: "Blinq Business is billed per
# card, per month, for the team cards in your account. When you sign up you
# choose how many cards to start with (minimum of five)". The replacements below
# quote that verbatim where a quotation is wanted, and paraphrase it otherwise.
BLINQ_SUBS = [
    ("Blinq requires a minimum payment equal to five Team Cards",
     "Blinq bills Business per card and starts you at a minimum of five cards"),
    ("“A minimum payment equal to 5 Team Cards is required”, and billing is per "
     "card rather than per person",
     "“You choose how many cards to start with (minimum of five)”, and billing is "
     "per card rather than per person"),
    ("Blinq’s Business plan requires “a minimum payment equal to 5 Team Cards”",
     "Blinq’s Business plan is billed per card and you “choose how many cards to "
     "start with (minimum of five)”"),
    ("Blinq's Business plan requires “a minimum payment equal to 5 Team Cards”",
     "Blinq's Business plan is billed per card and you “choose how many cards to "
     "start with (minimum of five)”"),
]
for f in ("digital-business-card-cost.html", "hihello-vs-blinq.html"):
    t = orig = open(f, encoding="utf-8").read()
    k = 0
    for old, new in BLINQ_SUBS:
        k += t.count(old)
        t = t.replace(old, new)
    if "minimum payment" in t:
        sys.exit("FAIL: stale 'minimum payment' wording still in " + f)
    if t != orig:
        open(f, "w", encoding="utf-8").write(t)
        changed[f] = changed.get(f, 0) + k

# ---- remaining card-vendor pages: stamps only -------------------------------
for f in RESTAMP:
    if f == "linq-alternative.html":
        continue
    t = orig = open(f, encoding="utf-8").read()
    t = bump_dates(t)
    if t != orig:
        open(f, "w", encoding="utf-8").write(t)
        changed[f] = orig.count("August 2026")

# ---- llms.txt: line-wise, skipping the toolkit line -------------------------
f = "llms.txt"
lines = open(f, encoding="utf-8").read().split("\n")
out, hit = [], 0
for ln in lines:
    if "small-business-toolkit-2027" in ln:      # not re-verified today
        out.append(ln)
        continue
    new = bump_dates(ln)
    if new != ln:
        hit += 1
    out.append(new)
open(f, "w", encoding="utf-8").write("\n".join(out))
if hit:
    changed[f] = hit

for k, v in sorted(changed.items()):
    print("  updated %-46s (%d)" % (k, v))
print("files changed: %d" % len(changed))
