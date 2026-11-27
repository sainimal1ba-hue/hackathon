# HEROKILL — The Winning Folder/Branch Structure (Final Law)

*Champion: TWIN FORTRESSES (48/60), refined with the spoils of MONOREPO LEGION. Two repositories, sovereign walls, one versioned gate.*

## The two trees

```
herokill-platform/               # FORTRESS ONE — THE PRODUCT (clean history)
├── app/{Domain,Deployer,Rollback,Hook,Autopsy}/   # A — Laravel core
├── engine/                       # B — heartbeat + rollback core
│   ├── src/{EventLog,RedCode,Rollback}.php
│   ├── schema/schema.sql         # append-only SQLite DDL — single source
│   ├── contract/contract.ts      # shared event types — fixed path, C imports
│   └── tests/                    # kill-drill suite: CI-green or dead
├── console/src/{wall,scrubber}/  # C — TS/Vite status wall + timeline replay
├── hook/post-receive             # bare repo → Docker socket → Caddy
├── caddy/Caddyfile   config/herokill.php   routes/hook.php
├── database/{migrations,seeders}/
├── docs/EVENT-SPEC.md            # semver law, generated from schema.sql
└── ci.yml  CODEOWNERS  CHANGELOG.md  composer.json  package.json  .env.example

herokill-arsenal/                # FORTRESS TWO — THE DEMO ARSENAL
├── weapons/                      # D — kill.sh · netsplit.sh · forkbomb.sh · diskfill/
├── autopsies/templates/          # D — exit-code → cause of death
├── repos/                        # real bare victims; hook pushes here
│   ├── goldrepo.git/  crashrepo.git/  zombie.git/   (each root: .herokill.yml)
├── vault/                        # E — SEALED ARMORY
│   ├── images/*.tar + SHA256SUMS
│   ├── certs/wildcard.crt + serial.txt
│   └── recordings/golden-incident.mp4 + cues.md
├── director/                     # E — beats.md · runbook · audio/ · env/
│   └── env/{.env.dev,.env.box,.env.venue}
├── manifests/images.lock         # name@digest → tarball → sha256
└── scripts/{bake.sh,verify-assets.sh,restore-state.sh}  Makefile
```

**Sovereignty:** never in Platform — chaos payloads, tarballs, recordings, venue scripts, audio, demo secrets. Never in Arsenal — hook/engine/console code, migrations. Crossing the wall unversioned is treason.

## Branch law + demo-hour ritual
Platform: `main` protected, PR-only, CI-green or the merge dies; work on `task/<role>-<slug>` branches born-merged-dead within 3 h and 300 changed lines — stale branches are deserters, Director E kills them. Hour −2: cut and sign tag `v1.0.0-frozen`; push ceases; a late fix is a NEW tag, never a rewrite. `/opt/herokill` runs detached HEAD at the frozen tag, `chmod -R a-w`, seeded, Caddy live on the pre-minted cert. Arsenal: E owns the timeline as `beat/01-first-push` … `beat/04-judge-chaos`; D commits weapons only onto beat branches; a beat merges to arsenal `main` only with the stamp `REHEARSED 3/3`; each surviving beat is tagged `demo/beat-N` so the scrubber jumps to the exact commit where the kill landed.

## Commit law
Both fortresses: `ROLE(type/scope): imperative`, ≤72 chars, enforced by in-repo commit-msg hook. Platform bodies end `Verified: CI + kill drill N/N`. Examples: `B(fix/rollback): abort deploy <10s on exit 139`; `D(weapon/kill): SIGKILL strike emits RED v1.2 — REHEARSED 3/3`; `E(chore/assets): re-seal vault, platform@sha256:…`. No wip, no asdf; the platform log is a product surface and doubles as the changelog slide.

## Pre-baked assets
Sealed in arsenal `vault/`: docker-save tarballs under SHA256SUMS; `images.lock` binding `name@digest → tarball → sha256`; wildcard cert pinned by serial + expiry; golden incident as checksummed video + cue sheet. `bake.sh` reproduces the vault byte-for-byte and verifies every hash; `make verify-assets` re-verifies at hall-open and before each beat — any drift and the hall does not open. Vault changes land only as E-signed `chore(assets)` commits; nothing regenerates on demo day; no network, no LFS.

## Env & config layering
Each victim repo's root `.herokill.yml` is the only wall gate: image ref `name@sha256`, route, health check, rollback budget, event schema version. The hook reads it and nothing else; the platform never knows a repo's name in advance. Venue reality lives in `director/env/.env.{dev,box,venue}` (laptops / demo Docker host / hall); the product ships only `.env.example`. Precedence: `.herokill.yml` → env file → `config/herokill.php` defaults. Every event carries its schema version; every weapon and recording declares the version it emits; schema bump = platform tag bump + arsenal re-bake.

## War-room repo
Remains sovereign planning memory: decisions, autopsy playbooks, run-of-show rationale. It references both fortresses by pinned tag/SHA, is linked from both READMEs, and is never cloned at demo hour — one offline copy rides the USB stick for the post-mortem. Code never depends on it; the executable runbook lives in arsenal `director/`.

## ACL (CODEOWNERS-enforced)
Platform: A `app/`, B `engine/`, C `console/` — PRs only. D and E hold ZERO write access to the platform; they file issues. Arsenal: D writes `weapons/` + `autopsies/` on beat branches only; E sole owner of `vault/`, `director/`, and all tags. Only E signs; retagging is heresy.

## Rollback-of-the-repo
`/opt/relics` holds git bundles of both fortresses plus SHA256SUMS, cut at freeze. A scorched checkout is never debugged on stage: `git clone /opt/relics/herokill-platform.bundle` (offline, ~90 s) + `restore-state.sh` reloads images, reseeds the event DB, remounts the cert — the repo receives the mercy it gives apps.
