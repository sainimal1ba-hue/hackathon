# ST-1 — MONOREPO LEGION

> Structure War · gladiator speech · fought 2026-11-27
> Fate: FELL — 43/60. Surviving elements adopted into the Final Law (TWIN FORTRESSES): ROLE commit prefixes + commit-msg hook, demo/beat-N scrubber jump tags, task branches born-merged-dead ≤3h/≤300 lines under an hourly Director merge window, make verify-assets as the hall-open gate, single-source event schema + contract.ts so drift breaks CI not the demo.

---

# MONOREPO LEGION — ONE CLONE = THE WHOLE WAR MACHINE

Twenty-four hours, no network, five gladiators. We clone ONCE and the war is armed. **HEROKILL lives in ONE repo. This is the law.**

## 1. THE FULL TREE

```
herokill/                      # ONE CLONE = THE WAR MACHINE
├── platform/             # A — Laravel core
│   ├── app/{Domain, Hook, Deployer, Rollback, Autopsy}/
│   ├── routes/hook.php        # post-receive target
│   └── config/herokill.php
├── events/               # B — the heartbeat
│   ├── schema.sql             # append-only SQLite DDL
│   ├── broadcaster/           # WS tailer → wall
│   └── contract.ts            # shared event types
├── console/              # C — web UI (TS/Vite)
│   ├── src/wall/              # status wall
│   └── src/scrubber/          # timeline replay
├── chaos/                # D — the arsenal
│   ├── strikes/               # kill.sh · netsplit.sh · forkbomb.sh
│   └── autopsy/               # exit-code → cause of death
├── assets/               # E — PRE-BAKED VAULT
│   ├── images/                # platform.tar · victim-base.tar + MANIFEST.sha256
│   ├── certs/                 # wildcard.pem + chain
│   ├── demo-repos/            # goldrepo.git · crashrepo.git · zombie.git
│   └── golden/                # incident recording · audio cues
├── infra/                # Caddyfile · dns-override.sh · forge.sh · entrypoints/
├── .github/workflows/    # CI: lint · test · image build (local runner)
├── .herokill.yml         # THE CONTRACT
├── .env.dev · .env.box · .env.venue
├── Makefile              # make forge · war · demo · verify-assets
├── compose.yml
└── docs/warbook.md       # run-of-show + autopsy playbooks
```

Five fortresses under one roof. Nobody owns a repo — everybody owns a directory.

## 2. BRANCH LAW — THE TRUNK RULES ALL

`main` is the only long-lived branch — deployable at every commit. Work happens on `task/<role>-<slug>` branches: born, merged, dead inside **three hours and 300 changed lines**. Longer, and the Director kills it — stale branches are deserters.

Director E runs the **merge window**: every hour, branches rebase onto `main`, E fast-forwards, CI on a local runner keeps the trunk green.

Demo hour: `main` frozen at tag **`demo/freeze`**, working tree clean, `make verify-assets` green. Every demo beat is its own tag — `demo/beat-1`…`beat-9` — so the scrubber jumps to the exact commit where the kill landed. Hall burns down? Re-clone from a cold USB stick; rearmed in ninety seconds.

## 3. COMMIT MESSAGE LAW — THE LOG IS THE STORYBOARD

`ROLE(scope): imperative` — `B(rollback): abort deploy under 10s on exit 139`. Judges WILL open `git log`. Role prefixes make `--oneline` read like a battle chronicle: who struck, what fell, when the rollback closed. An in-repo commit-msg hook enforces it; at demo hour the log becomes our auto-generated changelog slide. Pure judge damage.

## 4. THE PRE-BAKED VAULT

Everything the demo needs ships **inside the tree as plain files** — no Git LFS, no network, no mercy. Docker images, the wildcard cert, real bare demo repos (`goldrepo.git` is what the hook actually pushes to), and the golden-incident recording. `MANIFEST.sha256` pins every hash; `make verify-assets` runs before the hall opens. Vault changes land only as E-signed `chore(assets):` commits — immutable during the war.

## 5. ENV & CONFIG — THREE ENVS, ONE CONTRACT

`.env.dev` (laptops), `.env.box` (demo Docker host), `.env.venue` (hall reality: DNS IP, domain, host paths). Above them all, **`.herokill.yml` at the repo root is the constitution**: wildcard domain, event-DB path, WS port, rollback budget, strike whitelist. `forge.sh`, Laravel, and the wall all read it — change venue reality once, every subsystem obeys or fails CI.

## 6. INTEGRATION — ONE HEARTBEAT

`events/schema.sql` defines the append-only timeline. Platform writes; `broadcaster/` tails SQLite and pushes WebSocket; wall and scrubber consume the same types via `contract.ts`. One repo, one schema: if B renames an event, C's wall breaks in the same CI run — not at 3 a.m. Scrubbing the golden incident is just pointing the wall at a copied DB. Zero adapters, zero drift.

## 7. KILL STROKES — TWIN FORTRESSES BLEEDS OUT

**Synchronization tax:** three repos means version pins and lockfile surgery on every cross-repo touch while the clock bleeds. **3 a.m. integration hell:** console built against platform v0.4 while trunk is v0.6 — the demo dies in an unscheduled merge conflict. **Split history before judges:** three logs tell no story; blame dissolves between repos; commit timeline and scrubber timeline don't even align. **Branch-per-demo-beat** turns your own show into merge debt.

ONE CLONE. ONE TRUNK. ONE STORY THE JUDGES CAN READ. **MONOREPO LEGION.**
