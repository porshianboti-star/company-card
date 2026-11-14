#!/usr/bin/env python3
"""Competitor-claim correction pass, 2026-11-14 (rank plan CC-2, as modified by both
verifiers). Idempotent: every edit is (old, new, expected_count); an edit whose old
text is gone is skipped only if its new text is already present.

Sources, all re-read on 2026-11-14 (curl 09:58Z, plus blinq.me/pricing in a real
browser with the Monthly/Annual tab clicked):

  hihello.com/pricing  Personal "Free forever", 1 user, "2 digital business cards",
      "Scan 5 paper business cards or badges a month". Professional $8 billed
      monthly / $6 a month "$72 billed yearly" ("Billed yearly" switch on by
      default), 8 cards, 20 scans "or unlimited with add-on". Business "5-100
      users", "14 days free. 5 users minimum", $6 per user/month monthly, $5 per
      user/month yearly ("$60 per user/year"), "4 cards per user, pooled across
      your team", "50 paper cards or badges per user a month, pooled", 10 card +
      10 signature templates, Salesforce/HubSpot/Microsoft Dynamics, Google and
      Microsoft SSO with directory sync. Enterprise "Custom", "100+ users",
      unlimited cards/templates/scans, SAML/SCIM, "Custom fonts and verified
      cards", "Dedicated implementation specialist and account manager". FAQ:
      "Other people can scan your own HiHello QR code as often as they like, on
      every plan." No line about HiHello branding on the free card.
  blinq.me/pricing  (default tab = Annual)  Free "$0 Free forever": "Two free
      digital business cards", unlimited sharing, unlimited contact creation,
      "Universal contact scanner", "AI Notetaker (access notes from the last 30
      days)", Google/Apple Wallet, personal email signature, virtual backgrounds.
      Premium $9.99 monthly / $7.33 annually: up to five cards, branded QR,
      "Custom card colors & design", "Remove Blinq branding". NEW Pro (for
      individuals) $22.49 monthly / $16.58 annually: AI contact enrichment,
      unlimited AI Notetaker, "Export contacts and notes via CSV", MCP, API.
      Business $6.99 / $4.99 "Billed monthly, per card, from 5 cards" (annual:
      "Billed annually, per card, from 5 cards"); native integrations "with
      Salesforce, HubSpot, Dynamics 365 and more" (no "20+" anywhere). FAQ:
      Premium has "no Blinq branding"; "Business starts at five cards"; "billed
      per card, per month ... (minimum of five)"; "Admins and team members who
      don't have a card assigned aren't billed".
  popl.co/pages/pricing  no prices, "Request Pricing", no free tier; "you won't
      be charged extra per user, per seat, or per license". (Unchanged.)
  uniqode.com/pricing  first card free, Team $6 per user per month, annual only,
      30-day money-back guarantee. (Unchanged.)

What this fixes (live HTML, llms.txt, and the generators' text; the three generators
that still have a renderer are guarded so a re-render cannot overwrite the live page):
  * HiHello free cards four -> two, Professional sixteen -> eight, everywhere.
  * best-virtual FAQ: the retracted "no monthly cap on scans" comparison.
  * hihello-vs-blinq: description "cheaper on both paid tiers"; Blinq's scanner
    is on the FREE plan now; Premium no longer holds enrichment/export (new Pro
    tier); HiHello Business is 4 cards + 50 scans per user pooled, not
    unlimited; Blinq's "20+ CRMs" is no longer on its page; "pays for four
    cards" under a five-card minimum; $5 labelled as HiHello's yearly rate;
    stamps 13 September -> 14 November 2026 (every HiHello/Blinq figure on the
    page re-read today).
  * blinq-vs-popl: Business is "per card, from 5 cards" (was quoted "per user");
    Blinq publishes five plans; "no vendor credit" (Premium lists "Remove Blinq
    branding"); Premium no longer lists scanner/notetaker/enrichment.
  * free-digital-business-card-comparison: Blinq's free card carries Blinq
    branding (was "None listed" / "without a listed branding line").
  * digital-business-card-cost: "that theirs do not" (an affirmative negative
    that is now false for Blinq) and the HiHello "4 cards" table cell.
  * hihello-alternative: table header "verified September 2026" vs the page's
    own "verified November 2026".
  * small-business-toolkit-2027: Blinq Business "$6.99 per user/month".
Repair, same day, after the two verifiers (sections marked "repair 2026-11-14"):
  * hihello-vs-popl: HiHello Business 50 scans + 50 enrichments per user, pooled
    (unlimited only on Enterprise), not "unlimited"; plan label "Free forever".
  * digital-business-card-cost: Blinq Pro ($22.49 / $16.58) above the $3-$10 personal
    range; "several free cards" -> two each at HiHello and Blinq.
  * hihello-vs-blinq: Blinq Business event lead capture "$9.99 per lead captured and
    enriched"; "no scan count" scoped to the universal contact scanner; hero names the
    HiHello and Blinq figures only; "add-on", not "paid add-on".
  * free-digital-business-card-comparison: visible "Last updated" = dateModified; Blinq
    cheapest cell yearly-first like the other rows.
  * generators: pages_data15/19/20 content = live (render-diffed); pages_data2/4/14 and
    add_vendor_matrix flagged lines synced; overwrite guards on build_pages15/19/20;
    DO NOT RE-RUN notes on wire_batch15/19/20; accurate SUPERSEDED notes.
Stamps: a page's own "verified <date>" is moved to 14 November 2026 only where every
competitor figure under it was re-read today; elsewhere the corrected figure gets a
"(re-checked 14 November 2026)" note and the older stamp stays.

dateModified + sitemap lastmod -> 2026-11-14 for the changed URLs only. Does NOT run
add_freshness.py. Run from repo root, then: python3 seo/sync_faq_schema.py,
python3 seo/build_llms_full.py, python3 seo/check_vendor_claims.py.
"""
import json
import os
import py_compile
import re
import sys

DATE = "2026-11-14"
changed_urls = []
report = []


def apply(path, edits):
    s = open(path, encoding="utf-8").read()
    orig = s
    for old, new, n in edits:
        assert old not in new, f"{path}: new contains old, not idempotent: {old[:60]!r}"
        c = s.count(old)
        if c:
            assert c == n, f"{path}: expected {n} of {old[:80]!r}, found {c}"
            s = s.replace(old, new)
            report.append(f"{path}: {n}x {old[:60]!r}")
        else:
            assert new in s, f"{path}: anchor gone and replacement absent: {old[:90]!r}"
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)
    return s != orig


def set_date(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r'("url":\s*"https://company-card\.com/' + re.escape(path) +
                  r'"[^<]*?"dateModified":\s*")(\d{4}-\d{2}-\d{2})(")', s)
    assert m, f"{path}: WebPage dateModified not found"
    if m.group(2) != DATE:
        s = s[:m.start(2)] + DATE + s[m.end(2):]
        open(path, "w", encoding="utf-8").write(s)


# ---------------------------------------------------------------- live HTML
HTML = {}

