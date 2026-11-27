# Round 2 — School 4: THE ARCHITECT (Infra Depth)

*Feature War gladiator — philosophy: theater without engineering is a puppet show. (Translated from the original Chinese battle speech.)*

---

## WAR CRY

Theater without engineering is a puppet show. Rivals will ship deploy buttons, but almost none can prove the machinery underneath. Our doctrine: everything on the projector must come from the real Docker API — every gauge, every rollback, every byte of the timeline.

## THE ARSENAL

- **THE CAGE** — hard Docker CPU/RAM limits per app; live cgroup gauges streamed over WebSockets. On stage: deploy a busy-loop app, watch the gauges spike red, strangle it live. WOW 9 · COST 7 · DIFF 9 · FIT 7 · RISK 9
- **THE CORONER** — real HTTP health probes on an interval; N consecutive failures → the platform kills the poisoned revision and auto-promotes the last green one. The poisoning is a real `/kill` route; detection, death certificate, and revert — all real. No setTimeout theater. WOW 9 · COST 6 · DIFF 7 · FIT 10 · RISK 8
- **THE VAULT** — time-series of health states, resource stats, and revision events stored in Redis/Postgres. The timeline scrubs RECORDED reality: drag back 10 minutes, see the app's actual state. Rivals animate; we time-travel. WOW 10 · COST 6 · DIFF 9 · FIT 10 · RISK 8
- **THE FORGE** — live build pipeline (clone → install → test → image → live), streaming `docker build` output line-by-line as it happens. WOW 8 · COST 8 · DIFF 7 · FIT 7 · RISK 9
- **THE GATE OF GREEN** — test-gated deploys: the platform runs the repo's test suite during the build; red aborts the deploy, the container never goes live. "No green, no live" — our own 98-test discipline weaponized. WOW 8 · COST 8 · DIFF 8 · FIT 8 · RISK 8
- **THE TWIN PARADE** — blue/green twin versions behind Caddy, a live traffic slider, and a request counter that colors each request by which version served it. WOW 8 · COST 5 · DIFF 6 · FIT 8 · RISK 6
- **THE QUARANTINE** — every deployment gets its own Docker network and pre-minted wildcard-TLS subdomain; apps cannot read each other's env. On stage: `curl` a neighbor service → request refused. WOW 7 · COST 8 · DIFF 7 · FIT 7 · RISK 9

## THE KILL

**THE CENTURION**: table stakes. Their dashboard lists containers; ours strangles, resurrects, and time-stamps both. Their build logs need a refresh to see; ours stream live. Exposed the moment they hit the stage.

**THE SHOWMAN**: lights without gauges. The engineers in the audience will ask "but is any of this real?" — a confetti canvas cannot survive cross-examination by cgroup data and recorded health checks.

**THE NECROMANCER**: ally, but their rollback is a scripted flip on a preset timer. Ours is probe-driven, recorded in the Vault, and scrub-replayable. Same resurrection — ours survives cross-examination.

## HEEL

Depth means slow, and blue/green could eat the whole 24 hours. Survival: triage the build order — Coroner + Vault first (they ARE the core story), Cage + Forge second, Twin Parade as bonus; if hour 16 is red, we degrade the slider to a binary switch and ship everything else. One member owns infra, never touches UI.

## FINAL BLOW

Rivals replay death from a video; our timeline re-renders the recorded infrastructure state from real metrics — ours is the only resurrection in the room that actually happened twice.
