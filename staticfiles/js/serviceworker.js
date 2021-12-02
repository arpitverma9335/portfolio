var staticCacheName = 'prefetch';

self.addEventListener('install', function(event) {
event.waitUntil(
  caches.open(staticCacheName).then(function(cache) {
  return cache.addAll([
     '/',
     '/about',
     '/contact',
     '/blog',
  ]);
  })
);
});

self.addEventListener("fetch", event => {
    if (event.request.url === "https://varpit.herokuapp.com/") {
        event.respondWith(
            fetch(event.request).catch(err =>
                self.cache.open(cache_name).then(cache => cache.match("/"))
            )
        );
    }else if (event.request.url === "https://varpit.herokuapp.com/about") {
        event.respondWith(
            fetch(event.request).catch(err =>
                self.cache.open(cache_name).then(cache => cache.match("/about"))
            )
        );
    }else if (event.request.url === "https://varpit.herokuapp.com/contact") {
        event.respondWith(
            fetch(event.request).catch(err =>
                self.cache.open(cache_name).then(cache => cache.match("/contact"))
            )
        );
    }else if (event.request.url === "https://varpit.herokuapp.com/blog") {
        event.respondWith(
            fetch(event.request).catch(err =>
                self.cache.open(cache_name).then(cache => cache.match("/blog"))
            )
        );
    }else {
        event.respondWith(
            fetch(event.request).catch(err =>
                caches.match(event.request).then(response => response)
            )
        );
    }
});