HTML["hihello-vs-blinq.html"] = [
    ("compared on published prices, verified 1 November 2026. HiHello&#x27;s free plan gives 2 cards, "
     "the same as Blinq&#x27;s, but caps its paper-card scanner. HiHello is cheaper on both paid tiers.",
     "compared on published prices, verified 14 November 2026. HiHello&#x27;s free plan gives 2 cards, "
     "the same as Blinq&#x27;s, but caps its paper-card scanner. HiHello is cheaper for one person; "
     "the team tier is a near tie.", 1),
    ("own pricing page, read on 13 September 2026 — free-plan limits",
     "own pricing page, read on 14 November 2026 — free-plan limits", 2),
    ("Every figure below was read off each vendor's own pricing page on 13 September 2026.",
     "Every HiHello and Blinq figure below was read off each vendor's own pricing page on 14 November 2026.", 1),
    ("Blinq puts its universal contact scanner and AI notetaker in Premium with no monthly count on the page.",
     "Blinq lists a universal contact scanner and an AI notetaker on its free plan, with no monthly "
     "cap published for that scanner.", 1),
    ("<h2>Every published figure, verified 13 September 2026</h2>",
     "<h2>Every published figure, verified 14 November 2026</h2>", 1),
    ("<td>“Free Forever” — 2 digital business cards, 1 user</td>",
     "<td>“Free forever” — 2 digital business cards, 1 user</td>", 1),
    ("<td>No monthly scan count published; the contact scanner is a Premium feature</td>",
     "<td>No monthly scan count published; the free plan lists a “Universal contact scanner”</td>", 1),
    ("<td>Universal contact scanner, AI notetaker, AI contact enrichment, branded QR code, custom design, "
     "contact export</td>",
     "<td>Up to five cards, branded QR code, custom card colours and design, “Remove Blinq branding”. "
     "AI contact enrichment, unlimited AI notes and CSV export are in a separate Pro tier for one "
     "person, “$22.49 / month” or “$16.58 / month” billed annually</td>", 1),
    ("<td>Business — “$5 per user/month” or “$60 per user/year”</td>"
     "<td>Business — “$6.99 / month” per user, or “$4.99 / month” billed annually</td>",
     "<td>Business — “$6 per user/month” billed monthly, or “$5 per user/month” (“$60 per user/year”) "
     "billed yearly</td><td>Business — “$6.99 / month” “per card, from 5 cards” billed monthly, or "
     "“$4.99 / month” billed annually</td>", 1),
    ("“Billed per card, per month”", "“billed per card, per month”", 3),
    ("<td>Unlimited cards and scans, team email signatures, event lead capture, team analytics, "
     "sub-team templates, SSO &amp; directory sync</td><td>Team management, CRM sync, lead capture, "
     "event campaigns, 20+ native CRM integrations</td>",
     "<td>4 cards and 50 paper-card or badge scans per user a month, pooled across the team; email "
     "signatures deployed to Gmail and Outlook; event lead capture; team analytics; 10 card and 10 "
     "signature templates; Google and Microsoft SSO with directory sync; Salesforce, HubSpot and "
     "Microsoft Dynamics</td><td>Team cards and admin platform, admin-controlled email signatures, "
     "event lead capture with badge scanning (“$9.99 per lead captured and enriched”, credits billed "
     "monthly), event campaigns, native integrations with Salesforce, HubSpot, Dynamics 365 “and "
     "more”</td>", 1),
    ("SAML/SCIM, SOC 2, verified badges, dedicated account manager",
     "SAML/SCIM, SOC 2, verified cards, dedicated account manager", 1),
    ("Read off hihello.com/pricing and blinq.me/pricing on 13 September 2026.",
     "Read off hihello.com/pricing and blinq.me/pricing on 14 November 2026.", 1),
    ("five scans a month on free, twenty on Professional, unlimited only on the Business tier you "
     "cannot buy under five users. Blinq publishes no monthly scan count and bundles the universal "
     "contact scanner and AI notetaker into Premium.",
     "five scans a month on free, twenty on Professional (unlimited with an add-on), fifty per "
     "user a month pooled on Business, which you cannot buy under five users, and unlimited only on "
     "Enterprise. Blinq publishes no monthly cap for the universal contact scanner on its free plan (and so on every plan above it), where it also lists an AI notetaker; event lead capture on Business is billed separately, at “$9.99 per lead captured and enriched”.", 1),
    ("A ten-person business where four people need a card and the office manager administers it "
     "pays for four cards on Blinq.",
     "A ten-person business where six people need a card and the office manager administers it "
     "pays for six cards on Blinq, not ten.", 1),
    ("<b>Blinq wins on CRM reach, on paper</b> Its Business tier advertises native integrations with "
     "20+ CRMs; HiHello's Business tier advertises SSO and directory sync but does not publish a CRM "
     "count.",
     "<b>On CRM sync it is close, on paper</b> Blinq's Business tier advertises native integrations "
     "with Salesforce, HubSpot, Dynamics 365 “and more”; HiHello's Business tier lists Salesforce, "
     "HubSpot and Microsoft Dynamics.", 1),
    ("The headline is that HiHello gives four free cards and Blinq gives two, and that is true.",
     "The headline is that HiHello and Blinq give the same two free cards.", 1),
    ("Blinq's free plan is the other way round: two cards, but its page emphasises unlimited sharing "
     "and unlimited contact creation, and it does not publish a monthly cap on the free tier. The "
     "scanner is what you pay for, not something you are rationed.",
     "Blinq's free plan is the other way round: two cards, unlimited sharing and unlimited contact "
     "creation, and a “Universal contact scanner” with no monthly cap published for the free tier.", 1),
    ("Hand out: HiHello, more cards. Collect: Blinq, no scan meter.",
     "Hand out: either — both give two cards. Collect: Blinq's free scanner has no published cap; "
     "event lead capture on Business is billed per lead.", 1),
    # FAQ pairs (JSON-LD + visible, byte-identical)
    ("Blinq's gives 2 cards with unlimited sharing and no published monthly cap, but keeps its contact "
     "scanner in the paid Premium tier. On free card count the two are level. If you collect other "
     "people's cards, Blinq does not meter you.",
     "Blinq's gives 2 cards with unlimited sharing and lists a universal contact scanner with no "
     "published monthly cap. On free card count the two are level. If you collect other people's "
     "cards, Blinq publishes no limit on that scanner.", 2),
    ("billed yearly, with unlimited cards and scans, and is sold for 5 to 100 users. Enterprise is "
     "custom pricing for 100+ users. Verified 1 November 2026 on hihello.com/pricing.",
     "billed yearly, with 4 cards and 50 paper-card and badge scans per user a month, pooled across "
     "the team, and is sold for 5 to 100 users. Enterprise is custom pricing for 100+ users, with "
     "unlimited cards and scans. Verified 14 November 2026 on hihello.com/pricing.", 2),
    ("for up to 5 cards. Business is $6.99 per month, or $4.99 billed annually, with a minimum of five "
     "cards and billing per card rather than per user. Enterprise is custom. Verified 1 November 2026 "
     "on blinq.me/pricing.",
     "for up to 5 cards. Pro, also for one person, is $22.49 a month, or $16.58 a month billed "
     "annually, and adds AI contact enrichment, unlimited AI notes and CSV export. Business is $6.99 "
     "per card a month, or $4.99 billed annually, with a minimum of five cards and billing per card "
     "rather than per user. Enterprise is custom. Verified 14 November 2026 on blinq.me/pricing.", 2),
    ("while Blinq publishes no monthly scan count. Verified 1 November 2026 on each vendor's own "
     "pricing page.",
     "while Blinq publishes no monthly cap on its universal contact scanner. Verified 14 November 2026 "
     "on each vendor's own pricing page.", 2),
]

HTML["blinq-vs-popl.html"] = [
    ("Which one fits a freelancer, a small team, or an events team. Both re-checked 11 September 2026.",
     "Which one fits a freelancer, a small team, or an events team. Blinq re-checked 14 November "
     "2026, Popl 11 September 2026.", 1),
    ("as of 11 September 2026 it publishes a free plan with two cards, a Premium plan at $9.99 a "
     "month, and a Business plan at $6.99 per user a month,",
     "as of 14 November 2026 it publishes a free plan with two cards, a Premium plan at $9.99 a "
     "month, and a Business plan at $6.99 per card a month,", 2),
    ("As of 11 September 2026 blinq.me/pricing lists a Free plan (\"$0 Free forever\", two cards), "
     "Premium at $9.99 a month, and Business at $6.99 per user a month,",
     "As of 14 November 2026 blinq.me/pricing lists a Free plan (\"$0 Free forever\", two cards), "
     "Premium at $9.99 a month, Pro at $22.49 a month, and Business at $6.99 per card a month,", 1),
    ("As of 11 September 2026 Blinq publishes four plans. Free is $0 forever with two digital business "
     "cards. Premium is $9.99 a month billed monthly or $7.33 a month billed annually, with up to five "
     "cards. Business is $6.99 a month billed monthly or $4.99 a month billed annually, per user, and "
     "Blinq's billing FAQ says it is billed per card with a minimum of five cards to start.",
     "As of 14 November 2026 Blinq publishes five plans. Free is $0 forever with two digital business "
     "cards. Premium is $9.99 a month billed monthly or $7.33 a month billed annually, with up to five "
     "cards. Pro, also for one person, is $22.49 a month billed monthly or $16.58 a month billed "
     "annually. Business is $6.99 a month billed monthly or $4.99 a month billed annually, per card, "
     "from five cards, and Blinq's billing FAQ says it is billed per card, per month, with a minimum "
     "of five cards to start.", 2),
    ("Per user, yes — but not from one user. As of 11 September 2026 Blinq's Business plan card says ",
     "Per card, yes — but not from one card. As of 14 November 2026 Blinq's Business plan card says ", 2),
    ("$6.99 / month Billed monthly, per user", "$6.99 / month Billed monthly, per card, from 5 cards", 2),
    ("It loses to Blinq on the free plan (two cards and no vendor credit, against our one card with a "
     "small CompanyCard credit)",
     "It loses to Blinq on the free plan (two cards against our one; Blinq's free card carries Blinq "
     "branding, which its Premium plan removes, as our Pro removes our small CompanyCard credit)", 2),
    ("though Blinq Premium lists a contact scanner, AI notetaker and contact enrichment that Pro does not.",
     "though Blinq's free plan already lists a universal contact scanner and an AI notetaker, and "
     "Blinq Pro ($22.49 a month) adds AI contact enrichment, which our Pro does not list.", 2),
    ("<b>Where we lose.</b> Blinq's free plan is two cards with no vendor credit; ours is one card, and "
     "it carries a small CompanyCard credit that Pro removes. Blinq Premium lists a contact scanner, AI "
     "notetaker and enrichment that our Pro does not.",
     "<b>Where we lose.</b> Blinq's free plan is two cards to our one. Both free cards carry their "
     "maker's branding — Blinq lists “Remove Blinq branding” as a Premium feature, and our free card "
     "carries a small CompanyCard credit that Pro removes. Blinq's free plan also lists a universal "
     "contact scanner and an AI notetaker, and Blinq Pro adds AI contact enrichment, which our Pro "
     "does not list.", 1),
    ("<b>Blinq's Premium is also the richer individual plan.</b> $9.99 a month buys up to five cards, "
     "a universal contact scanner, an AI notetaker and AI contact enrichment.",
     "<b>Blinq also has the richer individual plans.</b> Its free plan already lists a universal "
     "contact scanner and an AI notetaker (notes from the last 30 days); Premium at $9.99 a month adds "
     "up to five cards, a branded QR code, custom design and no Blinq branding; Pro at $22.49 a month "
     "($16.58 billed annually) adds AI contact enrichment, unlimited AI notes and CSV export.", 1),
    ("Yes — Free, Premium <b>$9.99/mo</b> ($7.33 annual), Business <b>$6.99/user/mo</b> ($4.99 annual), "
     "Enterprise custom",
     "Yes — Free, Premium <b>$9.99/mo</b> ($7.33 annual), Pro <b>$22.49/mo</b> ($16.58 annual), "
     "Business <b>$6.99/card/mo</b> ($4.99 annual), Enterprise custom", 1),
    ("<td>Premium: “Create up to five cards”</td>",
     "<td>Premium: “Create up to five digital business cards”</td>", 1),
    ("<p class=\"lp-note\">Read from blinq.me/pricing, popl.co and popl.co/pages/pricing on 11 September "
     "2026; the “Popl for Individuals” link",
     "<p class=\"lp-note\">Blinq column re-read from blinq.me/pricing on 14 November 2026, with both "
     "billing tabs; Popl read from popl.co and popl.co/pages/pricing on 11 September 2026; the "
     "“Popl for Individuals” link", 1),
]

