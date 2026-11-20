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

    print("=== 扫描所有积分榜包含的知名俱乐部 ===")
    
    # 查找重点俱乐部
    tracked_leagues = {}
    for lt in save.league_tables():
        teams_in_table = [team_to_club.get(r.team_id, f"t_{r.team_id}") for r in lt.rows]
        teams_str = " ".join(teams_in_table)
        
        # 探测比甲 (Jupiler Pro League)
        if any(club in teams_str for club in ['布鲁日足球俱乐部', '皇家安德莱赫特', '标准列日', '皇家圣吉罗斯']):
            tracked_leagues['比甲 (Jupiler Pro League)'] = (lt.competition_id, teams_in_table[:6])
            
        # 探测英超 (Premier League)
        if any(club in teams_str for club in ['曼彻斯特城', '阿森纳', '利物浦足球俱乐部', '切尔西']):
            if lt.club_count == 20:
                tracked_leagues['英超 (Premier League)'] = (lt.competition_id, teams_in_table[:6])

        # 探测西甲 (La Liga)
        if any(club in teams_str for club in ['皇家马德里', '巴塞罗那足球俱乐部', '马德里竞技']):
            if lt.club_count == 20:
                tracked_leagues['西甲 (La Liga)'] = (lt.competition_id, teams_in_table[:6])

        # 探测德甲 (Bundesliga)
        if any(club in teams_str for club in ['拜仁慕尼黑', '多特蒙德', '勒沃库森']):
            if lt.club_count == 18:
                tracked_leagues['德甲 (Bundesliga)'] = (lt.competition_id, teams_in_table[:6])

        # 探测意甲 (Serie A)
        if any(club in teams_str for club in ['国际米兰', '尤文图斯', 'AC米兰', '那不勒斯']):
            if lt.club_count == 20:
                tracked_leagues['意甲 (Serie A)'] = (lt.competition_id, teams_in_table[:6])

        # 探测法甲 (Ligue 1)
        if any(club in teams_str for club in ['巴黎圣日耳曼', '摩纳哥足球俱乐部', '马赛奥林匹克', '里尔']):
            if lt.club_count in [18, 20]:
                tracked_leagues['法甲 (Ligue 1)'] = (lt.competition_id, teams_in_table[:6])

    for k, v in tracked_leagues.items():
        print(f"\n{k}: comp_id={v[0]}")
        print(f"  前几名/代表队: {v[1]}")

