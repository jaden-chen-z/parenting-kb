// folders.jsx — 阶段文件夹分类页
// 9 个文件夹（S0–S8）层叠堆放,纸质质感
// (2026-05-04 更新:从 8 段 0-2yr 扩到 9 段 0-6yr,对接真实知识卡 yaml 段命名)

// 文件夹用月龄命名 + 中文关键词副标题
// id 必须对应 yaml 卡片的 stages[0] 值(S0..S8),URL `?stage=S1` 即用此 id
const STAGES = [
  { id: 'S0', tabLabel: '-9～0 月', name: '孕期',       en: 'PRENATAL',       count: 0 },
  { id: 'S1', tabLabel: '0～1 月',  name: '新生',       en: 'NEWBORN',        count: 0 },
  { id: 'S2', tabLabel: '1～3 月',  name: '社交萌芽',   en: 'SOCIAL BUD',     count: 0 },
  { id: 'S3', tabLabel: '3～6 月',  name: '感知翻身',   en: 'SENSE · ROLL',   count: 0 },
  { id: 'S4', tabLabel: '6～9 月',  name: '探索坐立',   en: 'EXPLORE · SIT',  count: 0 },
  { id: 'S5', tabLabel: '9～12 月', name: '爬行站立',   en: 'CRAWL · STAND',  count: 0 },
  { id: 'S6', tabLabel: '1～2 岁',  name: '行走说话',   en: 'WALK · WORDS',   count: 0 },
  { id: 'S7', tabLabel: '2～3 岁',  name: '自我表达',   en: 'SELF · EXPRESS', count: 0 },
  { id: 'S8', tabLabel: '3～6 岁',  name: '早童',       en: 'EARLY CHILD',    count: 0 },
];

// 异步加载段计数(cards.json 的 stages 字段)
// 缓存破坏:?t=<时间戳> + cache: no-store(防 iOS Safari 永久缓存,与 cards.jsx 同步)
function useStageCounts() {
  const [counts, setCounts] = React.useState({});
  React.useEffect(() => {
    fetch('cards.json?t=' + Date.now(), { cache: 'no-store' })
      .then((r) => r.ok ? r.json() : null)
      .then((j) => {
        if (!j || !j.stages) return;
        const m = {};
        j.stages.forEach((s) => { m[s.id] = s.count; });
        setCounts(m);
      })
      .catch(() => {});
  }, []);
  return counts;
}