HTML["best-virtual-business-card.html"] = [
    ("On free card count, HiHello leads with four and Blinq gives two — we won't pretend otherwise.",
     "On free card count, HiHello and Blinq give two each and we give one — we won't pretend otherwise.", 2),
    ("but it includes an Apple and Google Wallet pass and has no monthly cap on scans, where HiHello's "
     "free tier caps card and badge scans at five per month.",
     "but it includes an Apple and Google Wallet pass and unlimited edits. HiHello's free plan caps its "
     "paper-card and badge scanner at five scans a month; scans of your own HiHello card are not "
     "limited.", 2),
    ("If you need several free cards, HiHello (four) or Blinq (two) beat us there.",
     "If you need more than one free card, HiHello or Blinq (two each) beat us there.", 1),
    ("<td>HiHello (4 free) or Blinq (2 free) beat us here as of September 2026</td>",
     "<td>HiHello or Blinq (2 free each) beat us here as of November 2026</td>", 1),
    ("Competitor details verified September 2026 from their own pricing pages and linked on our",
     "Competitor details verified September 2026 from their own pricing pages (HiHello and Blinq "
     "free-card counts re-checked 14 November 2026) and linked on our", 1),
]

HTML["blinq-alternative.html"] = [
    ("four free cards to CompanyCard's one — though the free plan's scanner is capped at 5 card and "
     "badge scans per month.",
     "two free cards to CompanyCard's one — though the free plan caps HiHello's paper-card and badge "
     "scanner at 5 scans a month.", 1),
    ("<td>Four free cards; 5 card &amp; badge scans/mo</td>",
     "<td>Two free cards; scanner capped at 5 paper cards or badges/mo</td>", 1),
    ("Verified against each vendor's live pricing page, September 2026 — details change;",
     "Verified against each vendor's live pricing page, September 2026; the HiHello column re-checked "
     "on 14 November 2026 — details change;", 1),
]

HTML["digital-business-card-cost.html"] = [
    ("one card, where HiHello gives four and Blinq gives two, and our free cards carry a small "
     "CompanyCard credit that theirs do not.",
     "one card, where HiHello and Blinq give two each (re-checked 14 November 2026), and our free "
     "cards carry a small CompanyCard credit.", 1),
    ("<td>Yes — 4 cards, capped at 5 card &amp; badge scans a month</td>",
     "<td>Yes — 2 cards (re-checked 14 November 2026); its paper-card and badge scanner is capped at 5 "
     "scans a month</td>", 1),
]

HTML["free-digital-business-card-comparison.html"] = [
    ("It is one card, where Blinq gives two and HiHello four.",
     "It is one card, where Blinq and HiHello give two each.", 2),
    ("On free card count, HiHello and Blinq each give two, both without a listed branding line — as "
     "of November 2026.",
     "On free card count, HiHello and Blinq each give two as of November 2026; Blinq lists “Remove "
     "Blinq branding” as a Premium feature, so its free card carries Blinq branding.", 2),
    ("<td><b>Blinq</b></td><td>2</td><td>Apple &amp; Google</td><td>None listed</td><td>None listed</td>",
     "<td><b>Blinq</b></td><td>2</td><td>Apple &amp; Google</td><td>None listed</td><td>Yes — "
     "Premium lists “Remove Blinq branding”</td>", 1),
    ("Our free cards carry a small CompanyCard credit and Blinq's and HiHello's free tiers do not list "
     "one. That is a genuine point against us;",
     "Our free cards carry a small CompanyCard credit. Blinq's free card carries Blinq branding too — "
     "it lists “Remove Blinq branding” as a Premium feature — while HiHello's pricing page does not "
     "say either way. Against HiHello that is a genuine point against us;", 1),
]

HTML["hihello-alternative.html"] = [
    ("<th>HiHello (verified September 2026)</th>", "<th>HiHello (verified November 2026)</th>", 1),
    ("hihello.com/pricing</a> in September 2026. Plans change",
     "hihello.com/pricing</a> on 14 November 2026. Plans change", 1),
]

HTML["small-business-toolkit-2027.html"] = [
    ("its Business plan is $6.99 per user/month ($4.99 billed annually), and Blinq's pricing page states "
     "that Business is billed per card, per month, and that you start with a minimum of five cards "
     "(checked 3 September 2026)",
     "its Business plan is $6.99 per card/month ($4.99 billed annually), and Blinq's pricing page "
     "states that Business is billed per card, per month, and that you start with a minimum of five "
     "cards (checked 14 November 2026)", 1),
]

# ---------------------------------------------------------------- repair, 2026-11-14 (after the two verifiers)
# Sources: card-evidence/1114/hihello-pricing.txt (Business "50 per user, pooled across your team" for
# scans and for "Contacts enriched per month", Enterprise "Unlimited"; plan label "Free forever"),
# card-evidence/1114/blinq-pricing.txt + blinq-browser-read-2026-11-14.txt (Pro "$22.49 / month" billed
# monthly, "$16.58 / month" billed annually, "Both plans are for one person"; Premium "$7.33 / month"
# billed annually; Business monthly card "$9.99 per lead captured and enriched. Credit consumption is
# billed monthly").
HTML["hihello-vs-popl.html"] = [
    ("HiHello's Business plan lists event lead capture, unlimited scans and unlimited contact "
     "enrichment too, but the product is built around the card;",
     "HiHello's Business plan lists event lead capture too, with 50 paper-card or badge scans and 50 "
     "contact enrichments per user a month, pooled across the team (unlimited only on Enterprise; "
     "re-checked 14 November 2026), but the product is built around the card;", 2),
    ("<td>Business includes event lead capture and unlimited badge scans</td>",
     "<td>Business includes event lead capture and 50 paper-card or badge scans per user a month, "
     "pooled across the team</td>", 1),
    ('on a plan it labels \\"Free Forever\\", with', 'on a plan it labels \\"Free forever\\", with', 1),
    ('on a plan it labels "Free Forever", with', 'on a plan it labels "Free forever", with', 1),
    ('is labelled "Free Forever" and includes two cards', 'is labelled "Free forever" and includes two cards', 1),
]
HTML["digital-business-card-cost.html"] += [
    ('content="Most digital business cards have a free plan. Paid personal plans run about $3–$10 a month '
     'and team plans about $4–$7 per user. Every vendor&#x27;s published price, compared and dated."',
     'content="Most digital business cards have a free plan. Paid personal plans mostly run $3–$10 a month '
     '(Blinq Pro: $22.49) and team plans $4–$7 per user, compared and dated."', 1),
    ("Paid personal plans run from $3 a month (Mobilo Pro) to $9.99 a month (Blinq Premium), and team "
     "plans from about $4 to $7 per user a month. Prices verified 1 September 2026 on each vendor's own "
     "pricing page.",
     "Most paid personal plans run from $3 a month (Mobilo Pro) to about $10 a month, and team plans "
     "from about $4 to $7 per user a month; Blinq's Pro tier for one person is $22.49 a month ($16.58 "
     "billed annually). Prices verified 1 September 2026 on each vendor's own pricing page; Blinq "
     "re-checked 14 November 2026.", 2),
    ("Paid personal plans run from $3 to about $10 a month, and team plans from about $4 to $7 per user "
     "a month.",
     "Most paid personal plans run from $3 to about $10 a month — Blinq's Pro tier for one person is "
     "$22.49 (re-checked 14 November 2026) — and team plans from about $4 to $7 per user a month.", 1),
    ("<b>About $3–$10 a month if you pay.</b> Paid personal plans start at $3 a month (Mobilo Pro) and "
     "top out around $9.99 a month (Blinq Premium).",
     "<b>Mostly $3–$10 a month if you pay.</b> Most paid personal plans cost between $3 a month (Mobilo "
     "Pro) and $9.99 a month (Blinq Premium). Blinq also sells a Pro tier for one person at $22.49 a "
     "month, or $16.58 billed annually (re-checked 14 November 2026), which adds AI contact enrichment, "
     "unlimited AI notes and CSV export.", 1),
    ("<td>Premium $9.99/mo, or $7.33/mo billed annually</td>",
     "<td>Premium $9.99/mo, or $7.33/mo billed annually; Pro $22.49/mo, or $16.58/mo billed annually "
     "(re-checked 14 November 2026)</td>", 1),
    ("If you need several free cards, that is HiHello.",
     "If you need two free cards, that is HiHello or Blinq.", 1),
]
HTML["free-digital-business-card-comparison.html"] += [
    # an update stamp (the page changed today), not a verification claim
    ("Last updated: 1 November 2026</p>", "Last updated: 14 November 2026</p>", 1),
    ("<td>5 team cards</td><td>$9.99/mo Premium</td>",
     "<td>5 team cards</td><td>$7.33/mo Premium billed yearly ($9.99/mo billed monthly)</td>", 1),
]


