// Cloudflare Pages Function — /api/progress
// KV 绑定:STATE_KV(在 Pages Settings → Functions → KV bindings 添加)
//
// KV key 格式:`progress:{email}` → JSON {stage:S0: idx, stage:S1: idx, favorites: idx, ...}
// admin /api/progress/all 路由由 functions/api/progress/all.js 处理

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
  const raw = await kv.get(`progress:${email}`);
  let progress = {};
  if (raw) { try { progress = JSON.parse(raw) || {}; } catch (e) {} }
  return jsonResponse({ progress });
}

export async function onRequestPut(context) {
  const kv = context.env.STATE_KV;
  if (!kv) return jsonResponse({ error: 'STATE_KV not bound' }, 500);
  const email = emailFromQuery(context.request.url);
  if (!email) return jsonResponse({ error: 'email required' }, 400);
  let body;
  try { body = await context.request.json(); }
  catch (e) { return jsonResponse({ error: 'invalid json' }, 400); }
  const progress = body && body.progress;
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) {
    return jsonResponse({ error: '"progress" must be an object' }, 400);
  }
  await kv.put(`progress:${email}`, JSON.stringify(progress));
  return jsonResponse({ ok: true });
}
