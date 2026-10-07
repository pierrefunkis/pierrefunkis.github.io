# -*- coding: utf-8 -*-
"""Careers page.

Lives at /join-network/ (formerly /for-talents/, which now redirects here).
It sits in the footer rather than the main nav, because the main nav
is for clients.
"""
from shared import ARROW, cta_band
from pages_home import CLIENT_STRIP
from plates import NETWORK, ICON_PROBLEM, ICON_GLOBAL, ICON_PAY

BENEFITS = [
    (ICON_PROBLEM, 'Genuinely challenging data problems',
     'We are embedded in our clients\' teams and step in on their most critical AI and '
     'data projects.'),
    (ICON_GLOBAL, 'An international client portfolio',
     'Engagements with companies across industries and across Europe, the US and the '
     'Middle East, from global consumer brands to healthcare to fast-growing marketplaces.'),
    (ICON_PAY, 'Competitive compensation',
     'We believe talent should be compensated fairly, and we do our best to match or exceed '
     'your expectations.'),
]

ROLES = [
    'Data Engineers', 'Analytics Engineers', 'Data Scientists', 'Data Analysts',
    'ML Engineers', 'Data Governance Managers',
    'BI Developers &amp; Analysts', 'AI &amp; Automation Experts',
    'Data Project Managers', 'Data Product Managers',
]

JOIN = 'https://tally.so/r/5Byl5P'

CAREERS = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Join Network</span>
      </nav>
      <div class="with-plate">
        <div>
          <h1 class="display">Work on data problems worth solving</h1>
          <p class="lede" style="margin-top:24px;">Semantic is a data consulting company
            operating from Lebanon and serving international clients. We work with a curated
            network of data specialists on demanding enterprise problems.</p>
          <div class="actions">
            <a class="btn btn--primary" href="{join}" rel="noopener">Join Network {arrow}</a>
          </div>
        </div>
        <div class="plate-slot">{plate}</div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--flush" aria-labelledby="why-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Why Semantic</p>
        <h2 class="h-xl" id="why-h">A team worth joining</h2>
      </div>
      <div class="grid grid--3">
{benefits}
      </div>
    </div>
  </section>
{clients}
  <section class="section section--mint" aria-labelledby="roles-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Who We Look For</p>
        <h2 class="h-lg" id="roles-h">Specialists across the data stack</h2>
        <p class="body">We work with experienced data professionals, technical and
          non-technical alike, from engineers and architects to project and product
          managers, with strong foundations and a track record of delivery.</p>
      </div>

      <ul class="tags">
{roles}
      </ul>
    </div>
  </section>
{cta}'''


def _benefits():
    out = []
    for icon, title, body in BENEFITS:
        out.append('''        <div class="cell">
          {icon}
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(icon=icon, title=title, body=body))
    return '\n'.join(out)


CAREERS = CAREERS.format(
    join=JOIN,
    arrow=ARROW,
    plate=NETWORK,
    benefits=_benefits(),
    clients=CLIENT_STRIP,
    roles='\n'.join('            <li class="tag">%s</li>' % r for r in ROLES),
    cta=cta_band('Think you would raise our bar?',
                 'Simply fill our 2 min form and we\'ll reach out when we have opportunities for you.',
                 label='Join Network', href=JOIN),
)

NOT_FOUND = '''
  <section class="hero hero--page">
    <div class="container">
      <p class="eyebrow">404</p>
      <div class="hero-cols">
        <div>
          <h1 class="display">That page is not here</h1>
        </div>
        <div>
          <p class="lede">The link may be out of date, or the page may have moved. These are
            the ones that exist.</p>
        </div>
      </div>
      <div class="actions">
        <a class="btn btn--primary" href="/">Back to home {arrow}</a>
        <a class="btn btn--ghost" href="/contact/">Get in touch</a>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0;">
    <div class="container">
      <div class="capabilities">
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">01</span>
            <h3><a href="/what-we-do/" style="text-decoration:none;">What We Do</a></h3>
          </div>
          <p class="body">The full set of Semantic capabilities, the technology we build
            in, and how engagements are run.</p>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">02</span>
            <h3><a href="/insights/" style="text-decoration:none;">Insights</a></h3>
          </div>
          <p class="body">Short pieces on data quality, AI readiness and migration.</p>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">03</span>
            <h3><a href="/about/" style="text-decoration:none;">About</a></h3>
          </div>
          <p class="body">Who is behind Semantic, why it exists, and how the team
            works.</p>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">04</span>
            <h3><a href="/contact/" style="text-decoration:none;">Contact</a></h3>
          </div>
          <p class="body">Book a free advisory conversation about the problem you are
            trying to solve.</p>
        </div>
      </div>
    </div>
  </section>
'''.format(arrow=ARROW)
