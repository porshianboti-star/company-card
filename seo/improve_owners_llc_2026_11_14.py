#!/usr/bin/env python3
"""Improve business-card-for-business-owners.html for the LLC questions (2026-11-14,
rank plan CC-1 as modified by both verifiers). Idempotent; every anchor is asserted.

Why: GSC (Search Console, 90 days to 2026-11-10) — the page is CompanyCard's only
non-brand click earner (13 clicks / 1,658 impressions / avg position 7.2; 93% of
impressions are anonymised, so their topics are unknown, and at least 5 of the 13
clicks are non-US). Visible LLC rows: "how to write llc on business card" 11 @ 17.8,
"how to put llc on business cards" 6 @ 36.3, "does llc need to be on business card"
3 @ 60.3. The page already has the FAQ "How do I put LLC on a business card?"
(10-23) — so this run does NOT add a near-duplicate "How do I write LLC" FAQ. What
the page lacks is the "write" wording in a heading, the "do I need it" question, and
the punctuation question the ranking answers cover ("LLC" vs ", LLC" vs "L.L.C.").
The meta description was 220 characters (cut off in results) and differed from
og/twitter.

What:
  1. description = og:description = twitter:description, 145 characters.
  2. H2 "Where LLC, Ltd or Inc goes on the card" -> "How to write LLC, Ltd or Inc on a
     business card", with id="llc". Section body unchanged except (3).
  3. One sentence in that section: copy the punctuation exactly as registered. It
     states no legal rule.
  4. "The fields that actually get used": one item for the business name, worded to
     match the section ("as it is registered") and the not-registered-yet section.
  5. ONE new FAQ, "Do I need to put LLC on my business card?", visible and appended to
     the FAQPage JSON-LD (sync_faq_schema.py only rewrites existing answers). Every
     clause restates text already on the page; no jurisdiction's rule is asserted.
  6. dateModified + sitemap lastmod -> 2026-11-14 for this URL only.
Title and H1 are untouched (the page ranks 4-9 daily). Does NOT re-run
improve_owners_titles_2026_10_23.py (its step 4 rewrites the dates to 10-23) and does
NOT run add_freshness.py. This page has no complete generator: seo/pages_data17.py
lacks the 10-23 and 11-14 edits, so the improve scripts are its source of truth.

Run from repo root: python3 seo/improve_owners_llc_2026_11_14.py
then python3 seo/sync_faq_schema.py and python3 seo/build_llms_full.py.
"""
import json
import re

DATE = "2026-11-14"
F = "business-card-for-business-owners.html"
s = open(F, encoding="utf-8").read()
changed = []

# ---------- 1. description = og = twitter ----------
DESC = ("Owner, Founder, Director or the trade itself? How to pick one title, where LLC goes, "
        "and what co-owners or unregistered businesses put on a card.")
assert len(DESC) == 145, len(DESC)
# The value each tag held on 2026-11-13 (HEAD d2e37c7). Anything else means another edit (the
# every-2-days GEO loop, say) touched it since: stop rather than overwrite it unseen.
OLD_DESC = {
    'name="description"': ("What job title to use when you own the business, how two co-owners should "
                           "handle cards, and what to put on a card when the business isn&#x27;t "
                           "registered yet. A practical guide for small business owners and the "
                           "self-employed."),
    'property="og:description"': ("Owner, Founder, Director or Principal? How co-owners should split cards, "
                                  "and what you can put on a card before the business is registered."),
}
OLD_DESC['name="twitter:description"'] = OLD_DESC['property="og:description"']
for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    m = re.search(r'<meta ' + re.escape(attr) + r' content="([^"]*)">', s)
    assert m, f"{attr} not found"
    assert s.count(m.group(0)) == 1, f"{attr} not unique"
    assert m.group(1) in (OLD_DESC[attr], DESC), f"{attr} changed since 2026-11-13: {m.group(1)[:80]!r}"
    if m.group(1) != DESC:
        s = s.replace(m.group(0), f'<meta {attr} content="{DESC}">', 1)
        changed.append(attr)

# ---------- 2. H2 rename + id ----------
OLD_H2 = "<h2>Where LLC, Ltd or Inc goes on the card</h2>"
NEW_H2 = '<h2 id="llc">How to write LLC, Ltd or Inc on a business card</h2>'
if NEW_H2 not in s:
    assert s.count(OLD_H2) == 1, "LLC H2 not unique"
    s = s.replace(OLD_H2, NEW_H2, 1)
    changed.append("h2")

# ---------- 3. punctuation sentence ----------
P_ANCHOR = ("&ldquo;Sam Okafor, LLC&rdquo; does not, because an LLC is a thing you own, not a "
            "title you hold.</p>")
P_NEW = ("&ldquo;Sam Okafor, LLC&rdquo; does not, because an LLC is a thing you own, not a "
         "title you hold. Copy the punctuation exactly as it appears on your registration "
         "&mdash; &ldquo;Okafor Bookkeeping LLC&rdquo;, &ldquo;Okafor Bookkeeping, LLC&rdquo; or "
         "&ldquo;Okafor Bookkeeping L.L.C.&rdquo;.</p>")
if "Copy the punctuation exactly" not in s:
    assert s.count(P_ANCHOR) == 1, "LLC paragraph anchor not unique"
    s = s.replace(P_ANCHOR, P_NEW, 1)
    changed.append("punctuation")

