# Round 2 — Wave 1: The Six-School Preliminary War（六学派海选 · 第一波裁决档案）

*Wave 1：六个战略学派先行海选，产出初版名单、施工序与完整 5 分钟剧本。本档为战史档案——随后 Wave 2 四学派终审定下最终军法（见 `emperor-verdict.md`），`warplan.md` 以终审为准。两套代号体系并存：如 JUDGE'S TRIGGER ≈ 评委之铳，SCAR-WALL ≈ 伤疤墙计分板。*

参战演讲存档：`01-centurion-table-stakes.md` · `02-necromancer-death-resurrection.md` · `03-showman-demo-theater.md` · `04-architect-infra-depth.md` · `05-merchant-developer-experience.md` · `06-chaos-mage-audience-arena.md`

---

## SCOREBOARD

| School | Features pitched | Avg WOW | Avg COST-efficiency | Verdict line |
|---|---|---|---|---|
| CENTURION | 8 | 5.6 | 8.6 | Hired as the floor and nothing more — right about every stake, thrilling about none; the floor prevents losing votes, it wins zero. |
| NECROMANCER | 7 | 8.6 | 7.4 | The autopsy IS the product's soul — Certificates, Verdicts, Graveyard and Last Rites are drafted; the Séance is a second product we cannot afford in 24h. |
| SHOWMAN | 8 | 8.3 | 8.5 | Correct that the projector is the product — Button, Klaxon, Scrubber and Director Mode are drafted — but only because Architect's spine makes the theater cross-examination-proof. |
| ARCHITECT | 7 | 8.4 | 6.9 | The Vault and the Coroner are the truth engine — the only timeline in the room backed by recorded reality; everything else pitched is a tar pit wearing a roadmap. |
| MERCHANT | 7 | 8.0 | 7.7 | One slim CLI beat buys the engineers in fifteen seconds; the Store, branches and YAML are a second roadmap wearing our jersey. |
| CHAOS MAGE | 6 | 9.2 | 8.3 | Highest WOW in the war and the reason we win the audience vote — drafted in full, on our hardware only, with your own fallback (Refuses-to-Die) standing guard all night. |

## THE FINAL ROSTER（初稿）

### TIER 0 — THE FLOOR（table stakes，~30 team-hours）
- Clone-to-Live Intake with staged launch sequence: paste URL → clone (cache-warmed) → detect → build (output streamed live) → probe → route → live, per-stage timers — ONE stack (Node), no buildpacks (~7h)
- Wildcard routing + port wiring: Caddy on-demand subdomains off the pre-minted cert + local DNS override (~4h)
- Per-app Docker network quarantine — neighbors can't curl or read each other's env; the proof line ships inside every Death Certificate (~2.5h)
- Env vars KV panel: edit → redeploy, injected at container create (~2.5h)
- Bulletproof log stream: WebSocket attach that never drops a line, keeps scrolling through death and rebirth (~4h)
- Health checks as referee: real HTTP probe polling → green/amber/red state machine with N-consecutive-fail verdict logic (~4h)
- AUTO-rollback in <5s (the Coroner core): every deploy retains a tagged image; probe verdict → stop new, start old, repoint — never revert-and-rebuild (~5h)
- Restart-on-crash: `--restart unless-stopped` — free, never hand-rolled (~0.5h)
- Mission Control: ONE dark projector-first screen — huge type, live status grid, per-container CPU/RAM gauges, deploy-history strip (~5h)

