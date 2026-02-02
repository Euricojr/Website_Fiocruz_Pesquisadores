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
});