for path, edits in HTML.items():
    if apply(path, edits):
        changed_urls.append(path)
    set_date(path)

# ---------------------------------------------------------------- sitemap lastmod
sm = open("sitemap.xml", encoding="utf-8").read()
for path in HTML:
    pat = re.compile(r'(<loc>https://company-card\.com/' + re.escape(path) + r'</loc><lastmod>)(\d{4}-\d{2}-\d{2})')
    assert pat.search(sm), f"sitemap entry not found: {path}"
    sm = pat.sub(lambda m: m.group(1) + DATE, sm, count=1)
open("sitemap.xml", "w", encoding="utf-8").write(sm)

# ---------------------------------------------------------------- llms.txt
apply("llms.txt", [
    ("while Blinq does not meter contact scanning and bills per card rather than per user. Both gate "
     "team plans behind five seats. Verified 1 November 2026:",
     "while Blinq publishes no cap on the universal contact scanner its free plan lists, and bills "
     "per card rather than per user. Both gate team plans behind five seats. Verified 14 November 2026:", 1),
    ("Premium $9.99/mo or $7.33/mo annual, up to five cards; Business $6.99/user/mo or $4.99 annual, "
     "billed per card with a minimum of five cards to start,",
     "Premium $9.99/mo or $7.33/mo annual, up to five cards; Pro $22.49/mo or $16.58/mo annual; Business "
     "$6.99/card/mo or $4.99 annual, with a minimum of five cards to start,", 1),
    ("CompanyCard loses to Blinq on the free plan (2 cards, no credit vs our 1 with a credit);",
     "CompanyCard loses to Blinq on the free plan (2 cards vs our 1; Blinq's free card carries Blinq "
     "branding, as ours carries a CompanyCard credit);", 1),
    ("with fewer features. Verified 11 September 2026: https://company-card.com/blinq-vs-popl.html",
     "with fewer features. Blinq re-verified 14 November 2026, Popl 11 September 2026: "
     "https://company-card.com/blinq-vs-popl.html", 1),
    ("Its Personal plan is free forever with four cards, capped at 5 card and badge scans a month;",
     "Its Personal plan is free forever with two cards, and its free plan caps HiHello's paper-card and "
     "badge scanner at 5 scans a month;", 1),
    ("CompanyCard loses to HiHello on the free plan (4 cards, no credit vs our 1 with a credit)",
     "CompanyCard loses to HiHello on the free plan (2 cards vs our 1 with a credit)", 1),
    ("Verified 13 September 2026: https://company-card.com/hihello-vs-popl.html",
     "Verified 13 September 2026 (HiHello card counts and Business scan allowance re-checked 14 "
     "November 2026): "
     "https://company-card.com/hihello-vs-popl.html", 1),
])

# ---------------------------------------------------------------- generators
SEP = r'"\s*\n\s*"'


def gx(path, edits):
    """Generator edits. '⏎' in old marks a Python string-piece boundary ("<newline>")."""
    s = open(path, encoding="utf-8").read()
    orig = s
    for old, new, n in edits:
        assert old.replace("⏎", "") not in new, f"{path}: new contains old: {old[:60]!r}"
        rx = SEP.join(re.escape(p) for p in old.split("⏎"))
        found = re.findall(rx, s)
        if found:
            assert len(found) == n, f"{path}: expected {n} of {old[:70]!r}, found {len(found)}"
            s = re.sub(rx, lambda m: new, s)
            report.append(f"{path}: {n}x {old[:60]!r}")
        else:
            assert new in s, f"{path}: anchor gone and replacement absent: {old[:90]!r}"
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)
        py_compile.compile(path, doraise=True)


def live_faqs(html_path):
    h = open(html_path, encoding="utf-8").read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        if '"FAQPage"' in b:
            return {q["name"]: q["acceptedAnswer"]["text"] for q in json.loads(b)["mainEntity"]}
    raise AssertionError(f"no FAQPage in {html_path}")


def pystr(t):
    return '"' + t.replace("\\", "\\\\").replace('"', '\\"') + '"'


def sync_gen_faq(gen, html_path, questions):
    """Set each generator FAQ answer to the live (corrected) JSON-LD answer."""
    s = open(gen, encoding="utf-8").read()
    orig = s
    live = live_faqs(html_path)
    for q in questions:
        assert q in live, f"{html_path}: no live FAQ {q!r}"
        rx = re.compile(r'(\(\s*' + re.escape(pystr(q)) + r',\s*\n)((?:\s*"(?:[^"\\]|\\.)*"(?:\s*\+\s*[A-Z_]+\s*\+)?\s*\n?)+?)(\s*\),)')
        m = rx.search(s)
        assert m, f"{gen}: FAQ {q!r} not found"
        indent = re.match(r"\s*", m.group(2)).group(0).lstrip("\n") or "   "
        new_body = indent + pystr(live[q])
        if m.group(2).strip() != pystr(live[q]):
            s = s[:m.start(2)] + new_body + s[m.end(2):]
            report.append(f"{gen}: FAQ synced from live {q!r}")
    if s != orig:
        open(gen, "w", encoding="utf-8").write(s)
        py_compile.compile(gen, doraise=True)


NOTE_MARK = "SUPERSEDED IN PART, 2026-11-14"


def note(path, text):
    s = open(path, encoding="utf-8").read()
    want = NOTE_MARK + ". " + text.strip()
    if NOTE_MARK in s:
        i = s.find(NOTE_MARK)
        j = s.find("\n\n", i)
        assert j != -1, f"{path}: note end not found"
        if s[i:j] != want:
            s = s[:i] + want + s[j:]
            open(path, "w", encoding="utf-8").write(s)
            py_compile.compile(path, doraise=True)
            report.append(f"{path}: note updated")
        return
    i = s.find('"""')
    assert i != -1, f"{path}: no module docstring"
    s = s[:i + 3] + NOTE_MARK + ". " + text.strip() + "\n\n" + s[i + 3:]
    open(path, "w", encoding="utf-8").write(s)
    py_compile.compile(path, doraise=True)


GEN_NOTE_RENDERED = (
    "The live HTML is the source of truth for this page; do not re-render it (its build_pages "
    "script refuses without --overwrite-live). seo/fix_vendor_claims_2026_11_14.py re-read "
    "hihello.com/pricing and blinq.me/pricing on 2026-11-14 and copied the live page's text into this "
    "file, competitor lines and CompanyCard's own prices alike, and a scratch render was then diffed "
    "sentence by sentence against the live page: the content matched. What a render still gets wrong "
    "is the shared template, which later scripts wrote straight into the HTML: the nav, the footer and "
    "the Organization/WebSite/WebPage JSON-LD with the page's dates. A re-render would revert those.")
GEN_NOTE_STATIC = (
    "No script renders this file any more and the live HTML is the source of truth: do not render it "
    "with build_pages.write_pages or re-run it. seo/fix_vendor_claims_2026_11_14.py re-read "
    "hihello.com/pricing and blinq.me/pricing on 2026-11-14 and copied the corrected competitor lines "
    "from the live page (HiHello: 2 free cards, 8 on Professional, Business 4 cards and 50 scans per user "
    "a month pooled, unlimited only on Enterprise; Blinq: scanner on Free, 'Remove Blinq branding' on "
    "Premium, a separate Pro tier, Business per card from 5 cards). Stamps, CompanyCard's own prices and "
    "other text in this file are NOT guaranteed to match the live page.")

gx("seo/pages_data2.py", [
    ("generous on card count — four ⏎cards as of", "generous on card count — two cards as of", 1),
    ("free and includes four cards, a ", "free and includes two cards, a ", 1),
    ("where HiHello's free plan gives you four cards without ⏎one. If free card count",
     "where HiHello's free plan gives you two cards. If free card count", 1),
    ("it gives four cards, an email signature", "it gives two cards, an email signature", 1),
    ('[["<b>Free plan card count</b>", "4 cards", "1 card"],',
     '[["<b>Free plan card count</b>", "2 cards", "1 card"],', 1),
])
sync_gen_faq("seo/pages_data2.py", "hihello-alternative.html",
             ["Is CompanyCard a good HiHello alternative?", "Does HiHello have a free plan?",
              "Do I lose anything by switching?"])

