/* ==========================================================================
   Semantic site behaviour

   Four small things, none of which the page depends on to be readable:
   the mobile menu, the navbar's scrolled state, the founder photo fallback,
   and the contact form on /contact/.
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

  var menu = document.getElementById('mobileMenu');
  var menuBtn = document.getElementById('navToggle');

  function closeMenu() {
    if (!menu) return;
    menu.classList.remove('is-open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }

  if (menu && menuBtn) {
    menuBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = menu.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    document.addEventListener('click', function (e) {
      if (!menu.contains(e.target) && !menuBtn.contains(e.target)) closeMenu();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });

    /* Rotating past the breakpoint would otherwise strand the open menu */
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) closeMenu();
    });
  }

  /* ── Navbar scrolled state ────────────────────────────────────────── */
  /* The bar only draws its bottom rule once there is content behind it, so
     the top of a page stays uninterrupted. */

  var nav = document.querySelector('.nav');

  if (nav) {
    var ticking = false;

    var syncNav = function () {
      nav.classList.toggle('is-scrolled', window.scrollY > 8);
      ticking = false;
    };

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(syncNav);
    }, { passive: true });

    syncNav();
  }

  /* ── Founder photo fallback ───────────────────────────────────────── */
  /* If the photograph is ever missing, swap in a monogram of the same size
     so the card never renders as a broken-image icon. */

  var founderPhoto = document.getElementById('founderPhoto');

  if (founderPhoto) {
    var showMonogram = function () {
      if (!founderPhoto.parentNode) return;
      var mono = document.createElement('div');
      mono.className = founderPhoto.className + ' founder-photo--fallback';
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

  /* ── Contact form ─────────────────────────────────────────────────── */

  var form = document.getElementById('contactForm');

  if (form) {
    var statusBox = document.getElementById('formStatus');
    var successBox = document.getElementById('formSuccess');
    var submitBtn = document.getElementById('formSubmit');
    var submitLabel = submitBtn ? submitBtn.textContent : 'Send';

    var showError = function (message) {
      if (!statusBox) return;
      statusBox.hidden = false;
      statusBox.classList.add('form-status--error');
      statusBox.textContent = message;
    };

    /* handedOff means we only opened the visitor's mail client. Nothing has
       reached us yet and it may never, so do not claim that it has. */
    var showSuccess = function (handedOff) {
      form.hidden = true;
      if (statusBox) statusBox.hidden = true;
      if (!successBox) return;
      successBox.hidden = false;
      successBox.querySelector('[data-success-title]').textContent =
        handedOff ? 'Almost there' : 'Thanks, that reached us';
      successBox.querySelector('[data-success-body]').textContent = handedOff
        ? 'We have opened your email app with the details filled in. Send that message and Pierre will come back to you within one business day. If nothing opened, write to ' + CONTACT_EMAIL + '.'
        : 'Pierre will read it and come back to you within one business day, usually with a time to talk.';
      successBox.setAttribute('tabindex', '-1');
      successBox.focus({ preventScroll: true });
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      /* Bot: show the same success state it would have got, and send
         nothing, so it gets no signal that it was caught. */
      var hp = form.querySelector('#hp');
      if (hp && hp.checked) { showSuccess(); return; }

      var payload = {};
      new FormData(form).forEach(function (v, k) { if (v) payload[k] = v; });

      if (FORM_ENDPOINT) {
        if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Sending…'; }
        if (statusBox) { statusBox.hidden = true; statusBox.classList.remove('form-status--error'); }

        payload.access_key = ACCESS_KEY;
        payload.subject = 'New enquiry from workwithsemantic.com'
          + (payload.company ? ': ' + payload.company : '');
        payload.from_name = payload.name || 'Semantic website';
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
            return r.json().then(function (body) {
              return { ok: r.ok, status: r.status, body: body };
            });
          })
          .then(function (res) {
            if (res.ok && res.body && res.body.success) { showSuccess(); return; }
            throw new Error(res.status === 429 ? 'rate-limited' : 'rejected');
          })
          .catch(function (err) {
            if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = submitLabel; }
            showError(err && err.message === 'rate-limited'
              ? 'Too many messages have been sent from here just now. Please try again shortly, or write to ' + CONTACT_EMAIL + '.'
              : 'Something went wrong sending that. Please write to ' + CONTACT_EMAIL + ' instead.');
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
        '?subject=' + encodeURIComponent('Data problem to solve') +
        '&body=' + encodeURIComponent(lines.join('\n'));
      showSuccess(true);
    });
  }

  /* ── Smooth in-page anchors that respect reduced motion ───────────── */

  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;
    var id = link.getAttribute('href').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    closeMenu();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });
})();
