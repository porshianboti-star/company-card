#!/usr/bin/env python3
"""Make every FAQPage answer byte-identical to the answer shown on the page,
and FAIL when a FAQPage Question has no visible twin at all.

The visible <details class="lp-faq"> copy is the source of truth; the JSON-LD is
rewritten to match it. Exact-match text is what an assistant can quote verbatim,
and it removes any doubt under Google's "structured data must reflect visible
content" rule. Idempotent — safe to re-run.

Twin rule (added 2026-09-27): every Question in a FAQPage block must be visible
on the page. A twin is either
  (a) a <details class="lp-faq"> whose <summary> equals the question — its body
      then overwrites the JSON-LD answer; or
  (b) the question AND the answer both present verbatim in the page's visible
      text (older pages mark their FAQ up as <h3>/<p>; nothing is rewritten).
A Question with neither is an orphan: it is listed on stderr and the script
exits 1. Before this rule a page with zero lp-faq blocks was skipped entirely,
and an orphan Question on a page that did have lp-faq blocks passed as
"synced 0" — that is how 'What is a digital business card?' on
digital-business-card.html lived in the JSON-LD with no visible twin.

Run from repo root: python3 seo/sync_faq_schema.py   (exit 0 = every FAQPage
Question has a visible twin and every lp-faq answer is byte-identical)
"""
import glob, re, json, html as ht, sys

LD = r'<script type="application/ld\+json">(.*?)</script>'

def visible_faqs(body):
    """{question: answer_text} from the rendered <details class="lp-faq"> blocks."""
    out = {}
    for m in re.finditer(r'<details class="lp-faq"><summary>(.*?)</summary>(.*?)</details>',
                         body, re.S):
        q = ht.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        a = ht.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        out[q] = re.sub(r"\s+", " ", a).strip()
    return out

def visible_text(body):
    """The page's rendered text (scripts/styles removed, tags → spaces, whitespace collapsed)."""
    body = re.sub(r"<(script|style)\b.*?</\1>", " ", body, flags=re.S | re.I)
    return re.sub(r"\s+", " ", ht.unescape(re.sub(r"<[^>]+>", " ", body))).strip()

def norm(s):
    return re.sub(r"\s+", " ", ht.unescape(s)).strip()

total_files = total_fixed = 0
orphans = []          # (file, question) — JSON-LD Question with no visible twin
verbatim_only = 0     # twins found via rule (b)
for f in sorted(glob.glob("*.html")):
    h = open(f, encoding="utf-8").read()
    blocks = re.findall(LD, h, re.S)
    if not any('"FAQPage"' in b for b in blocks):
        continue
    body = re.sub(LD, "", h, flags=re.S)
    vis = visible_faqs(body)
    text = visible_text(body)
    changed = 0
    for b in blocks:
        if '"FAQPage"' not in b:
            continue
        d = json.loads(b)
        for q in d.get("mainEntity", []):
            name = q["name"].strip()
            ans = q["acceptedAnswer"]["text"]
            v = vis.get(name)
            if v is not None:                      # rule (a): lp-faq twin, visible copy wins
                if ans != v:
                    q["acceptedAnswer"]["text"] = v
                    changed += 1
            elif norm(name) in text and norm(ans) in text:   # rule (b): verbatim elsewhere
                verbatim_only += 1
            else:
                orphans.append((f, name))
        if changed:
            new = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
            h = h.replace(b, new, 1)
    if changed:
        open(f, "w", encoding="utf-8").write(h)
        print(f"  {f}: synced {changed} answer(s)")
        total_fixed += changed
    total_files += 1

print(f"Scanned {total_files} FAQ pages; synced {total_fixed} answers; "
      f"{verbatim_only} question(s) matched verbatim outside lp-faq markup.")
if orphans:
    print(f"FAIL: {len(orphans)} FAQPage question(s) with no visible twin:", file=sys.stderr)
    for f, name in orphans:
        print(f"  {f}: {name!r}", file=sys.stderr)
    sys.exit(1)
print("OK: every FAQPage question has a visible twin.")
