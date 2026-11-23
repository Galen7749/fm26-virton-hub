import fmsave
import datetime

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with fmsave.open(save_path) as save:
    for target_date in [datetime.date(2026, 6, 12), datetime.date(2026, 6, 17)]:
        print(f"\n================ DATE: {target_date} ================")
        pms_list = [p for p in save.player_match_stats() if p.date == target_date]
        print(f"Total PMS: {len(pms_list)}")
        for p in pms_list:
            print(f"  Player: {getattr(p, 'player_name', 'None'):24s} | UID: {getattr(p, 'player_uid', 'None')} | Min: {str(getattr(p, 'minutes', None)):4s} | SubIn: {str(getattr(p, 'entered_at_minute', None)):4s} | G: {getattr(p, 'goals', None)} | A: {getattr(p, 'assists', None)} | Rat: {getattr(p, 'rating', None)} | Opp: {getattr(p, 'opponent_club_name', None)}")
