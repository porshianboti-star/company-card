#!/usr/bin/env python3
"""CompanyCard page generator — builds SMB/self-employed + profession landing
pages that are byte-faithful to the existing site template (header/footer/style
are lifted verbatim from the live pages into seo/_tpl_*.txt).

Run from the repo root:  python3 seo/build_pages.py

Every page gets: unique title/meta/canonical, OG+Twitter, single H1, visible
FAQ (details/summary) whose text MATCHES the FAQPage JSON-LD verbatim (Google
policy), BreadcrumbList, and — where the page describes a process — HowTo.
Honesty rules: no invented ratings, review counts, customer counts or awards.
"""
import os, json, html, re

BASE = "https://company-card.com/"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
APP = "app/builder.html"

HEADER = open(os.path.join(HERE, "_tpl_header.txt"), encoding="utf-8").read()
FOOTER = open(os.path.join(HERE, "_tpl_footer.txt"), encoding="utf-8").read()
STYLE = open(os.path.join(HERE, "_tpl_style.txt"), encoding="utf-8").read()

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
 '&family=Poppins:wght@500;600;700;800&family=Marcellus&display=swap" rel="stylesheet">\n'
 '<link rel="stylesheet" href="assets/styles.css">')


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&middot;", "·").strip()


# ---------- section builders ----------

def cards3(items):
    """3-up feature cards — items: [(title, body_html), ...]"""
    cells = "".join(
        f'<div class="card"><h3>{esc(t)}</h3><p>{d}</p></div>' for t, d in items)
    return f'<div class="grid-3">{cells}</div>'


def table(headers, rows, note=None):
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    n = f'<p class="lp-note">{note}</p>' if note else ""
    return (f'<div class="lp-table"><table><thead><tr>{th}</tr></thead>'
            f'<tbody>{tb}</tbody></table></div>{n}')


TICK = ('<span class="tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M20 6 9 17l-5-5"/></svg></span>')


def checklist(items):
    """items: [(bold_lead, rest_html), ...] — uses the site's global .checklist CSS"""
    lis = "".join(
        f'<li>{TICK}<span><b>{esc(b)}</b> {r}</span></li>' for b, r in items)
    return ('<ul class="checklist" style="max-width:640px;margin:0 auto;">'
            + lis + '</ul>')


def prose(h2, paras):
    body = "".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in paras)
    return (f'<section class="section"><div class="container lp-prose">'
            f'<div class="section-head" style="margin-bottom:24px;"><h2>{esc(h2)}</h2></div>'
            f'{body}</div></section>')


def block(h2, inner, tint=False, tight=False):
    bg = ' style="background:var(--slate-50);"' if tint else ""
    head = (f'<div class="section-head" style="margin-bottom:32px;"><h2>{esc(h2)}</h2></div>'
            if h2 else "")
    return f'<section class="section"{bg}><div class="container">{head}{inner}</div></section>'


def steps_howto(items):
    """Ordered steps rendered as prose list (mirrors HowTo schema)."""
    lis = "".join(f"<li>{s}</li>" for s in items)
    return f'<div class="container lp-prose"><ol>{lis}</ol></div>'


def faq_html(faqs):
    items = "".join(
        f'<details class="lp-faq"><summary>{esc(q)}</summary><p>{a}</p></details>'
        for q, a in faqs)
    return ('<section class="section"><div class="container">'
            '<div class="section-head" style="margin-bottom:32px;">'
            '<h2>Frequently asked questions</h2></div>' + items + '</div></section>')


def cta(h2, p, related):
    rel = " &middot; ".join(f'<a href="{u}">{esc(t)}</a>' for t, u in related)
    return ('<section class="section"><div class="container"><div class="cta-band">'
            f'<h2>{esc(h2)}</h2><p>{esc(p)}</p>'
            '<div class="hero-actions" style="justify-content:center;margin-top:28px;">'
            f'<a href="{APP}" class="btn btn-primary btn-lg shine">Create your free card</a>'
            '</div></div>'
            f'<p class="lp-related" style="margin-top:28px;">Related: {rel}</p>'
            '</div></section>')


# ---------- schema ----------

def schema_blocks(p):
    out = []
    faqs = p.get("faqs") or []
    if faqs:
        out.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                           for q, a in faqs]})
    out.append({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": p["crumb"],
             "item": BASE + p["slug"]}]})
    if p.get("howto"):
        out.append({
            "@context": "https://schema.org", "@type": "HowTo",
            "name": p["howto_name"],
            "step": [{"@type": "HowToStep", "position": i + 1, "name": strip_tags(s)}
                     for i, s in enumerate(p["howto"])]})
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False, separators=(",", ":"))}</script>'
        for b in out)


# ---------- render ----------

def render(p):
    canonical = BASE + p["slug"]
    head = (
      '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
      '<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
      f'<title>{esc(p["title"])}</title>\n'
      f'<meta name="description" content="{esc(p["meta"])}">\n'
      f'<link rel="canonical" href="{canonical}">\n'
      '<meta name="robots" content="index,follow,max-image-preview:large">\n'
      f'<meta property="og:title" content="{esc(p["title"])}">\n'
      f'<meta property="og:description" content="{esc(p.get("og", p["meta"]))}">\n'
      '<meta property="og:type" content="website">\n'
      f'<meta property="og:url" content="{canonical}">\n'
      '<meta property="og:site_name" content="CompanyCard">\n'
      '<meta property="og:image" content="https://company-card.com/assets/png/favicon-512.png">\n'
      '<meta name="twitter:card" content="summary">\n'
      f'<meta name="twitter:title" content="{esc(p["title"])}">\n'
      f'<meta name="twitter:description" content="{esc(p.get("og", p["meta"]))}">\n'
      '<link rel="icon" href="assets/logo-icon.svg" type="image/svg+xml">\n'
      + FONTS + '\n<style>\n' + STYLE + '</style>\n'
      + schema_blocks(p) + '\n</head>\n<body>\n\n')

    hero = ('<section class="page-hero">\n<div class="container">\n'
            f'<h1 style="max-width:840px;margin:0 auto;">{p["h1"]}</h1>\n'
            f'<p class="lead">{p["lead"]}</p>\n'
            '<div class="hero-actions" style="justify-content:center;margin-top:28px;">\n'
            f'<a href="{APP}" class="btn btn-primary btn-lg shine">{esc(p["cta_btn"])}</a>\n'
            f'<a href="{p["cta2"][1]}" class="btn btn-ghost btn-lg">{esc(p["cta2"][0])}</a>\n'
            '</div>\n</div>\n</section>\n\n')

    body = "\n".join(p["sections"])
    tail = (faq_html(p["faqs"]) + "\n" + cta(p["cta_h"], p["cta_p"], p["related"]) + "\n")
    return (head + HEADER + "\n\n" + hero + body + "\n" + tail + FOOTER +
            '\n\n<script>document.getElementById("year").textContent = new Date().getFullYear();</script>\n'
            '<script src="assets/analytics.js"></script>\n</body>\n</html>\n')


def write_pages(pages):
    written = []
    for p in pages:
        fn = os.path.join(ROOT, p["slug"])
        with open(fn, "w", encoding="utf-8") as f:
            f.write(render(p))
        written.append(p["slug"])
    return written


if __name__ == "__main__":
    from pages_data import PAGES
    w = write_pages(PAGES)
    print(f"Wrote {len(w)} pages:")
    for s in w:
        print("  " + s)
