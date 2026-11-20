from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    for lt in save.league_tables():
        if lt.competition_id == 1:
            print(f"Table index: {lt.competition_id}, rows count: {len(lt.rows)}")
            rows = sorted(lt.rows, key=lambda r: (r.points, r.goals_for - r.goals_against, r.goals_for), reverse=True)
            for pos, r in enumerate(rows, 1):
                name = team_to_club.get(r.team_id, r.team_id)
                is_virton = "★ VIRTON ★" if r.team_id == 245 else ""
                print(f"{pos:2d}. {name:<30} P:{r.played} W:{r.won} D:{r.drawn} L:{r.lost} GF:{r.goals_for} GA:{r.goals_against} GD:{r.goals_for - r.goals_against:+3d} PTS:{r.points} {is_virton}")
