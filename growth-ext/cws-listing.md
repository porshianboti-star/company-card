# Chrome Web Store — submission kit (CompanyCard)

Console: https://chrome.google.com/webstore/devconsole (account: porshianboti@gmail.com —
same dev account that published ProSignature).
Upload: `extension/companycard-extension-store.zip` (build: `python3 extension/build-zip.py`).

## Store listing

**Name** (from manifest): CompanyCard — digital business card

**Summary** (≤132 chars, from manifest):
Your digital business card, one click away: show its QR code, copy the share link, or save it as a contact.

**Description:**
Create your digital business card on company-card.com, then carry it in your
browser toolbar. Meet someone? Open the popup and show the QR code — they scan
it and get your full card: photo, phone, email, socials, and a Save-contact
button that adds you straight to their phone.

HOW IT WORKS
1. Create your card at company-card.com (free plan available).
2. Open your CompanyCard dashboard once — the extension picks your card up
   automatically.
3. Click the toolbar icon anywhere: show the QR, copy your share link, open
   the card, download it as a contact file (.vcf), or copy a matching email
   signature for Gmail.

WHAT IT CAN AND CAN'T DO
• No sign-in, no permissions beyond local storage, and zero network requests —
  the extension never talks to any server.
• Your card is read from your own CompanyCard pages and stored locally in your
  browser. Nothing is uploaded anywhere.
• Works offline once your card is loaded.
• Multiple cards? A picker lets you switch the active one.

Made by CompanyCard — digital business cards for professionals and teams.

**Category:** Productivity → Tools
**Language:** English
**Homepage URL:** https://company-card.com
**Support URL:** https://company-card.com/contact

## Privacy tab

**Single purpose:**
Give the user one-click toolbar access to the digital business card they
created on company-card.com: display its QR code and share link, open it,
download it as a vCard, or copy an email signature version of it.

**Permission justifications:**
- `storage` — Stores the user's own business card locally so the popup can
  show it (and its QR code) without opening the website. Nothing is synced
  to external servers.
- Content script on `company-card.com/app/*` — Reads the card the user
  created on their own CompanyCard pages (from the page's localStorage) and
  copies it into the extension's local storage. Read-only; it does not modify
  pages and runs only on the user's own CompanyCard app pages.
- Remote code: none. All code is packaged (MV3); the QR library (qrcodejs
  1.0.0) is bundled in the zip.

**Data usage disclosures (check):**
- Nothing collected by the developer — the extension makes no network requests.
- Certify: complies with CWS User Data Policy incl. Limited Use.

**Privacy policy URL:** https://company-card.com/privacy-policy

## Assets

- Icon 128×128: `extension/icon128.png` (in zip; from assets/png/logo-icon-256.png)
- Screenshots 1280×800: `growth-ext/shot1.png` (popup + QR), `growth-ext/shot2.png`
  (scan → full card), `growth-ext/shot3.png` (email signature).
- Small promo tile 440×280: optional at launch.

## Verification notes (E2E test, 2026-07-30)

Real-Chromium test (`--load-extension`, Playwright): content script on
company-card.com/app/* synced localStorage cards → popup rendered name, QR
(2 DOM children), share link; link decoded back to the same card; empty state
shown before sync. Share-link encoder verified byte-identical to the site's
`app/product.js` `CC.encode` (ASCII + Hebrew cards). A generated link opens a
fully rendered live card on company-card.com (checked in Chrome).

## Status log

- 2026-07-30: extension built (repo `extension/`), tested E2E, kit + screenshots
  ready. Next: create item in dev console, upload zip, paste listing, submit.
