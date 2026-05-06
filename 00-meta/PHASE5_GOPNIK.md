# Phase 5 执行任务书 · Gopnik《摇篮里的科学家》(并行 session 2)

> 项目代号:parenting-kb · Phase 5 第二本(与 Davies《Montessori Baby》SRC-014 并行)· 版本 v1.0(2026-05-03)
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE5_GOPNIK.md)
> 2. `00-meta/PHASE4_WONDER_WEEKS.md`(段定义 / 工作流 / ID 隔离参考)
> 3. `00-meta/checkpoints/checkpoint_PHASE5_GOPNIK_20260503.md`(本次产出 + 教训)

---

## 0. 一句话任务

抓 Gopnik / Meltzoff / Kuhl 1999《摇篮里的科学家》(认知科学反早教经典),
产 **35 张 v3.5 中文白话认知卡** + 19 张术语卡。
**与 Davies SRC-014 session 并行运行,严格 ID 隔离**(+50 buffer)。

> **更新日志**:
> - **首轮** 2026-05-03:产 28 张知识卡 + 12 张术语
> - **二次补** 2026-05-03:用户反馈"卡片偏少",补 5 张拓展(哲学 / Hubel-Wiesel / 跨模态 / size constancy / categorical perception)→ 33 张
> - **三次补** 2026-05-03:用户要求审查全部卡,发现漏知识点 + 漏术语,补 2 张知识卡(7-8 月 babbling 普适 / 4 岁虚假信念)+ 7 张术语(fast-mapping / joint-attention / social-referencing / categorical-perception / theory-theory / Spelke / Bruner)→ **35 张 + 19 术语**

---

## 1. 选定的书 + 来源

