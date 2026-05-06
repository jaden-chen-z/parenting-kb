# Phase 14 执行任务书 · 最后一本:Murkoff《海蒂育儿大百科 0-1 岁》

> 项目代号:parenting-kb · books_to_buy 第 16 条目(也是最后一本)· 版本 v1.0(2026-05-04)
> **自主运行模式**:用户在开头**一次性授权**后,session 自动跑完整本书,中途不打扰。
> 并行场景:与 SRC-031 WHO session 同时跑,**严格 ID 隔离避撞**。

---

## 0. 一句话任务

独立 session **自主**读完《海蒂育儿大百科 0-1 岁》中译本,**自动分段**,**逐段提取**知识点产卡,**反向覆盖审计**补漏,**跨源整合**互链,产出**不限张数**的中文循证卡片。整本完成后打印总结,等用户验收。

---

## 1. 🔓 一次性权限请求(用户开头处理)

**重要 — Session 开始时第一件事**:

请你向用户**一次性请求**以下工具的全部权限,用户会一次性 yes-to-all,之后中途**不再打扰用户**:

| 工具 | 用途 |
|---|---|
| **Bash** | 批量 grep / find / git add / wc / yq 等;子任务调度 |
| **Read** | 读源 MD / 已有卡片 / 任务书 / index |
| **Edit** | 修改 source_index.yaml / 已有卡片 related_cards / INDEX_BY_SOURCE.md |
| **Write** | 创建新卡片 / SRC-040.yaml / checkpoint MD |
| **Agent**(Task)| spawn subagent 提取每 part / 跨段审计 / 反向覆盖 |
| **TodoWrite** | 跟踪 part 进度 + 自检任务 |
| **WebSearch / WebFetch**(可选)| 仅当需要核对 ISBN / 出版年份 / 中译本译者时使用,**不做内容查询** |

**只在以下场景例外打断用户**(write 进 `00-meta/questions_for_user.md` 后**继续跑**,不阻塞):
1. 发现源 MD 严重 OCR 损坏导致整段无法解析(损坏 > 30% 才算)
2. 发现与 conflicts.md 完全相反的新立场(立场冲突,需要用户拍板默认立场)
3. 发现 source_index.yaml 实际被占的 SRC ID 与本任务书冲突,且 +10 buffer 也撞上

其他全部**自主决策**,在 checkpoint 中说明决策。

---

## 2. 必读前置(自动,~10 分钟)

按顺序 Read(主线只看精简部分,大文档分块):

1. **`00-meta/README.md`** §0 硬规则 + §2 主题清单 + §4 schema + §5 evidence_level + §9 卡片质量(只读这几节,~15KB)
2. **`00-meta/PHASE1_KARP.md`** §2-§2.5(规范 v3.3 字段+字数+引用+白话)+ §10(14 条实战教训)
3. **`00-meta/PHASE2_AAP.md`** §2.6-2.9(翻译两步走 + 前情提要 + 术语卡片化 + inline 引用渲染)
4. **`00-meta/progress.md`** 头部 + 当前总览(知道你在啥位置)
5. **`30-cards/INDEX_BY_SOURCE.md`** 头 200 行(看清现有卡片分布,避免重复主题)
6. **`00-meta/conflicts.md`** 全部(知道哪些立场已被识别,海蒂可能补哪些视角)
7. **`00-meta/gaps.md`** §3 P0 严重缺口(尤其 G6-G8 黄疸 / 脐带 / 新筛 — 海蒂可能补)

主上下文增长目标:< 50 KB(规范全收,卡片正文不进)。

---

## 3. 选定的书

**Murkoff《What to Expect the First Year》中译《海蒂育儿大百科 0-1 岁》**