### TIER 1 — THE KILLERS（~48 team-hours）
- THE RESURRECTION TIMELINE, VAULT-BACKED (Architect × Showman): health events, resource stats, revision markers persisted in SQLite and replayed over WS; drag back through the murder, release at green; rivals animate, we time-travel (~12h)
- THE BIG RED POISON BUTTON + KLAXON (Showman): safety cover, 3-second arm-hold, deterministic poison via a real /kill route (~5h)
- DEATH CERTIFICATES (Necromancer): verdict stamp (POISONED DEPLOY / OOM / CRASH LOOP / FAILED HEALTH CHECK / MANUAL MURDER), exit code, OOM bit, last 50 log lines as last words, murder-weapon `docker diff` (~7h)
- THE GRAVEYARD (Necromancer × Chaos Mage): ONE tombstone wall for every death from any killer; click tombstone → full autopsy → one-click RESURRECT (~6h)
- THE ASSASSIN'S LAPTOP + KILL FEED + DOOM SLIDER (Chaos Mage): second laptop on a wired LAN island handed to a volunteer; attack pool targets victim containers only, never the brain (~8h)
- THE REFUSES-TO-DIE APP (Chaos Mage): a cursed starter dying every 30 seconds, resurrected forever, mortality counter ticking — the volunteer-proof fallback (~3h)
- LAST RITES (Necromancer × Showman): rollback ceremony — FREEZE → SNAPSHOT (`docker commit`) → RESTORE (~3h)
- SCAR-WALL (Chaos Mage): closing scoreboard — uptime %, fastest resurrection, deaths survived, TOP ASSASSIN OF THE NIGHT (~3h)
- herokill CLI, slim (Merchant): `deploy` / `kill` / `rollback` / `status` — first on the hour-16 cut list (~4h)

### TIER 2 — THE STRETCH（only if hour 20 arrives green；~10h）
- DEMO DIRECTOR MODE (Showman): hidden conductor hotkeys to jump scripted beats — build early as the rehearsal harness (~2h)
- GREEN MEANS LIVE (Showman): synthetic traffic pulses green across the grid; dies with the murder, returns with the rollback (~3h)
- GATE OF GREEN (Architect): repo's own test suite runs inside the build; red aborts the deploy — "no green, no live" (~4h)
- .herokill.yml (Merchant): env, health check, `rollback: on-health-fail, keep: 3` declared in-repo — resurrection as contract (~3h)
- THE CAGE, full (Architect): hard `--cpus`/`--memory` limits per app plus a live strangle beat on a busy-loop app (~3h)

### THE KILLED
- THE SÉANCE — proxy traffic recording + sandbox replay is a second product; its soul already lives in the Vault-backed scrubber.
- TWIN PARADE — a live traffic slider is deep proxy surgery for diff-6 wow; the crowd can't see 200ms of downtime from thirty feet.
- BRANCH PREVIEW ENVIRONMENTS — three versions alive at once triples on-stage state to babysit.
- THE APP STORE — off-brief for the engineer judges; its soul survives as the pre-warmed three-repo shortlist in the intake beat.
- TRUE RANDOM ROULETTE — randomness on stage is a loaded gun aimed at our own demo; the Doom Slider keeps the ritual, we keep the determinism.
- TERMINAL VELOCITY CRT — scanlines are for screenshots; severity colors and huge mono type already read from the back row.
- THE MORGUE (as a second wall) — one Graveyard, one truth pipeline: every kill source feeds the same certificate → tombstone → resurrection.
- NECROLOG / AUTOPSY TABLE / THE BUTLER — absorbed into Death Certificates and the Kill Feed.
- BUILDPACKS FOR ARBITRARY STACKS / GRAFANA / AUTH / MULTI-TENANCY / BILLING / SSH PUSH — every trap the Centurion flagged.

## THE 24H BATTLE BUDGET（初稿施工序）

Roles (5 builders; at 4 members D absorbs the cursed-app and Kill Feed work, cuts fire early): **A — INFRA** (Docker/Caddy/networks/rollback engine, never touches UI) · **B — STATE** (probe state machine, Vault recorder, WS event bus) · **C — FRONTEND** (Mission Control, scrubber, theater) · **D — FULL-STACK** (deploy API, certificates, Graveyard, Kill Feed) · **E — OPS/DEMO** (assassin laptop, cursed app, CLI, rehearsal harness).

