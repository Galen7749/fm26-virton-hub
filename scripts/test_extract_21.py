import fmsave
import datetime
import json
from pathlib import Path

SAVE_DIR = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games")
save_files = list(SAVE_DIR.glob("*.fm"))
save_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
latest = save_files[0]
print(f"Opening {latest.name}...")

VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1

with fmsave.open(str(latest)) as save:
    club_names = {}
    for c in save.clubs():
        for t in c.teams:
            club_names[t.team_id] = c.name

    fixtures = [
        f for f in save.fixtures()
        if f.competition_id == BEL_D2_CID
        and (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID)
        and f.home_goals is not None
    ]
    fixtures.sort(key=lambda x: x.date)
    print(f"Total fixtures: {len(fixtures)}")

    # Let's inspect fixture properties
    f0 = fixtures[8] # Round 9
    print(f"Round 9 fixture props: {dir(f0)}")
    print(f"Date: {f0.date}, Home: {club_names.get(f0.home_team_id)} ({f0.home_goals}), Away: {club_names.get(f0.away_team_id)} ({f0.away_goals})")
    
    # Check player match stats
    virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == VIRTON_CLUB_UID or getattr(p, 'team_id', None) == VIRTON_TEAM_ID}
    print(f"Virton players count: {len(virton_uids)}")

    # Check match stats for round 9 date
    r9_date = f0.date
    r9_stats = [pms for pms in save.player_match_stats() if pms.player_uid in virton_uids and pms.date == r9_date]
    print(f"Round 9 player match stats count: {len(r9_stats)}")
    for pms in r9_stats:
        p_name = next((p.name for p in save.players() if p.uid == pms.player_uid), str(pms.player_uid))
        print(f"  {p_name}: min={pms.minutes}, entered={pms.entered_at_minute}, rating={pms.rating}, goals={getattr(pms, 'goals', None)}, assists={getattr(pms, 'assists', None)}")
