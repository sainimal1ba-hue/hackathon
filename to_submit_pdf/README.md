# to_submit_pdf — Round 0 Deck (HEROKILL · PS-WEB-01)

*The produced Round 0 submission deck. Forged 2026-11-28 under the organizers' official format law.*

## Format law (organizers' official template — frozen, found 2026-11-27)

- **8 slides, 10 × 5.625 in** (Google Slides default, 16:9), **"PPT or PDF · max 20 MB"** — produced as PDF, 317 KB.
- Section order is **fixed**: Cover (project title / one-line pitch / track / team) → Problem Definition → Proposed Solution → System Architecture → Feasibility & Scope → Impact Metrics → References & Attribution → Extra Slide.
- **Only the content inside the template changes.** Titles, order, slide count and dimensions never do.
- Anonymous submission: the deck carries the codename HEROKILL only — no member names, no account links.

## Files

- `HEROKILL_Round0_Deck.pdf` — the produced deck (delivered with the repo work; binaries are not pushed through the text-only commit channel).
- `HEROKILL_Round0_Deck.html` — the layout source: eight fixed 960×540 px pages, rendered to vector PDF via Playwright (`html2pdf-next.js`).
- `fonts/` — self-hosted Space Grotesk + JetBrains Mono (Google Fonts woff2 subsets + generated `fonts.css`).
- `ROUND0_DECK_CONTENT.md` — the exact slide copy; **edit content here first**, then mirror into the HTML.
- `SKILL.md` — 中文复刻手册.
- Production knowledge: `pdf_generation/SKILL.MD` (中文).

## Human-craft law applied (the research, condensed)

1. **Assertion-evidence headlines** — every slide title is a claim ("Deploying is a gamble. Failure hides behind dashboards."), not a topic label.
2. **One idea per slide, ≤150 words per slide** — deck copy edited brutally; details live in the warplan, not the deck.
3. **Two typefaces max** — Space Grotesk (voice) + JetBrains Mono (machine voice). Nothing else.
4. **≤5 colors, single-family accents** — ink `#161619`, muted `#6E6E76`, hairline `#E7E7EA`, RED CODE `#FF1E27`, resurrection green `#00A65A` (print-safe dim green) on white. One accent per slide.
5. **No stock images, no clipart, no AI-generated decoration** — the only drawn element is the brand's flatline-to-spike SVG stroke.
6. **No AI-tell phrases** — no "In today's fast-paced world", no "seamless", no "revolutionize", no "delve". Concrete numbers over adjectives: ≤10 s, ≤3 s, 137, 143, 00:07.
7. **Left-aligned lists, hanging indents, quiet chrome** — hairline rules, mono meta, generous whitespace; the template breathes like a human built it.
8. **Claims traceable to the warplan** — every number and feature on these slides exists in `warplan.md` §4–§6. Nothing invented for the deck.

## Rebuild

Fetch fonts → validate HTML → render → QA → set anonymous metadata. Full steps: `pdf_generation/SKILL.MD`.
