/* CompanyCard PWA service worker — cache the app shell for offline + installability.
   (Active only when the app is served over http(s)/localhost or wrapped natively.) */
const CACHE = "companycard-v3";
const SHELL = [
  "mobile.html", "mobile.css", "product.js", "app.css", "config.js", "auth.js",
  "../assets/styles.css", "../assets/logo-primary.svg", "../assets/logo-white.svg", "../assets/logo-icon.svg",
  "../assets/png/logo-icon-256.png", "../assets/png/favicon-512.png",
  "manifest.webmanifest"
];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(SHELL); }).catch(function () {}));
  self.skipWaiting();
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }));
  self.clients.claim();
});

/* cache-first, falling back to network, then to the shell for navigations */
self.addEventListener("fetch", function (e) {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request).then(function (hit) {
      return hit || fetch(e.request).then(function (resp) {
        var copy = resp.clone();
        caches.open(CACHE).then(function (c) { c.put(e.request, copy); }).catch(function () {});
        return resp;
      }).catch(function () {
        if (e.request.mode === "navigate") return caches.match("mobile.html");
      });
    })
  );
});
