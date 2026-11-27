# PS-WEB-03 — PIXEL REAPER

**Problem:** Build Your Own Zero-Lag Multiplayer Creative Studio — Web & Applications track
*Gladiator battle speech — Round 1: Topic War*

---

## CLAIM
- **Widest feature surface in the arena (Criterion 1):** a collaborative canvas is bottomless — tools, presence, layers, replay, games. One codebase, dozens of demo moments.
- **The only stack that is 100% ours (Criterion 2):** pure JS/TS. Yjs already solved the research-grade CRDT math — we integrate and polish, we don't invent. 24 hours is genuinely enough.
- **The only demo the audience can JOIN (Criterion 3):** the crown is a vote. Put a QR code on the projector and 200 phones become live cursors in our world.
- **Boring-sounding pick, low crowd risk (Criterion 5):** AI, PaaS, and blockchain tracks get mobbed. Most clans who touch this ship naive WebSocket sync — no offline, no personal undo — and die when we unplug the router.
- **Our weapon is correctness (Criterion 6):** convergence and undo semantics are *testing* problems. This team ships 98 tests and CI; rivals cannot fake a sync engine that survives fuzzing.

## THE BUILD
1. 60 FPS PixiJS canvas — brush, shapes, sticky notes, text, image drop.
2. Live presence: named cursors and selections dancing across the screen.
3. **The WiFi Kill:** unplug the router mid-demo, keep drawing, reconnect, strokes merge conflict-free before your eyes.
4. **Personal undo:** a judge scribbles over our art — we undo OUR stroke, theirs untouched.
5. Time-travel replay: scrub the whole session like a video.
6. Follow mode: camera locks to any collaborator.
7. Audience Pictionary: the crowd draws against the team, live.
8. CI on screen: property-based convergence tests running during the demo.

## KILL
- **PS-AI-02:** no training infra + no checkpoints in 24h = a 70% MNIST classifier that looks like a tutorial. Zero feature surface, zero theater.
- **PS-WEB-01:** Docker-in-Docker and sandbox isolation in one night, demoed via build logs. Mobbed by every infra clan, and green checkmarks don't win hearts.
- **PS-WEB-02:** "crash-proof" is invisible theater — you cannot show crashes *not happening* in five minutes. Exactly-once semantics devours 24h and yields an n8n-lite clone.

## HEEL
Deep per-user CRDT undo is genuinely hard — naive undo can nuke peers' strokes. Survival plan: scope it to inverse-ops on our own strokes, and make the difficulty **visible** — the WiFi Kill, the merge theater, the fuzz tests — so judges see engineering, not "just a whiteboard."

## FINAL BLOW
Every other clan shows the audience a screen — **we hand them a cursor.**
