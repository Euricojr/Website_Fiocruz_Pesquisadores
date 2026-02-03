document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navbar");

  // Check if navbar should be static (always dark/visible) or already light
  if (navbar.classList.contains("navbar-static") || navbar.classList.contains("navbar-light")) {
     // Already styled or static, no scroll effect needed usually
  } else {
      // Only add scroll listener if not static/pre-colored
      window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
          navbar.classList.add("scrolled");
        } else {
          navbar.classList.remove("scrolled");
        }
      });
  }
  // Dark Mode Logic
  const themeSwitch = document.getElementById('switch');
  const body = document.body;
  const currentTheme = localStorage.getItem('theme');

  // Check LocalStorage or System Preference
  if (currentTheme) {
    if (currentTheme === 'dark') {
      body.classList.add('dark-mode');
      if (themeSwitch) themeSwitch.checked = true;
    }
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    body.classList.add('dark-mode');
    if (themeSwitch) themeSwitch.checked = true;
  }

  // Toggle Event Listener
  if (themeSwitch) {
      themeSwitch.addEventListener('change', function (e) {
        if (e.target.checked) {
          body.classList.add('dark-mode');
          localStorage.setItem('theme', 'dark');
        } else {
          body.classList.remove('dark-mode');
          localStorage.setItem('theme', 'light');
        }
      });
  }
});
