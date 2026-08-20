# -*- coding: utf-8 -*-
from shared import ARROW, cta_band
from plates import strata
from tech import TECH_ITEMS

# The five capabilities in full. Each carries a short list of what the work
# concretely involves, so the page says what we do rather than what we believe.
CAPABILITIES = [
    ('01', 'Data Quality &amp; Reliability',
     'The data a business runs on has to be right, and it has to be right on a Monday '
     'morning without anyone checking by hand. We put testing, monitoring and incident '
     'response around the pipelines and tables that matter, and we make the results '
     'visible to the people who depend on them.',
     ['Data testing and contract enforcement',
      'Freshness, volume and schema monitoring',
      'Incident response and root-cause analysis',
      'Reconciliation between systems of record']),

    ('02', 'Data &amp; AI Readiness',
     'Most AI initiatives do not stall on the model. They stall on the data underneath '
     'it: undocumented definitions, no lineage, and no way to tell whether a training '
     'set is representative. We do the groundwork that makes an AI programme buildable, '
     'and we are direct about what is not ready yet.',
     ['Readiness assessment against a concrete use case',
      'Lineage and documentation for the data in scope',
      'Access, ownership and sensitivity mapping',
      'Feature and training data pipelines']),

    ('03', 'Data Migration',
     'Legacy system migrations and cloud warehouse adoption, delivered without losing '
     'trust in the numbers along the way. The hard part is rarely moving the data. It '
     'is proving, to people who will be held accountable for the figures, that what '
     'came out matches what went in.',
     ['Target architecture and migration sequencing',
      'Parallel running and reconciliation',
      'Model rebuild in the new platform',
      'Cutover, decommissioning and handover']),

    ('04', 'Analytics &amp; Decision Support',
     'Analytics is worth what the decisions it changes are worth. We work backwards '
     'from the decision: what is being decided, by whom, on what cadence, and what '
     'evidence would actually move it. Then we build the smallest thing that answers '
     'it well.',
     ['Decision mapping and metric definition',
      'Semantic and reporting layers',
      'Experimentation and causal analysis',
      'Self-serve analytics that teams genuinely use']),

    ('05', 'Data Management',
     'Ownership, definitions, master data and lineage that survive contact with '
     'reality. Governance fails when it is written for an audit rather than for the '
     'people doing the work, so we design it to be the path of least resistance.',
     ['Ownership and stewardship models',
      'Business glossary and metric definitions',
      'Master and reference data management',
      'Lineage, cataloguing and access control']),
]

MODEL_POINTS = [
    'We understand the problem first, in business terms, before proposing anything.',
    'We define the approach and put it in writing: the outcome, the sequence, and how we will know it worked.',
    'We bring together the right specialists for that specific problem rather than staffing whoever is free.',
    'We deliver remotely, inside your tools and your rituals, shipping in increments you can review.',
    'We stay accountable for the outcome. One team, one counterpart, from the first call onwards.',
]


def _capabilities():
    out = []
    for idx, title, body, bullets in CAPABILITIES:
        items = '\n'.join('            <li>%s</li>' % b for b in bullets)
        out.append('''      <article class="capability">
        <div class="capability-head">
          <span class="capability-index">{idx}</span>
          <h3>{title}</h3>
        </div>
        <p class="body">{body}</p>
        <ul class="capability-list">
{items}
        </ul>
      </article>'''.format(idx=idx, title=title, body=body, items=items))
    return '\n'.join(out)


WHAT_WE_DO = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>What We Do</span>
      </nav>
      <p class="eyebrow">What We Do</p>
      <div class="hero-cols">
        <div>
          <h1 class="display">Complex data problems, solved properly</h1>
        </div>
        <div>
          <p class="lede">Five areas where enterprises most often need senior help. We work
            across all of them, and we are direct when a problem is not ours to take.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- EXPERTISE -->
  <section class="section section--tight section--flush" aria-labelledby="expertise-h">
    <div class="container">
      <h2 class="visually-hidden" id="expertise-h">Our expertise</h2>
      <div class="capabilities">
{capabilities}
      </div>
    </div>
  </section>

  <!-- THE SEMANTIC MODEL -->
  <section class="section section--ink" aria-labelledby="model-h">
    <div class="container">
      <div class="section-head section-head--wide">
        <div>
          <p class="eyebrow">The Semantic Model</p>
          <h2 class="h-xl" id="model-h">Senior expertise, backed by a dedicated team</h2>
        </div>
        <div>
          <p class="body">You are not buying an individual, and you are not buying a
            pyramid. You get a senior counterpart who owns the problem, and a team behind
            them with the capacity to execute it.</p>
        </div>
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
        <p class="eyebrow">Technology</p>
        <h2 class="h-lg" id="tech-h">We have the technical depth to execute</h2>
        <p class="body">Tools follow the problem, not the other way round. This is the stack
          we build in most often.</p>
      </div>
      <ul class="tech-list">
{tech}
      </ul>
    </div>
  </section>

  <!-- SELECTED WORK -->
  <section class="section section--paper" aria-labelledby="work-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Selected Work</p>
        <h2 class="h-lg" id="work-h">What engagements look like in practice</h2>
      </div>

      <div class="split">
        <div>
          <p class="body" style="font-size:18px;color:var(--ink-soft);">We do not publish
            client case studies. The work sits inside systems and commercial decisions our
            clients would rather not see described on a website, and we would rather keep it
            that way.</p>
          <p class="body" style="margin-top:20px;">What we will do is walk you through
            comparable engagements on a call: the context, what was actually wrong, how we
            approached it, and what changed by the end. Where a client is happy to be
            referenced, we will introduce you.</p>
          <a class="link" href="/contact/" style="margin-top:28px;">Ask us about relevant work {arrow}</a>
        </div>
        <div class="note">
          <h3 class="h-md">The shape of an engagement</h3>
          <p class="body" style="margin-top:14px;">A free advisory conversation, then a
            focused diagnosis where the problem warrants one, then delivery scoped to a
            written outcome. Project-based or an ongoing retainer, depending on whether the
            problem has an end.</p>
        </div>
      </div>

      <!-- Case-study template. Fill one block per engagement, drop the copy above,
           and the section becomes a proper work page:

      <article class="capability">
        <div class="capability-head">
          <span class="capability-index">01</span>
          <h3>Client or context</h3>
        </div>
        <div>
          <p class="body"><strong>Challenge.</strong> ...</p>
          <p class="body"><strong>Approach.</strong> ...</p>
          <p class="body"><strong>Outcome.</strong> ...</p>
        </div>
      </article>
      -->
    </div>
  </section>
{cta}'''.format(
    capabilities=_capabilities(),
    plate=strata(on_forest=True),
    points='\n'.join('            <li>%s</li>' % p for p in MODEL_POINTS),
    tech=TECH_ITEMS.strip('\n'),
    arrow=ARROW,
    cta=cta_band("Have a data problem you're trying to solve?", "Let's talk about it."),
)
