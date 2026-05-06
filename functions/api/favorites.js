// Cloudflare Pages Function — /api/favorites
// KV 绑定:STATE_KV
// KV key 格式:`favorites:{email}` → JSON [card_id, ...] (有顺序)

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' },
  });
}

function emailFromQuery(url) {
  const u = new URL(url);
  const e = (u.searchParams.get('email') || '').trim().toLowerCase();
  return e || null;
}

export async function onRequestGet(context) {
  const kv = context.env.STATE_KV;
  if (!kv) return jsonResponse({ error: 'STATE_KV not bound' }, 500);
  const email = emailFromQuery(context.request.url);
  if (!email) return jsonResponse({ error: 'email required' }, 400);
  const raw = await kv.get(`favorites:${email}`);
  let favorites = [];
  if (raw) { try { const v = JSON.parse(raw); if (Array.isArray(v)) favorites = v; } catch (e) {} }
  return jsonResponse({ favorites });
}

export async function onRequestPut(context) {
  const kv = context.env.STATE_KV;
  if (!kv) return jsonResponse({ error: 'STATE_KV not bound' }, 500);
  const email = emailFromQuery(context.request.url);
  if (!email) return jsonResponse({ error: 'email required' }, 400);
  let body;
  try { body = await context.request.json(); }
  catch (e) { return jsonResponse({ error: 'invalid json' }, 400); }
  const favorites = body && body.favorites;
  if (!Array.isArray(favorites)) return jsonResponse({ error: '"favorites" must be a list' }, 400);
  await kv.put(`favorites:${email}`, JSON.stringify(favorites.map(String)));
  return jsonResponse({ ok: true });
}
