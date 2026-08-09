# Semantic, workwithsemantic.com

Marketing site for Semantic, served by GitHub Pages from this repository.
Static HTML, CSS and vanilla JS, with no build step and no dependencies. Push to the
default branch and it deploys.

## Structure

```
index.html             /               → Services (home)
for-talents/index.html /for-talents/   → Careers (path kept for existing links)
about/index.html       /about/         → About
404.html                               → GitHub Pages serves this on unknown URLs
style.css                              → all styles
main.js                                → mobile menu, nav pill, contact modal
favicon.svg
logos/                                 → client logos for the home page strip
og-image.png                           → 1200x630 social preview
robots.txt  sitemap.xml
CNAME                                  → www.workwithsemantic.com
```

Nav and footer are repeated in each page on purpose: the links have to be in
the HTML for search engines to follow them. The contact modal is built in
`main.js` instead, since it cannot work without JS and nothing in it needs to
be indexed.

## Local preview

Serve from the repo root so root-relative paths (`/style.css`) resolve:

```
npx http-server -p 8080
```

Then visit http://127.0.0.1:8080/.

## Editing

- **Copy and page content**: edit the relevant `.html` file directly.
- **Styles**: `style.css`. Design tokens are the CSS custom properties in
  `:root` at the top; responsive rules live in the media queries at the bottom.
- **Adding a page**: copy an existing page, update `<title>`, the meta
  description, `<link rel="canonical">`, the Open Graph/Twitter tags and the
  JSON-LD block, then add the link to the nav and footer of every page and a
  new `<url>` entry in `sitemap.xml`.

## Contact form

The modal form posts to [Web3Forms](https://web3forms.com), which emails each
submission to the address registered against the access key. Both live at the
top of `main.js`:

```js
var FORM_ENDPOINT = 'https://api.web3forms.com/submit';
var ACCESS_KEY    = '6092d285-4b44-4798-9e7f-bb4429798754';
```

The access key is public by design, exactly as in Web3Forms' own copy-paste
snippet, so it belongs in this file rather than in a secret store. Restrict it
to this domain in the Web3Forms dashboard so it cannot be reused elsewhere.

The handler posts JSON and adds `access_key`, `subject`, `from_name` and
`replyto` (set to the enquirer's address, so replying in your mail client goes
to them). Web3Forms answers `200` with `success: false` for a rejected
submission, so the handler checks the body rather than the status alone, and
gives a distinct message on `429`.

Spam is filtered by a honeypot checkbox named `botcheck`, which the browser
drops before sending and which Web3Forms also rejects server-side.

Clearing `FORM_ENDPOINT` reverts to the mail-client fallback, which shows its
own "we opened your email app" message rather than claiming the message was
received.

The free tier allows 250 submissions a month. Spam POSTed straight at the
endpoint counts towards that, since it never loads the page and so never sees
the honeypot.

## SEO checklist for new pages

Every page should carry a unique `<title>` (under ~60 characters), a unique meta
description (under ~160), a self-referencing canonical URL, Open Graph and
Twitter tags, exactly one `<h1>`, and a JSON-LD block. `sitemap.xml` and
`robots.txt` both point at `https://www.workwithsemantic.com`.

## House style

- No em dashes in visible copy. Use commas, colons or a full stop instead.
- The nav labels are Services / Careers / About. The Careers page still lives at
  `/for-talents/` so existing inbound links keep working; only the label changed.

## Social preview image

`og-image.png` is 1200x630 and is generated, not hand-drawn: a small HTML card
using the site's own fonts and hero illustration, screenshotted headlessly at
exactly 1200x630. Regenerate it whenever the home headline changes, and keep the
`og:image:width` / `og:image:height` meta values in step with the real file.

## Known follow-ups

- Every address on the site is `pierre@workwithsemantic.com`: the footer
  Contact link, the Careers apply CTAs, the Organization schema, and the
  contact form's fallback. That mailbox has to exist.
- Submit `sitemap.xml` in Google Search Console once the domain is verified.
