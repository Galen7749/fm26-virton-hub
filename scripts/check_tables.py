from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    for i, lt in enumerate(save.league_tables()):
        if lt.competition_id == 1:
            for row in lt.rows:
                if row.team_id == 245:
                    print(f"Index {i}, played={row.played}, pts={row.points}, len(matches)={len(row.matches)}, row.stage_id={getattr(row, 'stage_id', None)}, lt.stage_id={getattr(lt, 'stage_id', None)}")
