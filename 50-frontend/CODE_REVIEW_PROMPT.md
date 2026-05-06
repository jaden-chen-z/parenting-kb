# 前端代码审查任务 · parenting-kb 知识卡 Web 端

> **给 Codex / 任何 AI 代码审查工具的完整 Prompt**
>
> 复制本文件全部内容(或挂载本文件路径)给审查工具,工具会照此审一遍。

---

## 1. 你的任务

审查这个项目的前端代码,**输出 2 类发现**:

1. **Bug**:逻辑错误 / 边界条件漏洞 / 内存泄漏 / 竞态条件 / 跨浏览器兼容问题
2. **同效更优实现**:在保持现有视觉 + 交互完全不变的前提下,用更高效 / 更稳定 / 更可维护的方式重写。

每条发现都要给:
- 文件路径 + 行号
- 现状代码片段
- 问题类型(Bug / Perf / Stability / Maintainability)
- 严重度(P0 用户可见崩溃 / P1 性能或潜在 bug / P2 代码质量)
- **可粘贴的修复 patch**(diff 格式或完整新代码段)
- 改动后预期效果(为什么更好)

---

## 2. 项目概览

**parenting-kb**:个人维护的中文育儿知识库前端,展示 1408 张 YAML 卡片 + 812 个术语词条。

**核心交互**:
1. **Login**:本地用户名 + 密码登录(localStorage scope 隔离每用户的收藏 / 进度)
2. **Stage Folders**:9 阶段(S0-S8 即孕期到 6 岁)文件夹堆叠,纸质风格,横向手势切换
3. **Cards**:卡片栈,单段内 N 张卡上下滑,内含 lede / body / 行动列表 / 误区 / 立场对照 / 引用底栏
4. **Favorites**:收藏夹,跨段聚合
5. **Admin**:管理面板(切换主题 / 调试)

**用户场景**:作者本人 + 妻子,主用 iOS Safari + macOS Safari/Chrome,本地 LAN 访问(`192.168.86.x:8765`),不公网。

---

## 3. 技术栈与约束

```
React 18.3.1            通过 unpkg CDN 引,umd 全局 React
@babel/standalone 7.29  浏览器内 Babel 把 .jsx 实时编译(无构建链)
zero build              纯静态文件,无 npm install / webpack / vite
Python 3.12             build_cards_json.py 把 yaml → cards.json + glossary.json
浏览器目标               iOS Safari ≥ 16, macOS Safari ≥ 16, Chrome 最新
fetch                   cards.json + glossary.json 异步加载,?t=Date.now() 缓存破坏
localStorage            per-user 收藏 / 进度持久化
SVG inline              文件夹形状 + drop-shadow filter 全部内联
inline style            React 组件全部用 style={{...}} 内联,无 CSS 文件 / styled-components
```

**硬性约束(改动方案必须遵守)**:

- ❌ **不能引构建链**(用户拒绝维护 npm / webpack)— 仍需要浏览器内 Babel + UMD React
- ❌ **不能换框架**(不上 Vue / Svelte / Solid)
- ❌ **不能换状态管理**(不上 Redux / Zustand / Jotai)
- ❌ **不能依赖额外 npm 包**(除非该包能从 unpkg 直接 `<script>` 引)
- ❌ **不能砍现有视觉效果**(纸质感 / 阴影 / 字体 / 动画都要 1:1 保留)
- ✅ **可重构 React 组件结构**(拆分 / 提取 hook / memo)
- ✅ **可优化样式表达**(改用 CSS-in-JS 字符串 + className,只要不引构建链)
- ✅ **可改 build_cards_json.py 输出结构**(若前端能更省力)
- ✅ **可拆 cards.jsx**(目前 1254 行单文件)

---

## 4. 文件清单

