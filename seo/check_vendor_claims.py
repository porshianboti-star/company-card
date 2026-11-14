#!/usr/bin/env python3
"""Stale competitor-claim checker (2026-11-14). Run from repo root; exit 1 on any hit.

Why it exists: the 2026-11-01 re-verify fixed HiHello's free-card count (4 -> 2) but
its checker only matched a numeral followed by the word "cards", so "HiHello leads
with four", "HiHello (four)", "HiHello four." and table cells like "Yes — 4 cards"
stayed live on five pages, in FAQPage JSON-LD and in llms.txt for two weeks. This
checker reads each page the way a reader (or an AI engine) does — visible text with
table cells flattened per row, meta descriptions and JSON-LD — and looks for every
retired claim, not one spelling of it.

Facts it encodes (re-read 2026-11-14, evidence in the run's card-evidence/1114/):
  * HiHello Personal (free) = 2 cards; Professional = 8 cards; Business = 4 cards and
    50 scans per user, pooled (only Enterprise is unlimited).
  * Blinq Free lists the "Universal contact scanner"; Premium lists "Remove Blinq
    branding"; enrichment and CSV export moved to a separate Pro tier; Business is
    "per card, from 5 cards"; no "20+" CRM count on the page.
  * Our own retracted framing: "no monthly cap on scans" as an edge over HiHello.
Monthly re-verifies should run this after their own edits and READ every hit; a
pass means none of these retired strings is present, not that the pages are right.

Scope: *.html, llms.txt, llms-full.txt, seo/pages_data*.py, seo/add_vendor_matrix.py,
seo/wire_*.py. Python module docstrings and comments are skipped (they record what
was true on an older date); adjacent string literals are joined first, so a claim
split across two source lines is still read as one sentence. seo/refresh_verified_*.py
and seo/fix_*.py are not scanned: they hold the old strings as their anchors by design.

Repair 2026-11-14 (after both verifiers showed a 0 here while stale claims were live):
  * new patterns: HiHello Business "unlimited" (Enterprise excepted), "unlimited scans /
    contact enrichment", the numeral 4 before "cards", "at every (paid) tier", Blinq
    Premium "is also the richer individual plan" / "$9.99 a month buys ... scanner",
    "several free cards", Blinq Premium as the top of the personal-plan range;
  * the "billed per user" allowance only applies to HiHello sentences that do not
    mention Blinq;
  * a self-test runs on every invocation: known stale sentences must hit and their
    corrected versions must not;
  * the generators that still have a renderer (pages_data15/19/20) are rendered into a
    temporary directory and scanned too (--no-render skips that), because a generator
    can be wrong while the live page is right.
Usage: python3 seo/check_vendor_claims.py [--no-render]
"""
import glob
import html
import os
import re
import shutil
import sys
import tempfile

FILES = (sorted(glob.glob("*.html")) + ["llms.txt", "llms-full.txt"] +
         sorted(glob.glob("seo/pages_data*.py")) + ["seo/add_vendor_matrix.py"] +
         sorted(glob.glob("seo/wire_*.py")))
RENDER_MODULES = ["pages_data15", "pages_data19", "pages_data20"]

