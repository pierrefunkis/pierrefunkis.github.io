# -*- coding: utf-8 -*-
from shared import ARROW, cta_band

HBS_URL = 'https://www.library.hbs.edu/working-knowledge/how-pernod-ricard-stirred-up-employee-enthusiasm-for-ai'

PERNOD = '''
  <div class="case">
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Pernod Ricard</span>
      </nav>
      <p class="eyebrow">Case study</p>
      <h1 class="display" style="max-width:none;">Making Pernod Ricard's AI sales engine trustworthy</h1>
      <p class="lede">Semantic built the data quality foundations of D-STAR, the in-house AI
        recommendation engine that Harvard Business School later featured as a model of
        successful AI adoption.</p>
    </div>
  </section>

  <section class="section section--tight section--flush section--compact" aria-labelledby="glance-h">
    <div class="container">
      <h2 class="h-xl" id="glance-h">At a glance</h2>
      <div class="grid grid--3" style="margin-top:28px;">
        <div class="cell cell--text"><h3 class="h-md">Client</h3>
          <p class="body">Pernod Ricard, the world's second-largest spirits company, active in
            more than 70 countries.</p></div>
        <div class="cell cell--text"><h3 class="h-md">Engagement</h3>
          <p class="body">15 months alongside Pernod Ricard's internal AI team, across 12
            markets worldwide.</p></div>
        <div class="cell cell--text cell--accent"><h3 class="h-md">Semantic's focus</h3>
          <p class="body">Data quality, built on dbt, Snowflake and the Elementary dbt
            package.</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="challenge-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="challenge-h">The challenge</h2>
      </div>
      <p class="body">D-STAR uses machine learning to optimise sales representatives' store
        visits and product recommendations. Sales teams had built their results on local
        expertise and intuition, and many were skeptical of a tool they had not asked for.</p>
      <p class="body" style="margin-top:20px;">A recommendation engine earns trust only if its
        outputs are right. One bad suggestion from bad data is enough for a representative to
        stop listening, so the quality of the data behind D-STAR was a precondition for
        adoption, not a technical detail.</p>
    </div>
  </section>

  <section class="section section--mint" aria-labelledby="results-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="results-h">Global impact</h2>
        <p class="body">Measured across 12 markets.</p>
      </div>
      <div class="grid grid--3">
        <div class="cell cell--accent"><h3 class="h-md">30% &rarr; 2.5%</h3>
          <p class="body">Data quality errors, after Semantic designed and scaled the
            resolution process.</p></div>
        <div class="cell cell--text cell--stat"><h3 class="h-md">28 &rarr; 4 days</h3>
          <p class="body">Average time to resolve a data quality issue.</p></div>
        <div class="cell cell--text cell--stat"><h3 class="h-md">6,000+ dbt tests</h3>
          <p class="body">Implemented to detect errors automatically and make the data
            more reliable.</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="impact-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="impact-h">What Semantic did</h2>
        <p class="body">We worked in dbt and Snowflake, using the Elementary dbt package to
          monitor data quality checks, and set up the ownership and process around them.</p>
      </div>
      <ul class="points">
        <li><span><strong>Clear ownership.</strong> One IT owner and one business owner for
          each data field in every market.</span></li>
        <li><span><strong>Standardized checks.</strong> A documented set of checks, with clear
          instructions to create, maintain and resolve them.</span></li>
        <li><span><strong>Trained owners.</strong> Training sessions so owners can use the
          Elementary dashboards and the data quality playbook to resolve issues.</span></li>
        <li><span><strong>Monitoring over time.</strong> Tracking of resolution trends to
          spot bottlenecks and keep improving data quality metrics.</span></li>
      </ul>
    </div>
  </section>

  <section class="section" aria-labelledby="hbs-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="hbs-h">Recognised by Harvard Business School</h2>
      </div>
      <img class="hbs-logo" src="/logos/HBS-styleguide-primary-logo-3.png" alt="Harvard Business School" width="2000" height="990" loading="lazy" decoding="async">
      <p class="body">Harvard Business School professors Iavor Bojinov and Edward McFowland III
        wrote a case study on Pernod Ricard's digital transformation, covered in HBS
        <em>Working Knowledge</em> on November 21, 2025. They found the company had done
        &ldquo;a fairly good job, better than some tech companies&rdquo; at getting employees
        to adopt AI. According to the article:</p>
      <ul class="points" style="margin-top:24px;">
        <li><span>D-STAR reached <strong>85% adoption</strong> across deployed markets by 2023.</span></li>
        <li><span>The tools delivered <strong>sales increases of 1.5% to 4.5%</strong>, depending on
          the market.</span></li>
        <li><span>In France, stores that followed D-STAR's recommendations outperformed control
          groups on net sales growth and net market share growth.</span></li>
      </ul>
      <a class="link" href="{hbs}" rel="noopener" style="margin-top:28px;">Read the HBS article {arrow}</a>
    </div>
  </section>

  </div>

{cta}'''.format(
    hbs=HBS_URL, arrow=ARROW,
    cta=cta_band('Is your data ready for AI?', 'Book a free diagnosis session.',
                 label='Book a free diagnosis session'))
