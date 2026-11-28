# to_submit_pdf — Round 0 Deck (HEROKILL · PS-WEB-01)

*The produced Round 0 submission deck. Forged 2026-11-28 under the organizers' official format law.*

## Format law (organizers' official template — frozen, found 2026-11-27)

- **8 slides, 10 × 5.625 in** (Google Slides default, 16:9), **"PPT or PDF · max 20 MB"** — produced as PDF, ~356 KB.
- Section order is **fixed**: Cover (project title / one-line pitch / track / team) → Problem Definition → Proposed Solution → System Architecture → Feasibility & Scope → Impact Metrics → References & Attribution → Extra Slide.
- **Only the content inside the template changes.** Titles, order, slide count and dimensions never do.
- Anonymous submission: the deck carries the codename HEROKILL only — no member names, no account links.

## Files

- `HEROKILL_Round0_Deck.pdf` — the produced deck (delivered with the repo work; binaries are not pushed through the text-only commit channel).
- `HEROKILL_Round0_Deck.html` — the layout source: eight fixed 960×540 px pages, rendered to vector PDF via Playwright (`html2pdf-next.js`).
- `workflow_diagram.html` — standalone source of the slide-4 workflow diagram (1160×560, same design language; PDF + 150 dpi PNG rendered alongside the deck).
- `fonts/` — self-hosted Space Grotesk + JetBrains Mono (Google Fonts woff2 subsets + generated `fonts.css`; regenerate via `pdf_generation/fetch_deck_fonts.py`).
- `ROUND0_DECK_CONTENT.md` — the exact slide copy; **edit content here first**, then mirror into the HTML.
- `SKILL.md` — 中文复刻手册.
- Production knowledge: `pdf_generation/SKILL.MD` (中文).

## The slide-4 workflow diagram (added 2026-11-28)

Four labeled lanes, read top to bottom — **BIRTH** (git push → post-receive hook → stack detector → Docker build → cgroup cage → Caddy), **DEATH** (chaos weapon → health fails → RED CODE → rollback → 00:07 resurrection → death certificate), **SPINE** (SQLite append-only event spine — WebSocket bus · 1 s pushes), **SINKS** (status wall · killfeed · incident scrubber · death certificates). Both chains append into the spine (hairline vertical ticks); the spine streams to the sinks. RED CODE carries the red accent, 00:07 resurrection the green. The template's section title, order, slide count and page size untouched — the diagram lives inside the frozen System Architecture slide.

## Human-craft law applied (the research, condensed)

1. **Assertion-evidence headlines** — every slide title is a claim ("Deploying is a gamble. Failure hides behind dashboards."), not a topic label.
2. **One idea per slide, ≤150 words per slide** — deck copy edited brutally; details live in the warplan, not the deck.
3. **Two typefaces max** — Space Grotesk (voice) + JetBrains Mono (machine voice). Nothing else.
4. **≤5 colors, single-family accents** — ink `#161619`, muted `#6E6E76`, hairline `#E7E7EA`, RED CODE `#FF1E27`, resurrection green `#00A65A` (print-safe dim green) on white. One accent per slide; the diagram's red+green pair follows the cover-stroke and slide-8 precedent.
5. **No stock images, no clipart, no AI-generated decoration** — the only drawn elements are the brand's flatline-to-spike SVG stroke and the hand-coded slide-4 workflow diagram (HTML/CSS lanes — informational content, not decoration).
6. **No AI-tell phrases** — no "In today's fast-paced world", no "seamless", no "revolutionize", no "delve". Concrete numbers over adjectives: ≤10 s, ≤3 s, 137, 143, 00:07.
7. **Left-aligned lists, hanging indents, quiet chrome** — hairline rules, mono meta, generous whitespace; the template breathes like a human built it.
8. **Claims traceable to the warplan** — every number and feature on these slides exists in `warplan.md` §4–§6. Nothing invented for the deck.

## Rebuild

Fetch fonts → validate HTML → render → QA → set anonymous metadata. Full steps: `pdf_generation/SKILL.MD`.
