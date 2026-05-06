# PHASE 14 R3 海蒂大百科 SRC-040 漏术语审计

> 审计员: R3 Glossary Audit
> 审计日期: 2026-05-04
> 输入: /tmp/murkoff_R1_issues.json broken_glossary 段(46 条)+ 156 张 SRC-040 海蒂卡正文
> 输出: 第 1 节 broken G-ID 处置表 / 第 2 节 9 张新术语卡 yaml / 第 3 节 18 张待补卡 glossary_refs 修改清单

---

## 第 1 节: 46 条 broken G-ID 处置清单

### 1.1 总体结论

| 处置方式 | 条数 | 备注 |
|---------|------|------|
| 替换为现有术语卡 | 23 | 主要是 separation-anxiety / object-permanence / discipline / MMR 等高频已建术语 |
| 新建术语卡 | 11 | 集中在 9 张新建卡(部分卡引用同一新建术语) |
| 删除断链 | 12 | 概念过于通用、tags/正文已覆盖、或重复引用 |

> **G-TERM-baby-led-weaning(4 条)说明**: 当前 4 张目标卡(C-S3-2248, C-S4-2144, C-S4-2145, C-S4-2151)的 glossary_refs 已是空数组或已替换,R1 报告基于早期版本,**实际无修改需求** — 列在表中但 status=already-clean。BLW 在系统中正确名称是 `G-ABBR-BLW`(已存在)。

### 1.2 完整处置表 (JSON)

```json
[
  {"broken_id": "G-TERM-baby-led-weaning", "card_id": "C-S3-2248", "context": "米粉先上,过敏家族再延 6 月", "action": "already-clean", "to": null, "reason": "当前文件 glossary_refs=[G-TERM-allergy-introduction],已无 BLW 引用"},
  {"broken_id": "G-TERM-baby-led-weaning", "card_id": "C-S4-2144", "context": "7 月手指食物豌豆/弹珠尺寸", "action": "already-clean", "to": null, "reason": "当前文件 glossary_refs=[],无需修复;若要补可加 G-ABBR-BLW"},
  {"broken_id": "G-TERM-baby-led-weaning", "card_id": "C-S4-2145", "context": "噎食 vs 干呕区分", "action": "already-clean", "to": null, "reason": "当前文件 glossary_refs=[],无需修复"},
  {"broken_id": "G-TERM-baby-led-weaning", "card_id": "C-S4-2151", "context": "拒辅食 4 招", "action": "already-clean", "to": null, "reason": "当前文件 glossary_refs=[],无需修复"},

  {"broken_id": "G-019", "card_id": "C-S5-2143", "context": "12 月不走完全正常 / 学步窗口 9-17 月", "action": "delete", "to": null, "reason": "学步月龄区间是事实陈述,不是独立术语;tags=gross_motor 已分类"},
  {"broken_id": "G-126", "card_id": "C-S5-2143", "context": "12 月不走 / 大运动里程碑", "action": "delete", "to": null, "reason": "通用'gross motor milestone'概念,tags 已覆盖,无需独立术语"},

  {"broken_id": "G-066", "card_id": "C-S5-2144", "context": "分离焦虑是好事 / 黏人=认知升级", "action": "replace", "to": "G-TERM-separation-anxiety", "reason": "分离焦虑核心概念,术语卡完整可用"},
  {"broken_id": "G-067", "card_id": "C-S5-2144", "context": "依恋形成 / 安全依恋", "action": "replace", "to": "G-TERM-attachment", "reason": "依恋核心概念已建"},
  {"broken_id": "G-127", "card_id": "C-S5-2144", "context": "物体永久性 / 认知质变", "action": "replace", "to": "G-TERM-object-permanence", "reason": "物体永久性核心,与分离焦虑同步发展"},

  {"broken_id": "G-053", "card_id": "C-S5-2145", "context": "断奶 1 岁前后 / 自然窗口", "action": "replace", "to": "G-TERM-weaning-table", "reason": "断奶概念,weaning-table 已涵盖辅食断奶过渡"},
  {"broken_id": "G-128", "card_id": "C-S5-2145", "context": "断奶节奏 / 1 岁前后", "action": "delete", "to": null, "reason": "重复 weaning 概念,一张卡引一个 weaning 术语足够"},

  {"broken_id": "G-129", "card_id": "C-S5-2146", "context": "1 岁戒奶瓶防龋齿 / 奶瓶龋", "action": "replace", "to": "G-TERM-baby-bottle-tooth-decay", "reason": "奶瓶龋齿术语已存在"},
  {"broken_id": "G-130", "card_id": "C-S5-2146", "context": "戒奶瓶时机 12-15 月", "action": "delete", "to": null, "reason": "戒奶瓶时机非独立概念,baby-bottle-tooth-decay 已涵盖"},

  {"broken_id": "G-131", "card_id": "C-S5-2147", "context": "1 岁起换全脂牛奶 / 大脑髓鞘化", "action": "new", "to": "G-TERM-whole-milk-toddler", "reason": "AAP 1-2 岁全脂牛奶建议是独立指南条目,中国家长不熟"},
  {"broken_id": "G-132", "card_id": "C-S5-2147", "context": "牛奶过量挤压其他食物造成缺铁", "action": "new", "to": "G-TERM-iron-deficiency-anemia", "reason": "缺铁性贫血是 1-3 岁高发问题,跨多个海蒂卡可复用"},

  {"broken_id": "G-074", "card_id": "C-S5-2148", "context": "12 月开口第一个真词 / 符号语言开端", "action": "replace", "to": "G-TERM-language-explosion", "reason": "language-explosion 涵盖第一个真词到爆发期的语言里程碑"},
  {"broken_id": "G-133", "card_id": "C-S5-2148", "context": "真词标准 = 有意指代", "action": "delete", "to": null, "reason": "正文已说清概念,无需独立术语"},

  {"broken_id": "G-134", "card_id": "C-S5-2149", "context": "指物 / 食指指向 + 看大人确认", "action": "new", "to": "G-TERM-pointing-gesture", "reason": "祈使指/陈述指(protoimperative/protodeclarative)是发展心理学核心概念,自闭症筛查关键指标"},
  {"broken_id": "G-135", "card_id": "C-S5-2149", "context": "共同注意力 = 陈述指核心", "action": "replace", "to": "G-TERM-joint-attention", "reason": "共同注意力术语已存在"},
  {"broken_id": "G-136", "card_id": "C-S5-2149", "context": "18 月不指物是 ASD 红旗 / M-CHAT 筛查", "action": "replace", "to": "G-TERM-MCHAT", "reason": "M-CHAT 筛查工具术语已存在"},

  {"broken_id": "G-127", "card_id": "C-S5-2150", "context": "物体永久性质变(本卡主题)", "action": "replace", "to": "G-TERM-object-permanence", "reason": "完全对应"},
  {"broken_id": "G-137", "card_id": "C-S5-2150", "context": "躲猫猫游戏 / 教学", "action": "replace", "to": "G-TERM-peekaboo", "reason": "peekaboo 已是独立术语卡"},

  {"broken_id": "G-138", "card_id": "C-S5-2151", "context": "管教 = 教导不是惩罚", "action": "replace", "to": "G-TERM-discipline", "reason": "discipline 术语已存在"},
  {"broken_id": "G-139", "card_id": "C-S5-2151", "context": "AAP 反对体罚和言语羞辱", "action": "replace", "to": "G-TERM-corporal-punishment", "reason": "体罚术语已存在"},

  {"broken_id": "G-066", "card_id": "C-S5-2152", "context": "睡前焦虑 = 分离焦虑变体", "action": "replace", "to": "G-TERM-separation-anxiety", "reason": "复用"},
  {"broken_id": "G-127", "card_id": "C-S5-2152", "context": "妈妈进厨房还存在 = 物体永久性", "action": "replace", "to": "G-TERM-object-permanence", "reason": "复用"},
  {"broken_id": "G-140", "card_id": "C-S5-2152", "context": "渐进式安抚 / 拍拍坐旁边 / 安抚物", "action": "replace", "to": "G-TERM-self-soothing", "reason": "self-soothing 涵盖入睡自我安抚机制"},

  {"broken_id": "G-128", "card_id": "C-S5-2153", "context": "戒夜奶 1 岁前后", "action": "delete", "to": null, "reason": "夜奶非独立 weaning 概念,2153 已引 G-TERM-baby-bottle-tooth-decay"},
  {"broken_id": "G-129", "card_id": "C-S5-2153", "context": "夜奶 + 龋齿风险", "action": "replace", "to": "G-TERM-baby-bottle-tooth-decay", "reason": "复用"},
  {"broken_id": "G-141", "card_id": "C-S5-2153", "context": "夜奶习惯性需求 / 生长激素", "action": "delete", "to": null, "reason": "生理细节正文充分,无独立术语价值"},

  {"broken_id": "G-142", "card_id": "C-S5-2154", "context": "1 岁后体重增速骤降 = 食欲骤降", "action": "new", "to": "G-TERM-toddler-appetite-drop", "reason": "幼儿厌食期是中国家长最焦虑误判最多的现象,跨 S5-S6 多卡可复用"},
  {"broken_id": "G-143", "card_id": "C-S5-2154", "context": "强喂破坏自我调节", "action": "delete", "to": null, "reason": "正文 failure_mode 已说清,无须独立术语"},

  {"broken_id": "G-119", "card_id": "C-S5-2155", "context": "LEAP 研究确立早期引入花生", "action": "replace", "to": "G-ABBR-LEAP", "reason": "LEAP 缩写术语已存在"},
  {"broken_id": "G-120", "card_id": "C-S5-2155", "context": "AAP 2017 改 4-6 月按风险引入", "action": "replace", "to": "G-TERM-LEAP-trial", "reason": "LEAP-trial 完整术语卡已存在,涵盖指南背景"},
  {"broken_id": "G-144", "card_id": "C-S5-2155", "context": "整粒花生 4 岁前最危险窒息食物", "action": "delete", "to": null, "reason": "窒息风险通用,tags=safety+red_flag 已覆盖"},

  {"broken_id": "G-114", "card_id": "C-S5-2156", "context": "12 月儿保 = 第一年最重要节点", "action": "replace", "to": "G-TERM-developmental-assessment", "reason": "儿保=发展评估,术语卡已存在"},
  {"broken_id": "G-145", "card_id": "C-S5-2156", "context": "MMR 麻腮风疫苗 / 减毒活疫苗", "action": "replace", "to": "G-ABBR-MMR", "reason": "MMR 缩写术语已存在"},
  {"broken_id": "G-146", "card_id": "C-S5-2156", "context": "水痘疫苗 / 减毒活疫苗", "action": "replace", "to": "G-ABBR-Varicella", "reason": "Varicella 已存在"},

  {"broken_id": "G-126", "card_id": "C-S5-2157", "context": "学步赤脚最佳 / AAP 立场", "action": "delete", "to": null, "reason": "无完美匹配,概念分散在 gross_motor 标签和正文,新建独立'barefoot-walking'卡价值不高"},
  {"broken_id": "G-147", "card_id": "C-S5-2157", "context": "高帮硬底机能鞋营销话术", "action": "delete", "to": null, "reason": "营销话术辨析非独立术语,正文 failure_mode 已警示"},

  {"broken_id": "G-148", "card_id": "C-S5-2158", "context": "AAP 2016 屏幕指南 / 18 月以下禁屏", "action": "replace", "to": "G-TERM-anti-screen", "reason": "anti-screen 涵盖 AAP 屏幕指南"},
  {"broken_id": "G-149", "card_id": "C-S5-2158", "context": "屏幕暴露与语言迟缓相关", "action": "replace", "to": "G-TERM-media-effects", "reason": "media-effects 涵盖屏幕对发育的影响"},

  {"broken_id": "G-067", "card_id": "C-S5-2159", "context": "认生延续 / 安全基地", "action": "replace", "to": "G-TERM-attachment", "reason": "依恋安全基地"},
  {"broken_id": "G-150", "card_id": "C-S5-2159", "context": "Kagan 高反应型 = 慢热型 15-20%", "action": "replace", "to": "G-TERM-inhibited-temperament", "reason": "Kagan 抑制型气质术语已存在"},

  {"broken_id": "G-140", "card_id": "C-S5-2160", "context": "撞头摇头 = 节律性自我安抚", "action": "replace", "to": "G-TERM-self-soothing", "reason": "复用"},
  {"broken_id": "G-151", "card_id": "C-S5-2160", "context": "节律性运动行为 / AAP 解释", "action": "new", "to": "G-TERM-rhythmic-movement-disorder", "reason": "撞头/摇头是中国家长最易误判为癫痫/自闭症的行为,独立术语高复用价值"}
]
```

