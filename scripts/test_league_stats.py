import fmsave
from collections import defaultdict

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    all_d2_fixtures = [f for f in save.fixtures() if f.competition_id == BEL_D2_CID and f.home_goals is not None]
    fixture_dates = {f.date for f in all_d2_fixtures}
    print(f"Total D2 finished fixtures: {len(all_d2_fixtures)}, unique dates: {len(fixture_dates)}")

    # Check player_match_stats for all D2 fixtures
    # Note: we need to map player_uid to player name and team
    # Let's count how many player_match_stats exist in total and how many goals
    goals_by_player = defaultdict(int)
    assists_by_player = defaultdict(int)
    matches_by_player = defaultdict(int)
    player_names = {}

    count = 0
    for pms in save.player_match_stats():
        if pms.date in fixture_dates and (pms.minutes or 0) > 0:
            count += 1
            p_name = pms.player_name
            player_names[pms.player_uid] = p_name
            matches_by_player[p_name] += 1
            if getattr(pms, 'goals', 0):
                goals_by_player[p_name] += pms.goals
            if getattr(pms, 'assists', 0):
                assists_by_player[p_name] += pms.assists

    print(f"Total D2 player performances collected: {count}")
    top_scorers = sorted(goals_by_player.items(), key=lambda x: x[1], reverse=True)[:15]
    print("Top Scorers in D2:")
    for name, g in top_scorers:
        print(f"  {name}: {g} goals ({matches_by_player[name]} matches)")
