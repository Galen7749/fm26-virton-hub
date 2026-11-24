import fmsave
import glob
import os
import datetime

save_files = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))
p = save_files[0]
print("Using save:", p)

with fmsave.open(p) as s:
    club_uid = 129566
    player_names = {p.uid: f"{p.first_name} {p.last_name}".strip() for p in s.players()}
    odra_players = {p.uid for p in s.players() if getattr(p, 'club_uid', None) == club_uid}
    target_dates = [datetime.date(2026, 7, 19), datetime.date(2026, 7, 26), datetime.date(2026, 8, 1)]
    
    print("--- Odra Goals / Assists in 3 rounds ---")
    for pms in s.player_match_stats():
        if pms.date in target_dates and pms.player_uid in odra_players:
            goals = getattr(pms, 'goals', 0) or 0
            assists = getattr(pms, 'assists', 0) or 0
            if goals > 0 or assists > 0:
                pname = player_names.get(pms.player_uid, str(pms.player_uid))
                print(f"{pms.date} | {pname} | Goals: {goals} | Assists: {assists} | Rating: {getattr(pms, 'rating', 0)}")

    print("\n--- All Opponents in 3 rounds ---")
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    for f in s.fixtures():
        if f.competition_id == 188 and f.date in target_dates and f.home_goals is not None:
            h_name = teams.get(f.home_team_id, clubs.get(f.home_club_uid, f.home_club_uid))
            a_name = teams.get(f.away_team_id, clubs.get(f.away_club_uid, f.away_club_uid))
            print(f"{f.date} | {h_name} {f.home_goals} - {f.away_goals} {a_name}")
