# -*- coding: utf-8 -*-
from shared import ARROW, LINKEDIN, cta_band
from plates import CONSTELLATION

TEAM_AREAS = [
    ('Data product', 'Framing the problem, defining the outcome, and keeping delivery pointed at it.'),
    ('Analytics', 'Metric definitions, semantic layers, experimentation and the reporting people actually use.'),
    ('Data engineering', 'Pipelines, modelling and platform work in the client stack.'),
    ('Data quality', 'Testing, monitoring, reconciliation and incident response.'),
    ('Data management', 'Ownership, glossaries, master data, lineage and access.'),
]

ABOUT = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>About</span>
      </nav>
      <p class="eyebrow">About</p>
      <div class="hero-cols">
        <div>
          <h1 class="display">Who is behind Semantic</h1>
        </div>
        <div>
          <p class="lede">A boutique data consultancy: senior expertise you speak to directly,
            with the execution capacity of a dedicated team behind it.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FOUNDER -->
  <section class="section section--tight section--flush" aria-labelledby="founder-h">
    <div class="container">
      <div class="founder">
        <img class="founder-photo" id="founderPhoto" src="/pierre-sarkis.jpeg"
             alt="Pierre Sarkis, founder of Semantic" width="576" height="576"
             data-monogram="PS" loading="lazy" decoding="async">
        <div>
          <h2 class="h-lg" id="founder-h">Pierre Sarkis</h2>
          <p class="founder-role">Founder &amp; Principal</p>

          <p class="body" style="font-size:18px;color:var(--ink-soft);">Pierre spent his
            career in data at Amazon, working across the US and Europe at the kind of scale
            where unreliable data is not an inconvenience but an operational risk. He founded
            Semantic to bring that standard to companies that want to be genuinely
            data-driven without hiring an army to get there.</p>

          <p class="body" style="margin-top:20px;">A graduate of HEC Paris, he combines a
            technical data background with business management training. That mix shapes how
            Semantic works: technical decisions are made in business terms, and business
            decisions are made with data that holds up.</p>

          <p class="body" style="margin-top:20px;">Since founding Semantic he has worked with
            data teams at companies including Pernod Ricard and Back Market, across Europe,
            the US and the Middle East. He is the counterpart on every engagement, and the
            person you speak to first.</p>

          <dl class="facts facts--pair" style="margin-top:36px;">
            <div class="fact"><dt>Previously</dt><dd><img class="fact-mark" src="/logos/amazon.svg" alt="Amazon" width="24" height="22" decoding="async"></dd></div>
            <div class="fact"><dt>Educated at</dt><dd><span class="fact-word">HEC Paris</span></dd></div>
          </dl>

          <a class="link" href="{linkedin}" rel="noopener" style="margin-top:28px;">Connect on LinkedIn {arrow}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- WHY SEMANTIC -->
  <section class="section section--mint" aria-labelledby="why-h">
    <div class="container">
      <div class="section-head section-head--wide">
        <div>
          <p class="eyebrow">Why Semantic</p>
          <h2 class="h-xl" id="why-h">A third option</h2>
        </div>
        <div>
          <p class="body" style="font-size:18px;color:var(--ink-soft);">Companies rarely have
            a data problem in the abstract. They have a specific, expensive one: a number two
            teams calculate differently, a pipeline nobody trusts before a board meeting, an
            AI initiative stalled because the data underneath it will not hold weight.</p>
        </div>
      </div>

      <div class="with-plate--lead with-plate">
        <div class="plate-slot">{plate_why}</div>
        <div>
          <p class="body">Large consulting organisations bring real
            capacity and a wide bench, but the senior person who scoped the work is not
            usually the one doing it. Freelance marketplaces bring capable individuals, but
            no structure behind them and no cover when one moves on. Both models work for
            some problems.</p>

          <p class="body" style="margin-top:20px;">Semantic exists for the problems in
            between: complex enough to need real senior judgement, and substantial enough to
            need a team that can execute. The person who understands your problem is the
            person accountable for solving it, and there is a dedicated team behind them
            with the capacity to deliver it properly.</p>

        </div>
      </div>

      <ul class="points points--2up" style="margin-top:48px;">
        <li>Senior-led. The people who scope the work are involved in doing it.</li>
        <li>Embedded, not adjacent. We work in your tools, your stack and your rituals.</li>
        <li>A counterpart who challenges you, including when the answer is that you do not need us.</li>
        <li>Accountable for the outcome, with regular service reviews and continuity we own rather than pass to you.</li>
      </ul>
    </div>
  </section>

  <!-- THE TEAM -->
  <section class="section" aria-labelledby="team-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">The Team</p>
        <h2 class="h-xl" id="team-h">A curated team, assembled around the problem</h2>
        <p class="body">Semantic works with a vetted team of data specialists rather than a
          bench to be filled. Who joins an engagement depends on what the diagnosis found,
          and the specialists work alongside a senior lead rather than being handed the
          problem.</p>
      </div>

      <div class="capabilities capabilities--2up">
{areas}
      </div>

      <div class="note" style="margin-top:56px;">
        <h3 class="h-md">Working with us as a specialist</h3>
        <p class="body" style="margin-top:14px;">We take on experienced data professionals
          and exceptional earlier-career specialists, always paired with a senior lead.</p>
        <a class="link" href="/for-talents/" style="margin-top:20px;">Join the team {arrow}</a>
      </div>
    </div>
  </section>
{cta}'''

def _areas():
    out = []
    for i, (title, body) in enumerate(TEAM_AREAS, start=1):
        out.append('''      <div class="capability">
        <div class="capability-head">
          <span class="capability-index">{idx:02d}</span>
          <h3>{title}</h3>
        </div>
        <p class="body">{body}</p>
      </div>'''.format(idx=i, title=title, body=body))
    return '\n'.join(out)


ABOUT = ABOUT.format(
    linkedin=LINKEDIN,
    plate_why=CONSTELLATION,
    arrow=ARROW,
    areas=_areas(),
    cta=cta_band("Have a data problem you're trying to solve?", "Let's talk about it."),
)
