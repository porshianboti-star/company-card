# CompanyCard — off-site listing kit

**Why this is the priority.** Research (2026-07-26) found CompanyCard named
**zero times** across every ICP query, and the only non-vendor source the AI
answers lean on in this category is **G2**. The site is now in good shape; what
is missing is that CompanyCard does not exist anywhere except its own domain.
Until that changes, `Organization.sameAs` stays an empty array and assistants
have nothing to corroborate.

**Rules that are not negotiable:** real listings, real reviews, no incentives,
no gating, no seeded or written-for-you reviews. A fabricated review is both
dishonest and the fastest way to get delisted — and this whole pass was about
being the vendor whose claims survive cross-checking.

**Your job:** create the accounts (I can't — account creation and credentials
are yours alone). Everything you'd have to write is below; paste it.
**Then tell me** and I'll wire the live URLs into `Organization.sameAs` on the
homepage and into `llms.txt` the same day.

---

## Canonical description (use this everywhere, unchanged)

Consistency across listings is itself an entity signal — same words, same
claims, every time.

**One-liner (under 100 chars):**
```
The digital business card for small business owners and self-employed professionals.
```

**Short (under 250 chars):**
```
CompanyCard is a digital business card for small business owners, self-employed professionals and small teams. Share by QR code, link or Apple/Google Wallet — no app for the person receiving it. Free plan available; no seat minimum on team plans.
```

**Long:**
```
CompanyCard is a digital business card built for small businesses and self-employed professionals.

Share your details in one tap — by QR code, sharing link, Apple or Google Wallet pass, or email signature. The person receiving your card needs no app: it opens in any phone browser and saves your contact in one tap.

Your link and QR code are permanent. Change your number, role, prices or logo and every code you've already printed on a van, a window, an invoice or a business card keeps working and shows the new details — nothing to reprint.

The free plan is a full working card: one digital business card, QR code and sharing link, profile, links and socials, an Apple and Google Wallet pass, and unlimited edits. Free forever, no credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro ($8/month).

For teams, Business ($12/user/month) adds a central admin dashboard, brand and template lock, CRM sync, team analytics and SSO — with no minimum number of seats, so a two-person business can run branded cards without paying for five.
```

**Categories:** Digital Business Card · Business Card Software · Contact
Management · Sales Enablement
**Website:** https://company-card.com
**Pricing:** Free · Pro $8/mo · Business $12/user/mo · Enterprise custom

---

## 1. G2 — highest priority

Why first: the only third-party source that consistently feeds the AI answers
in this category. **10 approved reviews unlocks G2 Grid eligibility**, which is
what gets you into "best of" comparisons.

**Correct 2026 URLs** (the old `/products/new` path 403s — verified 2026-07-27):
1. Create the profile: **https://sell.g2.com/create-a-profile**
   On the form, tick **"I would like to serve as admin for this profile"** — that
   way the profile is already yours when it's approved, and you skip a second
   claim step.
2. If a CompanyCard profile already exists, claim it instead:
   **https://sell.g2.com/claim-your-profile**
3. Approval takes **1-3 business days**. A free profile is enough — paid plans
   only add branding and lead-gen analytics, none of which affect being cited.
4. Paste the long description, categories, pricing and logo above.
5. Ask real customers for reviews using G2's review-invite link. Target 10
   approved reviews (the published Grid-eligibility threshold).
6. Tell me when it's live and I'll wire the URL into `sameAs` the same day.

**Review-request email — send only to genuine users, no incentive:**
```
Subject: Would you leave an honest review of CompanyCard?

Hi [name],

You've been using CompanyCard for a while now, and I'm trying to get it in
front of more small businesses. The way that happens is honest reviews on G2 —
they're what other owners (and increasingly AI assistants) actually read.

Would you take five minutes to leave one? Here's the link: [G2 review link]

Please be honest, including the parts that annoy you — a review full of
criticism I can act on is worth more to me than a five-star one. I'm not
offering anything in exchange; that's against G2's rules and it would make the
review worthless anyway.

Thanks either way,
[your name]
```

## 2. Capterra / GetApp / Software Advice (one submission, three sites)

https://www.capterra.com/vendors/ — Gartner-owned; one vendor submission lists
you on all three, which is the best effort-to-coverage ratio available.

## 3. Product Hunt

