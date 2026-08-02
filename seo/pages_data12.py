# -*- coding: utf-8 -*-
"""Batch 12: vcard-qr-code.html — the payload/encoding-mechanics page.

POSITIONING (anti-cannibalisation). Two live pages already touch this topic and
neither is being rewritten:
  * qr-code-business-card.html — the PRODUCT/generator page. It already owns the
    H2 "vCard QR vs. dynamic QR: which should you use?" (a FEATURE comparison)
    and the FAQ "What is the difference between a vCard QR code and a dynamic QR
    code?".
  * electronic-business-card.html — the definitional "built on the vCard
    standard" page.
This page is deliberately the TECHNICAL one: what is literally encoded in the
.vcf payload, which properties the spec requires, and why adding fields raises
the QR version and therefore the physical print size needed to scan it. Its
table is about ENCODING MECHANICS, not features, so it does not restate the
existing comparison.

FACT PROVENANCE — every technical assertion below was fetched from a primary
source on 2026-08-02 and nothing outside this list is asserted:
  * RFC 6350 (rfc-editor.org) — vCard 4.0; obsoletes RFC 2425, RFC 2426 and
    RFC 4770; updates RFC 2739. "A vCard object MUST include the VERSION and FN
    properties. VERSION MUST come immediately after BEGIN:VCARD."
  * RFC 2426 (rfc-editor.org) — "vCard MIME Directory Profile", vCard 3.0;
    VERSION value MUST be "3.0" for cards conforming to it.
  * qrcode.com/en/about/version.html (Denso Wave) — version 1 = 21x21 modules,
    version 40 = 177x177, "each higher version number comprises 4 additional
    modules per side".
  * qrcode.com/en/about/error_correction.html (Denso Wave) — levels L, M, Q, H;
    M restores ~15%, Q ~25%; raising the level adds Reed-Solomon data and
    "increases the amount of data QR Code size" must carry.

DELIBERATELY NOT STATED (could not be verified today, so absent from the page):
  * any minimum printed QR size in mm or inches, and any scan-distance ratio;
  * the maximum byte capacity of a version 40 code (Denso Wave's capacity table
    did not load);
  * the L and H error-correction percentages (only M and Q were given);
  * what any specific phone or scanner app does with a scanned vCard, which
    varies by scanner — the page says so instead of asserting OS behaviour;
  * anything about a named competitor.

The workflow that was to draft this hit the session agent limit, so the copy was
written and fact-checked directly against the sources above.
"""
from build_pages import prose, block, checklist, table

FREE_SPEC = ("one digital business card, a QR code and sharing link, your profile, links and "
             "socials, an Apple and Google Wallet pass, and unlimited edits — free forever, no "
             "credit card. Free cards carry a small CompanyCard credit; removing it is part of Pro.")

RFC6350 = ('<a href="https://www.rfc-editor.org/rfc/rfc6350" target="_blank" rel="noopener nofollow">RFC&nbsp;6350</a>')
RFC2426 = ('<a href="https://www.rfc-editor.org/rfc/rfc2426" target="_blank" rel="noopener nofollow">RFC&nbsp;2426</a>')

