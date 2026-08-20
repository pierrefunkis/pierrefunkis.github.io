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

from shared import SITE, EMAIL, LINKEDIN, ORG_LD, head, nav, FOOTER  # noqa: E402
from pages_home import HOME  # noqa: E402
from pages_wwd import WHAT_WE_DO  # noqa: E402
from pages_about import ABOUT  # noqa: E402
from pages_contact import CONTACT  # noqa: E402
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
         'name': 'Senior Data Expertise for Enterprises | Semantic',
         'description': 'Semantic is a boutique data consultancy that helps enterprises '
                        'solve complex data problems, from diagnosis to implementation.',
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#organization'},
         'inLanguage': 'en'},
        {'@type': 'Service', 'serviceType': 'Data consulting',
         'provider': {'@id': SITE + '/#organization'},
         'name': 'Enterprise data consulting',
         'description': 'Senior data expertise delivered by a dedicated team, from diagnosis '
                        'through implementation.',
         'hasOfferCatalog': {
             '@type': 'OfferCatalog', 'name': 'What we do',
             'itemListElement': [
                 {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n}}
                 for n in ['Data Quality & Reliability', 'Data & AI Readiness',
                           'Data Migration', 'Analytics & Decision Support',
                           'Data Management']]}},
    ],
}, indent=2)

PAGES.append((
    'index.html', '/',
    'Senior Data Expertise for Enterprises | Semantic',
    'Semantic is a boutique data consultancy. We help enterprises solve complex data '
    'problems, from diagnosis to implementation.',
    'Senior data expertise, delivered by a dedicated team | Semantic',
    'Semantic helps enterprises solve complex data problems, from diagnosis to '
    'implementation.',
    home_ld, HOME,
))

# ── What We Do ──────────────────────────────────────────────────────────────
PAGES.append((
    'what-we-do/index.html', '/what-we-do/',
    'What We Do: Enterprise Data Capabilities | Semantic',
    'Data quality and reliability, AI readiness, migration, analytics and data '
    'management, delivered by a senior-led team that stays accountable for the outcome.',
    None, None,
    webpage_ld('/what-we-do/', 'What We Do | Semantic',
               'The full set of Semantic capabilities, the technology we build in, and how '
               'engagements are run.'),
    WHAT_WE_DO,
))

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
    'Notes from inside enterprise data work: quality that does not hold, AI programmes '
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

# ── Careers ─────────────────────────────────────────────────────────────────
PAGES.append((
    'for-talents/index.html', '/for-talents/',
    'Careers at Semantic | Data Specialists',
    'Semantic works with a curated team of data specialists on demanding enterprise '
    'problems, with training, certifications and conferences funded.',
    None, None,
    webpage_ld('/for-talents/', 'Careers | Semantic',
               'Join a curated team of data specialists working on demanding enterprise '
               'problems.'),
    CAREERS,
))


for filename, path, title, desc, og_t, og_d, ld, body in PAGES:
    active = path if any(path == href for href, _ in
                         [('/what-we-do/', 1), ('/insights/', 1), ('/about/', 1)]) else ''
    # Article pages keep Insights marked as the current section.
    if path.startswith('/insights/'):
        active = '/insights/'
    write(filename, head(title, desc, path, og_t, og_d, ld) + nav(active) + body + FOOTER)

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
urls = [('/', '1.0', '2026-08-20'),
        ('/what-we-do/', '0.9', '2026-08-20'),
        ('/insights/', '0.8', '2026-08-20'),
        ('/about/', '0.7', '2026-08-20'),
        ('/contact/', '0.9', '2026-08-20'),
        ('/for-talents/', '0.5', '2026-08-20')]
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