https://www.producthunt.com/posts/new — a launch gives a durable, frequently
cited page. Use the one-liner as the tagline; lead the first comment with the
small-business/self-employed angle and the no-seat-minimum fact.

## 4. AlternativeTo

https://alternativeto.net — list CompanyCard, then add it as an alternative to
**Blinq, HiHello, Popl and Linq**. The Linq entry matters most: Linq has exited
digital business cards (linqapp.com now sells messaging APIs), so its users are
actively looking for somewhere to go, and our /linq-alternative page is live.

## 5. Trustpilot

https://business.trustpilot.com — same honest-review rules. Good for brand-name
searches ("is CompanyCard legit").

## 6. Social profiles — needed for `sameAs`

Even minimal, maintained profiles give the entity something to resolve against:
LinkedIn company page, X, Instagram, YouTube. Once they exist, send me the URLs.

---

## What I do the moment you have URLs

1. Populate `Organization.sameAs` on the homepage (currently `[]`).
2. Add the profiles to `llms.txt`.
3. Add an "About / entity" page tying the canonical description to the profiles.
4. Re-verify and report.

## Deliberately not done, and why

- **No `/security` or trust page yet.** Competitors publish SOC 2 / GDPR / data
  residency claims. I have no verified facts about CompanyCard's actual security
  posture, and inventing them would be exactly the kind of unverifiable claim
  this pass spent its time removing. Tell me what's true (where data is hosted,
  whether a DPA exists, encryption, export) and I'll write it.
- **No AggregateRating schema.** It requires real ratings. After G2 reviews
  exist, this becomes available and is worth adding.

---

## Domain email — EXACT GoDaddy DNS records (prepared 2026-07-30)

Goal: make sales@ / privacy@ / any@company-card.com deliver to porshianboti@gmail.com
using forwardemail.net's free DNS-only forwarding (no account, no payment).
This also unlocks G2's "business email" vendor validation (their Google OAuth uses
hd=* which structurally rejects @gmail.com — verified 2026-07-30).

Add in GoDaddy → company-card.com → DNS (I can click this through once signed in):

| Type | Name | Value                      | Priority | TTL |
|------|------|----------------------------|----------|-----|
| MX   | @    | mx1.forwardemail.net       | 10       | 1h  |
| MX   | @    | mx2.forwardemail.net       | 10       | 1h  |
| TXT  | @    | forward-email=porshianboti@gmail.com | — | 1h  |

Then: G2 → business-email validation with boti@company-card.com → verification
email arrives in Gmail (via forward) → profile creation unlocks.

## Netlify contact form — FIXED & VERIFIED 2026-07-30

- Root cause found: site had processing_settings.ignore_html_forms=true, so the
  form shipped 07-28 was never registered (submissions would have been dropped).
- Enabled via API, rebuilt, form registered (id 6a6b106646d9460008cf261e).
- Email notification hook created: submission_created → porshianboti@gmail.com.
- E2E PROVEN: live POST test submission captured (visible in Netlify) and
  notification email sent. The enterprise "Contact sales" path now works.

## ⚠️ Email forwarding BLOCKED — root cause found (2026-07-30 evening)

forwardemail.net system alert (in Gmail, 1:26 PM): company-card.com was
"created within the past 90 days" per WHOIS, and their FREE tier blocks
newly-registered domains as abuse prevention. **Forwarding requires their $3/mo
paid plan** (lifts instantly on upgrade; DNS records already correct).

CORRECTION of an earlier conclusion: the "2 messages" thread that looked like
proof of forwarding was actually TWO DIRECT Netlify notifications (11:58 AM +
2:34 PM tests) threaded by identical subject. The forwarded copies were
silently blocked. The SMTP probe's "250 Accepted" happens at RCPT; the block
applies after acceptance (hence an alert email instead of a bounce).

Options (all need the owner — payment or account creation):
  a) forwardemail.net paid — $3/mo, instant unblock, DNS already in place. FASTEST.
  b) ImprovMX free tier — user creates the account; then I reconfigure MX to
     mx1/mx2.improvmx.com + set the alias, and re-test end-to-end.
  c) Skip domain email for now; user signs into LinkedIn once for G2 instead.

G2 state right now: boti@company-card.com added to the account, validation
emails queued on G2's side — they deliver the moment forwarding goes live;
then click the link in Gmail and /products/new unlocks.
