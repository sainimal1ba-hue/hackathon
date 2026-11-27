# WARPLAN — HEROKILL

**PS-WEB-01 · Mini-Cloud Hosting Platform · Clash of Commits (2026-12-04/05 · VIT Chennai)**

> One-line pitch: **HEROKILL — the mini-cloud you can watch die and resurrect in one click.**
> The mini-cloud we build: you push it live yourself, you poison it yourself, then you watch it resurrect within ten seconds and drag the timeline back to freeze the exact cause of death.

---

## 1. Battlefield summary (details in `intel.md`)
- 24h offline hackathon, clans of 4–5; three rounds: Round 0 anonymous idea deck (~120–150 clans survive) → Round 1 "The Raid" 24h build (top 8 advance) → Round 2 Arena Finals **crowned by audience vote**.
- Judged on six axes: feature surface / 24h feasibility / demo impact / differentiation / crowd appeal / team fit.
- Offline iron law: our own laptops + router LAN + projector; venue Wi-Fi is presumed dead; zero third-party APIs, zero AI inference, zero live interactive infrastructure.

## 2. Why this problem (Round 1 verdict: 46/60)
- The only problem where every hour buys theater instead of a learning curve: 98 tests, CI, Docker deploys are this team's daily life — all 24 hours go to polish and rehearsal.
- The quietest lane in the arena: Docker-heavy work scares off casual clans; half of those who dare die in container-in-container hell — we sidestep it by mounting the host socket.
- Every rival ships a "deploy button": the death theater and the resurrection timeline are unclaimed territory.

## 3. Core narrative: death and resurrection
"You push it live yourself → you poison it yourself → the platform screams → auto-rollback → the container resurrects → you drag the playhead back and freeze the cause of death."

**KILL SHOT (those 60 seconds)**: the judge personally poisons the version they personally deployed → the red wall blares → the whole crowd counts down aloud → 00:07 green-pulse resurrection → the playhead drags back and freezes on "it died on this log line." One hand kills, one hand pardons, the whole hall shouts — and the votes follow.

## 4. Final feature roster (Round 2 emperor verdict — see `round2-feature-war/emperor-verdict.md`)

### 4.1 TABLE STAKES (nine, deduplicated — everyone will have these; we do them harder)
| # | Feature | Execution essentials |
|---|---|---|
| 1 | git push is deploy | bare repo + post-receive hook, typed by the judge's own hand; pre-baked image layers masquerade as a hot start |
| 2 | Zero-config stack detection | scan composer.json / package.json / static files; a rules table emits the Dockerfile + process topology directly |
| 3 | Custom domain + HTTPS | pre-minted wildcard cert + local DNS override; the green lock lights offline |
| 4 | Health checks | polling + consecutive-failure threshold; heartbeats land in the timeline |
| 5 | Auto-rollback | a green image cached permanently; switch back in <10 s |
| 6 | Four chaos types | poison code / dependency bomb / memory leak / kill -9, all caged by cgroups |
| 7 | Death records | exit-code autopsy (137=OOM, 143=SIGTERM), numbered Death Certificates filed, appended to the SQLite event stream |
| 8 | Container status wall | big-type three-color grid, readable at thirty meters, 1 s WebSocket pushes |
| 9 | Log stream | grep-able stdout waterfall, same source appended to the event table |

### 4.2 SIGNATURE MOVES (five — they won't have, we will)
| # | Codename | From | One-liner | Demo moment |
|---|---|---|---|---|
| 1 | JUDGE'S TRIGGER | KILLSTREAK | the judge executes the kill personally and pardons personally | press resurrect amid the flashing red; the ten-second heartbeat returns |
| 2 | THREE-SECOND LIFT | ARCHITECTUS | the judge pushes personally; the lock lights in three seconds | the keyboard is in their hands; so is the impact |
| 3 | RESURRECTION WINDOW | FURIOSA | red wall fills the screen; the crowd chants ten, nine, eight | the timer freezes at 00:07; green-pulse resurrection |
| 4 | SCRUB THE INCIDENT | CHRONOS | drag the playhead back; the logs visibly run backwards (minimal scrubber) | terminal text rewinds in public; freeze on the death line |
| 5 | THE ROAR | FURIOSA | three numbered containers; the loudest shout gets executed | a rehearsal for the vote |

