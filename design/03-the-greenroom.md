# DG-3 — THE GREENROOM

> Design War · gladiator speech · fought 2026-11-27
> Fate: FELL — 48/60. Surviving elements adopted into the Final Law (THE OPERA): green-lock theater (fake browser chrome + padlock beat), accessibility law (color + icon + label, prefers-reduced-motion, arrow-key scrubber), IntersectionObserver entrances, screenshot-bait certificate copy.

---

# THE GREENROOM — I Make Death Adorable

200 students in a dark auditorium don't vote for terminals — they vote for what made them smile while looking funded. Warmth wins the crowd; engineering still wins the judges.

## 1 BRAND
Lowercase "herokill" wordmark; the "o" is the mascot's face — a tiny container with dot-eyes. Logo: rounded-square container (a Docker wink), heartbeat line flatlining left, one green pulse right — works at favicon scale. Tagline: "Watch it die. Bring it back. Learn why." Voice: warm, dry engineer-friend; comic dignity, never gore. Buttons say "Deploy something doomed." Statuses say "It died. It's back. Autopsy attached."

## 2 COLOR
Background #FAF7F2 warm paper; surfaces #FFFFFF and #F3EFE8; border #E7E0D5; ink #1A1D1F; muted #6B645A. Revival green #00C874 (hover #00A862, glow rgba(0,200,116,.25)) — reserved exclusively for resurrection, so every flash is dopamine. Death red #FF5A5F on tint #FFEDEC: coral, not alarm. Chaos taxonomy: leak blue #4AA8FF, dependency-bomb violet #7C5CFF, kill-9 amber #FFB020. Stripe-warmth reads commercial; discipline makes the mascot pop.

## 3 TYPE
Display: Bricolage Grotesque 700/800 — friendly, characterful SaaS. Body: Inter 400/500/600 at 16/1.6. Mono: IBM Plex Mono 400/600 for exit codes and certificates. Scale 12/14/16/20/28/40/56/72, clamp() fluid; mono eyebrows 13px uppercase.

## 4 LAYOUT
12-col grid, 1200px max, 8px base unit, 24px radii, 96px section rhythm. Homepage top→bottom:
1. **Nav** — sticky pill, blur, logo, CTA.
2. **Hero** — headline left; right, a soft product card where a real deploy dies and resurrects on loop.
3. **Proof strip** — "ships on student laptops."
4. **The Loop** — three cards: PUSH, DIE, RESURRECT, mascots performing each.
5. **Chaos Playground** — full-bleed sandbox.
6. **Resurrection Timeline** — playhead replay demo.
7. **Death Certificates** — hover-flip gallery.
8. **Status Garden** — apps as potted plants.
9. **Pricing simulator.**
10. **Footer** — cert-stamped "HEROKILL, est. 24h."

## 5 INTERACTIVITY
1. **Chaos Playground** — pick the poison: leak, dependency bomb, or kill -9 — JUDGE'S TRIGGER; the caged container drains, RED CODE trips, rollback fires <10s, countdown runs. The demo the crowd shouts at.
2. **Scroll resurrection** — mascot flatlines past "DIE," gets green CPR at "RESURRECT." The whole pitch without a click.
3. **Death Certificates** — hover flips a stamped card to its exit-code autopsy (137 = OOM, "ran out of snacks"). Collectible, screenshot-bait.
4. **Incident scrubber** — drag the playhead across the SQLite event stream; logs run backwards, graphs rewind. THE ROAR moment.
5. **Pricing simulator** — toggle traffic and chaos tiers; mock invoices and uptime animate. Reads funded.
6. **Status Garden** — healthy plants bloom green, dead ones swoon, one-click revive.
7. **Green-lock theater** — fake browser chrome, padlock, pre-minted cert, offline DNS note. Trust, staged.

## 6 MOTION
Mascot: squash-and-stretch swoons, X-eyes, 400ms falls; one green pulse ring, 600ms, never gore. Entrances: cubic-bezier(.22,1,.36,1). Swoons: (.45,0,.55,1). One hero motion per viewport; red is attention, green is resolution. The resurrection timer freezes at 00:07 so the audience finishes the countdown.

## 7 IMAGES
STYLE CORE, appended to every prompt: flat vector illustration, soft rounded shapes, warm off-white #FAF7F2 background, palette of #00C874 green, #FF5A5F coral, #7C5CFF violet, subtle paper grain, friendly mascot energy, Stripe-style marketing art, no text.
1. Hero portrait — cute rounded-square container character, dot-eyes, heartbeat halo, waving.
2. Death swoon, three frames — mascot overheating, blushing coral, X-eyes, dramatic backward fall.
3. Resurrection — mascot sitting up inside expanding green pulse rings, sparkling.
4. Chaos icons — bomb, dripping faucet, hammer labeled 9, tiny grinning characters.
5. Status garden — potted app-plants in a sunny warm conservatory, one plant swooning.
6. Autopsy lab — mascot on a clean lab table, clipboard certificate, magnifying glass.
7. OG card — mascot beside the wordmark, single green pulse.

## 8 KILL STROKES
THE VAULT: terminal-brutalism earns judges' respect and the crowd's glaze. Black rectangles don't make 200 students shout — shouters are voters, and respect without love dies in audience-vote finals. THE OPERA: cinematic dark motion is a render-budget mirage — in 24h it ships half-finished, fights the projector's wash, and darkness says "hacker theatre," not "product I'd trust with my app." Only I feel funded AND hug the room.

## 9 BUILDABILITY
Hours 0–2: tokens, grid, nav. 2–5: mascot as SVG frame-swaps, no rigging. 5–9: playground as a state machine over mock events. 9–12: scrubber from pre-recorded JSON on a range input. 12–14: hover-flip certificates. Trick: everything is CSS transforms plus IntersectionObserver; WebSockets only if the wire proves live, else replay. Risk: art quality — one style pass across all seven images at hour 20. Freeze at 22, rehearse the ROAR.

Green is life after death. The crowd votes with eyes and laughter. HEROKILL, served warm — THE GREENROOM.
