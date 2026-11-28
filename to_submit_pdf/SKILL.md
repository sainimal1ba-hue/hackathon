# to_submit_pdf 复刻手册（中文）

*本目录是 Round 0 匿名路演 PDF 的产房。母法：组委会官方模板（2026-11-27 查得）——8 页、10×5.625 英寸、PPT 或 PDF · 最大 20 MB，章节顺序冻结：Cover → Problem Definition → Proposed Solution → System Architecture → Feasibility & Scope → Impact Metrics → References & Attribution → Extra Slide。只改内容，不动骨架。*

## 前置条件

- Node + Playwright（`html2pdf-next.js` 依赖）、Python 3、`pymupdf`（QA 用）。
- PDF 技能目录：`/home/z/my-project/skills/pdf`（下称 `$PDF_SKILL_DIR`）。

## 字体自托管（一次性）

沙盒的 Chromium 加载不了 Google Fonts CDN，必须把字体落到本地：

1. 用 Chrome UA 拉取 CSS：`curl -s -A "Mozilla/5.0 ... Chrome/120" "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" -o /tmp/gf.css`
2. 提取 CSS 里全部 `fonts.gstatic.com` URL，逐个下载到 `to_submit_pdf/fonts/`（woff2）。
3. 跑 `pdf_generation/fetch_deck_fonts.py`：把 CSS 里每个 URL 替换成同目录相对文件名，生成 `fonts/fonts.css`。**注意：CSS 内的 url() 相对于 CSS 文件自身目录解析，不要带 `fonts/` 前缀**——这是本管线踩过的坑。
4. HTML 头部用 `<link href="fonts/fonts.css" rel="stylesheet">` 替换 Google CDN 链接。

## 构建管线（每改必跑）

```bash
PDF_SKILL_DIR=/home/z/my-project/skills/pdf
cd to_submit_pdf
# 1. 预检（HTML→PDF 铁律）
python3 "$PDF_SKILL_DIR/scripts/poster_validate.py" check-html HEROKILL_Round0_Deck.html
# 2. 渲染（固定 960×540px 页，Chromium 原生分页——固定尺寸页不需要 Paged.js）
node "$PDF_SKILL_DIR/scripts/html2pdf-next.js" HEROKILL_Round0_Deck.html \
  --output HEROKILL_Round0_Deck.pdf --width 960px --height 540px --nopaged
# 3. QA
python3 "$PDF_SKILL_DIR/scripts/pdf_qa.py" HEROKILL_Round0_Deck.pdf --no-tables
# 4. 元数据（匿名！不得写生成工具名）
python3 "$PDF_SKILL_DIR/scripts/pdf.py" meta.set HEROKILL_Round0_Deck.pdf -o /tmp/deck_meta.pdf -d '{"Title":"HEROKILL — Round 0 Idea Deck (PS-WEB-01...)", "Author":"HEROKILL clan (anonymous Round 0 submission)", ...}'
mv /tmp/deck_meta.pdf HEROKILL_Round0_Deck.pdf
# 5. 目检（全部 8 页）
pdftoppm -r 60 -jpeg HEROKILL_Round0_Deck.pdf /tmp/render/page
```

## 本项目踩过的坑（勿重蹈）

1. **`cover_validate.js` 对本类文档是误报源**：它是给 Report/Academic 的绝对定位封面用的；对并排表格单元格/同行 flex 元素会报假的 text↔text 重叠。技能文件地图明言"Do NOT run on posters or documents"。本管线以全页目检代替它。
2. **@page 不认 CSS 变量**：`size: 960px 540px` 必须写死。
3. **禁止 overflow:hidden** 于 html/body/.page；装饰元素不得越界（width ≤100%，无负偏移）。
4. **@media screen 缩放块必须存在**（浏览器预览用，不影响打印）。
5. **960px = 720pt = 10 英寸；540px = 405pt = 5.625 英寸**——QA 报 254×143mm 即正确。
6. **二进制 PDF 不走 push_files**（文本通道会毁掉 blob）：成品 PDF 直接交付用户，仓库只存 HTML 源 + 内容 + 手册。

## 修改守则

- 改内容先改 `ROUND0_DECK_CONTENT.md`，再镜像进 HTML；标题、页数、顺序、尺寸永不改。
- 每页 ≤150 词、两字族、≤5 色、每页装饰 ≤3、无库存图/AI 图、无 AI 腔短语（seamless / delve / revolutionize / In today's world）。
- 每个数字必须能在 `warplan.md` §4–§6 找到出处，禁止为页面上墙编造。
- 交付前：pdf_qa 全绿 + 8 页目检 + 元数据匿名。
