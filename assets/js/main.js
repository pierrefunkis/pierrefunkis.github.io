  /* ── Page switching ─────────────────────────── */
  function switchPage(target) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-page-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.mobile-nav-btn').forEach(b => b.classList.remove('active'));

    document.getElementById(target).classList.add('active');

    const dBtn = document.querySelector('.nav-page-btn[data-page="' + target + '"]');
    const mBtn = document.querySelector('.mobile-nav-btn[data-page="' + target + '"]');
    if (dBtn) dBtn.classList.add('active');
    if (mBtn) mBtn.classList.add('active');

    updatePill();
    window.scrollTo({ top: 0 });
  }

  /* ── Sliding pill ───────────────────────────── */
  function updatePill() {
    var pill      = document.getElementById('navPill');
    var navCenter = document.getElementById('navCenter');
    var activeBtn = document.querySelector('.nav-page-btn.active');
    if (!pill || !navCenter || !activeBtn) return;

    var bR = activeBtn.getBoundingClientRect();
    var nR = navCenter.getBoundingClientRect();
    pill.style.left  = (bR.left - nR.left) + 'px';
    pill.style.width = bR.width + 'px';
  }

  window.addEventListener('load',   updatePill);
  window.addEventListener('resize', updatePill);

  /* ── Mobile menu ────────────────────────────── */
  function toggleMobileMenu() {
    document.getElementById('mobileNavMenu').classList.toggle('open');
  }

  function closeMobileMenu() {
    document.getElementById('mobileNavMenu').classList.remove('open');
  }

  document.addEventListener('click', function(e) {
    var menu = document.getElementById('mobileNavMenu');
    var btn  = document.getElementById('mobileMenuBtn');
    if (!menu.contains(e.target) && !btn.contains(e.target)) {
      menu.classList.remove('open');
    }
  });

  /* ── Modal ──────────────────────────────────── */
  function openModal(type) {
    var title      = document.getElementById('modalTitle');
    var sub        = document.getElementById('modalSub');
    var company    = document.getElementById('companyField');
    var needLabel  = document.getElementById('needLabel');
    var msgArea    = document.getElementById('msgArea');
    var formEl     = document.getElementById('modalForm');
    var successEl  = document.getElementById('modalSuccess');

    formEl.style.display    = '';
    successEl.style.display = 'none';

    if (type === 'talent') {
      title.textContent      = 'Join Our Network';
      sub.textContent        = 'Tell us about yourself and we\'ll be in touch.';
      company.style.display  = 'none';
      needLabel.textContent  = 'Your specialisation';
      msgArea.placeholder    = 'Tell us about your background, stack, and the types of projects you\'re interested in...';
    } else {
      title.textContent      = 'Request a Data Expert';
      sub.textContent        = 'Tell us about your project and we\'ll get back to you within 24 hours.';
      company.style.display  = '';
      needLabel.textContent  = 'What do you need?';
      msgArea.placeholder    = 'Briefly describe your project, timeline, or any specific requirements...';
    }

    document.getElementById('modalOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    document.getElementById('modalOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }

  function handleOverlayClick(e) {
    if (e.target === e.currentTarget) closeModal();
  }

  function handleSubmit() {
    document.getElementById('modalForm').style.display    = 'none';
    document.getElementById('modalSuccess').style.display = '';
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
  });
