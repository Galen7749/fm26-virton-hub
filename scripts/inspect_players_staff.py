import fmsave, glob, os

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    print("Classes in s:", [a for a in dir(s) if not a.startswith('_')])
    
    # Check s.staff, s.players, s.human_managers, etc.
    if hasattr(s, 'staff'):
        staff_list = list(s.staff())
        print(f"Total staff: {len(staff_list)}")
        for st in staff_list[:5]:
            print("Staff example:", st.name, getattr(st, 'club_uid', None), getattr(st, 'job', None))
            break
            
    if hasattr(s, 'players'):
        players = list(s.players())
        print(f"Total players: {len(players)}")
        
        # Look for players belonging to Odra (129566) and Virton (292)
        odra_players = [pl for pl in players if getattr(pl, 'club_uid', None) == 129566 or getattr(pl, 'club_id', None) == 129566]
        virton_players = [pl for pl in players if getattr(pl, 'club_uid', None) == 292 or getattr(pl, 'club_id', None) == 292]
        print(f"Odra players found: {len(odra_players)}")
        print(f"Virton players found: {len(virton_players)}")
        if odra_players:
            print("Odra player sample:", odra_players[0].name, [a for a in dir(odra_players[0]) if not a.startswith('_')])
