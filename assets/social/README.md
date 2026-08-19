# Social images — source, not mystery PNGs

Both images in `docs/` are rendered from the two HTML files here, so they can be regenerated when
wording changes rather than reconstructed by eye.

    node shot.js og-1200x630.html  out@2x.png 1200 630   # deviceScaleFactor 2
    node shot.js og-1080x1080.html out@2x.png 1080 1080
    # then downsample to the nominal size with PIL/LANCZOS and save optimized PNG

`shot.js` is a six-line Puppeteer screenshot script: launch, `setViewport({deviceScaleFactor: 2})`,
`goto('file://…')`, `screenshot()`. Rendering at 2× and downsampling is what keeps the hairlines and
the letter-spaced monospace from crawling.

| File | Size | Where it goes |
| --- | --- | --- |
| `docs/og-image.png` | 1200 × 630 | `og:image` / `twitter:image` — link previews |
| `docs/social-square.png` | 1080 × 1080 | feed posts |

Palette and type come from `docs/index.html`; the design brief they were built against is in the
builder's `briefs/og-images/`. Both must survive being scaled to thumbnail size — check that the
headline and the three type words still read at 300 px wide before replacing either.
