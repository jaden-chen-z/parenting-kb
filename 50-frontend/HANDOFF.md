# 前端继续开发 · 前情提要(2026-05-04)

> 给新 session 用 — 直接读这份文档接手前端工作。
> 项目地址:`~/Desktop/parenting-kb/`
> 前端在 `~/Desktop/parenting-kb/50-frontend/`

---

## 1. 项目一句话

中文育儿知识库,1437 张知识卡 + 211 张术语卡跨 9 段(S0-S8 = 孕期到 3-6 岁)。前端是个 **静态 React SPA**(Babel-in-browser,无构建链),浏览/收藏/段过滤这些卡片。

---

## 2. 必读文件(按顺序)

```bash
cd ~/Desktop/parenting-kb

# 1. 项目背景(2 分钟)
cat README.md
cat 00-meta/progress.md          # 知识库当前进度

# 2. 前端架构 + 启动方法
cat 50-frontend/README.md

# 3. 卡片数据 schema
ls 30-cards/                      # 9 段目录 s0-s8
head -60 30-cards/s1-newborn/C-S1-001.yaml   # 看一张样本卡 yaml

# 4. 前端代码
ls 50-frontend/
# Cards.html / Stage Folders.html / Favorites.html
# cards.jsx (~683 行) folders.jsx (~430 行) folder-asset.jsx tweaks-panel.jsx
# build_cards_json.py — yaml→JSON 转换
# cards.json — 1437 卡的 JSON,用 build_cards_json.py 生成
```

---

## 3. 前端架构

### 数据流

```
30-cards/*.yaml (1437 张)  ──┐
                             │  build_cards_json.py
                             ▼
                   50-frontend/cards.json (2.3 MB)
                             │  fetch
                             ▼
                   cards.jsx 用 useCards() hook 加载
```

### 页面

| HTML | 加载的 JSX | 作用 |
|---|---|---|
| `Stage Folders.html` | `tweaks-panel.jsx` + `folder-asset.jsx` + `folders.jsx` | 9 段文件夹堆叠首页 |
| `Cards.html` | `cards.jsx` | 卡片栈,URL `?stage=S1` 过滤 |
| `Favorites.html` | `cards.jsx`(自动加 `?favorites=1`) | 收藏夹模式 |

### 段映射

| YAML stage | URL param | folder 标签 |
|---|---|---|
| S0 | `?stage=S0` | 孕期 |
| S1 | `?stage=S1` | 0-1 月 / 新生 |
| S2 | `?stage=S2` | 1-3 月 |
| S3 | `?stage=S3` | 3-6 月 |
| S4 | `?stage=S4` | 6-9 月 |
| S5 | `?stage=S5` | 9-12 月 |
| S6 | `?stage=S6` | 12-24 月 |
| S7 | `?stage=S7` | 24-36 月 |
| S8 | `?stage=S8` | 3-6 岁 |

### Schema 映射(yaml → JSON for frontend)

详见 `build_cards_json.py` 的 `convert_card()` 函数:
- `back.why_matters` → `back.lede`(首句)+ `back.body[]`(其余)
- `back.what_to_do[]` → `back.what[]`
- `back.failure_mode` → `back.fail`
- `tags[]` → `tag`(优先级 red_flag > safety > controversy > philosophy,大写)
- `citation` 6 字段 → `citation` 4 字段(简化)

---

## 4. 已完成功能 ✅

