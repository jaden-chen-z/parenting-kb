// Cloudflare Pages Function — /api/progress/all
// 列出所有用户的 progress(admin 看进度用)。KV.list() 拿 progress:* 前缀的所有 key。

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' },
  });
}

function requireAdmin(context) {
  const expected = context.env.ADMIN_TOKEN;
  if (!expected) return null;
  const got = context.request.headers.get('x-pkb-admin-token') || '';
  if (got !== expected) return jsonResponse({ error: 'forbidden' }, 403);
  return null;
}

export async function onRequestGet(context) {
  const denied = requireAdmin(context);
  if (denied) return denied;
  const kv = context.env.STATE_KV;
  if (!kv) return jsonResponse({ error: 'STATE_KV not bound' }, 500);

  const out = {};
  let cursor;
  do {
    const list = await kv.list({ prefix: 'progress:', cursor, limit: 1000 });
    for (const item of list.keys) {
      const email = item.name.slice('progress:'.length);
      const raw = await kv.get(item.name);
      if (!raw) continue;
      try { out[email] = JSON.parse(raw) || {}; } catch (e) {}
    }
    cursor = list.list_complete ? null : list.cursor;
  } while (cursor);

  return jsonResponse({ progress: out });
}
