# HEROKILL — The Winning System Architecture (Final Law)

*Champion: THE CASTLE (51/60), stealing the Organism's heart. Nine rooms, one heartbeat. The Castle is the map; the Organism's log is the pulse. One daemon, nine folders, one SQLite spine.*

## Component map

```
git push -> GATE -> FORGE -> DUNGEON <-- chaos -- LOOKOUT
 (bare repo,   (build,     (cage+net+             (autopsy)
  sniff, gate)  host        Caddy+DNS,
               socket)     image bank)
                             | pulse
                          INFIRMARY
                             | INSERT-only
                             v
             CRYPT (SQLite WAL, one writer, no UPDATE)
                             | 1 s fan-out
                          HERALD (WebSocket)
                             v
             GREAT HALL (3-color wall, scrubber, Death Certificates)
                             ^ reads RED_CODE
                            THRONE --> DUNGEON: rerun last green (<10 s)
```

Everything flows down to the Crypt; only the Throne commands back up.

## The three walks

**Walk I — Birth.** Push lands in the bare repo; post-receive sniffs composer.json / package.json and mints a stack card (stretch: GATE OF GREEN — tests must pass before the Forge lights). Forge builds on the host Docker socket, tags image:sha, banks layers in the cache. Dungeon cages it: cgroup v2 CPU/memory caps (THE CAGE), private bridge network, non-root user, Caddy route + local DNS override on the pre-minted wildcard. Infirmary polls; N green pulses fold to deploy.green; Herald paints the wall GREEN. (Stretch: GREEN MEANS LIVE fires synthetic traffic at the minted URL.)

**Walk II — Death.** Lookout injects poison / dependency bomb / memory leak / kill -9 inside the cage — blast radius zero. Infirmary trips the threshold (K fails in window) -> death.detected{exit_code, cgroup_stats} + red.code.raised appended; Herald pushes RED within 1 s. Lookout reads the exit code — 137=OOM, 143=SIGTERM — and files a numbered Death Certificate (death.certified).

**Walk III — Resurrection.** Throne is the rollback subscriber: it reads the Crypt, not the wire. On RED CODE it folds the log for the last image whose health folded green, then commands the Dungeon: bury the corpse, rerun the cached image — no rebuild, that is the <10 s budget. Infirmary confirms the pulse -> resurrection.completed{from_tag,to_tag,ms} -> wall shows RESURRECTED; the scrubber replays the death backwards.

## Event schema + WebSocket messages

```sql
events(no INTEGER PRIMARY KEY, ts, repo, deploy_id, type, payload JSON);
-- INSERT only. WAL mode. One writer (Crypt scribe). State folded on boot, never stored.
```

Types: push.received, build.detected, build.built, build.failed, gate.green, deploy.green, health.probe, chaos.injected, death.detected, death.certified, red.code.raised, red.code.cleared, resurrection.started, resurrection.completed, traffic.synthetic.

WS messages: HELLO{snapshot} | WALL{cell,color} | TICK | EVENT{no,type,payload} | RED_CODE | AUTOPSY{exit_code,verdict} | RESURRECTED{ms}.

## Isolation & security model

- Every repo: own bridge network, cgroup v2 cpu.max / memory.max hard caps, non-root user.
- Platform daemon: unprivileged host user in the docker group — root-adjacent, admitted and mitigated: parametrized exec only; no DinD (host socket, one kernel, CI-runner pattern).
- Caddy edges the castle with a pre-minted wildcard cert + local DNS override — no live ACME roulette.
- Lookout touches only caged PIDs; chaos is caged violence.
- Every room: own folder, own try/catch, own cursor; every effect carries an idempotency key (at-least-once, deduped).

## Failure-path table

| Room falls | Effect | Blast radius |
|---|---|---|
| Gate | Pushes bounce | Zero — running rooms live |
| Forge | No new builds | Cached images keep the rollback story |
| Dungeon | Cells go RED | Crypt/Herald/Hall live on; resurrect when the daemon returns |
| Infirmary | Wall paints AMBER | Silence is not green; Throne rolls back only on explicit RED CODE |
| Crypt | It is a WAL file | Pause, replay, resnapshot — not a fall |
| Herald | Wall freezes | Crypt still records; reconnect resnapshots |
| Throne | No rollbacks | Deaths still logged and certified |

## Why-not list

- **k8s** — a second product to debug in 24 offline hours; illegible to judges.
- **docker-in-docker** — privileged + nested overlayfs; a grenade in the cellar.
- **Redis/RabbitMQ** — a broker becomes a second brain; WAL SQLite already gives durability and replay free.
- **Postgres** — a server, migrations, ceremony; SQLite is the exact shape of an append-only stream.
- **Nginx** — config ritual; Caddy is one file and the spec whispers its name.
- **Dual stores** — event table plus current-state tables is duplicate truth, the classic hackathon killer; state must be folded, never stored.

## Spec-verb mapping

builds -> Gate + Forge | runs -> Dungeon | isolates -> cage + Lookout blast radius | monitors -> Infirmary + Crypt + Herald + Hall | auto-rolls back -> Throne (<10 s). Stretches: GATE OF GREEN at the Gate; GREEN MEANS LIVE as Lookout's benign twin; THE CAGE as the Dungeon's bars.

## Roles A–E (one folder, one owner; merge by contract, not by prayer)

- **A Gatekeeper** — Gate, post-receive, stack sniff, GATE OF GREEN.
- **B Jailer** — Dungeon, cgroup cages, Caddy, DNS, bridge networks.
- **C Nurse** — Infirmary, Lookout, chaos menu, Death Certificates.
- **D Scribe** — Crypt, event envelope, Herald, cursors + idempotency keys.
- **E Monarch** — Throne, Great Hall, demo choreography; the three walks ARE the demo.

**The law in one line:** everything flows down to the Crypt; only effectors touch Docker; the Throne commands back up; every death is certified; every resurrection is under ten seconds.