| 字段 | 值 |
|---|---|
| 文件路径 | `~/Desktop/parenting-kb/10-sources/tier3-books/raw_pdfs/murkoff_what_to_expect_zh.md` |
| 文件大小 | **1.88 MB / 188 万字符**(最大中文 OCR 之一)|
| 来源 | 192 MB 扫描 PDF + ocrmypdf chi_sim+eng + markitdown |
| 流派 | 美国主流育儿百科,**非流派原典**,定位"主流共识对照"(参考 books_to_buy.md #12 注:"引用要节制,B/C 级") |
| 对应段 | **S1 主战场 + 全 S0-S5 覆盖**(0-1 岁百科)|

### 这本书在知识库中的独特角色

- **美国主流共识参照**:Karp 是流派、AAP 是机构、海蒂是**最畅销大众百科**,代表"普通美国家庭实际遵循的共识"
- **填 P0 缺口**:gaps.md G6 新生儿黄疸 / G7 脐带护理 / G8 新生儿筛查 / G11 母乳→混合喂养过渡 等海蒂大概率覆盖
- **跨源对照**:同议题(共睡 / 奶嘴 / 包裹 / 辅食时机)海蒂与 Karp / AAP / Davies 立场对照 → 直接挂 conflicts.md
- **避免重复**:已有 8 本书覆盖核心主题,海蒂应**只取增量** — 优先抓:1) 任务书 §2 主题清单中尚缺的;2) gaps.md P0/P1 列出的;3) 海蒂独家立场(主流大众视角)

---

## 4. 自主工作流(5 阶段,自动顺序)

### Phase A · 自动分段(主线 + 1 个 subagent,~15 分钟)

```
1. Read 源 MD 头部 100 行,识别 OCR 质量(乱字率)
2. grep 章节标题(中文 "第\|章\|月" 等)定位 TOC
3. spawn 1 个 subagent: "Read murkoff_what_to_expect_zh.md 用 offset/limit 分块扫,
   返回 章节地图 yaml: 每章起止行号 + 主题概括 + 对应月龄段 (S0-S5)"
4. 主线收 yaml,根据章节自然边界 + 内容量,自动分 5-8 个 Part
5. Write 分段计划到 `00-meta/checkpoints/checkpoint_PHASE14_MURKOFF_planning_YYYYMMDD.md`
6. TodoWrite 创建 Part 1 ~ Part N 任务
```

**典型分段(预估)**:

| Part | 主题 | 段 |
|---|---|---|
| Part 1 | 孕产期 + 新生儿(0-2 周)| S0/S1 |
| Part 2 | 第 1 月(满月期)| S1 |
| Part 3 | 第 2-3 月 | S2 |
| Part 4 | 第 4-6 月(辅食起点)| S3 |
| Part 5 | 第 7-9 月 | S4 |
| Part 6 | 第 10-12 月 | S5 |
| Part 7 | 跨段专题(喂养 / 睡眠 / 疾病 / 安全 / 妈妈恢复)| 跨段 |

### Phase B · 逐 Part 自主提取(每 Part 1 个 subagent,串行)

每个 Part 一个 subagent,prompt 模板(自动填入):

```
任务:从 murkoff_what_to_expect_zh.md 的 [起止行号] 提取 Part X 的所有知识点。
做法:
1. 用 Read offset/limit 分块读 (每次 500-1000 行)
2. 识别该 Part 内的所有"独立知识点"(一个知识点 = 一个独立可记忆的主张)
3. 对每个知识点:
   a) 检查 INDEX_BY_SOURCE.md / conflicts.md / gaps.md
      - 已有 8 源充分覆盖且立场一致 → 跳过(不重复造卡)
      - 已有但立场不同(主流 vs 流派) → 产卡,标 controversy + cross-link
      - 没有覆盖或填 gap → 产卡(优先!)
   b) 提取核心论点 / why_matters / what_to_do(3-5 条) / failure_mode / 章节页码
   c) 评估 evidence_level:海蒂是大众百科,默认 B(主流共识),引外部研究升 A,纯编辑意见 C
   d) 决定 tags:safety / philosophy(海蒂不算流派原典,慎用)/ controversy / red_flag
4. 严格遵守 PHASE1_KARP §2.2 字数上限 + §2.5 白话风格
5. citation 5 字段全填(英文书名 + 中译 + 作者 + 年份 + 章节页码 + source_id=SRC-040)
6. glossary_refs:正文出现的专业术语必须 G-ID 引用,不得内联解释
7. related_cards:跨源同主题卡片必须互链(尤其 Karp/AAP/鲍秀兰/Davies 同议题)

输出:
- 每张卡片完整 yaml,直接 Write 到 `30-cards/sX-XXX/C-SX-NNN.yaml`(NNN 见 §5 隔离规则)
- 该 Part 摘要 yaml 返回主线(只含 N 张卡 + 主题清单 + 缺术语清单 + 跨派对接清单)
- subagent 不返回卡片正文,只返回结构化结果
```

主线收每 Part 摘要后:
- 更新 TodoWrite
- 写 progress 到 checkpoint
- 启动下一 Part subagent
- **不停下问用户**

