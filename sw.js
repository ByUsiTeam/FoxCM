self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('foxcm-cache').then(function(cache) {
      return cache.addAll([
        '/',
        '/static/css/bootstrap.min.css',
        '/static/Font/css/all.css',
        '/static/js/jquery.min.js',
        '/static/js/bootstrap.bundle.min.js',
        '/static/icons/icon-192x192.png',
        '/static/icons/icon-512x512.png'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
