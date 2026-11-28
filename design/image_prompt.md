# HEROKILL — Image Generation Prompts (v2 — The Sealed Flow Law)

*Supersedes v1. Sealed 2026-11-28 by the Inquisitor–Wordsmith retrial: the seven v1 Flow outputs were forensically audited — 5 KILL, 2 FIX, 0 KEEP (full autopsy in `image_audit.md`) — and the prompt law was rebuilt. This file is the only prompt source of truth. Platform: Google Flow (labs.google.com/flow) — Nano Banana Pro for images; Omni Flash 1.2 / Veo 3.1 Lite for video (Veo 3.1 Fast/Quality retire 2026-12-05).*

## 1. Generation law (settings, non-negotiable)

- **Model:** Nano Banana Pro for all frames (supports 4:1 and 8:1 ultra-wide ratios).
- **Seed:** lock one seed for the whole asset family and record it here once chosen — SEED = (lock at first generation).
- **Consistency:** copy the description block verbatim between generations; up to 3 ingredient/reference images lock the look. Mandatory, not advice.
- **Resolution floor:** long edge ≥2000 px (heroes ≥2560 px). OG card exactly 1200×630. Native Flow sizes are rejected for hero use.
- **Palette:** fire-truck red `#FF1E27` · traffic-light green `#00FF7B` · seal gold `#C9A227` · bone `#F2F0EB` · void `#050505`. One accent hue per frame (red XOR green XOR gold). The only sanctioned two-hue assets: the divider and the OG card.
- **Aspect ratios:** heroes 16:9; certificate 4:3; divider 4:1 ultra-wide; OG 1200×630 (generate 16:9 composed crop-safe, crop in the DOM).

## 2. OPERA LOCK (append to EVERY prompt, never paraphrase)

> Pure #050505 black void fills most of the frame; matte surfaces; one physical light source with natural falloff; fine 35mm film grain. Avoid: text, letters, glyphs, watermark marks, starburst lens flares, sparkles, bokeh lights, HDR glow, plastic sheen, duplicated objects, orange tint, mint tint, people, daylight, windows, ambient glow, extra lamps.

## 3. Image prompt skeleton

`[SHOT: angle + distance] of one [SUBJECT: object, material, count, state in CAPS] in [SCENE: near-black context, ≥60% void], lit by [ONE LIGHT: physical source, visible in frame, position, beam color = fire-truck red #FF1E27 | traffic-light green #00FF7B | seal gold #C9A227, anchored to a real-world object], [PHYSICS: matte finish, hard contact shadow, resting on X, solids occlude light and haze, reflective surfaces mirror their neighbors], [CAMERA: 35mm deep focus | 100mm macro], {aspect ratio}. + OPERA LOCK`

## 4. The seven assets (sealed wording)

1. **Overture backdrop** (Act 01 hero, 16:9, ≥2560 px)
   "Wide shot from the auditorium of an empty black stage; one lone matte-black server rack standing UPRIGHT, base flat on the boards, hard contact shadow; a visible spotlight rig overhead beams a single emergency-red cone (#FF1E27, fire-truck red) through thin haze onto the rack; one faint red LED on its face; 90% of frame pure #050505 void; 35mm, deep focus, fine grain. + OPERA LOCK."
2. **Resurrection** (Act 05, 16:9)
   "Wide shot; the same rack standing UPRIGHT, base flat on the boards, hard contact shadow, under a single overhead beam of traffic-light green (#00FF7B); the beam pools on the floor with natural falloff, floor reflection grounded; haze thinning; rack LEDs green; everything else #050505 void; 35mm, deep focus. + OPERA LOCK."
3. **Autopsy** (Act 04, 16:9)
   "Top-down macro, 100mm; one brushed-steel motherboard lying FLAT on a brushed-steel autopsy table, grounded, hard contact shadow; three surgical instruments laid parallel, each a unique shape, irregular spacing; a single red surgical lamp above-left casts emergency-red light (#FF1E27) with natural falloff; the brushed steel softly mirrors the instruments; matte, fine grain. + OPERA LOCK."
4. **The house** (Act 07 background, 16:9)
   "Wide shot from the stage into black void; tiers of dark opera balconies receding into #050505, fully in shadow, deep focus; each seat edge catches one tiny steady green glow like an exit sign (#00FF7B), glows varying in brightness with irregular spacing; silhouettes remain pure black featureless shapes; a single weak green wash from the seats themselves, natural falloff; 35mm. + OPERA LOCK, with faces added to the avoid-list."
