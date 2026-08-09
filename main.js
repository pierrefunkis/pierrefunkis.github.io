/* ==========================================================================
   Semantic site behaviour
   ========================================================================== */
(function () {
  'use strict';

  /* --------------------------------------------------------------------
     Lead form: Web3Forms.

     Submissions POST as JSON to the endpoint below and are delivered to the
     address registered against the access key. The key is public by design,
     the same way it is in Web3Forms' own copy-paste HTML snippet, so it
     belongs in this file rather than in a secret store. Restrict it to the
     site's domain in the Web3Forms dashboard to stop it being reused.

     Clear FORM_ENDPOINT to fall back to opening the visitor's mail client.
     -------------------------------------------------------------------- */
  var FORM_ENDPOINT = 'https://api.web3forms.com/submit';
  var ACCESS_KEY = '6092d285-4b44-4798-9e7f-bb4429798754';
  var CONTACT_EMAIL = 'pierre@workwithsemantic.com';

  /* ── Mobile menu ──────────────────────────────────────────────────── */
  var menu = document.getElementById('mobileNavMenu');
  var menuBtn = document.getElementById('mobileMenuBtn');

  function closeMobileMenu() {
    if (!menu) return;
    menu.classList.remove('open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }

  if (menuBtn && menu) {
    menuBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = menu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    document.addEventListener('click', function (e) {
      if (!menu.contains(e.target) && !menuBtn.contains(e.target)) closeMobileMenu();
    });
  }

  /* ── Sliding nav pill ─────────────────────────────────────────────── */
  var pill = document.getElementById('navPill');
  var navCenter = document.getElementById('navCenter');

  function updatePill() {
    if (!pill || !navCenter) return;
    var active = navCenter.querySelector('[aria-current="page"]');
    if (!active) { pill.style.opacity = '0'; return; }
    var b = active.getBoundingClientRect();
    var n = navCenter.getBoundingClientRect();
    pill.style.opacity = '1';
    pill.style.left = (b.left - n.left) + 'px';
    pill.style.width = b.width + 'px';
  }

  window.addEventListener('load', updatePill);
  window.addEventListener('resize', function () {
    updatePill();
    /* rotating past the breakpoint would otherwise strand the open menu */
    if (window.innerWidth > 900) closeMobileMenu();
  });

  /* ── Founder photo fallback ───────────────────────────────────────── */
  /* Until the photograph is committed, swap the broken image for a monogram
     of the same size so the card never renders as a missing-file icon. */
  var founderPhoto = document.getElementById('founderPhoto');

  if (founderPhoto) {
    var showMonogram = function () {
      if (!founderPhoto.parentNode) return;
      var mono = document.createElement('div');
      mono.className = founderPhoto.className;
      mono.setAttribute('aria-hidden', 'true');
      mono.textContent = founderPhoto.getAttribute('data-monogram') || '';
      founderPhoto.replaceWith(mono);
    };

    founderPhoto.addEventListener('error', showMonogram);

    /* This script is deferred, so a missing photo may already have failed
       before the listener above was attached. A finished load with no
       intrinsic width is that case. */
    if (founderPhoto.complete && founderPhoto.naturalWidth === 0) showMonogram();
  }

  /* ── Modal ────────────────────────────────────────────────────────── */
  /* Built here rather than duplicated into every page: it cannot work
     without JS, and nothing inside it needs to be crawlable. */
  /* Client enquiries only. Applications go straight to email from the
     Careers CTAs, so there is no second variant of this form. */
  var COPY = {
    title: 'Tell us about your data challenge',
    sub: 'Tell us what you are facing and we will come back within one business day.',
    needLabel: 'What do you need help with?',
    needPlaceholder: 'Select an area',
    msgLabel: 'The challenge',
    msgPlaceholder: 'What is breaking, what stack it sits on, and what a good outcome looks like...',
    submit: 'Send'
  };

  var DISCIPLINES = [
    'Data Quality & Reliability', 'Data Governance', 'Data Engineering',
    'Analytics Engineering', 'Advanced Analytics & Data Science',
    'Data Modelling & Architecture', 'Master Data Management',
    'Business Intelligence', 'Machine Learning', 'AI & Automation',
    'Data Project Management', 'Other'
  ];

  var overlay, form, successBox, lastFocused;

  function buildModal() {
    overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    overlay.id = 'modalOverlay';
    overlay.innerHTML =
      '<div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="modalTitle">' +
        '<button class="modal-close" type="button" aria-label="Close dialog">' +
          '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M1 1l12 12M13 1L1 13" stroke="#475569" stroke-width="1.5" stroke-linecap="round"/></svg>' +
        '</button>' +
        '<form id="modalForm" novalidate>' +
          '<h2 class="modal-title" id="modalTitle">Tell us about your data challenge</h2>' +
          '<p class="modal-sub" id="modalSub"></p>' +
          '<div class="form-row">' +
            '<div class="form-group">' +
              '<label for="fName">First name</label>' +
              '<input type="text" id="fName" name="firstName" placeholder="Alex" autocomplete="given-name" required>' +
            '</div>' +
            '<div class="form-group">' +
              '<label for="lName">Last name</label>' +
              '<input type="text" id="lName" name="lastName" placeholder="Smith" autocomplete="family-name" required>' +
            '</div>' +
          '</div>' +
          '<div class="form-group">' +
            '<label for="email">Work email</label>' +
            '<input type="email" id="email" name="email" placeholder="alex@company.com" autocomplete="email" required>' +
          '</div>' +
          '<div class="form-group" id="companyField">' +
            '<label for="company">Company</label>' +
            '<input type="text" id="company" name="company" placeholder="Your company name" autocomplete="organization">' +
          '</div>' +
          '<div class="form-group">' +
            '<label for="need" id="needLabel">What do you need?</label>' +
            '<select id="need" name="discipline" required>' +
              '<option value="" disabled selected id="needPlaceholder">Select a discipline</option>' +
              DISCIPLINES.map(function (d) {
                return '<option>' + d.replace(/&/g, '&amp;') + '</option>';
              }).join('') +
            '</select>' +
          '</div>' +
          '<div class="form-group">' +
            '<label for="msg" id="msgLabel">Tell us more</label>' +
            '<textarea id="msg" name="message"></textarea>' +
          '</div>' +
          /* Honeypot. Named botcheck because Web3Forms rejects submissions
             carrying it, so a bot that gets past this browser is stopped
             again server-side. Off-screen and hidden from assistive tech, so
             only something filling every field will tick it. */
          '<div class="hp-field" aria-hidden="true">' +
            '<label for="hp">Do not fill this in</label>' +
            '<input type="checkbox" id="hp" name="botcheck" tabindex="-1" autocomplete="off">' +
          '</div>' +
          '<button class="form-submit" type="submit" id="formSubmit">Send request →</button>' +
        '</form>' +
        '<div class="form-success" id="modalSuccess" hidden>' +
          '<div class="form-success-icon">' +
            '<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true"><path d="M6 14l5 5 11-11" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
          '</div>' +
          '<h2 class="heading-sm" id="successTitle" style="margin-bottom:8px;">We got your message</h2>' +
          '<p class="body-md" id="successBody" style="font-size:15px;">We\'ll review it and be in touch within one business day.</p>' +
          '<button class="btn-primary" type="button" id="successClose" style="margin-top:24px;">Close</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(overlay);

    form = overlay.querySelector('#modalForm');
    successBox = overlay.querySelector('#modalSuccess');

    overlay.querySelector('.modal-close').addEventListener('click', closeModal);
    overlay.querySelector('#successClose').addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal();
    });
    form.addEventListener('submit', handleSubmit);
  }

  function openModal() {
    if (!overlay) buildModal();

    overlay.querySelector('#modalTitle').textContent = COPY.title;
    overlay.querySelector('#modalSub').textContent = COPY.sub;
    overlay.querySelector('#needLabel').textContent = COPY.needLabel;
    overlay.querySelector('#needPlaceholder').textContent = COPY.needPlaceholder;
    overlay.querySelector('#msgLabel').textContent = COPY.msgLabel;
    overlay.querySelector('#msg').placeholder = COPY.msgPlaceholder;
    overlay.querySelector('#formSubmit').textContent = COPY.submit + ' →';

    form.hidden = false;
    successBox.hidden = true;

    lastFocused = document.activeElement;
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    overlay.querySelector('#fName').focus();
  }

  function closeModal() {
    if (!overlay) return;
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (!form.reportValidity()) return;

    /* Bot: show the same success state it would have got, and send nothing,
       so it gets no signal that it was caught. */
    if (form.querySelector('#hp').checked) { showSuccess(); return; }

    var data = new FormData(form);
    var payload = {};
    data.forEach(function (v, k) { if (v) payload[k] = v; });

    var name = ((payload.firstName || '') + ' ' + (payload.lastName || '')).trim();

    if (FORM_ENDPOINT) {
      var btn = overlay.querySelector('#formSubmit');
      btn.disabled = true;
      btn.textContent = 'Sending…';

      payload.access_key = ACCESS_KEY;
      payload.subject = 'New enquiry from workwithsemantic.com'
        + (payload.discipline ? ': ' + payload.discipline : '');
      payload.from_name = name || 'Semantic website';
      /* So a reply goes to the enquirer rather than back to the form */
      if (payload.email) payload.replyto = payload.email;

      fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) {
          /* Web3Forms answers 200 with success:false for a rejected
             submission, so the status alone is not enough. */
          return r.json().then(function (body) { return { ok: r.ok, status: r.status, body: body }; });
        })
        .then(function (res) {
          if (res.ok && res.body && res.body.success) { showSuccess(); return; }
          throw new Error(res.status === 429 ? 'rate-limited' : 'rejected');
        })
        .catch(function (err) {
          btn.disabled = false;
          btn.textContent = COPY.submit + ' →';
          alert(err && err.message === 'rate-limited'
            ? 'Too many messages have been sent from here just now. Please try again shortly, or email ' + CONTACT_EMAIL + '.'
            : 'Sorry, something went wrong sending that. Please email ' + CONTACT_EMAIL + ' instead.');
        });
      return;
    }

    /* No endpoint configured: hand off to the visitor's mail client so the
       enquiry is not simply dropped. */
    var lines = [];
    Object.keys(payload).forEach(function (k) {
      if (k !== 'botcheck') lines.push(k + ': ' + payload[k]);
    });
    window.location.href = 'mailto:' + CONTACT_EMAIL +
      '?subject=' + encodeURIComponent(COPY.title) +
      '&body=' + encodeURIComponent(lines.join('\n'));
    showSuccess(true);
  }

  /* handedOff means we only opened the visitor's mail client. Nothing has
     reached us yet and it may never, so do not claim that it has. */
  function showSuccess(handedOff) {
    overlay.querySelector('#successTitle').textContent =
      handedOff ? 'Almost there' : 'We got your message';
    overlay.querySelector('#successBody').textContent = handedOff
      ? 'We have opened your email app with the details filled in. Send that message and we will come back within one business day. If nothing opened, email us at ' + CONTACT_EMAIL + '.'
      : 'We\'ll review it and be in touch within one business day.';
    form.hidden = true;
    successBox.hidden = false;
  }

  /* Any element with data-modal opens the dialog */
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-modal]');
    if (!trigger) return;
    e.preventDefault();
    closeMobileMenu();
    openModal();
  });

  document.addEventListener('keydown', function (e) {
    if (!overlay || !overlay.classList.contains('open')) return;

    if (e.key === 'Escape') { closeModal(); return; }

    /* Keep focus inside the dialog while it is open */
    if (e.key !== 'Tab') return;
    /* :not(#hp) keeps the honeypot out of the trap; it is rendered off-screen
       rather than hidden, so it would otherwise qualify as focusable. */
    var f = overlay.querySelectorAll('button, input:not(#hp), select, textarea, a[href]');
    var visible = Array.prototype.filter.call(f, function (el) {
      return el.offsetParent !== null && !el.disabled;
    });
    if (!visible.length) return;
    var first = visible[0], last = visible[visible.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  /* ── Smooth in-page anchors that respect reduced motion ───────────── */
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;
    var id = link.getAttribute('href').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    closeMobileMenu();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });
})();
