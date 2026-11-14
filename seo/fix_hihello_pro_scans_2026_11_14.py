"""HiHello Professional scan cap: add the add-on clause (2026-11-14).

hihello.com/pricing (read 2026-11-14, card-evidence/1114) lists Professional scans as
"20, or unlimited with add-on". hihello-vs-blinq said "20" with no add-on. Idempotent:
each edit is skipped when its NEW text is already present; otherwise OLD must occur
exactly the expected number of times.
"""
import sys

EDITS = [
    ("hihello-vs-blinq.html", "Professional users at 20, while", "Professional users at 20 (unlimited with an add-on), while", 2),
    ("hihello-vs-blinq.html", "Professional tier at twenty;", "Professional tier at twenty (unlimited with an add-on);", 1),
    ("seo/pages_data15.py", "Professional users at 20, while", "Professional users at 20 (unlimited with an add-on), while", 1),
]

done = 0
for path, old, new, n in EDITS:
    t = open(path, encoding="utf-8").read()
    if t.count(new) >= n:
        continue
    c = t.count(old)
    assert c == n, f"{path}: {old!r} found {c} times, want {n}"
    open(path, "w", encoding="utf-8").write(t.replace(old, new))
    done += 1
print(f"{done} edits applied")
sys.exit(0)
