// sw.js — Service Worker
//
// 策略:
//   - HTML / clean URL:network-first(总拉新,网断走 cache)
//   - cards.json / glossary.json:stale-while-revalidate(立即返 cache + 后台更新)
//                                  → 第一次访问后,二次起秒开;数据改了下次刷新才看到新版
//   - 其他静态(.js / vendor/*):cache-first
//   - /api/*:绕开 SW(直连)
//
// Cache key 剥掉 ?t= / ?v= query string —— cards.jsx 用 ?t=Date.now() 绕 iOS 缓存,
// 但同样会让 SW miss。SW 内部统一用 path-only cache key,实际请求保持原 URL。

const CACHE_NAME = 'pkb-v3';

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Cache key 只剥 ?t= (cards.json/glossary.json 的 Date.now() 时间戳 cache buster),
// 保留 ?v=(jsx 显式版本号 — v23 vs v24 是不同代码,必须区分)。
// 没区分会让 SW 在改 jsx 后还命中旧版本,部署完用户拿不到新代码。
function cacheKey(url) {
  const u = new URL(url);
  u.searchParams.delete('t');
  u.hash = '';
  return new Request(u.toString());
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.startsWith('/api/')) return;

  const isHTML = req.destination === 'document' ||
                  url.pathname.endsWith('.html') ||
                  url.pathname === '/' ||
                  /^\/[^./]+$/.test(url.pathname);    // 干净 URL 如 /Login /Cards

  // 数据 JSON 用 stale-while-revalidate(立即返 cache,后台静默更新)
  const isData = url.pathname.endsWith('cards.json') || url.pathname.endsWith('glossary.json');

  const key = cacheKey(req.url);

  if (isHTML) {
    // network-first
    event.respondWith(
      fetch(req).then((res) => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(key, copy));
        }
        return res;
      }).catch(() => caches.match(key))
    );
    return;
  }

  if (isData) {
    // stale-while-revalidate
    event.respondWith(
      caches.match(key).then((cached) => {
        const fetchPromise = fetch(req).then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(key, copy));
          }
          return res;
        }).catch(() => null);
        return cached || fetchPromise;
      })
    );
    return;
  }

  // 其他静态:cache-first
  event.respondWith(
    caches.match(key).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        if (res.ok && (res.type === 'basic' || res.type === 'default')) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(key, copy));
        }
        return res;
      });
    })
  );
});
