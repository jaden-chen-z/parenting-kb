const stage = document.querySelector("#scrollStage");
const device = document.querySelector("#device");
const typedText = document.querySelector("#typedText");

const cardText = `头 3 个月是"第四产程"

他其实早产了 3 个月。

为什么重要:
第四产程 = 出生后头 3 月仍是孕期延续, 属于"子宫外适应期"。

这解释了为什么新生儿需要类子宫刺激: 温暖、紧裹、响动、摇晃。

你可以做:
01 把"新生儿"看成"还没出生足月的人"
02 主动给他造一个像子宫的环境
03 3 月内的手抖、惊跳通常会自动消失
04 他"难带"不等于有问题, 3 月后再评估

常见误区:
用 6 月大宝宝的标准看新生儿, 会把正常适应期误读成"有问题"。

证据等级: C
来源: Harvey Karp`;

let latestProgress = -1;
let lastVisibleCount = -1;
let strikeTimer = 0;
let ticking = false;

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function easeOutCubic(value) {
  return 1 - Math.pow(1 - value, 3);
}

function setStrike() {
  window.clearTimeout(strikeTimer);
  device.classList.remove("is-striking");
  void device.offsetWidth;
  device.classList.add("is-striking");
  strikeTimer = window.setTimeout(() => {
    device.classList.remove("is-striking");
  }, 62);
}

function update() {
  ticking = false;

  const maxScroll = stage.offsetHeight - window.innerHeight;
  const progress = maxScroll > 0 ? clamp(-stage.getBoundingClientRect().top / maxScroll, 0, 1) : 1;

  if (Math.abs(progress - latestProgress) < 0.001) {
    return;
  }

  latestProgress = progress;

  const paperProgress = easeOutCubic(clamp(progress * 1.08, 0, 1));
  const typedProgress = clamp((progress - 0.035) / 0.9, 0, 1);
  const visibleCount = Math.floor(cardText.length * typedProgress);
  const lineColumn = visibleCount % 24;
  const lineBounce = Math.floor(visibleCount / 24) % 2;
  const headX = 13 + lineColumn * 2.7 + lineBounce * 0.7;

  document.documentElement.style.setProperty("--paper-y", `${-42 * paperProgress}%`);
  document.documentElement.style.setProperty("--paper-roll", `${(progress - 0.5) * 0.7}deg`);
  document.documentElement.style.setProperty("--head-x", `${clamp(headX, 12, 82)}%`);

  if (visibleCount !== lastVisibleCount) {
    typedText.textContent = cardText.slice(0, visibleCount);
    if (visibleCount > lastVisibleCount && visibleCount > 0) {
      setStrike();
    }
    lastVisibleCount = visibleCount;
  }
}

function requestUpdate() {
  if (!ticking) {
    ticking = true;
    window.requestAnimationFrame(update);
  }
}

window.addEventListener("scroll", requestUpdate, { passive: true });
window.addEventListener("resize", requestUpdate);
window.addEventListener("load", requestUpdate);
requestUpdate();
