import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 245
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    all_d2_fixtures = [f for f in save.fixtures() if f.home_goals is not None]
    virton_fixtures = [f for f in all_d2_fixtures if f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID]
    virton_fixtures.sort(key=lambda x: x.date)
    print(f"Total Virton finished fixtures across all comps: {len(virton_fixtures)}")

    for idx, f in enumerate(virton_fixtures[20:], 21):
        is_home = (f.home_team_id == VIRTON_TEAM_ID)
        sh, sa = f.home_goals, f.away_goals
        opp = f.away_club_name if is_home else f.home_club_name
        res = "W" if (sh > sa if is_home else sa > sh) else ("D" if sh == sa else "L")
        score_str = f"{sh}-{sa}" if is_home else f"{sa}-{sh}"
        print(f"Match #{idx:2d} | {f.date.strftime('%Y-%m-%d')} | {'主' if is_home else '客'} vs {opp:16s} | {res} {score_str} | comp={f.competition_name} (cid={f.competition_id}, stage={f.stage_id})")

    # Let's inspect the latest match's players and events
    latest_f = virton_fixtures[-1]
    print(f"\n--- Latest Match (# {len(virton_fixtures)}) Details ---")
    print(f"Date: {latest_f.date}, Home: {latest_f.home_club_name} {latest_f.home_goals} - {latest_f.away_goals} {latest_f.away_club_name}")
    
    # Check player match stats for latest match
    pms_list = [p for p in save.player_match_stats() if p.date == latest_f.date and (p.minutes or 0) > 0]
    virton_pms = [p for p in pms_list if getattr(p, 'club_uid', None) == 292 or 'Virton' in str(getattr(p, 'club_name', ''))]
    if not virton_pms:
        # filter by player_uid
        virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == 292}
        virton_pms = [p for p in pms_list if p.player_uid in virton_uids]
    
    print(f"Virton players with stats: {len(virton_pms)}")
    for p in virton_pms:
        if (p.goals or 0) > 0 or (p.assists or 0) > 0 or (p.rating or 0) >= 7.5:
            print(f"  {p.player_name}: goals={p.goals}, assists={p.assists}, rating={p.rating}, min={p.minutes}, entered={p.entered_at_minute}")
