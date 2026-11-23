import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    # Check Belgian league/playoff opponent clubs
    target_clubs = [
        "皇家利尔斯体育俱乐部",
        "登德尔",
        "布鲁日预备队",
        "RFC列日",
        "贝弗伦",
        "洛默尔",
        "奥斯坦德"
    ]
    
    club_players = {}
    for p in save.player_season_stats():
        if p.club_name in target_clubs and (p.goals or 0) > 0:
            club_players.setdefault(p.club_name, []).append((p.player_name, p.goals, p.kind))
            
    for club, p_list in club_players.items():
        print(f"\n=== {club} ===")
        # sort by goals desc
        sorted_p = sorted(p_list, key=lambda x: x[1], reverse=True)[:10]
        for name, g, kind in sorted_p:
            print(f"  {name}: {g} goals ({kind})")