5. **Section divider** (all acts, 4:1 ultra-wide)
   "Ultra-wide 4:1; slow billowing formless smoke on pure #050505; emergency-red (#FF1E27) on the left edge, traffic-light green (#00FF7B) on the right edge, the two hues blending only in a narrow middle band, no third hue; the smoke thins to pure void at all four edges; matte, fine film grain, static camera. + OPERA LOCK."
6. **Certificate plate** (Act 04, 4:3, ≥2000 px)
   "Still life, 4:3; one flat single sheet of thick cream cotton paper (#F2F0EB) lying FLAT on black velvet, fully open; blind-embossed border and seal pressed into the paper; one matte gold wax seal (#C9A227), deep pressed impression, unlit; a single green candle at lower-left burns with traffic-light green light (#00FF7B) grazing the embossing; hard contact shadow; 100mm macro. + OPERA LOCK, with envelope and folds in the avoid-list."
7. **OG social card** (exactly 1200×630)
   "A monolithic slab of bone-colored (#F2F0EB) chiseled abstract geometry, cropped blocky forms, on solid #050505; a thin emergency-red filament (#FF1E27) embedded in the slab, terminating in one short traffic-light green segment (#00FF7B); faint haze; matte surfaces; 35mm. + OPERA LOCK." Generate 16:9 composed crop-safe for 1200×630; crop in the DOM.

## 5. Video prompt skeleton (official Flow anatomy)

`[4s|6s|8s], [CAMERA: locked-off | single named move]. [STATE A] → [STATE B]; [subject animation] + [one environmental animation]; [ONE light source, named, hue locked for the entire clip]. Mood: dark theater, slow, still. Ends on [held terminal state ≥1s, loop-ready]. Audio: [ambience], [one SFX]. Avoid: strobing, flicker, quick cuts, text, color shifts.`

## 6. Motion law for video (binding)

- Prompt motion ONLY between frames; re-describing frame contents confuses the model.
- One scene, one change per clip; chain clips by saving the last frame as the next start frame.
- A death lands as an instant single-frame cut — never ask a generator to fade or dim.
- Resurrection is a breaker tripping: the beam lands within the first half-second, the LED cascade completes under one second, then the frame holds steady green ≥1s.
- End every clip on a held terminal state; loop seams must be pixel-verified.
- Negative lists are bare nouns; no quotation marks anywhere in prompts.
- Audio: ambience as separate sentences, SFX explicit, dialogue in colon format (A says: ...). Site audio is muted by default.

## 7. Anti-slop prompting doctrine

1. One clip, one scene, one change.
2. Prompt motion only between frames.
3. States in CAPS at the sentence front (UPRIGHT, FLAT, DARK).
4. Every light has a body — name the physical source and its position.
5. One hue per state, anchored twice (hex + real-world object); hex alone drifts.
6. Negative lists are bare nouns, never "no" or "don't".
7. No quotation marks anywhere.
8. Physics phrases kill slop on contact: contact shadow, resting on, matte, fine grain, natural falloff; ban HDR, bokeh, sparkles, flares.
9. Consistency = same seed + verbatim repeated description block + ingredient images. Mandatory.
10. Design the last frame: a held state for chaining and DOM loops.

## 8. Acceptance — the 60-second slop check (before any image is committed)

1. **Corner hunt at 400%** — all four corners + center; any sparkle/star glyph → KILL.
2. **Picker test** — key light within ~10% of the exact hex; all four corners ≤ #0A0A0A.
3. **Name the light source** — no visible or implied emitter → KILL.
4. **Contact shadows** under every grounded object.
5. **Clone hunt** — any element repeated ≥2× at the same scale and rotation → KILL.
6. **Glyph hunt** — any legible character anywhere → KILL.
7. **Color-state law** — one accent hue; gold only on certificates; red+green only on the sanctioned plates.
8. **Squint test** — mush zones in an otherwise sharp frame → KILL.
9. **Physics** — reflections mirror neighbors; solids occlude light and haze; leaning objects have a pivot.
10. **In-situ test** — on a #050505 page at final size, 10 seconds, fresh eyes.
11. **Delivery spec** — long edge ≥2000 px (hero ≥2560), OG exactly 1200×630, no fake upscaling.

---

*Retrial record: `image_audit.md`. Hero animation law: `hero_animation.md`. War history: `animation_war.md`.*
