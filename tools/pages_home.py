# -*- coding: utf-8 -*-
from shared import ARROW, cta_band
from figure import HERO_FIGURE

CLIENT_STRIP = '''
  <section class="clients" aria-labelledby="clients-h">
    <div class="container">
      <p class="clients-label" id="clients-h">Trusted by data teams in Europe, the US and the Middle East</p>
      <ul class="client-logos">
        <!-- Optically balanced, not mathematically. See logos/README.md. -->
        <li><img class="client-logo client-logo--tall" src="/logos/pernod-ricard.svg" alt="Pernod Ricard" width="1024" height="377" loading="lazy" decoding="async"></li>
        <li><img class="client-logo client-logo--wide" src="/logos/back-market.svg" alt="Back Market" width="1500" height="169" loading="lazy" decoding="async"></li>
        <li><img class="client-logo" src="/logos/pawp.svg" alt="Pawp" width="112" height="30" loading="lazy" decoding="async"></li>
        <li><img class="client-logo client-logo--dense" src="/logos/med-surg-solutions.png" alt="Med Surg Solutions" width="1804" height="670" loading="lazy" decoding="async"></li>
        <li><img class="client-logo client-logo--light" src="/logos/shelt.png" alt="Shelt" width="1291" height="380" loading="lazy" decoding="async"></li>
      </ul>
    </div>
  </section>
'''

# Four of the five capabilities. The fifth, data management, lives on What We Do
# so the home page stays an introduction rather than a catalogue.
HOME_CAPABILITIES = [
    ('01', 'Data Quality &amp; Reliability',
     'Testing, monitoring and incident response for the data the business actually '
     'runs on, so the numbers stop being a matter of opinion.'),
    ('02', 'Data &amp; AI Readiness',
     'The quality, lineage and ownership groundwork that separates AI initiatives '
     'that ship from AI initiatives that stall in proof of concept.'),
    ('03', 'Data Migration',
     'Legacy system migrations and cloud warehouse adoption, delivered without '
     'losing trust in the numbers along the way.'),
    ('04', 'Analytics &amp; Decision Support',
     'Analytics built around the decisions it informs. Hypotheses, experiments and '
     'causal analysis, rather than dashboards nobody acts on.'),
]

STEPS = [
    ('01', 'Talk', 'A conversation about the business, the data problem behind it, and what a good outcome would actually look like.'),
    ('02', 'Diagnose', 'We look at the real systems and data, not the org chart, and come back with root causes, priorities and a recommended approach.'),
    ('03', 'Build', 'We bring together the right specialists for the problem and execute, shipping in increments you can review.'),
    ('04', 'Improve', 'Where it is useful, we stay on to keep raising the standard and hand the capability over to your team.'),
]


def _capability_rows(items):
    out = []
    for idx, title, body in items:
        out.append('''      <article class="capability">
        <div class="capability-index">{idx}</div>
        <div><h3>{title}</h3></div>
        <div><p class="body">{body}</p></div>
      </article>'''.format(idx=idx, title=title, body=body))
    return '\n'.join(out)


def _steps(items, ink=False):
    out = []
    for num, title, body in items:
        out.append('''        <div class="step">
          <div class="step-num">{num}</div>
          <h3>{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(num=num, title=title, body=body))
    return '\n'.join(out)


HOME = '''
  <!-- HERO -->
  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="hero-brand">Semantic</p>
        <h1 class="display">Senior data expertise, delivered by a dedicated team.</h1>
        <p class="lede">Semantic helps enterprises solve complex data problems,
          from diagnosis to implementation.</p>
        <div class="actions">
          <a class="btn btn--primary" href="/contact/">Book a free diagnosis session {arrow}</a>
          <a class="btn btn--ghost" href="/what-we-do/">Explore our expertise</a>
        </div>
        <p class="hero-note">A boutique data consultancy working with enterprise data teams</p>
      </div>

      <div class="figure">
        {figure}
        <p class="figure-caption">Sources are checked against rules before anything
          reaches a decision. The point of monitoring is that it catches things.</p>
      </div>
    </div>
  </section>
{clients}
  <!-- WHAT WE DO -->
  <section class="section" aria-labelledby="wwd-h">
    <div class="container">
      <div class="section-head section-head--split">
        <div>
          <p class="eyebrow">What We Do</p>
          <h2 class="h-xl" id="wwd-h">Where enterprises most often need senior help</h2>
        </div>
        <a class="link" href="/what-we-do/">Explore our expertise {arrow}</a>
      </div>

      <div class="capabilities">
{capabilities}
      </div>
    </div>
  </section>

  <!-- CREDIBILITY -->
  <section class="section section--paper" aria-labelledby="cred-h">
    <div class="container">
      <div class="split">
        <div>
          <p class="eyebrow">Credibility</p>
          <h2 class="h-lg" id="cred-h">Backed by serious enterprise experience</h2>
        </div>
        <div>
          <p class="body" style="font-size:18px;color:var(--ink-soft);">Semantic was founded
            by Pierre Sarkis, who spent his career in data at Amazon across the US and Europe,
            at the kind of scale where unreliable data is an operational risk rather than an
            inconvenience. Since then Semantic has worked with data teams at companies
            including Pernod Ricard and Back Market.</p>
          <dl class="facts" style="margin-top:40px;">
            <div class="fact"><dt>Founder</dt><dd>Pierre Sarkis, ex-Amazon</dd></div>
            <div class="fact"><dt>Education</dt><dd>HEC Paris</dd></div>
            <div class="fact"><dt>Working across</dt><dd>Europe, US, Middle East</dd></div>
          </dl>
          <a class="link" href="/about/" style="margin-top:32px;">Who is behind Semantic {arrow}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW WE WORK -->
  <section class="section section--ruled" aria-labelledby="how-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">How We Work</p>
        <h2 class="h-xl" id="how-h">Four steps, and we are honest at each one</h2>
        <p class="body">Every engagement starts the same way: a conversation, then a
          diagnosis. If the answer is that you do not need us for this, we say so.</p>
      </div>
      <div class="steps">
{steps}
      </div>
    </div>
  </section>
{cta}'''.format(
    arrow=ARROW,
    figure=HERO_FIGURE,
    clients=CLIENT_STRIP,
    capabilities=_capability_rows(HOME_CAPABILITIES),
    steps=_steps(STEPS),
    cta=cta_band("Have a data problem you're trying to solve?", "Let's talk about it."),
)
