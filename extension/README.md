# CompanyCard — Chrome extension

Your CompanyCard digital business card in the browser toolbar: show its QR code
to anyone, copy the share link, open the card, download it as a vCard (.vcf),
or copy a matching email signature.

## How it gets your card

Open any page under `https://company-card.com/app/` (dashboard, builder…) while
the extension is installed. A content script reads the cards that page keeps in
`localStorage` and mirrors them into `chrome.storage.local`. That's the entire
data path — the extension itself makes **zero network requests**, has **no host
permissions**, and needs **no sign-in**.

## Files

- `manifest.json` — MV3, permissions: `storage` only.
- `content.js` — read-only sync from company-card.com/app/* localStorage.
- `background.js` — stores cards, answers popup + site messages.
- `popup.html/css/js` — QR, share link, open card, vCard, email signature.
- `cc-core.js` — trimmed copy of `app/product.js` helpers (encode/vcard/signature).
  Keep `CC.encode` byte-identical to the site's, or share links diverge.
- `vendor/qrcode.min.js` — qrcodejs 1.0.0 (same library the site uses), vendored
  because MV3 forbids remote code.

## Build the store zip

    python3 extension/build-zip.py

writes `extension/companycard-extension-store.zip` (manifest at zip root).

## Load unpacked (dev)

chrome://extensions → Developer mode → Load unpacked → this folder.
