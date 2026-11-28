# The Image Retrial — The Inquisitor's Verdict

*Fought 2026-11-28. The seven Flow-generated v1 assets (prompts from `image_prompt.md` v1) were forensically audited by a vision model and sentenced by THE INQUISITOR. Summary judgment: 5 KILL, 2 FIX, 0 KEEP — nothing ships as-is. The replacement law lives in `image_prompt.md` (v2, sealed).*

## Scoreboard

| # | Asset | Verdict | Cause of death |
|---|---|---|---|
| 1 | Overture backdrop (rack, red cone) | FIX | Right composition (cohesion 8/10) — but a 4-point sparkle watermark lower-right, melted pseudo-hardware, impossible fog wrap, weak contact shadow. |
| 2 | Resurrection (green god-light) | KILL | Fidelity inversion: the prompt said rising upright, the model delivered toppled. Floating cables, no pivot under the rack, second sparkle artifact, green desaturated. |
| 3 | Autopsy (motherboard tray) | KILL | Cloned instruments at 120° intervals, no contact shadows, a tray that ignores its instruments, sparkle glyph bottom-right, red drifted to #C0392B, PCB silkscreen gibberish. |
| 4 | The house (balconies) | KILL | A daylight shaft inside a pitch-dark hall; green lights floating unattached to hands; cloned same-size screens; melted crowd; tack-sharp squares riding blurred seats. |
| 5 | Divider (red→green smoke) | FIX | The only theatre-grade frame of the set (cohesion 9, lighting 8). Regrade to exact hex, crop the melted right curtain, give the smoke a floor line. |
| 6 | Certificate plate | KILL | Delivered an envelope, not a certificate. Zero brand color: olive candle, crimson seal — Seal Gold #C9A227, reserved by law for exactly this shot, absent. Impossible candle-lit set (lighting 3/10). |
| 7 | OG card (letters + flatline) | KILL | Legible diffusion type violates the type law; the letters ignore the neon's bounce light (composited feel); gray-green haze background seams against the void page; delivered 16:9, not 1200×630. |

Delivery-spec failure across the set: 1376×768 heroes, one 512×382 "macro", one 1.89:1 "ultra-wide", nothing at 1200×630. The prompts' format specs were ignored because they were never stated as specs.

## Fidelity analysis — why the words failed

- "Fallen server rack rising upright" — models render named states, not motion; "fallen" won because it was the concrete state glued to the noun. v2 freezes terminal states in CAPS.
- "Embossed paper certificate" — no visual spec, so the wax-seal prior produced an envelope. v2 specs objects like a props master: a flat single sheet, fully open, gold hex anchored.
- "Blood red" / "resurrection green" — adjectives, not colors; the model supplied stock versions. v2 hex-anchors every hue twice (hex + real-world object).
- "Filled with… each holding" — a clone instruction. "Darkness" without prohibitions let daylight walk in. v2 adds variance clauses and bare-noun avoid lists.
- "Unnatural precision" — read as radial symmetry, producing 120° instrument clones.
- The style lock's "single rim light" died every time the prompt body itself named a second light noun. v2 moves lighting law into each prompt's body and forbids rivals in the lock.

## The slop taxonomy (ranked by lethality on a near-black site)

| Tell | At hero size | In darkness |
|---|---|---|
| 4-point sparkle glyph (provenance tattoo) | FATAL | FATAL — it glows on the void |
| Impossible light | FATAL | subliminal wrongness |
| Floating objects / no contact shadows | FATAL | barely visible |
| Palette drift (no hex anchor) | FATAL — brand law is hex-exact | FATAL even at 40px |
| Cloned repetition | FATAL | invisible until motion or crop |
| Composited feel (objects ignore light and reflections) | FATAL | masked by scrim |
| Object-state inversion | FATAL — the story is wrong | FATAL |
| Background ≠ void → page seam | FATAL | FATAL |
| Melted micro-detail | visible at 100% | hidden ≤800px behind scrim |
| Plastic sheen + HDR halos | visible | mostly masked by grain |

Pattern: the model paints light beautifully and physics not at all. Geometry was the lowest score on every frame (4–7).

## Retrial of the v2 law — SEALED WITH PATCHES

The Wordsmith's rewrite was cross-examined and sealed with these patches, now baked into `image_prompt.md` v2: base-flat + contact-shadow clauses (asset 2); natural falloff + mirror clauses (asset 3); brightness/spacing variance clauses (asset 4); edge-void, formless, narrow-band blend (asset 5); gold-hex wax seal + bone paper anchor (asset 6); exact 1200×630 + abstract-geometry wording + embedded filament (asset 7); daylight/windows/ambient-glow in the OPERA LOCK avoid-list; resolution floors; mandatory seed + verbatim description block.

Final authority over model-native artifacts stays with the 60-second corner hunt — the LOCK is the strongest promptable defense, not a guarantee.
