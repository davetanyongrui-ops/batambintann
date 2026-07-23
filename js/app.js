// ===========================================================================
// RioU Escapes - Mobile Nav, Scroll Animations, Navbar Behavior
// ===========================================================================

document.addEventListener('DOMContentLoaded', function() {

  // -- Hamburger Toggle --
  var hamburger = document.getElementById('hamburger');
  var navLinks = document.getElementById('navLinks');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function() {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('open');
    });

    // Auto-close on any link tap
    var links = navLinks.querySelectorAll('a');
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function() {
        hamburger.classList.remove('active');
        navLinks.classList.remove('open');
      });
    }
  }

  // -- Navbar Scroll State --
  var navbar = document.getElementById('navbar');
  if (navbar) {
    var lastScrollY = 0;
    var ticking = false;

    function updateNav() {
      var scrollY = window.scrollY || window.pageYOffset;
      if (scrollY > 120) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
      // Hide on scroll down, show on scroll up (only beyond initial viewport)
      if (scrollY > 300) {
        if (scrollY > lastScrollY) {
          navbar.style.transform = 'translateY(-100%)';
        } else {
          navbar.style.transform = 'translateY(0)';
        }
      } else {
        navbar.style.transform = 'translateY(0)';
      }
      lastScrollY = scrollY;
      ticking = false;
    }

    window.addEventListener('scroll', function() {
      if (!ticking) {
        window.requestAnimationFrame(updateNav);
        ticking = true;
      }
    });
  }

  // -- IntersectionObserver Scroll Animations --
  var fadeElements = document.querySelectorAll('.fade-in-up');
  if (fadeElements.length > 0) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    for (var j = 0; j < fadeElements.length; j++) {
      // Stagger delays by index
      var delay = (j % 4) * 100;
      fadeElements[j].style.transitionDelay = delay + 'ms';
      observer.observe(fadeElements[j]);
    }
  }

  // -- Smooth Scroll for Anchor Links --
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;
      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var offsetTop = target.getBoundingClientRect().top + window.scrollY - 80;
        window.scrollTo({ top: offsetTop, behavior: 'smooth' });
      }
    });
  });

});
