# HEROKILL — The Winning Design (Final Law)

*Champion: THE OPERA (50/60), refined with the spoils of THE VAULT and THE GREENROOM. This document is the complete, executable design system for the commercial HEROKILL website. A designer must be able to build from this file alone.*

## 1. Brand
- **Name treatment:** the word never renders in one color — **HERO** in resurrection green, **KILL** in RED CODE red, split by a flatline glyph. Anton caps, tight tracking.
- **Logo:** one SVG stroke: a heartbeat that flatlines, then spikes. Favicon (16px) = the spike alone. Projector (20m) = the full stroke.
- **Tagline:** "Push. Die. Rise."
- **Voice:** mortuary-poetic terseness. Exit codes quoted like scripture: "137. Out of memory. We remember." UI copy is lowercase, laconic, never apologizes — it certifies. Buttons are verbs: EXECUTE, RESURRECT, SCRUB.

## 2. Color tokens
Void `#050505` bg · Stage `#0B0B0D` panels · Wings `#131316` raised · Veil `#1F1F24` hairlines · Bone `#F2F0EB` text · Muted `#75757E` · RED CODE `#FF1E27` · Blood Pool `#5C0A0F` glow · Rise Green `#00FF7B` · Dim Green `#0E3B24` · Seal Gold `#C9A227`.
**Law:** red and green never share a screen state; gold never leaves the certificates; 60% of every resting screen is pure void, so the floods hit like floods.

## 3. Typography
- **Anton 400** display, clamp(64px, 14vw, 220px); dramatic beats at 8–14vw, two lines — one red, one green.
- **Space Grotesk** 400/500/700 body, 16px/1.6.
- **JetBrains Mono** 400/700 — logs, timers, certificates, machine voice.
- Scale 1.333 on 16px: 12, 16, 21, 28, 38, 50, 67, 90.

## 4. Layout
12-col, 1440 max, 8pt spacing, 1px Veil hairlines. Sections are numbered acts (01–07) with mono eyebrow labels. Whitespace is a weapon.

## 5. Homepage — the Seven Acts
1. **01 OVERTURE** — the visitor dies first: void; "IT DIED AT 00:07." in red as the heartbeat line flatlines; one scroll later, "IT CAME BACK. NINE SECONDS." green — the line spikes. Thesis performed, never claimed.
2. **02 THE PUSH** — self-typing terminal: `$ git push herokill main`; build log scrolls like a libretto. Adopted beat: green-lock theater — fake browser chrome, padlock snaps green: "pre-minted wildcard · dns overridden · offline."
3. **03 THE DEATH** — pick your weapon (memory leak / dependency bomb / kill -9). The JUDGE'S TRIGGER is a confirm-hold: press 800ms, release, EXECUTE. The screen floods RED CODE in steps(1) — dying is never a fade — and the container card goes dark.
4. **04 THE AUTOPSY** — Death Certificate No. 047, gold-stamped; exit code translated: "137 — out of memory. we remember."
5. **05 THE RESURRECTION WINDOW** — countdown 3-2-1; the timer freezes at 00:07 for 1.5s — the room finishes the count aloud — then the flood: void to Rise Green. This is THE ROAR.
6. **06 THE TIMELINE** — playhead pinned to the viewport edge; dragging scrubs the SQLite event stream and the logs run backwards.
7. **07 JOIN THE HOUSE** — one input: "push your own death."

## 6. Interactive components (build these)
1. **Overture heartbeat** — SVG stroke-dashoffset driven by scroll.
2. **Self-typing terminal** — typed.js, deterministic loop.
3. **JUDGE'S TRIGGER** — confirm-hold; scales under finger; release fires the scripted death.
4. **Countdown freeze** — freezes 00:07, green flood, single 600ms glow pulse.
5. **Incident scrubber** — rAF over the pre-recorded JSON event array; logs invert, graphs rewind; arrow-key operable.
6. **Live heartbeat wall / killfeed** — deterministic JS array ticking (WS only if live); hover a death, its certificate opens.
7. **Certificate generator** — every kill mints a numbered, gold-sealed card; OG-shareable — viral by design.

## 7. Motion law
Entrances: cubic-bezier(.16,1,.3,1) 600–900ms, once. Deaths: steps(1,end) — instant. Resurrection: 400ms flood + one pulse. Live data: raw, no easing. Nothing decorative moves; only state changes. Parallax capped at 0.35. No strobes, ever.

## 8. Accessibility
Color never carries meaning alone — every state is color + icon + label. Scrubber, picker and trigger are fully keyboard-operable with 2px green focus rings. prefers-reduced-motion: floods become 150ms crossfades, the terminal types instantly. Overture completes under ten seconds. Verify red/green under projector wash at +3 brightness.

## 9. 24h build order
H0–2 tokens, grid, and the event-stream JSON spine (one array drives wall, killfeed, scrubber, certificates). H2–6 overture + terminal. H6–10 weapon picker, death flood. H10–14 countdown freeze, roar, certificate template. H14–18 scrubber. H18–21 killfeed wall, green-lock beat, JOIN THE HOUSE. H21–24 reduced-motion, OG card, projector test, live-demo rehearsal.

## 10. Image assets
Full generation prompts: `image_prompt.md` (v2 — the sealed Flow law: seven assets, the OPERA LOCK, delivery specs, the 60-second acceptance check). The v1 Flow outputs were retried on 2026-11-28: 5 KILL / 2 FIX / 0 KEEP — see `image_audit.md`. Regenerate all seven under v2 before the site build.

## 11. Hero animation
The Act 01 hero animation is law in `hero_animation.md` — THE CHANT, champion of the Animation War (53/60; war history in `animation_war.md`). Three Flow clips (VIGIL-RED / BREAKER / SAINT) chained frame-to-frame; the DOM is the clock; the death is a single-frame cut; the kill frame gets a gold-stamped certificate with the visitor's real timestamp.

**The crown is struck. Build the Opera — and let the room count to seven.**
