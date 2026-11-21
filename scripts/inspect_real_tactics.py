from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    print("--- 1. Managed Clubs ---")
    try:
        for mc in save.managed_clubs():
            print("Managed club:", mc)
    except Exception as e:
        print("managed_clubs error:", e)

    print("\n--- 2. Tactics ---")
    try:
        for i, t in enumerate(save.tactics()):
            print(f"Tactic {i}:")
            attrs = [a for a in dir(t) if not a.startswith('_')]
            print("  attributes:", attrs)
            for a in ['formation', 'mentality', 'style', 'team_id', 'club_uid', 'name']:
                if hasattr(t, a):
                    print(f"  {a}: {getattr(t, a)}")
    except Exception as e:
        print("tactics error:", e)

    print("\n--- 3. Selections ---")
    try:
        for i, s in enumerate(save.selections()):
            print(f"Selection {i}:", [a for a in dir(s) if not a.startswith('_')])
            for a in ['team_id', 'club_uid', 'players', 'selected_players', 'lineup']:
                if hasattr(s, a):
                    print(f"  {a}: {getattr(s, a)}")
            break
    except Exception as e:
        print("selections error:", e)
