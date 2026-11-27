# Round 2 — School 5: THE MERCHANT (Developer Experience)

*Feature War gladiator — philosophy: judges live in terminals, students live in wonder; every feature wows in under fifteen seconds.*

---

## WAR CRY

Judges live in terminals; students live in wonder. A dashboard is wallpaper — a CLI is proof this thing outlives the hackathon. Doctrine: every feature wows in under fifteen seconds, so our five minutes hold more beats than any clan's five.

## THE ARSENAL

1. **`herokill` CLI — the terminal IS the product.** `herokill deploy` from any repo; build logs stream over WebSocket; ends with the live URL. — WOW 8 · COST 8 (thin Node client over our own API) · DIFF 8 (rivals ship dashboards; products ship CLIs) · FIT 7 · RISK 9.
2. **`.herokill.yml` — the murder contract.** Declares env, health check, rollback policy: `rollback: on-health-fail, keep: 3`. Resurrection isn't magic — it's contractual, versioned in the repo. — WOW 6 · COST 9 · DIFF 8 · FIT 10 · RISK 9.
3. **`herokill kill` — the murder verb.** Poison your own app from the terminal; timeline scrubs, health screams, auto-resurrect fires. Hands the crowd the weapon. — WOW 9 · COST 9 · DIFF 8 · FIT 10 · RISK 9.
4. **`herokill rollback` — two-second time travel.** One command, green restored, terminal prints the diff. — WOW 8 · COST 9 · DIFF 6 · FIT 10 · RISK 9.
5. **Branch preview environments.** Push a branch → `feat-x.app.herokill.live`. Three versions of one app alive AT ONCE, three projector tabs — wildcard cert + Caddy on-demand, already pre-minted. — WOW 9 · COST 5 · DIFF 8 (nobody ships previews in 24h) · FIT 8 · RISK 7 (pre-push branches locally).
6. **The App Store — one-click starters.** Pre-baked snake game, live poll, chat wall; an audience member picks one, it's LIVE in ten seconds, zero network. — WOW 9 · COST 6 · DIFF 8 · FIT 6 · RISK 10.
7. **The Butler — deploy hooks.** Dashboard toasts and terminal banners narrate everything: "☠ APP RESURRECTED — v3 → v2 in 1.9s." — WOW 7 · COST 8 · DIFF 5 · FIT 9 · RISK 9.

## THE KILL

**THE SHOWMAN** — your theater needs props; mine IS the interface. The curtain falls on rented drama; a command they can type becomes a habit.

**THE ARCHITECT** — no judge proofs your etcd in five minutes. Depth nobody can touch is depth nobody scores; I surfaced ours as a fifteen-second command.

**THE CENTURION** — table stakes are table stakes: 150 clans will push a deploy button. Buttons prove nothing; terminals prove products.

## HEEL

Honest: judges score the platform, not the CLI — a slick shell over a shallow core is costume, and the students who decide the final vote don't love YAML. Survival: every DX feature is a LENS on the resurrection engine, never a side quest — the CLI streams the murder, the manifest contracts the resurrection, previews multiply the graveyard — while the App Store buys the students and the CLI buys the engineers.

## FINAL BLOW

An audience member picks a starter from the App Store and it's live on the projector before they sit back down — because the crowd votes for the platform that let THEM deploy.
