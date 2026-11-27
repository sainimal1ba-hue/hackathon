# Round 2 — School 1: THE CENTURION (Table Stakes)

*Feature War gladiator — philosophy: the crowd votes for the platform that never died on stage; flawless basics ARE the show.*

---

## WAR CRY

The crowd doesn't vote for the best platform — it votes for the one that never died on stage. Every stake we drive is a stake through a rival's demo. Flawless basics ARE the show.

## THE ARSENAL

- **Clone-to-Live Intake + Staged Build Theater** — MANDATORY + HIDDEN-GEM. Paste a repo URL, watch a numbered launch sequence — clone → detect → build → probe → route → live — with per-stage timings. Everyone ships deploys; nobody stages a countdown. TRAP inside: buildpacks for arbitrary stacks — ONE stack only. W8 C7 D4 F8 R9.
- **Port Wiring + Wildcard Routing** — MANDATORY. Random container port auto-bound to a named subdomain via Caddy, pre-minted cert + local DNS. Invisible when right, fatal when wrong. W6 C8 D3 F7 R10.
- **Env Vars Panel** — MANDATORY, minimal. Key-value editor injected at container create; edit → redeploy. Twenty lines of code, zero vaults, zero secrets encryption. W3 C10 D3 F6 R10.
- **Bulletproof Log Stream** — MANDATORY + HIDDEN-GEM. WebSocket attach that never drops a line and keeps scrolling through death and rebirth — logs that narrate the resurrection while rivals' streams freeze at the moment of death. W7 C7 D5 F10 R9.
- **Health Checks as Referee** — MANDATORY. Polling state machine → green/amber/red badge, audible pulse that flatlines on failure. The badge is the crowd's heart monitor. TRAP: Grafana dashboards. W7 C8 D4 F10 R10.
- **Restart-on-Crash** — MANDATORY and FREE. Docker `--restart unless-stopped`; never hand-roll a supervisor. W4 C10 D4 F6 R10.
- **Sub-5-Second Rollback** — MANDATORY, crown jewel. Every deploy is a tagged, retained image; rollback = stop new, start old, repoint. Never revert-and-rebuild — that's two silent minutes on stage. W9 C8 D5 F10 R10.
- **One-Screen Dashboard** — MANDATORY floor, TRAP as project. App cards with state badges + deploy-history strip; nothing more. TRAP: auth, multi-tenancy, billing, SSH push, settings pages. W6 C8 D2 F8 R10.

## THE KILL

**THE NECROMANCER** calls health checks "too basic," so their deaths are timeout scripts — theater without a referee. Ours fires because a real probe failed in front of the crowd; theirs is a cron job in costume.

**THE ARCHITECT** brings Kubernetes depth to a five-minute projector slot — namespaces nobody sees, architecture nobody watches deploy. Depth invisible in five minutes doesn't exist in the Arena.

**THE CHAOS MAGE** lets the audience pick the poison, and 150 clans will pick the one that kills the demo. We poison on script: chosen chaos is drama; audience chaos is a coin flip.

## HEEL

Table stakes are what losers also ship — every eliminated clan had deploy, logs, rollback; the floor earns zero votes, it only prevents losing them. Survival: fuse every stake into the Resurrection Timeline — health checks feed it, logs narrate it, rollback scrubs it — so the basics ARE the story, then drill the five-minute clock until failure is impossible.

## FINAL BLOW

A sub-five-second rollback from a retained image — while rivals' rebuild-based rollbacks burn two silent minutes, ours resurrects instantly: the one "basic" nobody else got right.
