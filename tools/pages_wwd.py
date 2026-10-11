# -*- coding: utf-8 -*-
from shared import cta_band
from plates import (strata, ICON_ANALYTICS, ICON_QUALITY, ICON_AI, ICON_MIGRATION)
import re
from tech import TECH_ITEMS

# Second copy for the stream: ids are suffixed so the page keeps unique ids.
TECH_COPY = re.sub(r'(SVG\w+)', r'\1b', TECH_ITEMS).strip('\n')

# The four areas, in the same order as the home page. Each carries a short list
# of what the work concretely involves.
AREAS = [
    ('analytics', ICON_ANALYTICS, 'Analytics &amp; Decision Support', 'Analytics',
     'We work backwards from the decision: who makes it, how often and on what '
     'evidence. Then we build the smallest thing that answers it well.',
     ['Decision mapping and metric definition',
      'Semantic and reporting layers',
      'Experimentation and causal analysis',
      'Self-serve analytics that teams genuinely use']),

    ('quality', ICON_QUALITY, 'Data Quality &amp; Reliability', 'Data Quality',
     'Testing, monitoring and incident response around the pipelines that matter, '
     'with the results visible to the people who depend on them.',
     ['Data testing and contract enforcement',
      'Freshness, volume and schema monitoring',
      'Incident response and root-cause analysis',
      'Reconciliation between systems of record']),

    ('ai-readiness', ICON_AI, 'Data &amp; AI Readiness', 'AI Readiness',
     'AI projects stall on the data underneath them. We do the groundwork that makes '
     'them buildable, and we are direct about what is not ready yet.',
     ['Readiness assessment against a concrete use case',
      'Lineage and documentation for the data in scope',
      'Access, ownership and sensitivity mapping',
      'Feature and training data pipelines']),

    ('migration', ICON_MIGRATION, 'Data Migration', 'Migration',
     'Legacy and cloud migrations, delivered without losing trust in the numbers. '
     'The hard part is proving that what came out matches what went in.',
     ['Target architecture and migration sequencing',
      'Parallel running and reconciliation',
      'Model rebuild in the new platform',
      'Cutover, decommissioning and handover']),
]

MODEL_POINTS = [
    'We select and vet specialists for your specific problem and tooling.',
    'We manage delivery and evaluate the work throughout.',
    'We work remotely, inside your tools and your rituals.',
    'We ensure follow-up and handover when it ends.',
]


def _areas():
    out = []
    for slug, icon, title, _short, body, bullets in AREAS:
        items = '\n'.join('            <li>%s</li>' % b for b in bullets)
        out.append('''      <article class="area" id="{slug}">
        <div class="area-head">
          {icon}
          <h3 class="h-md">{title}</h3>
        </div>
        <div>
          <p class="body">{body}</p>
          <ul class="area-list">
{items}
          </ul>
        </div>
      </article>'''.format(slug=slug, icon=icon, title=title, body=body, items=items))
    return '\n'.join(out)


def _jump():
    return '\n'.join('        <li><a class="tag" href="#%s">%s</a></li>' % (slug, short)
                     for slug, _i, _t, short, _b, _l in AREAS)


WHAT_WE_DO = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>What We Do</span>
      </nav>
      <p class="eyebrow">What We Do</p>
      <h1 class="display">Complex data challenges, solved properly</h1>
      <ul class="tags" style="margin-top:32px;">
{jump}
      </ul>
    </div>
  </section>

  <!-- AREAS -->
  <section class="section section--tight section--flush" aria-labelledby="expertise-h">
    <div class="container">
      <h2 class="visually-hidden" id="expertise-h">Our expertise</h2>
      <div class="areas">
{areas}
      </div>
    </div>
  </section>

  <!-- ONE ACCOUNTABLE POINT OF CONTACT -->
  <section class="section section--ink" aria-labelledby="model-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="model-h">One accountable point of contact</h2>
      </div>

      <div class="with-plate">
        <ul class="points">
{points}
        </ul>
        <div class="plate-slot">{plate}</div>
      </div>
    </div>
  </section>

  <!-- TECHNOLOGIES -->
  <section class="section" aria-labelledby="tech-h">
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
    jump=_jump(),
    areas=_areas(),
    plate=strata(on_forest=True),
    points='\n'.join('            <li>%s</li>' % p for p in MODEL_POINTS),
    tech=TECH_ITEMS.strip('\n'),
    tech_copy=TECH_COPY,
    cta=cta_band('Discuss your data challenge with us', 'Book a free diagnosis session.',
                 label='Book a free diagnosis session'),
)
