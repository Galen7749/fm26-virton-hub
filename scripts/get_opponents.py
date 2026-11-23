import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    club_scorers = {}
    # Let's map player uid to club uid or team
    # Check what fields are in save.player_season_stats()
    stats = list(save.player_season_stats())
    print(f"Total player_season_stats: {len(stats)}")
    if stats:
        p0 = stats[0]
        print("Sample stats fields:", dir(p0))
        # let's see top 20 scorers
        top = sorted([p for p in stats if (getattr(p, 'goals', 0) or 0) > 0], key=lambda x: x.goals, reverse=True)[:30]
        for p in top:
            print(f"{p.player_name}: {p.goals} goals, {getattr(p, 'club_uid', None)}, {getattr(p, 'team_name', None)}")
