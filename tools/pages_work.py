# -*- coding: utf-8 -*-
from shared import ARROW, cta_band

HBS_URL = 'https://www.library.hbs.edu/working-knowledge/how-pernod-ricard-stirred-up-employee-enthusiasm-for-ai'

PERNOD = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Pernod Ricard</span>
      </nav>
      <p class="eyebrow">Case study</p>
      <h1 class="display" style="max-width:none;">Making Pernod Ricard's AI sales engine trustworthy</h1>
      <p class="lede">Semantic strengthened the data foundations of D-STAR, the in-house AI
        recommendation engine that Harvard Business School later featured as a model of
        successful AI adoption.</p>
    </div>
  </section>

  <section class="section section--tight section--flush" aria-labelledby="glance-h">
    <div class="container">
      <h2 class="h-xl" id="glance-h">At a glance</h2>
      <div class="grid grid--3" style="margin-top:28px;">
        <div class="cell"><h3 class="h-md">Client</h3>
          <p class="body">Pernod Ricard, the world's second-largest spirits company, active in
            more than 70 countries.</p></div>
        <div class="cell"><h3 class="h-md">Engagement</h3>
          <p class="body">15 months alongside Pernod Ricard's internal AI team on D-STAR.</p></div>
        <div class="cell cell--accent"><h3 class="h-md">Semantic's focus</h3>
          <p class="body">Data quality: tooling and global processes behind the product.</p></div>
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

  <section class="section section--mint" aria-labelledby="impact-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="impact-h">What Semantic did</h2>
        <p class="body">Data quality is the part of AI projects that is most often overlooked.
          Semantic made it a first-class workstream.</p>
      </div>
      <div class="grid grid--3">
        <div class="cell"><h3 class="h-md">Deployed data quality tooling</h3>
          <p class="body">Data quality tools deployed on the data behind the product, to
            keep its recommendations dependable.</p></div>
        <div class="cell"><h3 class="h-md">Set global processes</h3>
          <p class="body">A global way of working for data quality, instead of one-off
            fixes.</p></div>
        <div class="cell"><h3 class="h-md">Strengthened the foundations</h3>
          <p class="body">More reliable outputs, higher user confidence and smoother AI
            adoption.</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="hbs-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="hbs-h">Recognised by Harvard Business School</h2>
      </div>
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
      <p class="body" style="margin-top:24px;">These results belong to Pernod Ricard's
        program and teams, and the article does not name Semantic. Reliable data is what a
        trusted recommendation engine stands on, and that was Semantic's part of the work.</p>
      <a class="link" href="{hbs}" rel="noopener" style="margin-top:28px;">Read the HBS article {arrow}</a>
    </div>
  </section>

{cta}'''.format(
    hbs=HBS_URL, arrow=ARROW,
    cta=cta_band('Is your data ready for AI?', 'Book a free diagnosis session.',
                 label='Book a free diagnosis session'))