### Phase C · 反向覆盖审计(subagent × 1,~30 分钟)

整本提取完后:

```
任务:重读 murkoff_what_to_expect_zh.md TOC + 抽样章节 + INDEX_BY_SOURCE 中海蒂卡列表,
找漏掉的高价值知识点。
方法:
1. 列出 TOC 全部章节 vs 已产卡覆盖章节
2. 对每个未产卡章节抽样读,判断是否值得产卡(增量价值标准:gap fills / 主流共识 / 立场对照)
3. 列出"漏掉但应补"的卡片清单
4. 自主决定补还是跳(标准:若属于 gaps.md P0/P1 → 必补;若纯重复 → 跳)
5. 自主补卡(直接 Write)
6. 返回主线:补卡清单 + 决策理由
```

### Phase D · 跨源整合(主线 + 1 subagent,~30 分钟)

```
任务:把海蒂全部卡(SRC-040)与现有 22 源卡(尤其 Karp/AAP/鲍秀兰/Davies)做整合
1. 找海蒂卡 vs 已有卡的"同主题"对(基于 title 关键词 + tag)
2. 给同主题对互加 related_cards(双向 Edit)
3. 找新冲突(海蒂主流立场 vs 流派立场)→ 写入 conflicts.md(追加,不覆盖)
4. 找 evidence_level 升级候选(本来 C/B,海蒂背书后可升 B/A)
5. 自主完成所有 Edit,写入 audit_log
```

### Phase E · 落地 + checkpoint(主线,~15 分钟)

```
1. Write SRC-040.yaml 到 10-sources/tier3-books/notes/
2. Edit source_index.yaml:加 SRC-040 entry + referenced_by_cards 完整清单
   ⚠️ 单点 Edit 避免覆盖 SRC-031 WHO session 的并行写入
3. Edit INDEX_BY_SOURCE.md:加 SRC-040 段
4. Edit progress.md:头部 + 已抓源数 + 已生成 + 当前总览 全部更新
5. Write checkpoint_PHASE14_MURKOFF_complete_YYYYMMDD.md:
   - Part 1-N 各产出统计
   - 反向覆盖补的卡
   - 跨源整合改的关系
   - 新增 conflicts 项
   - 升级 evidence_level 卡数
   - 待用户验收清单
6. 终端打印总结(< 30 行),等用户
```

---

## 5. 并行隔离(关键 — 避撞 SRC-031 WHO session)

### SRC ID

**SRC-040**(跳到 040 留 +9 buffer 给 WHO 任何子 SRC)

启动前确认:
```bash
ls 10-sources/*/notes/SRC-{031,032,033,034,035,036,037,038,039,040}.yaml 2>/dev/null
```
如果有占用,跳到下一空 SRC-NNN。

### 卡片 ID buffer

启动前**实测**当前各段最大 NNN:

```bash
for stage in s0 s1 s2 s3 s4 s5; do
  max=$(ls 30-cards/${stage}-*/C-S?-*.yaml 2>/dev/null | grep -oE "C-S[0-9]-[0-9]+" | sort -t- -k3n | tail -1)
  echo "$stage max: $max"
done
```

每段 NNN 取 `max + 500` 作为本任务起点。例:S1 当前最大 250 → 海蒂 S1 卡从 **C-S1-750** 起。

这样无论 WHO session 怎么跑都不会撞 ID。

### source_index.yaml 写入

只 Edit 一个位置(末尾 next_src_id 之前插 SRC-040 entry),**不重写整个文件**。如果 WHO session 同时改,git 可能 conflict — 用 `git diff` 先看,如有冲突手动合并(merge,不 reset)。

### INDEX_BY_SOURCE.md / progress.md

同样**末尾追加**而不是 rewrite。

---

## 6. 自主决策边界(避免无脑产卡)

### ✅ 可以自主决策的事(不打扰用户)

- 分多少 Part(看内容量,5-8 范围内)
- 每 Part 产多少卡(不限,按内容)
- 是否跳过某主题(已 8 源充分覆盖且无新立场)
- evidence_level 评 B 还是 A
- tags 怎么标
- 跨派对照卡是否新建
- conflicts.md 追加内容
- gaps.md 哪些被填(标 ✅ resolved)
- 卡片字数微调(强制控制在 §2.2 上限内)

### ⚠️ 必须打断用户的事(写 questions_for_user.md 后继续跑)

