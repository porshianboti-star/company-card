# -*- coding: utf-8 -*-
"""Batch 23: embed-digital-business-card-on-your-website.html — the how-to for
the app's "Add to your website" panel (dashboard.html / builder.html share
modals, 2026-09-27).

WHY THIS PAGE. The product had no way for a customer to put a link to
company-card.com on their own site: the share UI stopped at QR + copy-link
(dashboard.html, builder.html) and SMS/email/WhatsApp (mobile.html). Every
on-site lever is exhausted (memory: prosignature-seo-ceiling; the 2026-09-01
pre-registered on-page test failed) and the one growth channel that owes
nothing to domain authority is a customer's own website. The panel produces
two snippets from the card's lite share link; this page documents them, shows
the badge on a light and a dark background, and says where an "HTML / embed
block" lives without describing any vendor's UI beyond that.

HONESTY (revised 2026-09-27, same day). Signed in, a card is pushed to
Supabase on every save and served at the stable /c/<slug> page (Netlify
rewrite to app/c.html), so the link survives edits. Not signed in, the card's
details are encoded INSIDE the share link (card.html#c=<encoded card>) with no
server lookup, so an edited card has a new link and the snippet must be
copied again. The page states both cases (prose + FAQ) rather than claiming
"update once, everywhere" for everyone. The free plan is one card; the card page carries a "Make your own
CompanyCard" link (app/card.html .made) and the embed adds a "Made with
CompanyCard" line — both named as the credits that keep the free plan free.
No conversion rates, customer counts or vendor UI claims. Badge size is the
measured file size (1,672 bytes on 2026-09-27) stated as "under 2 KB".
"""
import html as _h
from build_pages import prose, block, checklist  # noqa: F401

SLUG = "embed-digital-business-card-on-your-website.html"
BADGE = "https://company-card.com/assets/badge-save-contact.svg"
CREDIT = "https://company-card.com/?utm_source=embed&utm_medium=web&utm_campaign=card_embed"

# The exact strings CC.embedSnippets() produces, with the two per-card values
# (share link, name) shown as placeholders / the app's own sample name.
BADGE_CODE = ('<a href="YOUR_SHARE_LINK" rel="noopener" title="Jordan Diaz — digital business card">'
              '<img src="' + BADGE + '" alt="Save my contact — digital business card by CompanyCard" '
              'width="220" height="52" style="border:0"></a>')
IFRAME_CODE = ('<iframe src="YOUR_SHARE_LINK" width="360" height="600" loading="lazy" '
               'title="Jordan Diaz — digital business card" '
               'style="border:0;border-radius:16px;max-width:100%"></iframe>\n'
               '<p style="font:13px system-ui;margin:6px 0 0"><a href="' + CREDIT + '" rel="noopener">'
               'Made with CompanyCard</a></p>')


def code(s):
    return '<pre class="lp-code"><code>' + _h.escape(s, quote=False) + '</code></pre>'


CSS = ('<style>'
       '.lp-code{max-width:760px;margin:0 auto 18px;background:var(--ink);color:#E2E8F0;border-radius:14px;'
       'padding:18px 20px;overflow-x:auto;font:.86rem/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;'
       'white-space:pre-wrap;word-break:break-word}'
       '.lp-code code{font:inherit;color:inherit;background:none;padding:0}'
       '.lp-demo{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;max-width:760px;margin:0 auto 22px}'
       '.lp-demo span{display:inline-flex;padding:18px 22px;border-radius:14px}'
       '.lp-demo .on-light{background:#fff;border:1px solid var(--slate-200)}'
       '.lp-demo .on-dark{background:var(--ink)}'
       '.lp-steps{max-width:760px;margin:0 auto;padding-left:24px}'
       '.lp-steps li{font-size:1.04rem;line-height:1.7;color:var(--slate-700);margin-bottom:12px}'
       '</style>')

STEPS = [
    'Create your card in the free builder if you have not already — name, title, phone, email, links.',
    'Open <b>My cards</b>, press <b>Share</b> on the card, then <b>Add to your website</b>.',
    'Press <b>Copy</b> next to the button snippet, or next to the card embed if you want the whole card on the page. Your share link is already filled in.',
    'In your website editor, add an HTML or embed block where the button should sit, paste the snippet and publish.',
    'Open the published page on your phone once and tap the button: your card should open and <b>Save contact</b> should offer the .vcf file.',
]

REL = [
    ("How to make a digital business card", "how-to-make-a-digital-business-card.html"),
    ("QR code business card", "qr-code-business-card.html"),
    ("Email signature generator", "email-signature-generator.html"),
    ("Free digital business card", "free-digital-business-card.html"),
]