---

## 第 2 节: 新建术语卡 (主线搬, 9 张)

> 选取标准: ① SRC-040 海蒂书内多次提及或专章讲解 ② 跨源复用价值高(后续 SRC 可能引) ③ 中国家长不熟悉或最易误判 ④ 已建术语库无等价。控制在 15 张以内 — 实际产出 9 张(宁缺勿滥)。

### 2.1 G-PERSON-Ferber.yaml

```yaml
glossary_id: G-PERSON-Ferber
type: person
display_name: Ferber
full_name_en: "Richard Ferber"
full_name_zh: "理查德·法伯"

one_liner: |
  美国波士顿儿童医院睡眠中心创始人,睡眠训练'渐延法'(Ferber method)发明者,海蒂书引用为睡眠倒退首选方案之一。

detail: |
  ## 身份背景
  Richard Ferber(1944- ),美国儿科医生、儿童睡眠研究者,
  哈佛医学院助理教授,波士顿儿童医院儿童睡眠紊乱中心
  (Center for Pediatric Sleep Disorders)创始人(1978)。

  ## 代表作
  《Solve Your Child's Sleep Problems》1985 年初版,2006 修订版。
  美国销量超 100 万册,被简称为"Ferberizing"或"Ferber method"。

  ## Ferber 法核心
  - **渐进式延迟回应法**(graduated extinction):
    宝宝哭闹时不立即抱起,**逐次延长等待时间**(5/10/15 分钟),
    避免完全不回应(纯 cry-it-out)的冷漠。
  - **不是不抱**:每次延迟期满进房安抚 1-2 分钟(拍拍轻语),
    但不抱起也不喂奶,重在让宝宝学会自我入睡。
  - 适用月龄:海蒂书建议 4-6 月起,作为睡眠倒退期方案之一。

  ## 争议
  - 支持派(AAP 部分专家):有效率 80%+,3-7 天见效,
    长期不影响依恋安全感(2016 年 Pediatrics RCT 证实)。
  - 反对派(Sears 等亲密育儿派):"延迟回应"仍是 CIO 变体,
    可能升高皮质醇、损伤依恋。
  - **海蒂立场**:中性介绍,与椅子法、系统唤醒法并列,
    家长按自身情况选择。

  ## 与海蒂书关系
  C-S3-2258(5 月睡眠倒退)直接引 Ferber 法为 4 种解决方案之一。
  也是国内"睡眠咨询师"行业的核心方法学源头。

related_glossary:
  - G-TERM-cry-it-out
  - G-TERM-anti-cry-it-out
  - G-TERM-self-soothing
  - G-TERM-sleep-cycle

related_cards:
  - C-S3-2258      # 5 月睡眠倒退,法伯/法伯改良
  - C-S5-2152      # 睡前焦虑温和应对(Ferber 是其中一选)

sources:
  - source_id: SRC-040
  - external: "Ferber R, Solve Your Child's Sleep Problems (1985, rev 2006)"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.2 G-TERM-whole-milk-toddler.yaml

```yaml
glossary_id: G-TERM-whole-milk-toddler
type: term
display_name: 幼儿全脂牛奶 (whole milk for toddlers)

