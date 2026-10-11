# -*- coding: utf-8 -*-
"""Writes the static HTML files that are committed and served.

Run from the repository root:  python3 tools/build.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)

from shared import SHOW_INSIGHTS, SITE, LINKEDIN, ORG_LD, head, nav, FOOTER  # noqa: E402
from pages_home import HOME  # noqa: E402
from pages_wwd import WHAT_WE_DO  # noqa: E402
from pages_about import ABOUT  # noqa: E402
from pages_contact import CONTACT  # noqa: E402
from pages_work import PERNOD  # noqa: E402
from pages_careers import CAREERS, NOT_FOUND  # noqa: E402
from pages_insights import insights_index, article_page  # noqa: E402
from articles import ARTICLES  # noqa: E402


def webpage_ld(path, name, desc):
    return json.dumps({
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        '@id': SITE + path + '#webpage',
        'url': SITE + path,
        'name': name,
        'description': desc,
        'inLanguage': 'en',
        'isPartOf': {'@id': SITE + '/#website'},
        'about': {'@id': SITE + '/#organization'},
    }, indent=2)


def with_graph(path, ld, crumb):
    """Wrap a single-page JSON-LD node into a graph that also defines the Organization
    and WebSite its @id references point at, plus a breadcrumb, so every page is
    self-contained for crawlers that read one URL at a time."""
    node = json.loads(ld)
    if '@graph' in node:
        return ld
    node.pop('@context', None)
    return json.dumps({
        '@context': 'https://schema.org',
        '@graph': [
            json.loads(ORG_LD),
            {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Semantic',
             'publisher': {'@id': SITE + '/#organization'}, 'inLanguage': 'en'},
            node,
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': crumb, 'item': SITE + path}]},
        ],
    }, indent=2)


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or '.', exist_ok=True)
    with open(full, 'w') as fh:
        fh.write(html)
    print('%-42s %6d bytes' % (path, len(html)))


PAGES = []

# ── Home ────────────────────────────────────────────────────────────────────
home_ld = json.dumps({
    '@context': 'https://schema.org',
    '@graph': [
        json.loads(ORG_LD),
        {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Semantic',
         'publisher': {'@id': SITE + '/#organization'}, 'inLanguage': 'en'},
        {'@type': 'WebPage', '@id': SITE + '/#webpage', 'url': SITE + '/',
         'name': 'Senior Data Expertise | Semantic',
         'description': 'We help companies solve complex data challenges, from diagnosis '
                        'to implementation.',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#organization'},
         'inLanguage': 'en'},
        {'@type': 'Service', 'serviceType': 'Data consulting',
         'provider': {'@id': SITE + '/#organization'},
         'name': 'Enterprise data consulting',
         'description': 'Senior data expertise embedded in your team, from diagnosis '
                        'through implementation.',
         'hasOfferCatalog': {
             '@type': 'OfferCatalog', 'name': 'What we do',
             'itemListElement': [
                 {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n}}
                 for n in ['Data Quality & Reliability', 'Data & AI Readiness',
                           'Data Migration', 'Analytics & Decision Support']]}},
    ],
}, indent=2)

PAGES.append((
    'index.html', '/',
    'Senior Data Expertise | Semantic',
    'We help companies solve complex data challenges, from diagnosis to implementation.',
    'Senior data expertise, embedded in your team | Semantic',
    'We help companies solve complex data challenges, from diagnosis to implementation.',
    home_ld, HOME,
))

# ── What We Do ──────────────────────────────────────────────────────────────
PAGES.append((
    'what-we-do/index.html', '/what-we-do/',
    'Our Expertise: Data Specialists | Semantic',
    'Vetted data specialists, managed by us: analysts, engineers, analytics engineers, '
    'managers and governance leads, with one accountable point of contact.',
    None, None,
    webpage_ld('/what-we-do/', 'Our Expertise | Semantic',
               'The specialists Semantic staffs, the technology they work in, and how we '
               'stay accountable for the outcome.'),
    WHAT_WE_DO,
))

if SHOW_INSIGHTS:
    # ── Insights ────────────────────────────────────────────────────────────────
    insights_ld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'Blog',
        '@id': SITE + '/insights/#blog',
        'url': SITE + '/insights/',
        'name': 'Semantic Insights',
        'description': 'Short pieces on enterprise data quality, AI readiness, migration and '
                       'analytics.',
        'publisher': {'@id': SITE + '/#organization'},
        'inLanguage': 'en',
        'blogPost': [
            {'@type': 'BlogPosting', 'headline': a['title'], 'datePublished': a['iso'],
             'url': SITE + '/insights/' + a['slug'] + '/', 'description': a['excerpt'],
             'author': {'@id': SITE + '/#organization'}}
            for a in ARTICLES],
    }, indent=2)

    PAGES.append((
        'insights/index.html', '/insights/',
        'Insights on Enterprise Data | Semantic',
        'Notes from inside enterprise data work: quality that does not hold, AI programs '
        'that stall, migrations that lose the room.',
        None, None, insights_ld, insights_index(),
    ))

    for a in ARTICLES:
        others = [o for o in ARTICLES if o['slug'] != a['slug']]
        path = '/insights/%s/' % a['slug']
        ld = json.dumps({
            '@context': 'https://schema.org',
            '@type': 'BlogPosting',
            'headline': a['title'],
            'description': a['excerpt'],
            'datePublished': a['iso'],
            'dateModified': a['iso'],
            'articleSection': a['category'],
            'url': SITE + path,
            'mainEntityOfPage': {'@type': 'WebPage', '@id': SITE + path},
            'author': {'@id': SITE + '/#organization'},
            'publisher': {'@id': SITE + '/#organization'},
            'isPartOf': {'@id': SITE + '/insights/#blog'},
            'inLanguage': 'en',
        }, indent=2)
        # Headlines are already long; appending the brand would push every article
        # title past the point where a results page truncates it.
        PAGES.append((
            'insights/%s/index.html' % a['slug'], path,
            a['title'],
            a['desc'], '%s | Semantic' % a['title'], None, ld, article_page(a, others),
        ))

# ── About ───────────────────────────────────────────────────────────────────
about_ld = json.dumps({
    '@context': 'https://schema.org',
    '@type': 'AboutPage',
    '@id': SITE + '/about/#webpage',
    'url': SITE + '/about/',
    'name': 'About Semantic',
    'description': 'Semantic combines senior data expertise with the execution capacity of '
                   'a dedicated team.',
    'inLanguage': 'en',
    'isPartOf': {'@id': SITE + '/#website'},
    'about': {'@id': SITE + '/#organization'},
    'mainEntity': {
        '@type': 'Person',
        'name': 'Pierre Sarkis',
        'jobTitle': 'Founder and Principal',
        'worksFor': {'@id': SITE + '/#organization'},
        'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'HEC Paris'},
        'image': SITE + '/pierre-sarkis.jpeg',
        'sameAs': LINKEDIN,
    },
}, indent=2)

PAGES.append((
    'about/index.html', '/about/',
    'About Semantic | Founded by Pierre Sarkis',
    'Senior data expertise with the execution capacity of a dedicated team. Founded by '
    'Pierre Sarkis, formerly of Amazon and a graduate of HEC Paris.',
    None, None, about_ld, ABOUT,
))

# ── Contact ─────────────────────────────────────────────────────────────────
contact_ld = json.dumps({
    '@context': 'https://schema.org',
    '@type': 'ContactPage',
    '@id': SITE + '/contact/#webpage',
    'url': SITE + '/contact/',
    'name': 'Contact | Semantic',
    'description': 'Start with a free advisory conversation about the data problem you are '
                   'trying to solve.',
    'inLanguage': 'en',
    'isPartOf': {'@id': SITE + '/#website'},
    'about': {'@id': SITE + '/#organization'},
}, indent=2)

PAGES.append((
    'contact/index.html', '/contact/',
    'Contact Semantic | Book a free diagnosis session',
    'Start with a free advisory conversation. Tell us the data problem you are trying to '
    'solve and we will tell you what it takes to fix it.',
    None, None, contact_ld, CONTACT,
))

# ── Case study ──────────────────────────────────────────────────────────────
PAGES.append((
    'work/pernod-ricard/index.html', '/work/pernod-ricard/',
    'Pernod Ricard Case Study: Data Quality for AI | Semantic',
    'How Semantic cut data quality errors from 30% to 2.5% across 12 markets for Pernod '
    'Ricard\'s D-STAR AI sales engine, featured by Harvard Business School.',
    None, None,
    webpage_ld('/work/pernod-ricard/', 'Pernod Ricard case study | Semantic',
               'Data quality tests, ownership and resolution processes behind D-STAR, the AI '
               'recommendation engine for Pernod Ricard sales teams.'),
    PERNOD,
))

# ── Careers ─────────────────────────────────────────────────────────────────
PAGES.append((
    'join-network/index.html', '/join-network/',
    'Join the Semantic Network | Data Professionals',
    'Join Semantic\'s network of data professionals: challenging AI and data projects, '
    'international clients and competitive compensation. Leave your details in two minutes.',
    'Data problems worth solving. Join the Semantic network.',
    'Challenging AI and data projects, international clients, competitive pay. '
    'Leave your details in a 2-minute form and we will reach out when there is a fit.',
    webpage_ld('/join-network/', 'Join Network | Semantic',
               'Join a curated team of data specialists working on demanding enterprise '
               'problems.'),
    CAREERS,
))

# Old URL: static redirect so inbound links and search results keep working.
write('for-talents/index.html',
      '<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8">'
      '<title>Redirecting to Join Network</title>'
      '<meta name="robots" content="noindex">'
      '<link rel="canonical" href="%s/join-network/">'
      '<meta http-equiv="refresh" content="0; url=/join-network/"></head>'
      '<body><a href="/join-network/">Join Network</a></body></html>\n' % SITE)


# Pages that end on the form rather than a dark band: no rule above the footer.
PLAIN_FOOTER = {'/contact/'}

# Breadcrumb label per page (the home page already ships its own graph).
CRUMBS = {'/what-we-do/': 'Our Expertise', '/about/': 'About Us',
          '/contact/': 'Contact', '/join-network/': 'Join Network',
          '/work/pernod-ricard/': 'Pernod Ricard Case Study'}

# Per-page link previews. Pages not listed use the default og-image.png.
CARDS = {
    '/join-network/': {
        'og_image': '/og-join-network.png',
        'og_alt': 'Data problems worth solving. Join the Semantic network: challenging work, '
                  'international clients, competitive pay. Two-minute form.',
    },
}

for filename, path, title, desc, og_t, og_d, ld, body in PAGES:
    active = path if any(path == href for href, _ in
                         [('/what-we-do/', 1), ('/insights/', 1), ('/about/', 1)]) else ''
    # Article pages keep Insights marked as the current section.
    if path.startswith('/insights/'):
        active = '/insights/'
    card = CARDS.get(path, {})
    if ld and path in CRUMBS:
        ld = with_graph(path, ld, CRUMBS[path])
    footer = FOOTER
    if path in PLAIN_FOOTER:
        footer = FOOTER.replace('class="footer"', 'class="footer footer--plain"', 1)
    write(filename, head(title, desc, path, og_t, og_d, ld, **card) + nav(active) + body + footer)

# ── 404 ─────────────────────────────────────────────────────────────────────
# noindex: GitHub Pages serves this for any unknown URL, so it must not be
# indexed as a page in its own right.
write('404.html',
      head('Page not found | Semantic',
           'That page is not here. Find what you were looking for from the links below.',
           '/404.html',
           extra='\n  <meta name="robots" content="noindex">')
      + nav() + NOT_FOUND + FOOTER)

# ── sitemap ─────────────────────────────────────────────────────────────────
LASTMOD = '2026-10-11'
urls = [('/', '1.0', LASTMOD),
        ('/what-we-do/', '0.9', LASTMOD),
        ('/about/', '0.7', LASTMOD),
        ('/contact/', '0.9', LASTMOD),
        ('/work/pernod-ricard/', '0.7', LASTMOD),
        ('/join-network/', '0.5', LASTMOD)]
if SHOW_INSIGHTS:
    urls.insert(2, ('/insights/', '0.8', '2026-08-20'))
    urls += [('/insights/%s/' % a['slug'], '0.6', a['iso']) for a in ARTICLES]

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, prio, lastmod in urls:
    sitemap += ['  <url>',
                '    <loc>%s%s</loc>' % (SITE, loc),
                '    <lastmod>%s</lastmod>' % lastmod,
                '    <changefreq>monthly</changefreq>',
                '    <priority>%s</priority>' % prio,
                '  </url>']
sitemap.append('</urlset>')
write('sitemap.xml', '\n'.join(sitemap) + '\n')

# ── robots.txt ──────────────────────────────────────────────────────────────
# Everything is public marketing copy, so welcome search and AI crawlers by name
# (some honour a named group over the wildcard) and point them at the sitemap.
AI_BOTS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User',
           'Claude-SearchBot', 'PerplexityBot', 'Perplexity-User', 'Google-Extended',
           'Applebot-Extended', 'CCBot']
robots = ['User-agent: *', 'Allow: /', '']
for bot in AI_BOTS:
    robots += ['User-agent: %s' % bot, 'Allow: /', '']
robots += ['Sitemap: %s/sitemap.xml' % SITE]
write('robots.txt', '\n'.join(robots) + '\n')

# ── llms.txt ────────────────────────────────────────────────────────────────
# Plain-markdown summary for LLM tools (llmstxt.org format).
write('llms.txt', f"""# Semantic

