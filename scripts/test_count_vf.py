import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
with fmsave.open(save_path) as save:
    vf = [f for f in save.fixtures() if f.competition_id == 1 and f.home_goals is not None and (f.home_team_id == 245 or f.away_team_id == 245)]
    vf.sort(key=lambda x: x.date)
    print("Total D2 matches for Virton:", len(vf))
    for i, f in enumerate(vf, 1):
        print(f"[{i:2d}] {f.date.strftime('%Y-%m-%d')} stage={f.stage_id} {f.home_club_name} {f.home_goals}-{f.away_goals} {f.away_club_name}")
