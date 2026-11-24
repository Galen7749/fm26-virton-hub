import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 245

with fmsave.open(save_path) as save:
    # check what comp 131, 0, 643 are
    all_virton = [f for f in save.fixtures() if (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID) and f.home_goals is not None]
    all_virton.sort(key=lambda x: x.date)
    
    club_names = {t.team_id: c.name for c in save.clubs() for t in c.teams}
    
    print("All non-BEL-D2 fixtures:")
    for f in all_virton:
        if f.competition_id != 1:
            home = club_names.get(f.home_team_id, f.home_team_id)
            away = club_names.get(f.away_team_id, f.away_team_id)
            print(f"  {f.date} | comp={f.competition_id} | stage={getattr(f,'stage_id',None)} | {home} {f.home_goals}-{f.away_goals} {away}")
    
    # Try to find Belgian top division competition id
    # Check competitions via fixtures
    bel_comps = {}
    for f in save.fixtures():
        if f.home_goals is not None and f.competition_id in [0, 131, 643, 2]:
            if f.competition_id not in bel_comps:
                h = club_names.get(f.home_team_id, '?')
                a = club_names.get(f.away_team_id, '?')
                bel_comps[f.competition_id] = f"{h} vs {a} ({f.date})"
    print("\nSample for each comp:")
    for cid, sample in bel_comps.items():
        print(f"  comp={cid}: {sample}")
