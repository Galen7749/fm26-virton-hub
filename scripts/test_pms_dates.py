import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    dates = set()
    for p in save.player_match_stats():
        if p.date and p.date.year == 2026 and p.date.month == 6:
            dates.add(p.date)
    print("June 2026 PMS dates:", dates)

    # For the June 17 date:
    for d in sorted(dates):
        pms_d = [p for p in save.player_match_stats() if p.date == d]
        print(f"\nDate {d}: {len(pms_d)} PMS records")
        for p in pms_d:
            if (p.goals or 0) > 0:
                print(f"  Scorer: {p.player_name} (goals={p.goals}, club={getattr(p, 'club_name', None)}, opp={getattr(p, 'opponent_club_name', None)})")
