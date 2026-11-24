import fmsave, glob, os, datetime, json

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

fixtures_week = []

with fmsave.open(p) as s:
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    comps = {getattr(c, 'id', getattr(c, 'competition_id', None)): c.name for c in s.competitions()}
    d_start = datetime.date(2026, 7, 25)
    d_end = datetime.date(2026, 8, 1)
    
    for f in s.fixtures():
        if d_start <= f.date <= d_end and f.home_goals is not None:
            h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, f.home_club_name or ""))
            a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, f.away_club_name or ""))
            cname = comps.get(f.competition_id, f.competition_name or "友谊赛")
            fixtures_week.append({
                "date": str(f.date),
                "competition": cname,
                "competition_id": f.competition_id,
                "home": h,
                "away": a,
                "home_goals": f.home_goals,
                "away_goals": f.away_goals,
                "stadium": f.stadium_name or ""
            })

print(f"Total fixtures found: {len(fixtures_week)}")
with open("scripts/week_fixtures.json", "w", encoding="utf-8") as out:
    json.dump(fixtures_week, out, ensure_ascii=False, indent=2)
print("Saved to scripts/week_fixtures.json")
