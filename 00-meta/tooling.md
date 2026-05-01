# 工具栈 · parenting-kb

> Phase 0 末尾安装,Phase 1 起使用。
> 安装日期:2026-04-30

## 已装工具

### 🍺 Homebrew(系统级,共享)

| 工具 | 用途 |
|---|---|
| `pandoc` 3.9 | 万能格式转换(EPUB↔MD↔HTML 等) |
| `pdftotext`(poppler 26)| 原生文本 PDF → TXT,快但糙 |
| `tesseract` 5.5 + lang | OCR 引擎,支持 eng / chi_sim / chi_tra / deu |
| `ebook-convert`(Calibre 9.7)| EPUB / AZW3 / MOBI ↔ PDF / EPUB / TXT / HTML |
| Calibre.app | EPUB/AZW3 GUI 管理 + DRM 检测 |

### 🐍 parenting-kb venv(Python 3.12,`~/Desktop/parenting-kb/.venv/`)

| 工具 | 用途 |
|---|---|
| `markitdown` 0.1.5 | 多格式 → MD 一站式(Microsoft 出品)|
| `ocrmypdf` 17.4 | 给扫描 PDF 加 OCR 文本层 |

### ♻️ 复用 hermes-kb-agent(不重装)

| 工具 | 位置 | 适用场景 |
|---|---|---|
| `rapidocr-onnxruntime` | hermes/.venv | 视频字幕 OCR(本项目用 tesseract 即可,不调用)|
| `mlx-whisper` | hermes/.venv | Tier 5 视频/播客转录(Phase 2+ 才用)|
| `ffmpeg` | brew(系统)| Tier 5 抽帧 |

## 常用命令速查

激活 venv(每次 session):
```bash
source ~/Desktop/parenting-kb/.venv/bin/activate
```

### EPUB / AZW3 → MD

```bash
# 单本(Calibre 法,质量最稳)
ebook-convert <input.epub> <output.md>

# 批量(在 raw_pdfs/ 里)
cd ~/Desktop/parenting-kb/10-sources/tier3-books/raw_pdfs
for f in *.epub *.azw3; do
  [ -f "$f" ] && ebook-convert "$f" "${f%.*}.md"
done
```

### 原生文本 PDF → MD

```bash
# 推荐: markitdown(质量最好)
markitdown <input.pdf> > <output.md>

# 备选: pdftotext(快但无版式)
pdftotext -layout <input.pdf> <output.txt>
```

### 扫描 PDF(图片型)→ 可搜索 PDF → MD

```bash
# 第一步: 加 OCR 文本层(中文需指定语言)
ocrmypdf --language chi_sim+eng <scanned.pdf> <searchable.pdf>
# 德语原版 #6 Pikler:
ocrmypdf --language deu <scanned.pdf> <searchable.pdf>

# 第二步: 转 MD
markitdown <searchable.pdf> > <output.md>
```

### DRM 检测

```bash
# Calibre 拖文件进 GUI,封面旁🔒图标 = 带 DRM
# 或命令行:
ebook-meta <file.epub>     # 能读出 metadata 即无 DRM
```

## 文件组织约定

```
10-sources/tier3-books/raw_pdfs/
├── karp_happiest_baby.epub      # 原始(gitignore)
├── karp_happiest_baby.md        # 转换产出(gitignore,版权同 EPUB)
├── stern_interpersonal_world.pdf
├── stern_interpersonal_world.md
└── ...
```

命名规则:`<author_lastname>_<short_title>.<ext>`,全小写,下划线分隔。

## 工具未覆盖的场景

| 场景 | 解决方案 |
|---|---|
| 带 DRM 的 Kindle / Apple Books | 不解决(任务书 §0)。买纸书 → iPhone 备忘录扫描 |
| 复杂版式 PDF(多栏/公式)markitdown 效果差 | 后续可装 `marker-pdf`(2GB ML 模型,Phase 1 视情况补) |
| 扫描质量差识别率低 | OCRmyPDF 加 `--deskew --clean` 参数,或预处理图像 |
| 中英混排 OCR | tesseract 用 `--language chi_sim+eng` 双语 |

## Phase 1 启动前的准备清单

- [ ] 把所有 EPUB/PDF/AZW3 拖到 `10-sources/tier3-books/raw_pdfs/`,按命名规则改名
- [ ] 检查 DRM(Calibre 拖一遍)
- [ ] 单本试转(推荐先转 #14 鲍秀兰中文 + #8 Karp 英文)
- [ ] 检查转出 MD 质量(乱码/缺页/版式失真),决定每本用哪条转换路线
- [ ] 全部转完后再启动 Phase 1 提取
