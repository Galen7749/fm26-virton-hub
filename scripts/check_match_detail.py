import fmsave, glob, os, datetime
p = sorted(glob.glob(r'C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm'), key=lambda x: -os.path.getmtime(x))[0]
with fmsave.open(p) as s:
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    d_start = datetime.date(2026, 7, 30)
    d_end = datetime.date(2026, 8, 1)
    for f in s.fixtures():
        if d_start <= f.date <= d_end and f.home_goals is not None:
            h = teams.get(f.home_team_id, clubs.get(f.home_club_uid, ''))
            a = teams.get(f.away_team_id, clubs.get(f.away_club_uid, ''))
            if any(k in h or k in a for k in ['华沙莱吉亚', '波兹南莱赫', '曼彻斯特城', '维尔通', '巴塞罗那', '阿森纳']):
                print(f"{f.date} | {h} {f.home_goals} - {f.away_goals} {a}")
                print("  attributes:", [a for a in dir(f) if not a.startswith('_')])
                break
