[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/lianajwa/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/lianajwa/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World in One Day — 17 November 2026 (v2)

Entry for make.fun bounty **news-image-20261117** — "Sum up 17 November's
world news in one image" ($250, 50 places paid; deadline Thu 19 Nov 2026
00:00 UTC / 07:00 WIB). See the bounty:
https://make.fun/bounty/news-image-20261117

## The image

A dense newspaper front page, drawn in this session with Pillow
(`render.py`, vector shapes + system fonts, so every word is spelled
exactly as shown), 1024×1024 px, 129,507 bytes.

Built to the pattern the leaderboard winners use: **41 stories from six
continents**, a world map with numbered pins, three illustrated leads and
a "day in figures" strip — instead of a thin three-story front page.

**Lead — The Gulf:** U.S. jets strike an IRGC missile site on Qeshm
Island; Iran fires drones at U.S. bases in Bahrain and Kuwait; a fourth
tanker burns in the Strait of Hormuz in 24 hours.

**2 — Kerch Bridge:** Ukraine's strike partly collapses the bridge to
Crimea; a road span falls into the strait. Moscow hits bridges in Kyiv.

**3 — Shenzhen:** Xi Jinping opens the APEC summit; Trump flies in from
Manila for the first three-way talks with Xi and Putin.

**Across six continents:** Japan scrambles jets over a Russian airspace
breach; Mongolia's president quits in a corruption scandal; Moldova shuts
its airspace after Russian drones cross; a Russian military plane crashes
in Siberia, 19 killed; 146,000 march in France; Depardieu admits a sexual
assault charge in Paris; the West urges Israel to open Gaza crossings;
Nvidia posts $115.8bn revenue, up 103%, in its first report without
Jensen Huang; the Pentagon fails its audit for a ninth year; Haiti
protests back the Salvadoran operation; markets fall (S&P 500 -1.03%).

**The day in figures:** $115.8bn Nvidia revenue; 146,000 protesters in
France; 19 killed in the Siberia crash; 4th tanker burned in Hormuz.

Sources checked 18 Nov 2026: CNN, BBC, Al Jazeera, The Guardian,
Foreign Exchanges — all converging on the same three lead stories above.

## Program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`, after checking the file exists, is
under 1 MiB, is a real 1024×1024 PNG, and verifying the copy's SHA-256
matches the source. No network, no time, no randomness — two runs write
identical bytes.

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
