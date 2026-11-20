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

    print("=== 扫描豪门所在的表 ===")
    targets = {
        '西甲': ['皇家马德里', '巴塞罗那', '马德里竞技'],
        '英超': ['曼彻斯特城', '阿森纳', '利物浦', '切尔西'],
        '德甲': ['拜仁慕尼黑', '多特蒙德', '勒沃库森', '莱比锡'],
        '法甲': ['巴黎圣日耳曼', '摩纳哥', '马赛', '里尔']
    }

    found = {}
    for lt in save.league_tables():
        teams = [team_to_club.get(r.team_id, f"t_{r.team_id}") for r in lt.rows]
        teams_str = " ".join(teams)
        for league, kws in targets.items():
            matches = sum(1 for kw in kws if kw in teams_str)
            if matches >= 2:
                print(f"[{league}] cid={lt.competition_id}, 队数={lt.club_count}, 球队数={len(teams)}")
                found[league] = (lt.competition_id, lt.club_count, teams)