| 文件 | 行数 | 角色 |
|---|---|---|
| `Login.html` + `login.jsx` | 35 + 165 | 登录页 |
| `Stage Folders.html` + `folders.jsx` + `folder-asset.jsx` + `swipe-stack.jsx` + `tweaks-panel.jsx` | 87 + 398 + 186 + 293 + 425 | 阶段文件夹首页 |
| `Cards.html` + `cards.jsx` | 43 + **1254** | 卡片栈页(最重) |
| `Favorites.html` (复用 cards.jsx) | 36 + (cards.jsx) | 收藏夹页 |
| `Admin.html` + `admin.jsx` | — + 163 | 管理页 |
| `auth.js` | 104 | localStorage 用户隔离工具(`PKB.auth` 命名空间) |
| `cards.json` | ~2.3 MB | 1408 张卡 |
| `glossary.json` | ~325 KB | 812 个术语 |

**所有路径相对仓库根的 `50-frontend/` 子目录**:`/Users/jjjjadennnn/Desktop/parenting-kb/50-frontend/`

**不在审查范围**:
- `build_cards_json.py` / `build_positions.py`(Python,仅当前端因数据 schema 不合理而吃力时再提)
- `30-cards/*.yaml` / `40-glossary/*.yaml`(数据,不是代码)

---

## 5. 关键架构 + 约定(知道这些避免误改)

### 5.1 数据流

```
30-cards/*.yaml       ─┐
                       ├──→ build_cards_json.py ──→ cards.json + glossary.json
40-glossary/*.yaml    ─┘                              ↓
                                                  fetch (Cards / Folders / Favorites)
                                                      ↓
                                            React state(useCards / useGlossary)
                                                      ↓
                                                  渲染卡片
```

### 5.2 卡片 schema(cards.jsx 期望的字段)

```jsonc
{
  "card_id": "C-S1-013",
  "stage": "S1",
  "stageName": "0–1 月",
  "tag": "CONTROVERSY",         // 单 tag,大写
  "no": 26,                      // 段内 1-indexed(visibleCards 重映射时覆写)
  "noInStage": 26,               // 后端原始段内 idx
  "totalInStage": 226,
  "front": { "title": "...", "hook": "..." },
  "back": {
    "lede": "首段...",
    "body": ["后续段落 1...", "段落 2..."],
    "what": ["行动 1", "行动 2"],   // ACTIONS 列表
    "fail": "误区段...",            // CAVEAT 段
    "evidence": "B",                // A/B/C/D
    "positions": {                   // 可选 — 立场对照(38 个议题用到)
      "issue": "议题",
      "views": [
        { "school": "Karp", "source": "SRC-003", "stance": "..." }
      ]
    },
    "pullQuote": null               // 暂未用,未来扩展槽
  },
  "citation": { "book_zh": "...", "authors": "...", "location": "...", "source_id": "SRC-003" },
  "related_cards": [...],
  "glossary_refs": ["G-TERM-swaddle", "G-PERSON-Karp", ...]
}
```

### 5.3 用户隔离(`auth.js`)

- 登录后 `PKB.auth.user()` 返回当前用户名
- 收藏 / 进度全走 `PKB.auth.readJSON(key, default)` / `PKB.auth.writeJSON(key, value)` — 自动 per-user 加前缀
- 跨标签页同步用 `window.dispatchEvent(new Event('pkb:favorites-changed'))`

### 5.4 路由

无 SPA 路由。每个页面独立 HTML。**通过 URL query 传参**:
- `Cards.html?stage=S1`     → 只看 S1 段
- `Cards.html?favorites=1`  → 看收藏夹
- `Cards.html?card=C-S1-013` → 直接跳到这张卡

### 5.5 视觉规范(任何重构必须保留)

- **字体**:Noto Serif SC(中文衬线,Google Fonts)+ ui-monospace(eyebrow / 序号 / 引用)
- **配色**:5 种纸色循环(`CARD_COLORS` 常量),每张卡按 idx 取
- **动画**:卡片切换 0.3s ease,文件夹展开 460ms 缓动
- **阴影**:文件夹 SVG `<feDropShadow stdDeviation="6 10">`(横竖不对称),卡片 box-shadow
- **触感**:`pointer-events` 让透明区穿透,触摸 `touch-action: none` 禁默认手势

