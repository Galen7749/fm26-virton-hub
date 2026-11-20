import fmsave
import json

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)

with fmsave.open(SAVE_PATH) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    print("=== 比乙 (competition_id=1) 所有已赛比赛 ===")
    d2_fixtures = []
    for f in save.fixtures():
        if f.competition_id == 1 and f.played:
            home = team_to_club.get(f.home_team_id, f"team_{f.home_team_id}")
            away = team_to_club.get(f.away_team_id, f"team_{f.away_team_id}")
            d2_fixtures.append({
                "date": str(f.date),
                "home": home,
                "away": away,
                "score": f"{f.home_goals}-{f.away_goals}",
                "home_goals": f.home_goals,
                "away_goals": f.away_goals,
                "home_team_id": f.home_team_id,
                "away_team_id": f.away_team_id
            })
            
    d2_fixtures.sort(key=lambda x: x["date"])
    for fix in d2_fixtures:
        print(f"  {fix['date']} | {fix['home']} {fix['score']} {fix['away']}")

