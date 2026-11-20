from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    for p in save.players():
        print("Player dir:", [a for a in dir(p) if not a.startswith('_')])
        print("Sample player:", {k: getattr(p, k) for k in ['id', 'uid', 'first_name', 'last_name', 'club_uid', 'team_id'] if hasattr(p, k)})
        break

    for pss in save.player_season_stats():
        print("PlayerSeasonStats dir:", [a for a in dir(pss) if not a.startswith('_')])
        break
