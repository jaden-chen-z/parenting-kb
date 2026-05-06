// admin.jsx — 管理员页面
//   - 当前用户列表(序号 + 邮箱 + 已读卡数)
//   - 增加成员(prompt 输入邮箱)
//   - 删除成员(每行 ✕,二次 confirm)
//   - 写盘:PUT users.json(由 admin_server.py 处理)

// 拉用户列表 — 走 /api/users
function useUsersAdmin() {
  const [users, setUsers] = React.useState(null);
  const [err, setErr] = React.useState(null);
  const refresh = React.useCallback(() => {
    fetch('/api/users?_t=' + Date.now())
      .then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then((j) => setUsers(Array.isArray(j && j.users) ? j.users : []))
      .catch((e) => { setErr(e); setUsers([]); });
  }, []);
  React.useEffect(refresh, [refresh]);
  return { users, err, refresh, setUsers };
}

// 把一个 progress 对象(stage:S0:idx, stage:S1:idx, ...)折算成"已读总卡数"。
// favorites scope 不计(它不是新卡片,只是收藏夹位置)。
function sumSeenFromProgress(progress) {
  if (!progress || typeof progress !== 'object') return null;
  let sum = 0; let any = false;
  for (const k of Object.keys(progress)) {
    if (k.indexOf('stage:') === 0) {
      const v = progress[k];
      if (typeof v === 'number' && v >= 0) { sum += v + 1; any = true; }
    }
  }
  return any ? sum : null;
}

async function saveUsers(users) {
  if (!window.PKB || !PKB.api) throw new Error('API 未加载');
  return PKB.api.putUsers(users);
}

function App() {
  const { users, err: usersErr, refresh, setUsers } = useUsersAdmin();
  const [busy, setBusy] = React.useState(false);
  const [flash, setFlash] = React.useState(null);     // { kind:'ok'|'err', msg }
  // 拉所有人进度(admin 视角,跨设备数据)
  const [allProgress, setAllProgress] = React.useState({});
  React.useEffect(() => {
    if (!window.PKB || !PKB.api) return;
    PKB.api.getAllProgress()
      .then((j) => setAllProgress(j.progress || {}))
      .catch(() => {});
  }, [users]);     // 用户列表变了重拉,保持新鲜

  const showFlash = (kind, msg) => {
    setFlash({ kind, msg });
    setTimeout(() => setFlash(null), 3500);
  };

  const onAdd = async () => {
    const input = window.prompt('请输入新成员的邮箱地址(必须含 @)');
    if (input == null) return;
    const v = input.trim().toLowerCase();
    if (!v) return;
    if (v === 'admin') { showFlash('err', '"admin" 是保留字,不能作为邮箱'); return; }
    if (!/^.+@.+\..+$/.test(v)) { showFlash('err', '邮箱格式不对,需要含 @ 和域名'); return; }
    if (users.some((u) => (u.email || '').trim().toLowerCase() === v)) {
      showFlash('err', '该邮箱已存在: ' + v);
      return;
    }
    const name = (input.split('@')[0] || '').trim() || v;
    const next = [...users, { email: v, name }];
    setBusy(true);
    try {
      await saveUsers(next);
      setUsers(next);
      showFlash('ok', '已添加: ' + v);
    } catch (e) {
      showFlash('err', '保存失败 — ' + e.message);
    } finally { setBusy(false); }
  };

  const onDelete = async (email) => {
    if (!window.confirm(`确认删除成员邮箱:\n\n${email}\n\n该用户的本地进度 / 收藏数据不会被删除,但他将无法再登录。`)) return;
    const next = users.filter((u) => (u.email || '').trim().toLowerCase() !== email);
    setBusy(true);
    try {
      await saveUsers(next);
      setUsers(next);
      showFlash('ok', '已删除: ' + email);
    } catch (e) {
      showFlash('err', '保存失败 — ' + e.message);
    } finally { setBusy(false); }
  };

  const onLogout = () => {
    PKB.auth.logout();
    location.replace('/');
  };

  return (
    <div className="page">
      {/* 顶部条 */}
      <div className="topbar">
        <div className="brand">
          <div className="title">管理员 · <span className="accent">用户</span></div>
          <div className="sub">ADMIN · MEMBERS</div>
        </div>
        <button className="logout" onClick={onLogout}>登出</button>
      </div>

      {/* 列表 */}
      <div className="card">
        <div className="card-head">
          <div className="head-left">成员列表 <span className="count">{users ? users.length : '…'}</span></div>
          <button className="add" onClick={onAdd} disabled={busy || !users}>+ 添加成员</button>
        </div>

        {usersErr && (
          <div className="row err">载入失败:{String(usersErr.message)}</div>
        )}
        {users && users.length === 0 && (
          <div className="row empty">暂无成员,点击"添加成员"创建第一个</div>
        )}
        {users && users.map((u, i) => {
          const email = (u.email || '').trim().toLowerCase();
          const seen = sumSeenFromProgress(allProgress[email]);
          return (
            <div className="row" key={email}>
              <span className="idx">{String(i + 1).padStart(2, '0')}</span>
              <div className="info">
                <div className="email">{u.email}</div>
                {u.name && <div className="name">{u.name}</div>}
              </div>
              <div className="seen">
                {seen == null
                  ? <span className="dim">— 张</span>
                  : <span>{seen} <small>张已读</small></span>}
              </div>
              <button className="del" onClick={() => onDelete(email)} disabled={busy}>✕</button>
            </div>
          );
        })}

        {flash && (
          <div className={'flash ' + flash.kind}>{flash.msg}</div>
        )}

        <div className="footer-note">
          * 已读张数从服务器进度数据汇总,跨设备实时反映该成员的最远阅读位置。
        </div>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
