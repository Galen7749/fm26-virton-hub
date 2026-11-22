import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    all_d2_fixtures = [f for f in save.fixtures() if f.competition_id == BEL_D2_CID and f.home_goals is not None]
    f = all_d2_fixtures[0]
    print("Fixture attributes:", [attr for attr in dir(f) if not attr.startswith('_')])
    for attr in ['goals', 'home_goals', 'away_goals', 'scorers', 'events', 'stats', 'match_id', 'uid']:
        if hasattr(f, attr):
            print(f"  {attr}:", getattr(f, attr))
    
    # Also check save methods or attributes related to competitions or player stats
    print("Save attributes:", [attr for attr in dir(save) if not attr.startswith('_')])