W = r"(?:[^.\n]|\.(?=\d))"   # one character of the same sentence (a decimal point does not end it)
NUM = r"(?<![\w$.,/])(?:four|sixteen|4|16)(?![\w.,%/])"
PATTERNS = [
    ("HiHello near 4/16", re.compile(r"HiHello[^.\n]{0,80}?" + NUM, re.I)),
    ("4/16 near HiHello", re.compile(NUM + r"[^.\n]{0,60}?HiHello", re.I)),
    ("four/16 cards", re.compile(r"\b(?:4|four|16|sixteen)(?: free)? (?:digital business )?cards\b", re.I)),
    ("gives/leads with four", re.compile(r"\b(?:gives|leads with|includes) four\b", re.I)),
    ("no vendor credit", re.compile(r"no vendor credit", re.I)),
    ("Blinq scanner in Premium", re.compile(r"scanner (?:is a|in the paid) Premium|scanner is what you pay for|"
                                            r"(?:scanner|notetaker)[^.\n]{0,40}(?:in|into) Premium", re.I)),
    ("Blinq Premium sales tools", re.compile(r"Blinq(?:'s|’s)? Premium(?:(?!free plan|\bPro\b)" + W + r"){0,160}?"
                                             r"(?:scanner|notetaker|enrich|export)|"
                                             r"Premium is also the richer individual plan|"
                                             r"\$9\.99 a month buys" + W + r"{0,120}?(?:scanner|notetaker|enrich)", re.I)),
    ("cheaper on both paid tiers / every tier", re.compile(r"cheaper on both paid tiers|at every (?:paid )?tier", re.I)),
    ("no monthly cap on scans", re.compile(r"no monthly cap on scans|scans" + W + r"{0,60}?ours has no monthly cap", re.I)),
    ("no listed branding (Blinq)", re.compile(r"without a (?:listed |vendor )?branding line|"
                                             r"do not list one", re.I)),
    ("theirs do not", re.compile(r"credit that theirs do not", re.I)),
    ("pays for four", re.compile(r"pays for four", re.I)),
    ("HiHello Business unlimited", re.compile(r"unlimited cards and scans|unlimited only on the Business|"
                                              r"HiHello" + W + r"{0,120}?Business" + W + r"{0,80}?unlimited|"
                                              r"Business includes" + W + r"{0,60}?unlimited|"
                                              r"unlimited (?:badge |paper-card )?scans|unlimited contact enrichment", re.I)),
    ("Blinq 20+ CRMs", re.compile(r"20\+ (?:native )?CRM", re.I)),
    ("Blinq per user", re.compile(r"\$6\.99 ?/ ?user|\$6\.99 per user|Billed monthly, per user|"
                                  r"\$6\.99/user|Blinq[^.\n]{0,40}\bper user\b", re.I)),
    ("Blinq four plans", re.compile(r"publishes four plans", re.I)),
    ("HiHello 101+ / verified badges", re.compile(r"101\+ users|verified badges", re.I)),
    ("Blinq does not meter", re.compile(r"does not meter", re.I)),
    ("several free cards", re.compile(r"several free cards", re.I)),
    ("Blinq Premium as the personal ceiling", re.compile(r"top out" + W + r"{0,60}?\$9\.99|"
                                                         r"to \$9\.99 a month \(Blinq|"
                                                         r"run about \$3[–-]\$10 a month", re.I)),
]
# Hits that read as current facts on inspection: (regex on the text around the hit, sentence must not name Blinq)
ALLOW = [
    (re.compile(r"four people need a card", re.I), False),          # a worked example, not a count
    (re.compile(r"two, three or four", re.I), False),               # team sizes, not a card count
    (re.compile(r"\b4 cards (?:and 50|per user)", re.I), False),    # HiHello Business: 4 per user, pooled
    (re.compile(r"Enterprise[^.\n]{0,60}unlimited cards and scans", re.I), False),
    (re.compile(r"unlimited only on Enterprise|Enterprise[^.\n]{0,60}unlimited", re.I), False),
    (re.compile(r"rather than per user|per user or per card", re.I), False),
    (re.compile(r"HiHello[^.\n]{0,40}bill(?:s|ed)? per user", re.I), True),
]


def strip_docstrings(src):
    src = re.sub(r'^(\s*(?:#[^\n]*\n|\s*\n)*)("""|\'\'\')(.*?)\2', lambda m: m.group(1) + "\n" * m.group(3).count("\n"),
                 src, count=1, flags=re.S)
    src = re.sub(r"(?m)^\s*#.*$", "", src)
    # join adjacent string literals ("...<newline>   ...") so a sentence split across lines is one
    return re.sub(r'"[ \t]*\n[ \t]*"', "", src).replace('\\"', '"')


def html_views(s):
    out = []
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        out.append(("json-ld", b.replace('\\"', '"')))
    for k, v in re.findall(r'<meta (?:name|property)="([^"]+)" content="([^"]*)"', s):
        out.append((k, html.unescape(v)))
    body = re.sub(r'<(script|style)\b.*?</\1>', " ", s, flags=re.S | re.I)
    body = re.sub(r"</tr>|</p>|</li>|</h\d>|</details>|<br\s*/?>", "\n", body, flags=re.I)
    body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    out.append(("visible", re.sub(r"[ \t]+", " ", body)))
    return out


def views(path):
    s = open(path, encoding="utf-8").read()
    if path.endswith(".py"):
        return [("source", strip_docstrings(s))]
    if path.endswith(".txt"):
        return [("text", s)]
    return html_views(s)


def sentence(text, a, b):
    lo = max(text.rfind(". ", 0, a), text.rfind("\n", 0, a), text.rfind("? ", 0, a)) + 1
    hi = min([x for x in (text.find(". ", b), text.find("\n", b)) if x != -1] or [len(text)])
    return text[lo:hi]


def scan(text):
    """Yield (pattern name, context) for every stale hit in TEXT."""
    for name, rx in PATTERNS:
        for m in rx.finditer(text):
            near = text[max(0, m.start() - 70):m.end() + 40]
            sent = sentence(text, m.start(), m.end())
            if any(a.search(near) and not (no_blinq and re.search(r"Blinq", sent, re.I)) for a, no_blinq in ALLOW):
                continue
            lo, hi = max(0, m.start() - 70), min(len(text), m.end() + 70)
            yield name, text[lo:hi].replace("\n", " ").strip()