- **H0–H2 (all):** freeze the contracts — API surface, WS event schema (this bus IS the product), Vault schema, Caddy config, repo shortlist. No pixels before hour 2.
- **H2–H6:** vertical slice — deploy → route → live → logs (A+B+D), dashboard shell + status grid (C), cursed app + cache warming (E).
- **H6–H10:** death engine — probes → verdict → auto-rollback from retained image (A+B), gauges + state badges (C), certificate minting (D), assassin-laptop skeleton + victim-only attack pool (E).
- **H10–H14:** Vault recording + scrubber (B+C), Graveyard + one-click resurrect (D), Poison Button + Klaxon (C), quarantine + env panel + Last Rites snapshot (A), Kill Feed + Doom Slider mapping (E).
- **H14–H16:** integration freeze — full murder → autopsy → rollback → scrub walkthrough on the actual stage hardware; tag the build.
- **HOUR 16 CHECKPOINT (the law):** run the entire 5-minute script with a stopwatch. Cut order: (1) herokill CLI, (2) all of Tier 2 plus the full Cage, (3) Doom Slider → three fixed attack buttons, (4) Last Rites animation → green flash + counter, (5) Scar-Wall → static summary card. Never cut: Poison Button, Death Certificates, auto-rollback, Assassin laptop. If the scrubber misses the bar, simplify to health-state replay first. At 4 builders (72 team-hours vs 78) these cuts close the gap.
- **H16–H20:** hardening — WS reconnect discipline, zero-log-loss test under kill storms, local audio files, DNS/cert drill on the actual projector + island laptop, offline lockdown, pre-bake every image.
- **H20–H23:** three timed dress runs; plant the fallback volunteer in row 3; drill the nightmares — volunteer freezes, WS drop mid-murder, klaxon feedback loop.
- **H23–H24:** freeze, tag, snapshot all images, charge the island laptop, rotate sleep.

## THE 5-MINUTE CROWN SCRIPT（初稿）

- **0:00–0:15 — COLD OPEN:** "This is HEROKILL. One machine, no internet, every pixel wired to a real Docker API call." No slides.
- **0:15–0:45 — THE CROWD DEPLOYS:** a volunteer picks repo A/B/C; the staged launch checklist rolls under a T-minus timer; their app goes LIVE on a named subdomain. *Fallback: operator picks C — five dead seconds, no more.*
- **0:45–1:00 — GREEN LIFE:** gauges pulse, logs scroll: "isolated, healthy, yours."
- **1:00–1:25 — THE MURDER:** flip the safety cover, three-second arm, PRESS — klaxon, red vignette, screen shake, failing probe stamped in giant type.
- **1:25–1:55 — THE AUTOPSY:** Death Certificate mints live — verdict stamp, exit code, last words; `docker diff` lights up the murder weapon; one click to raw inspect JSON.
- **1:55–2:15 — THE RESURRECTION:** FREEZE → SNAPSHOT → RESTORE, bell toll, green floods, "v3 → v2 in 1.9 seconds" stamped on screen.
- **2:15–2:40 — THE TIMELINE:** drag the scrubber back through the murder — recorded real state flips back to the moment of death — release at green.
- **2:40–3:35 — CHAOS CROWN (the peak):** Assassin's Laptop to a volunteer — "Your turn. Kill something." Handle hits the Kill Feed; then the Doom Slider: the crowd chants "FIVE" — kill + spike + OOM simultaneously, every tile red, then every tile green, total resurrection time stamped.
- **3:35–3:55 — THE REFUSES-TO-DIE REVEAL:** "That cursed app behind me has died nine times since we started. It has never been down."
- **3:55–4:20 — THE GRAVEYARD:** pan the tombstones; one-click resurrect; fifteen seconds of `herokill rollback` in the terminal for the engineers.
- **4:20–4:50 — THE SCAR-WALL:** uptime %, fastest resurrection, deaths survived — TOP ASSASSIN OF THE NIGHT crowned live.
- **4:50–5:00 — CLOSE:** "You deployed it. You tried to kill it. It's still standing. HEROKILL."

**Interaction fallback ladder:** planted teammate in row 3 "volunteers" if the room freezes; if nobody takes the laptop, the operator fires the same attacks and the script loses zero seconds; if even that fails, Refuses-to-Die has been carrying the story all along. A WS drop mid-murder reloads the view at the next beat boundary — the timeline is recorded, so nothing is ever lost.

## THE BRAND

**HEROKILL** — the self-hosted mini-cloud where anyone can murder a deployment and nothing stays dead: poison it live, watch the autopsy, resurrect in under five seconds.
