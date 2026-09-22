# LotusArise social image template (approved 22 Sept 2026)

Renders branded post images from HTML/CSS with headless Chromium. Used by the daily
"LotusArise daily social media posts" task. Brand: blue #015289, orange #D17502, navy #0A2A4A.

## Setup (in the task's workspace)
```bash
cd template
npm i @fontsource/poppins @fontsource/inter lucide-static playwright-core
mkdir -p assets html out
curl -sSL -o assets/logo.png https://lotusarise.com/wp-content/uploads/brand/lotusarise-ias-logo.png   # read-only download
```

## Build slides
Write a Python script modelled on `example_rare_earths.py`:
```python
from la_design import *
html = page(slide(HEAD, BODY), page_no='2/6')          # standard slide with URL footer + page number
html = page(slide(HEAD, BODY), cta='Share your answer in comments')   # MCQ question slide
html = page(..., W=1000, H=1500)   # Pinterest pin      html = page(..., W=1200, H=675)  # X / LinkedIn card
```
Then: `node render.js out html/*.html` → PNGs in `out/`. **Exit code 2 = some slide overflowed; fix text and re-render.**

### Header helpers
- `top(date='22 September 2026')` – logo card + "CURRENT AFFAIRS" block + date (cover slides)
- `top(kicker_a='MAINS', kicker_b='ANGLE', date=...)`
- `mini_top('WHY IN NEWS', logo=False)` – orange label + rule line (inner slides; logo=True adds small logo)
- `headline('Navy part', 'orange part')` (cover h1), `h2('Navy part', 'orange part')` (inner titles)
- Cover extras: `'<div class="tagrow"><span class="tag">ECONOMY | GS-3</span><span class="line"></span></div>'`, `'<div class="rule"></div>'`, `'<div class="lead">…</div>'`, `hero('magnet', ['car','wind','plane','cpu'])` + swipe label

### Body blocks (combine 2–4 per slide)
- `info(icon, title, body, orange=False)` – light-blue box with round icon
- `bullets_box(icon, title, [points], orange=False)`
- `cards([(icon, heading, text), …])` – 3 icon cards with dashed dividers
- `stats([(number, label, big?), …])` – big-number cards; first one with big=True spans full width
- `chain(['Oxide','Metal','Alloy','Magnet'])` – process/value-chain arrows
- `flash([(key, value), …])` – Prelims flashcards (use `slide(..., fill=True)`)
- `mcq_q([statements], ask, [4 options])`, answer slide: `'<div class="ans">…'` + `verdicts([(True/False, heading, reason), …])`
- `'<div class="banner">Section</div>'` (navy) / `'<div class="banner or">…'` (orange), `'<div class="mq">Mains Q…</div>'`, `'<div class="chips"><span class="chip">GS-3</span>…</div>'`

Inline text: `**bold**` = navy bold, `==highlight==` = orange bold. Icons: any name from `node_modules/lucide-static/icons/` (e.g. globe, landmark, scale, shield, factory, leaf, droplets, ship, gavel, users, trending-up).

## Rules (owner-approved)
- Footer shows ONLY a globe icon + www.lotusarise.com inside the dark band (no social handles). Page number on the right.
- Max ~40 words per slide body; one idea per slide; body text never below 22px; overflow must be 0.
- Logo: official file only, on a white card; never redraw, recolour or crop.
- No competitor logos, contact details, photos or copied wording.
