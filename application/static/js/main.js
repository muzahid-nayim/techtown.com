window.addEventListener("scroll", function () {
  var nav = document.querySelector(".home-top-nav");
  var scrollPos = window.scrollY;

  if (scrollPos > 0) {
    nav.classList.add("scrolled");
  } else {
    nav.classList.remove("scrolled");
  }
});