> Semantic is a boutique data consultancy that helps companies solve complex data challenges, from diagnosis to implementation. Senior data expertise, embedded in your team, with one accountable point of contact. Founded by Pierre Sarkis (formerly Amazon, HEC Paris). Serves clients in Europe, the United States and the Middle East.

## Pages

- [Home]({SITE}/): What Semantic does, how it works in four steps, and who it is for.
- [Our Expertise]({SITE}/what-we-do/): Vetted data specialists (analysts, engineers, analytics engineers, managers, governance leads), the data stack they work in, and how Semantic stays accountable for outcomes.
- [About Us]({SITE}/about/): The founder, Pierre Sarkis, and the principles behind the firm.
- [Pernod Ricard case study]({SITE}/work/pernod-ricard/): How Semantic cut data quality errors from 30% to 2.5% across 12 markets behind D-STAR, Pernod Ricard's AI sales recommendation engine, featured by Harvard Business School.
- [Contact]({SITE}/contact/): Book a free diagnosis session about a data problem.
- [Join the Network]({SITE}/join-network/): For data professionals who want to take on challenging AI and data projects with Semantic's international clients.

## Expertise

Data quality and reliability, data and AI readiness, data migration, analytics and decision support, data governance, master data management, business intelligence, data engineering.

## Optional

- [LinkedIn]({LINKEDIN}): Company page.
- [Sitemap]({SITE}/sitemap.xml)
""")
