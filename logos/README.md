# Client logos

Each file here is loaded by the client strip on the home page:

```
<img class="client-logo" src="/logos/back-market.svg" alt="Back Market" ...>
```

The files currently committed are **typographic placeholders**. To swap in a
real logo, replace the file at the same path and keep the same filename. No
HTML or CSS change is needed.

| File | Client |
| --- | --- |
| `pernod-ricard.svg` | Pernod Ricard |
| `back-market.svg` | Back Market |
| `pawp.svg` | Pawp |
| `med-surg-solutions.svg` | Med Surg Solutions |
| `shelt.svg` | Shelt |

## Preparing a replacement file

- **SVG is strongly preferred.** PNG works too, but then change the extension in
  the `src` on the home page and supply a 2x resolution file (roughly 400px wide)
  so it stays sharp on retina screens.
- Trim the artboard to the logo itself. Built-in padding makes one logo look
  smaller than its neighbours, since the strip sizes everything by height.
- Full colour is correct. The strip desaturates the logos in CSS and restores
  colour on hover, so a colour source file is what you want.
- Logos sit on a white background, so avoid files whose artwork is white or
  very light.

## Usage rights

Displaying a client's logo usually needs their sign-off, and several of these
brands publish specific logo usage guidelines. Confirm permission for each one
before this goes live.