| 功能 | 状态 |
|---|---|
| 9 段文件夹堆叠首页(Stage Folders.html)| ✅ 桌面 + 手机都通 |
| 段计数从 cards.json 异步加载 | ✅ |
| 文件夹堆叠,点击展开,点击其他收回 | ✅ |
| 展开后右滑触发飞出动画 + 跳 Cards.html?stage=X | ✅ |
| Tweaks 面板(配色 warm/cool/mono / 布局 alternate/stagger)| ✅ |
| 文件夹差异化阴影(横向±10px,纵向 stdDev 9,alpha 0.20)| ✅ |
| 卡片页 yaml→JSON 数据接入 | ✅ |
| 卡片 stage 过滤(?stage=Sx)| ✅ |
| 卡片栈翻页 — 点击左半 → 下一张,右半 → 上一张 | ✅ |
| 翻页动画(translateX + rotate)| ✅ |
| 收藏 localStorage 持久化 | ✅ |
| Window 渲染(只画当前 ±1 张,1437 卡不全进 DOM)| ✅ |
| 卡片页固定视口高度(`100dvh`),不上下滚 | ✅ |
| 卡内容超长时,**卡内部 overflow: auto** 滚动 | ✅ |

---

## 5. 待做 / 用户最后的需求 🔨

### 5.1 触摸滑动(P0,做了 1 次踩坑回退)

**用户需求**:
- **手指左滑 = 下一张**(替代点击左半屏)
- **手指右滑 = 上一张**(替代点击右半屏)
- **手指上下滑** 让卡内容**内部滚动**(已经能,因为 Card 内部 overflow:auto)

**踩过的坑**(2026-05-04 凌晨):
- 我加触摸 handler 后,Cards 页**白屏**
- 原因可能是:
  - `React.useRef` 调用顺序违反 Hook 规则
  - `e.touches[0]` 在 undefined 时崩
  - 或某个 effect 副作用
- **回退到点击翻页能用,触摸 handler 全删了**

**重做时注意**:
- ⚠️ **每加一行就 desktop 验证一次**,别一次性大改
- ⚠️ 可以参考 `folders.jsx` 的 onTouchStart / onTouchMove / onTouchEnd 实现(那边已工作 — 见 PaperFolder 组件)
- 触摸 ref 要在组件顶层,不能在条件分支里
- 横滑判定:`Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)`(纵向多 = 滚动,不触发翻页)
- 抑制滑动结束的"虚假点击":用 `swipedRef.current` 标记 + onClick 检查

### 5.2 备选优化(可选)

- 卡片之间互相跳转(根据 `related_cards` 字段,目前没渲染)
- 卡内 glossary 术语 hover/tap 显示定义
- 收藏夹空状态优化(已有基础)
- 数据 hot reload(目前要重跑 build_cards_json.py)

---

## 6. 启动 + 测试

```bash
cd ~/Desktop/parenting-kb/50-frontend

# 1. 重新生成 cards.json(若 yaml 卡有变动)
~/Desktop/parenting-kb/.venv/bin/python build_cards_json.py

# 2. 起 server(8765 端口)
python3 -m http.server 8765

# 3. 桌面浏览器打开测试
open "http://localhost:8765/Stage%20Folders.html"
open "http://localhost:8765/Cards.html?stage=S1"   # S1 = 0-1 月,238 张
open "http://localhost:8765/Favorites.html"

# 4. 手机用同一 WiFi,Mac IP:
ipconfig getifaddr en0   # 拿到本机 IP,如 10.5.17.209
# 手机 Safari 打开 http://10.5.17.209:8765/Stage%20Folders.html
```

---

## 7. 关键代码位置(新 session 改之前先看)

| 改什么 | 看哪 |
|---|---|
| 卡片栈 / 翻页 / 触摸 / 数据加载 | `cards.jsx` 函数 `CardStack` (~441 行) |
| 单张卡渲染(title/lede/body/what/fail/citation)| `cards.jsx` 函数 `Card` (~78 行) |
| 触摸 reference 实现 | `folders.jsx` 函数 `PaperFolder` 内的 onTouchStart/Move/End |
| 阴影 / 文件夹形状 | `folders.jsx` 函数 `PaperFolder` |
| 数据 schema 映射 | `build_cards_json.py` 函数 `convert_card` |
| 段 / 配色 / Tweaks 默认值 | `folders.jsx` `FoldersPage` 头部 |

---

