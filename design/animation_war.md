# The Animation War — The Emperor's Verdict

*Fought 2026-11-28. Four director-gladiators fought to the death for the right to direct the homepage hero animation — frame-by-frame generation in Google Flow, Awwwards level. Judged on six axes (0–10): WOW · BRAND · BUILD24 · DIFF · CRED · FIT. Binding law during battle (from the Inquisitor's retrial): a death lands as an instant single-frame cut; resurrection is a breaker tripping (beam <0.5s, LED cascade <1s, hold ≥1s); loop seams pixel-verified; red and green never share a frame.*

## Scoreboard

| Gladiator | WOW | BRAND | BUILD24 | DIFF | CRED | FIT | Total |
|---|---|---|---|---|---|---|---|
| DG-4 THE SHOWMAN — THE CHANT | 10 | 9 | 7 | 9 | 8 | 10 | **53 / 60** |
| DG-3 THE MOTION ARCHITECT — DEAD RECKONING | 8 | 10 | 10 | 7 | 8 | 7 | 50 / 60 |
| DG-2 THE STAGE DIRECTOR — THE KILL LEVER | 9 | 10 | 6 | 9 | 6 | 9 | 49 / 60 |
| DG-1 THE CINEMATOGRAPHER — THE FLATLINE PROSCENIUM | 8 | 9 | 8 | 7 | 8 | 7 | 47 / 60 |

## The gladiators

- **DG-1 THE FLATLINE PROSCENIUM** — one locked-off master shot; light is the only actor; the two-second black hold; the loop seam IS the death. Fallback: stills + CSS light-cone ≈ 80% of the shot.
- **DG-2 THE KILL LEVER** — a stagehand silhouette walks the boards and pulls the lever that kills the machine, mirroring the product's JUDGE'S TRIGGER; the red act plays once, then the green loop breathes. Fallback: hard cuts between locked stills + DOM floods.
- **DG-3 DEAD RECKONING** — the visitor's scroll is the defibrillator; three micro-clips (red loop / flood / green loop), pixel-verified seams, 1.7MB AV1, poster = reduced-motion fallback, architecture that never depends on video.
- **DG-4 THE CHANT** — the hero is counted down aloud; VIGIL / DEATH / REBIRTH; the kill frame freezes and gets a Seal Gold certificate stamp bearing the visitor's real timestamp; the room chants.

## Kill blows that decided the war

- **Against DG-1:** the cooling ember is a fade in costume (unlawful death); the two-second black reads as "the video crashed" on a projector's grey-crush floor; a 14s master with a mid-shot light-state change is generation roulette. *DG-1's redemption:* the death was moved out of the video — a machine-cut layer swap between stills; Flow is only ever asked to pulse, drift, and hold.
- **Against DG-2:** a walking human is AI video's loudest slop tell at forty feet; "LEDs cascade like breath returning" is an unlawful slow bloom; a stagehand makes the audience witnesses when the law wants them killers. *DG-2's redemption:* a backlit silhouette — no face, no resolvable fingers — with the lever locked in both endpoint stills; the micro-clip split adopted.
- **Against DG-3:** playbackRate mapped to scroll velocity hands the breaker's timing to the visitor's wrist — the law violated live on stage, un-QA-able; 720p AV1 is mud at forty feet; the resting loop's "flicker once" is decorative motion. *DG-3's concession:* the flood re-cut to fixed-rate breaker timing; the death was never in the video.
- **Against DG-4:** a 6s red→green interpolation forces red and green to share frames — a birth defect; 18s and 6MB is a hostage negotiation; the loop opened on green VIGIL when the Overture law says the visitor dies first. *DG-4's concession:* the resurrection was never the video's job — the DOM 400ms flood is the breaker; the video re-specs to beam-at-frame-one; the chant needs zero audio.

## The decisive argument for THE CHANT

FIT is the axis the finals are crowned on — the finals are decided by audience vote — and no rival competes there: a countdown a live hall obeys unbidden, a death the visitor performs, a kill frame gold-stamped with their own real timestamp — screenshot bait that campaigns for the vote after the demo ends. Its wounds (BUILD24 weight, sync risk) are engineering problems, and engineering was looted from DG-3's corpse. Nobody can loot the roar.

## Adopted from the fallen (now law)

From **DG-3 DEAD RECKONING**: the entire engineering rig — micro-clip economy (one scene, one change, 4–6s, cheap retries), ALL state transitions as preloaded-layer steps(1) edits, pixel-verified endpoints, poster = reduced-motion fallback, IntersectionObserver pause offscreen, fixed-rate playback (never scroll-scrubbed video), architecture that never depends on the video.

From **DG-1 THE FLATLINE PROSCENIUM**: the void beat — a half-second dead-black hold before the breaker slams; the locked-off frame discipline.

From **DG-2 THE KILL LEVER**: the once-only death — the red act fires once per visit, then the hero parks on the green vigil; a machine resurrected forever must not also die forever. The stagehand himself was cut: humans stay optional and out of the hero.

**CHAMPION: DG-4 — THE CHANT (53/60).** Final Law: `hero_animation.md`.
