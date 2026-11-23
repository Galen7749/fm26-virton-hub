import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    all_fixtures = [f for f in save.fixtures() if f.home_goals is not None]
    virton_fixtures = [f for f in all_fixtures if f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID]
    virton_fixtures.sort(key=lambda x: x.date)

    virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == VIRTON_CLUB_UID or getattr(p, 'team_id', None) == VIRTON_TEAM_ID}

    pms_by_date = {f.date: [] for f in virton_fixtures}
    for pms in save.player_match_stats():
        if pms.player_uid in virton_uids and pms.date in pms_by_date:
            pms_by_date[pms.date].append(pms)

    for idx, f in enumerate(virton_fixtures, 1):
        is_home = (f.home_team_id == VIRTON_TEAM_ID)
        sh, sa = f.home_goals, f.away_goals
        opp = f.away_club_name if is_home else f.home_club_name
        res = "W" if (sh > sa if is_home else sa > sh) else ("D" if sh == sa else "L")
        score_str = f"{sh}-{sa}" if is_home else f"{sa}-{sh}"
        stats = pms_by_date.get(f.date, [])
        scorers = [(p.player_name, p.goals) for p in stats if (p.goals or 0) > 0]
        assists = [(p.player_name, p.assists) for p in stats if (p.assists or 0) > 0]
        
        stage_desc = ""
        if f.stage_id == 234:
            stage_desc = f"常规赛第{idx}轮"
        elif f.stage_id == 5398:
            stage_desc = "冲甲附加赛·半决赛首回合(客)"
        elif f.stage_id == 5399:
            stage_desc = "冲甲附加赛·半决赛次回合(主)"
        elif f.stage_id == 5400:
            stage_desc = "冲甲附加赛·决赛首回合(客)"
        elif f.stage_id == 5401:
            stage_desc = "冲甲附加赛·决赛次回合(主·决胜战)"
        else:
            stage_desc = f"杯赛/热身赛 (cid={f.competition_id})"
        
        print(f"[{idx:2d}] {f.date.strftime('%Y-%m-%d')} | {stage_desc:28s} | vs {opp:14s} | {res} {score_str} | 进球: {scorers} | 助攻: {assists}")
