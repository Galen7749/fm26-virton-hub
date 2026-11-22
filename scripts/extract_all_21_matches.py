import fmsave
import datetime
import json
from pathlib import Path

SAVE_DIR = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games")
save_files = list(SAVE_DIR.glob("*.fm"))
save_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
latest = save_files[0]
print(f"Opening {latest.name}...")

VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1

POS_MAP = {
    1: "GK",
    4: "DR",
    32: "DR",
    16: "DC",
    8: "DL",
    64: "DM",
    128: "DM",
    256: "MC",
    512: "MC",
    1024: "MC",
    2048: "AMR",
    4096: "AML",
    8192: "AMC",
    16384: "ST"
}

with fmsave.open(str(latest)) as save:
    club_names = {}
    for c in save.clubs():
        for t in c.teams:
            club_names[t.team_id] = c.name

    fixtures = [
        f for f in save.fixtures()
        if f.competition_id == BEL_D2_CID
        and (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID)
        and f.home_goals is not None
    ]
    fixtures.sort(key=lambda x: x.date)
    print(f"Total fixtures: {len(fixtures)}")

    match_dates = {f.date: i+1 for i, f in enumerate(fixtures)}
    virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == VIRTON_CLUB_UID or getattr(p, 'team_id', None) == VIRTON_TEAM_ID}

    pms_by_date = {f.date: [] for f in fixtures}
    for pms in save.player_match_stats():
        if pms.player_uid in virton_uids and pms.date in pms_by_date:
            pms_by_date[pms.date].append(pms)

    for i, f in enumerate(fixtures):
        r_num = i + 1
        d = f.date
        ht = club_names.get(f.home_team_id, "主队")
        at = club_names.get(f.away_team_id, "客队")
        p_list = pms_by_date[d]
        starters = [p for p in p_list if p.entered_at_minute is None and p.minutes is not None and p.minutes > 0]
        subs = [p for p in p_list if p.entered_at_minute is not None and p.minutes is not None and p.minutes > 0]
        
        scorers = []
        for p in starters + subs:
            if getattr(p, 'goals', 0) and p.goals > 0:
                scorers.append(f"{p.player_name}({p.goals}球)")
        
        print(f"R{r_num:02d} [{str(d)[:10]}] {ht} {f.home_goals}-{f.away_goals} {at} | 首发:{len(starters)} 替补:{len(subs)} | 进球:{', '.join(scorers) if scorers else '无'}")
