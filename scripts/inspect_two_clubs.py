import fmsave, glob, os, json

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    print("Save date:", s.info.game_date)
    clubs = {c.uid: c for c in s.clubs()}
    
    # Odra Opole
    odra = clubs.get(129566)
    if odra:
        print("\n--- ODRA OPOLE ---")
        print("Name:", odra.name)
        print("Reputation:", getattr(odra, 'reputation', None))
        for attr in dir(odra):
            if not attr.startswith('_') and not callable(getattr(odra, attr)):
                val = getattr(odra, attr)
                if isinstance(val, (int, str, bool, float)):
                    print(f"  {attr}: {val}")
    
    # Find Virton
    virton = None
    for uid, c in clubs.items():
        if "维尔通" in c.name or "Virton" in c.name:
            virton = c
            break
    if virton:
        print("\n--- VIRTON ---")
        print("UID:", virton.uid, "Name:", virton.name)
        for attr in dir(virton):
            if not attr.startswith('_') and not callable(getattr(virton, attr)):
                val = getattr(virton, attr)
                if isinstance(val, (int, str, bool, float)):
                    print(f"  {attr}: {val}")