# ---------- 4. fields list item ----------
TICK = ('<li><span class="tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/>'
        '</svg></span><span>')
LINK_ITEM = ("<b>One link.</b> The page that proves you are real: a site, a booking page, a "
             "portfolio, a profile. One.</span></li>")
NAME_ITEM = (TICK + "<b>The business name.</b> As it is registered, with LLC, Ltd or Inc only if "
             "the business really is one (see <a href=\"#llc\">how to write LLC</a> above), or "
             "your own name and the work if it is not registered yet.</span></li>")
if "<b>The business name.</b>" not in s:
    assert s.count(LINK_ITEM) == 1, "One link item not unique"
    assert s.find(NEW_H2) < s.find(LINK_ITEM), "LLC section is not above the fields list"
    s = s.replace(LINK_ITEM, LINK_ITEM + NAME_ITEM, 1)
    changed.append("field-item")

# ---------- 5. one FAQ, visible + JSON-LD ----------
Q = "Do I need to put LLC on my business card?"
A = ("It depends on where the business is registered. Some jurisdictions expect the registered "
     "name, suffix included, wherever the business presents itself; others let a registered "
     "company trade under a shorter name as long as the legal name is disclosed somewhere. Check "
     "with your own registrar before you print it. If you include it, it belongs to the business "
     "name — “Okafor Bookkeeping LLC” — not to your own name, and if the business is not "
     "registered yet, leave LLC off.")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


FAQ_H2 = "<h2>Frequently asked questions</h2>"
i = s.find(FAQ_H2)
assert i != -1 and s.count(FAQ_H2) == 1, "FAQ section not found"
j = s.find("</section>", i)
assert s[j - len("</details></div>"):j] == "</details></div>", "unexpected FAQ section ending"
if f"<summary>{esc(Q)}</summary>" not in s:
    blk = f'<details class="lp-faq"><summary>{esc(Q)}</summary><p>{esc(A)}</p></details>'
    s = s[:j - len("</div>")] + blk + s[j - len("</div>"):]
    changed.append("faq")

ld = re.search(r'<script type="application/ld\+json">(\{"@context":"https://schema.org",'
               r'"@type":"FAQPage".*?)</script>', s, re.S)
assert ld, "FAQPage JSON-LD not found"
data = json.loads(ld.group(1))
if Q not in {q["name"] for q in data["mainEntity"]}:
    data["mainEntity"].append({"@type": "Question", "name": Q,
                               "acceptedAnswer": {"@type": "Answer", "text": A}})
    s = s.replace(ld.group(1), json.dumps(data, ensure_ascii=False, separators=(",", ":")), 1)
    changed.append("faq-schema")

# ---------- 6. dateModified + sitemap ----------
m = re.search(r'("url":"https://company-card\.com/' + re.escape(F) +
              r'"[^<]*?"dateModified":")(\d{4}-\d{2}-\d{2})(")', s)
assert m, "WebPage dateModified not found"
if m.group(2) != DATE:
    s = s[:m.start(2)] + DATE + s[m.end(2):]
    changed.append("dateModified")
open(F, "w", encoding="utf-8").write(s)

sm = open("sitemap.xml", encoding="utf-8").read()
pat = re.compile(r'(<loc>https://company-card\.com/' + re.escape(F) + r'</loc><lastmod>)(\d{4}-\d{2}-\d{2})')
mm = pat.search(sm)
assert mm, "sitemap entry not found"
if mm.group(2) != DATE:
    sm = pat.sub(lambda x: x.group(1) + DATE, sm, count=1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    changed.append("sitemap-lastmod")

# ---------- 7. generator: same description, and a note that the page outgrew it ----------
G = "seo/pages_data17.py"
g = open(G, encoding="utf-8").read()
OLD_META = ('"meta": ("What job title to use when you own the business, how two co-owners should "\n'
            '             "handle cards, and what to put on a card when the business isn\'t registered "\n'
            '             "yet. A practical guide for small business owners and the self-employed."),')
OLD_OG = ('"og": ("Owner, Founder, Director or Principal? How co-owners should split cards, and "\n'
          '           "what you can put on a card before the business is registered."),')
NEW_META = '"meta": ("' + DESC + '"),'
NEW_OG = '"og": ("' + DESC + '"),'
if NEW_META not in g:
    assert g.count(OLD_META) == 1 and g.count(OLD_OG) == 1, "pages_data17 meta/og anchors"
    g = g.replace(OLD_META, NEW_META, 1).replace(OLD_OG, NEW_OG, 1)
    changed.append("generator-meta")
NOTE = ("SUPERSEDED IN PART, 2026-11-14. The live page carries sections and FAQs this file does "
        "not: the title-table rows, the LLC section and two FAQs from "
        "seo/improve_owners_titles_2026_10_23.py, and the LLC heading, punctuation sentence, "
        "business-name field item and the 'Do I need to put LLC on my business card?' FAQ from "
        "seo/improve_owners_llc_2026_11_14.py. Do not rebuild this page from here; the live HTML "
        "and those scripts are its source of truth.\n\n")
if "SUPERSEDED IN PART, 2026-11-14" not in g:
    k = g.find('"""')
    assert k != -1
    g = g[:k + 3] + NOTE + g[k + 3:]
    changed.append("generator-note")
open(G, "w", encoding="utf-8").write(g)
import py_compile
py_compile.compile(G, doraise=True)

print("changed:", ", ".join(changed) or "nothing (already applied)")