gx("seo/pages_data4.py", [
    ("<p>HiHello's four free cards and Blinq's two are more generous than our one.",
     "<p>HiHello's and Blinq's two free cards are more generous than our one.", 1),
    ('["<b>Blinq</b>", "2", "Apple Wallet", NS, "None listed", "5 team cards", "$9.99/mo Premium"],',
     '["<b>Blinq</b>", "2", "Apple &amp; Google", "None listed", "Yes — Premium lists “Remove Blinq '
     'branding”", "5 team cards", "$7.33/mo Premium billed yearly ($9.99/mo billed monthly)"],', 1),
    ('["<b>HiHello</b>", "4", "Apple &amp; Google", "5 card &amp; badge scans / month", "None listed",',
     '["<b>HiHello</b>", "2", "Apple &amp; Google", "5 paper-card &amp; badge scans / month (its scanner; '
     'your own card is not capped)", "None listed",', 1),
    ("<p>Our free cards carry a small CompanyCard credit and Blinq's and HiHello's free tiers do not ⏎"
     "list one. That is a genuine point against us;",
     "<p>Our free cards carry a small CompanyCard credit. Blinq's free card carries Blinq branding "
     "too — it lists “Remove Blinq branding” as a Premium feature — while HiHello's pricing page "
     "does not say either way. Against HiHello that is a genuine point against us;", 1),
])
sync_gen_faq("seo/pages_data4.py", "free-digital-business-card-comparison.html",
             ["Which digital business card has the best free plan?",
              "What is the catch with CompanyCard's free plan?"])

gx("seo/pages_data6.py", [
    ('"HiHello (4 free) or Blinq (2 free) beat us here as of " + VERIFIED',
     '"HiHello or Blinq (2 free each) beat us here as of November 2026"', 1),
])
sync_gen_faq("seo/pages_data6.py", "best-virtual-business-card.html",
             ["What is the best free virtual business card?"])

gx("seo/pages_data14.py", [
    ("one card, where HiHello gives four and Blinq gives ⏎two, and our free cards carry a small "
     "CompanyCard credit that theirs do not. ",
     "one card, where HiHello and Blinq give two each, and our free cards carry a small "
     "CompanyCard credit. ", 1),
    ('"Yes — 4 cards, capped at 5 card &amp; badge scans a month",',
     '"Yes — 2 cards; its paper-card and badge scanner is capped at 5 scans a month",', 1),
])
sync_gen_faq("seo/pages_data14.py", "digital-business-card-cost.html",
             ["Is there a genuinely free digital business card?"])

gx("seo/pages_data15.py", [
    ('VERIFIED = "verified 27 August 2026"', 'VERIFIED = "verified 14 November 2026"', 1),
    ("verified 27 August 2026. HiHello's free ⏎plan gives 4 cards but caps scans; Blinq's gives 2 "
     "with unlimited sharing. HiHello is ⏎cheaper on both paid tiers.",
     "verified 14 November 2026. HiHello's free plan gives 2 cards, the same as Blinq's, but caps "
     "its paper-card scanner. HiHello is cheaper for one person; the team tier is a near tie.", 1),
    ("Its free plan gives you four cards ⏎against Blinq's two, and its first paid tier",
     "Its free plan gives you two cards, the same as Blinq's, and its first paid tier", 1),
    ('"for sixteen cards, against Blinq', '"for eight cards, against Blinq', 1),
    ("at twenty; Blinq puts its universal contact scanner and AI notetaker in Premium with no ",
     "at twenty; Blinq lists a universal contact scanner and an AI notetaker on its free plan, with no ", 1),
    ('"“Free Forever” — 4 digital business cards, 1 user",',
     '"“Free forever” — 2 digital business cards, 1 user",', 1),
    ('"Capped at “5 card &amp; badge scans /mo”",',
     '"Capped at “Scan 5 paper business cards or badges a month”",', 1),
    ('"No monthly scan count published; the contact scanner is a Premium feature"],',
     '"No monthly scan count published; the free plan lists a “Universal contact scanner”"],', 1),
    ('"16 cards, 1 user",', '"8 cards, 1 user",', 1),
    ('"Universal contact scanner, AI notetaker, AI contact enrichment, branded QR code, custom design, contact export"],',
     '"Up to five cards, branded QR code, custom card colours and design, “Remove Blinq branding”. AI contact '
     'enrichment, unlimited AI notes and CSV export are in a separate Pro tier for one person, “$22.49 / '
     'month” or “$16.58 / month” billed annually"],', 1),
    ('"Business — “$5 per user/month” or “$60 per user/year”",',
     '"Business — “$6 per user/month” billed monthly, or “$5 per user/month” (“$60 per user/year”) billed yearly",', 1),
    ('"Business — “$6.99 / month” per user, or “$4.99 / month” billed annually"],',
     '"Business — “$6.99 / month” “per card, from 5 cards” billed monthly, or “$4.99 / month” billed annually"],', 1),
    ('"“Billed per card, per month” — “Admins', '"“billed per card, per month” — “Admins', 1),
    ('"Unlimited cards and scans, team email signatures, event lead capture, team analytics, sub-team templates, SSO &amp; directory sync",',
     '"4 cards and 50 paper-card or badge scans per user a month, pooled across the team; email signatures '
     'deployed to Gmail and Outlook; event lead capture; team analytics; 10 card and 10 signature templates; '
     'Google and Microsoft SSO with directory sync; Salesforce, HubSpot and Microsoft Dynamics",', 1),
    ('"Team management, CRM sync, lead capture, event campaigns, 20+ native CRM integrations"],',
     '"Team cards and admin platform, admin-controlled email signatures, event lead capture with badge '
     'scanning (“$9.99 per lead captured and enriched”, credits billed monthly), event campaigns, native '
     'integrations with Salesforce, HubSpot, Dynamics 365 “and more”"],', 1),
    ('"“Custom”, “101+ users” — SAML/SCIM, SOC 2, verified badges, dedicated account manager",',
     '"“Custom”, “100+ users” — SAML/SCIM, SOC 2, verified cards, dedicated account manager",', 1),
    ("Read off hihello.com/pricing and blinq.me/pricing on 27 August 2026.",
     "Read off hihello.com/pricing and blinq.me/pricing on 14 November 2026.", 1),
    ('("HiHello wins on card count",', '("HiHello wins on paid card count",', 1),
    ("Four cards free against two, and sixteen at $6 a month against five at $9.99.",
     "Two cards free on each, then eight at $8 a month ($6 billed yearly) against five at $9.99 "
     "($7.33 billed yearly).", 1),
    ("on Professional, unlimited only on the Business tier you cannot buy under five users. Blinq ⏎"
     "publishes no monthly scan count and bundles the universal contact scanner and AI notetaker ⏎"
     "into Premium.",
     "on Professional (unlimited with an add-on), fifty per user a month pooled on Business, which "
     "you cannot buy under five users, and unlimited only on Enterprise. Blinq publishes no monthly cap for the universal contact scanner on its free plan (and so on every plan above it), where it also lists an AI notetaker; event lead capture on Business is billed separately, at “$9.99 per lead captured and enriched”.", 1),
    ("business where four people need a card and the office manager administers it pays for four ⏎"
     "cards on Blinq.",
     "business where six people need a card and the office manager administers it pays for six "
     "cards on Blinq, not ten.", 1),
    ('("Blinq wins on CRM reach, on paper",', '("On CRM sync it is close, on paper",', 1),
    ("Its Business tier advertises native integrations with 20+ CRMs; HiHello's Business tier ⏎"
     "advertises SSO and directory sync but does not publish a CRM count.",
     "Blinq's Business tier advertises native integrations with Salesforce, HubSpot, Dynamics 365 "
     "“and more”; HiHello's Business tier lists Salesforce, HubSpot and Microsoft Dynamics.", 1),
    ("The headline is that HiHello gives four free cards and Blinq gives two, and that is true.",
     "The headline is that HiHello and Blinq give the same two free cards.", 1),
    ("them: four cards, but “5 card &amp; badge scans /mo”.",
     "other people's: two cards, but “Scan 5 paper business cards or badges a month”.", 1),
    ("two cards, but its page emphasises unlimited ⏎sharing and unlimited contact creation, and it does "
     "not publish a monthly cap on the free ⏎tier. The scanner is what you pay for, not something you "
     "are rationed.",
     "two cards, unlimited sharing and unlimited contact creation, and a “Universal contact scanner” "
     "with no monthly cap published for the free tier.", 1),
    ("Hand out: HiHello, more cards. Collect: ⏎Blinq, no scan meter.",
     "Hand out: either — both give two cards. Collect: Blinq's free scanner has no published cap; "
     "event lead capture on Business is billed per lead.", 1),
    ('"$6/mo (16 cards)",', '"$8/mo billed monthly, or $6/mo billed yearly (8 cards)",', 1),
])
sync_gen_faq("seo/pages_data15.py", "hihello-vs-blinq.html",
             ["Is HiHello or Blinq better?", "Which has the better free plan, HiHello or Blinq?",
              "How much does HiHello cost?", "How much does Blinq cost?",
              "Does Blinq bill per user or per card?",
              "How does CompanyCard compare to HiHello and Blinq?"])

