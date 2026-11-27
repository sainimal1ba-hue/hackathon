# PS-AI-03 — CONSUL COORDINUS

**Problem:** Autonomous Team of AI Problem-Solvers (AI War Room) — AI & Machine Learning track
*Gladiator battle speech — Round 1: Topic War*

---

## CLAIM
- **Feature surface (C1):** A war room is a feature factory — detector agents, investigator swarms, sandbox lab, repair executor, verifier, mission-control dashboard, live incident timeline, auto-postmortems. Every agent and every incident type is a separate demo-able feature.
- **24h feasibility + team fit (C2/C6):** LangGraph/CrewAI is *plumbing*, not ML training. Our Docker, GitHub Actions, and 98-green-tests discipline IS the substrate: the war room is literally CI/CD turned into theater. No blockchain, no native mobile, no GPUs needed.
- **Demo wow (C3):** A live outage is a five-act play — sirens, swarm, surgery, resurrection, green light. Audiences vote for visible cause and effect, and we cause the effect ourselves.
- **Differentiation room (C4):** The obvious build is "agents fix things." Nobody else will think of the **Chaos Agent that attacks our own system on stage**, or confidence-scored repair plans with a human approval gate.
- **Crowd risk (C5):** "Multi-agent coordination" scares clans — they'll stampede to voice assistants. Thin battlefield, easy to dominate.

## THE BUILD
1. Mission-control dashboard: fleet map, red alarms, live MTTR counter.
2. Detector agents watching logs/metrics — flag anomaly in seconds.
3. Investigator swarm: triage, blast-radius graph, root-cause hypotheses with confidence scores.
4. Sandboxed staging: suspect fix replayed on a containerized clone before touching "prod".
5. Repair agents executing real actions — rollback, restart, failover, visibly done.
6. Verifier agent: green checkmarks, auto-generated incident postmortem.
7. **Chaos lever: an audience member presses the button** that breaks the system — war room heals it live.
8. Human-in-the-loop approval gate for destructive actions.

## KILL
- **PS-AI-02:** Blank weights + zero training infra = one sad loss curve and a 60% accuracy toy. That's ONE feature. Judges vote for theater, not tensors.
- **PS-AI-01:** The most crowded lane, and offline STT plus PyAutoGUI coordinate brittleness dies on unfamiliar accents and demo machines. One flub and the voice demo is silence.
- **PS-WEB-01:** A PaaS demo is a website deploying — boring, and rollback only looks good if something breaks, which they pray won't. Ours breaks *on purpose*, and that's the hero moment.

## HEEL
Honest truth: agent reasoning is nondeterministic and API-dependent — a wobbly demo kills us. Survival plan: hybrid brain — rule-based playbooks drive deterministic actions, LLM plays the reasoning narrator on top; incidents are seeded, not random; recorded-trace fallback if APIs choke. Our test discipline guarantees every repair path is proven before it hits stage.

## FINAL BLOW
When the dashboard goes red, the machines heal themselves in front of a screaming audience, and the breaker of worlds is standing among the voters — no loss curve on Earth out-votes that.
