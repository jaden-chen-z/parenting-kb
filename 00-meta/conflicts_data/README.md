# conflicts_data — 立场对照数据集

> `positions.yaml` 是 84 个冲突的"立场对照"版块原始数据,
> 由 `50-frontend/build_positions.py` 写入卡片 YAML 的 `back.positions` 字段。

---

## 📂 目录

- `positions.yaml` — 全部冲突数据(议题 + 派别 + 立场 + 涉及卡片)
- `README.md` — 本文件,语言规范 + 操作流程

---

## 🛠 操作流程

```bash
cd ~/Desktop/parenting-kb/50-frontend

# 试算(看影响哪些卡片,不写文件)
../.venv/bin/python build_positions.py --dry-run

# 真写(写入 30-cards/*.yaml)
../.venv/bin/python build_positions.py

# 重生成 cards.json
../.venv/bin/python build_cards_json.py
```

> `build_positions.py` **幂等** — 已有 `positions:` 块会被替换而非重复添加。
> 文本插入,不破坏原 YAML 的 `|` 块标量、双引号、空行格式。

---

## ✏️ 立场表述语言规范(v1.0)

任务书 §0 #5:**不替用户做"争议话题"立场决策 — 只列各方,等用户拍板。**
立场表述必须客观、循证、不带情绪。

### ❌ 避免使用的词

| 类别 | 禁词 | 原因 |
|---|---|---|
| 玄学色彩 | 法门 / 真传 / 心法 / 之道 | 偏佛教 / 武侠语境,不属循证育儿 |
| 情绪过强 | 颠覆 / 摧毁 / 抹除 / 剥夺 | 暗示价值判断,除非论文原文如此 |
| 贬义引导 | 所谓 / 美其名曰 / 不过是 | 隐含立场否定 |
| 绝对语气 | 唯一正确 / 必然 / 肯定 / 永远 | 未留余地,违反循证态度 |
| 因果误用 | 基于 X(若 X 是同一对象) | 逻辑循环 |

### ✅ 推荐用法

| 类别 | 推荐 | 例 |
|---|---|---|
| 操作动词 | 推荐 / 反对 / 接受 / 限定 / 强调 | "AAP 反对 bed-sharing" |
| 客观后果 | 具体名词 + 量化 | "DDH 髋发育不良" / "延长睡眠 1-2 小时" |
| 中性程度词 | 倾向 / 多数 / 部分情况 / 通常 | "蒙氏倾向不用奶嘴" |
| 操作建议 | 改用 / 替代 / 配合 | "改用小毯或睡袋" |

### 📏 长度规范

- **issue**:15-30 字一句话,议题点 + 关键变量(`X 该不该用 · 怎么用 · 何时停`)
- **stance**:40-80 字,1 句完整立场 + 1 句具体操作或后果。**不要超过 100 字**(卡片末端拥挤)
- **派别名 (school)**:中文派别(蒙氏 / 鲍秀兰)用中文;西文派(Karp / AAP / WHO)保留英文;并列派用 `蒙氏(Davies/Lillard)` 形式
- **来源 (source)**:`SRC-XXX`(单源)或 `SRC-XXX/YYY`(多源并列)

### 🎯 例:好 vs 不好

❌ 不好:
> Karp 派的 5S 法门基于子宫模拟原理,通过包裹这一神器让宝宝重新感受到母体环境,从而显著延长睡眠时间。

✅ 好:
> 5S 安抚法第一招(Swaddle)。紧裹 + 双臂内 + 配白噪音,可延长睡眠 1-2 小时;锁住莫罗反射(惊跳反射)防止干扰其他四招。

---

## 📋 数据格式(positions.yaml)

```yaml
A1:                                       # 冲突 ID(对照 conflicts.md)
  issue: 包裹(swaddle)该不该用 · 怎么用 · 何时停    # 议题(15-30 字)
  cards:                                  # 涉及卡片 ID 列表
    - C-S1-013
    - C-S1-014
    # ...
  views:                                  # 各派立场(2-5 派)
    - school: Karp                        # 派别名(必填)
      source: SRC-003                     # 来源 ID(可选)
      stance: 5S 安抚法第一招...           # 立场(40-80 字,必填)
    - school: AAP
      source: SRC-004
      stance: 可用,但只起安抚作用...
```

### 一卡多议题

如 C-S1-013 同时属于 A1(包裹) + A19(理论上),`build_positions.py` 自动合并:
- `views` 按 `school` 去重(后写覆盖前)
- `issue` 取第一个议题(其余作为内部 `_conflict_ids` 留底,不渲染)

如有展示需求,渲染层(`cards.jsx`)自行决定如何呈现多议题。

---

## 🔄 维护节奏

- **新增冲突**:在 `positions.yaml` 加新顶层 key(`A8`, `B6` 等),跑脚本即可
- **修改文案**:改 `positions.yaml` 后跑脚本(自动替换,不会残留旧版本)
- **删除冲突**:删除 yaml 中的 key 后,**手工清理**对应卡片的 `back.positions` 字段
  (或在 `build_positions.py` 加 `--prune` 模式,扫所有卡片删孤立 positions)

---

*v1.0 · 2026-05-04 · 试点 A1 包裹完成,余 83 项待铺*
