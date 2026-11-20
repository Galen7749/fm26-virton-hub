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

    # 查意甲 (cid=3560)
    for lt in save.league_tables():
        if lt.competition_id == 3560:
            print("=== 意甲 (cid=3560) ===")
            for r in lt.rows:
                print(f"  {r.position}. {team_to_club.get(r.team_id)} | {r.played}场 | {r.points}分")
            break