VCARD_QR = {
 "slug": "vcard-qr-code.html",
 "crumb": "vCard QR Code",
 "title": "vCard QR Code: What's Encoded Inside | CompanyCard",
 "meta": ("What a vCard QR code actually encodes: the .vcf payload, why extra fields make the "
          "code denser and harder to scan, and when a link works better."),
 "og": ("What a vCard QR code actually encodes: the .vcf payload, why extra fields make the "
        "code denser and harder to scan, and when a link works better."),
 "h1": 'What is actually inside a <span class="gradient-text">vCard QR code</span>',
 "lead": ("A vCard QR code carries your contact details inside the code itself, rather than a link "
          "to them. That single design choice explains what it is good at and the two ways it goes "
          "wrong."),
 "cta_btn": "Create your free card",
 "cta2": ("Make a QR code business card", "qr-code-business-card.html"),
 "cta_h": "A code that survives a change of number",
 "cta_p": "Free forever, no credit card, and the link behind your QR never changes.",

 "howto_name": "How to make a vCard QR code that still scans",
 "howto": [
   "Decide first whether the details are final. If any of them could change, encode a link to a card you can edit rather than the contact record itself.",
   "Keep the payload short. Every optional property you add lengthens the encoded text, and length is what forces the code up a version.",
   "Leave error correction at a middling level unless the code will be printed somewhere it gets scuffed. Raising it adds recovery data and pushes the module count up again.",
   "Test the code at the size and distance you will actually use, printed rather than on screen, before you commit to a print run.",
 ],

 "sections": [
  prose("What a vCard QR code actually is", [
    "A vCard is the standard file format for a contact record — the <code>.vcf</code> file your phone "
    "produces when you share someone from your address book. Version 4.0 is defined in " + RFC6350 +
    ", which replaced the earlier vCard 3.0 specification in " + RFC2426 + ". Both versions are still "
    "in circulation, which is why every card carries a <code>VERSION</code> line saying which one it "
    "follows.",

    "A vCard QR code is that file encoded directly into the squares. Nothing is fetched and no server "
    "is involved: the whole contact record is physically present in the printed code. Scan it offline, "
    "in a basement, in a country with no signal, and the details are still there.",

    "The specification asks for remarkably little. " + RFC6350 + " requires only <code>BEGIN:VCARD</code>, "
    "a <code>VERSION</code> property immediately after it, an <code>FN</code> property holding the "
    "formatted name, and <code>END:VCARD</code>. Your phone number, email, employer and website are all "
    "optional additions — and each one makes the payload longer.",
  ]),

  block("The anatomy of the payload", checklist([
    ("BEGIN:VCARD and END:VCARD",
     "the wrapper. Every vCard opens and closes with these two lines."),
    ("VERSION",
     "required, and " + RFC6350 + " specifies that it must come immediately after "
     "<code>BEGIN:VCARD</code>. It declares which specification the card follows — <code>3.0</code> for "
     + RFC2426 + ", <code>4.0</code> for " + RFC6350 + "."),
    ("FN",
     "the formatted name, as you would want it displayed. Under vCard 4.0 this is the only content "
     "property the specification makes mandatory."),
    ("TEL, EMAIL, ORG, TITLE, URL",
     "the optional properties that carry your number, address, company, role and website. These are "
     "what people actually want from your card, and they are also what makes the payload grow."),
    ("Everything you add",
     "costs characters. There is no compression step that rescues you: a longer contact record is a "
     "longer string, and a longer string needs a bigger code."),
  ]), tint=True),

  block("Why a detailed vCard becomes a code that will not scan",
    table(
      ["What you change", "What happens inside the code", "What you notice"],
      [
        ["You add more properties",
         "More characters to encode, so the code has to move up a version to fit them",
         "The grid becomes finer at the same printed width"],
        ["The version goes up",
         "Version 1 is 21&times;21 modules and every higher version adds 4 more modules per side, "
         "up to 177&times;177 at version 40",
         "Each square shrinks unless you print the code larger"],
        ["You raise the error correction level",
         "Reed-Solomon recovery data is added on top of your payload, so there is more to store — "
         "level M restores about 15% of the code, level Q about 25%",
         "The same trade again: more modules, or a bigger print"],
        ["Your phone number changes",
         "Nothing at all. The old details are already encoded in every code you printed",
         "Every card you have handed out is now quietly wrong"],
      ],
      note=('Sources, verified August 2026: vCard requirements from ' + RFC6350 + ' and ' + RFC2426 +
            '; QR version, module and error-correction behaviour from '
            '<a href="https://www.qrcode.com/en/about/version.html" target="_blank" rel="noopener nofollow">Denso Wave</a>, '
            'the originator of the QR code.')
    )),

  prose("The failure that has nothing to do with scanning", [
    "The first three rows of that table are a printing problem, and printing problems have printing "
    "solutions: shorten the record, print it bigger, test before you order. The fourth row does not.",

    "A static vCard QR code is a photograph of your details on the day you made it. Change your number, "
    "your email, your company or your role, and every code already in the world keeps handing out the "
    "old ones. The code still scans perfectly. It is simply wrong, and there is no way to tell from "
    "looking at it — not for you, and not for the person who scanned it last month and saved a number "
    "that no longer rings.",

    "If your details are genuinely fixed, none of this matters and a static vCard QR code is a clean, "
    "offline-proof way to hand them over. If they are not fixed — and for most self-employed people "
    "and small businesses they are not — the fix is to encode a short link to a card you control, so "
    "the code stays the same and the details behind it move.",

    "That is what a "
    '<a href="qr-code-business-card.html">CompanyCard QR code</a> does. The code and link are permanent, '
    "the details behind them are editable, and what the person scanning gets is a card with a save "
    "button rather than a raw contact file. The free plan covers this: " + FREE_SPEC,
  ]),
 ],

 "faqs": [
  ("What is a vCard QR code?",
   "It is a QR code with a contact record encoded directly inside it, in the vCard format — the same "
   "<code>.vcf</code> format your phone uses when you share a contact. Because the details are in the "
   "code itself rather than behind a link, it works with no internet connection."),

  ("What does a vCard QR code contain?",
   "At minimum, the four things the specification requires: <code>BEGIN:VCARD</code>, a "
   "<code>VERSION</code> line, an <code>FN</code> property with your formatted name, and "
   "<code>END:VCARD</code>. Everything else — telephone, email, organisation, job title, website — is "
   "optional, and each addition makes the encoded payload longer."),

  ("Should I use vCard 3.0 or 4.0?",
   "vCard 4.0 is the current specification, defined in RFC 6350, which replaced the 3.0 specification "
   "in RFC 2426. Both are still in use, and the <code>VERSION</code> property in every card declares "
   "which one it follows, so check what your generator writes if compatibility with an older system "
   "matters to you."),

  ("Why will my vCard QR code not scan?",
   "Usually because there is too much in it for the size you printed. More encoded characters push the "
   "code up to a higher version, and a version 40 code packs 177 modules across the same width where a "
   "version 1 code packs 21. Remove optional fields, or print the code larger, then test it at the "
   "distance people will actually scan from."),

  ("Can I change the details in a vCard QR code after printing it?",
   "No. In a static vCard QR code the details are encoded in the pattern itself, so changing them means "
   "generating a new code and reprinting everything that carried the old one. To keep one code and edit "
   "the details behind it, encode a link to a card you control instead."),

  ("Is it free to make one?",
   "Yes. The CompanyCard free plan includes " + FREE_SPEC),
 ],

 "related": [
   ("QR code business card", "qr-code-business-card.html"),
   ("Electronic business card (vCard)", "electronic-business-card.html"),
   ("Digital business card vs NFC card", "digital-business-card-vs-nfc-card.html"),
   ("Free digital business card", "free-digital-business-card.html"),
 ],
}

PAGES = [VCARD_QR]
