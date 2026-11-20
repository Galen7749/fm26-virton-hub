from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    # Build player dict
    players = {}
    for p in save.players():
        if getattr(p, 'club_uid', None) == 292 or getattr(p, 'team_id', None) == 245:
            players[p.player_id] = f"{getattr(p, 'first_name', '')} {getattr(p, 'last_name', '')}".strip()

    print(f"Indexed {len(players)} Virton players.")

    # Check player_season_stats
    print("\n--- Virton Player Season Stats ---")
    try:
        for pss in save.player_season_stats():
            pid = getattr(pss, 'player_id', None)
            if pid in players or getattr(pss, 'team_id', None) == 245:
                pname = players.get(pid, f"Player_{pid}")
                apps = getattr(pss, 'appearances', getattr(pss, 'starts', 0))
                sub_apps = getattr(pss, 'sub_appearances', 0)
                goals = getattr(pss, 'goals', 0)
                assists = getattr(pss, 'assists', 0)
                rating = getattr(pss, 'average_rating', getattr(pss, 'rating', 0))
                print(f"  {pname}: Apps={apps}(+{sub_apps}), G={goals}, A={assists}, Rating={rating}")
    except Exception as e:
        print(f"player_season_stats error: {e}")
