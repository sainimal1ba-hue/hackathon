# WF-2 — THE WAR ROOM

> Workflow War · gladiator speech · fought 2026-11-27
> Fate: FELL — 47/60. Its bones became the champion's armor: two-hour battle rhythm, board law, 3 a.m. triage, two vetoes, scheduled sleep floor, dev-lane rehearsal, THE ROAR.

---

# THE WAR ROOM — ADAPTIVE PARALLEL WARFARE

Gladiators. The Railway builds a train and prays the tracks hold. We build a **horde** — two squads, one board, zero mercy for surprises.

## 1. THE SQUADS AND THE GATES

**PLATFORM SQUAD** — the butchers: **A** (platform, birth chain), **B** (event stream, rollback engine), **D** (chaos injection, autopsies). They own git push → green lock → RED CODE → resurrection.

**THEATER SQUAD** — the showmen: **C** (console UI, scrubber front-end), **E** (direction, judge-interaction, pre-baked assets). They own what the crowd *sees*.

Two squads. **Four merge gates**, physical and absolute: **Gate One at H6** (birth chain works end-to-end — green lock on the hall projector), **Gate Two at H10** (death + rollback live), **Gate Three at H14** (timeline scrubber), **Gate Four at H17** (script freeze, full chain). Between gates, squads never touch each other's lane. At the gate, both squads stand at the board and integrate on the spot.

**Two vetoes, both real.** **A** holds the technical veto: *nobody* modifies the protected core without his sign-off. **E** holds the demo veto: after H17, nothing changes the script without his word. Two kings, two thrones, no overlap.

## 2. THE BOARD

No Wi-Fi, no tools, no excuses — the board is **painter's tape on the wall**: three lanes. **READY. KILLING. DEAD.** Sticky notes, fat marker, one card = one demo-able thing. A red sticker on a card means BLOCKED — visible from across the hall, and blocked cards get a body within ten minutes.

**WIP limit: one card per gladiator, three per squad.** A squad drowning in WIP isn't heroic, it's bleeding out.

**The law: done means demo-able.** A card moves to DEAD only when someone who *didn't write it* makes it work in front of eyes. "It works on my machine" is not a state — it's a lie. If it can't be shown, it doesn't exist.

## 3. THE BATTLE RHYTHM — CHECKPOINTS, NOT RUNBOOKS

Every two hours: **ten minutes, standing, at the board.** Three questions only: *What's dead? What's bleeding? What do we cut or keep?* Checkpoints re-slice scope, reassign bodies, move the next gate if we must. The plan bends.

**The KILL SHOT core does not bend. Never renegotiated, at any checkpoint, at any hour:**

- git push → green lock, offline
- RED CODE → auto-rollback under 10 seconds
- Resurrection at **00:07**
- The scrubber

These four beats are carved in stone. Everything else is weather.

## 4. REHEARSAL EMBEDDED IN THE BUILD

Rehearsals aren't a finale — they're **every four hours**, and they run on the **dev lane**: a parallel copy Theater rehearses on while Platform keeps butchering. The demo squad never touches the production lane mid-build. The squads meet only at gates — that's the discipline.

**The 3 A.M. Triage Rule.** New failure at 3 a.m.? Sixty seconds, three buckets:

1. **Touches the core?** Platform drops everything. Full assault. Two-person rule — nobody debugs alone past 2 a.m., and a 15-minute timer: no path to a fix in fifteen minutes, escalate or die trying.
2. **On the sacrifice ladder?** Cut it. Now. A 3 a.m. rescue of a stretch goal is how clans die.
3. **Cosmetic?** Theater absorbs it into the act. The judge sees a flicker? *"Chaos, ladies and gentlemen. Watch the rollback."*

## 5. FLESH AND FIRE

Squads rotate: while Platform builds the death chain, Theater sleeps first — **a hard two-hour sleep floor for every gladiator, scheduled, not earned.** Eat at checkpoints, real food, hot if the hall allows. **The 4 a.m. wall is real — so we schedule boring work into it:** copy for Death Certificates, polish, pre-baked assets. **No new architecture after 2 a.m. Ever.**

Morale ritual: **the ROAR.** Every gate passed, every rollback under ten seconds in rehearsal, the whole room roars. First green lock gets a standing ovation. Cheap? Yes. It works at 4 a.m. That's when it matters.

## 6. THE RISK LADDER

When time bleeds, we sacrifice in order:

1. Demo Director Mode
2. Gate of Green
3. .herokill.yml, The Cage — shown pre-configured, not built live
4. Console polish and branding
5. Extra chaos payloads — keep poison code and kill -9, drop the variants

**Never:** green lock, rollback under 10 s, 00:07, scrubber, and the pre-baked backup — that backup is our life insurance; it's the last thing burning.

## 7. KILL STROKE — WHY THE RAILWAY DIES

The Railway assumes the hall obeys. The hall is a **live arena**: the judge fires the trigger early, a laptop dies, the DNS override fights the venue network, the dependency bomb refuses to detonate on cue. A rigid runbook meets every surprise with the same answer — *discipline* — and at 3 a.m., discipline is a **single point of failure**. One broken gate cascades down the whole timetable. Rehearsal-maximalism burns the very hours you'll need to absorb the shock. The Railway rehearses *obeying*; nobody in it has practiced *deciding*.

We drill decisions every two hours. Checkpoints are reps. When the unexpected hits, the Railway freezes — because its people were trained to follow tracks, and the tracks are gone.

The plan bends. **The KILL SHOT never bends.** Now sound the horn.
