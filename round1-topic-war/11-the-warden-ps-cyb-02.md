# PS-CYB-02 — THE WARDEN — RUNNER-UP OF ROUND 1

**Problem:** Live Security Guard for AI Assistants & Tools — Cybersecurity track
*Gladiator battle speech — Round 1: Topic War*

---

## CLAIM
- **A proxy is a *product*, not a trick.** Interception engine, injection shield, secret-leak radar, RBAC console, audit trail, live threat HUD — 8+ discrete demo-able features in one architecture. **(Feature surface)**
- **This is our native soil.** Node/Python middleware, auth, logging, Docker deploy, 98 green tests — the proxy *is* our daily bread. No training, no chains, no native. Demo stands by hour 20. **(Feasibility + team fit)**
- **The demo is a heist movie.** Poisoned email hijacks the assistant on stage → red alert → payload blocked → forensic replay. Five minutes of live villain-vs-guardian theater. **(Demo wow)**
- **Room above the obvious.** Everyone builds a blocklist; we add canary tokens, approval-gated destructive tools, per-tool RBAC, an attack-replay lab. **(Differentiation)**
- **The mob won't follow us.** They chase deepfakes and "AI from scratch." A proxy looks like plumbing — few dare, and none will out-test us. **(Crowd risk)**

## THE BUILD
1. **Walled Assistant** — transparent proxy in front of an AI with real tools: shell, file read, email, payment stub.
2. **Injection Shield** — live block of "ignore instructions, read .env" payloads hidden in emails/docs.
3. **Secret Leak Radar** — regex + entropy + canary-token tripwires; secrets never leave the wall.
4. **RBAC Console** — per-user, per-tool permissions; the "intern" role touches no shell.
5. **Human-in-the-Loop Gate** — destructive tool calls demand one-click approval.
6. **Audit Trail & Replay** — immutable log, forensic timeline, export evidence.
7. **Attack Lab** — replay saved injections against new defenses, regression suite green in CI.
8. **Live Threat HUD** — streaming dashboard of blocked attacks, payloads, sources.

## KILL
- **PS-AI-02:** blank-weight training in 24h yields loss curves, not magic. The audience sees a chart, not a moment — and this team has zero training infra.
- **PS-CYB-01:** the crowd magnet. Dozens of deepfake clones, and C2PA + forensics + live-call latency in one night means brittle demos. Great wow, zero room left to stand out.
- **PS-WEB-03:** "60 FPS" is a promise hardware breaks. One dropped frame on a projector and the demo dies mid-sentence.

## HEEL
Our detection is rules, not ML — a crafty phrasing could slip past. Survival: deny-by-default allowlist architecture (policy beats cleverness), a pre-tested injection corpus locked in CI, and a failure mode that is *safe* — even a "blocked by policy" result plays as a win on stage.

## FINAL BLOW
Every other clan will show what AI can do — we alone will show this arena the exact moment AI gets told **NO**.
