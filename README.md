# Semantic, workwithsemantic.com

Marketing site for Semantic, served by GitHub Pages from this repository. Static
HTML, CSS and vanilla JS, with no runtime dependencies and no build step at
deploy time. Push to the default branch and it deploys.

## Positioning

> **SEMANTIC**
> Senior data expertise, delivered by a dedicated team.

Semantic is a boutique data consultancy for enterprises. Pierre Sarkis is the
founder and principal, but the site is branded around Semantic: Pierre appears
on About, in one short credibility block on the home page, and as the person
behind the contact CTA. He does not appear anywhere else.

Each page answers exactly one question, and no page repeats another's answer:

| Page | Answers |
| --- | --- |
| `/` | What is Semantic? |
| `/what-we-do/` | What can Semantic do? |
| `/insights/` | Does Semantic have something intelligent to say? |
| `/about/` | Who is behind Semantic? |
| `/contact/` | How do I start working with Semantic? |

## Structure

```
index.html                    /                → Home
what-we-do/index.html         /what-we-do/     → Expertise, technology, delivery model
insights/index.html           /insights/       → Editorial index
insights/<slug>/index.html    /insights/<slug>/→ One article each
about/index.html              /about/          → Founder, why Semantic, the team
contact/index.html            /contact/        → Contact, booking form
for-talents/index.html        /for-talents/    → Careers (path kept for inbound links)
404.html                                       → GitHub Pages serves this on unknown URLs
style.css                                      → all styles
main.js                                        → mobile menu, nav state, contact form
favicon.svg  og-image.png  robots.txt  sitemap.xml
logos/                                         → client logos for the home page strip
pierre-sarkis.jpeg                             → founder photograph
tools/                                         → the generator that writes the HTML
CNAME                                          → www.workwithsemantic.com
```

`/for-talents/` is linked from the footer rather than the main nav. The main nav
is for clients; the path is unchanged so existing inbound links keep working.

## Editing

The HTML files are generated from `tools/`, so edit the source and rebuild
rather than editing the emitted HTML by hand:

```
python3 tools/build.py
```

That rewrites every page, `404.html` and `sitemap.xml` from:

| File | Holds |
| --- | --- |
| `tools/shared.py` | `<head>`, navbar, footer, CTA band, Organization schema |
| `tools/pages_home.py` | home page, client strip, the four home capabilities |
| `tools/pages_wwd.py` | the five capabilities in full, delivery model, selected work |
| `tools/pages_insights.py` | insights index and article layouts |
| `tools/articles.py` | **article content**: one dict per piece |
| `tools/pages_about.py` | founder, why Semantic, the team |
| `tools/pages_contact.py` | first-session copy, form, next steps |
| `tools/pages_careers.py` | careers page and the 404 body |
| `tools/tech.py` | the 22 technology tags, as inline SVG |
| `tools/plates.py` | the three line illustrations |

Nav and footer are emitted into every page rather than injected by script: the
links have to be in the HTML for search engines to follow them.

Python 3 only, standard library only. There is nothing to install.

### Adding an article

Add a dict to `ARTICLES` in `tools/articles.py` (slug, category, ISO date,
display date, title, excerpt, meta description, body HTML) and rebuild. The
first entry in the list is the featured piece on `/insights/`. The page,
the index card, the JSON-LD and the sitemap entry all follow from it.

### Adding a case study

`/what-we-do/` currently states that we do not publish client case studies. A
commented-out `<article class="capability">` template sits in
`tools/pages_wwd.py` under **Selected Work**: fill one block per engagement
(client or context, challenge, approach, outcome), drop the copy above it, and
the section becomes a proper work page.

### Styles

`style.css`. The design tokens are the CSS custom properties in `:root` at the
top; responsive rules live in the media queries at the bottom.

- Near-black `#111111` for headings, `#3D3D39` for running copy, neutral gray
  `#6F6F6A` for labels and captions, hairline `#E4E2DC`.
