# -*- coding: utf-8 -*-
"""Shared chrome for the Semantic site generator.

The site itself is plain static HTML with no build step. This module exists so
the nav, footer and <head> boilerplate are written once instead of drifting
across seven hand-edited pages; running build.py rewrites the HTML files that
are actually committed and served.
"""

import os
import re

SITE = 'https://www.workwithsemantic.com'
EMAIL = 'pierre@workwithsemantic.com'
LINKEDIN = 'https://www.linkedin.com/in/pierresarkis/'

FONTS = ('https://fonts.googleapis.com/css2?'
         'family=Schibsted+Grotesk:wght@400;500;600'
         '&family=Inter:wght@400;500;600&display=swap')

# Two overlapping circles, carried over from the previous identity and recoloured
# to the new palette. Dark disc in front, green disc behind, light core.
MARK = ('<svg width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true">'
        '<circle cx="11" cy="16" r="8.5" fill="#304A43" opacity="0.5"/>'
        '<circle cx="21" cy="16" r="8.5" fill="#111111"/>'
        '<circle cx="16" cy="16" r="3.6" fill="#FFFFFF"/></svg>')

ARROW = ('<svg width="13" height="13" viewBox="0 0 13 13" fill="none" aria-hidden="true">'
         '<path d="M1.5 6.5h10M7.5 2.5l4 4-4 4" stroke="currentColor" stroke-width="1.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

NAV_ITEMS = [
    ('/what-we-do/', 'What We Do'),
    ('/insights/', 'Insights'),
    ('/about/', 'About'),
]

CTA_LABEL = 'Get in touch'
CTA_HREF = '/contact/'


def head(title, desc, path, og_title=None, og_desc=None, jsonld='', extra=''):
    """<head> for one page. path is the site-root-relative URL, e.g. '/about/'."""
    canonical = SITE + path
    og_title = og_title or title
    og_desc = og_desc or desc
    ld = '\n  <script type="application/ld+json">\n%s\n  </script>' % jsonld if jsonld else ''
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#111111">

  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Semantic">
  <meta property="og:locale" content="en_US">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:image" content="{site}/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Semantic: senior data expertise, delivered by a dedicated team">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="{site}/og-image.png">

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/favicon.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts}" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">{extra}{ld}
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>
'''.format(title=title, desc=desc, canonical=canonical, og_title=og_title,
           og_desc=og_desc, site=SITE, fonts=FONTS, extra=extra, ld=ld)


def nav(active=''):
    """Sticky navbar. active is the href of the current page, or '' for none.

    The links are real markup on every page rather than injected by script, so
    crawlers can follow them.
    """
    links = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        links.append('      <li><a class="nav-link" href="%s"%s>%s</a></li>' % (href, cur, label))

    mobile = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        mobile.append('  <a href="%s"%s>%s</a>' % (href, cur, label))

    return '''
<nav class="nav" aria-label="Main">
  <div class="container nav-inner">
    <a class="nav-brand" href="/" aria-label="Semantic home">{mark}Semantic</a>

    <ul class="nav-links">
{links}
    </ul>

    <div class="nav-spacer"></div>

    <a class="btn btn--primary nav-cta" href="{cta_href}">{cta_label}</a>

    <button class="nav-toggle" id="navToggle" type="button" aria-label="Open navigation"
            aria-expanded="false" aria-controls="mobileMenu">
      <svg width="20" height="14" viewBox="0 0 20 14" fill="none" aria-hidden="true">
        <path d="M0 1h20M0 7h20M0 13h20" stroke="currentColor" stroke-width="1.5"/>
      </svg>
    </button>
  </div>
</nav>

<div class="mobile-menu" id="mobileMenu">
{mobile}
  <a class="btn btn--primary" href="{cta_href}">{cta_label}</a>
</div>

<main id="main">
'''.format(mark=MARK, links='\n'.join(links), mobile='\n'.join(mobile),
           cta_href=CTA_HREF, cta_label=CTA_LABEL)


def cta_band(heading, sub, label=CTA_LABEL, href=CTA_HREF):
    return '''
  <section class="cta-band">
    <div class="container">
      <h2>{heading}</h2>
      <p>{sub}</p>
      <div class="actions">
        <a class="btn btn--light" href="{href}">{label} {arrow}</a>
      </div>
    </div>
  </section>
