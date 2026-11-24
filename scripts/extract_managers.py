import fmsave, glob, os, json, datetime

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    nations = {n.id: n.name for n in s.nations()} if hasattr(s, 'nations') else {}
    clubs = {c.uid: c.name for c in s.clubs()}
    
    # 1. Staff / Manager
    odra_staff = []
    virton_staff = []
    for st in s.staff():
        cuid = getattr(st, 'club_uid', None)
        if cuid == 129566:
            odra_staff.append({"name": st.name, "job": getattr(st, 'job', None), "role": getattr(st, 'role', None), "contract": str(getattr(st, 'contract', ''))})
        elif cuid == 292:
            virton_staff.append({"name": st.name, "job": getattr(st, 'job', None), "role": getattr(st, 'role', None), "contract": str(getattr(st, 'contract', ''))})
            
    print("Odra staff count:", len(odra_staff))
    for st in odra_staff:
        print("  Odra staff:", st)
    print("Virton staff count:", len(virton_staff))
    for st in virton_staff:
        print("  Virton staff:", st)
