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

The modal form is **not yet wired to a backend**. Until it is, submitting opens
the visitor's mail client with the answers pre-filled, so enquiries still reach
you rather than disappearing.

To take real submissions, create a form at [formspree.io](https://formspree.io)
(or any equivalent) and set the endpoint at the top of `main.js`:

```js
var FORM_ENDPOINT = 'https://formspree.io/f/xxxxxxxx';
```

The submit handler already POSTs the form data and shows the success state on a
2xx response, so nothing else needs changing.

## SEO checklist for new pages

Every page should carry a unique `<title>` (under ~60 characters), a unique meta
description (under ~160), a self-referencing canonical URL, Open Graph and
Twitter tags, exactly one `<h1>`, and a JSON-LD block. `sitemap.xml` and
`robots.txt` both point at `https://www.workwithsemantic.com`.

## House style

- No em dashes in visible copy. Use commas, colons or a full stop instead.
- The nav labels are Services / Careers / About. The Careers page still lives at
  `/for-talents/` so existing inbound links keep working; only the label changed.

## Known follow-ups

- `og-image.png` still carries the previous positioning. It needs regenerating
  to match the current headline.
- The client logos in `logos/` are typographic placeholders. See `logos/README.md`
  for how to swap in the real files.
- `CNAME` is `www.workwithsemantic.com` but the contact address on the site is
  `hello@semantic-data.io`. Confirm the mailbox before switching the address, so
  the contact form does not start sending to somewhere undeliverable.
- Submit `sitemap.xml` in Google Search Console once the domain is verified.
