#!/usr/bin/env python3
"""Add the GA4 tag (G-33HCVG9DKG) to every served CompanyCard page, plus
pay_intent / signup_click event instrumentation on the pages that carry CTAs.

Safety rules (learned the hard way in this repo):
  * Insert-only edits. We NEVER remove text and NEVER anchor anything at
    </head> (a past bounded edit at </head> wiped a stylesheet in prod).
  * The GA tag is inserted immediately after the opening <head> tag,
    matched robustly with a regex (some pages have byte-distinct heads).
  * The events snippet is inserted immediately before the LAST </body>.
  * Idempotent: files already containing the GA id / event code are skipped.
  * After every edit we assert the file only grew by exactly the snippet
    size and that every <style>/<link> block survived, then HTML-parse it.

Usage: python3 seo/add_ga4.py            (from anywhere; paths are absolute)
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GA_ID = "G-33HCVG9DKG"
HEAD_RE = re.compile(r"<head[^>]*>", re.IGNORECASE)

GA_SNIPPET_LINES = [
    "<!-- Google tag (gtag.js) -->",
    '<script async src="https://www.googletagmanager.com/gtag/js?id=G-33HCVG9DKG"></script>',
    "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
    "gtag('js',new Date());gtag('config','G-33HCVG9DKG');</script>",
]

# Pages that carry the CTAs we instrument. pricing.html is the only page in
# the repo with the paid-plan (Pro $8 / Business $12) buttons; index.html
# carries the free get-started CTAs. Other pages mention $8/$12 only in
# comparison-table prose, with no plan buttons.
EVENT_PAGES = ["index.html", "pricing.html"]

EVENTS_SNIPPET = """<script>
/* GA4 CTA events: pay_intent (paid-plan buttons) + signup_click (free/get-started) */
document.addEventListener('click',function(e){
  if(typeof gtag!=='function')return;
  var a=e.target.closest&&e.target.closest('a.btn');
  if(!a)return;
  var plan=a.closest('.plan');
  if(plan){
    var h=plan.querySelector('h3');
    var name=h?h.textContent.trim().toLowerCase():'';
    if(name==='pro'||name==='business'){
      gtag('event','pay_intent',{plan:name,page_location:location.pathname});
      return;
    }
  }
  if((a.getAttribute('href')||'').indexOf('app/builder.html')>-1){
    gtag('event','signup_click',{page_location:location.pathname});
  }
});
</script>
"""


class _Checker(HTMLParser):
    """Parse-only pass; raises nothing on well-formed-enough HTML."""


def parse_ok(text: str) -> bool:
    try:
        p = _Checker(convert_charrefs=True)
        p.feed(text)
        p.close()
        return True
    except Exception:
        return False


def preserved(old: str, new: str, inserted_len: int, path: Path) -> None:
    """Assert the edit was purely additive and no head assets were lost."""
    if len(new) != len(old) + inserted_len:
        sys.exit(f"FATAL {path}: size changed by {len(new)-len(old)}, "
                 f"expected +{inserted_len}. Aborting before write.")
    for token in ("<style", "</style>", "<link", "</head>", "</body>"):
        if new.count(token) != old.count(token):
            sys.exit(f"FATAL {path}: count of {token!r} changed. Aborting.")
    if not parse_ok(new):
        sys.exit(f"FATAL {path}: patched HTML no longer parses. Aborting.")


def add_ga_tag(path: Path) -> str:
    old = path.read_text(encoding="utf-8")
    if GA_ID in old:
        return "already"
    m = HEAD_RE.search(old)
    if not m:
        return "no-head"
    # Match the indentation of the first line that follows <head>.
    after = old[m.end():]
    nl = after.find("\n")
    next_line = after[nl + 1:].split("\n", 1)[0] if nl != -1 else ""
    indent = next_line[: len(next_line) - len(next_line.lstrip())] if next_line.strip() else ""
    block = "\n" + "\n".join(indent + line for line in GA_SNIPPET_LINES)
    if not after.startswith("\n"):
        block += "\n"  # keep any same-line content on its own line
    new = old[: m.end()] + block + old[m.end():]
    preserved(old, new, len(block), path)
    path.write_text(new, encoding="utf-8")
    return "tagged"


def add_events(path: Path) -> str:
    old = path.read_text(encoding="utf-8")
    if "pay_intent" in old or "signup_click" in old:
        return "already"
    i = old.rfind("</body>")
    if i == -1:
        return "no-body"
    block = EVENTS_SNIPPET
    new = old[:i] + block + old[i:]
    preserved(old, new, len(block), path)
    path.write_text(new, encoding="utf-8")
    return "added"


def main() -> None:
    # Root pages + app/ product pages. extension/, growth-ext/, growth/,
    # seo/, server/, assets/ are never touched.
    targets = sorted(REPO.glob("*.html")) + sorted((REPO / "app").glob("*.html"))
    tagged, skipped_dup, skipped_nohead = [], [], []
    for f in targets:
        r = add_ga_tag(f)
        {"tagged": tagged, "already": skipped_dup, "no-head": skipped_nohead}[r].append(f)

    ev = {}
    for name in EVENT_PAGES:
        ev[name] = add_events(REPO / name)

    print(f"GA4 tag inserted : {len(tagged)}")
    print(f"already tagged   : {len(skipped_dup)}")
    for f in skipped_nohead:
        print(f"skipped (no <head>): {f.relative_to(REPO)}")
    for name, r in ev.items():
        print(f"events on {name}: {r}")


if __name__ == "__main__":
    main()
