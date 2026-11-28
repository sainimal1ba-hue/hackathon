# HEROKILL — Hero Animation Law: THE CHANT

*Champion of the Animation War (53/60), refined with the spoils of all three fallen gladiators. Executable law: a developer builds from this file alone. Prompt law, generation settings and acceptance checks: `image_prompt.md` (v2).*

## The concept

The visitor conducts a public execution and watches it resurrect. The hero counts down aloud — giant numerals, one per second — the rack dies in a single frame, the kill frame is gold-stamped with the visitor's real timestamp, half a second of void, then the breaker slams green. First paint is a finished sentence: a corpse, a verdict, and a giant 7.

## Frames (Nano Banana Pro, seed-locked, per image_prompt.md v2)

- **F1** — Overture backdrop (asset 1): the lone rack, red cone. Doubles as poster and reduced-motion fallback.
- **F2** — NEW: the identical stage, rack dark, cone dead — same seed, verbatim description block; only the light and LED states change.
- **F3** — Resurrection (asset 2): the rack upright in the green god-light.

## Clips (Google Flow, Omni Flash 1.2; locked-off; motion-only prompts; OPERA LOCK appended)

1. **THE VIGIL-RED** (4–6s; F1 → F1 held): Dust drifts slowly down through the red beam; the rack LEDs hold steady red; haze barely moves. Hue locked fire-truck red, zero green. Ends held one second. Audio: faint low stage hum.
2. **THE BREAKER** (4s; F2 → F3): The green beam lands in the first instant; the rack LEDs snap on bottom to top in a fast cascade within one second; haze lifts; then all holds steady. Hue locked traffic-light green, zero red. Ends held steady green. Audio: one clean power-up chime.
3. **THE SAINT** (8s loop; F3 → F3, pixel-identical): The rack LEDs breathe in slow unison like a sleeping chest; dust motes rise slowly through the green beam; the light stays constant. Ends pixel-identical to start, held. Audio: soft room tone.

Every clip ends on a held terminal state ≥1s; endpoints pixel-verified before export.

## The beat sheet (the DOM is the clock; the video is ambience)

| Beat | What happens | Law |
|---|---|---|
| 0s — first paint | F1 poster + DOM type: IT DIED AT 00:07. (red Anton), ECG flatlines | the sentence reads with zero video |
| 0–7s — THE CHANT | VIGIL-RED loops; giant JetBrains Mono numerals 7→1, one per second, rAF-driven | the hall chants aloud |
| 7s — THE KILL | single-frame cut to F2; no interpolation, ever | steps(1); the video never renders the death |
| 7s — THE STAMP | the kill frame freezes; a Seal Gold certificate stamp slams in bearing the visitor's real timestamp (JetBrains Mono) | gold only here |
| +0.5s — THE VOID | half-second dead-black hold (DOM layer) | adopted from DG-1/DG-3 |
| then — THE BREAKER | cut to clip 2 (beam <0.5s, cascade <1s, hold) + DOM 400ms green flood + one pulse; type flips: IT CAME BACK. NINE SECONDS. (green) | breaker law |
| rest — THE SAINT | clip 3 loops green forever; ECG spikes; certificate stays on screen | once-only death (DG-2) |
| re-run | scroll-to-top, or press-and-hold the kill card 800ms (the JUDGE'S TRIGGER pattern), re-fires the sequence once per trigger | the room can demand an encore |

## Integration law

- Weight ≤3MB total hero assets; 1080p minimum (720p banned — the projector at forty feet); AV1 WebM + H.265/MP4 fallback.
- Autoplay muted, playsinline, loop; IntersectionObserver pauses offscreen.
- prefers-reduced-motion: poster F1 + static type + stepped ECG only — the sentence still lands.
- Audio muted by default; first interaction unmutes (heartbeat, flatline tone, power-up chime at 00:07). The chant works with zero audio: giant numerals are visual percussion.
- Numerals beat against deterministic DOM layer cuts, never against video currentTime.
- Red and green never share a frame: every red→green passage passes through the void beat or a single-frame cut.

## Build order (~8.5h, inside the winner-design H-budget)

| Task | Hours |
|---|---|
| Generate F2 + regenerate F1/F3 under v2 law (seed-locked, hex-checked) | 1.0 |
| Flow: 3 clips with retries at micro-clip prices | 3.0 |
| DOM beat rig: countdown, layer cuts, stamp, flood, void beat | 3.0 |
| Pixel-diff loop verification, weight pass, reduced-motion, projector test | 1.5 |

**Fallback if Flow misbehaves:** three locked stills + the full DOM choreography already perform the chant — the architecture never depended on the video.

*The room counts to seven. Let it.*
