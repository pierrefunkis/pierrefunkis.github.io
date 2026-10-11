# -*- coding: utf-8 -*-
from shared import ARROW, cta_band
from plates import (CONVERGENCE, ICON_QUALITY, ICON_AI, ICON_MIGRATION, ICON_ANALYTICS,
                    ICON_TALK, ICON_DIAGNOSE, ICON_BUILD, ICON_IMPROVE)

CLIENT_STRIP = '''
  <section class="clients" aria-labelledby="clients-h">
    <div class="container">
      <p class="clients-label" id="clients-h">Trusted by data teams around the world</p>
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
    (ICON_QUALITY, 'Data Quality &amp; Reliability',
     'Testing, monitoring and incident response, so the numbers you run the business on '
     'can be trusted.'),
    (ICON_AI, 'Data &amp; AI Readiness',
     'The quality, lineage and ownership foundations that take AI from pilot to '
     'production.'),
    (ICON_MIGRATION, 'Data Migration',
     'Legacy and cloud migrations, delivered without losing trust in the numbers.'),
    (ICON_ANALYTICS, 'Analytics &amp; Decision Support',
     'Analytics built around the decisions it informs, not dashboards nobody uses.'),
]

STEPS = [
    (ICON_TALK, '01', 'Talk',
     'A conversation about the business, the data challenge behind it and the outcome you want.'),
    (ICON_DIAGNOSE, '02', 'Diagnose',
     'We examine the real systems and data, then recommend root causes, priorities and an approach.'),
    (ICON_BUILD, '03', 'Build',
     'We assemble the right specialists and deliver in increments you can review.'),
    (ICON_IMPROVE, '04', 'Improve',
     'Where useful, we stay on to raise the standard and hand the capability to your team.'),
]


def _capability_cells(items):
    out = []
    for icon, title, body in items:
        out.append('''        <div class="cell">
          {icon}
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(icon=icon, title=title, body=body))
    return '\n'.join(out)


def _steps(items):
    out = []
    for icon, num, title, body in items:
        out.append('''        <div class="step">
          {icon}
          <div class="step-num">{num}</div>
          <h3>{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(icon=icon, num=num, title=title, body=body))
    return '\n'.join(out)


HOME = '''
  <!-- HERO -->
  <section class="hero">
    <div class="container with-plate">
      <div>
        <h1 class="display">Senior data expertise, delivered by a dedicated team.</h1>
        <div class="hero-body">
          <p class="lede">We help companies solve complex data challenges, from
            diagnosis to implementation.</p>
          <div class="actions">
            <a class="btn btn--primary" href="/contact/">Book a free diagnosis session {arrow}</a>
            <a class="btn btn--ghost" href="/what-we-do/">See what we do</a>
          </div>
        </div>
      </div>
      <div class="plate-slot">{plate}</div>
    </div>
  </section>
{clients}
  <!-- WHAT WE DO -->
  <section class="section" aria-labelledby="wwd-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">What We Do</p>
        <h2 class="h-xl" id="wwd-h">How we help</h2>
      </div>

      <div class="grid grid--4">
{capabilities}
      </div>
    </div>
  </section>

  <!-- HOW WE WORK -->
  <section class="section section--ruled" aria-labelledby="how-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">How We Work</p>
        <h2 class="h-xl" id="how-h">Four steps from problem to outcome</h2>
      </div>
      <div class="steps">
{steps}
      </div>
    </div>
  </section>
{cta}'''.format(
    arrow=ARROW,
    plate=CONVERGENCE,
    clients=CLIENT_STRIP,
    capabilities=_capability_cells(HOME_CAPABILITIES),
    steps=_steps(STEPS),
    cta=cta_band('Discuss your data challenge with us', 'Book a free diagnosis session.',
             label='Book a free diagnosis session'),
)