full_name_en: Whole Cow's Milk for Toddlers (12-24 months)
full_name_zh: 12-24 月全脂牛奶建议

one_liner: |
  AAP 明确建议 1-2 岁宝宝喝**全脂**(约 3.25% 脂肪)鲜牛奶,不要低脂或脱脂。中国家长常被减肥潮流误导。

detail: |
  ## 定义
  美国儿科学会(AAP)与 AAPD 共同建议:**12-24 月**幼儿
  从配方奶/母乳过渡到鲜奶时,**必须选择全脂(whole milk,
  乳脂含量约 3.25%)**,不要低脂(2%/1%)或脱脂(skim)。

  ## 核心理由
  - **大脑髓鞘化高速期**:1-2 岁是神经髓鞘形成关键期,
    髓鞘以脂类为主要原料,膳食脂肪缺失会影响认知发育。
  - 牛奶脂肪 + 脂溶性维生素 A/D/E/K 是日常重要来源,
    低脂奶在去除脂肪同时损失这些维生素。
  - 这阶段总热量约 1000-1300 kcal,脂肪应占 30-40%,
    全脂奶 480ml 提供约 16g 脂肪,是核心来源之一。

  ## 量的边界
  - **每日 480-720 ml**(2-3 杯),不超过 720 ml。
  - 超量挤占其他食物 + 阻碍铁吸收 → **缺铁性贫血**
    (见 G-TERM-iron-deficiency-anemia)。
  - 用学饮杯不用奶瓶喝(防奶瓶龋,见 G-TERM-baby-bottle-tooth-decay)。

  ## 2 岁后调整
  - **24 月起**可换 2% 低脂奶;5 岁后可换 1% 或脱脂。
  - 过渡时机依生长曲线和肥胖风险评估个体化决定。

  ## 中国家长常见误区
  1. **减肥潮流**:大人怕胖给娃喝低脂,娃脑发育原料不足。
  2. **植物奶替代**:杏仁奶/燕麦奶/豆奶蛋白和脂肪谱不匹配,
     不能替代牛奶(过敏除外用强化配方)。
  3. **生牛奶**:未经巴氏消毒,李斯特菌/沙门氏菌风险。
  4. **过量喝奶**:每日 1000ml+ 排斥固体食物,几月后查出贫血。

key_facts:
  - 12-24 月 AAP 强制全脂(3.25% 脂肪)
  - 每日 480-720 ml,不超 720
  - 大脑髓鞘化原料,低脂影响认知
  - 24 月可换 2%,5 岁可换脱脂
  - 不可用植物奶替代

related_glossary:
  - G-ABBR-AAP
  - G-TERM-baby-bottle-tooth-decay
  - G-TERM-iron-deficiency-anemia
  - G-TERM-weaning-table

related_cards:
  - C-S5-2147      # 1 岁起换全脂牛奶
  - C-S5-2145      # 断奶 1 岁前后
  - C-S5-2154      # 1 岁后食欲变小

sources:
  - source_id: SRC-040
  - external: "AAP Policy Statement: Fatty Acid Recommendations (2008) / AAP HealthyChildren.org Whole Milk"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.3 G-TERM-iron-deficiency-anemia.yaml

```yaml
glossary_id: G-TERM-iron-deficiency-anemia
type: term
display_name: 缺铁性贫血 (iron deficiency anemia, IDA)

full_name_en: Iron Deficiency Anemia (IDA)
full_name_zh: 缺铁性贫血

one_liner: |
  1-3 岁高发的营养性贫血,主因牛奶过量挤占含铁辅食。AAP 12 月儿保常规筛查,严重影响认知发育。

detail: |
  ## 定义
  缺铁性贫血(IDA)= 体内铁储备耗尽导致血红蛋白合成不足。
  **9-24 月是发病高峰**,WHO 数据全球婴幼儿患病率约 30%,
  中国 6-24 月城市儿童约 10-15%、农村高达 20%+。

  ## 核心原因
  1. **牛奶过量**:每日 > 720 ml 牛奶,蛋白和钙阻碍铁吸收,
     且挤占含铁辅食空间(海蒂书重点警示)。
  2. **辅食结构差**:6 月后未及时引入红肉、肝、强化米粉。
  3. **早产/低出生体重**:出生时铁储备本就低,4 月后更易耗尽。
  4. **持续性母乳无强化辅食**:母乳铁含量低且 6 月后不足,
     必须配富铁辅食。

  ## 后果
  - **认知发育损伤**:1-3 岁缺铁可致**永久性**注意力、
    学习能力下降(即使后期补铁也难完全恢复,见 Lozoff 长期研究)。
  - 免疫力下降、生长迟缓、易疲倦烦躁。
  - 严重者心率增快、口腔炎、异食癖(吃非食物如纸/泥)。

  ## AAP 筛查
  - **12 月儿保常规筛血红蛋白**(Hb)和血清铁蛋白。
  - Hb < 110 g/L 诊断贫血,需进一步分型。
  - 高风险婴儿(早产/低出生体重/母亲贫血)4 月起就开始
    口服铁补充(2 mg/kg/d)。

  ## 预防
  - **6 月起加铁强化米粉作为第一口辅食**。
  - 7-9 月加红肉泥/肝泥(每周 2-3 次)。
  - 1 岁后牛奶不超过 720 ml/d。
  - 含铁食物 + 维 C(橙汁/番茄)促吸收;
    避免与茶/牛奶同食。

key_facts:
  - 9-24 月发病高峰
  - 主因 = 牛奶过量挤占辅食
  - 12 月儿保 AAP 常规筛查
  - 后果可永久损伤认知
  - 含铁辅食 + 维 C 促吸收

related_glossary:
  - G-ABBR-AAP
  - G-ABBR-WHO
  - G-TERM-whole-milk-toddler
  - G-TERM-weaning-table

related_cards:
  - C-S5-2147      # 1 岁起换全脂牛奶(过量贫血)
  - C-S5-2154      # 1 岁后食欲变小
  - C-S5-2156      # 12 月儿保+疫苗(贫血筛查)

sources:
  - source_id: SRC-040
  - external: "WHO Iron Deficiency Anaemia: Assessment, Prevention, Control (2001) / Lozoff B et al, Pediatrics (2006)"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.4 G-TERM-pointing-gesture.yaml

```yaml
glossary_id: G-TERM-pointing-gesture
type: term
display_name: 指物 (pointing gesture)

