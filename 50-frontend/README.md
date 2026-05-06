# 50-frontend · 卡片浏览前端

Static SPA(无构建链),本地起 server 即可看 1,437 张知识卡。

## 快速启动

```bash
cd ~/Desktop/parenting-kb/50-frontend

# 1. 生成 cards.json(从 30-cards/*.yaml 全部转出)
~/Desktop/parenting-kb/.venv/bin/python build_cards_json.py

# 2. 起 server
python3 -m http.server 8765

# 3. 浏览器打开
# 段文件夹首页:
open "http://localhost:8765/Stage Folders.html"
# 直接看某段卡片:
open "http://localhost:8765/Cards.html?stage=S1"
# 收藏夹:
open "http://localhost:8765/Favorites.html"
```

## 文件

| 文件 | 用途 |
|---|---|
| `Stage Folders.html` | 9 段文件夹堆叠首页 |
| `Cards.html` | 卡片栈页(URL `?stage=S1` 段过滤) |
| `Favorites.html` | 收藏夹页(localStorage 持久化) |
| `cards.jsx` | 卡片栈组件(从 cards.json 加载) |
| `folders.jsx` | 文件夹首页组件 |
| `folder-asset.jsx` | 文件夹素材 |
| `tweaks-panel.jsx` | 调试面板(色板/布局切换) |
| `assets/` | 纸质纹理图 |
| `build_cards_json.py` | yaml → JSON 转换器 |
| `cards.json` | 1,437 卡数据(脚本生成,不进 git)|

## 卡片更新流程

每次修改 `30-cards/*/C-*.yaml` 后:

```bash
cd ~/Desktop/parenting-kb/50-frontend
~/Desktop/parenting-kb/.venv/bin/python build_cards_json.py
# cards.json 自动重新生成,刷新浏览器即可
```

## URL 参数

| URL | 行为 |
|---|---|
| `Cards.html` | 全部 1437 张卡(段名显示"全部卡片") |
| `Cards.html?stage=S0` | 只看 S0 孕期(145 张) |
| `Cards.html?stage=S1` | 只看 S1 0-1 月(238 张) |
| ... `?stage=S2..S8` | 同上 |
| `Cards.html?favorites=1` | 收藏夹模式 |
| `Favorites.html` | 同上(自动加 ?favorites=1) |

## 数据 schema 映射(yaml → JSON)

| YAML 字段 | JSON 字段 |
|---|---|
| `stages[0]` | `stage` |
| `tags[]` 优先级取 1 | `tag`(大写) |
| `back.why_matters` 拆 | `back.lede` + `back.body[]` |
| `back.what_to_do[]` | `back.what[]` |
| `back.failure_mode` | `back.fail` |
| `back.evidence_level` | `back.evidence` |
| `citation.book_title_zh` | `citation.book_zh` |
| `citation.authors[]` | `citation.authors`(逗号连)|
| `citation.location` | `citation.location` |

详见 `build_cards_json.py` §`convert_card`。

## 段映射

| YAML | 前端显示 |
|---|---|
| S0 | 孕期 (-9~0 月) |
| S1 | 新生 (0-1 月) |
| S2 | 社交萌芽 (1-3 月) |
| S3 | 感知翻身 (3-6 月) |
| S4 | 探索坐立 (6-9 月) |
| S5 | 爬行站立 (9-12 月) |
| S6 | 行走说话 (1-2 岁) |
| S7 | 自我表达 (2-3 岁) |
| S8 | 早童 (3-6 岁) |

## 设计来源

原型由用户外部设计师产出(zip 文件 2026-05-04 提供)。
本目录在原型基础上做了**数据接入改造**:
- 删除原 5 张 hardcoded 样卡(cards.jsx)
- 加 `useCards` hook 异步 fetch cards.json
- CardStack 加段过滤(`?stage=S1` URL 参数)
- 段从 8 段(0-2yr)扩到 9 段(0-6yr,匹配 yaml schema)
- 段计数从 cards.json 异步加载
- palette 各调色盘加 9 色(深紫/最深/最深)
