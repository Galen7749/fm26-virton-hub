import fmsave, glob, os

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    for st in s.staff():
        cuid = getattr(st, 'club_uid', None)
        if cuid in (129566, 292):
            print(f"Club {cuid} Staff: {st.name} | attributes: {[a for a in dir(st) if not a.startswith('_')]}")
            for a in ['job', 'role', 'contract', 'job_type', 'is_manager']:
                if hasattr(st, a):
                    print(f"  {a}: {getattr(st, a)}")