**Alison Gopnik + Andrew N. Meltzoff + Patricia K. Kuhl《The Scientist in the Crib: What Early Learning Tells Us About the Mind》**

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/gopnik_scientist_in_the_crib.md`(.epub 转 .md, 558KB) |
| 作者 | Alison Gopnik(UC Berkeley)/ Andrew N. Meltzoff(华大 I-LABS)/ Patricia K. Kuhl(华大 I-LABS) |
| 流派 | Tier 3 顶级认知发展科学家三人合著 |
| 范围 | 0-3 岁认知发展科学综述 |
| 出版 | 1999 William Morrow / HarperCollins |

### 为什么这本(并行 session 2)

1. **顶级科学源** — 三作者都是认知发展领域顶尖学者,引用全是大型研究
2. **反早教科学** — 中国家长高频痛点(早教焦虑 / 赢在起跑线)的硬科学回答
3. **跨段全覆盖** — 0-3 岁所有阶段(认知 / 语言 / 心智)
4. **跨源对照价值** — 跟 Wonder Week 跃迁理论 + Bowlby 依恋 + Brazelton 优势视角形成完整对照
5. **OCR 已就位**(.epub 转 .md,无 OCR 错字)

---

## 2. 段定义(继承 Phase 3 段制)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S1 | 0-1 月 | s1-newborn | 7 张(C-S1-240..246) |
| S2 | 1-3 月 | s2-1to3mo | 4 张(C-S2-181..184) |
| S3 | 3-6 月 | s3-3to6mo | 4 张(C-S3-187..190) |
| S4 | 6-9 月 | s4-6to9mo | 6 张(C-S4-184..189) |
| S5 | 9-12 月 | s5-9to12mo | 4 张(C-S5-180..183) |
| S6 | 12-24 月 | s6-12to24mo | 5 张(C-S6-179..183) |
| S7 | 24-36 月 | s7-24to36mo | 5 张(C-S7-125..129) |
| **总计** | | | **35 张** |

S1 卡数最多(7 张)— 出生即模仿 / 识母声 / 对人脸特化 / 哲学三大问题 / 视觉关键期等中国家长最易低估的窗口集中段。
S4(6 张)+ S6(5 张)+ S7(5 张)— S4 知觉重组 + 物体永久性 + babbling 普适 / S6 ToM + 因果 + 命名爆发"三连击"/ S7 反早教 + 教学悖论 + 4 岁虚假信念。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3 第三本扩展。

### 评级 evidence_level(本书标尺)

Gopnik 三人都是顶级认知科学家,引用研究都是经过多家独立复制:
- **A**:与 Tier 1 共识对齐 OR Gopnik / Meltzoff / Kuhl 大型实验复制验证(Meltzoff 模仿 / Kuhl 知觉重组 / 物体永久性早于 Piaget 等)
- **B**:Gopnik 引用具体研究(认知科学实验)
- **C**:三作者个人理论推断(本次实测 0 张 — 此书证据基础特别硬)

实测产出:**A=25 / B=10 / C=0** — Gopnik 三人是科学源,A 占 71%。

---

## 4. ⚠️ 并行协调

### 4.1 ID 隔离规则

另一 session 正在做 Davies《Montessori Baby》(SRC-014),会往 S1-S7 加卡。**本 session 严格遵守**:

1. **SRC ID** = SRC-015(跳过 SRC-014,即使 source_index.yaml 还显示 next=SRC-014)
2. **卡片 ID buffer +50**(给 Davies 留 40 张余量)

实测起始(本次 session,2026-05-03):
| 段 | grep max | +50 起步 | 实际产出 |
|---|---|---|---|
| S1 | 190 | 240 | C-S1-240..246(7) |
| S2 | 131 | 181 | C-S2-181..184(4) |
| S3 | 137 | 187 | C-S3-187..190(4) |
| S4 | 134 | 184 | C-S4-184..189(6) |
| S5 | 130 | 180 | C-S5-180..183(4) |
| S6 | 129 | 179 | C-S6-179..183(5) |
| S7 | 075 | 125 | C-S7-125..129(5) |

**实测验证**:Davies 在并行 session 中实际用约 9 张/段(查 max 后确认 S1 到 190 / S2 到 134 等),buffer 充足。

### 4.2 不动的文件(并行不安全)

- ❌ 不动 `30-cards/INDEX_BY_SOURCE.md`(让 Davies 收尾或用户手动合并)
- ❌ 不动 `00-meta/progress.md`(同上)
- ❌ 不动 `10-sources/source_index.yaml`(避免 next_src_id 字段冲突)
- ❌ 不动 `10-sources/tier3-books/notes/SRC-014.yaml`(Davies session 在写)

### 4.3 OK 的文件(各自独立,不冲突)

- ✅ `10-sources/tier3-books/notes/SRC-015.yaml`(新建文件)
- ✅ `30-cards/sN/C-SN-XXX.yaml`(新建文件,ID 已 +50 buffer)
- ✅ `40-glossary/G-XXX-YYY.yaml`(新建文件)
- ✅ `00-meta/PHASE5_GOPNIK.md`(本文件)
- ✅ `00-meta/checkpoints/checkpoint_PHASE5_GOPNIK_<YYYYMMDD>.md`(下一步)

---

## 5. 章节地图

Gopnik 558KB / 7 章 + notes / sources / index。Python `text[start:end]` 切片读取:

```python
ch1_ancient_questions: 12791..54213    # 41K · 古老问题(框架理论)
ch2_about_people:      54213..125788   # 71K · Meltzoff 模仿
ch3_about_things:      125788..187889  # 62K · 物体永久性 / 因果
ch4_about_language:    187889..266710  # 79K · Kuhl 知觉重组 / Parentese
ch5_minds:             266710..345858  # 79K · ToM 综述
ch6_brains:            345858..391891  # 46K · 突触修剪 / 关键期
ch7_clouds_of_glory:   391891..419521  # 28K · 反早教 / 政策
```

---

## 6. 反向覆盖审计(两轮完成)

每段产卡完成后重列"父母从认知科学视角必须知道的事",对照已写卡查漏。

### 6.1 首轮反向审计(28 张)

实测覆盖完整 — 28 张卡覆盖了:
- 总论(婴儿是天生科学家 / 长童年是优势)
- 出生即有(42 分钟模仿 / 识母声 / 对人脸特化)
- 0-6 月(parentese / cooing turn-taking / 镜像情绪 / 唇读)
- 6-12 月(知觉重组 / joint attention / 物体永久性 / 重音规律)
- 1 岁(social referencing / 延迟模仿 / fast mapping / 录像无效)
- 18 月(ToM / 因果实验 / 命名爆发 / 词义创造)
- 反早教(科学反 flash cards / Mozart / 教学悖论 / 突触修剪 / 公共支持)

首轮补漏 1 张:**C-S6-183 宝宝词义创造不照搬**(Gopnik Oxford 长期录音观察)。

### 6.2 二次补漏(用户反馈"卡片偏少"后,5 张)

用户审视 28 张总数后指出书的字数其实不少(558KB),问为什么产卡偏少。
反思:Gopnik 是综述/哲学书,主题集中,首轮策略偏保守。
二次按 Wonder Weeks 同样标准充分挖,补 5 张拓展卡:

- **C-S1-245** 婴儿要解决的 3 大问题(Other Minds / External World / Language)— Ch1 哲学框架
- **C-S1-246** 0-6 月视觉关键期窗 — Hubel-Wiesel 1962 经典 + 临床应用(白内障 / 弱视 / 斜视)
- **C-S2-184** 1 月嘴感觉就匹配视觉 — Meltzoff 1979 奶嘴跨模态实验
- **C-S3-190** 4 月已懂物体不变形 — size constancy + 3D 距离感知
- **C-S4-188** 婴儿听音是黑白不是灰 — categorical perception R/L 实验

二次后 33 张,A=23(70%)。

### 6.3 三次审查 + 补漏(用户要求全面审查,2 张知识卡 + 7 张术语)

用户要求"对所有卡片审查一遍,看有没有漏知识点 / 漏专业词 / 内部结构问题"。
三次审查发现 + 补漏:

**A. 内部结构 + 内容审查(已修)**:
- 4 处 title=hook 重复(C-S4-186 / C-S5-183 / C-S6-181 / C-S7-126)
- 1 处 inline 引用不存在(C-S4-184 引用 C-S5-184 应是 C-S5-183)
- 5 处老术语卡学究词残留(编码 / 维度 / 物理重组 / 范式)

**B. 漏知识点(补 2 张)**:
- **C-S4-189** 全球宝宝先 dadada — 7-8 月 babbling 跨文化普适(中国家长高频"几月叫妈妈"痛点)
- **C-S7-129** 4 岁前不懂"别人会误信" — 虚假信念测试(Sally-Anne / candy box,ToM 顶峰)

**C. 漏术语卡(补 7 张)**:
- 高频被引用的核心机制术语:
  - **G-TERM-fast-mapping**(被 3 张卡引用)
  - **G-TERM-joint-attention**(被 2 张卡引用,自闭症筛查关键)
  - **G-TERM-social-referencing**(被 1 张卡引用)
  - **G-TERM-categorical-perception**(机制层,补 perceptual-narrowing 现象层)
- Gopnik 标志理论:
  - **G-TERM-theory-theory**(婴儿建理论像科学家)
- 关键人物:
  - **G-PERSON-Spelke**(物体永久性 4 月研究奠基)
  - **G-PERSON-Bruner**(Gopnik 师承 + 长童年期假说)

**最终 35 张,A=25(71%),术语 19 张,引用闭环全部建立**。

---

## 7. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── ⚠️ source_index.yaml(不改)
│   └── tier3-books/notes/
│       └── SRC-015.yaml ✅(新建)
├── 30-cards/
│   ├── ⚠️ INDEX_BY_SOURCE.md(不改)
│   ├── s1-newborn/        # C-S1-240..246 ✅
│   ├── s2-1to3mo/         # C-S2-181..184 ✅
│   ├── s3-3to6mo/         # C-S3-187..190 ✅
│   ├── s4-6to9mo/         # C-S4-184..189 ✅
│   ├── s5-9to12mo/        # C-S5-180..183 ✅
│   ├── s6-12to24mo/       # C-S6-179..183 ✅
│   └── s7-24to36mo/       # C-S7-125..129 ✅
├── 40-glossary/
│   ├── G-PERSON-Gopnik.yaml ✅(新建)
│   ├── G-PERSON-Meltzoff.yaml ✅(新建)
│   ├── G-PERSON-Kuhl.yaml ✅(新建)
│   ├── G-PERSON-Vygotsky.yaml ✅(新建)
│   ├── G-TERM-baby-scientist.yaml ✅(新建)
│   ├── G-TERM-imitation.yaml ✅(新建)
│   ├── G-TERM-theory-of-mind.yaml ✅(新建)
│   ├── G-TERM-statistical-learning.yaml ✅(新建)
│   ├── G-TERM-perceptual-narrowing.yaml ✅(新建)
│   ├── G-TERM-causal-learning.yaml ✅(新建)
│   ├── G-TERM-synaptic-pruning.yaml ✅(新建)
│   └── G-TERM-phoneme.yaml ✅(新建)
└── 00-meta/
    ├── PHASE5_GOPNIK.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE5_GOPNIK_20260503.md(下一步)
```

