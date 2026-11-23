import fmsave
import datetime

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    target_date = datetime.date(2026, 6, 17)
    pms_list = [p for p in save.player_match_stats() if p.date == target_date]
    print(f"Total PMS: {len(pms_list)}")
    for i, p in enumerate(pms_list):
        print(f"[{i:2d}] name={p.player_name:24s} min={p.minutes} sub={p.entered_at_minute} g={p.goals} a={p.assists} opp={p.opponent_club_name}")
