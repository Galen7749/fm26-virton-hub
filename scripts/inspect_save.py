import fmsave
import json
from pathlib import Path

SAVE_DIR = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games")
save_files = list(SAVE_DIR.glob("*.fm"))
save_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
latest = save_files[0]
print(f"Latest save: {latest.name} ({latest.stat().st_size / 1024 / 1024:.2f} MB)")

VIRTON_TEAM_ID = 245
BEL_D2_CID = 1

with fmsave.open(str(latest)) as save:
    team_names = {}
    for c in save.clubs():
        for t in c.teams:
            team_names[t.team_id] = c.name

    fixtures = [
        f for f in save.fixtures()
        if f.competition_id == BEL_D2_CID
        and (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID)
        and f.home_goals is not None
    ]
    fixtures.sort(key=lambda x: x.date)
    print(f"Total finished fixtures for Virton in D2: {len(fixtures)}")
    for i, f in enumerate(fixtures):
        ht = team_names.get(f.home_team_id, f.home_team_id)
        at = team_names.get(f.away_team_id, f.away_team_id)
        d_str = str(f.date)[:10]
        print(f"Round {i+1}: {d_str} | {ht} {f.home_goals} - {f.away_goals} {at}")
