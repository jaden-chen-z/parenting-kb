# 部署到 Cloudflare Pages

域名: **www.chenyunen.dev**(在 Cloudflare 注册或迁入,域名管理一并放 Cloudflare 最方便)

## 一次性配置(30 分钟)

### 1. 推 GitHub
```bash
cd ~/Desktop/parenting-kb
git init
git add -A && git commit -m "init"
# 在 github.com 创建一个仓库 parenting-kb(私有也行),然后:
git remote add origin git@github.com:YOUR_NAME/parenting-kb.git
git push -u origin main
```

### 2. Cloudflare 开 Pages 项目

1. 登录 https://dash.cloudflare.com
2. 左侧 **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
3. 授权 GitHub,选 `parenting-kb` 仓库
4. 部署设置:
   - **Production branch**: `main`
   - **Build command**: 留空
   - **Build output directory**: `50-frontend`
5. **Save and Deploy**

第一次部署会成(静态文件能渲染),但 API 还不行 — 还没绑 KV。

### 3. 创建 2 个 KV namespace

Cloudflare 左侧 **Workers & Pages** → **KV** → **Create a namespace** 各做一个:

| Namespace 名 | 用途 |
|---|---|
| `parenting-kb-users` | 存用户列表 |
| `parenting-kb-state` | 存进度 + 收藏 |

### 4. Pages 项目绑定 KV

回到 Pages 项目 → **Settings** → **Functions** → **KV namespace bindings** → **Add binding** 各加一条:

| Variable name | KV namespace |
|---|---|
| `USERS_KV` | `parenting-kb-users` |
| `STATE_KV` | `parenting-kb-state` |

**Variable name 必须严格对齐 functions/api/*.js 里的引用**。

### 5. Retry deployment
Pages 项目 → **Deployments** → 最新一次 → **Retry deployment**(KV 绑完才能让 Functions 跑起来)

部署完成会拿到默认域名 `parenting-kb-xxx.pages.dev`,先用它访问 `/Login.html` 测试。

### 6. 绑定自定义域名 www.chenyunen.dev

1. 域名先在 Cloudflare 加站(Add site)
2. Pages 项目 → **Custom domains** → **Set up a custom domain**
3. 输 `www.chenyunen.dev`
4. Cloudflare 自动加 DNS CNAME + 签 SSL
5. 等 1-5 分钟生效

如果你也想 `chenyunen.dev`(不带 www)可访问:
- 加一个 redirect rule:`chenyunen.dev` → `https://www.chenyunen.dev`

### 7. 创建第一个用户

访问 `https://www.chenyunen.dev/Login.html`:
1. 邮箱框输入 `Admin` → **进入 →**
2. **+ 添加成员** → 输入你自己的邮箱
3. 退出 → 用刚加的邮箱登录使用

**或者**直接在 KV 里写入(技术方式):
- Cloudflare → KV → `parenting-kb-users` → `+`
  - Key: `users`
  - Value: `{"users":[{"email":"jadenttk@gmail.com","name":"Jaden"}]}`

## 后续维护

### 改卡片 / 词典数据
```bash
# 本地改 30-cards/*.yaml 或 40-glossary/*.yaml 后:
cd 50-frontend
python3 build_cards_json.py    # 重新生成 cards.json + glossary.json
git add -A && git commit -m "update cards"
git push
# Cloudflare Pages 检测到 push 自动重新部署(2-3 分钟生效)
```

### 改前端代码
同样 push 即可。

### 加 / 删用户
先在 Cloudflare Pages 环境变量里配置 `ADMIN_TOKEN`,再到 `https://www.chenyunen.dev/Login.html` 输 `Admin`,按提示输入管理员密码进管理页操作 → 数据写 `USERS_KV`,所有人立即生效。

### 看用户进度
管理员页面已经显示每个用户的"已读 N 张"(从 `STATE_KV` 实时取)。

## API 总览

| 路径 | 方法 | 用途 | KV |
|---|---|---|---|
| `/api/users` | GET / PUT | 用户列表 | `USERS_KV` |
| `/api/progress?email=xxx` | GET / PUT | 单用户进度 | `STATE_KV` |
| `/api/progress/all` | GET | 所有用户进度(admin)| `STATE_KV` |
| `/api/favorites?email=xxx` | GET / PUT | 单用户收藏 | `STATE_KV` |

本地 `admin_server.py` 实现完全相同的接口(数据落盘到 `users.json` + `state.json`),所以本地 / 云端代码一套。

## 限制 & 注意

- **Admin 入口需要密码**:线上必须配置 `ADMIN_TOKEN`。管理页写用户列表和读取全员进度都会带 `X-PKB-Admin-Token`,服务端校验通过才放行。
- **KV 免费额度**:100k 读 / 1k 写 / 1GB 存储。20 用户场景每天日均几百次写,远低于阈值。
- **数据迁移**:本地的 `users.json` / `state.json` 是单独的;你部署上去后,KV 里是空的,需要重新通过 Admin 加用户(或一次性把 users.json 内容粘到 KV 的 `users` key)。
- **Cloudflare 大陆访问**:速度比国内服务器慢,但比海外快得多。一般 100-300ms,体验流畅。
