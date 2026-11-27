# filmlab-editor

An open-source film photo editor that runs entirely in the browser. Inspired by VSCO and Adobe Lightroom. One HTML file, no install, no server — your photos never leave your machine.

![Filmlab Editor](images/filmlab-editor.png)

## Use it

Open `index.html` in a recent Chrome, Edge, Safari or Firefox (WebGL2 required). Drop in photos or a whole folder, or click **Sample**.

## Features

- **Film scans** — invert colour negatives, auto-detect the orange film base or pick it from the rebate.
- **Light & colour** — exposure, contrast, highlights, shadows, fade, temperature, tint, saturation, vibrance, black & white, split toning.
- **Film character** — resolution-aware grain, halation, vignette, and presets (Portra 400, Gold 200, Ektar 100, Fuji 400H, Cinestill 800T, Superia 400, Tri-X 400, HP5 Plus).
- **Generative effects** — pixelate/LED, Bayer and noise dithering, CMY halftone, gaussian splats, Voronoi glass, Kuwahara, flow lines (LIC), ink edges, ASCII, CRT.
- **Crop & rotate** — film-format aspect ratios (35mm, 645, 6×7, 4×5, XPan), straighten with auto-fit, 90° rotation, flips.
- **Batch** — import a folder, per-image edits and history, apply a look to every frame.
- **Export** — JPEG, PNG, WebP, AVIF, TIFF, BMP; several formats and several images at once as a .zip; full-size or scaled.
- **Tools** — live histogram, 1:1 loupe (hold Z), before/after (hold \), undo/redo.

Everything is rendered in a single WebGL2 shader, so the preview is live and exports are rendered at full resolution in tiles.

## Fonts

The UI is set in [ABC Areal](https://abcdinamo.com/typefaces/areal) by Dinamo, which is a licensed typeface and is **not included** in this repo. Without it the page falls back to system fonts. If you hold a licence, put these files in a `fonts/` folder next to `index.html` (it's git-ignored):

```
fonts/ABCAreal-Regular.woff2
fonts/ABCAreal-Medium.woff2
fonts/ABCArealMono-Regular.woff2
```

## Build

`index.html` is generated from `src/index.template.html`:

```sh
python3 build.py               # index.html — fonts linked from ./fonts/
python3 build.py --standalone  # dist/film-lab.html — fonts embedded (git-ignored, for your own use)
```

## Keyboard

| Key | Action |
| --- | --- |
| ← → | Previous / next image |
| C · Enter · Esc | Crop · apply · cancel |
| [ ] | Rotate |
| \ (hold) | Before / after |
| Z (hold) | 1:1 loupe |
| ⌘O · ⌘E | Upload · export |
| ⌘Z · ⇧⌘Z | Undo · redo |

## License

Code: MIT — see [LICENSE](LICENSE). The sample photo (`assets/pnw_pond.jpg`) is © Jules (@itsjoopark), all rights reserved. ABC Areal is © Dinamo and not part of this repository.
