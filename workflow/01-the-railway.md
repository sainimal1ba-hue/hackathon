# WF-1 — THE RAILWAY

> Workflow War · gladiator speech · fought 2026-11-27
> Fate: **CHAMPION — 48/60.** Refined into the Final Law in `winner-workflow.md` (adopts the War Room's battle rhythm, board law, triage rule, vetoes, sleep floor, dev-lane rehearsal and THE ROAR).

---

# THE RAILWAY: WE WIN BEFORE THE DOORS OPEN

The War Room improvises. The Railway arrives with the track already laid. In a 24h offline arena with a crowd-vote finale, genius is not the weapon — preparation is. Every hour rivals spend debugging, we spend performing. Here is the doctrine.

## 1. PRE-EVENT TIMELINE — RAILS BEFORE THE TRAIN

- **Nov 27–28:** Golden repo frozen — HEROKILL skeleton, Laravel event schema, SQLite stream, WebSocket channels. Round 0 deck locked on the official anonymous template, under 20 MB, submitted and verified on the portal.
- **Nov 29:** Docker images pre-baked — php-fpm, Caddy, chaos toolkit, autopsy bench — tagged `dec3-gold`.
- **Nov 30:** Wildcard cert pre-minted, stuffed into the deploy image. DNS override kit scripted: one command flips every demo laptop to `*.herokill.offline`; green lock verified with the network cable pulled.
- **Dec 1:** Demo repos authored — four premeditated murders: poison code, dependency bomb, memory leak, `kill -9`. Each one `git push` away from RED CODE.
- **Dec 2:** Audio cut, normalized, committed — RED CODE alarms, the 00:07 resurrection chime, THE ROAR.
- **Dec 3:** FULL DRESS REHEARSAL — eight-hour clock, all five roles, real gates.

## 2. THE 24H RUNBOOK — GATES, NOT HOPES

- **H0–2 Foundations:** schema migrated, Docker network up. **GATE 1:** clean deploy from golden repo, zero edits.
- **H2–6 Birth chain:** post-receive hook → host-socket Docker → Caddy → offline green lock. **GATE 2:** a stranger's laptop sees the lock.
- **H6–10 Death chain:** three chaos weapons live, cgroups caging the blast radius.
- **H10–14 Revival chain:** auto-rollback under 10 seconds, resurrection, exit-code Death Certificates.
- **H14–17 Timeline scrubber:** SCRUB THE INCIDENT, frame-perfect replay.
- **H17–18:** Script freeze.
- **H18–22 Full-chain rehearsal:** JUDGE'S TRIGGER end to end, under the clock.
- **H22–24:** Stress test, triple backup, mandatory sleep rotation.

**FREEZE RULE AT H18:** no features, no refactors, no quick fixes. Only documentation of failure. If it wasn't rehearsed, it doesn't exist.

## 3. REHEARSAL PROTOCOL — DRILL THE DISASTER

Three full-chain runs: Dec 3 dress rehearsal, H18–20 arena run, H20–22 encore with chaos doubled. **Passing means:** push→kill→resurrect→scrub in one take, under time, zero console heroics. Since Nov 28, GitHub Actions runs the failure drills nightly on a runner with the Docker socket — inject, detect, rollback, assert stream and certificate output. The machine rehearses while we sleep. Every crash at 2 a.m. already died in CI at home.

## 4. ROLES & HANDOFFS

- **A — Platform:** hooks, Docker, Caddy. Owns the green lock.
- **B — Stream & rollback:** append-only SQLite, rollback engine.
- **C — Frontend:** timeline scrubber, dashboard.
- **D — Chaos & autopsy:** weapons, Death Certificates.
- **E — DIRECTOR:** owns the script, the clock, the judges' line of sight — and the DEAD-MAN SWITCH: pre-baked recovery repos and media that restore any failed beat in 60 seconds. E never codes; E watches the arena and calls the gates.

Handoffs happen at gates only. Nobody crosses tracks without the director's call.

## 5. GIT & ASSET DISCIPLINE

Main branch is sacred — only gate-passing merges, conventional commits. Every pre-baked asset — images, certs, audio, demo repos — versioned as SHA-tagged releases. Backups: gold snapshot at H22 and every three hours after — two USB keys, one bare clone on a spare laptop. If the hall burns down, we rebuild from a backpack.

## 6. FATIGUE & FAILURE LADDER

**3 a.m. protocol:** no solo debugging past 20 minutes — rubber-duck to E; if it resists, fall back to the rehearsed path. Document the failure, don't fight it. **Sacrifice order:** stretch goals die first — GATE OF GREEN, then DEMO DIRECTOR MODE, then `.herokill.yml`; THE CAGE and GREEN MEANS LIVE only if H18 was flawless. The kill-and-resurrect loop is never sacrificed. **Demo morning:** wake, shower, eat, 90-minute final rehearsal, voice warmed for THE ROAR.

## 7. KILL STROKES — WHY THE WAR ROOM DIES

The War Room doctrine — parallel squads, live task boards, adapt-over-plan — is beautiful, and fatal. Offline, in 24 hours, adaptation is a tax, and time is the one currency you cannot mint. Their squads collide over one shared codebase; their task board becomes triage; their pivots burn the hours we spent rehearsing the THREE-SECOND LIFT. And the finale is a CROWD VOTE. Crowds don't vote for your pivots. They vote for THE ROAR — the RESURRECTION WINDOW at 00:07 that lands every time, because it landed every night in CI. Improvisation hopes. The Railway guarantees. Champions aren't made in the arena — they arrive already crowned.
