# Structure War — The Emperor's Verdict

*Two folder/branch-structure gladiators fought over how HEROKILL's repositories are organized. The Emperor judged them on six axes, 0–10 each (total /60): CLONE · BLAST · JUDGESTORY · PARALLEL · BAKE · FIT.*

---

## SCOREBOARD

| Axis | ST-1 Legion | ST-2 Fortresses |
|---|---|---|
| CLONE | 8 | 6 |
| BLAST | 4 | 10 |
| JUDGESTORY | 8 | 8 |
| PARALLEL | 8 | 7 |
| BAKE | 7 | 10 |
| FIT | 8 | 7 |
| **TOTAL** | **43** | **48** |

## KILL LINES

- **CLONE:** ST-1 — one clone is the whole war machine; USB re-clone, 90 s. ST-2 pays twin-sync tax and needs two clones, though pre-staged `/opt` state absorbs most pain at demo hour.
- **BLAST:** ST-2, 10–4 massacre. The trunk that must never fail (hook + engine) cannot share a tree with `forkbomb.sh` and tarballs. ST-1's firewalls are social conventions; conventions die at 3 a.m.
- **JUDGESTORY:** 8–8. ST-1's ROLE chronicle is seductive but the same log must digest `final-audio-v3-REALLY`; ST-2's platform log is engineer-honest, but two logs split the narrative.
- **PARALLEL:** ST-1 — five directories plus born-dead task branches flow freely. ST-2's ACL is safer, but D/E filing issues against the platform is a bottleneck for five people in 24 h.
- **BAKE:** ST-2, 10. `images.lock` binding name@digest→tarball→sha256 plus byte-reproducible `bake.sh` is mechanical truth; ST-1's MANIFEST verifies files, but vault-in-git bloats every clone and immutability is by convention.
- **FIT:** ST-1 — `.herokill.yml` constitution + one schema + `contract.ts` make drift break CI, not the demo. ST-2's semver'd EVENT-SPEC is correct but heavy for 24 h; per-repo `.herokill.yml` gate is elegant.

## CHAMPION: ST-2 TWIN FORTRESSES, 48–43

Decisive argument: HEROKILL's product *is* reliability. You cannot sell a sub-10-second auto-rollback system from a repo whose trunk hosts chaos weapons and Docker tarballs — one bad merge from D bricks the machine that must never fail. Twin fortresses give the engine a history engineers respect and the arsenal a range it may freely scorch; the versioned `.herokill.yml` gate replaces the monorepo's "one schema" with a contract that survives the wall.

## BINDING ADOPTIONS FROM THE DEFEATED
1. ROLE prefixes A–E + in-repo commit-msg hook.
2. `demo/beat-N` tags as scrubber jump-points.
3. Task branches born-merged-dead ≤3 h/≤300 lines under an hourly Director merge window.
4. `make verify-assets` as the hall-open gate.
5. Single-source event schema + `contract.ts` at fixed platform paths, mirrored to EVENT-SPEC.md, so a rename breaks CI — not the 3 a.m. demo.

---

Final Law: `winner-structure.md`.
