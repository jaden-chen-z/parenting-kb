# Checkpoint · Phase 8 Magda Gerber 深度本(SRC-022)初版 + 二审(2026-05-03)

> 项目:parenting-kb · Phase 8 第二轮深度本(Shonkoff fallback)
> 启动:2026-05-03(同日完成)
> 任务规模:42 张初版 + 3 张漏知识反向覆盖补 = 45 张
> 任务书:`PHASE8_GERBER_DEEP.md`
> 上游姊妹:`checkpoint_PHASE8_GERBER_20260503.md`(SRC-021 并行 session 32 张产出)

---

## 0. 一句话总结

**Phase 8 原目标 Shonkoff OCR 缺,fallback 到 Magda Gerber《Your Self-Confident Baby》(SRC-022,深度本第二轮)。本 session 写出 42 张初版 + 3 张反向覆盖补 = 45 张知识卡 + 9 张术语卡,跟并行 session SRC-021(32 张)互补不重叠。**

---

## 1. 工作流时间线

### Phase A:必读上下文 + 状态扫描(20 分钟)
- 读 5 个必读文档(checkpoint_PHASE7_LANSBURY_USER_AUDIT + STERN_AUDIT + PHASE2_AAP §2.5-2.9 + PHASE1_KARP §10 + SRC-019)
- Python 实测各段 max ID + next_src_id + 现有 glossary 总数
- ID 策略:max + 51 buffer

### Phase B:扫书 + 主题映射(20 分钟)
- Gerber 8 章 488K 字符 / 12387 行
- Python 扫章节 offset
- 8 段映射预估:42 张

### Phase C:批量产卡(2.5 小时,4 组)
- 组 1 S0+S1 = 8 张
- 组 2 S2+S3 = 9 张
- 组 3 S4+S5 = 10 张
- 组 4 S6+S7 = 15 张
- **初版 42 张完成**

### Phase D:9 张术语卡(30 分钟)
- 8 张新建术语 + Round 3 补 1(time-out)= 9 张

### Phase E:4 轮独立审(详见 AUDIT MD)

### Phase F:更新索引 + 写文档(30 分钟)
- 发现 SRC-021 已被并行 session 占用
- 重命名 SRC-020 → SRC-022 + Python 批量替换 55 文件
- source_index.yaml + INDEX_BY_SOURCE.md + progress.md 全部更新

---

## 2. 初版 42 张卡分布

| 段 | 月龄 | 初版卡数 | 主题侧重 |
|---|---|---|---|
| S0 | 孕期 | 3 | 8 大原则 + 不完美 + 求助 |
| S1 | 0-1 月 | 5 | Tell Before Do + 真声音 + 哭 = 语言 + 仰卧 + 不宠坏 |
| S2 | 1-3 月 | 5 | 慢下来 + 可预测 + 别说 OK + 全注意 + 平静日 |
| S3 | 3-6 月 | **4** | 玩环境 + 模范 + 选择性注意 + 户外睡 |
| S4 | 6-9 月 | 5 | 里程碑 + 选择性介入 + 100% 安全房 + 群玩 + 主动参与 |
| S5 | 9-12 月 | **5** | 分离焦虑 + 陌生焦虑 + 戒奶 + 矮桌椅 + 不偷溜 |
| S6 | 12-24 月 | **10** | 基本信任 + I want + 好奇 + 不教 + 红黄绿 + Antaeus + 撞头 + 自律 + 序列 + 不 time-out |
| S7 | 24-36 月 | 5 | RIE 不止 2 岁 + 兄弟 + 学如厕 + 测试限度 + 不必完美 |
| **总** | | **42** | |

---

## 3. Round 2 反向覆盖审 — 3 张高价值漏点

逐章 spot-check 8 章(Lansbury 用户三审教训)。

### 3.1 C-S3-354 选托育看 4 件事(Ch6) ⭐⭐⭐
**重要度**:中国家长普遍痛点
**核心**:不看硬件,看大人 4 个细节(说话 / 告知 / 比例 / 处理冲突)
**跨源**:↔ C-S0-167 + C-S1-406 + C-S6-138

### 3.2 C-S5-450 新食物 30 次再试(Ch7) ⭐
**重要度**:中国家长普遍 3-4 次拒绝就贴"挑食"标签
**核心**:30 次累计后才算他真不爱
**跨源**:↔ C-S5-448 + C-S2-345 + Davies C-S5-135

