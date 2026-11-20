from pathlib import Path
import json
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    played_fixtures = []
    for f in save.fixtures():
        if (f.home_team_id == 245 or f.away_team_id == 245) and f.home_goals is not None:
            is_home = (f.home_team_id == 245)
            opp_id = f.away_team_id if is_home else f.home_team_id
            opp_name = team_to_club.get(opp_id, f"Team_{opp_id}")
            sh = f.home_goals
            sa = f.away_goals
            vg = sh if is_home else sa
            og = sa if is_home else sh
            res = "胜" if vg > og else "平" if vg == og else "负"
            
            played_fixtures.append({
                "date": str(f.date),
                "is_home": is_home,
                "opp_id": opp_id,
                "opp_name": opp_name,
                "sh": sh,
                "sa": sa,
                "virton_goals": vg,
                "opp_goals": og,
                "result": res,
                "competition_id": f.competition_id,
                "stadium": getattr(f, 'stadium_name', '')
            })

    played_fixtures.sort(key=lambda x: x['date'])
    for idx, pf in enumerate(played_fixtures, 1):
        ha = "主场" if pf['is_home'] else "客场"
        comp = "比乙联赛" if pf['competition_id'] == 1 else "比利时杯 (Croky Cup)"
        print(f"{idx}. [{pf['date']}] {comp} ({ha}) vs {pf['opp_name']}: {pf['sh']}-{pf['sa']} -> {pf['result']} (进{pf['virton_goals']} 失{pf['opp_goals']})")
