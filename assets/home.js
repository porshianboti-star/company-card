/* CompanyCard — homepage cinematic interactions (home.js) */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isTouch = window.matchMedia && window.matchMedia("(hover: none)").matches;

  /* ---------- 3D pointer tilt + chip parallax ---------- */
  function initTilt() {
    if (reduce || isTouch) return;
    document.querySelectorAll("[data-tilt]").forEach(function (stage) {
      var card = stage.querySelector(".tilt3d");
      var chips = stage.querySelectorAll(".chip");
      var max = parseFloat(stage.getAttribute("data-tilt")) || 9;
      var raf;
      stage.addEventListener("mousemove", function (e) {
        var r = stage.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        if (raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(function () {
          if (card) card.style.transform = "rotateY(" + (px * max) + "deg) rotateX(" + (-py * max) + "deg)";
          chips.forEach(function (c, i) {
            var d = (i % 2 ? 1 : -1) * (10 + i * 5);
            c.style.translate = (px * d) + "px " + (py * d) + "px";
          });
        });
      });
      stage.addEventListener("mouseleave", function () {
        if (card) card.style.transform = "";
        chips.forEach(function (c) { c.style.translate = ""; });
      });
    });
  }

  /* ---------- Hover tilt on cards ---------- */
  function initHovTilt() {
    if (reduce || isTouch) return;
    document.querySelectorAll("[data-hov3d]").forEach(function (el) {
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(800px) rotateY(" + (px * 7) + "deg) rotateX(" + (-py * 7) + "deg) translateY(-5px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- Showcase parallax (mouse + scroll) ---------- */
  function initShowcase() {
    var sc = document.querySelector(".showcase");
    if (!sc) return;
    var cards = sc.querySelectorAll(".float-card");
    if (!reduce && !isTouch) {
      sc.addEventListener("mousemove", function (e) {
        var r = sc.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        cards.forEach(function (c) {
          var dz = parseFloat(c.getAttribute("data-depth")) || 20;
          c.style.translate = (px * dz) + "px " + (py * dz) + "px";
        });
      });
      sc.addEventListener("mouseleave", function () {
        cards.forEach(function (c) { c.style.translate = ""; });
      });
    }
  }

  /* ---------- Auto-typing persona cycle ---------- */
  function initTyper() {
    var nameIn = document.getElementById("b-name");
    if (!nameIn) return;
    var roleIn = document.getElementById("b-role");
    var coIn = document.getElementById("b-company");
    var dName = document.getElementById("dc-name");
    var dRole = document.getElementById("dc-role");
    var dCo = document.getElementById("dc-company-name");
    var dAv = document.getElementById("dc-avatar");
    var people = [
      { n: "Jordan Diaz", r: "Head of Sales", c: "CompanyCard" },
      { n: "Mia Chen", r: "Product Designer", c: "Lumen" },
      { n: "Samuel Okoro", r: "Founder & CEO", c: "Vertex" },
      { n: "Aria Bianchi", r: "Marketing Lead", c: "Atlas Co" }
    ];
    var stopped = false, timers = [];
    function stop() {
      stopped = true;
      timers.forEach(clearTimeout);
      if (dName) dName.classList.remove("type-caret");
    }
    [nameIn, roleIn, coIn].forEach(function (el) { if (el) el.addEventListener("focus", stop); });
    function initials(s) { return s.trim().split(/\s+/).slice(0, 2).map(function (w) { return w[0] || ""; }).join("").toUpperCase(); }
    function setMeta(p) {
      if (roleIn) roleIn.value = p.r; if (coIn) coIn.value = p.c;
      if (dRole) dRole.textContent = p.r; if (dCo) dCo.textContent = p.c;
      if (dAv) dAv.textContent = initials(p.n);
    }
    var idx = 0;
    function typeName(p, done) {
      if (dName) dName.classList.add("type-caret");
      var i = 0;
      (function step() {
        if (stopped) return;
        i++;
        var s = p.n.slice(0, i);
        if (nameIn) nameIn.value = s;
        if (dName) dName.textContent = s || " ";
        if (dAv) dAv.textContent = initials(p.n.slice(0, i));
        if (i < p.n.length) timers.push(setTimeout(step, 70 + Math.random() * 50));
        else { if (dName) dName.classList.remove("type-caret"); done && done(); }
      })();
    }
    function cycle() {
      if (stopped) return;
      var p = people[idx % people.length];
      setMeta(p);
      if (nameIn) nameIn.value = "";
      typeName(p, function () { timers.push(setTimeout(function () { idx++; cycle(); }, 2600)); });
    }
    if (reduce) { setMeta(people[0]); if (nameIn) nameIn.value = people[0].n; if (dName) dName.textContent = people[0].n; }
    else { timers.push(setTimeout(cycle, 1200)); }
  }

  /* ---------- Count-up stats ---------- */
  function initCount() {
    var els = [].slice.call(document.querySelectorAll("[data-count]"));
    if (!els.length) return;
    function fmt(v, dec) {
      var s = dec ? v.toFixed(dec) : Math.round(v).toString();
      var parts = s.split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    }
    function run(el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var dec = parseInt(el.getAttribute("data-dec") || "0", 10);
      var suf = el.getAttribute("data-suffix") || "";
      if (reduce) { el.textContent = fmt(target, dec) + suf; return; }
      var dur = 1500, start = performance.now();
      (function tick(now) {
        var t = Math.min(1, (now - start) / dur);
        t = 1 - Math.pow(1 - t, 3);
        el.textContent = fmt(target * t, dec) + suf;
        if (t < 1) requestAnimationFrame(tick); else el.textContent = fmt(target, dec) + suf;
      })(start);
    }
    if (!("IntersectionObserver" in window)) { els.forEach(run); return; }
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) { if (en.isIntersecting) { run(en.target); io.unobserve(en.target); } });
    }, { threshold: 0.4 });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- Marquee seamless clone ---------- */
  function initMarquee() {
    document.querySelectorAll(".marquee-track").forEach(function (t) { t.innerHTML += t.innerHTML; });
  }

  /* ---------- Magnetic buttons ---------- */
  function initMagnetic() {
    if (reduce || isTouch) return;
    document.querySelectorAll("[data-magnetic]").forEach(function (b) {
      b.addEventListener("mousemove", function (e) {
        var r = b.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        b.style.transform = "translate(" + (x * 0.22) + "px," + (y * 0.3) + "px)";
      });
      b.addEventListener("mouseleave", function () { b.style.transform = ""; });
    });
  }

  /* ---------- How-it-works animated steps ---------- */
  function initDemo() {
    var btns = [].slice.call(document.querySelectorAll(".demo-step-btn"));
    var screens = [].slice.call(document.querySelectorAll(".demo-screen"));
    if (!btns.length) return;
    var i = 0, timer;
    function set(n) {
      i = n;
      btns.forEach(function (b, k) { b.classList.toggle("active", k === n); });
      screens.forEach(function (s, k) { s.classList.toggle("active", k === n); });
    }
    function next() { set((i + 1) % btns.length); }
    btns.forEach(function (b, k) {
      b.addEventListener("click", function () { set(k); if (timer) { clearInterval(timer); if (!reduce) timer = setInterval(next, 5000); } });
    });
    set(0);
    if (!reduce) timer = setInterval(next, 5000);
  }

  /* ---------- Hero particle constellation ---------- */
  function initCanvas() {
    var cv = document.getElementById("hero-canvas");
    if (!cv || reduce || window.innerWidth < 760) { if (cv) cv.style.display = "none"; return; }
    var ctx = cv.getContext("2d");
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var pts = [], N = 42, raf, running = true, W, H;
    function size() {
      var r = cv.parentElement.getBoundingClientRect();
      W = r.width; H = r.height;
      cv.width = W * dpr; cv.height = H * dpr;
      cv.style.width = W + "px"; cv.style.height = H + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    function seed() {
      pts = [];
      for (var i = 0; i < N; i++) pts.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - 0.5) * 0.25, vy: (Math.random() - 0.5) * 0.25 });
    }
    function draw() {
      if (!running) return;
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;
        ctx.beginPath(); ctx.arc(p.x, p.y, 2, 0, 6.283);
        ctx.fillStyle = "rgba(124,77,246,.5)"; ctx.fill();
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j], dx = p.x - q.x, dy = p.y - q.y, dist = dx * dx + dy * dy;
          if (dist < 13000) {
            ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y);
            ctx.strokeStyle = "rgba(139,92,246," + (0.16 * (1 - dist / 13000)) + ")";
            ctx.lineWidth = 1; ctx.stroke();
          }
        }
      }
      raf = requestAnimationFrame(draw);
    }
    size(); seed(); draw();
    window.addEventListener("resize", function () { size(); seed(); });
    document.addEventListener("visibilitychange", function () {
      running = !document.hidden;
      if (running) { raf = requestAnimationFrame(draw); } else if (raf) { cancelAnimationFrame(raf); }
    });
  }

  /* Original animated card editor (replaces 3rd-party demo clip) */
  function initEditor() {
    var ed = document.querySelector(".editor");
    if (!ed) return;
    var cover = ed.querySelector(".ed-cover");
    var sws = [].slice.call(ed.querySelectorAll(".sw"));
    var links = [].slice.call(ed.querySelectorAll(".ed-link"));
    var photo = ed.querySelector(".ed-photocue");
    var toast = ed.querySelector(".ed-toast");
    var themes = ["t0", "t1", "t2", "t3", "t4"];
    function setTheme(i) {
      cover.className = "ed-cover " + themes[i];
      sws.forEach(function (s, k) { s.classList.toggle("active", k === i); });
    }
    if (reduce) {
      setTheme(0);
      links.forEach(function (l) { l.classList.add("in"); });
      return;
    }
    var timers = [];
    function at(ms, fn) { timers.push(setTimeout(fn, ms)); }
    function cycle() {
      timers.forEach(clearTimeout); timers = [];
      setTheme(0);
      links.forEach(function (l) { l.classList.remove("in"); });
      if (toast) toast.classList.remove("show");
      if (photo) photo.classList.remove("show");
      at(700, function () { setTheme(1); });
      at(1400, function () { setTheme(2); });
      at(2100, function () { setTheme(3); });
      at(2800, function () { setTheme(4); });
      at(3300, function () { setTheme(0); });
      if (photo) { at(2500, function () { photo.classList.add("show"); }); at(3500, function () { photo.classList.remove("show"); }); }
      at(3900, function () { if (links[0]) links[0].classList.add("in"); });
      at(4250, function () { if (links[1]) links[1].classList.add("in"); });
      at(4600, function () { if (links[2]) links[2].classList.add("in"); });
      at(4950, function () { if (links[3]) links[3].classList.add("in"); });
      if (toast) { at(5800, function () { toast.classList.add("show"); }); at(7300, function () { toast.classList.remove("show"); }); }
      at(8000, cycle);
    }
    cycle();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initMarquee();
    initEditor();
    initTilt();
    initHovTilt();
    initShowcase();
    initTyper();
    initCount();
    initMagnetic();
    initDemo();
    initCanvas();
  });
})();