PAGE = {
 "slug": SLUG,
 "crumb": "Add Your Card to Your Website",
 "title": "How to Add a Digital Business Card to Your Website | CompanyCard",
 "meta": ("Put a Save-my-contact button or your whole digital business card on your website with "
          "two copy-paste snippets. Any HTML or embed block, free plan included."),
 "og": ("Two copy-paste snippets from the CompanyCard app: a Save-my-contact button, or your card "
        "embedded on the page. Any site with an HTML block, free plan included."),
 "h1": 'How to add a digital business card to <span class="gradient-text">your website</span>',
 "lead": ("A contact page that lists a phone number asks the visitor to do the work. A "
          "Save-my-contact button does it for them: one tap opens your card, a second saves you "
          "to their phone. Here is how to put it on any site, in two copy-paste snippets."),
 "cta_btn": "Create your free card",
 "cta2": ("How to make a card first", "how-to-make-a-digital-business-card.html"),
 "cta_h": "Your card, on every page you own",
 "cta_p": ("Create a free card, open Share, press Add to your website and paste the snippet. "
           "The credit line under it is what keeps the free plan free."),
 "related": REL,
 "howto_name": "How to add a digital business card to your website",
 "howto": STEPS,
 "faqs": [
   ("Does the Save-my-contact button work on the free plan?",
    "Yes. The free plan includes one digital business card with a QR code and a share link, and "
    "both snippets are built from that link, so nothing on this page needs a paid plan. A card's "
    "page carries a small Make your own CompanyCard link under the card, and the embed snippet "
    "adds a Made with CompanyCard line under the frame. Those two credits are what keep the free "
    "plan free."),
   ("Do my visitors need an app or an account?",
    "No. The button opens your card as an ordinary web page in whatever browser the visitor is "
    "using. Tapping Save contact downloads a standard .vcf contact file, which iPhones and Android "
    "phones open straight into Contacts. Only you, the card's owner, have a CompanyCard account."),
   ("What happens to the button when I change my card?",
    "It depends on whether you were signed in when you copied it. Signed in: your link stays the "
    "same when you edit the card, because the card is saved to your account and the link points "
    "at its page on company-card.com, so nothing on your website needs touching. Not signed in: "
    "the link encodes the card itself, so re-copy it after edits by opening Share, then Add to "
    "your website again, and pasting the fresh snippet over the old one. The panel tells you "
    "which kind of link you have."),
   ("Will the embed slow my website down?",
    "The button is a single SVG image of under 2 KB plus a link, with no script to load. The card "
    "embed is an iframe with lazy loading, so the browser fetches the card page only when a "
    "visitor scrolls near it, and its max-width rule lets it shrink to fit a phone screen."),
 ],
}

PAGE["sections"] = [
  prose("Why your website should carry your card", [
    "A contact page usually offers a phone number, an email address and a form. All three ask the "
    "visitor to do the work: copy the number, type the address, wait for a reply. A Save-my-contact "
    "button turns that around. One tap opens your digital business card in the visitor's browser and "
    "a second tap saves your name, number, email, company and links into their phone — the same "
    "<code>.vcf</code> contact file a phone produces when you share someone from your address book. "
    "No app to install, nothing to type.",

    "That matters because a saved contact is the outcome a business card exists for. Someone who has "
    "you in their phone recognises your call, finds your email without searching and has your "
    "website one tap away. A visitor who merely read your contact page has none of that once the "
    "tab is closed.",

    "CompanyCard gives you two ways to do it, both built in the app from the same share link that "
    "sits behind your QR code: a button that links to your card, or the card itself embedded on the "
    "page. Open <b>My cards</b>, press <b>Share</b>, then <b>Add to your website</b>. Both snippets "
    "appear with your link already filled in, each with its own Copy button.",
  ]),

  block("Two snippets, both free", CSS +
    '<div class="lp-prose"><h3>1. The Save-my-contact button</h3>'
    '<p>A single image wrapped in a link to your card. It has its own rounded background, so it '
    'reads the same on a white page and a dark footer:</p></div>'
    '<div class="lp-demo">'
    '<span class="on-light"><img src="assets/badge-save-contact.svg" alt="The Save my contact button on a light background" width="220" height="52" loading="lazy"></span>'
    '<span class="on-dark"><img src="assets/badge-save-contact.svg" alt="The Save my contact button on a dark background" width="220" height="52" loading="lazy"></span>'
    '</div>'
    + code(BADGE_CODE) +
    '<div class="lp-prose"><p>The app replaces <code>YOUR_SHARE_LINK</code> with your card\'s link and '
    '<code>Jordan Diaz</code> with your name. Nothing else changes, and there is no script or '
    'stylesheet to add.</p>'
    '<h3>2. Your whole card on the page</h3>'
    '<p>If you would rather show the card itself — photo, links and the Save contact button — '
    'embed the card page in a frame. It is 360 by 600 pixels, shrinks to fit a phone screen and '
    'loads only when a visitor scrolls to it:</p></div>'
    + code(IFRAME_CODE) +
    '<div class="lp-prose"><p>The line under the frame, <em>Made with CompanyCard</em>, is a small credit '
    'that links back to us. That credit is what keeps the free plan free, so please leave it in place.</p></div>'),

  block("Where to paste it", checklist([
    ("Wix, Squarespace, Webflow, Shopify.",
     "Each has an HTML or embed-code block. Add one where the button should appear, paste the "
     "snippet into it and publish the page."),
    ("WordPress.",
     "Add an HTML block in the page editor, or paste the snippet into a text widget in the footer "
     "or sidebar so the button shows on every page."),
    ("A hand-coded site.",
     "Paste it into the page's HTML wherever the button belongs. It is plain HTML, so it needs no "
     "script tag and nothing to load first."),
    ("Anywhere else a link works.",
     "Linktree-style bio pages, Notion pages, forum signatures and your "
     '<a href="email-signature-generator.html">email signature</a>: use the button image where '
     "images are allowed and the plain share link where they are not."),
  ]), tint=True),

  block("Step by step",
    '<ol class="lp-steps">' + "".join("<li>" + s + "</li>" for s in STEPS) + "</ol>"),

  prose("One thing to know before you paste", [
    "<b>Signed in:</b> your link stays the same when you edit the card. Every save goes to your "
    "account and the link points at your card's own page on company-card.com, so the button on your "
    "website, your bio and your email signature all show the current card without being touched.",

    "<b>Not signed in:</b> the link encodes the card itself — that is why it opens with nothing "
    "installed on the visitor's side and nothing added to your site — so re-copy it after edits. "
    "Open <b>Share</b> → <b>Add to your website</b> again and paste the new snippet over the old one; "
    "the old button keeps working in the meantime and simply shows the card as it was. The panel "
    "says which kind of link you are holding, and signing in before you copy is the way to get the "
    "stable one.",
  ]),
]

PAGES = [PAGE]
