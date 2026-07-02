/* CompanyCard — shared interactions */
(function () {
  "use strict";

  /* Mobile nav toggle */
  function initNav() {
    var nav = document.querySelector(".nav");
    var toggle = document.querySelector(".nav-toggle");
    if (!nav || !toggle) return;
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
    nav.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
    /* Elevate navbar once the page is scrolled (ui-ux-pro-max: state-clarity) */
    var onScroll = function () { nav.classList.toggle("scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Scroll reveal */
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || !els.length) {
      els.forEach(function (e) { e.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    els.forEach(function (e) { io.observe(e); });
  }

  /* Pricing monthly / annual toggle */
  function initPricing() {
    var toggle = document.querySelector("[data-toggle]");
    if (!toggle) return;
    var prices = document.querySelectorAll("[data-monthly]");
    var pers = document.querySelectorAll("[data-per]");
    toggle.addEventListener("click", function () {
      var annual = toggle.classList.toggle("on");
      prices.forEach(function (el) {
        var v = annual ? el.getAttribute("data-annual") : el.getAttribute("data-monthly");
        if (v !== null) el.firstChild.nodeValue = v;
      });
      pers.forEach(function (el) {
        el.textContent = annual ? "per user / month · billed yearly" : "per user / month";
      });
    });
  }

  /* Live card builder (home hero) */
  function initBuilder() {
    var nameIn = document.getElementById("b-name");
    if (!nameIn) return;
    var roleIn = document.getElementById("b-role");
    var coIn = document.getElementById("b-company");
    var name = document.getElementById("dc-name");
    var role = document.getElementById("dc-role");
    var co = document.getElementById("dc-company-name");
    var avatar = document.getElementById("dc-avatar");
    function initials(s) {
      return s.trim().split(/\s+/).slice(0, 2).map(function (w) { return w[0] || ""; }).join("").toUpperCase() || "JD";
    }
    function sync() {
      if (name) name.textContent = nameIn.value || "Jordan Diaz";
      if (role && roleIn) role.textContent = roleIn.value || "Head of Sales";
      if (co && coIn) co.textContent = coIn.value || "CompanyCard";
      if (avatar) avatar.textContent = initials(nameIn.value || "Jordan Diaz");
    }
    [nameIn, roleIn, coIn].forEach(function (el) { if (el) el.addEventListener("input", sync); });
    sync();
  }

  /* Footer year */
  function initYear() {
    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initReveal();
    initPricing();
    initBuilder();
    initYear();
  });
})();
