#!/usr/bin/env python3
"""Add a three-card example gallery under the hero of every landing page that
shows no CompanyCard card yet (owner request 2026-09-29: every such page should
show at least one real card, ideally three side by side).

Images are the existing product screenshots in assets/examples/ (demo people,
real CompanyCard renderer). The copy says they are examples — no page claims
they are customers.

Marker-bounded (<!-- CARDS:BEGIN --> ... <!-- CARDS:END -->), idempotent, and
inserted right after the page-hero </section> — never bounded at </head>.
build_pages.write_pages calls apply() so a rebuilt page keeps its gallery.

Run from repo root: python3 seo/add_card_gallery.py
"""
import os, re, zlib

MARK, END = "<!-- CARDS:BEGIN -->", "<!-- CARDS:END -->"
HERO_END = re.compile(r'(<section class="page-hero">.*?</section>\n?)', re.S)

# (file stem, height at 840 wide, alt detail, caption)
CARDS = {
    "sofia": ("virtual-business-card-example", 1474,
              "Sofia Costa, Customer Success — WhatsApp, phone and website",
              "WhatsApp, phone, website"),
    "rachel": ("digital-business-card-example-real-estate", 1606,
               "Rachel Kim, VP Sales at Northwind Luxury Real Estate",
               "Book-a-viewing link"),
    "diego": ("digital-business-card-example-account-executive", 1438,
              "Diego Martín, Account Executive — phone, email and LinkedIn",
              "Phone, email, LinkedIn"),
    "amara": ("digital-business-card-example-partnerships", 1540,
              "Amara Okafor, Partnerships Lead — with a book-a-call button",
              "Book-a-call link"),
    "tom": ("digital-business-card-example-team-marketing", 1446,
            "Tom Walsh, Marketing Manager — social links and website",
            "Social links and website"),
    "qr": ("qr-code-business-card-example", 1624,
           "digital business card with a built-in QR code to scan and save the contact",
           "Built-in QR code to scan"),
}
TRIOS = [("amara", "sofia", "diego"), ("rachel", "amara", "tom"),
         ("sofia", "diego", "rachel"), ("tom", "amara", "sofia"),
         ("diego", "rachel", "amara")]
QR_PAGES = ("qr", "vcard", "event", "nfc", "paper", "apple-wallet", "how-to-make",
            "free-digital-business-card.html")

# Landing pages only; utility, legal and tool pages are left alone.
SKIP = {"about.html", "contact.html", "contact-thanks.html", "privacy-policy.html",
        "pricing.html", "features.html", "business.html", "email-signature-generator.html",
        "virtual-background-for-video-calls.html", "open-vcf-file.html", "index.html"}

STYLE = ('<style>.cc-ex-grid{display:grid;grid-template-columns:repeat(3,minmax(0,250px));'
         'gap:26px;justify-content:center;margin-top:8px}.cc-ex-grid figure{margin:0}'
         '.cc-ex-grid img{width:100%;height:auto;border-radius:20px;border:1px solid '
         'var(--slate-200,#e5e7eb);box-shadow:0 12px 30px rgba(15,23,42,.12);background:#fff;'
         'display:block}.cc-ex-grid figcaption{margin-top:10px;font-size:13.5px;color:'
         'var(--slate-500,#64748b);text-align:center}@media(max-width:640px){.cc-ex-grid{'
         'grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}.cc-ex-grid img{'
         'border-radius:12px}.cc-ex-grid figcaption{font-size:11.5px}}</style>')


def trio(slug):
    t = list(TRIOS[zlib.crc32(slug.encode()) % len(TRIOS)])
    if any(k in slug for k in QR_PAGES):
        t[1] = "qr"
        # the QR screenshot is Rachel's card — never show her twice
        t = ["amara" if k == "rachel" else k for k in t]
    return t


def gallery(slug):
    figs = []
    for key in trio(slug):
        stem, h, detail, cap = CARDS[key]
        figs.append(
            "<figure><picture><source srcset='/assets/examples/%s.webp' type='image/webp'>"
            "<img src='/assets/examples/%s.png' alt=\"CompanyCard digital business card "
            "example — %s\" width='840' height='%d' loading='lazy' decoding='async'>"
            "</picture><figcaption>%s</figcaption></figure>" % (stem, stem, detail, h, cap))
    return (MARK + '\n<section class="section" style="padding-top:8px;padding-bottom:24px;">\n<div class="container">\n'
            '<div class="section-head"><h2>What a CompanyCard looks like</h2>'
            '<p style="max-width:640px;margin:10px auto 0;color:var(--slate-500,#64748b)">'
            'Three example cards made with CompanyCard (the people and companies are demo '
            'examples). Each one opens from a link or QR code, and the reader saves the contact '
            'with one tap — no app needed.</p></div>\n' + STYLE + '\n<div class="cc-ex-grid">'
            + "".join(figs) + '</div>\n</div>\n</section>\n' + END + '\n')


def apply(h, slug):
    """Return h with the gallery inserted/refreshed, or unchanged if not eligible."""
    if slug in SKIP:
        return h
    if MARK in h:
        return re.sub(re.escape(MARK) + r".*?" + re.escape(END) + r"\n?",
                      lambda m: gallery(slug), h, count=1, flags=re.S)
    if "assets/examples/" in h:
        return h  # page already shows example cards
    m = HERO_END.search(h)
    if not m:
        return h
    return h[:m.end()] + "\n" + gallery(slug) + h[m.end():]


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    n = 0
    for fn in sorted(f for f in os.listdir(".") if f.endswith(".html")):
        h = open(fn, encoding="utf-8").read()
        new = apply(h, fn)
        if new != h:
            open(fn, "w", encoding="utf-8").write(new)
            n += 1
            print("gallery: " + fn + " " + ",".join(trio(fn)))
    print("%d pages changed" % n)
