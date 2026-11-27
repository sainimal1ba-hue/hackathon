# AR-1 — THE CASTLE

> Architecture War · gladiator speech · fought 2026-11-27
> Fate: **CHAMPION — 51/60.** Refined into the Final Law in `winner-architecture.md` (adopts the Organism's event envelope, fold-not-store state, projections, per-room cursors + idempotency keys, effectors pattern).

---

# THE CASTLE — Nine Rooms, One Law

The Organism lives until it twitches. A castle is built to be besieged. HEROKILL is an estate — nine rooms, one-way water flow, every failure door labeled. Auditable at 3 a.m.; auditable by judges in ninety seconds.

## 1 · Component Map

```
git push ─▶ GATE (receive + stack sniff)
              │ build card
              ▼
            FORGE (docker build + image cache)
              │ image:sha
              ▼
            DUNGEON (cage + net + Caddy) ◀─ injects ── LOOKOUT (autopsy)
              │ pulse
              ▼
            INFIRMARY (poll + threshold)
              │ every room appends; nobody edits
              ▼
            CRYPT (SQLite, append-only WAL)
              │ 1 s fan-out
              ▼
            HERALD (WebSocket) ─▶ GREAT HALL (3-color wall + scrubber)

THRONE ◀── reads RED CODE from CRYPT ──▶ DUNGEON: rerun last green (<10 s)
```

Law: everything flows down to the Crypt; only the Throne commands back up.

## 2 · Three Walks

**Walk I — Birth (git push).** Gate receives the push into a bare repo; post-receive sniffs composer.json/package.json and mints a stack card. Forge builds on the host socket, tags the image with the git SHA, banks the layers in cache. Dungeon cages it — cgroup caps, private bridge network, Caddy route + DNS override. Infirmary polls; N green pulses flip it GREEN. Every step lands in the Crypt; Herald paints the wall.

**Walk II — Death.** Lookout injects poison code, a dependency bomb, a memory leak, or kill -9 — inside the cage, blast radius zero. Infirmary's threshold trips: RED CODE appended; Herald pushes red within one second. Lookout reads the exit code — 137 OOM, 143 SIGTERM — and files a numbered Death Certificate.

**Walk III — Resurrection.** Throne watches the Crypt, not the wire. On RED CODE it commands Dungeon: bury the corpse, rerun the last green cached image. No rebuild — that is the <10 s budget. Infirmary confirms the pulse; RESURRECTED appended; the scrubber replays the death backwards.

## 3 · Event Schema Sketch

`events(id PK, ts, room, kind, repo, deploy_id, exit_code?, detail JSON)` — INSERT only; no UPDATE, no DELETE; WAL mode; single writer. Kinds: PUSH, BUILD_OK, DEPLOY, TICK, CHAOS, RED_CODE, ROLLBACK, RESURRECTED, AUTOPSY. Herald messages: HELLO (snapshot), WALL (cell + color), TICK, EVENT, RED_CODE, AUTOPSY, RESURRECTED.

## 4 · Walls & Swords — Isolation

Every repo runs in its own bridge network (no shared bridge), under cgroup v2 CPU/memory hard caps (THE CAGE), as a non-root user. The platform daemon: an unprivileged host user in the docker group (root-adjacent — we admit that out loud). Host socket, never docker-in-docker: one kernel, one daemon, the CI-runner pattern; DinD demands a privileged container and nested storage — a grenade in the cellar. Lookout touches only caged PIDs. Caddy edges the castle with a pre-minted wildcard cert + local DNS override — no ACME roulette live.

## 5 · If a Room Falls

- **Gate:** pushes bounce; running rooms untouched; monitoring + chaos demo still stands.
- **Forge:** no new builds; cached images carry the rollback story.
- **Dungeon:** the honest worst case — cells go RED while Crypt, Herald, Hall live on; resurrect when the daemon returns.
- **Infirmary:** Herald paints AMBER — silence is not green. Throne rolls back only on explicit RED CODE, never on absence.
- **Crypt:** it is a WAL file — restart, replay, resnapshot. The castle pauses; it does not fall.

Rooms share nothing but the Crypt. No cascade.

## 6 · Why-Not List

- **k8s:** a second product to debug in 24 offline hours; illegible to judges.
- **Docker-in-docker:** privileged, nested overlayfs, slow — host socket wins.
- **Redis/RabbitMQ:** another daemon to babysit offline; WAL + a Herald loop covers 1 s pushes, and it is one file to back up.
- **Postgres:** a server, migrations, ceremony — for an append-only stream, SQLite is the exact shape.
- **Nginx:** config ritual; Caddy is one file, and the spec whispers its name.

## 7 · Mapping — Spec & Clan

Spec verbs: **builds** → Gate + Forge · **runs** → Dungeon · **isolates** → Dungeon cages + Lookout's blast radius · **monitors** → Infirmary + Crypt + Herald + Hall · **auto-rolls back** → Throne. Stretches: GATE OF GREEN at the Gate, GREEN MEANS LIVE as Lookout's benign twin, THE CAGE as the Dungeon's bars.

Clan of five: **Gatekeeper** (Gate/Forge), **Jailer** (Dungeon, Caddy, DNS), **Nurse** (Infirmary/Lookout), **Scribe** (Crypt/Herald), **Monarch** (Throne/Great Hall + demo choreography). One folder, one owner; merge by contract, not by prayer.

## 8 · Kill Strokes — Why the Organism Dies

- **3 a.m. debuggability:** the loop twitches — which organ? Here the event names the room; the exit code names the cause.
- **Judge legibility:** judges can walk a map; nobody grades a single function called "the organism."
- **Error isolation:** one throwing reducer convulses the whole body; a dead room is quarantined behind walls while the Crypt keeps the story.
- **Clocks:** hooks, polls and rollbacks keep different tempos; one loop conflates urgency — rooms keep their own watches.
- **The clan:** five builders cannot share one brain. They can hold nine rooms.

Push. Cage. Kill. Resurrect. Audited stone by stone. **The Castle stands.**