### 5.6 已修复的历史 bug(不要倒退)

1. **iOS Safari 永久缓存 cards.json** — fetch 已加 `?t=Date.now()` + `cache: 'no-store'`,**别去掉**
2. **bfcache 飞出动画错位** — `pageshow` 事件检测 `e.persisted` 强制 reload,**别去掉**
3. **inline list `[S1]` YAML 解析** — Python 端处理,前端不动
4. **文件夹横向阴影累积成竖线** — `<feDropShadow>` 用 stdDeviation 不对称值修过,**别改宽度参数**
5. **触摸滑动白屏** — swipe-stack.jsx 多次返工,改触摸逻辑前请 grep `startRef` / `pointer` 看注释

---

## 6. 审查重点

### 6.1 P0 必查(用户可见崩溃 / 数据丢失类)

- **localStorage 写满**:用户收藏 + 进度多年累积是否会撞 5MB 上限?有降级策略吗?
- **cards.json 加载失败**:fetch 失败 / 慢网下用户看到什么?有 timeout / retry 吗?
- **glossary 缺失术语**:卡片 `glossary_refs` 引用了不存在的 G-id 时,parseRichText 是否安全?
- **触摸手势竞态**:swipe-stack.jsx 同时在 React 重渲染 + 触摸事件 + 飞出动画,有没有未清理 listener 或 stale closure?
- **iOS 横屏 / 折叠 / 分屏**:`100dvh` 在折叠瞬间的行为?
- **登录态过期**:`PKB.auth.user()` 返回空时,`requireLogin()` 跳转链路是否一定正确?
- **多用户切换**:同设备 A 用户切到 B 用户后,B 是否会看到 A 的收藏 / 进度残影?
- **直接访问 `Cards.html?card=C-S1-013`**:卡片不存在时如何降级?

### 6.2 P1 性能 / 稳定性

- **Babel 浏览器内编译耗时**:首次加载会卡 1-2 秒,有办法预编译为 `.js` 而不引构建链吗?(例如 Python 跑一次本地 babel CLI 输出 .js)
- **cards.jsx 1254 行**:能拆几个文件而不引构建链(`<script>` 多个 jsx)?
- **inline style 重复**:每张卡的 5 种纸色 + 衍生 alpha 在每次 render 都重算,能否提到模块层?
- **parseRichText 复杂度**:每张卡每次 render 都扫一遍正文做 glossary 匹配,能 memoize 吗?
- **SVG filter 重复定义**:文件夹 9 个 + 卡片 N 张,各自 inline `<filter id>`,能否提到 `<defs>` 共享?
- **React dev build**:UMD 引的是 `react.development.js`(开发版,慢 + 大),能换 `react.production.min.js` 而不破坏 babel-standalone 吗?
- **memo / useCallback 缺失**:`Card` 组件每次父级 setState 都重 render,prop 引用是否稳定?
- **大列表无虚拟化**:Cards 段最多 238 张卡同时挂 DOM,iOS 低端机吃得消吗?

### 6.3 P2 代码质量 / 可维护性

- **inline style vs className**:能否只把高频 style object 提为常量(避免每次 render 新对象触发 React diff)?
- **魔法数字**:卡片宽 460 / 文件夹 W=360 / TAB_W=150 / 360 等数字散落多处
- **重复逻辑**:`useCards` / `useGlossary` 几乎一致的 fetch 套路,能抽公共 `useJSON` 吗?
- **命名一致性**:`useFavorite` 单数 / `readFavList` 复数,统一一下
- **错误边界**:有 ErrorBoundary 吗?Card 渲染异常时会整页白屏吗?
- **PropTypes / TypeScript-like 检查**:无类型,组件 prop 误传难追

### 6.4 跨浏览器 / 移动端

- **iOS Safari 100dvh** 在键盘弹起时跳变,有处理吗?
- **`touch-action: none`** 在某些 Android 浏览器是否支持?
- **`-webkit-tap-highlight-color`** 之外还有没有其他点击高亮泄漏?
- **`will-change: opacity`** 滥用会内存爆,有审视过哪些地方真需要吗?
- **`<link rel="preconnect">`** 到 unpkg 能否进一步优化(预加载 React)?

