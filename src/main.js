// Theme persistence
const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const storedTheme = localStorage.getItem('theme');
if (storedTheme) {
  document.documentElement.dataset.theme = storedTheme;
} else {
  document.documentElement.dataset.theme = prefersDark ? 'dark' : 'light';
}

// Theme toggle
const toggle = document.getElementById('theme-toggle');
function updateTheme() {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  localStorage.setItem('theme', next);
}
if (toggle) toggle.addEventListener('click', updateTheme);

// Mobile nav toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!expanded));
    navLinks.classList.toggle('show');
  });
}

// Smooth scrolling for same-page links
document.addEventListener('click', (e) => {
  const target = e.target;
  if (target.tagName === 'A' && target.getAttribute('href')?.startsWith('#')) {
    const id = target.getAttribute('href');
    const el = document.querySelector(id);
    if (el) {
      e.preventDefault();
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
});

// Footer year
const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());


