from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    for f in save.fixtures():
        if (f.home_team_id == 245 or f.away_team_id == 245) and f.home_goals is not None:
            print(f"Date: {f.date}, {f.home_club_name} {f.home_goals}-{f.away_goals} {f.away_club_name}")
            # check all attributes of f
            for k in ['round', 'round_index', 'stage_id', 'competition_id']:
                print(f"  {k}: {getattr(f, k, None)}")
            # see if there's any other objects in save: matches?
            break

    print("Checking save properties...")
    props = [a for a in dir(save) if not a.startswith('_')]
    print("Save methods/properties:", props)
