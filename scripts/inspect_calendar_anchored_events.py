import fmsave
import glob
import os
import datetime
from pathlib import Path

save_files = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))
p = save_files[0]
print("Using save:", p)

with fmsave.open(p) as s:
    print("Game Date:", s.info.game_date)
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    comps = {getattr(c, 'id', getattr(c, 'competition_id', None)): c.name for c in s.competitions()}
    
    # Check fixtures between 2026-07-25 and 2026-08-01
    d_start = datetime.date(2026, 7, 25)
    d_end = datetime.date(2026, 8, 1)
    
    # Look for Polish league (188), Champions League (or UCL qualifiers), Belgian leagues, or friendly tours of top clubs
    big_clubs = ["皇家马德里", "巴塞罗那", "曼彻斯特城", "阿森纳", "利物浦", "拜仁慕尼黑", "巴黎圣日耳曼", "切尔西", "曼彻斯特联", "AC米兰", "国际米兰", "维尔通精英", "奥波莱奥德拉"]
    
    print("\n--- 1. Polish League (Comp 188) Matches This Week ---")
    for f in s.fixtures():
        if f.competition_id == 188 and d_start <= f.date <= d_end and f.home_goals is not None:
            h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, f.home_team_id))
            a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, f.away_team_id))
            print(f"  {f.date} | {h} {f.home_goals} - {f.away_goals} {a}")

    print("\n--- 2. European / Champions League / Friendly Matches of Giants This Week ---")
    for f in s.fixtures():
        if d_start <= f.date <= d_end and f.home_goals is not None:
            h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, ""))
            a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, ""))
            if any(bc in h or bc in a for bc in big_clubs):
                cname = comps.get(f.competition_id, f"Comp_{f.competition_id}")
                print(f"  {f.date} | {cname} | {h} {f.home_goals} - {f.away_goals} {a}")

    print("\n--- 3. Belgian League / Virton / Belgian Pro League This Week ---")
    for f in s.fixtures():
        if d_start <= f.date <= d_end and f.home_goals is not None:
            h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, ""))
            a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, ""))
            if "维尔通" in h or "维尔通" in a or "布鲁日" in h or "安德莱赫特" in h:
                cname = comps.get(f.competition_id, f"Comp_{f.competition_id}")
                print(f"  {f.date} | {cname} | {h} {f.home_goals} - {f.away_goals} {a}")
