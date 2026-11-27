# Round 2 — School 2: THE NECROMANCER (Death & Resurrection)

*Feature War gladiator — philosophy: every platform logs death; ours performs autopsies.*

---

## WAR CRY

Every platform logs death; ours performs autopsies. A green-light dashboard is a liar's mirror — HEROKILL makes the corpse testify. Death isn't downtime; it's the product.

## THE ARSENAL

Seven instruments, every one a real Docker API call:

1. **Death Certificates** — auto-minted autopsy report: verdict, exit code, OOM bit, last 50 log lines as "last words," named killer (health check / OOM / manual), timestamps — pulled from `inspect` + `logs` on the still-warm corpse. (wow 9 · cost 8 · diff 8 · fit 10 · risk 9)
2. **Cause-of-Death Verdicts** — classifier turning raw Docker signals into five stamps: POISONED DEPLOY, OOM, CRASH LOOP, FAILED HEALTH CHECK, MANUAL MURDER. Rivals show logs; we pronounce verdicts. (wow 7 · cost 9 · diff 9 · fit 9 · risk 8)
3. **The Graveyard** — tombstone grid of every dead deploy: name, death time, verdict glyph. Click → full autopsy → one-click RESURRECT rebuilds that exact revision and re-routes traffic. (wow 9 · cost 7 · diff 9 · fit 10 · risk 8)
4. **Autopsy Table** — `docker diff` on the corpse shows which files changed before death; the poisoned config lights up as the murder weapon, beside the health-probe log that watched it die. (wow 8 · cost 9 · diff 10 · fit 9 · risk 9)
5. **NecroLog** — dead containers' logs persisted and greppable, time-aligned with deploy marker → health flip → death event. Time-travel debugging on a corpse. (wow 7 · cost 8 · diff 8 · fit 8 · risk 9)
6. **Last Rites** — rollback as a three-beat animated ceremony: FREEZE traffic, SNAPSHOT (`docker commit`), ROLL BACK (green floods) — every beat a real API call, scored with a bell toll. (wow 10 · cost 6 · diff 7 · fit 10 · risk 8)
7. **The Séance** — our proxy records every request; one click resurrects the murdered image in an isolated sandbox network and replays the traffic until the crash reenacts itself, on demand. (wow 10 · cost 5 · diff 10 · fit 10 · risk 7)

## THE KILL

**THE CENTURION** ships green-light dashboards — mirrors that only show the living; we make the corpse the interface. **THE ARCHITECT** drowns judges in topology; an autopsy is depth made legible — `docker diff` as murder weapon beats a K8s diagram in a projector war. **THE CHAOS MAGE** kills containers at random and calls it a demo; chaos without a verdict is noise — we stamp every death with a killer and resurrect on cue. They murder; we prosecute.

## HEEL

Gimmick overload: gothic theater can read as costume over platform — "haunted house, not product." Survival plan: every artifact sits one click from raw evidence (certificate → inspect JSON → log lines), the skin stays thin over real API calls, and the boring push-to-deploy path stays flawless because judges will poke it. All demo traffic is pre-recorded and replayed locally — zero dice rolls on stage.

## FINAL BLOW

The Séance — summon the dead version and replay its own murder traffic until it dies in front of the crowd, then Last Rites drags it back green.