## 8. 当前关键参数(改前先了解)

### Cards.html 视口锁定

```css
html, body { height: 100%; overflow: hidden; overscroll-behavior: none; }
#root {
  max-width: 460px;
  margin: 0 auto;
  height: 100vh;            /* fallback */
  height: 100dvh;            /* iOS Safari 排除底部工具栏的可见区 */
  background: transparent;
}
```

⚠️ **不要改成 `position: fixed`** — 之前试过,坏了。
⚠️ **不要改成 `height: '100dvh'` 单独用** — 部分浏览器 fail。`100vh` fallback 必须留。

### CardStack root

```jsx
height: '100%',                // #root 已固定 100vh,这里 100% 跟随
display: 'flex',
flexDirection: 'column',
overflow: 'hidden',
```

### Card stage 区(flex:1 子)

```jsx
flex: 1,
minHeight: 0,                  // 关键! 让 flex item 严格按可用空间收缩
position: 'relative',          // 让 visibleCards 的 absolute 锚定在这
```

### 文件夹尺寸

```jsx
const W = 360;                 // folder 宽 — 给两侧阴影 16.5px 呼吸空间(393 视口)
// 不要改 W,改了会让阴影累加成竖线
```

### 文件夹阴影 filter

```jsx
<filter id={`drop-${stage.id}`} filterUnits="userSpaceOnUse"
        x="-10" y="0" width={W + 20} height={TAB_H + BODY_H + 6 + 30}>
  <feDropShadow dx="0" dy="7" stdDeviation="3 9"
                floodColor="black" floodOpacity="0.20" />
</filter>
```

⚠️ **stdDeviation 要写 SVG 的两值形式**(横/纵分别),CSS `filter: drop-shadow` 不支持非对称。

---

## 9. 给新 session 的开局指令(直接 paste)

```
我接手前端继续开发。请先:

1. 读 ~/Desktop/parenting-kb/50-frontend/HANDOFF.md(本文件,看完整上下文)
2. 读 ~/Desktop/parenting-kb/50-frontend/cards.jsx(主要工作文件)
3. 起 server: cd ~/Desktop/parenting-kb/50-frontend && python3 -m http.server 8765(后台)
4. 桌面 Chrome 验证 Cards.html?stage=S1 当前能正常工作(基线)
5. 然后实现 §5.1 触摸滑动(每加一行就刷新桌面验证,避免上次踩的坑)

我不在,你做决定。卡住了写到 ~/Desktop/parenting-kb/00-meta/questions_for_user.md。
```

---

## 10. 安全边界

| 不要 | 应该 |
|---|---|
| 改 `30-cards/*.yaml` 卡片内容 | 只改 `50-frontend/` 内文件 |
| 改 `build_cards_json.py` schema 映射(无强烈理由)| 调 cards.jsx 内的渲染逻辑 |
| 改 cards.json 数据 | 只读,有变动跑 build 脚本重生成 |
| 用 `position: fixed` 在 #root | 用 `height: 100vh; height: 100dvh` 双声明 |
| 一次性改大量代码 | 增量改,每步桌面 + 手机验证 |
| 跳过 Hook 规则 | useRef/useState/useEffect 都在组件顶层,不进 if/else |

---

## 11. 项目其他相关 meta(可不读,但有助于理解)

| 路径 | 内容 |
|---|---|
| `00-meta/README.md` | 总任务书(知识库构建,跟前端无关) |
| `00-meta/progress.md` | 知识库进度(1974 张卡 / 24 SRC) |
| `00-meta/checkpoints/` | 各阶段 checkpoint 报告 |
| `30-cards/INDEX_BY_SOURCE.md` | 卡片按 SRC 分类索引 |
| `40-glossary/` | 术语卡(目前前端不展示) |
| `10-sources/source_index.yaml` | 源 SRC 索引 |

---

*本文档生成于 2026-05-04 19:30 (前端阶段 1 完成,触摸滑动待做)*
