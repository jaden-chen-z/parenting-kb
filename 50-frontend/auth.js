// auth.js — 多用户共享 helper(挂全局 window.PKB)
//   - currentUser():     当前登录邮箱(小写),无则 null
//   - login(email):      标记登录(localStorage)
//   - logout():          清登录态
//   - requireLogin():    页面顶部守卫,没登录就 redirect Login.html
//   - dataKey(scope):    返回 per-user localStorage key,如 'baby-cards.jaden@x.com.favorites'
//   - readJSON / writeJSON: per-user 包装(自动加 dataKey 前缀)
//
// 设计:用户标识用邮箱本身(已登录态由 currentUser localStorage 标志)。
// 同一台机器多账号时数据按 email 分桶不冲突。
(function (global) {
  const KEY_USER = 'baby-cards.currentUser';
  const KEY_ADMIN = 'baby-cards.adminMode';

  function currentUser() {
    try { return (localStorage.getItem(KEY_USER) || '').trim().toLowerCase() || null; }
    catch (e) { return null; }
  }
  function login(email) {
    try {
      localStorage.setItem(KEY_USER, String(email || '').trim().toLowerCase());
      localStorage.removeItem(KEY_ADMIN);   // 普通登录退出 admin 模式
      sessionStorage.removeItem('baby-cards.adminToken');
    } catch (e) {}
  }
  function logout() {
    try {
      localStorage.removeItem(KEY_USER);
      localStorage.removeItem(KEY_ADMIN);
      sessionStorage.removeItem('baby-cards.adminToken');
    } catch (e) {}
  }
  function isAdmin() {
    try { return localStorage.getItem(KEY_ADMIN) === '1'; }
    catch (e) { return false; }
  }
  function loginAdmin(token) {
    try {
      localStorage.setItem(KEY_ADMIN, '1');
      if (token) sessionStorage.setItem('baby-cards.adminToken', String(token));
      localStorage.removeItem(KEY_USER);    // admin 不算普通 user
    } catch (e) {}
  }
  function adminToken() {
    try { return sessionStorage.getItem('baby-cards.adminToken') || ''; }
    catch (e) { return ''; }
  }
  function requireLogin() {
    if (!currentUser()) {
      const here = location.pathname.split('/').pop() || '';
      if (here !== 'Login.html') location.replace('Login.html');
      return false;
    }
    return true;
  }
  function requireAdmin() {
    if (!isAdmin()) {
      const here = location.pathname.split('/').pop() || '';
      if (here !== 'Login.html') location.replace('Login.html');
      return false;
    }
    if (!adminToken()) {
      const token = window.prompt('请输入管理员密码');
      if (!token || !token.trim()) {
        logout();
        const here = location.pathname.split('/').pop() || '';
        if (here !== 'Login.html') location.replace('Login.html');
        return false;
      }
      loginAdmin(token.trim());
    }
    return true;
  }
  function dataKey(scope) {
    const u = currentUser() || 'anon';
    return `baby-cards.${u}.${scope}`;
  }
  function readJSON(scope, fallback) {
    try {
      const raw = localStorage.getItem(dataKey(scope));
      if (raw == null) return fallback;
      return JSON.parse(raw);
    } catch (e) { return fallback; }
  }
  function writeJSON(scope, value) {
    try { localStorage.setItem(dataKey(scope), JSON.stringify(value)); } catch (e) {}
  }

  global.PKB = global.PKB || {};
  global.PKB.auth = {
    currentUser, login, logout, requireLogin,
    isAdmin, loginAdmin, adminToken, requireAdmin,
    dataKey, readJSON, writeJSON,
  };

  // ── PKB.api ─────────────────────────────────────────────
  // 统一封装 server / Cloudflare 端的接口。本地 admin_server.py 和云端
  // Functions(functions/api/*.js)实现完全相同的 API,所以前端切换 host 透明。
  //
  //   GET  /api/users                       → { users:[{email,name},...] }
  //   PUT  /api/users        { users }      → { ok, count }
  //   GET  /api/progress?email=xxx          → { progress:{ "stage:S1":5, ... } }
  //   PUT  /api/progress?email=xxx { progress } → { ok }
  //   GET  /api/progress/all                → { progress:{ email:{ ... } } }  (admin 用)
  //   GET  /api/favorites?email=xxx         → { favorites:[card_id,...] }
  //   PUT  /api/favorites?email=xxx { favorites } → { ok }
  function _enc(e) { return encodeURIComponent(String(e || '').trim().toLowerCase()); }
  function _adminHeaders(extra) {
    const headers = Object.assign({}, extra || {});
    const token = adminToken();
    if (token) headers['X-PKB-Admin-Token'] = token;
    return headers;
  }
  async function _json(res) {
    if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
    return res.json();
  }
  global.PKB.api = {
    getUsers:       ()        => fetch('/api/users').then(_json),
    putUsers:       (users)   => fetch('/api/users', { method:'PUT', headers:_adminHeaders({'Content-Type':'application/json'}), body: JSON.stringify({ users }) }).then(_json),
    getProgress:    (email)   => fetch(`/api/progress?email=${_enc(email)}`).then(_json),
    putProgress:    (email, p) => fetch(`/api/progress?email=${_enc(email)}`, { method:'PUT', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ progress: p }) }).then(_json),
    getAllProgress: ()        => fetch('/api/progress/all', { headers:_adminHeaders() }).then(_json),
    getFavorites:   (email)   => fetch(`/api/favorites?email=${_enc(email)}`).then(_json),
    putFavorites:   (email, f) => fetch(`/api/favorites?email=${_enc(email)}`, { method:'PUT', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ favorites: f }) }).then(_json),
  };
})(window);
