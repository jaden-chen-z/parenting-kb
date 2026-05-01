# parenting-kb · 育儿知识库

> 一个文件夹里的循证育儿知识库,服务一个中文双语家庭,两个 0-1 岁孩子。

## 是什么

把权威机构 / peer-reviewed 文献 / 流派原典里的育儿知识,
按 0-1 岁的发展"关节"切成 5 段(S1-S5),
最终蒸馏成可记忆 + 可执行的卡片。

## 怎么用

1. 找卡片:`30-cards/sN-{stage}/C-SN-NNN.yaml`
2. 顺藤摸瓜到知识单元:`20-units/sN-{stage}/K-{TOPIC}-SN-NNN.yaml`(跨段机制在 `cross-stage/`)
3. 再到一手源:`10-sources/tierN-{type}/notes/SRC-NNN.yaml`
4. 看进度:`00-meta/progress.md`
5. 看待你拍板的问题:`00-meta/questions_for_user.md`

## 三层 ID

- 源:`SRC-NNN`(全局唯一)
- 单元:`K-{TOPIC}-{STAGE}-NNN` 或 `K-{TOPIC}-CROSS-NNN`
- 卡片:`C-{STAGE}-NNN`

## 月龄分段

| 段 | 月龄 | 段名 | 文件夹 |
|---|---|---|---|
| S1 | 0-1 月 | 第四产程 | `s1-newborn` |
| S2 | 1-3 月 | 社交萌芽 | `s2-1to3mo` |
| S3 | 3-6 月 | 认知爆发 | `s3-3to6mo` |
| S4 | 6-9 月 | 探索期 | `s4-6to9mo` |
| S5 | 9-12 月 | 前行走+前语言 | `s5-9to12mo` |

## 完整任务书

`00-meta/README.md`(v3.0,2026-04-30)

## 当前阶段

Phase 0 Bootstrap 已完成,等待 Phase 1(S1 端到端 POC)启动。
详见 `00-meta/progress.md`。
