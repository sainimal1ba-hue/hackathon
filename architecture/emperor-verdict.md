# Architecture War — The Emperor's Verdict

*Two architecture gladiators fought over HEROKILL's system design. The Emperor judged them on six axes, 0–10 each (total /60): SPEC · BUILD24 · DEBUG · LEGIBLE · TIMELINE · SAFEFAIL.*

---

## SCOREBOARD

| Axis | AR-1 CASTLE | AR-2 ORGANISM |
|---|---|---|
| SPEC | 9 | 9 |
| BUILD24 | 8 | 7 |
| DEBUG | 9 | 7 |
| LEGIBLE | 9 | 6 |
| TIMELINE | 7 | 10 |
| SAFEFAIL | 9 | 7 |
| **TOTAL** | **51** | **46** |

## KILL LINES

- **SPEC 9–9:** Both cover every verb. The Organism's taxonomy enumerates all four chaos kinds and ms-timed resurrection; the Castle maps every stretch to a room. Dead heat.
- **BUILD24:** Nine folders with one owner each beats one brain with five surgeons. The Organism's reentrancy (subscribers emit, loop appends again), cursor discipline, and state-never-stored purity are elegant — and a midnight trap at hour 20.
- **DEBUG:** Castle — the event names the room, the exit code names the cause. Organism — cursor drift and a convulsing heart are 3 a.m. mysteries; one loop, one blast radius.
- **LEGIBLE:** Judges walk a map; nobody grades a reducer. "Fold current state" loses the room in minute four of the demo.
- **TIMELINE:** Organism sweeps — ORDER BY no DESC; wall, scrubber, Death Certificates, synthetic traffic are pure projections of one log, each an evening's work. The Castle's Herald fan-out works but re-invents the projection.
- **SAFEFAIL:** A dead room is quarantined while the Crypt keeps the story; a dead heart needs replay, dedupe, and prayer. The Castle also admits its docker-group root-adjacency out loud — honesty scores.

## CHAMPION: AR-1 THE CASTLE, 51–46

Decisive argument: the clock and the clan decide this fight, not the schema — 24 offline hours, five builders, a live judge demo demand modularity with a spine, not a spine with modules. But the Castle wins ugly if it keeps nine doors of sync; it wins beautifully only by stealing the Organism's heart.

## ADOPTED FROM THE ORGANISM (spoils of war)
1. The event envelope and typed taxonomy — richer than the Castle's bare kinds.
2. State is derived, never stored — fold on boot; no duplicate truth tables.
3. Projections: wall, scrubber, Death Certificates, synthetic traffic as pure reads (ORDER BY no DESC).
4. Per-room cursors plus idempotency keys on every effect — at-least-once, deduped.
5. The effectors pattern: rooms command, effectors exec Docker.

---

Final Law: `winner-architecture.md`.
