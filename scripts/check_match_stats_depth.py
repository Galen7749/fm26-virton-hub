from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    print("Checking player_match_stats...")
    try:
        pms_list = []
        for i, pms in enumerate(save.player_match_stats()):
            attrs = [a for a in dir(pms) if not a.startswith('_')]
            print("player_match_stats attributes:", attrs)
            print("Sample 0:", {k: getattr(pms, k) for k in attrs if hasattr(pms, k)})
            break
    except Exception as e:
        print("player_match_stats error:", e)

    print("\nChecking team_match_stats...")
    try:
        for i, tms in enumerate(save.team_match_stats()):
            attrs = [a for a in dir(tms) if not a.startswith('_')]
            print("team_match_stats attributes:", attrs)
            print("Sample 0:", {k: getattr(tms, k) for k in attrs if hasattr(tms, k)})
            break
    except Exception as e:
        print("team_match_stats error:", e)
