var lastFocusedElement = null;
var currentModalType = 'company';
var pageIds = ['companies', 'talents', 'about'];

function getPageFromHash() {
  var hash = window.location.hash.replace('#', '');
  return pageIds.includes(hash) ? hash : 'companies';
}

function switchPage(target, options) {
  if (!pageIds.includes(target)) return;

  var shouldUpdateHash = !options || options.updateHash !== false;

  document.querySelectorAll('.page').forEach(function(page) {
    page.classList.remove('active');
  });
  document.querySelectorAll('.nav-page-btn').forEach(function(button) {
    button.classList.remove('active');
  });
  document.querySelectorAll('.mobile-nav-btn').forEach(function(button) {
    button.classList.remove('active');
  });

  document.getElementById(target).classList.add('active');

  var desktopButton = document.querySelector('.nav-page-btn[data-page="' + target + '"]');
  var mobileButton = document.querySelector('.mobile-nav-btn[data-page="' + target + '"]');
  if (desktopButton) desktopButton.classList.add('active');
  if (mobileButton) mobileButton.classList.add('active');

  if (shouldUpdateHash && window.location.hash !== '#' + target) {
    history.pushState(null, '', '#' + target);
  }

  updatePill();
  window.scrollTo({ top: 0 });
}

function updatePill() {
  var pill = document.getElementById('navPill');
  var navCenter = document.getElementById('navCenter');
  var activeButton = document.querySelector('.nav-page-btn.active');
  if (!pill || !navCenter || !activeButton) return;

  var buttonRect = activeButton.getBoundingClientRect();
  var navRect = navCenter.getBoundingClientRect();
  pill.style.left = (buttonRect.left - navRect.left) + 'px';
  pill.style.width = buttonRect.width + 'px';
}

function setMobileMenu(open) {
  var menu = document.getElementById('mobileNavMenu');
  var button = document.getElementById('mobileMenuBtn');
  menu.classList.toggle('open', open);
  button.setAttribute('aria-expanded', String(open));
}

function toggleMobileMenu() {
  var menu = document.getElementById('mobileNavMenu');
  setMobileMenu(!menu.classList.contains('open'));
}

function closeMobileMenu() {
  setMobileMenu(false);
}

function openModal(type) {
  var title = document.getElementById('modalTitle');
  var sub = document.getElementById('modalSub');
  var company = document.getElementById('companyField');
  var companyInput = document.getElementById('companyName');
  var needLabel = document.getElementById('needLabel');
  var msgArea = document.getElementById('msgArea');
  var formEl = document.getElementById('modalForm');
  var successEl = document.getElementById('modalSuccess');
  var overlay = document.getElementById('modalOverlay');

  currentModalType = type === 'talent' ? 'talent' : 'company';
  lastFocusedElement = document.activeElement;
  formEl.reset();
  formEl.style.display = '';
  successEl.style.display = 'none';

  if (currentModalType === 'talent') {
    title.textContent = 'Join Our Network';
    sub.textContent = 'Tell us about yourself and we\'ll be in touch.';
    company.style.display = 'none';
    companyInput.required = false;
    needLabel.textContent = 'Your specialisation';
    msgArea.placeholder = 'Tell us about your background, stack, and the types of projects you\'re interested in...';
  } else {
    title.textContent = 'Request a Data Expert';
    sub.textContent = 'Tell us about your project and we\'ll get back to you within 24 hours.';
    company.style.display = '';
    companyInput.required = false;
    needLabel.textContent = 'What do you need?';
    msgArea.placeholder = 'Briefly describe your project, timeline, or any specific requirements...';
  }

  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  window.setTimeout(function() {
    document.getElementById('firstName').focus();
  }, 0);
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
  document.body.style.overflow = '';

  if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
    lastFocusedElement.focus();
  }
}

function handleOverlayClick(event) {
  if (event.target === event.currentTarget) closeModal();
}

function handleSubmit(event) {
  event.preventDefault();

  var form = event.currentTarget;
  var formData = new FormData(form);
  var subject = currentModalType === 'talent'
    ? 'Semantic talent network application'
    : 'Semantic data expert request';
  var body = [
    'First name: ' + formData.get('firstName'),
    'Last name: ' + formData.get('lastName'),
    'Email: ' + formData.get('email'),
    'Company: ' + (formData.get('company') || 'N/A'),
    'Discipline: ' + formData.get('discipline'),
    '',
    'Message:',
    formData.get('message')
  ].join('\n');

  window.location.href = 'mailto:hello@semantic-data.io?subject='
    + encodeURIComponent(subject)
    + '&body='
    + encodeURIComponent(body);

  form.style.display = 'none';
  document.getElementById('modalSuccess').style.display = '';
}

window.addEventListener('load', function() {
  switchPage(getPageFromHash(), { updateHash: false });
  updatePill();
});

window.addEventListener('resize', updatePill);

window.addEventListener('hashchange', function() {
  switchPage(getPageFromHash(), { updateHash: false });
});

document.addEventListener('click', function(event) {
  var menu = document.getElementById('mobileNavMenu');
  var button = document.getElementById('mobileMenuBtn');
  if (!menu.contains(event.target) && !button.contains(event.target)) {
    closeMobileMenu();
  }
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeMobileMenu();
    closeModal();
  }
});