- Two grounds: warm off-white `#F7F6F2` and a soft green tint `#EDF2EE`, used
  in alternating bands so the page is not a run of white blocks.
- Brand green `#304A43` carries primary buttons and links, `#3E6157` is its
  hover, and deep green `#1F332C` is the ground for dark bands. Dark sections
  are green rather than black: black read as heavy and colourless.
- The footer is a light ground with a green rule on top. A dark footer under a
  dark CTA band gave every page a black slab at the bottom.
- Client and technology logos are shown in their own colours, always. Colour on
  hover only throws away recognisability, and the reveal depends on a hover the
  row often never gets.
- Schibsted Grotesk for headings, Inter for running text, both from Google
  Fonts with a system fallback stack.
- Corners are 3px. Sections are separated by hairlines, tinted grounds and
  whitespace rather than by cards.

Illustrations live in `tools/plates.py` as three line drawings: a fan of
sources converging to one answer (home hero), an oblique stack of planes (the
delivery model band), and a group of nodes around one lead (About). They are
strokes, arcs and dots only, with no frame and no ground of their own, so they
read as drawing rather than as an embedded image. Nothing built from filled
grey rectangles belongs here: an earlier hero was, and it read as a loading
skeleton. Below 1040px the plates are hidden and the copy takes the column.

Headings never sit alone in their own column. A heading in the left half of a
two-column block ends up stranded at the top of several hundred pixels of
nothing, because the row's height comes from the other column. Use
`.section-head--wide`, which sets the heading and its intro side by side and
lets the content run full width below. The same applies to a capability row:
title above its own body, one left edge, `.capabilities--2up` when the bodies
are short enough to pair.

## Local preview

Serve from the repo root so root-relative paths (`/style.css`) resolve:

```
python3 -m http.server 8080
```

Then visit http://127.0.0.1:8080/.

## Contact form

`/contact/` carries an inline form (name, company, role, work email, what are
you trying to solve) that posts to [Web3Forms](https://web3forms.com), which
emails each submission to the address registered against the access key. Both
live at the top of `main.js`:

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

### Adding a booking calendar

There is no scheduling tool connected. If one is adopted, its embed drops into
the marked comment above the form in `tools/pages_contact.py`; the form then
becomes the fallback for people who would rather write than book a slot.

## SEO

Every page carries a unique `<title>` (under ~60 characters), a unique meta
description (under ~160), a self-referencing canonical URL, Open Graph and
Twitter tags, exactly one `<h1>`, and a JSON-LD block. `404.html` is
`noindex`, since GitHub Pages serves it for any unknown URL. `sitemap.xml` and
`robots.txt` both point at `https://www.workwithsemantic.com`.

## House style

- No em dashes in visible copy. Use commas, colons or a full stop instead.
- Nav labels are What We Do / Insights / About, with **Get in touch** as the
  CTA. There is no "Home" nav item; the wordmark links home. The CTA label is
  `CTA_LABEL` in `tools/shared.py`; the footer and breadcrumb say "Contact".
- Do not invent clients, metrics, team size, certifications or years of
  experience. Where content is missing, say so plainly or leave a placeholder.

## Social preview image

`og-image.png` is 1200x630 and is generated, not hand-drawn: `tools/og-card.html`
is a card using the site's own fonts and palette, screenshotted headlessly at
exactly 1200x630. Regenerate it whenever the home headline changes, and keep the
`og:image:width` / `og:image:height` meta values in step with the real file.

## Known follow-ups

- Every address on the site is `pierre@workwithsemantic.com`: the footer
  contact link, the Careers apply CTAs, the Organization schema, and the
  contact form's fallback. That mailbox has to exist.
- Client logos are shown with the clients' permission in mind: several of these
  brands publish logo usage guidelines. Confirm sign-off for each before this
  goes live (see `logos/README.md`).
- The three articles under `/insights/` are drafts written to give the section
  a real shape. Review the voice before promoting them.
- Submit `sitemap.xml` in Google Search Console once the domain is verified.