Executed (cut): the scale slider (admin-panel energy); 16x frame-by-frame time travel (downgraded to a replay appendix). The Wave-1 six-school cuts also stand: THE SÉANCE traffic replay (= building a second product), TWIN PARADE blue/green dual versions (5 hours for an invisible 200 ms), BRANCH PREVIEW triple parallel versions (triples on-stage state), APP STORE one-click starters (off-topic), true-random roulette (firing a random gun on stage), CRT scanline effect (pretty in screenshots, unreadable from the back rows). Full kill orders: `round2-feature-war/emperor-verdict-wave1-six-schools.md`.

### 4.3 STRETCH ARSENAL (unlocked only if all-green at hour 20; sacrificed in order; from the Wave-1 six-school Tier 2 verdict)
| # | Codename | One-liner | Hours |
|---|---|---|---|
| 1 | GATE OF GREEN | the repo's own test suite runs inside the build; red refuses to go live — "no green, no live" | ~4h |
| 2 | DEMO DIRECTOR MODE | hidden hotkeys jump between beats — a rehearsal rig, built early | ~2h |
| 3 | GREEN MEANS LIVE | synthetic traffic pulses green veins with the heartbeat; a rollback landing is a regression | ~3h |
| 4 | .herokill.yml contract | env / health check / rollback policy declared inside the repo — resurrection as contract | ~3h |
| 5 | THE CAGE | --cpus / --memory hard limits; deploy a fork-bomb app live, watch the gauges spike red, strangle it on the spot | ~3h |

## 5. 24-hour build order (Round 1 on-site execution)
| Phase | Milestone |
|---|---|
| H0–2 | Freeze the foundation: event-table schema + append-only boot logging; all four chaos types bare-running |
| H2–6 | Birth chain: push → hook → build → green light → lock; images pre-baked into the registry |
| H6–10 | Death chain: injection + threshold + RED CODE + Death Certificate |
| H10–14 | Resurrection chain: green-cache rollback + status wall + heartbeat graph |
| H14–17 | Timeline: minimal scrubber (log rewind + replay); full time travel decapitated on the spot |
| H17–18 | Script freeze: the three-minute beat sheet takes over; audio / certs / repos all pre-baked locally |
| H18–22 | Full-chain rehearsal into CI: including the judge-stage-fright contingency and the dead-man switch |
| H22–24 | Stress test, backup images, sleep |

Role split (4–5): A platform engineering (hook / build / domain, never touches UI) · B event stream + rollback engine · C frontend (status wall / scrubber / theater) · D chaos + autopsy engine · E director + judge interaction + pre-baked assets (with 4 members, E merges into A).

## 6. Demo script (three-minute beat sheet, FURIOSA military law)
| Time | Act | Content |
|---|---|---|
| 0:00–0:15 | COLD OPEN | black screen; one giant terminal line, `$ git push`; the status wall lights up cell by cell |
| 0:15–1:00 | THE HANDS | the judge pushes personally; log waterfall; the lock lights in three seconds — "deployed by <judge>" |
| 1:00–1:40 | GREEN GATE | liveness gating demo: the poisoned version is stopped by the green gate; traffic never blinks (the first death, silent) |
| 1:40–2:00 | THE MURDER | the judge presses the chaos-weapon card; RED CODE; the red wall blares |
| 2:00–2:40 | RESURRECTION | the crowd chants ten, nine, eight; rollback; 00:07 green-pulse resurrection; the timer freezes |
| 2:40–3:00 | AUTOPSY + REPLAY | read the Death Certificate aloud (died of OOM, lived 4 minutes 12 seconds); drag the playhead back; the logs rewind and freeze on the death line |
| Overtime | THE ROAR | if 5 minutes: three numbered containers, the loudest shout gets executed — a rehearsal for the vote, the finale |

(The 3-minute version cuts THE ROAR; the 5-minute version keeps it as the finale.)

