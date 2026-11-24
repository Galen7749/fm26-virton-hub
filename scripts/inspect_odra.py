import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
with fmsave.open(save_path) as save:
    print("Managed clubs:", list(save.managed_clubs()))
    for s in save.staff():
        if "耶稣" in s.first_name or "徐" in s.last_name or "Xu" in (s.first_name or "") or "Xu" in (s.last_name or ""):
            print("Found manager staff:", s.first_name, s.last_name, "club_id:", getattr(s, "club_id", None))
    # Also search clubs for Opole
    for c in save.clubs():
        if "Opole" in c.name or "Odra" in c.name:
            print(f"Club found: {c.name}, uid: {c.uid}")
            for t in c.teams:
                print(f"  Team: {t.name}, team_id: {t.team_id}")
