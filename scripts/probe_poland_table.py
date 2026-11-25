import fmsave, glob, os

saves = sorted(
    glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"),
    key=lambda x: -os.path.getmtime(x),
)
p = saves[0]
print("Using save:", p)

with fmsave.open(p) as s:
    team_to_club = {}
    odra_team_ids = set()
    for c in s.clubs():
        for t in getattr(c, "teams", []):
            team_to_club[t.team_id] = (c.uid, c.name)
            if c.uid == 129566:
                odra_team_ids.add(t.team_id)

    comps = {c.id: getattr(c, "name", "") for c in s.competitions()}
    print("Odra team_ids:", odra_team_ids)

    for i, lt in enumerate(s.league_tables()):
        row_tids = {r.team_id for r in lt.rows}
        if row_tids & odra_team_ids:
            cname = comps.get(lt.competition_id, str(lt.competition_id))
            print(f"\n=== LT[{i}] comp_id={lt.competition_id} ({cname}) stage_id={getattr(lt, 'stage_id', None)} rows={len(lt.rows)} ===")
            for idx, r in enumerate(lt.rows):
                cid, tname = team_to_club.get(r.team_id, (None, f"team_{r.team_id}"))
                print(
                    f"  {idx+1:2d}. team_id={r.team_id:<10} club_uid={str(cid):<10} {tname:<35} "
                    f"P={r.played} W={r.won} D={r.drawn} L={r.lost} GF={r.goals_for} GA={r.goals_against} Pts={r.points}"
                )
