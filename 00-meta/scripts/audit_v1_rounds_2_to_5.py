"""Phase E Rounds 2-5: chapter coverage + glossary + hook style + cross-school rate + structure"""
import os, glob, yaml, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'
GLOSS = '/Users/jjjjadennnn/Desktop/parenting-kb/40-glossary'

# Find all V1 cards
v1_cards = []
for seg in os.listdir(BASE):
    seg_path = os.path.join(BASE, seg)
    if not os.path.isdir(seg_path): continue
    for path in glob.glob(f'{seg_path}/C-*.yaml'):
        with open(path) as f:
            content = f.read()
        if 'SRC-030' in content:
            v1_cards.append(path)

print(f"=== Phase E Rounds 2-5 Audit ===")
print(f"Total V1 cards: {len(v1_cards)}")

# === Round 2: Chapter Coverage ===
print(f"\n=== Round 2: Chapter Coverage (17 chapters) ===")
chapter_hits = {f'Ch {i}': 0 for i in range(1, 18)}
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    chapter_str = d.get('citation', {}).get('chapter', '')
    # Extract chapter number(s)
    matches = re.findall(r'Ch\s*(\d+)', chapter_str)
    for m in matches:
        chapter_hits[f'Ch {m}'] = chapter_hits.get(f'Ch {m}', 0) + 1

for ch, hits in sorted(chapter_hits.items(), key=lambda x: int(x[0].split()[1])):
    status = '✓' if hits > 0 else '✗ MISSING'
    print(f"  {ch}: {hits} cards {status}")

uncovered = [ch for ch, h in chapter_hits.items() if h == 0]
print(f"\nUncovered chapters: {len(uncovered)} - {uncovered}")

# === Round 3: Glossary Coverage ===
print(f"\n=== Round 3: Key Theorist + Framework Coverage ===")
required_persons = [
    'Overton', 'Cairns-R', 'Valsiner', 'Gottlieb', 'Lickliter', 'Wahlsten',
    'Thelen', 'Smith-LB', 'Fischer-K', 'Magnusson', 'Stattin',
    'Csikszentmihalyi', 'Rathunde', 'Brandtstadter',
    'Baltes', 'Lindenberger', 'Staudinger', 'Elder', 'Shanahan',
    'Shweder', 'Markus', 'Miller', 'Goodnow', 'Hatano', 'LeVine',
    'Morris', 'Spencer', 'Benson', 'Scales', 'Hamilton', 'Sesma',
    'Oser', 'Scarlett', 'Bucher', 'Werner-H', 'Wapner',
    'Cole-M', 'Rogoff', 'Riegel', 'Cairns-B',
]
missing_persons = []
for p in required_persons:
    if not os.path.exists(f'{GLOSS}/G-PERSON-{p}.yaml'):
        missing_persons.append(p)
print(f"Required theorists: {len(required_persons)}")
print(f"Missing: {len(missing_persons)} - {missing_persons}")

required_terms = [
    'split-metatheory', 'relational-metatheory', 'cartesian-dualism',
    'relational-developmental-systems', 'developmental-science',
    'probabilistic-epigenesis', 'canalization', 'anti-genetic-determinism',
    'anti-determinism', 'anti-reductionism',
    'dynamic-systems-theory', 'self-organization', 'emergence', 'attractors',
    'variability-as-signal',
    'dynamic-skill-theory', 'constructive-web', 'skill-reorganization',
    'holistic-person', 'person-oriented-approach', 'individual-pathway',
    'flow-theory', 'intrinsic-motivation', 'autotelic-personality',
    'action-theory', 'assimilation-accommodation', 'intentional-self-development',
    'lifespan-theory', 'plasticity', 'SOC-model', 'wisdom-paradigm',
    'critical-period', 'sensitive-period',
    'life-course-theory', 'linked-lives', 'timing-principle',
    'bioecological-model', 'microsystem', 'mesosystem', 'exosystem',
    'macrosystem', 'chronosystem', 'PPCT-model', 'proximal-processes',
    'PVEST', 'identity-formation', 'racism-in-development',
    'positive-youth-development', '5C-framework', 'asset-based-model',
    'cultural-psychology', 'multiple-mentalities', 'constitutive-culture',
    'cultural-construction',
    'orthogenetic-principle', 'three-grand-systems',
    'continuity-discontinuity', 'nature-vs-nurture', 'systems-thinking',
    'religious-spiritual-development',
]
missing_terms = []
for t in required_terms:
    if not os.path.exists(f'{GLOSS}/G-TERM-{t}.yaml'):
        missing_terms.append(t)
