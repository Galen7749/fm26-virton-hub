import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 5340026
BEL_D2_CID = 100000000 # Wait, check BEL_D2_CID in sync_fm.py

with fmsave.open(save_path) as save:
    club_names = {t.team_id: c.name for c in save.clubs() for t in c.teams}
    
    # Let's inspect fixtures
    fixtures = [f for f in save.fixtures() if f.home_goals is not None and (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID)]
    fixtures.sort(key=lambda x: x.date)
    print(f"Virton fixtures: {len(fixtures)}")
    for i, f in enumerate(fixtures):
        is_home = (f.home_team_id == VIRTON_TEAM_ID)
        home = club_names.get(f.home_team_id, "Home")
        away = club_names.get(f.away_team_id, "Away")
        opp_name = away if is_home else home
        vg = f.home_goals if is_home else f.away_goals
        og = f.away_goals if is_home else f.home_goals
        print(f"R{i+1:02d} ({f.date}): {home} {f.home_goals} - {f.away_goals} {away} | Virton {vg} - Opp {og} ({opp_name})")
