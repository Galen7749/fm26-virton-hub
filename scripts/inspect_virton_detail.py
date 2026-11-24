import fmsave, glob, os, json

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    # Check Virton manager in s.job_vacancies or staff
    print("--- Managed Clubs ---")
    if hasattr(s, 'managed_clubs'):
        for m in s.managed_clubs():
            print("Managed club:", m)
            
    print("\n--- Virton Staff ---")
    for st in s.staff():
        if getattr(st, 'club_uid', None) == 292:
            print(f"Virton staff: {st.name} (age {st.age})")
            
    # Check Virton players
    virton_players = []
    for pl in s.players():
        if getattr(pl, 'club_uid', None) == 292:
            virton_players.append({
                "name": pl.name,
                "age": pl.age,
                "positions": pl.positions,
                "contract_end": str(getattr(pl, 'contract_end', getattr(getattr(pl, 'contract', None), 'contract_end', ''))),
                "transfer_value": getattr(pl, 'transfer_value', 0)
            })
    print(f"\nVirton players: {len(virton_players)}")
    for pl in virton_players[:10]:
        print(" ", pl)
