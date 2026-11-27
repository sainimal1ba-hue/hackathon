# PB-1 — THE OFFLINE THEATER

> Publishing War · gladiator speech · fought 2026-11-27
> Fate: **CHAMPION — 50/60.** Refined into the Final Law in `winner-publishing.md` (adopts the Layered Presence's golden-run insurance video, artifact trail, static export kit, dogfood doctrine, Round-0 anonymity cunning).

---

# THE OFFLINE THEATER — GLADIATOR PB-1

**We don't bring a website to a dead-internet venue. We bring the internet itself.**

## 1. THE HARDWARE STACK

- **HOST LAPTOP** (16GB+, Docker): the mini-cloud — bare repos, post-receive hooks, Caddy, SQLite timeline. Fallback: second identical laptop, disk-cloned, cold spare under the table.
- **ROUTER**: forms our isolated LAN. WAN port taped empty — nothing in, nothing out. Fallback: ethernet cable host→judge laptop, or host's built-in hotspot with same SSID/IP plan.
- **PROJECTOR**: the status wall — live deploy timeline, RED CODE strobing. Fallback: HDMI into a spare monitor; worst case, the host's own screen.
- **JUDGE'S LOANER LAPTOP**: the client. We request it, we configure it. Fallback: our third laptop, pre-loaded, identical browser profile — the judge notices nothing.
- **PHONE**: two jobs only — tethering for the single Round 0 portal upload, and the war-room clock. Never in the demo path.
- **USB STICK**: pre-baked Docker images, certs, deck. The escape hatch.

## 2. NETWORK & DOMAIN THEATER

LAN `10.13.37.0/24`. Router DHCP reserves `.10` for the host; clients get `.20–.50`. Router DNS (dnsmasq) answers every query for `*.herokill.dev` with `10.13.37.10`. Judge types a real-looking domain — resolves through 30cm of air.

**DNS override**: primary is router-level (we never touch the judge machine); secondary is a one-line hosts file if the router fights us.

**Cert kill shot**: mint a REAL Let's Encrypt wildcard `*.herokill.dev` at home via DNS-01 challenge before the hackathon. Browsers verify at mint time, not visit time — 90-day validity, genuine padlock, offline, zero warnings, no CA install on the judge machine. Backup: mkcert root imported into the browser trust store in 60 seconds during setup. Caddy serves both paths. The green lock lands because we manufactured trust before doors opened.

## 3. VENUE RUNBOOK

1. T-120min: power strips, table layout, router up, WAN taped.
2. T-90: host boots; containers, DNS, cert live.
3. T-60: judge laptop configured — Wi-Fi joined, browser smoke-tested — or spare substituted.
4. T-45: projector wired; status wall live.
5. T-30: full dress rehearsal — push → deploy → RED CODE → rollback <10s → resurrection.
6. T-15: Round 0 deck uploaded via phone tether. Phone to airplane mode.
7. T-5: sit. Breathe. We are the internet.

## 4. ROUND-BY-ROUND PUBLISHING

- **Round 0**: 8 slides, PDF, under 20MB, named by codename — anonymity intact. Uploaded once, via hotspot, before the offline clock means anything.
- **Round 1**: judges walk the floor. Loaner laptop in their hands. "Type app.herokill.dev." Green lock. They push. It deploys. We kill it. It resurrects in 9 seconds. SQLite timeline, Death Certificate. The URL story: a real domain on zero internet.
- **Round 2**: projector rig — deploy terminal left, RED CODE resurrection full-screen on the wall. The crowd doesn't read a pitch. They watch something die and come back. Vote with your eyes.

## 5. FALLBACK LADDER

- Router dies → ethernet or host hotspot, same SSID/IP. 60s.
- Cert errors → mkcert fallback root, or honest HTTP with the story. 90s.
- No judge laptop → our prepped spare, already trusted. 30s.
- Projector fails → monitor, then laptop screens. 60s.

## 6. WHY NOT PUBLIC HOSTING

Venue Wi-Fi is a corpse. Vercel and GitHub Pages chain our demo to a network we don't control — one dead access point kills the pitch. Worse: HEROKILL claims sovereign offline deploys. Hosting our own site on someone else's cloud is self-decapitation. Instead: cert pre-minted at home, repos mirrored on USB, everything served from silicon we can slap. Their weakness is the venue's. Our stack has none.

## 7. KILL STROKE — "THE LAYERED PRESENCE"

The rival splits 24 precious hours between offline build and marketing polish, depends on the corpse Wi-Fi twice over, and ends with a weaker stage: a link anyone can visit from their couch. We hand judges one URL, one genuine padlock, one resurrection — hardware they can touch on our table. They demonstrated a website. **We manufactured an internet.** There is no second layer. There is only ours.