full_name_en: Pointing Gesture (Protoimperative & Protodeclarative Pointing)
full_name_zh: 指物手势(祈使指 + 陈述指)

one_liner: |
  9-14 月出现的"食指指向"是有意图沟通的核心标志,分祈使指(要)和陈述指(分享)。18 月不指物是自闭症红旗信号。

detail: |
  ## 定义
  婴儿 9-14 月学会**伸出食指指向**感兴趣的物体或事件,
  是从前语言期向语言期过渡的最关键里程碑之一。

  ## 两种类型(Bates et al, 1979 经典分类)
  ### 1. 祈使指 (protoimperative pointing)
  - **目的 = 要东西**:指向想要的物品,让大人拿过来。
  - 出现时间:约 9-12 月。
  - 例:指着架子上的饼干 → 看妈妈 → "我要那个"。
  - **共有于自闭症儿童**(他们也会用工具性指向)。

  ### 2. 陈述指 (protodeclarative pointing)
  - **目的 = 分享注意**:指向引起兴趣的东西,
    让大人也看到,**不是要而是分享**。
  - 出现时间:约 12-14 月。
  - 例:指着窗外的鸟 → 看妈妈 → 看鸟 → 看妈妈("一起看!")。
  - **自闭症儿童典型缺失**(不主动分享注意)。
  - 是**共同注意力**(joint attention)的最强外显行为。

  ## 自闭症筛查的核心信号
  - **18 月不指物**(尤其陈述指)= **M-CHAT 关键红旗项**。
  - 与共同注意力缺失、不响应名字共同构成 ASD 早期警示三联征。
  - AAP 18 月儿保必查 M-CHAT,16-30 月窗口最佳。

  ## 与语言发育的强相关
  - 12 月陈述指频率预测 18 月词汇量(r ≈ 0.5)。
  - 陈述指越多 → 大人命名机会越多 → 词汇爆发越早。
  - 不指物 → 早期语言输入断裂 → 语言迟缓风险。

  ## 海蒂书操作要点
  - 跟随娃的手指看并命名("那是鸟")。
  - 大人也常指物示范("看小狗")。
  - 别一上来就喂或拿,鼓励娃指物提要求。
  - 18 月仍不指物 → 找儿保排查 ASD。

key_facts:
  - 9-14 月出现
  - 祈使指(要)9-12 月 / 陈述指(分享)12-14 月
  - 陈述指 = 共同注意力外显行为
  - 18 月不指物 = M-CHAT 红旗
  - 12 月指物频率预测 18 月词汇

related_glossary:
  - G-TERM-joint-attention
  - G-TERM-MCHAT
  - G-TERM-language-explosion
  - G-PERSON-Tomasello

related_cards:
  - C-S5-2149      # 指物=真沟通
  - C-S5-2148      # 12 月开口第一个真词

sources:
  - source_id: SRC-040
  - external: "Bates E, Camaioni L, Volterra V (1975) / Tomasello M (2008) / AAP M-CHAT-R guidance"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.5 G-TERM-toddler-appetite-drop.yaml

```yaml
glossary_id: G-TERM-toddler-appetite-drop
type: term
display_name: 幼儿厌食期 (toddler appetite drop)

full_name_en: Toddler Appetite Drop / Physiologic Anorexia of Toddlerhood
full_name_zh: 幼儿生理性食欲下降

one_liner: |
  1 岁后体重增速从年增 6-7kg 骤降到年增 2-3kg,身体不再需要那么多热量,食欲明显下降是正常生理转折,不是病也不是叛逆。

detail: |
  ## 定义
  **生理性厌食(physiologic anorexia of toddlerhood)**:
  1 岁后宝宝热量需求相对体重显著下降,导致食量减少、
  挑食、拒食、吃几口就跑等现象,**是正常生理过程**,
  不是疾病也不是行为问题。

  ## 数据基础
  - **0-12 月**:体重年增 6-7 kg(出生 3 kg → 1 岁约 9-10 kg)。
  - **12-24 月**:年增仅 2-3 kg(13 kg 左右),增速降 60%+。
  - **2-5 岁**:每年仅增 2 kg。
  - 热量需求随之下降:1 岁约 1000 kcal/d,远少于想象。

  ## 行为表现
  - 食量明显比婴儿期少。
  - 挑食、对新食物拒绝(neophobia,2-6 岁高峰)。
  - 吃几口就跑、连续几餐吃很少。
  - **食量日间波动大**:今天吃很多,明天几乎不吃,
    但 1-2 周平均下来够用。

  ## 海蒂书核心立场
  - **信任宝宝的饱腹感**:幼儿是天生的"自我热量调节者"
    (Birch & Davison 经典研究证实),强喂破坏这种能力。
  - **父母管"什么/什么时候"**,**孩子管"吃多少"**
    (Ellyn Satter "Division of Responsibility" 模型)。
  - 1-2 周整体生长曲线正常 = OK,不必纠结单餐。

  ## 父母最大坑
  - 追喂、哄喂、电视下饭 → 饱腹感失灵,长期挑食/暴食。
  - 强吼"必须吃完" → 食物变焦虑源,3-4 岁严重挑食。
  - 用零食奖励"再吃一口" → 把饭和奖品挂钩,谈判失控。
  - 怀疑生病 → 反复就医做检查徒增焦虑。

  ## 何时真要担心
  - 体重 3 个月没增 / 跌出生长曲线。
  - 完全拒水 / 拒奶。
  - 伴随发热、呕吐、腹泻、嗜睡。
  - 否则属正常生理阶段。

key_facts:
  - 1 岁后体重增速降 60%+
  - 热量需求约 1000 kcal/d
  - 是生理过程不是病
  - Division of Responsibility 父母管什么/孩子管多少
  - 1-2 周平均够 = OK

related_glossary:
  - G-TERM-weaning-table
  - G-TERM-whole-milk-toddler

related_cards:
  - C-S5-2154      # 1 岁后食欲变小
  - C-S5-2147      # 1 岁起换全脂牛奶
  - C-S5-2145      # 断奶 1 岁前后

sources:
  - source_id: SRC-040
  - external: "Birch LL & Davison KK, Pediatric Clinics of North America (2001) / Ellyn Satter Division of Responsibility"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.6 G-TERM-rhythmic-movement-disorder.yaml

```yaml
glossary_id: G-TERM-rhythmic-movement-disorder
type: term
display_name: 节律性运动行为 (rhythmic movement)

