# HEROKILL — The Winning Publishing Plan (Final Law)

*Champion: THE OFFLINE THEATER (50/60), gilded with the Layered Presence's ghost layers. One hall, one internet, four layers, zero excuses.*

## I. Where the website is published

On the public internet: nowhere. On silicon we own:

- **Host laptop** (16GB+, Docker): bare repos, post-receive hooks, Caddy, SQLite timeline; **cold spare**: identical disk-cloned laptop under the table.
- **Router**: isolated LAN, WAN taped empty — nothing in, nothing out. Fallbacks: host-to-judge ethernet or host hotspot, same SSID/IP.
- **Projector**: the status wall — live deploy timeline, RED CODE strobing. Fallback: HDMI monitor, then host screen.
- **Judge's loaner laptop**: the client; requested, joined, smoke-tested. Fallback: our third laptop, identical browser profile — the judge notices nothing.
- **Phone**: Round-0 portal upload plus war-room clock only; airplane mode after. Never in the demo path.
- **USB stick**: pre-baked images, certs, deck, static kit, golden run.

### Network and cert theater (exact mechanics)

- LAN 10.13.37.0/24; router DHCP reserves .10 for the host; clients get .20–.50.
- Router dnsmasq answers every `*.herokill.dev` query with 10.13.37.10 — the judge types a real domain; it resolves through 30cm of air; the judge machine is never touched. Secondary: one-line hosts entry if the router fights.
- **Cert kill shot**: real Let's Encrypt wildcard `*.herokill.dev`, minted at home via DNS-01 before the event — browsers verify at mint time, not visit time; 90-day validity; genuine offline padlock, zero CA installs on the judge machine. Backup: mkcert root imported into browser trust in 60 seconds. Caddy serves both paths.
- **Dogfood law**: the host is deployed to via HEROKILL's own post-receive hook — we deploy HEROKILL with HEROKILL.

## II. Venue runbook

**T-120** power strips, table layout, router up, WAN taped. **T-90** host boots; containers, DNS, cert live. **T-60** judge laptop configured — Wi-Fi joined, browser smoke-tested — or spare substituted. **T-45** projector wired; status wall live. **T-30** full dress rehearsal: push, deploy, RED CODE, rollback under 10s, resurrection. **T-15** Round-0 deck uploaded via tether; phone to airplane mode. **T-5** sit, breathe — we are the internet.

## III. Round-by-round publishing map

- **Round 0**: 8 slides, PDF, under 20MB, codename filename; uploaded once via hotspot; no names, links, or repo hints. Anonymity by rule and by cunning.
- **The Raid (24h)**: LAN assembled by hour 6, hardened by hour 12. Repo committed privately throughout. Static export kit built hours 4–10. Golden run recorded around hour 18. Devfolio drafted.
- **Arena Finals**: LAN live on the projector — deploy terminal left, RED CODE full-screen on the wall; the crowd watches something die and come back. Golden run armed. At score-lock: repo public, Devfolio live, Pages deployed if internet forgives us.

## IV. Fallback ladder

Router dies: ethernet or host hotspot, same SSID/IP (60s); cold-spare swap (120s); golden run, announced. Cert errors: mkcert import (60s); honest HTTP with the story (90s). No judge laptop: prepped, pre-trusted spare (30s). Projector fails: monitor, then laptop screens (60s). Total LAN collapse: USB static kit plus golden run — narrate, never fake.

## V. Artifact trail and anonymity law

Timing is integrity: while judges score, zero public footprint. At lock: README-as-landing-page — tagline above the fold, death-and-resurrection GIF, three-column grid (deploy, death system, certificates), five-line quickstart, architecture diagram, timeline screenshot, certificate gallery as scroll candy; clean commits, branch history, license. Devfolio mirrors the narrative with embedded demo video.

## VI. Static export kit

The marketing site as one zip of pure HTML — zero CDN calls, zero Google fonts, zero analytics; born offline, runs from USB in any browser on any laptop. One command deploys to GitHub Pages post-event; if the internet stays dead, the USB is the domain.

## VII. The golden run

Ninety seconds recorded around hour 18: git push, build log, green-lock browsing, chaos kill, RED CODE, rollback under 10s, resurrection, certificate minted. Full-screen browser tab, same terminal font and theme. Played only when the stage bleeds — and always announced: "This is our golden run, recorded last night." A confessed recording is theater; a faked live run is fraud.

## VIII. Post-event publishing

Scores lock, then: repo public, Devfolio live, Pages deployed, real domain if we win. On Tuesday the crowd finds a landing page with a certificate gallery — a project become a product. The hall was the battle; the internet is the aftermath, and we own it.
