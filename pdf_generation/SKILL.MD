# PDF 生成总纲 — pdf_generation/SKILL.MD（中文）

*HEROKILL 战争房的一切 PDF 生产知识，自此文件始。路由、管线、字体、坑位、守则，全部在此沉淀。生成日期：2026-11-28。*

## 一、路由判决

| 交付物 | 路由 | 工具 | 关键参数 |
|---|---|---|---|
| Round 0 路演 PDF（8 页、10×5.625 英寸、固定模板） | Creative Fixed-Canvas **bypass 模式**（模板复刻，非蓝图生成） | `html2pdf-next.js` | `--width 960px --height 540px --nopaged` |
| 后续若做海报/证书/信息图 | Creative Fixed-Canvas 蓝图模式 | `design_engine.py` + `convert.blueprint` | 5 阶段蓝图 |
| 纯文报告/合同/试卷 | Report（ReportLab） | `report.md` | 先跑 `palette.cascade` |

**为何 bypass**：组委会模板已冻结结构，生成式蓝图会和"只改内容"的铁律打架。手写 8 个固定 960×540px 的 `.page`，全走技能的通用铁律（@page 写死 px、margin 0、无 overflow:hidden、@media screen 缩放、装饰不越界、字体带兜底）。

**为何 --nopaged**：固定尺寸页逐页 `page-break-after`，Chromium 原生分页即可；Paged.js 面向流式内容，此处多余且会重排绝对定位。

## 二、字体法

- 品牌字族：**Space Grotesk**（人声）+ **JetBrains Mono**（机器声）。两族封顶。
- Chromium 沙盒加载不了 Google CDN → **必须自托管**：拉 CSS、下 woff2、生成 `fonts/fonts.css`（url 相对 CSS 自身目录）、`<link>` 本地引入。
- 每次 `font-family` 必须带通用兜底（validator 会查）：`'Space Grotesk', Arial, Helvetica, sans-serif` / `'JetBrains Mono', 'Courier New', monospace`。
- 中文文档走 ReportLab 时用 Noto Serif SC；HTML/Playwright 中文用 Google Fonts Noto Sans SC `<link>`（外网通时）或本地字体。

## 三、管线（通用七步）

1. **改内容**：先改文案源（`to_submit_pdf/ROUND0_DECK_CONTENT.md`），再镜像进 HTML。结构与尺寸永不碰。
2. **预检**：`poster_validate.py check-html`。ERROR 必修；`COVER_TEXT_OVERLAP` 若来自并排表格/同行 flex，为 cover_validate 越界误报（该工具仅限 Report/Academic 封面），以全页目检裁决。
3. **渲染**：`html2pdf-next.js --width 960px --height 540px --nopaged`。禁止手写 Playwright 脚本。
4. **QA**：`pdf_qa.py <pdf> --no-tables`。PASS 才准出门；FAIL 必修重渲。正确页面尺寸报告 = 254×143mm。
5. **元数据**：`meta.set` 写 Title/Author/Subject/Creator。**匿名交付物禁止出现生成工具名**，Author 写队伍代号。
6. **目检**：`pdftoppm -r 60 -jpeg` 后逐页看图。8 页看全 8 页。看：重复块、空列、断行、溢出、装饰越界、页脚碰撞、字体未加载（Liberation 兜底出现即字体没吃到）。
7. **交付**：成品 PDF + HTML 源一起交付；二进制不入库（push_files 是文本通道），入库的是源与知识。

## 四、铁律清单（违反即返工）

- `@page { size: 960px 540px; margin: 0; }` —— px 写死，CSS 变量在 @page 里静默失效。
- `html,body { margin:0; padding:0; background:<页色> }` —— 深浅混排时 body 用最深页色。
- `.page { width:960px; height:540px; position:relative }`，页间 `page-break-after: always`。
- html/body/.page 上禁止 `overflow:hidden`；装饰元素 width ≤100%、无负偏移。
- 每 `.page` 内容填充 ≥60%；每页 ≤3 个装饰元素；单族色系 ≤5 色；两字族封顶。
- 无库存图、无 clipart、无 AI 生成装饰图；唯一允许的图形是品牌自己的 SVG 平线-复搏笔画。
- 无 AI 腔：In today's world / seamless / delve / revolutionize / empower 一律禁用；用具体数字说话。
- 断言式标题：每页标题是一个主张，不是话题标签。
- 匿名规则：Round 0 交付物上只有代号，无真名、无账号、无生成工具水印。
- 每个上墙的数字必须能在 `warplan.md` §4–§6（或 intel.md）找到出处。

## 五、已知坑位（血泪账）

1. CSS 内 url() 相对 **CSS 文件自身目录**，不是 HTML 目录——字体路径写错字体会静默掉到 Liberation。
2. `cover_validate.js` 只该跑在 Report/Academic 的绝对定位封面上；对表格/flex 文档全是假重叠。
3. `meta.set` 不能覆盖输入文件，先输出到 /tmp 再 mv。
4. QA 字体列表出现 LiberationSans/LiberationMono = 品牌字体没吃到，先查 fonts.css 路径。
5. `pdf_qa.py` 的 Author 警告若因 meta.set 失败，重跑第 5 步。
6. woff2 校验：文件头四字节 `wOF2`。

## 六、当前状态

- Round 0 deck：`to_submit_pdf/HEROKILL_Round0_Deck.pdf` 已产（8 页，~317KB，矢量文字，匿名元数据），HTML 源与内容同目录。QA 10 项全过，8 页目检通过。
- 待办：若组委会下发给真名/队伍信息的注册表，Cover 的 TEAM 行按注册信息替换后重渲。