# ---------------------------------------------------------------- self-test (runs every time)
MUST_HIT = [
    "HiHello's Business plan lists event lead capture, unlimited scans and unlimited contact enrichment too",
    "Business includes event lead capture and unlimited badge scans",
    "Blinq's Premium is also the richer individual plan. $9.99 a month buys up to five cards, a universal "
    "contact scanner, an AI notetaker and AI contact enrichment.",
    "If you need several free cards, that is HiHello.",
    "Paid personal plans start at $3 a month (Mobilo Pro) and top out around $9.99 a month (Blinq Premium).",
    "Paid personal plans run from $3 a month (Mobilo Pro) to $9.99 a month (Blinq Premium), and team plans",
    "Most digital business cards have a free plan. Paid personal plans run about $3–$10 a month and team plans",
    "Blinq Business is billed per user at $6.99",
    "HiHello bills per user and Blinq bills per user too.",
    "Free plan\n 4 cards, 5 scans/mo",
    "HiHello wins on price, at every tier",
    "HiHello and Blinq are both cheaper than CompanyCard at every paid tier",
    "$0 — Personal, 4 cards, 5 scans a month",
    "HiHello's free tier caps card and badge scans at five per month; ours has no monthly cap.",
]
MUST_PASS = [
    "HiHello's Business plan lists event lead capture too, with 50 paper-card or badge scans and 50 contact "
    "enrichments per user a month, pooled across the team (unlimited only on Enterprise; re-checked 14 "
    "November 2026), but the product is built around the card;",
    "Business includes event lead capture and 50 paper-card or badge scans per user a month, pooled across the team",
    "4 cards and 50 paper-card or badge scans per user a month, pooled across the team",
    "Blinq also has the richer individual plans. Its free plan already lists a universal contact scanner and "
    "an AI notetaker (notes from the last 30 days); Premium at $9.99 a month adds up to five cards, a branded "
    "QR code, custom design and no Blinq branding; Pro at $22.49 a month ($16.58 billed annually) adds AI "
    "contact enrichment, unlimited AI notes and CSV export.",
    "If you need two free cards, that is HiHello or Blinq.",
    "Most paid personal plans cost between $3 a month (Mobilo Pro) and $9.99 a month (Blinq Premium). Blinq "
    "also sells a Pro tier for one person at $22.49 a month",
    "Business is $6.99 per card a month, with a minimum of five cards and billing per card rather than per user.",
    "HiHello wins on price for one person; the team tier is a near tie",
    "twenty on Professional (unlimited with an add-on), fifty per user a month pooled on Business, which you "
    "cannot buy under five users, and unlimited only on Enterprise.",
    "HiHello's Business plan is billed per user.",
    "and our Pro plan is $4.99 a month against Blinq Premium at $9.99, though Blinq's free plan already lists "
    "a universal contact scanner and an AI notetaker, and Blinq Pro ($22.49 a month) adds AI contact enrichment",
]


def self_test():
    bad = [t for t in MUST_HIT if not list(scan(t))] + [t for t in MUST_PASS if list(scan(t))]
    for t in bad:
        print("SELF-TEST FAILED on: " + t[:120])
    return len(bad)


def render_generators():
    """Render RENDER_MODULES into a temp dir (never the repo) and yield (slug, html)."""
    tmp = tempfile.mkdtemp(prefix="cvc-render-")
    try:
        sys.path.insert(0, os.path.abspath("seo"))
        import importlib
        import build_pages
        build_pages.ROOT = tmp
        for mod in RENDER_MODULES:
            for slug in build_pages.write_pages(importlib.import_module(mod).PAGES):
                yield mod + "->" + slug, open(os.path.join(tmp, slug), encoding="utf-8").read()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


hits = 0
failed = self_test()
for f in FILES:
    try:
        vs = views(f)
    except FileNotFoundError:
        continue
    for view, text in vs:
        for name, ctx in scan(text):
            hits += 1
            print(f"{f} [{view}] {name}: …{ctx}…")
rendered = 0
if "--no-render" not in sys.argv:
    for label, h in render_generators():
        rendered += 1
        for view, text in html_views(h):
            for name, ctx in scan(text):
                hits += 1
                print(f"render:{label} [{view}] {name}: …{ctx}…")
print(f"check_vendor_claims: {hits} stale hit(s) in {len(FILES)} files"
      + (f" + {rendered} generator render(s)" if rendered else "")
      + f"; self-test {'FAILED (' + str(failed) + ')' if failed else 'ok'} "
        f"({len(MUST_HIT)} stale + {len(MUST_PASS)} corrected sentences)")
sys.exit(1 if hits or failed else 0)