**Audience-interaction fallback ladder**: planted teammates in row three "volunteer" → if the hall freezes, the MC presses the same attack personally (zero script loss) → ultimate fallback: a "die-hard" demo app on a timed self-destruct loop keeps dying and resurrecting on the status wall all night (chaos panel timed injections + resurrection counter) — the theater never goes dark; WS outage → the next beat boundary reloads the whole page (the timeline is already persisted; not a second is lost).

## 7. Round 0 deck (English, anonymous submission)
| Page | Title | Key points |
|---|---|---|
| P1 | Cover — HEROKILL | "The mini-cloud you can watch die and resurrect." (anonymous codename) |
| P2 | The problem | Deploying is fragile; every platform hides failure. We put failure on stage. |
| P3 | The obvious build | Push-to-deploy mini-cloud — what every clan will ship. |
| P4 | Our twist | Death & Resurrection: poison it live, watch the autopsy, resurrect in seconds. |
| P5 | Signature moves | JUDGE'S TRIGGER / THREE-SECOND LIFT / RESURRECTION WINDOW / SCRUB THE INCIDENT / THE ROAR |
| P6 | Architecture | bare repo + hook → Docker API + cgroup cages → Caddy wildcard TLS (pre-minted, offline) → WebSocket event bus → SQLite append-only timeline |
| P7 | The resurrection timeline | Every second recorded: logs, health, versions; scrub your incident like a video. |
| P8 | 24h build plan | H0–H24 phase table; CI-rehearsed failure drills; test-gated deploys. |
| P9 | Demo storyboard | The 3-minute beat table: cold open → judge's push → poison → countdown → 00:07 revival → autopsy. |
| P10 | War declaration | "You deployed it. You poisoned it. It's still standing. HEROKILL." |

**UPDATE 2026-11-27 — the official template supersedes this sketch.** The Round 0 submission must follow the official Google Slides template (8 slides, 10 × 5.625 in, "PPT or PDF · max 20 MB"): Cover (project title / one-line pitch / track / team) → Problem Definition → Proposed Solution → System Architecture → Feasibility & Scope → Impact Metrics → References & Attribution → Extra Slide. The ten-page sketch above folds into those eight; the produced deck lives in `to_submit_pdf/`, and the production knowledge in `pdf_generation/SKILL.md`.

## 8. Risk register
| Risk | Countermeasure |
|---|---|
| On-site docker build sinks into a swamp | images pre-baked into the registry on Dec 3; on failure auto-degrade to "pre-baked layer + diff layer" — the UI flow unchanged, the audience never knows |
| The death system dies on stage (won't poison / rollback sticks / judge freezes) | cgroup cages (memory cap + isolated network); a guaranteed green image standing by; injection failure degrades to kill -9 hard kill; if the judge freezes, the MC takes the knife |
| Blank timeline or runaway UI | append-only event table logged from boot; scrubber kept minimal; a pre-baked "golden incident" recording as backup |
| Venue Wi-Fi stone dead | fully local chain: pre-minted wildcard cert + DNS override; the green lock lights offline |
| Script overrun / forgotten lines | script frozen at hour 18, fixes only; one dedicated director; a timekeeper + three full run-throughs |

## 9. Six-axis self-check (the mirror before battle)
- **Feature surface**: 9 table stakes + 5 signature moves + 5 stretch weapons — a floor full of weapons.
- **24h feasibility**: the entire daily stack (PHP/JS/TS + Docker + CI); every move labeled real-engineering vs theater-wrapper.
- **Demo impact**: the 60-second KILL SHOT = personal execution + crowd countdown + freeze-frame autopsy.
- **Differentiation**: death theater + autopsy narrative + replay-any-second — unclaimed in this lane.
- **Crowd appeal**: the judge participates personally + the hall chants together + THE ROAR (a rehearsal for the vote).
- **Team fit**: CI / test discipline becomes "GATE OF GREEN" and deploy gating directly.

---

*Ruled by the Emperors of Rounds 1 & 2 (feature war in two waves: Wave 1 six-school draft roster → Wave 2 four-school final law; full battle history in `round2-feature-war/`); plan wars concluded 2026-11-27 — Final Laws adopted from `design/` · `workflow/` · `structure/` · `architecture/` · `publishing/`; scribed into law by the war room. Next battlefield: forge §7 into the official eight-slide deck and submit Round 0.*
