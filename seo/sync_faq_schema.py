#!/usr/bin/env python3
"""Make every FAQPage answer byte-identical to the answer shown on the page.

The visible <details> copy is the source of truth; the JSON-LD is rewritten to
match it. Substance already matched (these were paraphrases, not phantom
answers) but exact-match text is what an assistant can quote verbatim, and it
removes any doubt under Google's "structured data must reflect visible content"
rule. Idempotent — safe to re-run.

Run from repo root: python3 sync_faq_schema.py
"""
import glob, re, json, html as ht

def visible_faqs(body):
    """{question: answer_text} from the rendered <details class="lp-faq"> blocks."""
    out = {}
    for m in re.finditer(r'<details class="lp-faq"><summary>(.*?)</summary>(.*?)</details>',
                         body, re.S):
        q = ht.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        a = ht.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        out[q] = re.sub(r"\s+", " ", a).strip()
    return out

total_files = total_fixed = 0
for f in sorted(glob.glob("*.html")):
    h = open(f, encoding="utf-8").read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    if not any('"FAQPage"' in b for b in blocks):
        continue
    body = re.sub(r'<script type="application/ld\+json">.*?</script>', "", h, flags=re.S)
    vis = visible_faqs(body)
    if not vis:
        continue
    changed = 0
    for b in blocks:
        if '"FAQPage"' not in b:
            continue
        d = json.loads(b)
        for q in d.get("mainEntity", []):
            v = vis.get(q["name"].strip())
            if v and q["acceptedAnswer"]["text"] != v:
                q["acceptedAnswer"]["text"] = v
                changed += 1
        if changed:
            new = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
            h = h.replace(b, new, 1)
    if changed:
        open(f, "w", encoding="utf-8").write(h)
        print(f"  {f}: synced {changed} answer(s)")
        total_fixed += changed
    total_files += 1

print(f"Scanned {total_files} FAQ pages; synced {total_fixed} answers.")
