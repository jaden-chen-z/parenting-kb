# Progress · 育儿知识库

## 当前阶段

**Phase 1 完成**(2026-05-01)— Karp《卡普新生儿安抚法》第一本书 33 张卡片 + SRC-003 + 任务书升级 v1.2 — 等用户验收(任务书 §6:抽 5 张随机审,4+ 张满意 = POC 通过 → Phase 2)

## 完成度

### Phase 0 Bootstrap(2026-04-30)
- [x] 目录结构(§3)
- [x] schemas 落实(§4 v3)
- [x] 任务书归档到 `00-meta/README.md`
- [x] 项目根 `README.md`
- [x] meta 文件:progress.md / questions_for_user.md / conflicts.md / gaps.md
- [x] source_index.yaml(初始 2 份样本)
- [x] books_to_buy.md
- [x] 2 份样本转 v3 yaml(SRC-001, SRC-002, K-MILE-S5-001, K-MECH-CROSS-001)
- [x] git init + 首次 commit
- [x] 工具栈安装 → 见 `tooling.md`

### Phase 1 Karp(2026-05-01,1 天完成)

**任务书**:`00-meta/PHASE1_KARP.md`(v1.0 → v1.1 加白话风格 → v1.2 加 §10 实战调整 14 条)
**第一本书**:Karp《卡普新生儿安抚法》中译本(SRC-003)

- [x] OCR 长单行文件分块(11 个 15KB chunks 到 `karp_chunks/`)
- [x] 全书结构地图(3 批 subagent)
- [x] 主题反向索引
- [x] 10 个主题包并行提取 verbatim 素材
- [x] SRC-003.yaml(23 个主题块,OCR 错字修正)
- [x] source_index.yaml 更新
- [x] **第一部分 12 张卡片**(C-S1-001..012)— 哭闹机制 + 第四产程 + 5S 概览
- [x] **第二部分 13 张卡片**(C-S1-013..025)— 5S 五招详解 + 拥抱疗法
- [x] **第三部分 8 张卡片**(C-S1-026..033)— 睡眠 + 红旗 + 食物过敏 + 产后
- [x] 反向覆盖审计(每部分跑一次)— 补 9 张高价值漏掉卡
- [x] GitHub Top 3 调研 → §10.13 外部方法论吸收(2000-token 块 / 黑白名单 / non-overlapping / 输入输出比 / ToC)
- [x] checkpoint MD(`00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md`)
- [ ] **用户抽 5 张审核**(待)— 4+ 张满意 = POC 通过

### Phase 2 (待启动)

**候选下一本书**(按优先级):
1. AAP《Caring for Your Baby and Young Child》— Tier 1 权威,直接 cross-validate Karp 33 张卡
2. Brazelton《Touchpoints: Birth to Three》— Karp 引用源,流派原典补充
3. 鲍秀兰《0-3 岁早期教育和潜能开发》— 中文 Tier 4 权威,补东方视角

## 已抓源数

| Tier | 已抓 | 预估 |
|---|---|---|
| Tier 1 权威机构 | 2(SRC-001/002,raw HTML 待补)| ~40 |
| Tier 2 学术 | 0 | ~60 |
| Tier 3 书籍 | **1**(SRC-003 Karp)| ~15 |
| Tier 4 中文权威 | 0 | ~10 |
| Tier 5 视频/播客 | 0 | ~8 |

## 已生成

- 单元:2 个(K-MILE-S5-001, K-MECH-CROSS-001)— Phase 1 知识单元层暂跳过
- **卡片:33 张**(S1: 31 张 + S2: 2 张,Karp 流派为主,等级分布:A 4 / B 23 / C 6)
  - 2026-05-01 微调:schema 升级 `stage: S1` → `stages: [S1]` 列表;C-S1-004/005(哭闹峰主题)挪到 S2 重命名为 C-S2-001/002(任务书 §2 把哭闹峰值列在 S2 主题清单)

## 阻塞

- 无(等用户验收)

## 待用户回答的问题

- Phase 1 33 张卡片是否通过 POC?
- Phase 2 启动哪本书?
- `_drafts_part2/` 旧包裹草稿(原 008/009/010)是否可删?

## 已确认的关键决策

- **Q1 → B**: Phase 1 第一批 fetch 顺手补抓 SRC-001/002 raw HTML(2026-04-30)— **未做,Phase 2 补**
- **Q2 → A**: Phase 1 仅用 Tier 3 书跑通(2026-04-30)— Phase 1 实际只用 SRC-003 一本书
- **Q3 → B → SUPERSEDED**: 卡片语言策略(2026-04-30)— **被 PHASE1_KARP §2 覆盖**:全中文,不双语
- **新增决策(Phase 1 实战)**:
  - 字段名英文 key,展示层翻中文(待建 `render_labels.yaml`)
  - hook 默认填(从可选改为必填,§10.10)
  - evidence_level 单本书阶段标尺(§10.7):C = Karp 一家言 / B = Karp 引外部研究 / A = 与 Tier 1 共识对齐
  - 反向覆盖审计固化为工作流必备步骤(§10.4)

## 上次 session 结束时间

2026-05-01(Phase 1 全部完成)

## 下次 session 起点

> 1. 用户验收 33 张卡片(抽 5 张随机审 4+ 张满意 = POC 通过)
> 2. 验收通过 → Phase 2 启动:选下一本书(优先 AAP《Caring for Your Baby》 Tier 1 cross-validate)
> 3. Phase 2 启动前补:`00-meta/render_labels.yaml`(英文 key → 中文展示标签映射)
> 4. Phase 2 启动前考虑:chunk 大小从 15KB 降到 ~5KB(§10.13 优先级 1 + 4)
>
> **下一 session 必读**:
> - `00-meta/PHASE1_KARP.md` v1.2(§10 沉淀的 14 条实战教训)
> - `00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md`(本次完整产出)
