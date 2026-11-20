import json
from pathlib import Path

data = json.loads(Path(r"I:\fm26-virton-hub\scripts\virton_players_season.json").read_text(encoding="utf-8"))

seen = set()
unique = []
for p in data:
    k = (p['name'], p['starts'], p['goals'], p['assists'], p['yellow_cards'])
    if k not in seen:
        seen.add(k)
        unique.append(p)

print(f"Total unique records: {len(unique)}")
for p in unique:
    print(f"{p['name']:<25} Apps:{p['starts']}(+{p['subs']}) G:{p['goals']} A:{p['assists']} Rating:{p['rating']:.2f} xG:{p['xg']:.2f} Shots:{p['shots']} KeyP:{p['key_passes']} Tackles:{p['tackles']} Yel:{p['yellow_cards']}")