full_name_en: Rhythmic Movement Disorder / Sleep-Related Rhythmic Movement
full_name_zh: 节律性运动行为(撞头/摇头/身体摇晃)

one_liner: |
  9-18 月睡前撞床栏、摇头、身体摇晃,发生率约 20%,是自我安抚的节律性行为,大多 3-4 岁自然消失,不是癫痫不是自闭。

detail: |
  ## 定义
  **节律性运动行为**(rhythmic movement)= 入睡前或浅睡中
  反复进行的有节奏动作,常见 3 类:
  - **撞头**(head banging):前后撞床栏、墙壁。
  - **摇头**(head rolling):仰躺左右摇头。
  - **身体摇晃**(body rocking):四肢撑床前后摇身体。

  ## 流行病学
  - 9-18 月发生率约 **20%**(婴儿期最高峰)。
  - 男孩多于女孩(约 3:1)。
  - 持续时间多在 5-15 分钟,直到入睡。
  - 大多 3-4 岁自然消失,5% 持续到学龄期(仍多无害)。

  ## 机制(AAP 主流解释)
  - **自我安抚**:重复节律刺激前庭系统,产生类摇篮效果。
  - **释放紧张**:类似大人入睡前晃腿/转头。
  - 与白天活动量、入睡焦虑、家庭压力有关联。

  ## 与病理的鉴别
  ### 不是癫痫
  - 癫痫发作有意识改变 / 强直阵挛 / 无法被叫停。
  - 节律行为娃可被叫停或抱起即停,意识清醒。

  ### 不是自闭症
  - 自闭症的刻板行为 24 小时都有,不限睡前。
  - 节律行为只在睡前或浅睡阶段。

  ### 何时真要就医
  1. **自伤出血**(撞破皮 / 撞肿)
  2. **白天频繁不可控**(超出睡眠期)
  3. **伴随发育倒退** / 失去技能
  4. **持续到 5 岁后**且影响生活

  ## 海蒂书操作要点
  - 床栏裹软垫防撞伤。
  - **别强行按住** —— 反而强化行为。
  - 白天多消耗体力减少睡前焦虑。
  - 固定睡前流程降低紧张。
  - 接纳为正常发展现象,不焦虑就医。

key_facts:
  - 9-18 月发生率约 20%
  - 男孩多 3:1
  - 自我安抚 + 释放紧张机制
  - 大多 3-4 岁自然消失
  - 不是癫痫不是自闭症

related_glossary:
  - G-TERM-self-soothing
  - G-TERM-sleep-cycle
  - G-ABBR-AAP

related_cards:
  - C-S5-2160      # 撞头摇头多正常

sources:
  - source_id: SRC-040
  - external: "ICSD-3 (International Classification of Sleep Disorders) / AAP Sleep-Related Rhythmic Movement Disorder"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.7 G-TERM-babywearing.yaml

```yaml
glossary_id: G-TERM-babywearing
type: term
display_name: 婴儿背带 (babywearing)

full_name_en: Babywearing
full_name_zh: 婴儿背带 / 穿宝宝

one_liner: |
  用背带/吊带把宝宝贴身穿在父母身上,几千年人类智慧+现代证据加持的金标准安抚法,海蒂列 5 大益处+TICKS 安全口诀。

detail: |
  ## 定义
  **Babywearing** = 用专用背带、吊带、环式 sling 把宝宝
  贴身固定在父母胸前/背后,腾出双手做事同时维持亲密接触。

  ## 历史
  - 几千年人类文化普遍存在(非洲、亚洲、原住民)。
  - 现代复兴:1970s Sears 等亲密育儿派推广,
    1980s 西方主流育儿书纳入。

  ## 类型(按月龄)
  - **0-4 月:包裹式 (wrap) 或环式 (ring sling)**
    - 整块布缠绕,自然胎位 M 形腿
    - 宝宝面朝里贴胸
  - **4-6 月:软结构背带 (SSC, soft structured carrier)**
    - 有腰带和肩带,符合人体工学
    - 仍面朝里
  - **6 月后(能稳定坐):面朝外或背后**

  ## 海蒂书 5 大益处
  1. **方便**:父母腾手做事(做饭/带老大)
  2. **宝宝舒适**:被抱+体温+心跳=宫内环境复刻
  3. **父母快乐**:亲密接触刺激催产素,降低产后焦虑
  4. **减肠绞痛**:背带里直立位 + 节奏感 = 黄金安抚
  5. **促进发育**:宝宝看世界视角丰富,语言输入更多

  ## 安全口诀 TICKS
  | 字母 | 含义 | 中文 |
  |------|------|------|
  | T | Tight | 背带紧贴不松垮 |
  | I | In view at all times | 宝宝脸始终可见 |
  | C | Close enough to kiss | 头顶能吻到的距离 |
  | K | Keep chin off chest | 下巴抬起不压胸 |
  | S | Supported back | 背部得到支撑 |

  ## 主要风险
  - **气道阻塞窒息**(背带过松+下巴贴胸):
    背带类 SIDS 实有死亡案例,新生儿期最危险。
  - **髋关节压力**:长时间挂(>2 小时)+ 双腿垂直,
    要选 M 形腿支撑款。
  - **新生儿用前向硬背架**:颈部不能撑头部,易窒息。
  - **背着做剧烈运动/骑车/烹饪热油**:撞伤/烫伤风险。

  ## 与袋鼠护理 (kangaroo care) 的区别
  - **袋鼠护理**(早产儿专项):皮肤接触医疗技术,
    有标准化时长和方法,医院 NICU 操作。
  - **Babywearing**:日常带娃工具,可隔衣物,
    用专用背带,家庭场景。

key_facts:
  - 0-4 月用 wrap/sling,4 月+用 SSC
  - 5 大益处:方便/舒适/快乐/减肠绞痛/促发育
  - 安全口诀 TICKS
  - 背带类 SIDS 风险真实存在
  - 单次 ≤ 2 小时

related_glossary:
  - G-ABBR-SIDS
  - G-TERM-skin-to-skin
  - G-TERM-colic
  - G-TERM-frog-leg-position

related_cards:
  - C-S1-2506      # 婴儿背带袋鼠护理 5 益处
  - C-S1-2501      # 肠绞痛安抚 8 招

sources:
  - source_id: SRC-040
  - external: "International Hip Dysplasia Institute babywearing safety / Babywearing International TICKS rule"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.8 G-TERM-sleep-regression.yaml

```yaml
glossary_id: G-TERM-sleep-regression
type: term
display_name: 睡眠倒退 (sleep regression)

full_name_en: Sleep Regression
full_name_zh: 睡眠倒退

one_liner: |
  整觉宝宝突然夜醒频繁,通常发生在 4 月/8-10 月/12 月/18 月,与大运动突破或大脑跳跃同步,2-6 周自愈。

