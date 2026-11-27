# DG-1 — THE VAULT

> Design War · gladiator speech · fought 2026-11-27
> Fate: FELL — 45/60. Surviving elements adopted into the Final Law (THE OPERA): deterministic data spine (pre-recorded JSON, WS only if live), CSS-only scrubber mechanics, typed.js terminal, JetBrains Mono machine voice, hour-by-hour build order.

---

# ⬛ THE VAULT — DESIGN DIRECTIVE: *HEROKILL*

*They will vote for the site that dies in front of them and comes back. So the site IS the product dying. Everything below is a weapon.*

## 1. BRAND
- **Name treatment:** `HEROKILL` set in monospace, all-caps, tight tracking — rendered like a shell command: `$ herokill`. Blinking block cursor after it. The logo is the cursor.
- **Logo concept:** A square terminal glyph `[ ]` split diagonally — top half green (alive), bottom half red (dead) — the killfeed icon. Reads at 16px favicon and on a projector from 20 meters.
- **Tagline:** **"WATCH IT DIE. BRING IT BACK."** Sub: `git push → chaos → resurrection in <10s.`
- **Voice/tone:** Terminal-laconic. Lowercase system messages. Say `exit 137 — oom` not "oh no, it crashed." No exclamation marks — ever. Confidence through understatement.

## 2. COLOR SYSTEM
| Token | Hex | Why |
|---|---|---|
| Void (bg) | `#0A0B0D` | True near-black; projector-proof |
| Panel | `#0F1115` | Card layer, no gradients |
| Raised | `#16191F` | Hover/active |
| Hairline grid | `#1F232B` | The blueprint skeleton — 1px everywhere |
| Text primary | `#E8EAED` | 16:1 contrast |
| Text secondary | `#8B929E` | Dimmed logs |
| RED CODE | `#FF2E4C` | One red. Deaths, borders, CTAs of destruction |
| RESURRECTION | `#23F0A0` | One green. Health, rollback success |
| Amber | `#FFB020` | Warnings only, rationed |

Two accents, never mixed in one component. The screen literally flushes red, then green — that's the drama.

## 3. TYPOGRAPHY (Google Fonts)
- **Display:** JetBrains Mono **800**, tracking -0.02em — brutalist headlines as commands.
- **Body:** Inter **400/500** — quiet, Vercel-grade legibility.
- **Mono (system voice):** JetBrains Mono **400** — logs, timestamps, exit codes.
- **Scale (fluid, clamp):** `12 / 14 / 16 / 20 / 28 / 40 / 64 / 96px`. Everything is 12px mono by default; type gets loud only for RED CODE.

## 4. LAYOUT SYSTEM
- 12-col grid, 1200px max, 8px spacing base, 24px site gutters, hairline borders on every cell — the page reads as a live circuit board.
- **Homepage, top to bottom:**
  1. **LIVE STATUS WALL (hero):** full-viewport grid of container tiles, green, pulsing. One dies mid-visit — red flash, border bleeds, crowd gasps.
  2. **KILLFEED TICKER:** infinite marquee of deaths: `13:42:07 api-gateway ✝ exit 143 → restored 3.1s`.
  3. **PUSH-TO-DEPLOY:** split-screen — a git command on the left, the build streaming on the right.
  4. **CHAOS PLAYGROUND:** pick your poison (OOM / kill -9 / poison push), press EXECUTE.
  5. **THE RESURRECTION WINDOW:** countdown freeze-frame at `00:07`.
  6. **SCRUB THE INCIDENT:** the timeline scrubber as a full section.
  7. **DEATH CERTIFICATES:** numbered certificates, embossed, `137 = OOM`.
  8. **STACK + CTA:** footer terminal: `$ herokill --start`.

## 5. INTERACTIVITY (the arsenal)
1. **Live Status Wall** — WebSocket-fed tiles breathing green; one randomly dies; grid heals. *Wow: the homepage is a morgue and an ICU.*
2. **Chaos Playground** — user executes a kill; container dies; rollback fires in <10s. Crowd pulls the trigger themselves.
3. **Timeline Scrubber** — drag the playhead; logs run *backwards*. Only we have time travel.
4. **Self-Typing Terminal** — types the demo while you watch, cursor blinking. Zero-effort storytelling.
5. **Hover Killfeed** — hover any death → tooltip autopsy: exit code, cgroup stats, timestamp.
6. **Countdown Moment** — big 800-weight mono timer, freezes at `00:07`, screen washes green. A built-in ritual for the room.
7. **Judge's Trigger** — a physical-feeling EXECUTE button with confirm hold; red ripple across the whole grid.

## 6. MOTION LANGUAGE
- UI feedback: **150ms ease-out**. State flips (red/green): **400ms** with a 2Hz flash ×3 — perceivable from the back row.
- Scroll: sections pin, hairline grid *draws itself* (CSS `clip-path` on scroll).
- Nothing floats, nothing bounces. Motion = state change. Brutal, legible, fast.

## 7. IMAGE ASSETS (generate in first 2h, style-locked)
Shared style suffix: *"dark terminal-brutalist, near-black #0A0B0D background, thin white hairline grid lines, monospace text fragments, one blood-red #FF2E4C and one neon-green #23F0A0 accent, flat vector, high contrast, no gradients, no people."*
1. **Hero backdrop:** "empty server cage blueprint, isometric wireframe containers glowing green, one red, on black graph-paper grid."
2. **Chaos icons:** "four flat glyphs — leaking memory drop, bomb, skull-9, broken package — line icons, red accents, minimal."
3. **Death Certificate:** "official-looking certificate mock, black paper, embossed white mono type 'CERTIFICATE OF DEATH — EXIT 137', red wax stamp."
4. **Resurrection streak:** "long-exposure light trail arcing from red dot to green dot across dark grid."
5. **Caddy/route diagram:** "hairline topology map: git → hook → docker → caddy, white lines, green nodes."
6. **OG social card:** "black card, giant white mono 'HEROKILL', tiny red cursor block, one green tile grid."

## 8. KILL STROKES
**THE OPERA dies because:** motion-everything = 24h suicide. Huge display type without an engine behind it is a poster, not a product. Dev-tool judges smell theater without credibility. And cinematic choreography collapses when the WiFi doesn't.
**THE GREENROOM dies because:** warmth cannot narrate death. You cannot paint a `kill -9` in pastel. Stripe polish takes 6 months; we can't fake it in 24 — but brutalism is *honest*. The product's drama IS dark. The crowd shouts for blood, not onboarding smiles.

## 9. 24H BUILDABILITY
- **Hours 0–4:** fonts, tokens, hairline grid, status wall with faked deterministic "live" data (a JS array, not WebSockets — swap to real WS only if time allows).
- **Hours 4–10:** scrubber (CSS `transform: scaleX`, invert log array), self-typing terminal (typed.js), killfeed marquee (CSS keyframes).
- **Hours 10–16:** chaos playground — reuses the real backend story with mocked timing.
- **Hours 16–24:** Death Certificates, countdown freeze, polish, deck screenshots.
- **Risk notes:** red-on-black contrast (keep body text `#E8EAED`); real chaos demo needs the Docker rig rehearsed by hour 12; fallback = pre-recorded resurrection timeline.

**The Vault closes. The grid breathes. Let them watch it die.**
