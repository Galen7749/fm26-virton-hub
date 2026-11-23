import fmsave

# Let's inspect everything in fmsave module
print("fmsave module contents:", dir(fmsave))

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
with fmsave.open(save_path) as save:
    print("save attributes:", [a for a in dir(save) if not a.startswith('_')])
    # Let's check team_match_stats
    print("Checking team_match_stats...")
    tms = list(save.team_match_stats())
    print(f"Total team_match_stats: {len(tms)}")
    if tms:
        print("TMS attributes:", [a for a in dir(tms[0]) if not a.startswith('_')])
