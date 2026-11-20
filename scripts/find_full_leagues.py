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

    print("=== 扫描所有 club_count 在 18 或 20 的积分榜 ===")
    big_tables = []
    for lt in save.league_tables():
        if lt.club_count in [18, 20]:
            teams = [team_to_club.get(r.team_id, f"t_{r.team_id}") for r in lt.rows]
            teams_str = " ".join(teams)
            big_tables.append((lt.competition_id, lt.club_count, teams))

    print(f"找到 18/20 队规模的积分榜总数: {len(big_tables)}")
    for cid, count, teams in big_tables:
        sample = ", ".join(teams[:4])
        print(f"cid={cid} | {count}队 | 样本: {sample}")

