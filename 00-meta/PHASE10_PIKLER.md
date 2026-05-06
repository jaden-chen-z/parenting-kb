# Phase 10 任务书:Pikler《Friedliche Babys – zufriedene Mütter》(SRC-026)

> 项目:parenting-kb · Phase 10 并行第二本(Shonkoff SRC-025 并行第一本)
> 启动:2026-05-04
> 任务规模:33-37 张知识卡 + 10-11 张术语卡 + 5 轮独立审
> 上游姊妹文档:PHASE9_MATSUDA.md(三审框架基线)+ PHASE8_GERBER_DEEP.md(深度本范式)

---

## 一句话总结

**Phase 10 第二本 — 把 RIE 派师承谱系闭环到德文原典。Pikler 1969 年《Friedliche Babys – zufriedene Mütter》是 Magda Gerber RIE 哲学的德文草稿源头,Lansbury Ch7 "Sitting Babies Up: 8 Reasons" / Magda Educaring + Pflege/Spiel + Loczy 故事 全部追溯到本卷。本卷产出 Pikler 原始论证 + Loczy 1946 规程 + 30 年 720 婴儿统计原始数据。跟并行 session Shonkoff(SRC-025 NRC 2000 美国综述)互补 — 欧洲 1969 临床 vs 美国 2000 综述。**

---

## 1. 背景 + 决策

### 1.1 选定本书理由

- **RIE 谱系闭环** — Pikler(SRC-026 师承)→ Magda Gerber(SRC-021/022 创始人)→ Lansbury(SRC-019 推广人)
  现库 124 张 RIE 卡的根源在此(Lansbury 60+ 处提 Magda → 30+ 处追溯 Pikler)
- **跨派关联硬密度高** — Pikler 是 RIE / 蒙氏 0-3 / 依恋派 共同根源(floor bed / observation / Pflege)
- **独家原始数据** — Pikler 30 年家庭 + 720 Loczy 婴儿大动作发育统计(Lansbury / Gerber 都引用,本卷有原始)

### 1.2 跟并行第一本 Shonkoff 的隔离

- SRC ID:SRC-025(Shonkoff)+ **SRC-026**(本卷)
- 段 ID:Shonkoff +100 buffer / **Pikler Shonkoff 起点 + 30**(避撞 + 给 Shonkoff 30 卡余量)
- 索引更新:**Edit 单点改**(避免覆盖 Shonkoff session 并行 Edit)
- 启动前验证:`grep "SRC-025" source_index.yaml` 确认 Shonkoff 已写入

### 1.3 跟现库 RIE 卡 124 张的不重建策略

- **不重建**(Lansbury / Gerber 已建):
  - sportscasting / I won't let you / magic word wait / acknowledging feelings
  - 8 Basic Principles 美国版 / Educaring 自创词 / Antaeus / 红黄绿
  - Tell Before You Do / Crying is language / Active Participant
  - 不撑坐 8 理由(Lansbury C-S2-290)— **本卷只补 Pikler 1969 德文原版论证**
  - floor bed(Davies / Lillard 已建)— **本卷只补 Pikler 1946 Loczy 起源数据**
- **本卷新建** — Pikler 独家:
  - Bewegungsentwicklung / 7-8 阶段大动作里程碑表
  - Loczy 1946 规程 / 720 婴儿统计原始
  - Pflege vs Spiel 二分(德文)
  - 不教翻身 / 不教坐 / 不教站 / 不教走 — 德文原版立场
  - 不便盆训练(Sauberkeitserziehung)— 德文系统
  - Geduld(耐心)育儿哲学

---

## 2. 工作过程(Phase A-G 已完成 / 进行中)

### 2.1 Phase A:必读上下文 + 状态扫描(20 分钟)