// ── 配色：参考图的暖纸感 + 扩展两层
// 参考图自上而下：珊瑚粉 / 玫瑰粉 / 米白 / 浅棕 / 深红
// 扩展加入：暖灰、苔棕、墨蓝（保持低饱和、纸感）
const PALETTES = {
  warm: [
    { tab: '#F1B5A6', body: '#EFB1A1', edge: '#D89887', ink: '#5a2a20' }, // S0 珊瑚粉
    { tab: '#E2A6A8', body: '#DFA1A3', edge: '#B98184', ink: '#5a2226' }, // S1 玫瑰粉
    { tab: '#E8E1D2', body: '#E5DECE', edge: '#C7BFAD', ink: '#3d3a2e' }, // S2 米白
    { tab: '#D9A57A', body: '#D6A176', edge: '#B68559', ink: '#4a2d12' }, // S3 浅棕
    { tab: '#7A2A2A', body: '#732626', edge: '#561818', ink: '#f4dcd0' }, // S4 深红
    { tab: '#B8A38A', body: '#B49E84', edge: '#937e64', ink: '#3a2d1e' }, // S5 暖灰棕
    { tab: '#8C9B7A', body: '#879675', edge: '#69785a', ink: '#1f2a16' }, // S6 苔绿
    { tab: '#3F4A5C', body: '#3B4658', edge: '#262f3c', ink: '#dfe4ee' }, // S7 墨蓝
    { tab: '#5C3A52', body: '#583752', edge: '#3A2236', ink: '#e8d5e0' }, // S8 深紫(早童)
  ],
  cool: [
    { tab: '#cbd9e6', body: '#c6d4e2', edge: '#9eb1c5', ink: '#1d2a3a' },
    { tab: '#b9c8d8', body: '#b3c2d3', edge: '#8a9db2', ink: '#1d2a3a' },
    { tab: '#e8e4dc', body: '#e3dfd6', edge: '#bfb9ad', ink: '#2c2a22' },
    { tab: '#9bb3c4', body: '#94adbf', edge: '#6f8a9d', ink: '#0f2230' },
    { tab: '#3a5972', body: '#34516a', edge: '#1f3849', ink: '#dfe9f2' },
    { tab: '#7d97a8', body: '#7791a3', edge: '#56738a', ink: '#0f2230' },
    { tab: '#5a7c80', body: '#547578', edge: '#385559', ink: '#e2eded' },
    { tab: '#26384a', body: '#22344a', edge: '#0f1c2c', ink: '#cfd9e6' },
    { tab: '#152030', body: '#121d2c', edge: '#06101a', ink: '#cfd9e6' }, // S8 最深
  ],
  mono: [
    { tab: '#ECE9E2', body: '#E8E5DD', edge: '#C9C5BB', ink: '#2a2926' },
    { tab: '#D9D5CB', body: '#D5D1C7', edge: '#B5B1A7', ink: '#2a2926' },
    { tab: '#C2BCAE', body: '#BEB8AA', edge: '#9b9686', ink: '#2a2926' },
    { tab: '#A39C8B', body: '#9F9887', edge: '#7d7765', ink: '#f3f1ea' },
    { tab: '#857D6B', body: '#817968', edge: '#605a4c', ink: '#f3f1ea' },
    { tab: '#665F50', body: '#625b4c', edge: '#443f34', ink: '#f3f1ea' },
    { tab: '#46402F', body: '#423d2c', edge: '#2c281c', ink: '#f3f1ea' },
    { tab: '#2A271D', body: '#26241b', edge: '#15140e', ink: '#efeadd' },
    { tab: '#15130C', body: '#121008', edge: '#080704', ink: '#efeadd' }, // S8 最深
  ],
};

