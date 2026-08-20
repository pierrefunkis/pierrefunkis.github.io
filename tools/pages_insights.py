# -*- coding: utf-8 -*-
from shared import ARROW, cta_band
from articles import ARTICLES


def _meta(a):
    return ('<div class="article-meta"><span>%s</span><span>'
            '<time datetime="%s">%s</time></span></div>' % (a['category'], a['iso'], a['date']))


def insights_index():
    featured = ARTICLES[0]
    rest = ARTICLES[1:]

    items = []
    for a in rest:
        items.append('''        <li class="article-item">
          <div>{meta}</div>
          <div>
            <h3><a href="/insights/{slug}/">{title}</a></h3>
            <p class="body">{excerpt}</p>
            <a class="link" href="/insights/{slug}/" style="margin-top:18px;">Read {arrow}</a>
          </div>
        </li>'''.format(meta=_meta(a), slug=a['slug'], title=a['title'],
                        excerpt=a['excerpt'], arrow=ARROW))

    return '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Insights</span>
      </nav>
      <p class="eyebrow">Insights</p>
      <h1 class="display">Notes from inside enterprise data work</h1>
      <p class="lede">Short pieces on the problems we keep running into: quality that does
        not hold, AI programmes that stall, migrations that lose the room. Written by the
        people doing the work.</p>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="articles-h">
    <div class="container">
      <h2 class="visually-hidden" id="articles-h">Articles</h2>

      <article class="featured">
        <div>
          {fmeta}
          <h2><a href="/insights/{fslug}/" style="text-decoration:none;">{ftitle}</a></h2>
        </div>
        <div>
          <p class="body" style="font-size:18px;color:var(--ink-soft);">{fexcerpt}</p>
          <a class="link" href="/insights/{fslug}/">Read the piece {arrow}</a>
        </div>
      </article>

      <ul class="article-list">
{items}
      </ul>
    </div>
  </section>
{cta}'''.format(
        fmeta=_meta(featured), fslug=featured['slug'], ftitle=featured['title'],
        fexcerpt=featured['excerpt'], items='\n'.join(items), arrow=ARROW,
        cta=cta_band('Recognise any of this in your own estate?',
                     "Start with a conversation. No pitch, no deck."),
    )


def article_page(a, others):
    more = []
    for o in others:
        more.append('''        <li class="article-item">
          <div>{meta}</div>
          <div>
            <h3><a href="/insights/{slug}/">{title}</a></h3>
            <p class="body">{excerpt}</p>
          </div>
        </li>'''.format(meta=_meta(o), slug=o['slug'], title=o['title'], excerpt=o['excerpt']))

    return '''
  <article>
    <section class="hero hero--page">
      <div class="container container--narrow">
        <nav class="crumbs" aria-label="Breadcrumb">
          <a href="/">Home</a><span aria-hidden="true">/</span>
          <a href="/insights/">Insights</a><span aria-hidden="true">/</span><span>{category}</span>
        </nav>
        {meta}
        <h1 class="h-xl" style="margin-top:20px;max-width:22ch;">{title}</h1>
        <p class="lede" style="margin-top:24px;">{excerpt}</p>
      </div>
    </section>

    <section class="section section--tight" style="padding-top:0;">
      <div class="container container--narrow">
        <div class="prose">
{body}
        </div>
        <p class="body--tight" style="margin-top:56px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);">
          Written by the Semantic team. If it is relevant to something you are dealing with,
          <a class="link" href="/contact/">tell us about it {arrow}</a>
        </p>
      </div>
    </section>
  </article>

  <section class="section section--paper" aria-labelledby="more-h">
    <div class="container container--narrow">
      <div class="section-head" style="margin-bottom:16px;">
        <p class="eyebrow">More from Insights</p>
        <h2 class="h-lg" id="more-h">Related reading</h2>
      </div>
      <ul class="article-list">
{more}
      </ul>
      <a class="link" href="/insights/" style="margin-top:32px;">All insights {arrow}</a>
    </div>
  </section>
{cta}'''.format(
        category=a['category'], meta=_meta(a), title=a['title'], excerpt=a['excerpt'],
        body=a['body'].rstrip(), more='\n'.join(more), arrow=ARROW,
        cta=cta_band("Have a data problem you're trying to solve?", "Let's talk about it."),
    )