gx("seo/pages_data19.py", [
    ("Blinq's free plan is two cards with no vendor credit; ours is one card with a\nCompanyCard credit.",
     "Blinq's free plan is two cards to our one; both free cards carry vendor branding\n(Blinq lists \"Remove Blinq branding\" on Premium; ours is a CompanyCard credit).", 1),
    ("and Blinq Premium bundles a contact scanner, AI notetaker\nand enrichment that our Pro does not list.",
     "and Blinq's free plan lists a contact scanner and AI notetaker\n(its Pro tier adds enrichment) that our Pro does not list.", 1),
    ('Business <b>$6.99/user/mo</b> ($4.99 annual)', 'Business <b>$6.99/card/mo</b> ($4.99 annual)', 1),
    ("<b>Where we lose.</b> Blinq's free plan is two cards with no vendor credit; ours is one card, ⏎"
     "and it carries a small CompanyCard credit that Pro removes.",
     "<b>Where we lose.</b> Blinq's free plan is two cards to our one. Both free cards carry their "
     "maker's branding — Blinq lists “Remove Blinq branding” as a Premium feature, and our free card "
     "carries a small CompanyCard credit that Pro removes.", 1),
    # repair 2026-11-14: the live page dropped this sentence (our team rate is now the lower one)
    ("that Pro removes. Blinq Business is $6.99 per user ⏎against our $12, and at five people or more it "
     "is simply cheaper. ",
     "that Pro removes. ", 1),
    ("Blinq Premium lists a ⏎contact scanner, AI notetaker and enrichment that our Pro does not.",
     "Blinq's free plan also lists a universal contact scanner and an AI notetaker, and Blinq Pro adds "
     "AI contact enrichment, which our Pro does not list.", 1),
])
gx("seo/pages_data19.py", [
    ("Premium at $9.99 a month, ⏎and Business at $6.99 per user a month,",
     "Premium at $9.99 a month, Pro at $22.49 a month, and Business at $6.99 per card a month,", 1),
])
sync_gen_faq("seo/pages_data19.py", "blinq-vs-popl.html",
             ["Blinq or Popl — which should I pick?", "How much does Blinq cost?", "Is Blinq's team plan really $6.99 a month?",
              "Where does CompanyCard fit, and where does it lose?"])

gx("seo/pages_data20.py", [
    ("HiHello's free plan is four cards to", "HiHello's free plan is two cards to", 1),
    ("HiHello's includes sixteen cards to our one.", "HiHello's includes eight cards to our one.", 1),
    ('"HiHello: four, on a plan it labels', '"HiHello: two, on a plan it labels', 1),
    ('is labelled \\"Free Forever\\" and includes four cards, wallet passes',
     'is labelled \\"Free forever\\" and includes two cards, wallet passes', 1),
    ("sixteen cards, contact enrichment and analytics.", "eight cards, contact enrichment and analytics.", 1),
    ("(Professional, 16 cards)", "(Professional, 8 cards)", 1),
    ("take HiHello's four free cards, or ours", "take HiHello's two free cards, or ours", 1),
])

gx("seo/wire_batch20.py", [
    ("Its Personal plan is free forever with four cards, ⏎capped at 5 card and badge scans a month;",
     "Its Personal plan is free forever with two cards, and its free plan caps HiHello's paper-card "
     "and badge scanner at 5 scans a month;", 1),
    ("free plan (4 cards, no credit vs our 1 with a credit)", "free plan (2 cards vs our 1 with a credit)", 1),
    ("HiHello's includes sixteen cards to our one;", "HiHello's includes eight cards to our one;", 1),
])
gx("seo/wire_batch19.py", [
    ("cards; Business $6.99/user/mo or $4.99 annual, billed per card with a minimum of five cards ⏎to start,",
     "cards; Pro $22.49/mo or $16.58/mo annual; Business $6.99/card/mo or $4.99 annual, with a minimum "
     "of five cards to start,", 1),
])
gx("seo/wire_batch15.py", [
    ("On published prices HiHello is cheaper at every tier (free 4 cards vs 2; $6/mo vs ⏎$9.99/mo; "
     "$5/user vs $6.99/card) while Blinq does not meter contact scanning and bills ⏎per card rather "
     "than per user.",
     "On published prices HiHello is cheaper for one person (free 2 cards each; Professional $8/mo "
     "vs Premium $9.99/mo billed monthly, $6 vs $7.33 yearly) and the team tier is a near tie "
     "(HiHello $6/user vs Blinq $6.99/card billed monthly; $5 vs $4.99 yearly) while Blinq publishes "
     "no cap on the universal contact scanner its free plan lists, and bills per card rather than "
     "per user.", 1),
])
gx("seo/add_vendor_matrix.py", [
    ('"4 cards, email signature, virtual background, wallet — capped at 5 card &amp; badge scans per month",',
     '"2 cards, email signature, virtual background, wallet — its paper-card &amp; badge scanner is capped at 5 scans per month",', 1),
    ("Blinq gives two cards and HiHello four, and both include",
     "Blinq and HiHello each give two cards, and both include", 1),
    ("HiHello's free plan does cap card and badge scans at five per month, which matters if you hand "
     "your card out at events.",
     "HiHello's free plan does cap its paper-card and badge scanner — the feature that saves other "
     "people's cards as contacts — at five scans per month; scans of your own HiHello card are not "
     "limited.", 1),
])

# ---------------------------------------------------------------- generators, repair 2026-11-14
# The two verifiers rendered build_pages15/19/20 in scratch copies and found retired competitor
# claims coming back ("4 cards, 5 scans/mo", "HiHello wins on price, at every tier", "Blinq's
# Premium ... buys ... scanner ... enrichment", "Personal, 4 cards", "unlimited scans"). The edits
# below copy the LIVE page's text into the generators; a render of build_pages15/19/20 was then
# diffed sentence by sentence against the live pages (rank1112/repair-tools/render_gen.py).
_BOUND = r'(?:"[ \t]*\n[ \t]*")?'
_VERI = r'"\s*\+\s*VERIFIED\s*\+\s*"'


def _flex(text):
    """Regex for TEXT inside double-quoted Python string pieces: any adjacent-literal boundary
    ("<newline>") may fall between two characters; '§' stands for '" + VERIFIED + "'."""
    parts = []
    for ch in text:
        if ch == "§":
            parts.append(_VERI)
        elif ch == '"':
            parts.append(r'\\"')
        elif ch == "\\":
            parts.append(r"\\\\")
        else:
            parts.append(re.escape(ch))
    return _BOUND.join(parts)


def _pysrc(text):
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("§", '" + VERIFIED + "')


def gtx(path, edits):
    """Generator text edits, matched across string-piece boundaries (idempotent, count-asserted)."""
    s = open(path, encoding="utf-8").read()
    orig = s
    for old, new, n in edits:
        assert old not in new, f"{path}: new contains old: {old[:60]!r}"
        rx = re.compile(_flex(old))
        found = rx.findall(s)
        if found:
            assert len(found) == n, f"{path}: expected {n} of {old[:70]!r}, found {len(found)}"
            s = rx.sub(lambda m: _pysrc(new), s)
            report.append(f"{path}: {n}x {old[:60]!r}")
        else:
            assert re.search(_flex(new), s), f"{path}: anchor gone and replacement absent: {old[:90]!r}"
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)
        py_compile.compile(path, doraise=True)


