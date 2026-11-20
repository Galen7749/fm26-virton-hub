from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    for f in save.fixtures():
        if (f.home_team_id == 245 or f.away_team_id == 245) and f.home_goals is not None:
            print("Fixture dir:", [a for a in dir(f) if not a.startswith('_')])
            match = getattr(f, 'match', None)
            if match:
                print("Match dir:", [a for a in dir(match) if not a.startswith('_')])
            break
