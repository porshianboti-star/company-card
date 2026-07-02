# CompanyCard

The digital business card for people & teams. — `www.company-card.com`

A complete brand + marketing website, modeled on the Blinq vision, built modern-minimal in an indigo-violet palette.

## Open the site
Double-click **`index.html`** to open the site in your browser. All pages are linked through the nav:

| Page | File | What's on it |
|------|------|--------------|
| Home | `index.html` | Hero with a **live card builder** (type your name → the demo card updates), features, how-it-works, individual vs. teams, testimonials |
| For Teams | `business.html` | Admin dashboard, brand control, SSO, CRM, security — the team product |
| Features | `features.html` | Full feature breakdown + product mockups |
| Pricing | `pricing.html` | Free / Pro / Business / Enterprise with a working monthly↔annual toggle |
| Brand Kit | `brand-kit.html` | Logo, colours, type, slogan, voice & messaging guidelines |

## Brand quick reference

**Slogan:** One tap. Every connection.

**Colours**
- Brand gradient `#6366F1 → #8B5CF6 → #A855F7` (135°)
- Indigo 500 `#6366F1` (primary) · Indigo 600 `#4F46E5` (hover)
- Ink `#0B0A1F` (headings) · Slate 600 `#475569` (body)
- Violet 50 `#F5F3FF` · Slate 100 `#F1F5F9` (surfaces)

**Type:** Poppins (display / headlines) · Inter (body / UI) — both free on Google Fonts.

## Logo files
- `assets/logo-primary.svg` — full lockup, light backgrounds
- `assets/logo-white.svg` — reversed, dark backgrounds
- `assets/logo-icon.svg` — icon only (app / favicon / avatar)
- `assets/png/` — PNG exports + favicons (32 / 64 / 180 / 512)

## Structure
```
CompanyCard/
├─ index.html  business.html  features.html  pricing.html  brand-kit.html
├─ README.md
└─ assets/
   ├─ styles.css   (design system: tokens + components)
   ├─ home.css     (homepage cinematic layer: mesh gradient, 3D, marquee, motion)
   ├─ app.js       (nav, scroll reveal, pricing toggle, live card builder)
   ├─ home.js      (3D tilt, parallax, auto-typing, count-up, magnetic, particles)
   ├─ logo-*.svg   (vector logos)
   └─ png/         (raster logos + favicons)
```

### Homepage motion
The home page is built to feel alive: an animated mesh-gradient backdrop with a subtle particle field, a 3D business card that tilts to your cursor with floating UI chips, an auto-typing card builder, an infinite logo marquee, a fanned 3D card showcase with parallax, hover-tilt feature cards, an animated step-through "how it works", and count-up stats. All motion respects `prefers-reduced-motion`. Drop real `.mp4` product clips into the demo sections anytime to replace the simulated motion.

The site is self-contained static HTML/CSS/JS — no build step. Host the folder on any static host (Netlify, Vercel, Cloudflare Pages, S3) pointed at `company-card.com`.
