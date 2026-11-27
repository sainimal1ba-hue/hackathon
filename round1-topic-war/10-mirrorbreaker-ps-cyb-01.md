# PS-CYB-01 — MIRRORBREAKER

**Problem:** Deepfake Shield & Live Fake-Media Detector — Cybersecurity track
*Gladiator battle speech — Round 1: Topic War*

---

## CLAIM
- **Feature surface (C1):** TWO products in one — offense (poison your media against AI cloning) and defense (live deepfake radar in calls). Ten-plus demoable surfaces, not one trick.
- **24h feasibility (C2):** Zero model training. We integrate pre-trained forensics models behind a Python service and wrap a TypeScript WebRTC extension around them — pure full-stack plumbing, our exact muscle.
- **Demo wow (C3):** Mid-pitch, a "teammate" joins the call as a deepfake; our extension flashes red with a live trust score. Audiences don't understand CRDTs — but everyone fears a fake video call.
- **Differentiation room (C4):** Every clan that touches this builds a detector. The poison side — immunize your face before scammers steal it — is the twist nobody will think of.
- **Crowd risk (C5):** Deepfakes *look* like ML research, so full-stack clans flee to chatbots and budget apps. Thin field, fat advantage.

## THE BUILD
1. **Clone Poisoner** — upload selfie + voice clip; get perturbed "vaccine" media that wrecks face-swap/voice-clone training.
2. **C2PA Credentials** — every protected asset gets signed provenance; tampering flagged instantly.
3. **WebRTC Browser Extension** — live trust-score overlay on real video calls, sampled in real time.
4. **Forensics Dashboard** — blink-rate, lip-sync error, face-landmark jitter, audio-spectral anomaly charts.
5. **Proof-of-Human Handshake** — cryptographic liveness challenge fired at a suspicious caller.
6. **Voice Clone Lie Detector** — cloned sample vs. original, caught live.
7. **Tamper Timeline** — CI-tested detection pipeline with an audit log; our 98-tests discipline, weaponized.

## KILL
- **PS-AI-02:** We own no ML training infra; in 24h you demo a loss curve, not a product. Nobody votes for gradient descent.
- **PS-AI-01:** Stage noise kills wake-words, hackathon laptops choke on local LLMs — and half the arena builds voice assistants. Crowd risk: fatal.
- **PS-CYB-03:** Your whole demo depends on an attacker showing up live. No intruder, no theater. We *manufacture* our villain on stage.

## HEEL
Real-time inference is our weak flank — detectors are heavy and false positives burn trust. Survival: sample frames server-side (Docker + CI keeps the pipeline honest), ship a pre-trained lightweight model in hour one, and frame output as an explainable assistive trust score, never a verdict.

## FINAL BLOW
Every other clan demos software — we demo the crime the audience already fears, then stop it live.