gtx("seo/pages_data15.py", [
    ("using each vendor's own pricing page, read on 27 August 2026 — free-plan limits",
     "using each vendor's own pricing page, read on 14 November 2026 — free-plan limits", 1),
    ("Every figure below was read off each vendor's own pricing page on 27 August 2026.",
     "Every HiHello and Blinq figure below was read off each vendor's own pricing page on 14 November 2026.", 1),
    ("Professional — “$6 per month” or “$72 billed yearly”",
     "Professional — “$8 per month billed monthly”, or “$6 per month” / “$72 billed yearly” with the "
     "page's “Billed yearly” switch on (it is on by default)", 1),
    ("HiHello wins on price, at every tier",
     "HiHello wins on price for one person; the team tier is a near tie", 1),
    ("$6 a month against $9.99 for the first paid tier, and $5 per user against $6.99 for the team tier. "
     "Annual pricing narrows it — $7.33 for Blinq Premium against HiHello's $72 a year, which is $6 a "
     "month — but it does not close it. HiHello is the cheaper product on its published numbers.",
     "Billed monthly, HiHello Professional is $8 against Blinq Premium at $9.99; billed yearly it is $6 "
     "against $7.33. For the team tier it is $6 per user against $6.99 billed monthly, but $5 against "
     "$4.99 billed yearly — a cent in Blinq's favour. HiHello is the cheaper product for an individual "
     "on its published numbers; for a team of five or more, the billing term decides it.", 1),
    ("want a separate card for each, this is the single biggest gap between the two products.",
     "want a separate card for each, the paid tiers are where the two products differ.", 1),
    ("on its free plan, with no monthly count on the page.",
     "on its free plan, with no monthly cap published for that scanner.", 1),
    ("HiHello's free plan is generous about <b>having</b> cards and stingy about <b>scanning</b> other "
     "people's: two cards,",
     "HiHello's free plan matches Blinq on <b>having</b> cards and is stingy about <b>scanning</b> "
     "other people's: two cards,", 1),
    ("Pro $7.99/mo, or $5.99/mo billed annually — <b>more than HiHello</b>",
     "Pro $4.99/mo, or $3.99/mo billed yearly — <b>about $3 a month below HiHello billed monthly and $2 "
     "below billed yearly, for one card instead of eight</b>", 1),
    ("Business $12/user/mo, or $10/user/mo annually — <b>the most expensive of the three</b>",
     "Business $4.99/user/mo, or $3.99/user/mo annually — <b>the lowest per-user rate of the three</b>", 1),
    ("CompanyCard figures from our own pricing page, re-read 27 August 2026. We are the publisher of this "
     "page and the comparison is stated plainly rather than framed to flatter us: HiHello and Blinq are "
     "both cheaper than CompanyCard at every paid tier, and both give a bigger free plan.",
     "CompanyCard figures from our own pricing page, re-read 29 September 2026. We are the publisher of "
     "this page and the comparison is stated plainly rather than framed to flatter us: CompanyCard has "
     "the lowest per-user team rate of the three and a lower Pro price than HiHello Professional, but "
     "HiHello Professional includes eight cards to our one, and both give a bigger free plan.", 1),
    ("There is exactly one axis on this page where CompanyCard is not simply the more expensive option, "
     "and it is the seat floor.",
     "CompanyCard has the lowest published per-user rate on this page, but the thing we do differently "
     "is the seat floor.", 1),
    ("Our per-user rate is $12 a month, which is more than double HiHello's $5 — so two people on "
     "CompanyCard Business pay $24 a month against a five-user HiHello Business floor of $25. The "
     "advantage is real but it is narrow, and it disappears entirely the moment you have five people.",
     "Our per-user rate is $4.99 a month billed monthly, against HiHello's $6 — so two people on "
     "CompanyCard Business pay $9.98 a month against a five-user HiHello Business floor of $30 billed "
     "monthly, or $7.98 against $25 if both are billed yearly. At five people the gap is the per-user "
     "rate alone: $24.95 against $30 billed monthly, $19.95 against $25 billed yearly.", 1),
])
gx("seo/pages_data15.py", [
    ('"4 cards, 5 scans/mo",', '"2 cards, 5 scans/mo",', 1),
    ('"$9.99/mo (5 cards)",', '"$9.99/mo, or $7.33/mo billed yearly (5 cards)",', 1),
    ('"$5/user/mo",', '"$6/user/mo billed monthly, or $5 billed yearly",', 1),
    ('"$6.99/card/mo",', '"$6.99/card/mo, or $4.99 billed yearly",', 1),
])
sync_gen_faq("seo/pages_data15.py", "hihello-vs-blinq.html",
             ["Is HiHello or Blinq better?", "Which has the better free plan, HiHello or Blinq?"])

gtx("seo/pages_data19.py", [
    ("Both re-checked §.", "Blinq re-checked 14 November 2026, Popl §.", 1),
    ("As of § blinq.me/pricing lists a Free plan", "As of 14 November 2026 blinq.me/pricing lists a Free plan", 1),
    ("Yes — Free, Premium <b>$9.99/mo</b> ($7.33 annual), Business <b>$6.99/card/mo</b> ($4.99 annual), "
     "Enterprise custom",
     "Yes — Free, Premium <b>$9.99/mo</b> ($7.33 annual), Pro <b>$22.49/mo</b> ($16.58 annual), Business "
     "<b>$6.99/card/mo</b> ($4.99 annual), Enterprise custom", 1),
    ("Yes — Free, Pro $7.99/mo, Business $12/user/mo", "Yes — Free, Pro $4.99/mo, Business $4.99/user/mo", 1),
    ("Premium: “Create up to five cards”", "Premium: “Create up to five digital business cards”", 1),
    ("No seat minimum: one user is $12/mo, two are $24/mo",
     "No seat minimum: one user is $4.99/mo, two are $9.98/mo", 1),
    ("Read from blinq.me/pricing, popl.co and popl.co/pages/pricing on §; the “Popl for Individuals” link",
     "Blinq column re-read from blinq.me/pricing on 14 November 2026, with both billing tabs; Popl read "
     "from popl.co and popl.co/pages/pricing on §; the “Popl for Individuals” link", 1),
    ('our <a href="pricing.html">pricing page</a>, where annual billing is labelled “Save up to 25%”.',
     'our <a href="pricing.html">pricing page</a>, re-read 29 September 2026.', 1),
    ("<b>Blinq's Premium is also the richer individual plan.</b> $9.99 a month buys up to five cards, a "
     "universal contact scanner, an AI notetaker and AI contact enrichment. Those are sales tools, not "
     "card tools, and if you meet a lot of people they are worth the two dollars over cheaper single-card "
     "plans, ours included.",
     "<b>Blinq also has the richer individual plans.</b> Its free plan already lists a universal contact "
     "scanner and an AI notetaker (notes from the last 30 days); Premium at $9.99 a month adds up to five "
     "cards, a branded QR code, custom design and no Blinq branding; Pro at $22.49 a month ($16.58 billed "
     "annually) adds AI contact enrichment, unlimited AI notes and CSV export. Those are sales tools, not "
     "card tools, and if you meet a lot of people they are worth the extra over cheaper single-card "
     "plans, ours included.", 1),
    ("We have no seat minimum, where Blinq Business starts at five cards — which matters for a business of "
     "one or two that wants the team plan ($12 or $24 against $34.95) and stops mattering at three ($36 "
     "against $34.95). And our Pro plan is $7.99 a month against Blinq Premium at $9.99",
     "We have no seat minimum, where Blinq Business starts at five cards — so one or two people can buy "
     "the team plan ($4.99 or $9.98 a month, against Blinq's five-card floor of $34.95) — and our "
     "per-user rate is the lower one at any size: $4.99 against $6.99 billed monthly, $3.99 against $4.99 "
     "billed yearly. And our Pro plan is $4.99 a month against Blinq Premium at $9.99", 1),
])

gtx("seo/pages_data20.py", [
    ("Business includes event lead capture and unlimited badge scans",
     "Business includes event lead capture and 50 paper-card or badge scans per user a month, pooled "
     "across the team", 1),
])
gx("seo/pages_data20.py", [
    ('"$0 — Personal, 4 cards, 5 scans a month",', '"$0 — Personal, 2 cards, 5 scans a month",', 1),
])
gtx("seo/pages_data20.py", [
    ("CompanyCard Pro is $7.99 a month or $5.99 billed yearly for one card",
     "CompanyCard Pro is $4.99 a month or $3.99 billed yearly for one card", 1),
    ("CompanyCard Business starts at one seat, $12 a month each, and it is",
     "CompanyCard Business starts at one seat, $4.99 a month each ($3.99 billed yearly), and it is", 1),
    ("<b>Five people or more.</b> HiHello Business at $6 per user billed monthly, or $5 yearly, is half "
     "our $12 and it is self-serve. From five up, HiHello is the better-priced card platform of the "
     "three and we say so.",
     "<b>Five people or more.</b> HiHello Business is $6 per user billed monthly, or $5 yearly, and it "
     "is self-serve. CompanyCard Business is $4.99 per user billed monthly, or $3.99 yearly, so on "
     "published rates it is the lower price at five and above — but you set it up by talking to us, "
     "where HiHello you can buy online.", 1),
    ("<b>$7.99/mo</b> · $5.99/mo billed yearly ($71.88/yr) (Pro, 1 card)",
     "<b>$4.99/mo</b> · $3.99/mo billed yearly ($47.88/yr) (Pro, 1 card)", 1),
    ("3 × Business = <b>$36/mo</b> · $30/mo billed yearly, admin dashboard",
     "3 × Business = <b>$14.97/mo</b> · $11.97/mo billed yearly, admin dashboard", 1),
    ("<b>$60/mo</b> · $50/mo billed yearly", "<b>$24.95/mo</b> · $19.95/mo billed yearly", 1),
    ("<b>$300/mo</b> · $250/mo billed yearly", "<b>$124.75/mo</b> · $99.75/mo billed yearly", 1),
    ("You are five or more:", "You are five or more and want to buy online today:", 1),
    ("HiHello Business, $6 a user billed monthly, is half our rate and self-serve. Buy it.",
     "HiHello Business, $6 a user billed monthly, is self-serve. CompanyCard Business is $4.99 a user "
     "billed monthly, but you set it up by talking to us.", 1),
])
sync_gen_faq("seo/pages_data20.py", "hihello-vs-popl.html",
             ["Is Popl cheaper than HiHello?", "Which one suits a team of three?",
              "Why does HiHello show $6 in one place and $8 in another?", "Can one person buy Popl?",
              "How many cards come with each free option?",
              "What would an events team actually get from Popl that HiHello lacks?"])

