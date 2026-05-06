// sw.js — Service Worker,把静态资源缓存到本地,二次访问几乎走本地 cache
//
// 策略:
//   - HTML:network-first(新版本优先,网断就拿 cache)
//   - 静态(.js / .json / 图片 / 字体):cache-first(已缓存直接命中,空缓存才网络)
//   - /api/*:绕开 SW(直连)
//   - 跨源(unpkg / google fonts):绕开 SW(浏览器自己缓存)
//
// 升级:改 CACHE_NAME 版本号 → 旧 cache 自动清,新 cache 重建

const CACHE_NAME = 'pkb-v1';

self.addEventListener('install', () => {
  // 不预缓存 — 第一次访问什么资源就缓存什么(避免装一个 SW 就拉 5MB)
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  // 跳过跨域(unpkg/字体 CDN 之类) + API
  if (url.origin !== self.location.origin) return;
  if (url.pathname.startsWith('/api/')) return;

  const isHTML = req.destination === 'document' ||
                  url.pathname.endsWith('.html') ||
                  url.pathname === '/' ||
                  /\/[^./]+$/.test(url.pathname);   // /Login /Cards 这种 clean URL

  if (isHTML) {
    // network-first:总拿最新 HTML(避免用户卡在旧版本)
    event.respondWith(
      fetch(req).then((res) => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => caches.match(req))
    );
  } else {
    // cache-first:静态资源命中即返
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((res) => {
          if (res.ok && (res.type === 'basic' || res.type === 'default')) {
            const copy = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(req, copy));
          }
          return res;
        });
      })
    );
  }
});