- 源 MD OCR 损坏 > 30%(需用户重新 OCR)
- 发现海蒂立场与 conflicts.md 已识别立场**完全相反**(需用户决定默认立场)
- SRC-040 + 卡 ID buffer 仍撞上 WHO session(极小概率,需用户协调)
- 任何"硬规则"(任务书 §0)被自己破坏的边缘案例

打断不是阻塞 — 写完 questions 继续跑别的 Part,该问题留待后续。

---

## 7. 输出清单

完工时应有:

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml                # SRC-040 已 Edit 加入
│   └── tier3-books/notes/
│       └── SRC-040.yaml                 # ⭐ 新建,海蒂源 metadata
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md               # SRC-040 段已加
│   └── s0/s1/s2/s3/s4/s5/                # ⭐ N 张新卡(C-SX-750+)
├── 40-glossary/                          # 海蒂引入的新术语卡(若有)
└── 00-meta/
    ├── progress.md                       # 已更新
    ├── conflicts.md                      # 海蒂相关追加
    ├── gaps.md                           # 海蒂填上的 P0/P1 标 ✅
    ├── audit_log.md                      # 本次自动改动轨迹
    └── checkpoints/
        ├── checkpoint_PHASE14_MURKOFF_planning_YYYYMMDD.md
        └── checkpoint_PHASE14_MURKOFF_complete_YYYYMMDD.md   # 主报告
```

---

## 8. 终端总结模板(完工时打印)

```
========================================
Phase 14 完成: 海蒂育儿大百科 0-1 岁(SRC-040)
========================================
卡片产出:
  总数: NNN 张知识卡 + MM 张术语卡
  段分布: S0=X / S1=X / S2=X / S3=X / S4=X / S5=X
  evidence_level: A=X / B=X / C=X
  tags: safety=X / red_flag=X / controversy=X / philosophy=X

反向覆盖审计补卡: X 张(章节漏掉清单见 checkpoint)

跨源整合:
  related_cards 双向链接新增: X 对
  conflicts.md 追加: X 项(C 节视角差异 / D 节...)
  evidence_level 升级: X 张(从 B → A)
  gaps.md ✅ 标记 resolved: X 项

books_to_buy.md 16 条目最终状态: 16/16 完成 ✅

待用户验收:
  - 抽 5 张随机审 (4+ 张满意 = POC 通过)
  - audit_log.md 内容审核(自动改动是否合理)
  - 决定是否启动 Phase 15(全库二次审计 / 卡片合并 / S8 段扩展 / 等)
========================================
```

---

## 9. 起步 5 分钟

新 session 收到本任务书后第一步:

```bash
cd ~/Desktop/parenting-kb

# 1. 实测当前状态(决定 buffer)
ls 10-sources/*/notes/SRC-*.yaml | tail -10
for stage in s0 s1 s2 s3 s4 s5; do
  echo -n "$stage max: "
  ls 30-cards/${stage}-*/C-S?-*.yaml 2>/dev/null | grep -oE "C-S[0-9]-[0-9]+" | sort -t- -k3n | tail -1
done

# 2. 看源
wc -m 10-sources/tier3-books/raw_pdfs/murkoff_what_to_expect_zh.md
head -100 10-sources/tier3-books/raw_pdfs/murkoff_what_to_expect_zh.md

# 3. 准备 TodoWrite 框架
TodoWrite([
  "Phase A: TOC 扫描 + 自动分段",
  "Phase B-1: Part 1 提取",
  "Phase B-2: Part 2 提取",
  "...(动态根据分段填)...",
  "Phase C: 反向覆盖审计",
  "Phase D: 跨源整合",
  "Phase E: checkpoint + 终端总结"
])

# 4. 向用户请求一次性权限(本任务书 §1)

# 5. 用户授权后,自主跑完
```

---

## 10. 用户开头确认要做的 3 件事

打开新 session,粘贴本任务书后,你只需要做 3 件事:

1. ✅ 一次性授权所有工具权限(本任务书 §1 列表)
2. ✅ 看 session 输出的"分段计划"(Phase A 末尾打印)— 觉得分得 OK 就说 "go"
3. ✅ 之后等终端打印完工总结(§8 模板)

**中间的所有步骤(读源、提取、产卡、审计、整合、写文件、commit?)session 全自主**。

注:本任务**不自动 git commit**(避免与 WHO session 冲突)。完工后用户单独 commit。

---

*v1.0 完。这是 books_to_buy.md 的最后一本。完工后整个 16 本书项目 100% 闭环。*
