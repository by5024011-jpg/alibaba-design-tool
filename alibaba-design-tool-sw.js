// Service Worker for Alibaba Design Tool
// Caches the main HTML + manifest for offline use
const CACHE = 'alibaba-design-v2';
const FILES = [
  './',
  './index.html',
  './alibaba-design-tool-prototype-v2.html',
  './alibaba-design-tool-manifest.json'
];

// Install: cache core files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(FILES))
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE).map(k => caches.delete(k))
    ))
  );
  self.clients.claim();
});

// Fetch: cache-first strategy for core files, network-first for others
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  // Only handle same-origin requests
  if (url.origin !== self.location.origin) return;

  // Cache-first for known static files
  if (FILES.some(f => f === './' ? url.pathname === '/' : url.pathname.endsWith(f.replace('./', '')))) {
    event.respondWith(
      caches.match(event.request).then(cached => cached || fetch(event.request))
    );
    return;
  }

  // Network-first for everything else (fallback to cache)
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
