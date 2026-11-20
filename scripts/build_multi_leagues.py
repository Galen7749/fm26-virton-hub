import fmsave
import json
import os

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)
VIRTON_TEAM_ID = 245
DATA_DIR = r"I:\fm26-virton-hub\web\src\data"

with fmsave.open(SAVE_PATH) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    # 1. 提取比乙 (cid=1)
    d2_table = []
    for lt in save.league_tables():
        if lt.competition_id == 1:
            for r in lt.rows:
                cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                d2_table.append({
                    "position": r.position,
                    "team_name": cname,
                    "played": r.played,
                    "won": r.won,
                    "drawn": r.drawn,
                    "lost": r.lost,
                    "gf": r.goals_for,
                    "ga": r.goals_against,
                    "gd": r.goals_for - r.goals_against,
                    "points": r.points,
                    "is_my_team": (r.team_id == VIRTON_TEAM_ID)
                })
            d2_table.sort(key=lambda x: x["position"])
            break

    # 2. 提取比甲 (cid=0)
    d1_table = []
    for lt in save.league_tables():
        if lt.competition_id == 0:
            for r in lt.rows:
                cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                d1_table.append({
                    "position": r.position,
                    "team_name": cname,
                    "played": r.played,
                    "won": r.won,
                    "drawn": r.drawn,
                    "lost": r.lost,
                    "gf": r.goals_for,
                    "ga": r.goals_against,
                    "gd": r.goals_for - r.goals_against,
                    "points": r.points,
                    "is_my_team": False
                })
            d1_table.sort(key=lambda x: x["position"])
            break

    print(f"比乙队数: {len(d2_table)}")
    print(f"比甲队数: {len(d1_table)}")

    # 组装多联赛体系
    multi_leagues = {
        "current_club": {
            "name": "维尔通精英",
            "name_en": "RE Virton",
            "stage_step": 1,
            "status": "流浪执教第 1 站",
            "league_name": "比乙（挑战者职业联赛）",
            "target_league": "比甲（Jupiler Pro League）"
        },
        "leagues": [
            {
                "id": "bel_d2",
                "name": "比乙 (挑战者职业联赛)",
                "short_name": "比乙",
                "flag": "🇧🇪",
                "tag": "当前所处",
                "is_current": True,
                "round": 3,
                "table": d2_table
            },
            {
                "id": "bel_d1",
                "name": "比甲 (Jupiler Pro League)",
                "short_name": "比甲",
                "flag": "🇧🇪",
                "tag": "上级联赛 / 目标",
                "is_parent": True,
                "round": 4,
                "table": d1_table
            },
            {
                "id": "pl",
                "name": "英格兰足球超级联赛",
                "short_name": "英超",
                "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
                "tag": "五大联赛",
                "round": 2,
                "table": [
                    { "position": 1, "team_name": "曼彻斯特城", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 6, "ga": 1, "gd": 5, "points": 6 },
                    { "position": 2, "team_name": "阿森纳", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 4, "ga": 0, "gd": 4, "points": 6 },
                    { "position": 3, "team_name": "利物浦", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 4, "ga": 0, "gd": 4, "points": 6 },
                    { "position": 4, "team_name": "切尔西", "played": 2, "won": 1, "drawn": 0, "lost": 1, "gf": 6, "ga": 4, "gd": 2, "points": 3 },
                    { "position": 5, "team_name": "纽卡斯尔联", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 2, "ga": 1, "gd": 1, "points": 4 },
                    { "position": 6, "team_name": "托特纳姆热刺", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 5, "ga": 1, "gd": 4, "points": 4 },
                    { "position": 7, "team_name": "阿斯顿维拉", "played": 2, "won": 1, "drawn": 0, "lost": 1, "gf": 2, "ga": 3, "gd": -1, "points": 3 },
                    { "position": 8, "team_name": "布莱顿", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 5, "ga": 1, "gd": 4, "points": 6 },
                    { "position": 9, "team_name": "曼彻斯特联", "played": 2, "won": 1, "drawn": 0, "lost": 1, "gf": 2, "ga": 2, "gd": 0, "points": 3 },
                    { "position": 10, "team_name": "西汉姆联", "played": 2, "won": 1, "drawn": 0, "lost": 1, "gf": 3, "ga": 2, "gd": 1, "points": 3 }
                ]
            },
            {
                "id": "laliga",
                "name": "西班牙足球甲级联赛",
                "short_name": "西甲",
                "flag": "🇪🇸",
                "tag": "五大联赛",
                "round": 2,
                "table": [
                    { "position": 1, "team_name": "皇家马德里", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 5, "ga": 0, "gd": 5, "points": 6 },
                    { "position": 2, "team_name": "巴塞罗那", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 4, "ga": 1, "gd": 3, "points": 6 },
                    { "position": 3, "team_name": "马德里竞技", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 5, "ga": 2, "gd": 3, "points": 4 },
                    { "position": 4, "team_name": "毕尔巴鄂竞技", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 2, "ga": 1, "gd": 1, "points": 4 },
                    { "position": 5, "team_name": "比利亚雷亚尔", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 4, "ga": 3, "gd": 1, "points": 4 }
                ]
            },
            {
                "id": "ligue1",
                "name": "法国足球甲级联赛",
                "short_name": "法甲",
                "flag": "🇫🇷",
                "tag": "五大联赛",
                "round": 2,
                "table": [
                    { "position": 1, "team_name": "巴黎圣日耳曼", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 10, "ga": 1, "gd": 9, "points": 6 },
                    { "position": 2, "team_name": "摩纳哥", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 4, "ga": 0, "gd": 4, "points": 6 },
                    { "position": 3, "team_name": "里尔", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 4, "ga": 0, "gd": 4, "points": 6 },
                    { "position": 4, "team_name": "马赛奥林匹克", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 7, "ga": 3, "gd": 4, "points": 4 },
                    { "position": 5, "team_name": "朗斯", "played": 2, "won": 2, "drawn": 0, "lost": 0, "gf": 3, "ga": 0, "gd": 3, "points": 6 }
                ]
            }
        ]
    }

    out_file = os.path.join(DATA_DIR, "standings.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(multi_leagues, f, ensure_ascii=False, indent=2)
    print(f"[✓] 多联赛数据已写入: {out_file}")

