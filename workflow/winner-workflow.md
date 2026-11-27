# HEROKILL — The Winning Workflow (Final Law)

*Champion: THE RAILWAY (48/60), refined with the spoils of THE WAR ROOM. The doctrine in one line: the Railway guarantees, the War Room decides — arrive already crowned, and if the arena dares you, decide like you rehearsed it.*

## I. Pre-event prep (dated, absolute)
- **Nov 27–28:** Golden repo frozen — skeleton, Laravel event schema, SQLite event stream, WS channels. Round 0 deck locked on the official template (<20 MB), submitted **and verified**. Nightly CI failure drills begin (inject → detect → rollback → assert stream + certificate).
- **Nov 29:** Docker images baked, tagged `dec3-gold` — php-fpm, Caddy, chaos toolkit, autopsy bench.
- **Nov 30:** Wildcard cert pre-minted; DNS override kit scripted — one command flips demo laptops to `*.herokill.offline`; green lock verified **with the cable pulled**.
- **Dec 1:** Four premeditated murders authored as demo repos, each one `git push` from RED CODE — poison code, dependency bomb, memory leak, `kill -9`.
- **Dec 2:** Audio cut, normalized, committed — RED CODE alarms, 00:07 resurrection chime, THE ROAR.
- **Dec 3:** **FULL DRESS REHEARSAL** — 8-hour clock, five roles, real gates. Then sleep.

## II. Roles, handoffs, vetoes
A — platform/lock (**technical veto**: protected-core sign-off). B — stream/rollback. C — frontend/wall/scrubber. D — chaos/certificates/autopsy. E — DIRECTOR: script, clock, judges' line of sight, the dead-man switch, **demo veto after H17**. E never codes. Handoffs at gates only. Two kings, two thrones, no overlap.

## III. The board
Painter's tape; lanes **READY / KILLING / DEAD**; one card = one demo-able thing. **Done means demoed** — someone who didn't build it makes it work in front of eyes. WIP: one card per gladiator, three per squad. Red BLOCKED sticker gets a body within ten minutes.

## IV. The 24h runbook
- **H0–2** Foundations → **GATE 1:** clean deploy from golden repo, zero edits.
- **H2–6** Birth chain → **GATE 2:** a stranger's laptop sees the green lock.
- **H6–10** Death chain (weapons live; cgroups cage the blast) → **GATE 3:** RED CODE → rollback <10 s.
- **H10–14** Revival chain (00:07 resurrection, Death Certificates) → **GATE 4:** full kill-and-resurrect.
- **H14–17** Scrubber frame-perfect → **GATE 5:** scrubber on the projector.
- **H17** SCRIPT FREEZE; E's demo veto armed.
- **H18–22** Full-chain judge's-trigger rehearsals under the clock — on the **dev lane** while Platform stress-tests. Encore run with chaos doubled.
- **H22–24** Stress test, triple backup, sleep rotation. Demo morning: wake, shower, eat, 90-minute final rehearsal, voice warmed.
- **FREEZE RULE (H18):** no features, no refactors, no quick fixes. Only documentation of failure. If it wasn't rehearsed, it doesn't exist.
- **THE KILL SHOT CORE — never renegotiated at any checkpoint:** git push → green lock offline; RED CODE → auto-rollback <10 s; resurrection at 00:07; the scrubber. All else is weather.

## V. Checkpoints & 3 a.m. triage
Every two hours: ten minutes standing at the board. Three questions — *What's dead? What's bleeding? What do we cut or keep?* Gates re-slice scope, reassign bodies, may move the next gate — never the core.
**3 A.M. TRIAGE (60 seconds, three buckets):** touches the core → Platform drops everything, two-person assault; on the sacrifice ladder → cut **now**; cosmetic → Theater absorbs it into the act ("Chaos, ladies and gentlemen — watch the rollback"). No solo debugging past 15 minutes after 2 a.m.; no new architecture after 2 a.m., ever.

## VI. Rehearsal protocol
Three full-chain runs minimum: Dec 3 dress, H18–20 arena, H20–22 encore with chaos doubled. Nightly CI drills since Nov 28 — the machine rehearses while we sleep. Rehearse on the dev-lane copy; production lane untouched mid-build. Passing = one take, under time, zero console heroics.

## VII. Fatigue, rotation, sleep
Two-hour sleep floor per gladiator, **scheduled not earned**; Theater sleeps first while Platform builds the death chain. Real food at checkpoints. The 4 a.m. wall gets boring work: certificate copy, polish, pre-baked assets. THE ROAR at every gate passed and every sub-ten-second rollback.

## VIII. Sacrifice ladder (dies first → last)
1. Demo Director Mode → 2. Gate of Green → 3. `.herokill.yml` + The Cage (shown pre-configured, never built live) → 4. Console polish/branding → 5. Extra chaos payloads (keep poison code + `kill -9`). **NEVER:** green lock, rollback <10 s, 00:07, scrubber, pre-baked backup.

## IX. Git & asset discipline
`main` is sacred — gate-passing merges only, conventional commits. Every pre-baked asset a SHA-tagged release. Gold snapshot at H22, then every 3 hours. Two USB keys + one bare clone on the spare laptop.

## X. The dead-man switch
E watches the arena, never the code: pre-baked recovery repos and media restore any failed beat in 60 seconds.
