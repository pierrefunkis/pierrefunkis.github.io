# -*- coding: utf-8 -*-
"""Careers page.

Kept at /for-talents/ so existing inbound links keep working; only the label
changed. It sits in the footer rather than the main nav, because the main nav
is for clients.
"""
from shared import ARROW, EMAIL, cta_band

BENEFITS = [
    ('Genuinely challenging problems',
     'The critical data challenges companies could not solve with their own teams. '
     'No ticket queues, no busywork, no maintenance duty disguised as a project.'),
    ('An international client portfolio',
     'Engagements with companies across industries and across Europe, the US and the '
     'Middle East, from global consumer brands to healthcare to fast-growing marketplaces.'),
    ('A senior peer group',
     'You will work with specialists who have built this before. The fastest way to get '
     'better at this is to be surrounded by people already better than you.'),
    ('Certifications, funded',
     'Snowflake, dbt, Databricks, AWS, GCP and Azure. We pay for the training and the '
     'exam, and we give you the time to prepare properly.'),
    ('Conferences and community',
     'An annual budget for the conferences that matter in your field, with encouragement '
     'to speak and write, not just attend.'),
    ('Mentorship and progression',
     'Every engagement is senior-led. Earlier-career specialists work alongside a senior '
     'lead from day one, with a defined path from supporting delivery to owning it.'),
]

ROLES = [
    'Data Engineers', 'Analytics Engineers', 'Data Scientists', 'Data Analysts',
    'ML Engineers', 'Data Architects', 'Data Quality &amp; Governance Specialists',
    'MDM Specialists', 'BI Developers &amp; Analysts', 'AI &amp; Automation Experts',
    'Data Project Managers',
]

APPLY = 'mailto:%s?subject=%s' % (EMAIL, 'Application%20to%20join%20Semantic')

CAREERS = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Careers</span>
      </nav>
      <p class="eyebrow">Careers</p>
      <div class="hero-cols">
        <div>
          <h1 class="display">Work on data problems worth solving</h1>
        </div>
        <div>
          <p class="lede">Semantic works with a curated team of data specialists on demanding
            enterprise problems. Training, certifications and conferences are funded as part of
            the job, not treated as a perk you have to justify.</p>
        </div>
      </div>
      <div class="actions">
        <a class="btn btn--primary" href="{apply}">Apply to join {arrow}</a>
        <a class="btn btn--ghost" href="/what-we-do/">See the work</a>
      </div>
    </div>
  </section>

  <section class="section section--tight section--flush" aria-labelledby="why-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Why Semantic</p>
        <h2 class="h-xl" id="why-h">A team worth joining</h2>
        <p class="body">Small team, high bar, real work.</p>
      </div>
      <div class="grid grid--3">
{benefits}
      </div>
    </div>
  </section>

  <section class="section section--mint" aria-labelledby="roles-h">
    <div class="container">
      <div class="split">
        <div>
          <p class="eyebrow">Who We Look For</p>
          <h2 class="h-lg" id="roles-h">Specialists across the data stack</h2>
        </div>
        <div>
          <p class="body" style="font-size:18px;color:var(--ink-soft);">We take on
            experienced data professionals with strong technical foundations and a track
            record of shipping. We also take on exceptional earlier-career specialists,
            always paired with a senior lead and never staffed alone on a client
            engagement.</p>
          <ul class="tags" style="margin-top:32px;">
{roles}
          </ul>
        </div>
      </div>
    </div>
  </section>
{cta}'''


def _benefits():
    out = []
    for title, body in BENEFITS:
        out.append('''        <div class="cell">
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(title=title, body=body))
    return '\n'.join(out)


CAREERS = CAREERS.format(
    apply=APPLY,
    arrow=ARROW,
    benefits=_benefits(),
    roles='\n'.join('            <li class="tag">%s</li>' % r for r in ROLES),
    cta=cta_band('Think you would raise our bar?',
                 'Send us your background and the problems you want to be working on. We read every application.',
                 label='Apply to join', href=APPLY),
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
        <a class="btn btn--ghost" href="/contact/">Talk to Pierre</a>
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
          <div><p class="body">The full set of Semantic capabilities, the technology we build
            in, and how engagements are run.</p></div>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">02</span>
            <h3><a href="/insights/" style="text-decoration:none;">Insights</a></h3>
          </div>
          <div><p class="body">Short pieces on data quality, AI readiness and migration.</p></div>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">03</span>
            <h3><a href="/about/" style="text-decoration:none;">About</a></h3>
          </div>
          <div><p class="body">Who is behind Semantic, why it exists, and how the team
            works.</p></div>
        </div>
        <div class="capability">
          <div class="capability-head">
            <span class="capability-index">04</span>
            <h3><a href="/contact/" style="text-decoration:none;">Talk to Pierre</a></h3>
          </div>
          <div><p class="body">Book a free advisory conversation about the problem you are
            trying to solve.</p></div>
        </div>
      </div>
    </div>
  </section>
'''.format(arrow=ARROW)
