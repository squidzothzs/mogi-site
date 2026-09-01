# MOGI — main site

Static site. No build step, no dependencies. Open `index.html` or serve the folder.

```bash
python -m http.server 4173
```

## Files

| File | What it is |
|---|---|
| `index.html` | Every page. Views are `<section class="view">`, switched by the URL hash. |
| `style.css` | All styling. Brand tokens are at the top in `:root`. |
| `app.js` | Router, About chapters, crewmate cards, holder list, scroll reveals. |
| `assets/` | Images. |
| `_optimize_images.py` | Optional. Shrinks everything in `assets/`. Re-run after adding big photos. |

## Routes

`#/` menu · `#/about` · `#/stock` · `#/owner` · `#/drop0`

## What to fill in before the expo

Everything still needing real content is marked `[EDIT]` in the page (shows in red) or
`<!-- TODO -->` in the source.

**In `app.js` (top of the file):**
- `HOLDERS` — the 20 Drop 0 buyers. Replace `'Anonymous'` with real names.
- `CREW` — the four people in the boat: role, name, one-line bio.

**In `index.html`:**
- Social + shop links — search for `TODO: real links` (footer) and `Shop ↗` (menu).
- Email — search for `hello@mogi.example` and replace everywhere.
- Drop 0 release date — `[EDIT — date]` in the Drop 0 section.
- Core beliefs, "how we get there" steps, founder story — all marked `[EDIT]`.
- Owner Info page is a deliberate placeholder, per the blueprint.

## Adding a product

Copy one `<article class="item">` block in the "In development" grid, swap the image
and text. Drop the image in `assets/` first (PNG with transparent background, ~850px).

## Notes

- Sold-out styling is the `item--gone` class — grey plate, drained image, `SOLD OUT` stamp.
  Add it to any item that runs out; nothing else needs to change.
- The boat scene is inline SVG in `index.html`. Crewmate positions are the `<use href="#crew">`
  x/y values; `data-crew` maps each one to the `CREW` array in `app.js`.
- Animations are disabled automatically for visitors with reduced-motion turned on.

## Deploying

Drag the whole folder onto [app.netlify.com/drop](https://app.netlify.com/drop) — it is a
plain static site, so any host works. No server needed.
