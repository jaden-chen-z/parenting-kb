#!/usr/bin/env python3
"""parenting-kb 本地开发服务器(支持 admin 写权限 + 多用户进度/收藏)。

跟 Cloudflare Pages Functions 完全一致的 API,前端代码不用切两套。

API:
  GET  /api/users                         {"users":[...]}
  PUT  /api/users        {users:[...]}    {"ok":true,"count":N}  (ADMIN_TOKEN 可选)
  GET  /api/progress?email=xxx            {"progress":{...}}
  PUT  /api/progress?email=xxx {progress} {"ok":true}
  GET  /api/progress/all                  {"progress":{email:{...},...}}  (ADMIN_TOKEN 可选)
  GET  /api/favorites?email=xxx           {"favorites":[card_id,...]}
  PUT  /api/favorites?email=xxx {favorites} {"ok":true}

数据文件:
  users.json     用户列表(同前)
  state.json     {"progress": {email:{...}}, "favorites": {email:[...]}}

启动: cd 50-frontend && python3 admin_server.py
"""

import os
import json
import threading
from urllib.parse import urlparse, parse_qs
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


PORT = 8765
ROOT = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(ROOT, 'users.json')
STATE_FILE = os.path.join(ROOT, 'state.json')

_lock = threading.Lock()


def _read_users():
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as fp:
            return json.load(fp)
    except Exception:
        return {'users': []}


def _write_users(data):
    existing = _read_users()
    existing['users'] = data.get('users', [])
    if '_comment' in data and '_comment' not in existing:
        existing['_comment'] = data['_comment']
    with open(USERS_FILE, 'w', encoding='utf-8') as fp:
        json.dump(existing, fp, ensure_ascii=False, indent=2)
        fp.write('\n')


def _read_state():
    try:
        with open(STATE_FILE, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
    except Exception:
        data = {}
    data.setdefault('progress', {})
    data.setdefault('favorites', {})
    return data


def _write_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, ensure_ascii=False, indent=2)
        fp.write('\n')


def _normalize_email(s):
    return (s or '').strip().lower()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        kwargs['directory'] = ROOT
        super().__init__(*args, **kwargs)

    def _send_json(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        try:
            length = int(self.headers.get('Content-Length', '0') or '0')
            raw = self.rfile.read(length).decode('utf-8') if length else ''
            return json.loads(raw) if raw else {}
        except Exception as e:
            return None

    def _require_admin(self):
        expected = os.environ.get('ADMIN_TOKEN') or ''
        if not expected:
            return True
        got = self.headers.get('X-PKB-Admin-Token') or ''
        if got != expected:
            self._send_json(403, {'error': 'forbidden'})
            return False
        return True

    # ── GET: 静态文件 + API ────────────────────────────
    def do_GET(self):
        u = urlparse(self.path)
        path = u.path
        qs = parse_qs(u.query)

        if path == '/api/users':
            data = _read_users()
            return self._send_json(200, {'users': data.get('users', [])})

        if path == '/api/progress':
            email = _normalize_email((qs.get('email') or [''])[0])
            if not email:
                return self.send_error(400, 'email required')
            with _lock:
                state = _read_state()
            return self._send_json(200, {'progress': state['progress'].get(email, {})})

        if path == '/api/progress/all':
            if not self._require_admin():
                return
            with _lock:
                state = _read_state()
            return self._send_json(200, {'progress': state['progress']})

        if path == '/api/favorites':
            email = _normalize_email((qs.get('email') or [''])[0])
            if not email:
                return self.send_error(400, 'email required')
            with _lock:
                state = _read_state()
            return self._send_json(200, {'favorites': state['favorites'].get(email, [])})

        return super().do_GET()

    # ── PUT: 全部 API,文件落盘 ─────────────────────────
    def do_PUT(self):
        u = urlparse(self.path)
        path = u.path
        qs = parse_qs(u.query)
        body = self._read_body()
        if body is None:
            return self.send_error(400, 'invalid json')

        if path == '/api/users':
            if not self._require_admin():
                return
            users = body.get('users')
            if not isinstance(users, list):
                return self.send_error(400, '"users" must be a list')
            for usr in users:
                if not isinstance(usr, dict) or not (usr.get('email') or '').strip():
                    return self.send_error(400, 'each user needs a non-empty email')
            _write_users({'users': users})
            return self._send_json(200, {'ok': True, 'count': len(users)})

        if path == '/api/progress':
            email = _normalize_email((qs.get('email') or [''])[0])
            if not email:
                return self.send_error(400, 'email required')
            progress = body.get('progress') or {}
            if not isinstance(progress, dict):
                return self.send_error(400, '"progress" must be an object')
            with _lock:
                state = _read_state()
                state['progress'][email] = progress
                _write_state(state)
            return self._send_json(200, {'ok': True})

        if path == '/api/favorites':
            email = _normalize_email((qs.get('email') or [''])[0])
            if not email:
                return self.send_error(400, 'email required')
            favorites = body.get('favorites') or []
            if not isinstance(favorites, list):
                return self.send_error(400, '"favorites" must be a list')
            with _lock:
                state = _read_state()
                state['favorites'][email] = [str(x) for x in favorites if x]
                _write_state(state)
            return self._send_json(200, {'ok': True})

        return self.send_error(404, 'unknown path')


if __name__ == '__main__':
    print(f'parenting-kb on :{PORT}  (cwd={ROOT})')
    print(f'  GET/PUT  /api/users')
    print(f'  GET/PUT  /api/progress?email=xxx     /api/progress/all')
    print(f'  GET/PUT  /api/favorites?email=xxx')
    ThreadingHTTPServer(('', PORT), Handler).serve_forever()