// ── 单个纸质文件夹的 SVG 视觉(纯展示,不管位置/手势)
// 位置/拖拽/吸附/飞出 由 SwipeStack 接管,这里只画 SVG path + 阴影 + 纹理 + 文字
function PaperFolderSVG({ stage, palette, layout, idx, expanded, isExpanded, textureLevel }) {

  const W = 360;            // 文件夹宽度(原始尺寸 — 给两侧阴影 16px 呼吸空间)
  const TAB_H = 44;
  const BODY_H = 240;
  const R = 18;             // 圆角
  const TAB_R = 14;
  const TAB_W = 150;

  // tab 横向位置(按 layout)— 永远用 idx 决定 slot,不随 expanded 状态重算,
  // 这样某个文件夹展开/收起时,其他文件夹的 tab 左右位置保持不变
  const slotCount = layout === 'stagger' ? 4 : 2;
  const slot = idx % slotCount;
  let tabX;
  if (layout === 'stagger') {
    // 4 个槽位平均分布
    const margin = 22;
    const usable = W - margin * 2 - TAB_W;
    tabX = margin + (usable / (slotCount - 1)) * slot;
  } else {
    // alternate：左右交替
    tabX = slot === 0 ? 28 : W - TAB_W - 28;
  }

  // 文件夹外形 path
  const x0 = 0, y0 = TAB_H, x1 = W, y1 = TAB_H + BODY_H;
  const tx0 = tabX, tx1 = tabX + TAB_W;
  const path = [
    `M ${x0} ${y1 - R}`,
    `L ${x0} ${y0 + R}`,
    `Q ${x0} ${y0} ${x0 + R} ${y0}`,
    `L ${tx0 - TAB_R} ${y0}`,
    `Q ${tx0} ${y0} ${tx0 + 8} ${y0 - 10}`,
    `L ${tx0 + 14} ${TAB_R}`,
    `Q ${tx0 + 14} 0 ${tx0 + 14 + TAB_R} 0`,
    `L ${tx1 - TAB_R - 14} 0`,
    `Q ${tx1 - 14} 0 ${tx1 - 14} ${TAB_R}`,
    `L ${tx1 - 8} ${y0 - 10}`,
    `Q ${tx1} ${y0} ${tx1 + TAB_R} ${y0}`,
    `L ${x1 - R} ${y0}`,
    `Q ${x1} ${y0} ${x1} ${y0 + R}`,
    `L ${x1} ${y1 - R}`,
    `Q ${x1} ${y1} ${x1 - R} ${y1}`,
    `L ${x0 + R} ${y1}`,
    `Q ${x0} ${y1} ${x0} ${y1 - R}`,
    `Z`,
  ].join(' ');

  const filterId = `paper-${stage.id}`;
  const textureOpacity = textureLevel === 'off' ? 0 : textureLevel === 'subtle' ? 0.18 : 0.35;
  const grainFreq = textureLevel === 'heavy' ? 1.4 : 0.85;

  return (
    <div
      className="folder"
      data-screen-label={`${stage.id} ${stage.name}`}
      style={{
        width: W,
        margin: '0 auto',           // wrapper 满宽,SVG 居中
      }}
    >
      <svg
        viewBox={`0 0 ${W} ${TAB_H + BODY_H + 6 + 30}`}
        width={W}
        height={TAB_H + BODY_H + 6 + 30}
        style={{
          display: 'block',
          overflow: 'visible',
        }}
      >
        <defs>
          <filter id={filterId} x="0" y="0" width="100%" height="100%">
            <feTurbulence type="fractalNoise" baseFrequency={grainFreq} numOctaves="2" seed={idx * 7 + 3} />
            <feColorMatrix values={`0 0 0 0 0
                                    0 0 0 0 0
                                    0 0 0 0 0
                                    0 0 0 ${textureOpacity} 0`} />
            <feComposite in2="SourceGraphic" operator="in" />
          </filter>
          {/* 投影 filter:横向软阴影过渡区扩到 ±20px,阴影羽化 stdDev=6,有 3D 立体感 */}
          <filter id={`drop-${stage.id}`}
            filterUnits="userSpaceOnUse"
            x="-20"
            y="0"
            width={W + 40}
            height={TAB_H + BODY_H + 6 + 30}
          >
            <feDropShadow dx="0" dy="7" stdDeviation="6 10"
              floodColor="black" floodOpacity="0.20" />
          </filter>
          <linearGradient id={`sh-${stage.id}`} x1="0" x2="0" y1="0" y2="1">
            <stop offset="0" stopColor="rgba(0,0,0,0.18)" />
            <stop offset="1" stopColor="rgba(0,0,0,0)" />
          </linearGradient>
          <clipPath id={`clip-${stage.id}`}>
            <path d={path} />
          </clipPath>
        </defs>

        {/* 主体(套上 drop filter — 阴影只往下/不往两侧) */}
        <path d={path} fill={palette.body} filter={`url(#drop-${stage.id})`} />
        {/* 顶部高光 */}
        <path d={path} fill={`url(#sh-${stage.id})`} opacity="0.35" />
        {/* 下方暗边 */}
        <path d={path} fill={palette.edge} opacity="0.18"
              transform="translate(0,2)" style={{ mixBlendMode: 'multiply' }} />
        {/* 纸质纹理叠加 */}
        <path d={path} fill="#000" filter={`url(#${filterId})`} />

        {/* tab 上的月龄文字 */}
        <text
          x={tabX + TAB_W / 2}
          y={TAB_H - 14}
          textAnchor="middle"
          fontFamily="'Noto Serif SC', 'Source Han Serif SC', Georgia, serif"
          fontSize="17"
          fontWeight="600"
          letterSpacing="0.06em"
          fill={palette.ink}
          opacity="0.88"
        >
          {stage.tabLabel}
        </text>

        {/* 折叠态：tab 旁的小字已去掉，保持简洁 */}

        {/* 主体内容:段名 / 月龄 / 卡片数 — 仅展开时显示。
            opacity 0/1 + transition 通过 CSS class .folder-expand-content + .is-shown
            控制(CSS 见 Stage Folders.html)。inline style 路线在 SVG <g> 上 transition
            可能被 React re-render 频繁干扰,CSS class 更稳定。 */}
        <g className={`folder-expand-content${isExpanded ? ' is-shown' : ''}`}
           style={{ pointerEvents: isExpanded ? 'auto' : 'none' }}>
          <text x="32" y={TAB_H + 60}
                fontFamily="'Noto Serif SC', 'Source Han Serif SC', Georgia, serif"
                fontSize="34" fontWeight="600" fill={palette.ink} letterSpacing="0.02em">
            {stage.name}
          </text>
          <text x="32" y={TAB_H + 88}
                fontFamily="ui-monospace, 'SF Mono', Menlo, monospace"
                fontSize="11" fill={palette.ink} opacity="0.5" letterSpacing="0.16em">
            {stage.en}
          </text>

          {/* 右下角:阅读进度 — 没看过显示 "X CARDS",看过显示 "已读 N / X"
              重置进度按钮在 Cards 页面右上角(看到进度的语境里),不在这 */}
          <text x={W - 32} y={TAB_H + BODY_H - 28} textAnchor="end"
                fontFamily="ui-monospace, 'SF Mono', Menlo, monospace"
                fontSize="11" fill={palette.ink}
                opacity={stage.seen > 0 ? 0.55 : 0.5}
                letterSpacing="0.1em">
            {stage.seen > 0 ? `已读 ${stage.seen} / ${stage.count}` : `${stage.count} CARDS`}
          </text>
        </g>
      </svg>
    </div>
  );
}

