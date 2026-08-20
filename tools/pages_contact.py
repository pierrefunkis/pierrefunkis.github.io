# -*- coding: utf-8 -*-
from shared import ARROW, EMAIL

SESSION_POINTS = [
    'Understand the problem, in your words and in business terms.',
    'Discuss the context around it: who it affects, what it costs, what has already been tried.',
    'Challenge the assumptions, including ours.',
    'Identify the approaches worth considering, and the ones that are not worth your money.',
    'Determine honestly whether Semantic is the right fit. Sometimes the answer is no.',
]

NEXT_STEPS = [
    ('01', 'Talk', 'A free advisory conversation. No deck, no pitch.'),
    ('02', 'Diagnose', 'Where the problem warrants it, a focused assessment of the real systems and data, ending in a written recommendation.'),
    ('03', 'Build', 'Delivery scoped to an outcome, with the right specialists assembled around it.'),
    ('04', 'Improve', 'Where it is useful, we stay on to keep raising the standard and hand the capability over.'),
]

CONTACT = '''
  <section class="hero hero--page">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a><span aria-hidden="true">/</span><span>Contact</span>
      </nav>
      <p class="eyebrow">Contact</p>
      <div class="hero-cols">
        <div>
          <h1 class="display">Have a data problem you're trying to solve?</h1>
        </div>
        <div>
          <p class="lede">Start with a free advisory conversation. Tell us roughly what is
            going on and we will find a time to talk it through properly.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0;" aria-labelledby="book-h">
    <div class="container">
      <div class="split split--even split--start">
        <div>
          <h2 class="h-lg" id="book-h">What the first session is for</h2>
          <p class="body" style="margin-top:20px;">It is a working conversation with Pierre,
            not a sales consultation. Roughly forty five minutes, usually enough to be useful
            on its own.</p>

          <ul class="points" style="margin-top:32px;">
{points}
          </ul>

          <div class="note" style="margin-top:40px;">
            <h3 class="h-md">You do not need to know what you want yet</h3>
            <p class="body" style="margin-top:14px;">Most people arrive with a symptom rather
              than a specification: a report nobody trusts, a migration that has stalled, an
              AI programme that will not leave the pilot. Working out what the problem
              actually is happens to be the first part of the job.</p>
          </div>

          <p class="body--tight" style="margin-top:32px;color:var(--muted);">Prefer email?
            Write to <a class="link" href="mailto:{email}">{email}</a></p>
        </div>

        <div class="contact-form-col">
          <!-- If a scheduling tool is adopted later, its embed drops in here and the
               form below becomes the fallback for people who would rather write. -->
          <div class="form-panel">
            <form id="contactForm" novalidate>
              <h2 class="h-md" style="margin-bottom:8px;">Book a free diagnosis session</h2>
              <p class="body--tight" style="margin-bottom:28px;color:var(--muted);">
                We reply within one business day.</p>

              <div class="form-row">
                <div class="field">
                  <label for="name">Name</label>
                  <input type="text" id="name" name="name" autocomplete="name" required>
                </div>
                <div class="field">
                  <label for="company">Company</label>
                  <input type="text" id="company" name="company" autocomplete="organization" required>
                </div>
              </div>

              <div class="form-row">
                <div class="field">
                  <label for="role">Role</label>
                  <input type="text" id="role" name="role" autocomplete="organization-title"
                         placeholder="Head of Data, CFO, CTO...">
                </div>
                <div class="field">
                  <label for="email">Work email</label>
                  <input type="email" id="email" name="email" autocomplete="email" required>
                </div>
              </div>

              <div class="field">
                <label for="problem">What are you trying to solve?</label>
                <textarea id="problem" name="problem" required
                          placeholder="What is breaking, what stack it sits on, and what a good outcome would look like."></textarea>
              </div>

              <!-- Honeypot. Named botcheck because Web3Forms rejects submissions carrying
                   it, so a bot that gets past the browser is stopped again server-side. -->
              <div class="hp-field" aria-hidden="true">
                <label for="hp">Do not fill this in</label>
                <input type="checkbox" id="hp" name="botcheck" tabindex="-1" autocomplete="off">
              </div>

              <button class="btn btn--primary" type="submit" id="formSubmit"
                      style="width:100%;">Send</button>

              <p class="form-footnote">We use what you send here to reply to you, nothing
                else. No newsletter, no list.</p>
            </form>

            <p class="form-status" id="formStatus" hidden></p>

            <div class="form-success" id="formSuccess" hidden>
              <h3 class="h-md" data-success-title>Thanks, that reached us</h3>
              <p class="body" data-success-body>Pierre will read it and come back to you
                within one business day, usually with a time to talk.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- NEXT STEPS -->
  <section class="section section--ink" aria-labelledby="next-h">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Next Steps</p>
        <h2 class="h-xl" id="next-h">Where the conversation can go</h2>
        <p class="body">Nothing beyond the first step is committed to in advance, and each
          step is only taken if the previous one showed it was worth it.</p>
      </div>
      <div class="steps">
{steps}
      </div>
    </div>
  </section>
'''


def _points():
    return '\n'.join('            <li>%s</li>' % p for p in SESSION_POINTS)


def _steps():
    out = []
    for num, title, body in NEXT_STEPS:
        out.append('''        <div class="step">
          <div class="step-num">{num}</div>
          <h3>{title}</h3>
          <p class="body">{body}</p>
        </div>'''.format(num=num, title=title, body=body))
    return '\n'.join(out)


CONTACT = CONTACT.format(points=_points(), steps=_steps(), email=EMAIL, arrow=ARROW)
