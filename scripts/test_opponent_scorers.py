import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    # 2026-06-17 match
    from datetime import datetime
    match_date = datetime(2026, 6, 17)
    
    pms_list = [p for p in save.player_match_stats() if p.date == match_date]
    print(f"Total PMS on 2026-06-17: {len(pms_list)}")
    
    # Virton players vs Opponent players
    virton_p = []
    opp_p = []
    for p in pms_list:
        if '利尔斯' in str(p.opponent_club_name or ''):
            virton_p.append(p)
        elif '维尔通' in str(p.opponent_club_name or ''):
            opp_p.append(p)

    print(f"Virton players: {len(virton_p)}")
    print("Virton scorers:", [(p.player_name, p.goals, p.assists, p.minutes, p.entered_at_minute) for p in virton_p if (p.goals or 0) > 0])
    
    print(f"Opponent (Lierse) players: {len(opp_p)}")
    print("Opponent scorers:", [(p.player_name, p.goals, p.assists, p.minutes, p.entered_at_minute) for p in opp_p if (p.goals or 0) > 0])
    print("Opponent lineup:", [(p.player_name, p.goals, p.rating) for p in opp_p if (p.minutes or 0) > 0])
