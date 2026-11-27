# ST-2 — TWIN FORTRESSES

> Structure War · gladiator speech · fought 2026-11-27
> Fate: **CHAMPION — 48/60.** Refined into the Final Law in `winner-structure.md` (adopts the Legion's ROLE commit prefixes + hook, beat tags, task-branch decay law, verify-assets gate, single-source event schema).

---

# TWIN FORTRESSES — THE DOCTRINE

Brothers — a product judged by engineers must wear a clean history, and a demo that must never fail must rehearse its weapons in private. One repo cannot be both cathedral and bomb range. **Two fortresses. Sovereign walls.**

## 1. THE TWO TREES

**Fortress One — THE PLATFORM** (the product, one deployable unit, clean history):

```
herokill-platform/
├── app/                    # Laravel core (A): Controllers, Models
├── engine/                 # event stream + rollback core (B)
│   ├── src/EventLog.php  src/RedCode.php  src/Rollback.php
│   └── tests/             # kill-drill suite, CI-green or dead
├── console/                # status wall + scrubber (C), JS/TS + WS
├── hook/                   # post-receive: bare repo → Docker socket
├── caddy/Caddyfile        # reverse proxy, wildcard cert mount
├── database/{migrations,seeders}/
├── docs/EVENT-SPEC.md     # event schema — THE LAW
├── scripts/install.sh
├── .github/workflows/ci.yml
└── composer.json  package.json  CHANGELOG.md
```

**Fortress Two — THE DEMO ARSENAL** (weapons, rehearsals, props):

```
herokill-arsenal/
├── weapons/                # chaos injectors (D)
│   ├── kill-container/{weapon.sh,README}  diskfill/  netcut/
├── repos/                  # victims, each with .herokill.yml
│   ├── guestbook/          # beat-01 victim
│   └── shop/               # beat-03 victim
├── vault/                  # PRE-BAKE (E)
│   ├── images/*.tar + SHA256SUMS
│   ├── certs/wildcard.crt + serial.txt
│   └── recordings/golden-incident.mp4 + cues.md
├── director/               # venue scripts (E): beats.md, runbook, audio/
├── autopsies/templates/    # exit-code autopsy formats
├── scripts/{bake.sh,restore-state.sh}
├── manifests/images.lock   # name@digest → tarball → sha256
└── README.md
```

## 2. SOVEREIGNTY RULES

**Never in the Platform:** chaos payloads, tarballs, recordings, venue scripts, audio, demo secrets. **Never in the Arsenal:** hook code, engine code, console source, migrations.

The wall has one gate — artifacts, versioned:
- **`.herokill.yml`** sits in every demo repo root: image ref (`name@sha256`), route, health check, rollback policy. The hook reads it and *nothing else* — the platform never knows a repo's name in advance.
- **Event schema** is `EVENT-SPEC.md`, semver'd. Every event carries its schema version; every weapon and recording declares the version it emits. Schema bump = platform tag bump + arsenal re-bake. Crossing the wall unversioned is treason.

## 3. BRANCH LAW

**Platform:** trunk only. `main` protected, CI-green or the merge dies. A (hook/build) and B (engine) merge via PR; C merges console after visual review. **D and E have zero write access to the platform** — they file issues. Releases are signed, immutable tags. Retagging is heresy.

**Arsenal:** branch-per-demo-beat — `beat/01-first-push`, `beat/02-red-code`, `beat/03-resurrection`, `beat/04-judge-chaos`. E owns the timeline; D commits weapons onto beat branches, never main. A beat merges to arsenal `main` only with the stamp `REHEARSED 3/3`.

## 4. COMMIT MESSAGE LAW

**Platform:** conventional and engineer-honest — `fix(engine): kill race in rollback poller`, body: `Verified: CI + local kill drill 40/40`. No `wip`. No `asdf`. The log is a product surface; judges will read it.

**Arsenal:** beat first — `[beat/02] weapon: kill-container — REHEARSED, schema v1.2`. Every message names its beat, rehearsal state, schema version. Noise lives on beat branches; only stamped silence reaches main.

## 5. DEMO-HOUR STATE

- `/opt/herokill` — platform, **detached HEAD at `v1.0.0-frozen`**, `chmod -R a-w`, seeded, Caddy live on the pre-minted cert.
- `/opt/arsenal` — on the current beat branch, weapons mounted read-only, images loaded at bake.
- `/opt/relics` — git bundles of both fortresses, hashes verified.

**Frozen-tag ritual:** hour −2. Cut and sign `v1.0.0`. Push ceases. A late fix = a *new* tag, never a rewrite.

**Rollback-of-the-repo:** a weapon scorches the checkout → we do not debug on stage. `git clone /opt/relics/herokill.bundle` (90 s, offline), run `restore-state.sh`. The repo gets the mercy it gives apps: fast rollback, clean resurrection.

## 6. PRE-BAKE VAULT

`vault/` is a sealed armory: `docker save` tarballs with `SHA256SUMS`; `images.lock` binding `name@digest → tarball → sha256`; the wildcard cert pinned with serial and expiry; the golden incident as a checksummed video plus cue sheet. `bake.sh` reproduces the vault byte-for-byte and verifies every hash. Nothing regenerates on demo day — rebuildable on any machine, no network, no mercy.

## 7. KILL STROKES — WHY "MONOREPO LEGION" DIES

1. **History pollution.** `final-audio-v3-REALLY` beside `fix(engine)` — judges run `git log` in Round 2. The log IS the product.
2. **3 a.m. blast radius.** One bad merge from a chaos weapon bricks the same tree hosting the hook and engine — the machine that must never fail.
3. **Clone of shame.** Gigabytes of images in history; venue Wi-Fi kills the final clone before first deploy.
4. **ACL rot.** D holding write access to A's throne — chaos with commit rights to the engine.
5. **Untaggable.** You cannot cut a clean product release from a repo that also mints demo noise.

Two fortresses. Clean history on one side, rehearsed carnage on the other, one narrow versioned gate between them. **Hold the wall.**
