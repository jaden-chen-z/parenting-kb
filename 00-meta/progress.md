# Progress · 育儿知识库

## 当前阶段

Phase 0 完成,等待 Phase 1(S1 端到端 POC)启动指令

## 完成度

### Phase 0 Bootstrap
- [x] 目录结构(§3)
- [x] schemas 落实(§4 v3,见样本 yaml)
- [x] 任务书归档到 `00-meta/README.md`
- [x] 项目根 `README.md`
- [x] 空 meta 文件:progress.md / questions_for_user.md / conflicts.md / gaps.md
- [x] 空 source_index.yaml(已含 2 份样本索引)
- [x] `books_to_buy.md` 完整购书清单
- [x] 2 份样本转 v3 yaml(SRC-001, SRC-002, K-MILE-S5-001, K-MECH-CROSS-001)
- [x] git init + 首次 commit
- [x] 工具栈安装(2026-04-30):pandoc / poppler / tesseract+lang / calibre + venv(markitdown / ocrmypdf)→ 见 `tooling.md`

### Phase 1 (任务书已就绪,待新 session 执行)
**任务书**:`00-meta/PHASE1_KARP.md`(v1.0,2026-05-01)
**第一本书**:Karp《卡普新生儿安抚法》中译本
**卡片规范**:v3.2(覆盖 v3.1 双语)— 全中文 + 难翻译术语括注英文 + 论文式引用脚注
**字数上限**:每张卡片背面正文 ≤310 字(不含 citation)

- [ ] 新 session 读 PHASE1_KARP.md + 总任务书
- [ ] 浏览 karp_happiest_baby_zh.md 结构
- [ ] 识别 Karp 涵盖的 S1 知识点(预估 20-40)
- [ ] subagent 提取每个知识点
- [ ] 生成 SRC-003.yaml + 索引更新
- [ ] 生成 20-40 张 C-S1-NNN.yaml
- [ ] checkpoint MD
- [ ] 用户抽 5 张审核(4+ 张满意 = POC 通过 → 进下一本书)

**后续**:Karp 完成后,逐步把其他 20 本书覆盖到 S1-S5 各阶段。

## 已抓源数

| Tier | 已抓 | 预估 |
|---|---|---|
| Tier 1 权威机构 | 2 | ~40 |
| Tier 2 学术 | 0 | ~60 |
| Tier 3 书籍 | 0 | ~15 |
| Tier 4 中文权威 | 0 | ~10 |
| Tier 5 视频/播客 | 0 | ~8 |

## 已生成

- 单元:2 个(K-MILE-S5-001, K-MECH-CROSS-001)
- 卡片:0

## 阻塞

- 无(等用户决定 Phase 1 启动时机 + 是否先购书)

## 待用户回答的问题

见 `questions_for_user.md`(0 条 pending,3 条已 resolved 2026-04-30)

## 已确认的关键决策(影响 Phase 1)

- **Q1 → B**: Phase 1 第一批 fetch 顺手补抓 SRC-001/002 raw HTML 到 `tier1-authoritative/raw/`
- **Q2 → A**: Phase 1 仅用 Tier 1+2 跑通,书后买
- **Q3 → B**: 卡片 schema 本地扩展为 v3.1 —— 卡面中文 + verbatim 英文 + 中译参考(详见 questions_for_user.md Q3 新增字段约定)

## 上次 session 结束时间

2026-04-30(Phase 0 完成 + Q1-3 已确认)

## 下次 session 起点

> 启动 Phase 1:先做 S1 探索 — Tier 1 / S1 主题相关 URL 全部验证 + 候选清单
> S1 主题清单见任务书 §2:喂养建立 / 安抚哭闹(Karp 5S/PURPLE) / 原始反射 / 黄疸 / 安全睡眠(SIDS) / 新生儿筛查 / 产后妈妈 / 第一次儿保 / 脐带护理 / 胎记 / 体温警戒线
>
> Phase 1 第一批 fetch 任务包含:
> - SRC-001 raw HTML 补抓(Q1 决定)
> - SRC-002 raw HTML 补抓(Q1 决定)
> - Harvard "5 Steps SR" PDF(gaps.md G2)
> - S1 关键 Tier 1 入口页(CDC LTSAE 0-1月 / AAP HealthyChildren / WHO / NICHD / NHC 等)
