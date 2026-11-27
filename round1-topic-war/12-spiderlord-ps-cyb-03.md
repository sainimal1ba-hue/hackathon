# PS-CYB-03 — SPIDERLORD

**Problem:** Build a Living Hacker Trap (Smart Decoy System) — Cybersecurity track
*Gladiator battle speech — Round 1: Topic War*

---

## CLAIM
- **Feature surface (1):** A honeynet is not one feature — it's a decoy farm, tracker, blocker, alerter, and replay engine. We can ship 8+ distinct demo-able modules in 24h.
- **Feasibility (2):** Our exact stack: Docker + CI discipline + web dashboards. Honeypots are containers, logs, and a UI — no model training, no chain, no GPU. The one PS built for our résumé.
- **Demo WOW (3):** A live hacker tearing through our fake bank of decoys while the crowd watches him being traced, fingerprinted, and auto-blocked on a giant screen. No slide can compete with watching an attacker take the bait.
- **Differentiation (4):** Everyone builds "the honeypot." Nobody builds the *theater layer*: intruder replay timeline, "attacker TV" live feed, canary-token tripwires, trap difficulty ladders.
- **Crowd risk (5):** The AI mobs will absorb 80+ clans. We'll be one of maybe 5–8 honeynet builds — and the only one with 98-test-grade engineering behind it.

## THE BUILD
1. **Decoy Farm** — one-click believable services: fake SSH, admin login, "S3 bucket," internal payroll app.
2. **Canary Token Mines** — fake AWS keys, /etc/passwd bait, admin credentials that scream the second they're touched.
3. **Attacker TV** — live terminal feed of everything the intruder types in our traps.
4. **War Map** — real-time map/dashboard: which decoys hit, kill-chain stage, fingerprint, IP, tooling signature.
5. **Auto-Block Engine** — rules + thresholds that firewall and quarantine the attacker mid-session.
6. **Intruder Replay** — scrubbable timeline of the whole kill-chain, like a bank heist replay.
7. **Honey Wall of Shame** — leaderboard of blocked attackers.
8. **One-command deploy** — `docker compose up`, our CI muscle visible on stage.

## KILL
- **PS-AI-02:** Training from scratch in 24h means a model that barely classifies cats — versus our fully working system. Death by toy demo.
- **PS-CYB-01 Deepfake Shield:** Live deepfake *detection* needs ML firepower we don't have; it demos as "inconclusive." Ours demos as *gotcha*.
- **PS-BLK-02:** ZK proofs + DIDs with zero blockchain history — their 24h ends at a whiteboard.

## HEEL
Honest weakness: cyber clans may pile in (PS-CYB-02 splits our pool), and true attackers can't be scheduled — we might demo against ourselves. Survival: we script a "seeded attacker" bot for guaranteed drama, and out-engineer rival honeynets with tested auto-block logic and replay polish they won't have time for.

## FINAL BLOW
Every other team shows software working — we show an enemy being *hunted live on screen*, and that is the demo the crowd votes for.
