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

    # 1. 提取比乙 (cid=1, 15队)
    bel_d2_table = []
    for lt in save.league_tables():
        if lt.competition_id == 1:
            for r in lt.rows:
                cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                bel_d2_table.append({
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
            bel_d2_table.sort(key=lambda x: x["position"])
            break

    # 2. 提取比甲 (cid=0, 18队)
    bel_d1_table = []
    for lt in save.league_tables():
        if lt.competition_id == 0:
            for r in lt.rows:
                cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                bel_d1_table.append({
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
            bel_d1_table.sort(key=lambda x: x["position"])
            break

    # 3. 提取意甲 (cid=3560, 20队)
    serie_a_table = []
    for lt in save.league_tables():
        if lt.competition_id == 3560:
            for r in lt.rows:
                cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                # 清洗部分未授权化名
                clean_name = cname
                if "蓝黑米兰" in cname: clean_name = "国际米兰"
                elif "螺丝刀米兰" in cname: clean_name = "AC米兰"
                elif "帕耳忒诺珀" in cname: clean_name = "那不勒斯"
                elif "天蓝卡皮托利尼" in cname: clean_name = "拉齐奥"
                elif "贝加莫" in cname: clean_name = "亚特兰大"
                serie_a_table.append({
                    "position": r.position,
                    "team_name": clean_name,
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
            serie_a_table.sort(key=lambda x: x["position"])
            break

    # 4. 英超完整 20 队
    pl_teams = [
        ("曼彻斯特城", 2, 2, 0, 0, 6, 1, 6),
        ("阿森纳", 2, 2, 0, 0, 4, 0, 6),
        ("利物浦", 2, 2, 0, 0, 4, 0, 6),
        ("布莱顿", 2, 2, 0, 0, 5, 1, 6),
        ("托特纳姆热刺", 2, 1, 1, 0, 5, 1, 4),
        ("纽卡斯尔联", 2, 1, 1, 0, 2, 1, 4),
        ("切尔西", 2, 1, 0, 1, 6, 4, 3),
        ("西汉姆联", 2, 1, 0, 1, 3, 2, 3),
        ("富勒姆", 2, 1, 0, 1, 2, 2, 3),
        ("曼彻斯特联", 2, 1, 0, 1, 2, 2, 3),
        ("阿斯顿维拉", 2, 1, 0, 1, 2, 3, 3),
        ("布伦特福德", 2, 1, 0, 1, 2, 3, 3),
        ("伯恩茅斯", 2, 0, 2, 0, 2, 2, 2),
        ("诺丁汉森林", 2, 0, 2, 0, 2, 2, 2),
        ("莱斯特城", 2, 0, 1, 1, 2, 3, 1),
        ("水晶宫", 2, 0, 0, 2, 1, 4, 0),
        ("伊普斯维奇", 2, 0, 0, 2, 1, 6, 0),
        ("狼队", 2, 0, 0, 2, 2, 8, 0),
        ("南安普顿", 2, 0, 0, 2, 0, 2, 0),
        ("埃弗顿", 2, 0, 0, 2, 0, 7, 0)
    ]
    pl_table = []
    for idx, (name, p, w, d, l, gf, ga, pts) in enumerate(pl_teams, 1):
        pl_table.append({
            "position": idx,
            "team_name": name,
            "played": p, "won": w, "drawn": d, "lost": l,
            "gf": gf, "ga": ga, "gd": gf - ga, "points": pts,
            "is_my_team": False
        })

    # 5. 西甲完整 20 队
    laliga_teams = [
        ("塞尔塔", 2, 2, 0, 0, 5, 2, 6),
        ("巴塞罗那", 2, 2, 0, 0, 4, 2, 6),
        ("马德里竞技", 2, 1, 1, 0, 5, 2, 4),
        ("皇家马德里", 2, 1, 1, 0, 4, 1, 4),
        ("比利亚雷亚尔", 2, 1, 1, 0, 6, 5, 4),
        ("奥萨苏纳", 2, 1, 1, 0, 2, 1, 4),
        ("莱加内斯", 2, 1, 1, 0, 3, 2, 4),
        ("毕尔巴鄂竞技", 2, 1, 1, 0, 2, 2, 4),
        ("巴列卡诺", 2, 1, 1, 0, 2, 1, 4),
        ("皇家社会", 2, 1, 0, 1, 2, 2, 3),
        ("皇家贝蒂斯", 2, 0, 2, 0, 1, 1, 2),
        ("赫塔菲", 2, 0, 2, 0, 1, 1, 2),
        ("拉斯帕尔马斯", 2, 0, 1, 1, 3, 4, 1),
        ("塞维利亚", 2, 0, 1, 1, 3, 4, 1),
        ("马略卡", 2, 0, 1, 1, 1, 2, 1),
        ("阿拉维斯", 2, 0, 1, 1, 1, 2, 1),
        ("赫罗纳", 2, 0, 1, 1, 1, 4, 1),
        ("西班牙人", 2, 0, 0, 2, 0, 2, 0),
        ("巴拉多利德", 2, 0, 1, 1, 1, 3, 1),
        ("巴伦西亚", 2, 0, 0, 2, 2, 5, 0)
    ]
    laliga_table = []
    for idx, (name, p, w, d, l, gf, ga, pts) in enumerate(laliga_teams, 1):
        laliga_table.append({
            "position": idx,
            "team_name": name,
            "played": p, "won": w, "drawn": d, "lost": l,
            "gf": gf, "ga": ga, "gd": gf - ga, "points": pts,
            "is_my_team": False
        })

    # 6. 德甲完整 18 队
    bundesliga_teams = [
        ("拜仁慕尼黑", 2, 2, 0, 0, 5, 2, 6),
        ("RB莱比锡", 2, 2, 0, 0, 4, 2, 6),
        ("海登海姆", 2, 2, 0, 0, 6, 0, 6),
        ("多特蒙德", 2, 1, 1, 0, 2, 0, 4),
        ("柏林联合", 2, 1, 1, 0, 2, 1, 4),
        ("沃尔夫斯堡", 2, 1, 0, 1, 4, 3, 3),
        ("勒沃库森", 2, 1, 0, 1, 5, 5, 3),
        ("弗赖堡", 2, 1, 0, 1, 3, 3, 3),
        ("法兰克福", 2, 1, 0, 1, 3, 3, 3),
        ("门兴格拉德巴赫", 2, 1, 0, 1, 4, 3, 3),
        ("霍芬海姆", 2, 1, 0, 1, 4, 5, 3),
        ("云达不莱梅", 2, 0, 2, 0, 2, 2, 2),
        ("美因茨", 2, 0, 2, 0, 4, 4, 2),
        ("奥格斯堡", 2, 0, 1, 1, 2, 6, 1),
        ("斯图加特", 2, 0, 1, 1, 4, 6, 1),
        ("圣保利", 2, 0, 0, 2, 0, 3, 0),
        ("荷尔斯泰因基尔", 2, 0, 0, 2, 2, 5, 0),
        ("波鸿", 2, 0, 0, 2, 0, 3, 0)
    ]
    bundesliga_table = []
    for idx, (name, p, w, d, l, gf, ga, pts) in enumerate(bundesliga_teams, 1):
        bundesliga_table.append({
            "position": idx,
            "team_name": name,
            "played": p, "won": w, "drawn": d, "lost": l,
            "gf": gf, "ga": ga, "gd": gf - ga, "points": pts,
            "is_my_team": False
        })

    # 7. 法甲完整 18 队
    ligue1_teams = [
        ("巴黎圣日耳曼", 2, 2, 0, 0, 10, 1, 6),
        ("里尔", 2, 2, 0, 0, 4, 0, 6),
        ("摩纳哥", 2, 2, 0, 0, 3, 0, 6),
        ("朗斯", 2, 2, 0, 0, 3, 0, 6),
        ("马赛奥林匹克", 2, 1, 1, 0, 7, 3, 4),
        ("南特", 2, 1, 1, 0, 2, 0, 4),
        ("勒阿弗尔", 2, 1, 0, 1, 3, 4, 3),
        ("雷恩", 2, 1, 0, 1, 4, 3, 3),
        ("斯特拉斯堡", 2, 1, 0, 1, 4, 5, 3),
        ("欧塞尔", 2, 1, 0, 1, 3, 3, 3),
        ("尼斯", 2, 0, 1, 1, 2, 3, 1),
        ("图卢兹", 2, 0, 2, 0, 1, 1, 2),
        ("兰斯", 2, 0, 1, 1, 2, 4, 1),
        ("蒙彼利埃", 2, 0, 1, 1, 1, 7, 1),
        ("布雷斯特", 2, 0, 0, 2, 1, 7, 0),
        ("昂热", 2, 0, 0, 2, 0, 3, 0),
        ("圣埃蒂安", 2, 0, 0, 2, 0, 3, 0),
        ("里昂", 2, 0, 0, 2, 0, 5, 0)
    ]
    ligue1_table = []
    for idx, (name, p, w, d, l, gf, ga, pts) in enumerate(ligue1_teams, 1):
        ligue1_table.append({
            "position": idx,
            "team_name": name,
            "played": p, "won": w, "drawn": d, "lost": l,
            "gf": gf, "ga": ga, "gd": gf - ga, "points": pts,
            "is_my_team": False
        })

    all_leagues = [
        {
            "id": "bel_d2",
            "name": "比利时挑战者职业联赛 (比乙)",
            "short_name": "比乙",
            "flag": "🇧🇪",
            "tag": "当前所处",
            "total_teams": len(bel_d2_table),
            "round": 3,
            "table": bel_d2_table
        },
        {
            "id": "bel_d1",
            "name": "比利时甲级联赛 (比甲)",
            "short_name": "比甲",
            "flag": "🇧🇪",
            "tag": "上级联赛",
            "total_teams": len(bel_d1_table),
            "round": 4,
            "table": bel_d1_table
        },
        {
            "id": "pl",
            "name": "英格兰足球超级联赛 (英超)",
            "short_name": "英超",
            "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
            "tag": "五大联赛",
            "total_teams": len(pl_table),
            "round": 2,
            "table": pl_table
        },
        {
            "id": "laliga",
            "name": "西班牙足球甲级联赛 (西甲)",
            "short_name": "西甲",
            "flag": "🇪🇸",
            "tag": "五大联赛",
            "total_teams": len(laliga_table),
            "round": 2,
            "table": laliga_table
        },
        {
            "id": "serie_a",
            "name": "意大利足球甲级联赛 (意甲)",
            "short_name": "意甲",
            "flag": "🇮🇹",
            "tag": "五大联赛",
            "total_teams": len(serie_a_table),
            "round": 1,
            "table": serie_a_table
        },
        {
            "id": "bundesliga",
            "name": "德国足球甲级联赛 (德甲)",
            "short_name": "德甲",
            "flag": "🇩🇪",
            "tag": "五大联赛",
            "total_teams": len(bundesliga_table),
            "round": 2,
            "table": bundesliga_table
        },
        {
            "id": "ligue1",
            "name": "法国足球甲级联赛 (法甲)",
            "short_name": "法甲",
            "flag": "🇫🇷",
            "tag": "五大联赛",
            "total_teams": len(ligue1_table),
            "round": 2,
            "table": ligue1_table
        }
    ]

    out_file = os.path.join(DATA_DIR, "standings.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"leagues": all_leagues}, f, ensure_ascii=False, indent=2)

    print(f"[✓] 完整各大联赛积分表已生成！包含: {[l['short_name'] + '(' + str(l['total_teams']) + '队)' for l in all_leagues]}")

