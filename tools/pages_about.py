# -*- coding: utf-8 -*-
from shared import credential, ARROW, LINKEDIN, cta_band

from plates import (ICON_BIGFIRM, ICON_FREELANCE, ICON_SEMANTIC_LIGHT, ICON_SENIOR,
                    ICON_EMBEDDED, ICON_RELIABLE)

MODELS = [
    (ICON_BIGFIRM, 'Large consultancies', False,
     'Substantial capacity, but slow to adapt and expensive. The senior person who scoped '
     'the work is rarely the one who delivers it.'),
    (ICON_FREELANCE, 'Freelance marketplaces', False,
     'Capable individuals, but without organizational structure behind them and without '
     'continuity if they become unavailable.'),
    (ICON_SEMANTIC_LIGHT, 'Semantic', True,
     'Senior judgment and a dedicated team that can execute. The person who understands '
     'your problem is accountable for solving it.'),
]

PRINCIPLES = [
    (ICON_SENIOR, 'Senior-led',
     'The people who scope the work are involved in delivering it.'),
    (ICON_EMBEDDED, 'Embedded',
     'We work in your tools, your stack and your rituals.'),
    (ICON_RELIABLE, 'Reliable',
     'We deliver what we commit to, with regular service reviews and continuity.'),
]

ABOUT = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>About Us</span>
      </nav>
      <h1 class="display" style="max-width:none;">Who is behind Semantic</h1>
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
          <p class="founder-role">Founder</p>

          <p class="body" style="font-size:18px;color:var(--ink-soft);">Pierre built his
            data expertise at Amazon, working across Paris and New York on large-scale
            data projects impacting millions of users. He combines this technical depth with
            the business acumen gained at HEC Paris, bridging the gap between complex
            technical challenges and business outcomes.</p>

          <p class="body" style="margin-top:20px;">He founded Semantic to help companies
            become truly data-driven without spending millions. Semantic brings senior
            expertise directly into your teams to tackle your most important data
            challenges, with the flexibility to adapt as your needs evolve.</p>

          <div class="cred-row" style="margin-top:32px;">
            <div>{mark_amazon}</div>
            <div>{mark_hec}</div>
          </div>

          <a class="link" href="{linkedin}" rel="noopener" style="margin-top:28px;">Connect on LinkedIn {arrow}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- WHY SEMANTIC -->
  <section class="section section--mint" aria-labelledby="why-h">
    <div class="container">
      <div class="section-head">
        <h2 class="h-xl" id="why-h">A third option</h2>
        <p class="body">Complex data problems need senior judgment to frame and a team to
          execute. Most firms offer one or the other.</p>
      </div>

      <div class="grid grid--3">
{models}
      </div>

      <div class="grid grid--3" style="margin-top:20px;">
{principles}
      </div>
      <a class="link" href="/join-network/" style="margin-top:36px;">Join our network of data professionals {arrow}</a>
    </div>
  </section>

{cta}'''

def _cells(items, with_flag=False):
    out = []
    for item in items:
        if with_flag:
            icon, title, accent, body = item
        else:
            icon, title, body = item
            accent = False
        out.append('''        <div class="cell{cls}">
          {icon}
          <h3 class="h-md">{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(cls=' cell--accent' if accent else '', icon=icon, title=title, body=body))
    return '\n'.join(out)


ABOUT = ABOUT.format(
    linkedin=LINKEDIN,
    mark_amazon=credential('amazon', 'Amazon', 'Amazon'),
    mark_hec=credential('hec-paris', 'HEC Paris', 'HEC Paris'),
    arrow=ARROW,
    models=_cells(MODELS, with_flag=True),
    principles=_cells(PRINCIPLES),
    cta=cta_band('Discuss your data challenge with us', 'Book a free diagnosis session.',
                 label='Book a free diagnosis session'),
)