---

## 8. 完成定义(实测)

- [x] 抓 Gopnik 全本(7 章)→ SRC-015.yaml + raw .md 已就位
- [x] 产 **35 张新卡**(任务范围 25-35 张 ✓,三次审查后到上限)
- [x] 新建 **19 张术语卡**(任务范围 ≥5 张 ✓)
- [x] 反向覆盖审计三轮(首轮补 1 张 + 二次补 5 张拓展 + 三次补 2 张知识 + 7 张术语)
- [x] 全部 35 张卡 YAML 验证通过(Python yaml.safe_load)
- [x] 全部 19 张术语卡 YAML 验证通过
- [x] 内部结构审查 0 issues(YAML / 必填字段 / citation / refs / 字数 / 学究词)
- [x] 内容审查通过(title≠hook / inline 引用 / 跨源关联)
- [x] 全部 12 张术语 YAML 验证通过
- [x] 全部 glossary_refs 指向存在的术语卡
- [x] 全部 related_cards 指向存在的知识卡(0 自引用 / 0 占位符)
- [x] 严格审查全过(0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 学究词残留)
- [x] **不动 INDEX_BY_SOURCE.md + progress.md + source_index.yaml + SRC-014.yaml**(并行安全)
- [x] 跨源 related_cards 标连(Gopnik ↔ Wonder Week / Bowlby / Brazelton / 鲍秀兰 / AAP)

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 5 第二本通过。

