// login.jsx — 登录页 React 应用
// 验证邮箱在 users.json 列表里就放行 + localStorage 记当前用户

// 拉取允许登录的用户列表 — 走 /api/users(本地 admin_server.py 和 Cloudflare
// Functions 都实现了这个接口),失败时降级 fetch 静态 users.json(部署在没 API
// 的纯静态环境也能跑)
function useUsers() {
  const [users, setUsers] = React.useState(null);
  const [err, setErr] = React.useState(null);
  React.useEffect(() => {
    fetch('/api/users')
      .then((r) => r.ok ? r.json() : null)
      .then((j) => {
        if (j && Array.isArray(j.users)) return setUsers(j.users);
        // 降级:静态 users.json
        return fetch('users.json')
          .then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
          .then((j2) => setUsers((j2 && j2.users) || []));
      })
      .catch((e) => { setErr(e); setUsers([]); });
  }, []);
  return { users, err };
}

const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "card1X": 128,
  "card1Y": -23,
  "card1W": 191,
  "card1H": 96,
  "card1Rot": -10,
  "card1Color": "#EFE8D2",
  "card2X": 189,
  "card2Y": 14,
  "card2W": 185,
  "card2H": 96,
  "card2Rot": -9,
  "card2Color": "#C7D1B5"
}/*EDITMODE-END*/;

function PeekCard({ x, y, w, h, rot, color }) {
  return (
    <div className="peek-card" style={{
      left: x, top: y, width: w, height: h,
      transform: `rotate(${rot}deg)`,
      background: color,
    }}>
      <div className="grain"></div>
      <div className="lines"><i></i><i></i><i></i></div>
    </div>
  );
}

function App() {
  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);
  const { users, err: usersErr } = useUsers();
  const [email, setEmail] = React.useState('');
  const [error, setError] = React.useState(null);

  // 已登录(普通 / 管理员)直接放行 — 避免登录页把已登录用户卡住
  React.useEffect(() => {
    if (PKB.auth.isAdmin()) location.replace('Admin.html');
    else if (PKB.auth.currentUser()) location.replace('Stage Folders.html');
  }, []);

  const onSubmit = (e) => {
    e.preventDefault();
    setError(null);
    const raw = (email || '').trim();
    const v = raw.toLowerCase();
    if (!raw) { setError('请输入邮箱'); return; }
    // 管理员入口:输入 "Admin"(任何大小写)→ 跳管理员页
    if (v === 'admin') {
      const token = window.prompt('请输入管理员密码');
      if (!token || !token.trim()) return;
      PKB.auth.loginAdmin(token.trim());
      location.replace('Admin.html');
      return;
    }
    if (users == null) { setError('用户列表加载中,稍候...'); return; }
    if (usersErr) { setError('用户列表加载失败,请确认 users.json 存在'); return; }
    const found = users.find((u) => (u.email || '').trim().toLowerCase() === v);
    if (!found) { setError('未注册的邮箱,请检查后重试'); return; }
    PKB.auth.login(v);
    location.replace('Stage Folders.html');
  };

  return (
    <div className="page">
      <div className="plate">
        <div className="name">Jaden 的<span className="accent">育儿</span>知识库</div>
        <div className="en">Jaden's Parenting Knowledge Base</div>
      </div>

      <div className="stack">
        {/* 卡片层(图层在文件夹下面) */}
        <div className="peek-cards">
          <PeekCard x={t.card2X} y={t.card2Y} w={t.card2W} h={t.card2H} rot={t.card2Rot} color={t.card2Color} />
          <PeekCard x={t.card1X} y={t.card1Y} w={t.card1W} h={t.card1H} rot={t.card1Rot} color={t.card1Color} />
        </div>

        {/* 文件夹 */}
        <div className="folder">
          <svg className="shape" viewBox="0 0 396 280" preserveAspectRatio="none">
            <defs>
              <filter id="paper-grain" x="0" y="0" width="100%" height="100%">
                <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7"/>
                <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.18 0"/>
                <feComposite in2="SourceGraphic" operator="in"/>
              </filter>
              <linearGradient id="folder-hl" x1="0" x2="0" y1="0" y2="1">
                <stop offset="0" stopColor="rgba(0,0,0,0.18)"/>
                <stop offset="1" stopColor="rgba(0,0,0,0)"/>
              </linearGradient>
            </defs>
            <path id="fpath" d="M 0 60 L 0 18 Q 0 0 18 0 L 150 0 Q 168 0 174 14 L 180 38 Q 186 48 200 48 L 378 48 Q 396 48 396 66 L 396 262 Q 396 280 378 280 L 18 280 Q 0 280 0 262 Z" fill="#EAD79A"/>
            <use href="#fpath" fill="url(#folder-hl)" opacity="0.32"/>
            <use href="#fpath" fill="#000" filter="url(#paper-grain)"/>
            <path d="M 0 18 Q 0 0 18 0 L 150 0 Q 168 0 174 14 L 180 38 Q 184 46 192 47 L 192 48 L 0 48 Z" fill="#D9C383" opacity="0.7"/>
            <path d="M 6 47 L 174 47 Q 184 47 188 44" stroke="#5a2a20" strokeWidth="1" fill="none" opacity="0.35"/>
            <text className="tab-text" x="22" y="32">项目情况</text>
          </svg>

          <div className="body-overlay">
            <div className="row">
              <div className="k">输入字符总量</div>
              <div className="v">42,700,000+</div>
            </div>
            <div className="row">
              <div className="k">卡片字符总量</div>
              <div className="v">4,100,000+</div>
            </div>
            <div className="note">
              * 1 汉字 = 1 字符;1 英文字母 = 1 字符<br/>
              * 数据持续更新
            </div>
          </div>
        </div>
      </div>

      <div className="login">
        {/* noValidate 关掉浏览器原生 "请填写此字段" tooltip,改走我们自己的 .login-error 提示
            (跟项目排版/字体/颜色一致) */}
        <form className={'field' + (error ? ' has-error' : '')} onSubmit={onSubmit} noValidate>
          <input
            type="email"
            name="email"
            placeholder="your@email.com"
            autoComplete="email"
            value={email}
            onChange={(e) => { setEmail(e.target.value); if (error) setError(null); }}
          />
          <button type="submit">进入 →</button>
        </form>
        {error && <div className="login-error">{error}</div>}
      </div>

      <TweaksPanel>
        <TweakSection label="前面那张卡片(米白)" />
        <TweakColor label="颜色" value={t.card1Color} onChange={(v)=>setTweak('card1Color', v)} />
        <TweakSection label="后面那张卡片(苔绿)" />
        <TweakColor label="颜色" value={t.card2Color} onChange={(v)=>setTweak('card2Color', v)} />
      </TweaksPanel>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
