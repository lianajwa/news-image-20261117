[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/lianajwa/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/lianajwa/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World in One Day — 17 November 2026

Entry for make.fun bounty **news-image-20261117** — "Sum up 17 November's
world news in one image" ($250, 50 places paid; deadline Thu 19 Nov 2026
00:00 UTC / 07:00 WIB). Bounty page:
https://make.fun/bounty/news-image-20261117

## The image

A newspaper front page, drawn in this session with Pillow (`render.py`,
vector shapes + system fonts, so every word is spelled exactly as shown),
1024×1024 px.

**Lead — The Gulf:** U.S. jets strike an Iranian missile site on Qeshm
Island; Iran fires drones at U.S. facilities in Bahrain and Kuwait; a
fourth tanker catches fire in the Strait of Hormuz in 24 hours; Trump
says the U.S. takes an alleged Iranian dirty-bomb plot against
Washington "very seriously".

**2 — Kerch Bridge:** Ukraine's strike partly collapses the bridge to
Crimea; a road span falls into the strait. Russia answers by striking
bridges in Kyiv, and Moldova closes its airspace after Russian drones
cross its border.

**3 — Shenzhen:** Xi Jinping opens the APEC summit in Shenzhen; Trump
flies in from Manila — where Quad leaders announced critical-minerals
pacts — for a first trilateral meeting with Xi and Putin.

**Also today:** Mongolia's president resigns in a corruption scandal;
Japan scrambles jets as Russian planes breach its airspace; Britain,
Australia, Canada and Italy urge Israel to open Gaza crossings for aid;
Gérard Depardieu admits a sexual assault charge in Paris.

Sources checked 18 Nov 2026: CNN, BBC, Al Jazeera, The Guardian,
Foreign Exchanges — all converging on the same three lead stories above.

## Program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. No network, no time, no randomness —
two runs write identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the image
- `render.py` — the script that drew `entry.png` in this session
- `README.md` — this file
- `LICENSE` — MIT

## Verify

```sh
python3 main.py   # writes /output/entry.png
python3 main.py   # second run, same bytes
sha256sum /output/entry.png
```