### 3.3 C-S6-468 幼儿说不是健康(Ch8 No! No! No!) ⭐
**重要度**:Magda 整节立场,Lansbury 没建
**核心**:18-24 月"不"= 自主期觉醒(Erikson 1-3 岁)
**跨源**:↔ C-S6-459 + C-S6-462 + Lansbury C-S6-403

---

## 4. 段分布 + 等级分布(终版 45 张)

### 段分布

| 段 | 月龄 | 卡数 | 备注 |
|---|---|---|---|
| S0 | 孕期 | 3 | 不变 |
| S1 | 0-1 月 | 5 | 不变 |
| S2 | 1-3 月 | 5 | 不变 |
| S3 | 3-6 月 | **5** | + 反向覆盖补 1 |
| S4 | 6-9 月 | 5 | 不变 |
| S5 | 9-12 月 | **6** | + 反向覆盖补 1 |
| S6 | 12-24 月 | **11** | + 反向覆盖补 1 |
| S7 | 24-36 月 | 5 | 不变 |
| **总** | | **45** | 42 + 反向覆盖补 3 |

### 等级分布
- **A 级**:25 张(56%)
- **B 级**:20 张(44%)
- **C 级**:0 张

---

## 5. SRC-021 vs SRC-022 关系(关键工程意外)

### 5.1 冲突发现

Phase F 更新 source_index.yaml 时发现:
- Line 953 已有 SRC-021 = Magda Gerber《Your Self-Confident Baby》(并行 session 32 张卡)

### 5.2 处理:重命名 SRC-020 → SRC-022

- 选择保留 + 互补:重命名为 SRC-022(下一可用 ID)
- Python 批量 replace 55 文件(45 卡 + 9 术语 + 1 SRC yaml)
- next_src_id: SRC-020 → SRC-023(SRC-020 留给 Shonkoff 未来真启动)

### 5.3 互补关系

两 session ID 不冲突,subject 互补不重复。详见任务书 §6。

---

## 6. 工程纪律(沉淀给 Phase 9)

### 6.1 ID 隔离(并行 session 安全)
- 每个 session 用不同 buffer(SRC-021 +200 / SRC-022 +51)

### 6.2 OCR 缺位的 fallback 流程
- Phase 8 任务书写明 (a)(b)(c) fallback 顺序
- OCR 缺时按顺序 fallback,不停下问
- Phase 9 启动时,要求用户预先确认 OCR 状态

### 6.3 索引文件单点 Edit 不全文 Write
- source_index.yaml 1000+ 行,Edit 加 entry 比 Write 全文安全
- 注意 indent 级别(SRC entries 是 sources: 数组下的 dict)

### 6.4 跨源率主动管理
- 每张卡写时主动放 1 张非自卷 related
- 终版 0 跨源孤岛卡 = 80% 跨源率

---

## 7. 跟 Lansbury(SRC-019)对照

详见任务书 §5。Magda SRC-022 独有 13 项:
1. Educaring 自创词解释
2. 8 Basic Principles 原版
3. Tell Before Do
4. Antaeus 神话比喻
5. 红黄绿三色限度系统
6. Loczy 罗茨研究院起源
7. Quality Time 真定义
8. Selective Attention
9. Active Participant in Caregiving
10. 选托育 4 标准
11. 30 次新食物
12. 幼儿说"不"是健康
13. You Don't Have to Be Perfect

---

## 8. 完成度对比(初版 → 二审)

| 维度 | 初版(42)| 二审(45)|
|---|---|---|
| 段覆盖 | S0-S7 | S0-S7 全段更深 |
| 章节覆盖 | Ch1-8 大部分 | + Ch6 + Ch7 + Ch8 No! 节 |
| A 级 % | 53% | **56%** |
| 跨源率 | ~75%(写时管理)| **80%** |
| 0 跨源卡 | 5 | **0** |
| 平均 related | 2.85 | **3.00** |
| 中国家长高频痛点 | 大部分 | + 选托育 + 新食物 + 说"不"|

---

*v1.0 · 2026-05-03 — Phase 8 SRC-022 初版 + 二审完成*
*终版 45 张 + 9 术语,跨 8 段 S0-S7,A 级 25 张(56%)*
*Phase 8 原目标 Shonkoff OCR 缺 → fallback 到 Magda Gerber 双轮(SRC-021 32 + SRC-022 45 = 77 总)*
*下次接手 session 必读:本文件 + checkpoint_PHASE8_GERBER_DEEP_AUDIT_20260503.md(三+四轮)+ PHASE8_GERBER_DEEP.md(任务书)*
