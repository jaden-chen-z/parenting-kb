// folder-asset.jsx
// 收藏夹素材：浅黄色纸质文件夹，开口朝左，夹着 5 张知识卡
// 固定在阶段页面顶部中央，点击进入 Favorites.html

(function () {
  const FOLDER_BG = '#EAD79A';
  const CARD_COLORS = ['#F5F4EE', '#EBE4D2', '#E8C5B4', '#CFD9C8', '#D8B4A0'];

  // 文件夹自然尺寸（设计 px）
  const W = 460, H = 600;
  const TAB_W = 42, TAB_H = 150, TAB_Y = 70;
  const R = 14, TR = 10;
  const xL = TAB_W, xR = W, yT = 0, yB = H;
  const tabL = 0, tabT = TAB_Y, tabB = TAB_Y + TAB_H;
  const earW = 36, earH = 28;
  const earX = xR - earW - 28;

  function folderBackPath() {
    return [
      `M ${xL + R} ${yT}`,
      `L ${xR - R} ${yT}`,
      `Q ${xR} ${yT} ${xR} ${yT + R}`,
      `L ${xR} ${yB - R}`,
      `Q ${xR} ${yB} ${xR - R} ${yB}`,
      `L ${earX + earW} ${yB}`,
      `Q ${earX + earW} ${yB + earH} ${earX + earW - 8} ${yB + earH}`,
      `L ${earX + 8} ${yB + earH}`,
      `Q ${earX} ${yB + earH} ${earX} ${yB}`,
      `L ${xL + R} ${yB}`,
      `Q ${xL} ${yB} ${xL} ${yB - R}`,
      `L ${xL} ${tabB + TR}`,
      `Q ${xL} ${tabB} ${xL - 6} ${tabB - 4}`,
      `L ${tabL + TR} ${tabB - 4}`,
      `Q ${tabL} ${tabB - 4} ${tabL} ${tabB - 4 - TR}`,
      `L ${tabL} ${tabT + TR}`,
      `Q ${tabL} ${tabT} ${tabL + TR} ${tabT}`,
      `L ${xL - 6} ${tabT + 4}`,
      `Q ${xL} ${tabT + 4} ${xL} ${tabT + 4 + TR}`,
      `L ${xL} ${yT + R}`,
      `Q ${xL} ${yT} ${xL + R} ${yT}`,
      `Z`,
    ].join(' ');
  }

  const FRONT_TOP = H * 0.45;
  function folderFrontPath() {
    return [
      `M ${xL} ${FRONT_TOP + 18}`,
      `C ${W * 0.35} ${FRONT_TOP - 18}, ${W * 0.7} ${FRONT_TOP - 8}, ${xR} ${FRONT_TOP + 6}`,
      `L ${xR} ${yB - R}`,
      `Q ${xR} ${yB} ${xR - R} ${yB}`,
      `L ${earX + earW} ${yB}`,
      `Q ${earX + earW} ${yB + earH} ${earX + earW - 8} ${yB + earH}`,
      `L ${earX + 8} ${yB + earH}`,
      `Q ${earX} ${yB + earH} ${earX} ${yB}`,
      `L ${xL + R} ${yB}`,
      `Q ${xL} ${yB} ${xL} ${yB - R}`,
      `Z`,
    ].join(' ');
  }

  const CARDS_LAYOUT = [
    { color: CARD_COLORS[0], cx: 175, cy: 110, w: 240, h: 320, rot: -16 },
    { color: CARD_COLORS[1], cx: 215, cy: 130, w: 240, h: 320, rot: -10 },
    { color: CARD_COLORS[3], cx: 200, cy: 170, w: 230, h: 310, rot: -6 },
    { color: CARD_COLORS[4], cx: 250, cy: 175, w: 230, h: 320, rot: -1 },
    { color: CARD_COLORS[2], cx: 195, cy: 210, w: 230, h: 320, rot: 4 },
  ];

  function FolderSVG({ instanceId = 'fa' }) {
    const back = folderBackPath();
    const front = folderFrontPath();
    const PAD = 30;
    const vbW = W + PAD * 2;
    const vbH = H + earH + PAD * 2;
    const vbX = -PAD;
    const vbY = -PAD;

    return (
      <svg viewBox={`${vbX} ${vbY} ${vbW} ${vbH}`} width="100%" height="100%"
           style={{ display: 'block', overflow: 'visible',
                    /* SVG viewport 矩形不接收事件,事件穿到内部 path/rect(默认 visiblePainted)
                       这样只有彩色形状才接收点击,周围透明区点不到 */
                    pointerEvents: 'none' }}>
        <defs>
          <filter id={`fg-${instanceId}`} x="0" y="0" width="100%" height="100%">
            <feTurbulence type="fractalNoise" baseFrequency="1.3" numOctaves="2" seed="11" />
            <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.42 0" />
          </filter>
          <filter id={`cg-${instanceId}`} x="0" y="0" width="100%" height="100%">
            <feTurbulence type="fractalNoise" baseFrequency="1.5" numOctaves="2" seed="3" />
            <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.35 0" />
          </filter>
          <linearGradient id={`fs-${instanceId}`} x1="0" y1="0" x2="1" y2="0.6">
            <stop offset="0" stopColor="rgba(0,0,0,0.18)" />
            <stop offset="0.4" stopColor="rgba(0,0,0,0)" />
          </linearGradient>
          <linearGradient id={`ffs-${instanceId}`} x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="rgba(0,0,0,0.18)" />
            <stop offset="0.6" stopColor="rgba(0,0,0,0)" />
          </linearGradient>
          {CARDS_LAYOUT.map((c, i) => (
            <linearGradient key={i} id={`cs-${instanceId}-${i}`} x1="0" y1="0" x2="0.4" y2="1">
              <stop offset="0" stopColor="rgba(0,0,0,0.12)" />
              <stop offset="0.5" stopColor="rgba(0,0,0,0)" />
            </linearGradient>
          ))}
          <clipPath id={`bc-${instanceId}`}><path d={back} /></clipPath>
          <clipPath id={`fc-${instanceId}`}><path d={front} /></clipPath>
        </defs>

        <ellipse cx={W / 2 + 10} cy={H + earH + 14} rx={W * 0.42} ry={14}
                 fill="rgba(0,0,0,0.32)" opacity="0.5" />

        <path d={back} fill={FOLDER_BG} />
        <g clipPath={`url(#bc-${instanceId})`}>
          <rect x={xL} y={yT} width={W - xL} height={H} fill={`url(#fs-${instanceId})`} />
          <rect x={vbX} y={vbY} width={vbW} height={vbH}
                filter={`url(#fg-${instanceId})`} opacity="0.55"
                style={{ mixBlendMode: 'multiply' }} />
          <line x1={xL} y1={tabT + 2} x2={xL} y2={tabB - 2}
                stroke="rgba(60,40,18,0.22)" strokeWidth="1" />
        </g>
        <path d={back} fill="none" stroke="rgba(60,40,18,0.18)" strokeWidth="1" />

        {CARDS_LAYOUT.map((c, i) => {
          const x = c.cx - c.w / 2;
          const y = c.cy - c.h / 2;
          return (
            <g key={i} transform={`rotate(${c.rot} ${c.cx} ${c.cy}) translate(${x} ${y})`}>
              <rect width={c.w} height={c.h} rx="6" ry="6" fill={c.color} />
              <rect width={c.w} height={c.h} rx="6" ry="6"
                    fill={`url(#cs-${instanceId}-${i})`} opacity="0.7" />
              <rect width={c.w} height={c.h} rx="6" ry="6" fill="black"
                    filter={`url(#cg-${instanceId})`} opacity="0.18"
                    style={{ mixBlendMode: 'multiply' }} />
              <rect width={c.w} height={c.h} rx="6" ry="6" fill="none"
                    stroke="rgba(60,40,20,0.18)" strokeWidth="1" />
            </g>
          );
        })}

        <path d={front} fill={FOLDER_BG} />
        <g clipPath={`url(#fc-${instanceId})`}>
          <rect x={xL} y={FRONT_TOP - 30} width={W - xL} height={H}
                fill={`url(#ffs-${instanceId})`} opacity="0.5" />
          <rect x={vbX} y={vbY} width={vbW} height={vbH}
                filter={`url(#fg-${instanceId})`} opacity="0.55"
                style={{ mixBlendMode: 'multiply' }} />
        </g>
        <path d={`M ${xL} ${FRONT_TOP + 18}
                 C ${W * 0.35} ${FRONT_TOP - 18}, ${W * 0.7} ${FRONT_TOP - 8}, ${xR} ${FRONT_TOP + 6}`}
              fill="none" stroke="rgba(60,40,18,0.32)" strokeWidth="1.4" />
        <path d={front} fill="none" stroke="rgba(60,40,18,0.22)" strokeWidth="1" />
      </svg>
    );
  }

  // 收藏夹素材：位置 / 大小 / 旋转可通过 props 调整（Tweaks 控制）
  function FolderAsset({ left = 50, top = 30, width = 240, rot = 8 } = {}) {
    // 保持文件夹宽高比（自然 ~520x680 → 容器宽: 高 ≈ 1 : 1.31）
    const height = Math.round(width * 0.83);
    return (
      <button
        onClick={() => { location.href = 'Favorites.html'; }}
        aria-label="打开收藏夹"
        style={{
          all: 'unset',
          position: 'absolute',
          left: `${left}%`,
          top: top,
          width: width,
          height: height,
          marginLeft: -width / 2,
          transform: `rotate(${rot}deg)`,
          transformOrigin: 'center center',
          cursor: 'pointer',
          zIndex: 50,
          filter: 'drop-shadow(0 8px 14px rgba(60,40,20,0.28))',
          /* button 自己不接收事件 — 让 hit test 落到内部 SVG 的 path/rect 上(visiblePainted),
             这样按钮的矩形透明区点不到,只有彩色文件夹 + 卡片形状才能触发 onClick。
             事件从 path/rect 冒泡到 button 仍会触发 React onClick(pointer-events 不影响冒泡) */
          pointerEvents: 'none',
        }}
      >
        <FolderSVG instanceId="fav" />
      </button>
    );
  }

  window.FolderAsset = FolderAsset;
  window.FolderSVG = FolderSVG;
})();