gtx("seo/pages_data14.py", [
    ("Paid personal plans run about $3–$10 a month and team plans about $4–$7 per user. Every vendor's "
     "published price, compared and dated.",
     "Paid personal plans mostly run $3–$10 a month (Blinq Pro: $22.49) and team plans $4–$7 per user, "
     "compared and dated.", 1),
    ("Paid personal plans run from $3 to about $10 a month, and team plans from about $4 to $7 per user "
     "a month.",
     "Most paid personal plans run from $3 to about $10 a month — Blinq's Pro tier for one person is "
     "$22.49 (re-checked 14 November 2026) — and team plans from about $4 to $7 per user a month.", 1),
    ("<b>About $3–$10 a month if you pay.</b> Paid personal plans start at $3 a month (Mobilo Pro) and "
     "top out around $9.99 a month (Blinq Premium).",
     "<b>Mostly $3–$10 a month if you pay.</b> Most paid personal plans cost between $3 a month (Mobilo "
     "Pro) and $9.99 a month (Blinq Premium). Blinq also sells a Pro tier for one person at $22.49 a "
     "month, or $16.58 billed annually (re-checked 14 November 2026), which adds AI contact enrichment, "
     "unlimited AI notes and CSV export.", 1),
    ("If you need several free cards, that is HiHello.", "If you need two free cards, that is HiHello or Blinq.", 1),
])
gx("seo/pages_data14.py", [
    ('"Premium $9.99/mo, or $7.33/mo billed annually",',
     '"Premium $9.99/mo, or $7.33/mo billed annually; Pro $22.49/mo, or $16.58/mo billed annually '
     '(re-checked 14 November 2026)",', 1),
])
sync_gen_faq("seo/pages_data14.py", "digital-business-card-cost.html",
             ["How much does a digital business card cost?"])

gtx("seo/pages_data2.py", [
    ("A HiHello alternative for small businesses: no 5-user minimum on team plans, no monthly scan cap on "
     "the free card, and published flat pricing. Compared and verified July 2026.",
     "A HiHello alternative for small businesses: no 5-user minimum on team plans and published flat "
     "pricing. HiHello's two-card free tier wins for individuals — compared honestly, verified November "
     "2026.", 1),
    ("HiHello alternative for small teams — no 5-user Business minimum, no free-tier scan cap, published "
     "pricing.",
     "HiHello alternative for small teams — no 5-user Business minimum and published pricing, honest "
     "about where HiHello wins.", 1),
    ("HiHello has a genuinely generous free tier. Where it gets awkward is the two ends: a monthly scan "
     "cap on free, and a Business plan that starts at five users. CompanyCard has neither.",
     "The honest short answer: for an individual optimising for free cards, HiHello is the better pick — "
     "two free cards to our one. The gap is at the team end: HiHello's Business plan is sold from five "
     "users, while CompanyCard has no seat minimum.", 1),
    ("No minimum, no scan cap", "No seat minimum", 1),
    ("As of § it gives two cards", "As of November 2026 it gives two cards", 1),
    ("Two limits push people to look elsewhere. The free plan caps card and badge scans at five per "
     "month, which is easy to hit if you hand your card out at events or on a counter.",
     "Two limits push people to look elsewhere. The free plan caps HiHello's paper-card and badge "
     "scanner — the feature that captures other people's cards and event badges into your contacts — "
     "at five scans per month, which matters if you collect leads at events.", 1),
    ("CompanyCard is aimed squarely at that second gap: no seat minimum, and no monthly cap on how often "
     "your free card gets scanned.",
     "CompanyCard is aimed squarely at that second gap: no seat minimum, so a two- or three-person "
     "business pays for exactly the seats it has.", 1),
    ("HiHello (verified §)", "HiHello (verified November 2026)", 1),
    ("$7.99 Pro ($5.99/mo billed yearly) · $12 per user Business ($10 billed yearly)",
     "$4.99 Pro ($3.99/mo billed yearly) · $4.99 per user Business ($3.99 billed yearly)", 1),
    ("No HiHello credit", "Not stated on hihello.com/pricing", 1),
])
apply("seo/pages_data2.py", [
    ('["<b>Scan cap on free</b>", "5 card &amp; badge scans per month", "No monthly scan cap"],',
     '["<b>Card &amp; badge scanner on free</b>", "Capped at 5 scans per month", '
     '"No scanner on free — lead capture is a Pro feature"],', 1),
    ("hihello.com/pricing</a> in '\n         + VERIFIED + '. Plans change",
     "hihello.com/pricing</a> on 14 November 2026. Plans change", 1),
])
sync_gen_faq("seo/pages_data2.py", "hihello-alternative.html",
             ["What does CompanyCard cost?", "Can a two-person business get a team plan?"])

gtx("seo/pages_data4.py", [
    # the retired "no monthly cap" edge (it compared HiHello's scanner with scans of our own card)
    ("<p>A monthly cap on how often your card can be scanned matters enormously if you work events, a "
     "counter or a shop floor, and not at all if you share your card a few times a month. HiHello's free "
     "tier caps card and badge scans at five per month; ours has no monthly cap.</p>",
     "<p>None of the free plans here caps how often your own card can be scanned — HiHello's pricing "
     "page says other people can scan your QR code as often as they like on every plan. What HiHello "
     "does cap on its free tier is its paper-card and badge scanner, the feature that saves other "
     "people's cards and event badges as contacts, at five scans a month. CompanyCard's free plan has "
     "no scanner at all; lead capture is a Pro feature.</p>", 1),
])

apply("seo/add_vendor_matrix.py", [
    ('"$8 Pro · $12 per user Business",',
     '"$4.99 Pro ($3.99/mo billed yearly) · $4.99 per user Business ($3.99 billed yearly)",', 1),
    ('"2 cards, email signature, virtual background, Apple Wallet",',
     '"2 cards, email signature, virtual background, Apple &amp; Google Wallet",', 1),
    ('"$9.99 Premium · $6.99 per card Business",',
     '"$9.99 Premium ($7.33/mo billed yearly) · $6.99 per card Business ($4.99 billed yearly)",', 1),
    ('"Individuals who want the most generous free tier"),',
     '"Individuals who want two free cards with signature, background and wallet included"),', 1),
    ('"Someone who wants several free cards and low scan volume"),',
     '"Someone who wants two free cards and scans few paper cards or badges"),', 1),
])

# The renderers must not overwrite the live pages: their shared template (nav, footer,
# Organization/WebSite JSON-LD) is older than the live pages, whatever the content strings say.
GUARD_MARK = "OVERWRITE-LIVE-GUARD-2026-11-14"
for b, slug in [("seo/build_pages15.py", "hihello-vs-blinq.html"), ("seo/build_pages19.py", "blinq-vs-popl.html"),
                ("seo/build_pages20.py", "hihello-vs-popl.html")]:
    t = open(b, encoding="utf-8").read()
    if GUARD_MARK not in t:
        anchor = "sys.path.insert(0, HERE)\n"
        assert t.count(anchor) == 1, f"{b}: guard anchor"
        t = t.replace(anchor, anchor +
                      f"# {GUARD_MARK}: the live {slug} is the source of truth; this renderer's template\n"
                      f"# (nav, footer, Organization/WebSite JSON-LD) is older than the live page.\n"
                      f"if \"--overwrite-live\" not in sys.argv:\n"
                      f"    sys.exit(\"refusing to overwrite {slug}: the live HTML is the source of truth. \"\n"
                      f"             \"Render into a scratch copy (build_pages.ROOT) and diff, or pass --overwrite-live.\")\n")
        open(b, "w", encoding="utf-8").write(t)
        py_compile.compile(b, doraise=True)
        report.append(f"{b}: overwrite-live guard")

DNR_MARK = "DO NOT RE-RUN (one-shot; non-idempotent)"
for w in ["seo/wire_batch15.py", "seo/wire_batch19.py", "seo/wire_batch20.py"]:
    t = open(w, encoding="utf-8").read()
    if DNR_MARK not in t:
        i = t.find('"""')
        assert i != -1, f"{w}: no docstring"
        t = (t[:i + 3] + DNR_MARK + ". Re-running it adds duplicate llms.txt bullets, rolls "
             "dateModified back to its batch date and rewires footers on other pages; wire_batch20 "
             "stops on an assertion. Its strings were corrected on 2026-11-14 for the record only.\n\n"
             + t[i + 3:])
        open(w, "w", encoding="utf-8").write(t)
        py_compile.compile(w, doraise=True)
        report.append(f"{w}: do-not-re-run note")


for g in ["seo/pages_data15.py", "seo/pages_data19.py", "seo/pages_data20.py"]:
    note(g, GEN_NOTE_RENDERED)
for g in ["seo/pages_data2.py", "seo/pages_data4.py", "seo/pages_data6.py", "seo/pages_data14.py",
          "seo/add_vendor_matrix.py"]:
    note(g, GEN_NOTE_STATIC)
note("seo/refresh_verified_nov2026.py",
     "Its Blinq line ('UNCHANGED') was wrong by 2026-11-12 at the latest: blinq.me/pricing "
     "now lists the Universal contact scanner on Free, 'Remove Blinq branding' on Premium, a new "
     "individual Pro tier ($22.49 monthly / $16.58 annually) holding AI enrichment and CSV export, "
     "and Business 'per card, from 5 cards'. Its HiHello sweep also missed five pages, because the "
     "checker below required the word 'cards' right after the numeral. Both were corrected by "
     "seo/fix_vendor_claims_2026_11_14.py; the wider checker is seo/check_vendor_claims.py.")

print("changed URLs:", ", ".join(changed_urls) or "none (already applied)")
print(f"{len(report)} edits applied this run")
for r in report:
    print("  ", r)