---

## 9. 关键约束(实测都遵守)

1. ✅ **不动现有 401 知识卡 + 116 术语卡**(其他源)
2. ✅ **ID 必须 +50 buffer**(防与 Davies SRC-014 撞)
3. ✅ **不动 INDEX + progress + source_index + SRC-014**(并行不安全)
4. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
5. ✅ **理论卡也按 v3.5 写白话**(避免学究腔)
6. ✅ **立场对照不判对错**:Gopnik 反早教 vs 中国早教焦虑 — 不判对错,展示数据
7. ✅ **Gopnik 学术语的中文家长版本** — 不照搬 "perceptual narrowing"等学术语,改成"知觉重组"或更白话

---

## 10. 工程纪律(继承 Phase 4 教训)

- 文件 .md 已 OCR(558KB,标准 markdown,无 OCR 错字)
- 主上下文 Python offset 切片读取(每章 15-25K 字符)
- 反向审计每段必做
- YAML 验证: 列表项不能以 `**` 开头(Phase 3 教训 — 本次 1 张违反 G-TERM-statistical-learning,已修复)
- 字段含中文双引号 `"X"` 必须不嵌入字符串末尾(本次 4 处违反,已修复)
- 字符串含 `*` 字符 + 列表起始位置:YAML 当 alias 解析报错(本次 1 处,已修复)

---

## 11. 立场对照(本次产出实测)

### 11.1 Gopnik 与已有源对照

