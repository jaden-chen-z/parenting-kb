# Checkpoint · Karp 33 张 + 术语卡按新规则 refactor(2026-05-02)

> 项目:parenting-kb · Phase 2 子任务 · Karp 整本回归 + 术语卡片化
> 启动:2026-05-02 上午
> 完成:2026-05-02 同日
> 任务来源:用户请求"按 §2.6/§2.7/§2.8 新规则把 Karp 33 张卡 + 涉及术语卡都补齐"

---

## 0. 一句话总结

Karp 33 张 S1/S2 卡片全部按 v3.5 schema(`stages` + `glossary_refs`)+ §2.5 白话风格 + §2.7 前情提要 refactor 完成。
新增 8 张 Karp 特有术语卡(我建)+ user 同期批量生成的 ~20 张其他术语卡。
40-glossary/ 当前 36 张术语卡。

---

## 1. 产出清单

### 1.1 术语卡(40-glossary/)

**我新建 8 张**:
- G-TERM-five-s(5S 安抚法)⭐
- G-TERM-fourth-trimester(第四产程)⭐
- G-TERM-calming-reflex(镇静反射)⭐
- G-TERM-cuddle-cure(拥抱疗法)
- G-TERM-Moro-reflex(惊跳反射)
- G-TERM-rooting-reflex(寻乳反射)
- G-PERSON-Illingworth(1954 X 光研究)
- G-PERSON-Field(1986 婴儿按摩 RCT)
- G-TERM-colic(肠绞痛)
- G-TERM-postpartum-depression(产后抑郁)

(实际 10 张,前 8 张是 §2.8.1 列的"Karp 必需",后 2 张是发现的缺口)

**user 同期建的 Karp 涉及术语卡**(8:30-8:55 期间):
- G-PERSON-Brazelton(1962 哭闹峰研究)
- G-PERSON-Wessel(1954 colic 3-3 规则)
- G-ABBR-SBS(摇晃婴儿综合征)
- G-ABBR-CPSC(消费品安全委员会)
- G-TERM-bed-sharing(共同入睡)

**40-glossary/ 当前共 36 张**(包括 user 之前建的 5 张样本 + 后续大批量 + 我补的)。

### 1.2 知识卡 refactor(33 张)

| 段 | 张数 | ID |
|---|---|---|
| S1 | 31 | C-S1-001/002/003/006/007/008/009/010/011/012/013/014/015/016/017/018/019/020/021/022/023/024/025/026/027/028/029/030/031/032/033 |
| S2 | 2 | C-S2-001/002 |

**全部改动**:
1. ✅ schema 已是 v3.5(`stages: [S1]` 列表)— 之前已升级
2. ✅ 加 `glossary_refs` 字段(在 citation 之前)
3. ✅ `why_matters` 加 2 句前情提要(关键概念定义 + 背景数字/严重性/历史)
4. ✅ 字数放宽到 ≤130 字(§2.7.3)
5. ✅ 白话度提升(§2.5/§2.6)— Karp 中译本不需"翻译两步走",主要做白话化复检
6. ✅ `updated: 2026-05-02`

### 1.3 双向回填术语卡 related_cards

- ✅ `G-ABBR-SIDS` 补 5 张 Karp 卡(013/015/022/028/029)
- ✅ `G-TERM-swaddle` 补 3 张(002/023/029)
- ✅ `G-ABBR-DDH` / `G-ABBR-LEAP` / `G-PERSON-Karp` — 已有 Karp 卡引用,无需补

User 建的术语卡(Brazelton / SBS / Wessel / CPSC / bed-sharing 等)的 related_cards 已经在建卡时回填了 Karp 卡 ID,无需追加。

---

## 2. POC 完成定义打勾

按 user 任务原文 § 验收标准:

- [x] 33 张卡全部加 `glossary_refs` 字段
- [x] 33 张卡的 `why_matters` 全部加 2 句前情提要(数字/概念定义/历史)
- [x] Karp 术语卡 ≥ 10 张(实际:Karp 涉及 14 个术语,全部已建)
- [x] 已有 5 张 AAP 术语卡的 related_cards 双向回填完成
- [ ] 抽 5 张样本(术语卡 2 + 知识卡 3)风格令人满意 — **等用户验收**

