# AR-2 — THE ORGANISM

> Architecture War · gladiator speech · fought 2026-11-27
> Fate: FELL — 46/60. Its heart became the champion's: event envelope + typed taxonomy, fold-not-store state, timeline-as-projections, per-subscriber cursors + idempotency keys, effectors pattern.

---

# THE ORGANISM — one heart, one log, one loop

Everything else is a limb.

## 1. THE ONE LOOP

```
git push ─► post-receive hook ─┐
                              ▼
            ┌─────────────────────────────────┐
 event in ─►│ APPEND → SQLite (WAL, event_no) │  the only writer's desk
            │ REDUCE → fold current state      │  state is derived, never stored
            │ EFFECTS → executors (jobs)       │
            └───────────────┬─────────────────┘
                            ▼  events emitted → APPEND again
            subscribers (own try/catch, own cursors):
            builder│monitor│chaos│rollback│WS-hub│autopsy
                            │
                            ▼
        WebSocket status wall (1s pushes) + scrubber
```

The rollback engine is not a subsystem — it's a **reducer over the log**: "last image whose health folded green." The loop is the only thing that appends; subscribers react, never command.

## 2. EVENT TAXONOMY

One envelope: `{no, ts, repo, deploy_id, type, payload}`

- `push.received {ref, sha, author}`
- `build.detected {stack}` → `build.built {image_tag}` / `build.failed {exit, logs[]}`
- `deploy.green {image_tag, url}`
- `health.probe {code, latency_ms, passes/fails}` (poll + threshold)
- `chaos.requested/injected {kind: poison|depbomb|memleak|kill9}`
- `death.detected {exit_code, cgroup_stats}` → `death.certified {verdict}`
- `resurrection.started/completed {from_tag, to_tag, ms}`
- `red.code.raised/cleared`; `traffic.synthetic {reqs, p95}`

## 3. CAPABILITIES AS SUBSCRIBERS

| capability | consumes | emits |
|---|---|---|
| builder | push.received | build.* |
| monitor | deploy.green | health.probe, red.code.* |
| chaos | deploy.green, manual | chaos.injected |
| rollback engine | death.detected, red.code.raised | resurrection.* |
| status wall | ALL | — (projection) |
| scrubber | ALL, read backwards | — |
| autopsy | death.detected | death.certified |
| GATE OF GREEN / traffic | deploy.green | traffic.synthetic |

New feature = new subscriber. Zero new schemas.

## 4. TIMELINE AS SPINE

The scrubber is `SELECT … ORDER BY no DESC` — logs *literally run backwards* because history is already append-only. Status wall: fold the latest event per deploy into 3 colors, push every 1s. Death Certificates: pretty-print `death.detected + death.certified` — 137 = OOM, 143 = SIGTERM. GREEN MEANS LIVE: a subscriber hitting the minted URL. All four are **projections** — pure functions of one log. No second state to corrupt, no sync to write, so each is an evening's work, not a day's.

## 5. ISOLATION MODEL

The loop never touches Docker. **Effectors** do: host-socket Docker client (build/run — DinD is dead on arrival), cgroup cages (`cpu.max`, `memory.max`) around every user container, Caddy admin API for routing, local DNS override for the wildcard. The loop only *describes* violence; effectors perform it, with idempotency keys. Untrusted code touches nothing but its cage — THE CAGE is just another effector config.

## 6. FAILURE PATHS

- **Loop crash**: WAL survives; on boot, replay events after each subscriber's cursor; effects dedupe by idempotency key — at-least-once, safe.
- **Dead subscriber**: every organ runs in its own try/catch queue; lag is not a heart attack. One corpse on the floor, heart still beating.
- A deploy's death is not the organism's failure — it's just an event. RED CODE is a color, not a panic.

## 7. WHY-NOT LIST

1. **Microservice mesh** — N pipelines for N services on one laptop rack in 24h; the mesh *is* the bug.
2. **Broker + workers (Redis/RabbitMQ)** — the broker becomes a second brain; WAL SQLite already gives durability + replay free. More daemons, more failure modes.
3. **UI polling the DB** — clients × seconds = query stampede; one WS hub fan-out is O(1) reads.
4. **Dual stores (event table + "current state" tables)** — duplicate truth is the classic hackathon killer; state must always be *folded*, never stored. One schema or death.
5. **Docker-in-Docker** — privileged and slow; host socket or nothing.

## 8. MAPPING — PS-WEB-01 + CLAN

Spec verbs: **builds** → builder subscriber; **runs/isolates** → effectors + cage; **monitors** → health probes; **auto-rolls back** → the reducer, <10 s because it's one fold. Roles: **Lead** owns loop + schema; **Docker hand** owns effectors; **Chaos engineer** owns chaos + autopsy; **Frontend/WS** owns wall + scrubber; **DevOps** owns Caddy, DNS, GitHub Actions. Five people, one spine.

## 9. KILL STROKES — vs THE CASTLE

Nine rooms means nine copies of the truth and eight doors between them — every door is a sync bug. They spend midnight writing adapters between named layers; we spend midnight signing Death Certificates. Their formality demands contracts and consensus before a single rollback; ours demands one SELECT. A castle needs a garrison — they have 4–5, for 24 hours, offline. More interfaces than a clan can hold means the walls collapse on their own. Cut us anywhere: the heart keeps beating, and the log remembers everything.
