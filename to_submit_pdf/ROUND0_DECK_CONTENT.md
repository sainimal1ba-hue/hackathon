# HEROKILL — Round 0 Deck · Slide Copy (organizer template, content only)

*The exact words on the eight slides. The template structure is frozen (see README); this file is the single editing surface for content. Mirrored 1:1 into `HEROKILL_Round0_Deck.html`.*

---

## Slide 1 — Cover

- Eyebrow: Round 0 · Build Your Base — Anonymous Submission
- Title: **HEROKILL**
- Brand mark: flatline stroke that spikes alive at its end (red → green)
- Pitch: The mini-cloud you can watch die and resurrect.
- TRACK: Web & Applications — PS-WEB-01 · Build Your Own Mini-Cloud Hosting Platform
- TEAM: Anonymous — Round 0 codename: HEROKILL
- EVENT: Clash of Commits · IEEE RAS VITC Chennai · 4–5 December 2026

## Slide 2 — Problem Definition

**Headline:** Deploying is a gamble. Failure hides behind dashboards.

- Push-to-deploy platforms end at a green "deploy" button. When a container dies, you dig raw logs by hand.
- Rollback is manual archaeology — no record of what died, when, or why.
- PS-WEB-01 asks for build → run → isolate → monitor → auto-rollback. Most clans will ship the first two and a status page.
- What nobody builds: failure as a first-class object — recorded, replayable, survivable.

Kicker: The obvious build stops at the deploy button. We stop at the resurrection.

## Slide 3 — Proposed Solution

**Headline:** HEROKILL: push it, poison it, watch it come back.

- git push is deploy — bare repo + post-receive hook; stack detection emits the Dockerfile and process topology with zero config.
- Four chaos weapons — poison code, dependency bomb, memory leak, kill -9 — each caged by cgroups, so the blast never leaves the cage.
- Auto-rollback to the last green image in <10 s, target 00:07, fired the moment health checks fail.
- Every death files a numbered Death Certificate — exit-code autopsy: 137 = out of memory, 143 = SIGTERM.
- Signature moves: JUDGE'S TRIGGER · THREE-SECOND LIFT · RESURRECTION WINDOW · SCRUB THE INCIDENT · THE ROAR.

## Slide 4 — System Architecture

**Headline:** One append-only event spine, boot to autopsy.

Chain: git push (judge's own keyboard) → bare repo + post-receive hook (deploy on commit) → stack detector (composer.json / package.json / static) → Docker build (pre-baked layers) → cgroup cage runtime (memory + cpu caps) → Caddy (wildcard TLS, local DNS, offline)

Bus: WebSocket event bus — every log line, health probe and version change is appended once.
Sinks: status wall · killfeed · incident scrubber · death certificates.

- One source of truth: the same SQLite append-only timeline drives the wall, the killfeed, the scrubber and the certificates.
- The green lock lights offline — wildcard certificate pre-minted, DNS overridden locally; venue Wi-Fi is never touched.

## Slide 5 — Feasibility & Scope

**Headline:** Our daily stack. The 24 hours go to polish, not learning.

Build order: H0–2 event-table foundation, four chaos types bare · H2–6 birth chain · H6–10 death chain · H10–14 resurrection chain + status wall · H14–17 incident scrubber · H17–18 script freeze · H18–22 full rehearsals incl. judge-stage-fright contingency · H22–24 stress test, backup images, sleep.

- Stack: PHP / JS / TS + Docker + CI discipline — every demo move labeled real-engineering vs theater-wrapper.
- Images pre-baked into the local registry before on-site; a sinking build degrades to pre-baked + diff, the audience never knows.
- Scope: 9 table-stakes features done harder + 5 signature moves; stretch arsenal (GATE OF GREEN, THE CAGE) unlocks only if all-green at hour 20.
- Offline law: our laptops + LAN router + projector; zero third-party APIs, zero cloud.

## Slide 6 — Impact Metrics

**Headline:** Failure becomes data. Resurrection becomes theater.

| Metric | Meaning |
|---|---|
| ≤10 s | resurrection window, target 00:07 — rollback to the last green image |
| ≤3 s | push to live — pre-baked layers masquerade as a hot start |
| 4 | chaos weapons with zero blast radius — cgroup cages |
| 100% | deaths recorded — exit-code autopsy, numbered certificates |
| 30 m | status-wall legibility at distance, 1 s WebSocket pushes |
| 1 | judge's own hand executes the kill — and the hall counts down aloud |

## Slide 7 — References & Attribution

**Headline:** Built on boring, proven plumbing. Nothing else.

1. Docker Engine API — docs.docker.com — build, inspect, exec, cgroup caps
2. Caddy Server — caddyserver.com — reverse proxy, wildcard TLS via internal CA
3. Linux cgroups v2 — kernel.org — memory / CPU isolation cages
4. SQLite — sqlite.org — append-only event timeline, WAL mode
5. RFC 6455, WebSockets — event bus, 1 s status pushes
6. typed.js — typed.js.org — deterministic terminal self-typing

- Original work. All code, design and copy are the team's own, built during the 24-hour raid.
- Zero third-party APIs. No cloud, no AI inference, no external services — the platform runs fully offline on our own hardware.
- Anonymous submission. This deck carries a codename only, per Round 0 rules.

## Slide 8 — Extra Slide: The Demo

**Headline:** Three minutes. One kill. One resurrection. A hall that counts aloud.

| Time | Beat |
|---|---|
| 0:00 | Cold open — one giant line, $ git push; the status wall lights cell by cell |
| 0:15 | The hands — the judge pushes personally; the lock lights in three seconds |
| 1:00 | Green gate — the poisoned build is stopped silently; traffic never blinks |
| 1:40 | The murder — RED CODE floods the wall |
| 2:00 | The window — the hall counts: ten, nine, eight… |
| 00:07 | Resurrection — green pulse; the timer freezes at 00:07 |
| 2:40 | Autopsy + replay — the certificate is read aloud; the logs rewind; freeze on the death line |
| OT | THE ROAR — three numbered containers; the loudest shout executes the next kill |

Kicker: You deployed it. You poisoned it. It's still standing. HEROKILL.
