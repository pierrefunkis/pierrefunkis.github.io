# Client logos

Each file here is loaded by the client strip on the home page:

```
<img class="client-logo" src="/logos/back-market.svg" alt="Back Market" ...>
```

| File | Client | Status |
| --- | --- | --- |
| `pernod-ricard.svg` | Pernod Ricard | real logo |
| `back-market.svg` | Back Market | real logo |
| `pawp.svg` | Pawp | real logo |
| `med-surg-solutions.svg` | Med Surg Solutions | **placeholder** |
| `shelt.svg` | Shelt | **placeholder** |

The placeholders are plain typographic wordmarks. To swap one out, replace the
file at the same path and keep the same filename, then update the `width` and
`height` attributes on its `<img>` in `index.html` to the new intrinsic size so
the browser reserves the right space before the file loads.

## Sizing

The strip sizes logos by height, not width, so they share one optical scale.
Two modifier classes handle shapes that do not suit the shared height:

- `.client-logo--tall` for stacked lockups (symbol above wordmark), which look
  undersized at the shared height. Pernod Ricard uses it.
- `.client-logo--wide` for long wordmarks, which look oversized at the shared
  height. Back Market uses it.

Judge this by eye after adding a logo rather than by matching numbers.

## Preparing a replacement file

- **SVG is strongly preferred.** PNG works too, but then change the extension in
  the `src` and supply a 2x file so it stays sharp on retina screens.
- Trim the artboard to the logo itself. Built-in padding makes a logo look
  smaller than its neighbours.
- Full colour is correct. The strip desaturates in CSS and restores colour on
  hover, so a colour source file is what you want.
- Logos sit on a white background, so avoid artwork that is white or very light.

## Usage rights

Displaying a client's logo usually needs their sign-off, and several of these
brands publish specific logo usage guidelines. Confirm permission for each one
before this goes live.