| 主题 | Gopnik 立场 | Wonder Week | Bowlby | Brazelton | AAP / 鲍秀兰 |
|---|---|---|---|---|---|
| 婴儿主动学习 | C-S1-240 baby scientist | C-S1-179 跃迁(神经维度) | (隐含) | C-S1-087 优势视角 | (隐含) |
| 出生即模仿 | C-S1-241 Meltzoff 42 分 | C-S6-128 WW64 模仿一切 | (无) | (无) | (无) |
| 6-9 月双关键期 | C-S4-184 知觉重组 + C-S4-185 joint attention | (无) | C-S4-068 依恋形成 | (触摸点 6-7 月) | C-S4-004 临床 |
| 反 KPI 育儿 | C-S7-125 反早教 + C-S7-126 教学悖论 | C-S6-127 质量时间伪 | (隐含) | C-S1-087 优势视角 | (无) |
| 真人 vs 屏幕 | C-S5-183 录像无效 | (无) | (无) | (无) | C-S6-031 0-2 岁不看屏 |
| 父母情绪传染 | C-S2-183 你的情绪宝宝镜像 | (无) | C-S1-122 依恋前奏 | (隐含) | (无) |

### 11.2 Gopnik 独有维度(填补理论空缺)

#### 反早教科学(现库首次系统覆盖)
- C-S7-125:Mozart effect / flash cards / Baby Einstein 商业骗局
- C-S7-126:教学悖论 — Bonawitz/Gopnik 实验
- C-S7-127:突触修剪 = 特化,不是损失
- 给 Wonder Week / Brazelton 的"反 KPI"提供硬科学证据

#### 双语启蒙关键窗(现库首次明确化)
- C-S4-184:6-12 月知觉重组(Kuhl R/L 实验)
- C-S5-183:录像 CD 无效,必须真人(Kuhl 2003 PNAS)
- 给中国家长"双语怕影响母语"的焦虑提供反驳

#### Theory of Mind 早期里程(现库首次系统覆盖)
- C-S5-180:1 岁 social referencing
- C-S6-179:18 月理解他人欲望(Repacholi & Gopnik 西兰花实验)
- C-S6-180:18 月用 social cue 学词
- 给"4 岁前不要逼共情"提供发展科学依据

#### 因果学习专项(现库首次)
- C-S3-189:3 月就懂"踢腿动 mobile"
- C-S6-181:18 月 blicket detector
- 给"宝宝破坏行为是做实验,不要打断"提供实证

### 11.3 Gopnik vs 中文文化常见误解

| 中文常见误解 | Gopnik 数据反驳 | 卡片 ID |
|---|---|---|
| "新生儿啥都看不懂,跟他说话没用" | 反:42 分钟就模仿 + 出生即识母声 | C-S1-241 / C-S1-242 |
| "跟宝宝说话像大人才高级" | 反:Parentese 是科学的语言加速器 | C-S2-181 |
| "外语 6 岁后再学,怕影响母语" | 反:6-12 月就关闭外语音素窗 | C-S4-184 |
| "刷英文动画 / CD 启蒙外语" | 反:被动音视频 0-3 岁无效 | C-S5-183 |
| "早教班赢在起跑线" | 反:陪伴 > 教学,教学悖论 | C-S7-125 / C-S7-126 |
| "孩子说错话要及时纠正" | 反:词义创造是认知发展,不是错 | C-S6-183 |
| "突触修剪 = 没刺激就完了" | 反:修剪是设计,自然环境就够 | C-S7-127 |
| "反正他不记得,这次破例吼一下" | 反:9 月延迟模仿 1 周仍记 | C-S5-181 |

---

## 12. 改进建议(给后续 Phase 6 接手)

1. **接 Bowlby Vol 3《丧失》**:儿童哀伤反应,跟 Gopnik 的 ToM 发展完整对接
2. **接 Stern《婴儿人际世界》**:跟 Gopnik 的 ToM 深度对照(self 4 阶段)
3. **接 Lillard《Montessori from the Start》**:补蒙氏理论(Davies 是实操,Lillard 是理论)
4. **接 RIE / Lansbury《Elevating Child Care》**:跟 Gopnik "陪伴 > 教学"深度对话
5. **接 Shonkoff / Phillips《From Neurons to Neighborhoods》**:NIH 早期发展百科,Gopnik 突触章节深化
6. **补 G-PERSON-Bruner**(Gopnik 师承,长童年期假说提出者)

---

*v1.0 · 2026-05-03 — Phase 5 第二本(并行 Gopnik)完整记录*
*基于 PHASE4_WONDER_WEEKS v1.0 段定义 + 并行协调框架*
*与 Phase 5 第一本(Davies SRC-014)并行执行,无 ID 冲突*
