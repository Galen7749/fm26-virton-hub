import fmsave
import glob
import os
import datetime
import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")
save_files = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))
p = save_files[0]
print("Using save:", p)

with fmsave.open(p) as s:
    club_uid = 129566
    teams_dict = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    clubs_dict = {c.uid: c.name for c in s.clubs()}
    
    # Competition 188 fixtures in 2026 between 2026-07-15 and 2026-08-05
    d1_fixs = [
        f for f in s.fixtures()
        if f.competition_id == 188 and f.home_goals is not None and f.date.year == 2026 and f.date.month in [7, 8]
    ]
    d1_fixs.sort(key=lambda x: x.date)
    print(f"Total comp 188 fixtures in early 2026/27: {len(d1_fixs)}")

    # Calculate table from these fixtures
    # Get all unique teams in comp 188
    team_stats = {}
    for f in d1_fixs:
        h_name = teams_dict.get(f.home_team_id, clubs_dict.get(f.home_club_uid, f"Team_{f.home_team_id}"))
        a_name = teams_dict.get(f.away_team_id, clubs_dict.get(f.away_club_uid, f"Team_{f.away_team_id}"))
        
        # Clean names
        h_clean = h_name.replace("足球俱乐部", "").strip()
        a_clean = a_name.replace("足球俱乐部", "").strip()
        
        for name in [h_clean, a_clean]:
            if name not in team_stats:
                team_stats[name] = {
                    "team_name": name,
                    "played": 0,
                    "won": 0,
                    "drawn": 0,
                    "lost": 0,
                    "gf": 0,
                    "ga": 0,
                    "gd": 0,
                    "points": 0
                }
        
        hg = f.home_goals
        ag = f.away_goals
        
        team_stats[h_clean]["played"] += 1
        team_stats[h_clean]["gf"] += hg
        team_stats[h_clean]["ga"] += ag
        
        team_stats[a_clean]["played"] += 1
        team_stats[a_clean]["gf"] += ag
        team_stats[a_clean]["ga"] += hg
        
        if hg > ag:
            team_stats[h_clean]["won"] += 1
            team_stats[h_clean]["points"] += 3
            team_stats[a_clean]["lost"] += 1
        elif hg < ag:
            team_stats[a_clean]["won"] += 1
            team_stats[a_clean]["points"] += 3
            team_stats[h_clean]["lost"] += 1
        else:
            team_stats[h_clean]["drawn"] += 1
            team_stats[h_clean]["points"] += 1
            team_stats[a_clean]["drawn"] += 1
            team_stats[a_clean]["points"] += 1

    for st in team_stats.values():
        st["gd"] = st["gf"] - st["ga"]

    # Sort table by points, GD, GF
    sorted_table = sorted(team_stats.values(), key=lambda x: (x["points"], x["gd"], x["gf"]), reverse=True)
    for idx, t in enumerate(sorted_table, start=1):
        t["position"] = idx
        if idx <= 2:
            t["note"] = "直接升级区"
            if "奥波莱" in t["team_name"]:
                t["note"] += " · 留洋主队 🇨🇳"
        elif 3 <= idx <= 6:
            t["note"] = "升级附加赛"
            if "奥波莱" in t["team_name"]:
                t["note"] += " · 留洋主队 🇨🇳"
        elif idx >= 16:
            t["note"] = "降级区"
        else:
            t["note"] = ""
        print(f"{t['position']}. {t['team_name']} | P:{t['played']} W:{t['won']} D:{t['drawn']} L:{t['lost']} GF:{t['gf']} GA:{t['ga']} GD:{t['gd']} PTS:{t['points']} ({t['note']})")

    # Output table json
    with open(r"I:\fm26-virton-hub\scripts\pol_d1_3rounds_table.json", "w", encoding="utf-8") as out:
        json.dump(sorted_table, out, ensure_ascii=False, indent=2)
    print("Saved table to pol_d1_3rounds_table.json")