print(f"Required frameworks: {len(required_terms)}")
print(f"Missing: {len(missing_terms)} - {missing_terms}")

# === Round 4: Hook Style ===
print(f"\n=== Round 4: Hook Style ===")
descriptive_keywords = ['是什么', '说明', '介绍', '概念', '定义', '解释', '描述', '阐述']
desc_hooks = []
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    cid = d.get('card_id', '')
    hook = d.get('front', {}).get('hook', '')
    for kw in descriptive_keywords:
        if kw in hook:
            desc_hooks.append((cid, hook, kw))
            break

print(f"Descriptive hooks: {len(desc_hooks)}")
for cid, hook, kw in desc_hooks[:5]:
    print(f"  {cid}: '{hook}' (matched: {kw})")

# === Round 4 (b): Cross-school rate ===
print(f"\n=== Round 4 (b): Cross-school Rate ===")
# Improved: any card NOT V1 (not citing SRC-030) is cross-school
all_v1_ids = set()
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    all_v1_ids.add(d.get('card_id', ''))

cross_school_count = 0
total_related = 0
no_cross_v2 = []  # Cards with NO related outside V1
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    cid = d.get('card_id', '')
    related = d.get('related_cards', [])
    has_cross = False
    for r in related:
        total_related += 1
        if r not in all_v1_ids:
            cross_school_count += 1
            has_cross = True
    if not has_cross:
        no_cross_v2.append(cid)

print(f"Total related links: {total_related}")
print(f"Cross-school links: {cross_school_count} ({100*cross_school_count/max(total_related, 1):.1f}%)")
print(f"Avg related/card: {total_related/len(v1_cards):.2f}")
print(f"Cards with 0 cross-school: {len(no_cross_v2)}")
if no_cross_v2:
    for cid in no_cross_v2[:10]:
        print(f"  {cid}")

# === Round 5: Structural Audit ===
print(f"\n=== Round 5: Structural Soundness ===")
structure_issues = []
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    cid = d.get('card_id', '')

    # Required fields
    if not d.get('front', {}).get('title'):
        structure_issues.append((cid, 'missing title'))
    if not d.get('front', {}).get('hook'):
        structure_issues.append((cid, 'missing hook'))
    if not d.get('back', {}).get('why_matters'):
        structure_issues.append((cid, 'missing why_matters'))

    wtd = d.get('back', {}).get('what_to_do', [])
    if len(wtd) < 3 or len(wtd) > 5:
        structure_issues.append((cid, f'wtd count {len(wtd)} (need 3-5)'))

    if not d.get('back', {}).get('failure_mode'):
        structure_issues.append((cid, 'missing failure_mode'))

    if not d.get('back', {}).get('evidence_level'):
        structure_issues.append((cid, 'missing evidence_level'))

    refs = d.get('glossary_refs', [])
    if len(refs) == 0:
        structure_issues.append((cid, 'no glossary_refs'))

    related = d.get('related_cards', [])
    if len(related) < 2:
        structure_issues.append((cid, f'only {len(related)} related'))

    if not d.get('citation', {}).get('source_id'):
        structure_issues.append((cid, 'missing citation source_id'))

print(f"Structural issues: {len(structure_issues)}")
for cid, issue in structure_issues[:10]:
    print(f"  {cid}: {issue}")

# === evidence_level distribution ===
print(f"\n=== evidence_level Distribution ===")
ev_count = {'A': 0, 'B': 0, 'C': 0}
for path in v1_cards:
    with open(path) as f:
        d = yaml.safe_load(f)
    ev = d.get('back', {}).get('evidence_level', '')
    ev_count[ev] = ev_count.get(ev, 0) + 1
total = sum(ev_count.values())
for lvl, cnt in ev_count.items():
    print(f"  {lvl}: {cnt} ({100*cnt/max(total,1):.0f}%)")
