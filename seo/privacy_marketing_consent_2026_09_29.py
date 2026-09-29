#!/usr/bin/env python3
"""Privacy policy: marketing emails are opt-in (2026-09-29). Idempotent.

Before the first tips/offers email the policy must say what the new signup
checkbox and Settings toggle do (legal checklist, item 5). Adds:
  * one bullet under "How we use your information";
  * one sentence under "Your rights" about unsubscribing;
  * "Last updated", JSON-LD dateModified and the sitemap <lastmod> -> 2026-09-29.
Wording is about CompanyCard only and states no price, provider or sending date.
Run from the repo root: python3 seo/privacy_marketing_consent_2026_09_29.py
"""
import re
import sys

PAGE = "privacy-policy.html"
SITEMAP = "sitemap.xml"
DATE_ISO = "2026-09-29"
DATE_TEXT = "29 September 2026"

USE_ANCHOR = "<li>To communicate with you about your account and important changes.</li>"
USE_BULLET = ("<li>To send you CompanyCard tips and occasional offers by email, only if you ask for them "
              "by ticking the box at signup or turning them on under Email preferences in your account. "
              "They are off unless you turn them on.</li>")

RIGHTS_ANCHOR = ("to object to or restrict certain processing. To exercise these rights, contact us using "
                 "the details below. You can edit or delete most data directly in the app.</p>")
RIGHTS_ADD = ("<p>If you agreed to tips and offers by email, you can stop them at any time: every such "
              "email has an unsubscribe link that works in one step, and you can switch them off under "
              "Email preferences in your account. Stopping them does not affect emails about your "
              "account itself.</p>")


def main() -> int:
    src = open(PAGE, encoding="utf-8").read()
    out = src
    if USE_BULLET not in out:
        if out.count(USE_ANCHOR) != 1:
            sys.exit(f"FATAL: use-anchor found {out.count(USE_ANCHOR)} times")
        out = out.replace(USE_ANCHOR, USE_ANCHOR + "\n" + USE_BULLET, 1)
    if RIGHTS_ADD not in out:
        if out.count(RIGHTS_ANCHOR) != 1:
            sys.exit(f"FATAL: rights-anchor found {out.count(RIGHTS_ANCHOR)} times")
        out = out.replace(RIGHTS_ANCHOR, RIGHTS_ANCHOR + "\n" + RIGHTS_ADD, 1)
    if out != src:
        out, n1 = re.subn(r"Last updated: [0-9]{1,2} [A-Z][a-z]+ 20[0-9]{2}", "Last updated: " + DATE_TEXT, out)
        out, n2 = re.subn(r'"dateModified":"20[0-9]{2}-[0-9]{2}-[0-9]{2}"', '"dateModified":"' + DATE_ISO + '"', out)
        if n1 != 1 or n2 != 1:
            sys.exit(f"FATAL: date stamps matched {n1}/{n2}, expected 1/1")
        open(PAGE, "w", encoding="utf-8").write(out)
        print(f"{PAGE}: updated")
    else:
        print(f"{PAGE}: already up to date")

    sm = open(SITEMAP, encoding="utf-8").read()
    pat = re.compile(r"(<loc>https://company-card\.com/privacy-policy\.html</loc>\s*<lastmod>)([0-9-]{10})(</lastmod>)")
    m = pat.search(sm)
    if not m:
        sys.exit("FATAL: privacy-policy entry not found in sitemap.xml")
    if m.group(2) < DATE_ISO and USE_BULLET in out:
        sm = pat.sub(lambda x: x.group(1) + DATE_ISO + x.group(3), sm, count=1)
        open(SITEMAP, "w", encoding="utf-8").write(sm)
        print(f"{SITEMAP}: privacy-policy lastmod -> {DATE_ISO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