### 6.5 安全

- **PKB.auth 用 localStorage 存密码 / token?**:localStorage 任何 JS 可读,有 XSS 风险吗?
- **登录守卫绕过**:`PKB.auth.requireLogin()` 在 React 加载之前跑,但用户能在 devtools 注入 `localStorage.setItem` 直接绕过吗?(因为是本地工具,影响低,但仍想知道)
- **cards.json 直接暴露**:无 ACL,是否有泄露风险?(本地 LAN 用,影响低)

---

## 7. 输出格式

请按 **优先级**(P0 → P1 → P2)排序输出,每条用如下结构:

```markdown
## P0-1 · [简短标题]

**位置**:`50-frontend/cards.jsx:712-728`

**类型**:Bug / Race condition

**症状**:[一句话描述用户会观察到什么]

**根因**:[为什么会发生,具体到哪一行]

**现状代码**:
```js
// 现有代码片段
```

**建议修复**:
```js
// 修后代码片段(完整可粘贴)
```

**为什么更好**:[1-2 句话]

**风险**:[改动可能引入什么副作用,如何验证]
```

---

## 8. 输出量预期

预期发现规模(给个心理预期,不是配额):

- **P0 bug**:0-3 条(代码不算太破,作者已经修过几轮)
- **P1 perf / stability**:5-10 条(主要是 cards.jsx 1254 行 + Babel 浏览器内编译)
- **P2 maintainability**:10-20 条(inline style / 魔法数字 / 重复逻辑)

如果你发现远多于这个量,**先报最 critical 的 5 条**,我看完决定再深挖。

---

## 9. 不要做的事

- ❌ **不要建议引构建链** — 用户明确拒绝
- ❌ **不要建议 TypeScript / ESLint 配置** — 同上
- ❌ **不要重写整个项目** — 增量改动,patch 形式
- ❌ **不要建议换 React 版本** — 18.3.1 锁死
- ❌ **不要建议改视觉**(纸色 / 字体 / 阴影 / 间距)
- ❌ **不要建议改 YAML / Python 数据层**(除非前端被它逼到很难做)
- ❌ **不要重命名公共 API**(`PKB.auth.*` 已被多处用)

---

## 10. 上下文资源(供你补全理解)

如果某段代码不理解,可以参考这些注释:

- `cards.jsx` 文件顶 1-30 行有 schema 说明
- `auth.js` 1-20 行有 PKB.auth 接口
- `swipe-stack.jsx` 整文件注释密集,讲触摸手势状态机
- `folders.jsx` 1-80 行有阶段配置 + 配色逻辑
- `00-meta/conflicts_data/README.md` 有立场对照数据规范

不熟的字段或常量,**优先 grep 而不是猜**。

---

## 11. 起点建议

按这个顺序看效率最高:

1. 跑通先看 `cards.jsx`(最大,bug 概率最高,1254 行)
2. 然后 `swipe-stack.jsx`(交互最复杂,触摸手势)
3. `folders.jsx` + `folder-asset.jsx`(SVG 渲染,可能有重绘问题)
4. `auth.js`(短但关键,localStorage + 跨标签页同步)
5. 最后扫剩下的 `login.jsx` / `admin.jsx` / `tweaks-panel.jsx`(短文件,逻辑简单)

---

## 12. 提交格式

把所有发现汇总到一个 markdown 文件,文件名 `frontend-review-{YYYY-MM-DD}.md`,放到仓库根。

第一段写**总结**(几条 P0 / P1 / P2 / 整体健康度评分 1-10),后面按优先级展开。

最后追一段 **"5 条最优先动手的"**,我会按这 5 条来打补丁。

---

*Prompt v1.0 · 2026-05-06 · 项目方:作者本人 + 妻子,主要 iOS Safari 用,后端只服务本地 LAN*
