# Mod 12

A PWA game to memorize the guitar neck with mod-12 arithmetic. It is a prototype. If it holds attention, it becomes a native game.

## The method

- Notes are numbers: C=1, C♯=2, D=3 … A♯=11, B=12 (0). All arithmetic is mod 12.
- On the B string the fret number is the note number.
- The other strings are translations of the B string: E strings +5, G −4, D +3, A −2.
- Chords and scales are fixed offsets from a root (major chord: r, r+4, r+7).

## Game design

Goal: move from calculation to recall. The game measures this with answer time. An answer below 2 seconds counts as "instant".

| Element | Mechanism | Purpose |
|---|---|---|
| Set | 60 seconds, 3 strings (lives), one-tap restart | Opportunity and quick repeatability |
| Loot draw | Pick 1 of 3 face-down picks after each set. The other two are revealed. | Unpredictable reward, near-miss |
| Golden note | 8% of questions score ×3 and give coins | Unpredictable reward inside the set |
| Combo | Multiplier up to ×4, +2 seconds at each 10 | Flow, loss aversion |
| Neck heatmap | 78 cells, 6 mastery levels | Collection, visible progress |
| Out of tune | Mastery decays on a spaced-repetition schedule (10 min, 1, 3, 7, 16 days) | Reason to return, real retention |
| Daily Gig | One attempt per day, 2× XP, two loot draws | Scarcity |
| Streak and freezes | Daily streak, freeze protects one missed day | Loss aversion |
| Quests | Three per day | Short-term goals |
| Stars | Per stage. ★★ and ★★★ need a fast average answer time | Direct measure of recall |
| Picks | 16 collectible picks in 4 rarities, change the accent colour | Collection |

Rewards are tied to learning: only instant answers raise mastery, and a level above 1 rises only after its review interval has passed.

## Stages

1. The Code (note ↔ number)
2. B String, 3. E Strings, 4. G String, 5. D String, 6. A String
7. Whole Neck (name the note, or find the note on a string)
8. Chords (tap the notes on the mod-12 dial)
9. Scales

A stage opens when the previous stage has one star. Settings has an "Unlock all stages" switch.

## Run

A service worker needs HTTP. Serve the folder, then open the URL:

```bash
python3 -m http.server 8137 --directory Mod12
```

To install on an iPhone, the folder must be on an HTTPS host. Open it in Safari, then Share → Add to Home Screen.

## Files

- `index.html` — the complete game (HTML, CSS, JavaScript, no dependencies)
- `manifest.webmanifest`, `sw.js`, icons — PWA shell and offline cache
- Progress is stored in `localStorage` under `mod12.v1`

## Not built yet

- Chord and scale shapes on the neck (the dial drills the arithmetic only)
- Frets above 12
- Sync between devices