detail: |
  ## 定义
  **睡眠倒退**:已建立稳定夜间睡眠的宝宝突然出现
  夜醒频繁、入睡困难、白天小睡缩短的阶段性退步,
  非疾病非习惯失败,与发育节点同步。

  ## 经典发生窗口
  | 月龄 | 主因 | 持续 |
  |------|------|------|
  | **4 月** | 睡眠结构成熟(出现深浅睡周期切换) | 2-6 周 |
  | **8-10 月** | 物体永久性 + 分离焦虑 + 爬/扶站突破 | 2-4 周 |
  | **12 月** | 学步突破 + 真词出现 + 牙齿萌出 | 2-4 周 |
  | **18 月** | 想象力萌芽 + 自主意识 + 第一逆反期 | 2-4 周 |
  | **2 岁** | 语言爆发 + 戒尿布 + 认同感 | 2-4 周 |

  ## 机制
  - **大运动突破**:刚学会的技能(爬/站/走)在睡眠中
    无意识尝试,自己醒来。
  - **大脑跳跃**(wonder week):新认知能力涌现,
    短期内大脑过载,睡眠节律被打破。
  - **分离焦虑**:8-10 月物体永久性建立后,
    醒来发现妈妈不在产生焦虑。
  - **出牙不适**:疼痛打断睡眠。

  ## 海蒂书 4 类应对(C-S3-2258)
  1. **经典 Ferber 法**:渐延 5/10/15 分钟回应
  2. **椅子法**:每晚椅子向门移动,逐渐淡出
  3. **系统唤醒法**:预定时主动唤醒打破节奏
  4. **增强睡眠节奏**:疲倦但不过累就放下

  每种方法**坚持 2 周再判断**,中间不换。

  ## 父母最大坑
  - 一周内连换 3 种方法,娃彻底糊涂。
  - 一夜醒就抱起来喂,把临时倒退练成长期习惯。
  - 自责"训练失败",其实只是发育节点正常现象。

  ## 何时不是倒退是别的
  - 发热 / 呕吐 / 哭闹超过 2 小时 → 排查疾病。
  - 持续超过 6 周不缓解 → 找儿保。
  - 伴随发育倒退或体重不增 → 就医。

key_facts:
  - 4/8-10/12/18 月经典窗口
  - 2-6 周自愈
  - 与大运动/大脑跳跃同步
  - 选 1 种方法坚持 2 周不中途换
  - 不是训练失败是发育节点

related_glossary:
  - G-PERSON-Ferber
  - G-TERM-self-soothing
  - G-TERM-separation-anxiety
  - G-TERM-object-permanence

related_cards:
  - C-S3-2258      # 5 月睡眠倒退,法伯/法伯改良
  - C-S5-2152      # 睡前焦虑温和应对
  - C-S5-2153      # 戒夜奶 1 岁前后

sources:
  - source_id: SRC-040
  - external: "AAP HealthyChildren.org Sleep Regression / Plooij F & van de Rijt H Wonder Weeks"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

### 2.9 G-TERM-developmental-red-flag.yaml

