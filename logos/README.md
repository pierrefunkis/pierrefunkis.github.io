# Client logos

Each file here is loaded by the client strip on the home page:

```
<img class="client-logo" src="/logos/back-market.svg" alt="Back Market" ...>
```

| File | Client |
| --- | --- |
| `pernod-ricard.svg` | Pernod Ricard |
| `back-market.svg` | Back Market |
| `pawp.svg` | Pawp |
| `med-surg-solutions.png` | Med Surg Solutions |
| `shelt.png` | Shelt |

## Credential marks

`amazon.svg` is not a client logo. It sits in the founder credentials row on
the home page and on About ("Previously"), and is Amazon's official
single-colour form, taken from [simple-icons](https://simpleicons.org) (CC0).
It is filled `#111111` rather than `currentColor`, because it is loaded through
an `<img>` and so has no colour context to inherit.

**HEC Paris has no file yet.** "Educated at" falls back to a typographic
stand-in, `<span class="fact-word">HEC Paris</span>`.

There is nothing to edit to fix that. `credential()` in `tools/shared.py`
looks for the file at build time:

```
logos/hec-paris.svg   (or .png)
```

Drop it in, run `python3 tools/build.py`, and both the home page and About
switch to the real mark. The intrinsic width and height are read out of the
file, so the row reserves the right box and does not shift as the mark loads.

The same applies to `amazon.svg`: replace the file and rebuild. `.fact-mark`
sizes by height, so a file only needs a trimmed artboard, and either SVG or a
transparent PNG at roughly 2x the displayed height works.

To replace one, drop in the new file and update the `src`, `width` and `height`
on its `<img>` in `index.html`. The dimensions should be the file's real
intrinsic size so the browser reserves the right space before it loads.

## Sizing

The strip sizes logos by height, not width, so they share one optical scale,
and each sits in a fixed-height row box so marks of different proportions share
a baseline. Modifier classes handle shapes that do not suit the shared height:

- `.client-logo--tall` for stacked lockups (symbol above wordmark), which look
  undersized at the shared height. Pernod Ricard uses it.
- `.client-logo--wide` for long wordmarks, which look oversized at the shared
  height. Back Market uses it.
- `.client-logo--dense` for solid, heavily inked lockups, which sit heavier than
  wordmarks at the shared height. Med Surg Solutions uses it.

Judge this by eye after adding a logo rather than by matching numbers.

## Preparing a replacement file

- **SVG is preferred** where the client provides one: sharp at any size and a
  fraction of the weight. PNG is fine otherwise, at roughly 2x the displayed
  size so it stays sharp on retina screens, with a transparent background.
- Trim the artboard to the logo itself. Built-in padding makes a logo look
  smaller than its neighbours.
- Full colour is correct, and it is what visitors see: the strip no longer
  desaturates anything.
- Logos sit on the warm off-white ground, so avoid artwork that is white or
  very light.

## Usage rights

Displaying a client's logo usually needs their sign-off, and several of these
brands publish specific logo usage guidelines. Confirm permission for each one
before this goes live.

The same applies to the credential marks, and more sharply: Amazon's trademark
guidelines restrict use of their marks where it could imply a partnership or
endorsement. A factual "previously worked here" credential on a founder
biography is the normal use of this pattern, but it is worth a look at their
current guidelines before launch.