---

## 3. 工程教训

### 3.1 与 user 并行工作的协调

**现象**:用户在我"扫描+计划"阶段(花了几分钟)同时在批量建术语卡。
我发起术语卡 Write 时,有 3 张已经被 user 建好(Brazelton/SBS/CPSC)→ Write 失败 "File has not been read yet"。
我 Write 成功的 8 张是 user 还没建的,所以我的版本就是真新建。

**教训**:多人/双 agent 并行时,**关键 race window 在"扫描计划期"**。
应对:
- 第一波 ls 后到第一次 Write 之间,user 可能添加文件
- 失败的 Write 当作信号:"user 已经做了" → 接受 user 版本,不强行覆盖
- 优先建 user 没动的(避免冲突)

### 3.2 linter 持续修改触发 Write 失败

**现象**:并行 5 张 Write 时,4 张失败 "File has been modified since read"。
linter(可能是 yamllint / 自动 sort / git hooks)在两个 message 之间修改了已 Read 的文件。

**对策**:Read + Write 紧贴(同一 message 不行,但相邻两个 message)。
**未来**:可以一开始就关闭自动 lint,或写 .editorconfig 让 linter 忽略 yaml。

### 3.3 §2.6 翻译两步走对中译本不适用

§2.6 设计是给"英文源 → 中文卡"用(AAP 卡场景)。
Karp 中译本已经是中文,不需要"先 English skeleton 再 Chinese 改写"——直接做白话化复检即可。
**§2.6 实操标尺**:
- 英文源 → 走两步走(先英 skeleton 再中文白话改写)
- 中译本 → 仅做白话化复检 + 加前情提要

### 3.4 §2.7 前情提要的实际写法

每张卡 `why_matters` 开头 2 句,具体内容根据卡片类型:

| 卡片类型 | 前情提要写什么 |
|---|---|
| 流派概念(C 级)| 概念是谁提的、属于什么流派、几年提出、循证强度 |
| 操作方法(B 级)| 是 5S/某某体系的第几招、目的、适用月龄 |
| 安全红线(A 级)| 风险定义、流行病学数据、严重程度 |
| 误解纠正 | 老观念是什么、新观念是什么、什么时候推翻的 |
| 父母心理 | 常见自责模式、研究反驳依据 |

### 3.5 Karp 流派标签保留

任务原文要求:不动 Karp 流派标签(`philosophy` / `controversy`)。
我严格遵守,所有 6 张 `philosophy` 标签卡(001/002/007/009/010/014/022/028)+ 3 张 `controversy` 标签卡(007/022/028)未动 tag。

---

## 4. 待办

| 待办 | 优先级 | 备注 |
|---|---|---|
| 用户抽 5 张样本验收 | 高 | 任务原文验收标准 |
| 更新 30-cards/INDEX_BY_SOURCE.md | 中 | 加术语卡引用统计? |
| 更新 progress.md | 已做 | 见同步项 |
| 把 ~20 张 user 建的非 Karp 涉及术语卡(BLW/CMPA/PURPLE/REM/tummy-time 等)细化 | 低 | 这些是 AAP 卡用,不在本次任务范围 |
| AAP 37 张卡的 `glossary` → `glossary_refs` 迁移(§2.8.4 步骤 3)| 中 | Phase 2 后续 |
| Karp vs AAP 立场冲突 conflicts.md | 高 | 至少 028(共睡)+ 022(奶嘴)2 处 |

---

## 5. Phase 2 整体进展

- Karp(SRC-003)Phase 1 + 本次 refactor:**33 张 v3.5 schema 知识卡**
- AAP(SRC-004/005/006)Phase 2 R1-R3 + 复盘:**37 张 v3.4 schema 知识卡**(待迁移到 v3.5)
- 术语卡:**36 张**(SRC-003/004/005/006 通用)
- 全库:**70 张知识卡 + 36 张术语卡**

---

*v1.0 · 2026-05-02 — Karp 整本回归 v3.5 schema 完成*
