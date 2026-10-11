# -*- coding: utf-8 -*-
from shared import ARROW, cta_band
from plates import (expertise_umbrella, ICON_W_VETTED, ICON_W_MANAGED, ICON_W_EMBEDDED,
                    ICON_W_HANDOVER, ICON_T_ANALYTICS, ICON_T_ENGINEERING,
                    ICON_T_ANALYTICS_ENG, ICON_T_MANAGEMENT, ICON_T_PRODUCT,
                    ICON_T_GOVERNANCE)
import re
from tech import TECH_ITEMS

# Second copy for the stream: ids are suffixed so the page keeps unique ids.
TECH_COPY = re.sub(r'(SVG\w+)', r'\1b', TECH_ITEMS).strip('\n')

WAYS = [
    (ICON_W_VETTED, 'Vetted',
     'We select and vet specialists for your specific problem and tooling.'),
    (ICON_W_MANAGED, 'Managed',
     'We manage delivery and evaluate the work throughout.'),
    (ICON_W_EMBEDDED, 'Embedded',
     'We work remotely, inside your tools and your rituals.'),
    (ICON_W_HANDOVER, 'Handed over',
     'We ensure follow-up and handover when it ends.'),
]

# The specialists we staff, in the order they appear on the page.
SPECIALISTS = [
    (ICON_T_ANALYTICS, 'Data Analysts',
     'Turn business questions into metrics, dashboards and decisions.',
     'Looker, Power BI, Tableau, Metabase'),
    (ICON_T_ENGINEERING, 'Data Engineers',
     'Build and run the pipelines and platforms the data moves through.',
     'Snowflake, Databricks, Airflow, Spark, Kafka'),
    (ICON_T_ANALYTICS_ENG, 'Analytics Engineers',
     'Model trusted, documented datasets and the semantic layer on top of them.',
     'dbt, Snowflake, Looker'),
    (ICON_T_MANAGEMENT, 'Data Managers',
     'Own the data estate: definitions, ownership, access and day-to-day quality.',
     None),
    (ICON_T_PRODUCT, 'Data Product Managers',
     'Frame the problem, define the outcome and keep delivery pointed at it.',
     None),
    (ICON_T_GOVERNANCE, 'Data Governance Managers',
     'Set up the ownership, policies and controls that people actually follow.',
     None),
]


def _ways():
    return '\n'.join('''        <div class="cell">
          {icon}
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(icon=i, title=t, body=b) for i, t, b in WAYS)


def _specialists():
    out = []
    for icon, title, body, tools in SPECIALISTS:
        meta = ('<br><span class="cell-meta">%s</span>' % tools) if tools else ''
        out.append('''        <div class="cell">
          {icon}
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}{meta}</p>
        </div>'''.format(icon=icon, title=title, body=body, meta=meta))
    return '\n'.join(out)


WHAT_WE_DO = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Our Expertise</span>
      </nav>
      <div class="with-plate">
        <div>
          <h1 class="display">One accountable point of contact</h1>
          <p class="lede" style="margin-top:24px;text-wrap:balance;">We select, manage and stand behind every
            data specialist we place.</p>
        </div>
        <div class="plate-slot">{plate}</div>
      </div>
      <div class="grid grid--4" style="margin-top:48px;">
{ways}
      </div>
    </div>
  </section>

  <!-- THE SPECIALISTS -->
  <section class="section" aria-labelledby="specialists-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="specialists-h">Vetted specialists, matched to your needs</h2>
      </div>
      <div class="grid grid--3">
{specialists}
      </div>
      <a class="link" href="/join-network/" style="margin-top:36px;">Join our network of data professionals {arrow}</a>
    </div>
  </section>

  <!-- TECHNOLOGIES -->
  <section class="section section--paper" aria-labelledby="tech-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-lg" id="tech-h">Specialists for your data stack</h2>
        <p class="body">Hands-on expertise across modern data platforms and tools.</p>
      </div>
      <div class="marquee">
        <div class="marquee-track">
          <ul class="tech-list">
{tech}
          </ul>
          <ul class="tech-list" aria-hidden="true">
{tech_copy}
          </ul>
        </div>
      </div>
    </div>
  </section>
{cta}'''.format(
    plate=expertise_umbrella(),
    ways=_ways(),
    specialists=_specialists(),
    arrow=ARROW,
    tech=TECH_ITEMS.strip('\n'),
    tech_copy=TECH_COPY,
    cta=cta_band('Discuss your data challenge with us', 'Book a free diagnosis session.',
                 label='Book a free diagnosis session'),
)
