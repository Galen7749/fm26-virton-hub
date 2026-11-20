import fmsave

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

    for lt in save.league_tables():
        teams = [team_to_club.get(r.team_id, f"t_{r.team_id}") for r in lt.rows]
        teams_str = " ".join(teams)
        if '安德莱赫特' in teams_str:
            print(f"cid={lt.competition_id}, count={lt.club_count}, teams: {teams[:4]}")

