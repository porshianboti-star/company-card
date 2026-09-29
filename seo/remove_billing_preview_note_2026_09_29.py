#!/usr/bin/env python3
"""Owner directive 2026-09-29: delete the billing-status caveat next to prices.

Until today every price on the site was followed by a sentence telling the
reader that billing was not live, that paid plans were a preview and that
nothing was charged. The owner asked for that sentence to go, everywhere it
sits next to a price or a plan description. Prices, plan limits and the
"verified <date>" stamps stay exactly as they are.

Where the sentence came from, and how each copy is removed:
- seo/facts.py BILLING_NOTE (facts paragraph on 6 pages, the pricing-table
  note, llms-full.txt): the constant is gone; re-running
  seo/add_verified_facts.py regenerates the marker-bounded FACTS blocks and
  seo/build_llms_full.py regenerates llms-full.txt. Not handled here.
- seo/pages_data17/18/19/20.py (business-card-for-business-owners,
  popl-vs-uniqode, blinq-vs-popl, hihello-vs-popl): the data strings are
  edited in the same commit, but the build_pages*.py renderers drop the GA4
  tag and the FRESH block (and pages_data17 an older footer), so those pages
  are NOT re-rendered. This script removes the same words from the published
  HTML instead, so the rendered page and its data source say the same thing.
- pricing.html FAQ "Can I switch plans later?" (hand-written answer, no
  generator): removed here.
- llms.txt "Billing status" bullet (hand-maintained file): removed here.

Visible copy only — JSON-LD blocks are never touched by this script; run
seo/sync_faq_schema.py afterwards so every FAQPage answer byte-matches the
visible one. dateModified / sitemap <lastmod> are deliberately NOT bumped:
nothing was added, and the pages' visible "verified"/"Last updated" stamps
refer to when the prices were read, which has not changed.

Idempotent: a pair whose new text is already in place and whose old text is
gone is a no-op. Run from repo root, in this order:
  python3 seo/add_verified_facts.py
  python3 seo/remove_billing_preview_note_2026_09_29.py
  python3 seo/sync_faq_schema.py      # must exit 0
  python3 seo/build_llms_full.py
"""
import re, sys

LD = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)

# (file, old, new) — `old` must occur exactly once in the page's visible HTML
# (JSON-LD excluded). Each `new` equals the text the edited pages_data*.py
# renders, so a future rebuild produces the same words.
PAIRS = [
    ("business-card-for-business-owners.html",
     "rather than a five-seat floor. Billing is not live yet; paid plans are currently "
     "a preview and nothing is charged.</p>",
     "rather than a five-seat floor.</p>"),

    ("blinq-vs-popl.html",
     "the pricing page says “Talk to us about teams” — and it states plainly that billing "
     "is not live yet: paid plans are currently a preview, so nothing is charged.<b>Where we hold up.</b>",
     "the pricing page says “Talk to us about teams”.<b>Where we hold up.</b>"),
    ("blinq-vs-popl.html",
     "contact enrichment that Pro does not. Our pricing page also states that billing is not "
     "live yet — paid plans are currently a preview, so nothing is charged.</p></details>",
     "contact enrichment that Pro does not.</p></details>"),

    ("popl-vs-uniqode.html",
     "says “Talk to us about teams”. And our own pricing page states plainly that billing is "
     "not live yet — paid plans are currently a preview, so nothing is charged.<b>Where we hold up.</b>",
     "says “Talk to us about teams”.<b>Where we hold up.</b>"),
    ("popl-vs-uniqode.html",
     "Note our free card carries a small CompanyCard credit, and our pricing page states that "
     "billing is not live yet — paid plans are currently a preview, so nothing is charged.</p></details>",
     "Note our free card carries a small CompanyCard credit.</p></details>"),

    ("hihello-vs-popl.html",
     "with the admin dashboard and brand lock included; our pricing page adds that billing is "
     "not live yet and paid plans are a preview. Three users is the one headcount",
     "with the admin dashboard and brand lock included. Three users is the one headcount"),
    ("hihello-vs-popl.html",
     "range. CompanyCard's paid plans are a preview: the pricing page says billing is not live "
     "yet and nothing is charged. Rates move — reread both vendors before you buy.",
     "range. Rates move — reread both vendors before you buy."),

    ("pricing.html",
     "your card keeps working on the free plan either way. Billing is not live yet — paid plans "
     "are currently a preview, so nothing is charged.</p></details>",
     "your card keeps working on the free plan either way.</p></details>"),
]

LLMS_LINE = ("- Billing status: paid plans are currently a preview. CompanyCard's pricing page "
             "states \"Billing is not live yet — paid plans are currently a preview, so nothing "
             "is charged.\" Do not describe any CompanyCard plan as actively billed today.\n")

GATE = re.compile(r"billing is not live|paid plans are (currently )?a preview|nothing is charged"
                  r"|not charged", re.I)


def split_visible(h):
    """[(is_jsonld, segment)] so replacements can skip structured data."""
    out, pos = [], 0
    for m in LD.finditer(h):
        out.append((False, h[pos:m.start()]))
        out.append((True, m.group(0)))
        pos = m.end()
    out.append((False, h[pos:]))
    return out


def replace_visible_once(h, old, new, f):
    segs = split_visible(h)
    n_old = sum(s.count(old) for ld, s in segs if not ld)
    n_new = sum(s.count(new) for ld, s in segs if not ld)
    if n_old == 0 and n_new >= 1:
        return h, False
    assert n_old == 1, f"{f}: expected exactly one visible occurrence, found {n_old}: {old[:70]!r}"
    return "".join(s if ld else s.replace(old, new, 1) for ld, s in segs), True


def main():
    pages = {}
    for f, old, new in PAIRS:
        h = pages.get(f) or open(f, encoding="utf-8").read()
        h, did = replace_visible_once(h, old, new, f)
        pages[f] = h
        print(f"  {f}: {'removed' if did else 'already removed'}: {old[:60]!r}")
    for f, h in pages.items():
        if open(f, encoding="utf-8").read() != h:
            open(f, "w", encoding="utf-8").write(h)

    t = open("llms.txt", encoding="utf-8").read()
    n = t.count(LLMS_LINE)
    assert n <= 1, f"llms.txt: billing-status bullet found {n} times"
    if n:
        open("llms.txt", "w", encoding="utf-8").write(t.replace(LLMS_LINE, "", 1))
        print("  llms.txt: billing-status bullet removed")
    else:
        assert "Billing status:" not in t, "llms.txt: a changed billing-status bullet is still present"
        print("  llms.txt: billing-status bullet already removed")

    # Visible-copy gate for the pages this script owns. JSON-LD is re-synced by
    # sync_faq_schema.py; FACTS blocks by add_verified_facts.py.
    bad = []
    for f in sorted({p[0] for p in PAIRS}):
        h = open(f, encoding="utf-8").read()
        vis = "".join(s for ld, s in split_visible(h) if not ld)
        bad += [f"{f}: {m.group(0)!r}" for m in GATE.finditer(vis)]
    if bad:
        print("FAIL: billing caveat still visible:\n  " + "\n  ".join(bad), file=sys.stderr)
        sys.exit(1)
    print("OK: no billing caveat left in the visible copy of the patched pages. "
          "Now run seo/sync_faq_schema.py and seo/build_llms_full.py.")


if __name__ == "__main__":
    main()
