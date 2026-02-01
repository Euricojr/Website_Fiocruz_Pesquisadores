document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navbar");

  // Check if navbar should be static (always dark/visible)
  if (navbar.classList.contains("navbar-static")) {
     navbar.classList.add("navbar-light");
  } else {
      // Only add scroll listener if not static
      window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
          navbar.classList.add("navbar-light");
        } else {
          navbar.classList.remove("navbar-light");
        }
      });
  }
});
