import fmsave, glob, os, datetime

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    
    print("--- Odra Fixtures (Past & Next) ---")
    for f in s.fixtures():
        h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, ''))
        a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, ''))
        if "奥波莱" in h or "奥波莱" in a:
            if datetime.date(2026, 7, 1) <= f.date <= datetime.date(2026, 8, 30):
                print(f"  {f.date} | {h} vs {a} | Score: {f.home_goals} - {f.away_goals}")

    print("\n--- Virton Fixtures (Past & Next) ---")
    for f in s.fixtures():
        h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, ''))
        a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, ''))
        if "维尔通" in h or "维尔通" in a:
            if datetime.date(2026, 7, 1) <= f.date <= datetime.date(2026, 8, 30):
                print(f"  {f.date} | {h} vs {a} | Score: {f.home_goals} - {f.away_goals}")