function FoldersPage() {
  const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
    "layout": "alternate",
    "texture": "subtle",
    "palette": "warm",
    "bg": "#ece5d4",
    "favLeft": 68,
    "favTop": -268,
    "favWidth": 416,
    "favRot": -160
  }/*EDITMODE-END*/;

  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);
  const palette = PALETTES[t.palette] || PALETTES.warm;

  // 从 cards.json 异步取段计数,merge 到 STAGES
  const counts = useStageCounts();
  // 当前用户的阅读进度 — 从 server API 拉取(本地 admin_server.py / 云端 KV 都行)
  // mount 一次,展示"已读 N / 总数";重置在 Cards 页,回本页时新加载
  const [progressMap, setProgressMap] = React.useState({});
  React.useEffect(() => {
    const email = window.PKB && PKB.auth.currentUser();
    if (!email || !window.PKB || !PKB.api) return;
    const localProgress = PKB.auth.readJSON('progress', {});
    PKB.api.getProgress(email)
      .then((j) => {
        const next = j.progress && typeof j.progress === 'object' && !Array.isArray(j.progress) ? j.progress : localProgress;
        setProgressMap(next);
        PKB.auth.writeJSON('progress', next);
      })
      .catch(() => setProgressMap(localProgress));
  }, []);
  // seen = 该段已读卡数(进度 idx + 1,0 表示没看过)
  // useMemo 稳定 stage 引用,否则每次 re-render 新对象 → 扰乱 opacity transition
  const stagesWithCounts = React.useMemo(
    () => STAGES.map((s) => {
      const savedIdx = progressMap[`stage:${s.id}`];
      const seen = (typeof savedIdx === 'number' && savedIdx >= 0) ? savedIdx + 1 : 0;
      return { ...s, count: counts[s.id] || 0, seen };
    }),
    [counts, progressMap]
  );

  return (
    <div style={{
      height: '100%',
      background: `radial-gradient(180% 140% at 50% 10%, #f6f1e6 0%, ${t.bg} 100%)`,
      fontFamily: "ui-sans-serif, -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif",
      color: '#2a2926',
      overflow: 'hidden',
      display: 'flex',
      flexDirection: 'column',
      position: 'relative',   // 让收藏夹素材锚点 wrapper 能 absolute 定位
    }}>
      {/* 顶部条:头像(邮箱大写首字母)+ 登出 */}
      <div style={{
        position: 'absolute', top: 0, left: 0, right: 0,
        padding: '14px 22px',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        zIndex: 60,
        pointerEvents: 'none',          // 子元素自己开 pointer-events
      }}>
        {/* 头像:圆 + 邮箱首字母大写 */}
        <span style={{
          pointerEvents: 'auto',
          display: 'inline-flex',
          alignItems: 'center', justifyContent: 'center',
          width: 32, height: 32,
          borderRadius: '50%',
          background: 'rgba(122,42,42,0.12)',
          color: '#7A2A2A',
          fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
          fontSize: 15,
          fontWeight: 600,
          letterSpacing: 0,
          userSelect: 'none',
        }}>{(((window.PKB && PKB.auth.currentUser()) || '?').charAt(0) || '?').toUpperCase()}</span>
        <button
          onClick={() => { PKB.auth.logout(); location.replace('/'); }}
          style={{
            all: 'unset', cursor: 'pointer',
            pointerEvents: 'auto',
            fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
            fontSize: 11, letterSpacing: '0.16em',
            color: '#7A2A2A',
          }}
        >登出</button>
      </div>

      {/* 顶部留白(为顶部收藏夹素材让位) */}
      <div style={{ height: 130, flexShrink: 0 }} />

      {/* 文件夹堆 — SwipeStack 接管位置/拖拽/吸附/飞出,PaperFolderSVG 只画外形 */}
      {/* itemHeight=62 = TAB_H 44 + 18 露出条; expandedHeight=308 = TAB_H 44 + BODY_H 240 + 24 缓冲 */}
      <SwipeStack
        items={stagesWithCounts}
        itemHeight={62}
        expandedHeight={308}
        enableHorizontalEnter={true}
        onEnter={(stage) => {
          // 全部 9 段都跳到 Cards.html?stage=<S0..S8>(cards.jsx 按段过滤)
          location.href = `Cards.html?stage=${encodeURIComponent(stage.id)}`;
        }}
        style={{
          margin: '0 auto',
          width: '100%',          // 强制撑到父级宽度,再被 maxWidth 截到 420
          maxWidth: 420,
          flexShrink: 0,
        }}
        renderItem={({ item: stage, idx, expanded: exp, isExpanded }) => (
          <PaperFolderSVG
            stage={stage}
            palette={palette[idx]}
            layout={t.layout}
            textureLevel={t.texture}
            idx={idx}
            expanded={exp}
            isExpanded={isExpanded}
          />
        )}
      />

      {/* 收藏夹素材锚点 wrapper: 跟 folder stack 同 maxWidth 居中,让 favLeft% 在手机/电脑下相对卡片中心位置一致 */}
      {/* z-index 必须高于 SwipeStackItem(100+ idx) — 否则文件夹堆遮挡收藏夹素材的 hit test */}
      <div style={{
        position: 'absolute',
        top: 0,
        left: '50%',
        transform: 'translateX(-50%)',
        width: '100%',
        maxWidth: 420,
        height: 0,
        zIndex: 200,
      }}>
        {/* 收藏夹素材:位置 / 大小 / 旋转 可在 Tweaks 中调 */}
        <FolderAsset left={t.favLeft} top={t.favTop} width={t.favWidth} rot={t.favRot} />
      </div>

      {/* Tweaks */}
      <TweaksPanel>
        <TweakSection label="Layout" />
        <TweakRadio label="Tab 位置" value={t.layout}
          options={['alternate', 'stagger']}
          onChange={(v) => setTweak('layout', v)} />
        <TweakSection label="Paper" />
        <TweakRadio label="纸质纹理" value={t.texture}
          options={['off', 'subtle', 'heavy']}
          onChange={(v) => setTweak('texture', v)} />
        <TweakSection label="Color" />
        <TweakRadio label="配色" value={t.palette}
          options={['warm', 'cool', 'mono']}
          onChange={(v) => setTweak('palette', v)} />
        <TweakColor label="背景" value={t.bg}
          onChange={(v) => setTweak('bg', v)} />
        <TweakSection label="Favorites 收藏夹" />
        <TweakSlider label="水平位置 %" value={t.favLeft} min={0} max={100} step={1} unit="%"
          onChange={(v) => setTweak('favLeft', v)} />
        <TweakSlider label="顶部偏移" value={t.favTop} min={-300} max={400} step={2} unit="px"
          onChange={(v) => setTweak('favTop', v)} />
        <TweakSlider label="大小" value={t.favWidth} min={60} max={1200} step={4} unit="px"
          onChange={(v) => setTweak('favWidth', v)} />
        <TweakSlider label="旋转" value={t.favRot} min={-180} max={180} step={1} unit="°"
          onChange={(v) => setTweak('favRot', v)} />
      </TweaksPanel>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<FoldersPage />);