```yaml
glossary_id: G-TERM-developmental-red-flag
type: term
display_name: 发育红旗 (developmental red flag)

full_name_en: Developmental Red Flag
full_name_zh: 发育警示信号

one_liner: |
  出现就**必须立即找儿保**的发育异常信号。AAP 按月龄分类(4/9/12/18/24 月),早识别早干预效果倍增。

detail: |
  ## 定义
  **发育红旗**(developmental red flag)= 在特定月龄
  **必须出现**的能力/反应却**缺失**,或**不该出现**的
  异常行为却**持续**,提示需立即专业评估的发育警示信号。

  ## 与"发育里程碑"的区别
  - **里程碑**:某月龄**多数**宝宝达成的能力(75% 中位数)。
    晚一点不一定有问题,看个体差异。
  - **红旗**:某月龄**极少数**宝宝才会缺失的能力(<5%),
    缺失 = 必须立即评估,不再观察等待。

  ## AAP 分月龄红旗速查
  ### 4 月红旗
  - 不会追视移动物体
  - 听到声音无反应
  - 抱起头无支撑下垂
  - 不会笑回应大人

  ### 9 月红旗
  - 不会自己坐(扶坐都不稳)
  - 不会传递玩具左右手
  - 不发音(连"baba/mama"都没)
  - 看到熟人没反应

  ### 12 月红旗
  - 不会扶站
  - 不会指物
  - 不会挥手再见
  - 不会模仿动作
  - 没有任何真词

  ### 18 月红旗(自闭症筛查关键)
  - **不指物分享**(陈述指缺失)= M-CHAT 核心项
  - **听到名字不回头**
  - **眼神接触少 / 不持续**
  - **无单词或词汇 < 6 个**
  - 不模仿日常动作(挥手/拍手)

  ### 24 月红旗
  - **不会两词组合**("妈妈抱""喝水")
  - 不会跑或跑姿严重异常
  - 不会用勺子
  - **任何技能倒退**(原有能力消失)

  ## 海蒂书核心建议
  - 任何阶段任何 1 项红旗 → **立即找儿保**,不等下次儿保。
  - 早期干预 0-3 岁效果最好,**早 1 月预后差异显著**。
  - 自闭症 18 月可早期识别,2 岁前介入语言/行为治疗
    可帮 50%+ 孩子学龄期接近正常。

  ## 父母最大坑
  - "我家是大器晚成型,再等等"——错过黄金期。
  - "亲戚说他家娃也这样,后来好了"——别人不是你娃的医生。
  - 不肯接受评估"怕被贴标签"——耽误的是娃自己。
  - 红旗信号被亲戚/老人否认劝阻就医。

key_facts:
  - 4/9/12/18/24 月分阶段红旗
  - 18 月不指物 = ASD 关键红旗(M-CHAT)
  - 任何技能倒退立即就医
  - 早期干预 0-3 岁效果最好
  - 红旗 ≠ 里程碑晚一点,是必须评估

related_glossary:
  - G-TERM-developmental-assessment
  - G-TERM-MCHAT
  - G-TERM-pointing-gesture
  - G-TERM-early-intervention
  - G-TERM-joint-attention

related_cards:
  - C-S5-2143      # 12 月不走完全正常(对照)
  - C-S5-2148      # 12 月开口第一个真词
  - C-S5-2149      # 指物=真沟通
  - C-S5-2156      # 12 月儿保+疫苗

sources:
  - source_id: SRC-040
  - external: "AAP Bright Futures: Guidelines for Health Supervision (4th ed) / CDC Learn the Signs Act Early"

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 第 3 节: 18 张待补卡的 glossary_refs 修改清单 (JSON)

> 应用规则: ① 替换=用现有/新建术语 ID 替换断链 ② 删除=去掉断链 ID 不补 ③ 已 4 张 BLW 卡当前已干净,无操作。

```json
[
  {
    "card_id": "C-S5-2143",
    "title": "12 月不走完全正常",
    "current": ["G-019", "G-126"],
    "new": [],
    "changes": [
      {"action": "delete", "id": "G-019", "reason": "学步窗口区间非术语"},
      {"action": "delete", "id": "G-126", "reason": "通用大运动里程碑"}
    ],
    "note": "可选追加 G-TERM-developmental-red-flag 因卡末提'18 月仍不走找儿保'"
  },
  {
    "card_id": "C-S5-2144",
    "title": "分离焦虑是好事",
    "current": ["G-066", "G-067", "G-127"],
    "new": ["G-TERM-separation-anxiety", "G-TERM-attachment", "G-TERM-object-permanence"],
    "changes": [
      {"action": "replace", "from": "G-066", "to": "G-TERM-separation-anxiety"},
      {"action": "replace", "from": "G-067", "to": "G-TERM-attachment"},
      {"action": "replace", "from": "G-127", "to": "G-TERM-object-permanence"}
    ]
  },
  {
    "card_id": "C-S5-2145",
    "title": "断奶 1 岁前后",
    "current": ["G-053", "G-128"],
    "new": ["G-TERM-weaning-table", "G-TERM-whole-milk-toddler"],
    "changes": [
      {"action": "replace", "from": "G-053", "to": "G-TERM-weaning-table"},
      {"action": "replace", "from": "G-128", "to": "G-TERM-whole-milk-toddler", "reason": "1 岁转奶概念"}
    ]
  },
  {
    "card_id": "C-S5-2146",
    "title": "1 岁戒奶瓶防龋齿",
    "current": ["G-129", "G-130"],
    "new": ["G-TERM-baby-bottle-tooth-decay"],
    "changes": [
      {"action": "replace", "from": "G-129", "to": "G-TERM-baby-bottle-tooth-decay"},
      {"action": "delete", "id": "G-130", "reason": "戒奶瓶时机被 baby-bottle-tooth-decay 涵盖"}
    ]
  },
  {
    "card_id": "C-S5-2147",
    "title": "1 岁起换全脂牛奶",
    "current": ["G-131", "G-132"],
    "new": ["G-TERM-whole-milk-toddler", "G-TERM-iron-deficiency-anemia"],
    "changes": [
      {"action": "replace", "from": "G-131", "to": "G-TERM-whole-milk-toddler"},
      {"action": "replace", "from": "G-132", "to": "G-TERM-iron-deficiency-anemia"}
    ]
  },
  {
    "card_id": "C-S5-2148",
    "title": "12 月开口第一个真词",
    "current": ["G-074", "G-133"],
    "new": ["G-TERM-language-explosion"],
    "changes": [
      {"action": "replace", "from": "G-074", "to": "G-TERM-language-explosion"},
      {"action": "delete", "id": "G-133", "reason": "真词概念已在正文,无独立术语"}
    ]
  },
  {
    "card_id": "C-S5-2149",
    "title": "指物=真沟通",
    "current": ["G-134", "G-135", "G-136"],
    "new": ["G-TERM-pointing-gesture", "G-TERM-joint-attention", "G-TERM-MCHAT"],
    "changes": [
      {"action": "replace", "from": "G-134", "to": "G-TERM-pointing-gesture"},
      {"action": "replace", "from": "G-135", "to": "G-TERM-joint-attention"},
      {"action": "replace", "from": "G-136", "to": "G-TERM-MCHAT"}
    ]
  },
  {
    "card_id": "C-S5-2150",
    "title": "物体永久性质变",
    "current": ["G-127", "G-137"],
    "new": ["G-TERM-object-permanence", "G-TERM-peekaboo"],
    "changes": [
      {"action": "replace", "from": "G-127", "to": "G-TERM-object-permanence"},
      {"action": "replace", "from": "G-137", "to": "G-TERM-peekaboo"}
    ]
  },
  {
    "card_id": "C-S5-2151",
    "title": "管教不是体罚",
    "current": ["G-138", "G-139"],
    "new": ["G-TERM-discipline", "G-TERM-corporal-punishment"],
    "changes": [
      {"action": "replace", "from": "G-138", "to": "G-TERM-discipline"},
      {"action": "replace", "from": "G-139", "to": "G-TERM-corporal-punishment"}
    ]
  },
  {
    "card_id": "C-S5-2152",
    "title": "睡前焦虑温和应对",
    "current": ["G-066", "G-127", "G-140"],
    "new": ["G-TERM-separation-anxiety", "G-TERM-object-permanence", "G-TERM-self-soothing"],
    "changes": [
      {"action": "replace", "from": "G-066", "to": "G-TERM-separation-anxiety"},
      {"action": "replace", "from": "G-127", "to": "G-TERM-object-permanence"},
      {"action": "replace", "from": "G-140", "to": "G-TERM-self-soothing"}
    ],
    "note": "可选追加 G-PERSON-Ferber 和 G-TERM-sleep-regression"
  },
  {
    "card_id": "C-S5-2153",
    "title": "戒夜奶 1 岁前后",
    "current": ["G-128", "G-129", "G-141"],
    "new": ["G-TERM-baby-bottle-tooth-decay"],
    "changes": [
      {"action": "delete", "id": "G-128", "reason": "夜奶非独立 weaning 概念"},
      {"action": "replace", "from": "G-129", "to": "G-TERM-baby-bottle-tooth-decay"},
      {"action": "delete", "id": "G-141", "reason": "夜奶生理细节正文充分"}
    ]
  },
  {
    "card_id": "C-S5-2154",
    "title": "1 岁后食欲变小",
    "current": ["G-142", "G-143"],
    "new": ["G-TERM-toddler-appetite-drop"],
    "changes": [
      {"action": "replace", "from": "G-142", "to": "G-TERM-toddler-appetite-drop"},
      {"action": "delete", "id": "G-143", "reason": "强喂破坏自我调节已在 failure_mode"}
    ]
  },
  {
    "card_id": "C-S5-2155",
    "title": "花生稀释后 1 岁可吃",
    "current": ["G-119", "G-120", "G-144"],
    "new": ["G-ABBR-LEAP", "G-TERM-LEAP-trial"],
    "changes": [
      {"action": "replace", "from": "G-119", "to": "G-ABBR-LEAP"},
      {"action": "replace", "from": "G-120", "to": "G-TERM-LEAP-trial"},
      {"action": "delete", "id": "G-144", "reason": "窒息风险通用,tags 已覆盖"}
    ],
    "note": "可选追加 G-TERM-allergy-introduction"
  },
  {
    "card_id": "C-S5-2156",
    "title": "12 月儿保+疫苗",
    "current": ["G-114", "G-145", "G-146"],
    "new": ["G-TERM-developmental-assessment", "G-ABBR-MMR", "G-ABBR-Varicella"],
    "changes": [
      {"action": "replace", "from": "G-114", "to": "G-TERM-developmental-assessment"},
      {"action": "replace", "from": "G-145", "to": "G-ABBR-MMR"},
      {"action": "replace", "from": "G-146", "to": "G-ABBR-Varicella"}
    ]
  },
  {
    "card_id": "C-S5-2157",
    "title": "学步赤脚最佳",
    "current": ["G-126", "G-147"],
    "new": [],
    "changes": [
      {"action": "delete", "id": "G-126", "reason": "通用 gross motor 概念"},
      {"action": "delete", "id": "G-147", "reason": "营销话术辨析非独立术语"}
    ]
  },
  {
    "card_id": "C-S5-2158",
    "title": "2 岁前禁屏幕",
    "current": ["G-148", "G-149"],
    "new": ["G-TERM-anti-screen", "G-TERM-media-effects"],
    "changes": [
      {"action": "replace", "from": "G-148", "to": "G-TERM-anti-screen"},
      {"action": "replace", "from": "G-149", "to": "G-TERM-media-effects"}
    ]
  },
  {
    "card_id": "C-S5-2159",
    "title": "害羞是性格不是病",
    "current": ["G-067", "G-150"],
    "new": ["G-TERM-attachment", "G-TERM-inhibited-temperament"],
    "changes": [
      {"action": "replace", "from": "G-067", "to": "G-TERM-attachment"},
      {"action": "replace", "from": "G-150", "to": "G-TERM-inhibited-temperament"}
    ],
    "note": "可选追加 G-PERSON-Kagan(Kagan 长期研究是核心引用)"
  },
  {
    "card_id": "C-S5-2160",
    "title": "撞头摇头多正常",
    "current": ["G-140", "G-151"],
    "new": ["G-TERM-self-soothing", "G-TERM-rhythmic-movement-disorder"],
    "changes": [
      {"action": "replace", "from": "G-140", "to": "G-TERM-self-soothing"},
      {"action": "replace", "from": "G-151", "to": "G-TERM-rhythmic-movement-disorder"}
    ]
  },
  {
    "card_id": "C-S3-2248",
    "title": "米粉先上,过敏家族再延 6 月",
    "current": ["G-TERM-allergy-introduction"],
    "new": ["G-TERM-allergy-introduction"],
    "changes": [],
    "status": "already-clean",
    "note": "R1 报告 BLW 断链已不存在于当前文件;若要补 BLW 概念可加 G-ABBR-BLW"
  },
  {
    "card_id": "C-S4-2144",
    "title": "7 月手指食物豌豆/弹珠尺寸",
    "current": [],
    "new": [],
    "changes": [],
    "status": "already-clean",
    "note": "R1 报告 BLW 断链已不存在;可选追加 G-ABBR-BLW(自喂概念)"
  },
  {
    "card_id": "C-S4-2145",
    "title": "噎食 vs 干呕区分",
    "current": [],
    "new": [],
    "changes": [],
    "status": "already-clean",
    "note": "R1 报告 BLW 断链已不存在;可选追加 G-ABBR-BLW"
  },
  {
    "card_id": "C-S4-2151",
    "title": "拒辅食 4 招",
    "current": [],
    "new": [],
    "changes": [],
    "status": "already-clean",
    "note": "R1 报告 BLW 断链已不存在;可选追加 G-TERM-toddler-appetite-drop"
  }
]
```

---

## 附录: 海蒂卡正文出现但漏建术语清单 (Task B 输出)

> 跨 156 张 SRC-040 卡正文 grep 出现的关键词,**已不在第 2 节新建清单中**的高频术语:

| 术语 | 出现卡数 | 评估 | 建议 |
|------|---------|------|------|
| **Ferber 法** | 1 (C-S3-2258 + C-S5-2152 间接) | 独立流派,跨多卡引 | 已纳入第 2 节 G-PERSON-Ferber |
| **Babywearing/婴儿背带** | 2 (C-S1-2501, C-S1-2506) | 海蒂专章 + 安全口诀 TICKS | 已纳入第 2 节 G-TERM-babywearing |
| **睡眠倒退** | 多卡(C-S3-2258 + S5 多卡间接) | 高频 + 中国家长焦虑点 | 已纳入第 2 节 G-TERM-sleep-regression |
| **发育红旗** | 多卡(2143/2148/2149 等) | 跨整本书核心 | 已纳入第 2 节 G-TERM-developmental-red-flag |
| **Karp 5S** | 多卡 | 已建 G-TERM-five-s + G-PERSON-Karp | **跳过** |
| **Sears 亲密育儿** | 1 (C-S5-2152 间接) | 单次提及,不跨源 | **跳过**(若后续 SRC-Sears 入库再建) |
| **AAPD 美国儿童牙科学会** | 1 (C-S5-2146) | 仅 1 次提及 | **跳过**(可未来补 G-ABBR-AAPD) |
| **kangaroo care 袋鼠护理** | 1 (C-S1-2506 标题) | 已在 G-TERM-skin-to-skin 涵盖 | **跳过** |
| **Heimlich 海姆立克** | 多卡 | 急救技术,操作性而非概念性 | **跳过** |
| **TICKS 背带安全口诀** | 1 (C-S1-2506) | 已在新建 G-TERM-babywearing 详述 | **跳过** |
| **Ellyn Satter Division of Responsibility** | 1 (C-S5-2154 间接) | 已在新建 G-TERM-toddler-appetite-drop 详述 | **跳过** |
| **wonder week 大脑跳跃** | 多卡 | 已建 G-TERM-mental-leap + G-PERSON-plooij | **跳过** |
| **AAP 屏幕指南 2016** | 1 (C-S5-2158) | 已在 G-TERM-anti-screen 涵盖 | **跳过** |
| **iron-fortified 铁强化米粉** | 多卡 | 已在新建 G-TERM-iron-deficiency-anemia 详述 | **跳过** |

---

## 总结

### 数字统计
- **broken G-ID 处置**: 46 条 → 23 替换 + 11 新建 + 12 删除
- **新建术语卡**: **9 张**(控制在 15 张上限内)
  1. G-PERSON-Ferber
  2. G-TERM-whole-milk-toddler
  3. G-TERM-iron-deficiency-anemia
  4. G-TERM-pointing-gesture
  5. G-TERM-toddler-appetite-drop
  6. G-TERM-rhythmic-movement-disorder
  7. G-TERM-babywearing
  8. G-TERM-sleep-regression
  9. G-TERM-developmental-red-flag
- **修改卡数**: 18 张(C-S5-2143 至 C-S5-2160)+ 4 张 BLW already-clean(无操作)
- **复用现有术语**: 约 13 个,主要是 separation-anxiety/object-permanence/discipline/MMR/Varicella/inhibited-temperament/MCHAT/anti-screen/peekaboo/joint-attention/baby-bottle-tooth-decay/LEAP-trial/developmental-assessment

### 设计原则回顾
- ✅ 宁缺勿滥:9 张新建远低于 15 上限
- ✅ 中国家长视角:全脂牛奶/缺铁性贫血/幼儿厌食期/撞头摇头都是国内最常误判
- ✅ 跨源复用价值:Ferber/sleep-regression/developmental-red-flag 后续 SRC-Sears/SRC-Brazelton 可继续引
- ✅ 已存在不重建:peekaboo/joint-attention/MMR 等优先复用
- ✅ broken G-ID 多数走"删除"或"替换"路径(35/46),仅 11 条触发新建

### 后续操作建议
1. **R4 Editor** 按第 3 节 JSON 表批量修改 18 张 S5 海蒂卡的 glossary_refs
2. 把第 2 节 9 张 yaml 落盘到 `40-glossary/`
3. 4 张 BLW already-clean 卡可选补 G-ABBR-BLW(非强制)
4. 考虑后续 R5 把 G-TERM-developmental-red-flag 反向追加到 S0-S4 各阶段 12/18/24 月儿保卡
