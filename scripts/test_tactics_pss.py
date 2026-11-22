import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    # 1. Tactics
    try:
        tactics = list(save.tactics())
        print(f"Total tactics: {len(tactics)}")
        if tactics:
            t0 = tactics[0]
            print("Tactic attributes:", [a for a in dir(t0) if not a.startswith('_')])
            for t in tactics[:5]:
                print("  Tactic:", getattr(t, 'name', None), getattr(t, 'formation', None), getattr(t, 'style', None))
    except Exception as e:
        print("Tactics error:", e)

    # 2. Player season stats
    try:
        pss = list(save.player_season_stats())
        print(f"Total player_season_stats: {len(pss)}")
        if pss:
            p0 = pss[0]
            print("PSS attributes:", [a for a in dir(p0) if not a.startswith('_')])
            # Check a few
            for p in pss[:5]:
                print("  PSS:", getattr(p, 'player_name', None), getattr(p, 'goals', None), getattr(p, 'appearances', None))
    except Exception as e:
        print("PSS error:", e)
