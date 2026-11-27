# DG-2 — THE OPERA

> Design War · gladiator speech · fought 2026-11-27
> Fate: **CHAMPION — 50/60.** Refined into the Final Law in `winner-design.md`.

---

# THE OPERA

**Every visitor dies once in the first ten seconds. That is the law of this house.**

**1. BRAND.** Name treatment: **HEROKILL** — HERO in resurrection green, KILL in blood red, split by a flatline glyph. Logo: one SVG stroke that dies flat and spikes alive — the whole product in a mark. Tagline: **"Push. Die. Rise."** Voice: mortuary-poetic terseness. Exit codes quoted like scripture: *"137. Out of memory. We remember."* Never playful in red moments; never solemn in green ones. Calm as a stagehand who has watched a thousand deaths.

**2. COLOR.** Void `#050505` (page), Stage `#0B0B0D` (sections), Wings `#131316` (cards). Bone text `#F2F0EB`, muted `#75757E`. RED CODE red `#FF1E27`, blood pool `#5C0A0F` for glows. Resurrection green `#00FF7B`, dim `#0E3B24`. Accent gold `#C9A227` — certificate seals only; rarity must look rare. Why: near-black makes light an event. The discipline IS the story — red means dying, green means alive, and they touch for exactly one second at the resurrection frame. That collision is the brand.

**3. TYPOGRAPHY.** Display: **Anton 400**, uppercase, hero at `clamp(64px,14vw,220px)`. Body: **Space Grotesk 400/500/700**, 16px, line-height 1.6. Mono: **JetBrains Mono 400/700** — logs, timers, certificates. Scale 1.333 on a 16px base; mono microcopy 12px, tracked 0.08em, uppercase. Dramatic moments: Anton at 8–14vw, two lines — one red, one green.

**4. LAYOUT.** 12 columns, 1440 max, 8pt spacing, sections numbered as acts.
- **01 OVERTURE** — void. "IT DIED AT 00:07." in red; a heartbeat line flatlines beneath it. One scroll later: "IT CAME BACK 9 SECONDS LATER." in green; the line spikes. Thesis performed, not claimed.
- **02 THE PUSH** — terminal types `git push herokill main`; the build log scrolls like a libretto.
- **03 THE DEATH** — visitor picks a chaos weapon; screen floods RED CODE; the container card goes dark.
- **04 THE AUTOPSY** — Death Certificate No. 047, stamped, mono; exit code translated into cause of death.
- **05 THE RESURRECTION WINDOW** — countdown 3-2-1, timer freezes at 00:07, green floods back. The roar.
- **06 THE TIMELINE** — a playhead pinned to the viewport edge; dragging it scrubs the entire story.
- **07 JOIN THE HOUSE** — one input: "Push your own death."

**5. INTERACTIVITY.**
1. **Scroll-driven overture** — the 10-second feel; the page performs the product.
2. **Drag-the-playhead scrubber** — logs run backwards; the signature demo made tactile.
3. **Live heartbeat wall** — WebSocket killfeed of containers dying and reviving; the site feels inhabited.
4. **Chaos-weapon picker** — poison code, dependency bomb, memory leak, `kill -9`; the Judge's Trigger — the crowd executes the kill itself.
5. **Countdown-to-resurrection** — freezes at 00:07 so the room counts the Three-Second Lift aloud; built for the audience vote.
6. **Cursor-reactive killfeed** — hover any event and its Death Certificate opens; autopsy as ambience.
7. **Certificate generator** — every kill mints a numbered certificate; viral by design.

**6. MOTION.** One easing: `cubic-bezier(.16,1,.3,1)`, 600–900ms entrances. Deaths use `steps(1,end)` — instant, never a fade; dying must not feel gentle. Scroll: parallax at 0.35–0.5 velocity, pinned sections scrubbed by transform. Hover: 150ms, opacity and translate only. Live data: raw, no easing. Rule: nothing decorative moves — only state changes move.

**7. IMAGES.** One style: cinematic dark theater, volumetric fog, single rim light, 35mm, no text.
1. "Empty black opera stage, one server rack as lone performer under blood-red spotlight, thick fog, cinematic, moody."
2. "Fallen server rack rising upright in green god-light, fog parting, dark theater, cinematic rim light."
3. "Overhead macro of a motherboard on a steel autopsy table, red gel lighting, surgical instruments, near-black."
4. "Opera balconies filled with faceless shadow figures holding tiny green glowing screens, eerie, dark."
5. "Abstract smoke gradient from blood red to resurrection green on pure black, billowing, film grain."
6. "Embossed death certificate on black velvet, one green candle glow, macro, aged paper texture."

**8. KILL STROKES.** THE VAULT dies: terminal brutalism is the default accent of forty dev-tool clans — it earns a nod, never a roar; it explains but makes no one feel. THE GREENROOM dies: warmth is wrong for a product whose demo is murder; mascots wilt at "dependency bomb"; Stripe already built that site, better. In a 24-hour arena nobody out-builds a feeling. Finals are crowned by audience vote — feeling wins, credibility is assumed. We weaponize the countdown; they weaponize gradients.

**9. 24H BUILDABILITY.** Ships fast: scrubber is rAF over a JSON array; heartbeat is SVG `stroke-dashoffset`; weapon picker replays scripted events; WebSocket feed is product core; certificates are SQLite plus template. CSS trickery: overture parallax, pinned timeline. Risks: cap scroll velocity against nausea; honor `prefers-reduced-motion`; pair every color with icon and label for colorblind judges; keep the overture under ten seconds.

**We do not show the product. We perform it. DG-2 stands.**
