# -*- coding: utf-8 -*-
SESSION_POINTS = [
    'Understand the problem and its business impact.',
    'Review the context: who is affected and what has been tried.',
    'Identify the approaches worth pursuing.',
    'Give you an honest view on whether we are the right fit.',
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
          <h1 class="display">Discuss your data challenge with us</h1>
        </div>
        <div>
          <p class="lede">Book a free diagnosis session. Share a few details and we will
            reply within one business day.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0;" aria-labelledby="book-h">
    <div class="container">
      <div class="split split--contact">
        <div>
          <h2 class="h-lg" id="book-h">What to expect</h2>
          <p class="body" style="margin-top:20px;">A focused conversation about your
            challenge with our senior team. Free and without obligation.</p>

          <ul class="points" style="margin-top:32px;">
{points}
          </ul>

          <p class="body--tight" style="margin-top:24px;color:var(--muted);">No brief is
            needed. Describe the symptom and we will help define the problem.</p>
        </div>

        <div class="contact-form-col">
          <!-- If a scheduling tool is adopted later, its embed drops in here and the
               form below becomes the fallback for people who would rather write. -->
          <div class="form-panel">
            <form id="contactForm" novalidate>
              <h2 class="h-md" style="margin-bottom:28px;">Book a free diagnosis session</h2>

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
                <label for="problem">What challenge are you trying to solve?</label>
                <textarea id="problem" name="problem" required
                          placeholder="Briefly describe the issue, the systems involved and the outcome you are looking for."></textarea>
              </div>

              <!-- Honeypot. Named botcheck because Web3Forms rejects submissions carrying
                   it, so a bot that gets past the browser is stopped again server-side. -->
              <div class="hp-field" aria-hidden="true">
                <label for="hp">Do not fill this in</label>
                <input type="checkbox" id="hp" name="botcheck" tabindex="-1" autocomplete="off">
              </div>

              <button class="btn btn--primary" type="submit" id="formSubmit"
                      style="width:100%;">Request a session</button>
            </form>

            <p class="form-status" id="formStatus" hidden></p>

            <div class="form-success" id="formSuccess" hidden>
              <h3 class="h-md" data-success-title>Thank you, your request has been received</h3>
              <p class="body" data-success-body>We will review it and reply within one
                business day, usually with a proposed time to talk.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''


def _points():
    return '\n'.join('            <li>%s</li>' % p for p in SESSION_POINTS)


CONTACT = CONTACT.format(points=_points())
