import fmsave, glob, os, json

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    # Get player stats
    stats_map = {}
    if hasattr(s, 'player_season_stats'):
        for st in s.player_season_stats():
            stats_map[st.player_uid] = st

    print("Total stats entries:", len(stats_map))
    if stats_map:
        sample_k = next(iter(stats_map))
        print("Sample stat attributes:", [a for a in dir(stats_map[sample_k]) if not a.startswith('_')])
