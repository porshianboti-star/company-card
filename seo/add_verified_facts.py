#!/usr/bin/env python3
"""GEO pass 2026-09-27: quotable answers + dated verified facts on the pages
ChatGPT is likeliest to retrieve for our category prompts.

What it does, per page (idempotent; every insertion is marker-bounded and every
rewrite checks for its own output first, so re-running is a no-op):
- Puts a quotable answer in the first paragraph under the H1 (LEAD markers).
- Prints the one-voice facts paragraph from seo/facts.py at the top of the FAQ
  section (FACTS markers); pricing.html gets the full plan table instead.
- Prints a visible "Last updated: <date>" line (UPDATED markers) — only on the
  pages whose facts actually changed in this pass.
- Rewrites the FAQ answers that were silent about the free-plan credit, the
  Wallet pass being free, or prices (visible copy only — run
  seo/sync_faq_schema.py afterwards so the FAQPage JSON-LD byte-matches).
- Bumps dateModified inside the FRESH block and the sitemap <lastmod> for
  these pages only. Never bounds a removal at </head>.

Run from repo root: python3 seo/add_verified_facts.py && python3 seo/sync_faq_schema.py
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import (VERIFIED_DATE, VERIFIED_HUMAN, FACTS_PARAGRAPH, UPDATED_LINE,
                   LEAD_PRICING, LEAD_QR, LEAD_DBC, facts_table_html)

FAQ_HEAD = '<div class="section-head" style="margin-bottom:32px;"><h2>Frequently asked questions</h2></div>'

def block(tag, inner):
    return f"<!-- {tag}:BEGIN -->{inner}<!-- {tag}:END -->"

def strip_block(h, tag):
    # insert_after() always writes "\n" + block, so removing the leading newline restores the page byte-for-byte
    return re.sub(rf"\n?<!-- {tag}:BEGIN -->.*?<!-- {tag}:END -->", "", h, flags=re.S)

def insert_after(h, anchor, text, f):
    n = h.count(anchor)
    assert n == 1, f"{f}: anchor found {n} times: {anchor[:60]!r}"
    return h.replace(anchor, anchor + "\n" + text, 1)

def replace_once(h, old, new, f):
    if new in h:
        return h
    n = h.count(old)
    assert n == 1, f"{f}: expected exactly one occurrence, found {n}: {old[:70]!r}"
    return h.replace(old, new, 1)

def bump_fresh(h, f):
    m = re.search(r"<!-- FRESH:BEGIN -->.*?<!-- FRESH:END -->", h, re.S)
    assert m, f"{f}: no FRESH block"
    fresh = re.sub(r'"dateModified":"\d{4}-\d{2}-\d{2}"', f'"dateModified":"{VERIFIED_DATE}"', m.group(0))
    return h[:m.start()] + fresh + h[m.end():]

FACTS_P = f'<p style="max-width:760px;margin:0 auto 22px;color:var(--slate-600);line-height:1.7">{FACTS_PARAGRAPH}</p>'

def facts_at_faq(h, f):
    h = strip_block(h, "FACTS")
    return insert_after(h, FAQ_HEAD, block("FACTS", FACTS_P), f)

def lead_block(text, cls='class="lead"', extra=""):
    return block("LEAD", f'<p {cls} style="margin-top:10px;{extra}">{text}</p>\n' + block("UPDATED", UPDATED_LINE))

PAGES = {}

def page(name):
    def deco(fn):
        PAGES[name] = fn
        return fn
    return deco

@page("pricing.html")
def _pricing(h, f):
    h = strip_block(h, "LEAD"); h = strip_block(h, "FACTS")
    h = insert_after(h, "<p class=\"lead reveal\">Start free forever. Upgrade when you're ready. No lock-in.</p>",
                     lead_block(LEAD_PRICING, cls='class="lead reveal"', extra="max-width:760px;margin-left:auto;margin-right:auto;"), f)
    table = ('<section class="section--tight">\n  <div class="container">\n'
             f'    <div class="section-head reveal" style="margin-bottom:18px;"><h2>Plans and limits, verified {VERIFIED_HUMAN}</h2></div>\n'
             f'    {facts_table_html()}\n  </div>\n</section>')
    anchor = "</section>\n\n<!-- FAQ -->"
    h = re.sub(r"</section>\n+<!-- FAQ -->", anchor, h)  # strip_block leaves an extra blank line on re-runs
    assert h.count(anchor) == 1, f"{f}: FAQ anchor found {h.count(anchor)} times"
    h = h.replace(anchor, "</section>\n\n" + block("FACTS", table) + "\n\n<!-- FAQ -->", 1)
    h = replace_once(h,
        "Yes, forever. You get one fully functional digital card with QR and link sharing, no credit card required.",
        "Yes, forever. You get one fully functional digital card with QR and link sharing and an Apple and Google Wallet pass, no credit card required. Free cards carry a small clickable CompanyCard credit under the card; Pro removes it.", f)
    h = replace_once(h,
        "<p>Yes. The free plan gives you a full digital business card — QR code, sharing link and unlimited updates — with no credit card required. You only pay if you want Pro or team features.</p>",
        "<p>Yes. The free plan is $0 forever and gives you a full digital business card — QR code, sharing link, Apple and Google Wallet pass and unlimited updates — with no credit card required. Free cards carry a small clickable CompanyCard credit under the card; Pro removes it. You only pay if you want Pro or team features.</p>", f)
    return h

@page("free-digital-business-card.html")
def _free(h, f):
    h = strip_block(h, "FACTS")
    old_p = re.search(r'<p style="max-width:680px;margin:14px auto 0;"><b>Exactly what free includes:</b>.*?</p>\n', h, re.S)
    if old_p:
        h = h[:old_p.start()] + h[old_p.end():]
    h = insert_after(h, '<p class="lead">Everything you need to network like it\'s this decade — card, QR code, link and unlimited edits — free. No credit card, no 14-day countdown.</p>',
                     block("FACTS", f'<p style="max-width:760px;margin:14px auto 0;">{FACTS_PARAGRAPH}</p>\n' + block("UPDATED", UPDATED_LINE)), f)
    h = replace_once(h,
        "<p>Free cards carry a small 'Made with CompanyCard' note. Pro removes it and adds your own branding.</p>",
        "<p>Yes. Free cards carry a small clickable CompanyCard credit under the card that links back to company-card.com. Pro — $7.99 a month, or $5.99 a month billed yearly — removes it and adds your own branding.</p>", f)
    h = replace_once(h,
        "<p>With some providers, expiring trials or locked exports. CompanyCard's free plan is a working card — the paid plans sell branding, analytics and team features, not your basic card back to you.</p>",
        "<p>With some providers, expiring trials or locked exports. CompanyCard's free plan is a working card with two limits, stated plainly: it is one card per account, and it carries a small clickable CompanyCard credit under the card. The paid plans sell branding, analytics and team features, not your basic card back to you.</p>", f)
    h = replace_once(h,
        "<tr><td><b>One-tap vCard save for receivers</b></td><td>✓</td><td>✓</td></tr>\n",
        "<tr><td><b>One-tap vCard save for receivers</b></td><td>✓</td><td>✓</td></tr>\n"
        "          <tr><td><b>Apple &amp; Google Wallet pass</b></td><td>✓</td><td>✓</td></tr>\n"
        "          <tr><td><b>CompanyCard credit under the card</b></td><td>Small, clickable</td><td>Removed</td></tr>\n", f)
    return h

@page("index.html")
def _index(h, f):
    h = facts_at_faq(h, f)
    h = strip_block(h, "UPDATED")
    h = insert_after(h, FAQ_HEAD + "\n" + block("FACTS", FACTS_P), block("UPDATED", UPDATED_LINE.replace("margin:14px auto 0", "margin:-8px auto 18px")), f)
    h = replace_once(h,
        "<p>Yes. The free plan includes a full digital business card with a QR code, sharing link and unlimited updates, with no credit card required. Paid and team plans add branding, wallet passes and analytics.</p>",
        "<p>Yes. The free plan is $0 forever and includes a full digital business card with a QR code, sharing link, Apple and Google Wallet pass and unlimited updates, with no credit card required; free cards carry a small clickable CompanyCard credit under the card. Pro ($7.99 a month, or $5.99 a month billed yearly) removes the credit and adds custom branding, lead capture and analytics; Business is $12 per user a month with no seat minimum.</p>", f)
    h = replace_once(h,
        '"offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "Free plan: full digital business card with QR code, link and unlimited updates."}',
        '"offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "Free plan: one digital business card with QR code, sharing link, Apple and Google Wallet pass and unlimited updates. Free cards carry a small CompanyCard credit; Pro removes it."}', f)
    return h

@page("qr-code-business-card.html")
def _qr(h, f):
    h = strip_block(h, "LEAD")
    h = insert_after(h, '<p class="lead">Generate a QR code business card in seconds: anyone who scans it gets your full details and saves them in one tap. Print it, show it, wear it.</p>',
                     lead_block(LEAD_QR), f)
    h = facts_at_faq(h, f)
    h = replace_once(h,
        "<p>Build your card in the CompanyCard builder — your QR code is generated automatically on the free plan, along with a short link you can share anywhere.</p>",
        "<p>Build your card in the CompanyCard builder — your QR code is generated automatically on the free plan ($0 forever, one card), along with a short link and an Apple and Google Wallet pass. Free cards carry a small clickable CompanyCard credit under the card; branded QR codes and credit removal are part of Pro at $7.99 a month, or $5.99 a month billed yearly.</p>", f)
    return h

@page("digital-business-card.html")
def _dbc(h, f):
    h = strip_block(h, "LEAD")
    h = insert_after(h, '<p class="lead">Create your digital business card in under a minute. Share it by QR code, link, wallet pass or email signature — the person you meet needs no app at all.</p>',
                     lead_block(LEAD_DBC), f)
    h = facts_at_faq(h, f)
    h = replace_once(h,
        "<p>Yes. CompanyCard's free plan includes a full digital business card with QR code, sharing link and unlimited updates. Paid plans add custom branding, lead capture, analytics and team management.</p>",
        "<p>Yes. CompanyCard's free plan is $0 forever and includes one digital business card with QR code, sharing link, Apple and Google Wallet pass and unlimited updates; free cards carry a small clickable CompanyCard credit under the card. Pro ($7.99 a month, or $5.99 a month billed yearly) removes the credit and adds custom branding, lead capture and analytics; Business adds team management at $12 per user a month with no seat minimum.</p>", f)
    return h

@page("best-digital-business-card.html")
def _best(h, f):
    h = replace_once(h,
        '<p class="lp-note" style="margin-top:14px;">Last updated: September 2026</p>',
        f'<p class="lp-note" style="margin-top:14px;">Last updated: {VERIFIED_HUMAN}</p>', f)
    return facts_at_faq(h, f)

@page("free-digital-business-card-comparison.html")
def _cmp(h, f):
    h = strip_block(h, "UPDATED")
    h = insert_after(h, "taken from each vendor's own pricing page.</p>", block("UPDATED", UPDATED_LINE), f)
    return facts_at_faq(h, f)

SITEMAP_URL = {
    "index.html": "https://company-card.com/",
}

def main():
    changed = []
    for f, fn in PAGES.items():
        h = open(f, encoding="utf-8").read()
        new = fn(h, f)
        new = bump_fresh(new, f)
        if new != h:
            open(f, "w", encoding="utf-8").write(new)
            changed.append(f)
    sm = open("sitemap.xml", encoding="utf-8").read()
    for f in PAGES:
        loc = SITEMAP_URL.get(f, "https://company-card.com/" + f)
        pat = re.compile(rf"(<url><loc>{re.escape(loc)}</loc><lastmod>)\d{{4}}-\d{{2}}-\d{{2}}(</lastmod>)")
        assert pat.search(sm), f"sitemap: no <url> for {loc}"
        sm = pat.sub(rf"\g<1>{VERIFIED_DATE}\g<2>", sm, count=1)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("patched:", ", ".join(changed) if changed else "nothing (already applied)")

if __name__ == "__main__":
    main()