读必读文档(✅ 完成):
- `00-meta/checkpoints/checkpoint_PHASE9_MATSUDA_AUDIT_20260503.md`(用户三审框架最新)
- `00-meta/PHASE8_GERBER_DEEP.md`(深度本 4 轮审范式)
- `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)
- `10-sources/tier3-books/notes/SRC-019.yaml`(Lansbury 模板,Pikler 引用)
- `10-sources/tier3-books/notes/SRC-022.yaml`(Gerber 深度本,Pikler 师承)
- `40-glossary/G-PERSON-Pikler.yaml`(已存在草稿,本卷扩展)
- `30-cards/s2-1to3mo/C-S2-290.yaml`(Lansbury 不撑坐 8 理由 — 本卷对接)

实测状态扫描:
- Shonkoff SRC-025 已起跑 — S0:619-622(4 卡)/ S1:864-869(6 卡)
- next_src_id:SRC-025(Shonkoff Phase F 未到,索引未 Edit)
- 各段 max ID(包含 Shonkoff)+ ID 全部 3 位数(无 4 位突破)

ID 策略:**Shonkoff 起点 + 30 buffer**(给 Shonkoff 30 卡余量,避撞)
- S1=894 / S2=832 / S3=835 / S4=834 / S5=933 / S6=956 / S7=891
- S0/S8 跳过(Pikler 主要 0-36 月)

### 2.2 Phase B:扫书结构 + 主题映射(进行中)

德文 OCR 357K 字符 / 7151 行 / 11 章主题分章(非月龄分章):

| 章 | offset | chars | 主题 | 重要性 |
|---|---|---|---|---|
| Einleitung | 3398 | 6300 | 引言 | ⭐ |
| Ch1 Jedes Kind | 9700 | 17518 | 每孩不同 | ⭐ |
| Ch2 Bewegung | 27218 | **68970** | 大动作发展 | ⭐⭐⭐ 主战场 |
| Ch3 Geistige | 96188 | 15087 | 精神发展 + 反例 | ⭐⭐ |
| Ch4 Verhältnis | 111275 | 22851 | 母婴关系 | ⭐⭐ |
| Ch5 Kind&Welt | 134126 | 2926 | 孩子&世界(短) | ⭐ |
| Ch6 Daumen | 137052 | 21921 | 吸大拇指 | ⭐ |
| Ch7 Spielen | 158973 | 17300 | 怎么玩 | ⭐⭐ |
| Ch8 Sprache | 176273 | 24721 | 语言 | ⭐ |
| Ch9 Topf | 200994 | 26301 | 如厕 | ⭐⭐ |
| Ch10 Übergang | 227295 | **55437** | 婴幼儿过渡 | ⭐⭐⭐ 副主战场 |
| Ch11 Abschließend | 282732 | 9000 | 总结 | ⭐ |

### 2.3 Phase C:批量产卡(分 5 组,2-2.5 小时)

预计 33-37 张卡:

#### 组 1:S1+S2(0-3 月)— 7-9 张
重点:仰卧位起点 + 不竖抱 + 母婴节律 + 自由动作起点 + 不教翻身

#### 组 2:S3+S4(3-9 月)— 9-12 张(主战场)
重点:翻身自主 + Ch2 大动作里程碑表 + **不教坐 8 理由德文原版** + Pflege/Spiel + 不撑坐反例

#### 组 3:S5(9-12 月)— 4-5 张
重点:不教站 + 自然站起立 + 反学步车

#### 组 4:S6(12-24 月)— 6-8 张
重点:自由活动 + Lóczy 1946 规程 + 不便盆训练 + 720 婴儿统计 + 玩具观

#### 组 5:S7(24-36 月)— 3-4 张
重点:平衡 + 大动作终态 + 反所有运动训练 + Geduld 总结

### 2.4 Phase D:10-11 张术语卡(40-60 分钟)

新建 10 张 + 扩展 G-PERSON-Pikler / G-TERM-Loczy-institute

### 2.5 Phase E:5 轮独立审(60-90 分钟)

继承 Phase 9 三审 + 用户深度审:
- 轮 1 = Python 机器审
- 轮 2 = 漏知识反向覆盖逐章 spot-check
- 轮 3 = 漏术语扫
- 轮 4 = 用户三审 3 维度(hook / 跨派率 / 章节)
- 轮 5 = 用户深度审(松田三审同标准 — 跨章重复主题独立卡 / 漏专业术语 / 内部结构)

### 2.6 Phase F:索引 Edit 单点改 + 写文档(30-40 分钟)

- 启动前 `grep "SRC-025" source_index.yaml` 确认 Shonkoff 已写入(若没写入,等 5 分钟再查)
- Edit 单点改 source_index.yaml / INDEX_BY_SOURCE.md / progress.md / memory
- 写 4 个 MD:PHASE10_PIKLER.md / checkpoint(初+二审)/ checkpoint AUDIT(三+四+五审)/ conflicts F 节

### 2.7 Phase G:最终报告

---

## 3. 关键约束(继承 + Phase 10 特定)

| 约束 | 内容 |
|---|---|
| §0 硬规则 | 不盗版 / 不凭训练记忆 / 不和稀泥 / 宁少勿滥 |
| v3.5 schema | title ≤ 15 字 / hook 8-12 字 / why_matters 含前情提要 / glossary_refs / related_cards |
| 字数无硬上限 | 用户 feedback memory 说取消 §2.7.3 字数上限,按内容紧凑而定(hook 8-12 字保留) |
| 跨派率 | ≥ 90% 含 12 派任何 1 派 related |
| 师承率 | ≥ 60% 含 Gerber/Lansbury related(机构数据卡 Loczy 豁免) |
| hook 风格 | 抓眼句,无描述型(Phase 9 五字 hook 教训) |
| 学究词清单 | 认知 / 机制 / 感知 / 内化 等 15 词全改白话 |
| 立场对照 | 不判对错,记 conflicts.md F1-F5 节 |
| Edit 单点改 | 索引文件全部 Edit(并行场景避免覆盖) |

---

## 4. 完成定义

- [ ] SRC-026.yaml(完整结构 + 跟 RIE 谱系师承对照)✅
- [ ] 33-37 张新卡入库(数量按内容决定)
- [ ] 10-11 张新术语卡入库
- [ ] 5 轮独立审全过(0 错)
- [ ] PHASE10_PIKLER.md 任务书 ✅(本文件)
- [ ] checkpoint MD(初+二审)+ AUDIT MD(三+四+五审)
- [ ] YAML 全部解析通过
- [ ] 0 跨派孤岛卡(每张 related ≥ 1 含 12 派)
- [ ] ≥ 60% 卡含 Gerber/Lansbury related(师承对接,机构数据豁免)
- [ ] hook 全部抓眼句(无描述型)
- [ ] glossary_refs / related_cards 全部存在
- [ ] source_index.yaml + INDEX_BY_SOURCE.md + progress.md + memory 全部 Edit 单点更新
- [ ] conflicts.md 整理 F1-F5(Pikler 独家 + 跨派对立)

---

*v1.0 · 2026-05-04 — Phase 10 第二本启动书*
*RIE 谱系师承根源 + Pikler 1969 德文原典 + 30 年 720 婴儿原始数据*
