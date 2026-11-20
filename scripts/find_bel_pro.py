import fmsave
import json
import os

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

    print("=== 提取各大联赛 ===")
    
    # 查找比甲 (competition_id=2218 或其他包含 Anderlecht, Club Brugge 的)
    for lt in save.league_tables():
        teams = [team_to_club.get(r.team_id, f"t_{r.team_id}") for r in lt.rows]
        teams_str = " ".join(teams)
        if '布鲁日足球俱乐部' in teams_str and '皇家安德莱赫特' in teams_str and lt.club_count == 16:
            print(f"[找到比甲!] cid={lt.competition_id}, teams={lt.club_count}")
            for r in lt.rows:
                print(f"  {r.position}. {team_to_club.get(r.team_id)} | {r.played}场 | {r.points}分")
            break

