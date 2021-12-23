var staticCacheName = 'prefetch';

self.addEventListener('install', function(event) {
event.waitUntil(
  caches.open(staticCacheName).then(function(cache) {
  return cache.addAll([
     '/',
     '/static/img/arpit_profile.909ee3d5a21b.webP',
     '/static/CACHE/css/output.c78c9cfed031.css',
     '/static/CACHE/js/output.4070f1273341.js',
     '/static/img/banner/banner-2.a2f6506de9b8.jpg?fc5f1c54e8f5',
     '/static/img/blog/feature-img1.fe76cd61d447.jpeg2000',
  ]);
  })
);
});

self.addEventListener("fetch", event => {
    event.respondWith(
            fetch(event.request).catch(err =>
                caches.match(event.request).then(response => response)
            )
        );
});