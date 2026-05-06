// Cloudflare Pages Functions — /api/users 路由
//
// 在 Cloudflare Pages 项目里需要一个 KV namespace 绑定:
//   Variable name: USERS_KV
//   KV namespace : (在 Pages Settings → Functions → KV namespace bindings 里创建)
//
// 数据结构:KV key "users" → value 是 JSON 字符串 {"users":[{email,name},...]}
//
// API:
//   GET  /api/users          → 200 {"users":[...]}
//   PUT  /api/users  body    → 200 {"ok":true,"count":N}
//                              body = {"users":[{"email":"...","name":"..."}]}
//
// 首次部署 KV 空时 GET 返回 {"users":[]}。第一次 PUT 成功后,前端 Login 页就能登录。
// 也可以在 Cloudflare 控制台 KV 直接写入初始值跳过 admin 步骤。

const KV_KEY = 'users';

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
    },
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
  const kv = context.env.USERS_KV;
  if (!kv) return jsonResponse({ error: 'USERS_KV not bound' }, 500);
  const raw = await kv.get(KV_KEY);
  if (!raw) return jsonResponse({ users: [] });
  try {
    const data = JSON.parse(raw);
    return jsonResponse({ users: Array.isArray(data.users) ? data.users : [] });
  } catch (e) {
    return jsonResponse({ users: [] });
  }
}

export async function onRequestPut(context) {
  const denied = requireAdmin(context);
  if (denied) return denied;
  const kv = context.env.USERS_KV;
  if (!kv) return jsonResponse({ error: 'USERS_KV not bound' }, 500);
  let payload;
  try {
    payload = await context.request.json();
  } catch (e) {
    return jsonResponse({ error: 'invalid json' }, 400);
  }
  if (!payload || !Array.isArray(payload.users)) {
    return jsonResponse({ error: 'payload must be { "users": [...] }' }, 400);
  }
  for (const u of payload.users) {
    if (!u || typeof u !== 'object' || !(u.email || '').trim()) {
      return jsonResponse({ error: 'each user needs a non-empty email' }, 400);
    }
  }
  await kv.put(KV_KEY, JSON.stringify({ users: payload.users }));
  return jsonResponse({ ok: true, count: payload.users.length });
}

// 不允许其他方法
export async function onRequest(context) {
  return jsonResponse({ error: 'Method Not Allowed' }, 405);
}