'''.format(heading=heading, sub=sub, href=href, label=label, arrow=ARROW)


FOOTER = '''
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <a class="footer-brand" href="/" aria-label="Semantic home">{mark}Semantic</a>
        <p class="footer-tag">Senior data expertise, delivered by a dedicated team. We help
          enterprises solve complex data problems, from diagnosis to implementation.</p>
      </div>
      <div class="footer-col">
        <h4>Semantic</h4>
        <ul>
          <li><a href="/what-we-do/">What We Do</a></li>
          <li><a href="/insights/">Insights</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="/for-talents/">Join the team</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="{linkedin}" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Semantic. All rights reserved.</span>
      <span>Europe &middot; United States &middot; Middle East</span>
    </div>
  </div>
</footer>

<script src="/main.js" defer></script>
</body>
</html>
'''.format(mark=MARK, email=EMAIL, linkedin=LINKEDIN)


ORG_LD = '''{
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "%s/#organization",
    "name": "Semantic",
    "url": "%s/",
    "logo": "%s/favicon.svg",
    "slogan": "Senior data expertise, delivered by a dedicated team.",
    "description": "Semantic is a boutique data consultancy that helps enterprises solve complex data problems, from diagnosis to implementation.",
    "email": "%s",
    "founder": {
      "@type": "Person",
      "name": "Pierre Sarkis",
      "jobTitle": "Founder and Principal",
      "alumniOf": { "@type": "CollegeOrUniversity", "name": "HEC Paris" },
      "sameAs": "%s"
    },
    "areaServed": [
      { "@type": "Place", "name": "Europe" },
      { "@type": "Place", "name": "United States" },
      { "@type": "Place", "name": "Middle East" }
    ],
    "knowsAbout": [
      "Data Quality", "Data Reliability", "Data Management", "Data Governance",
      "Data Migration", "Analytics", "Decision Support", "Data Engineering",
      "AI Readiness", "Business Intelligence", "Master Data Management"
    ]
  }''' % (SITE, SITE, SITE, EMAIL, LINKEDIN)


# ── Founder credentials ─────────────────────────────────────────────────────

LOGO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'logos')


def _intrinsic(path):
    """The file's own pixel dimensions, so the <img> reserves the right box and
    the row does not shift as the mark loads."""
    if path.endswith('.png'):
        with open(path, 'rb') as fh:
            head = fh.read(33)
        # IHDR width and height are the two big-endian longs at offset 16
        return int.from_bytes(head[16:20], 'big'), int.from_bytes(head[20:24], 'big')

    svg = open(path).read(4096)
    box = re.search(r'viewBox="[\d.+-]+\s+[\d.+-]+\s+([\d.]+)\s+([\d.]+)"', svg)
    if box:
        return int(round(float(box.group(1)))), int(round(float(box.group(2))))
    w = re.search(r'\bwidth="([\d.]+)', svg)
    h = re.search(r'\bheight="([\d.]+)', svg)
    if w and h:
        return int(round(float(w.group(1)))), int(round(float(h.group(1))))
    # Square is the safest guess; .fact-mark sizes by height either way.
    return 24, 24


def credential(slug, alt, fallback):
    """One founder credential: "Previously", "Educated at".

    Renders the institution's own mark when logos/<slug>.svg or .png is present,
    and a typographic stand-in when it is not. The check happens at build time
    rather than being hardcoded, so dropping the file into logos/ and rebuilding
    is the entire swap, with the right intrinsic dimensions picked up from the
    file itself.
    """
    for ext in ('svg', 'png'):
        path = os.path.join(LOGO_DIR, '%s.%s' % (slug, ext))
        if os.path.exists(path):
            w, h = _intrinsic(path)
            # A stacked lockup carries its own second line, so at the height a
            # single-line wordmark wants, that line stops being readable. Same
            # judgement the client strip makes, from the file's own proportions:
            # anything squarer than about 2.4:1 gets the taller box.
            cls = 'fact-mark' if w / float(h) >= 2.4 else 'fact-mark fact-mark--tall'
            return ('<img class="%s" src="/logos/%s.%s" alt="%s" '
                    'width="%d" height="%d" decoding="async">' % (cls, slug, ext, alt, w, h))
    return '<span class="fact-word">%s</span>' % fallback
