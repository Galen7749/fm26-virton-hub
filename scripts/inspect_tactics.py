import fmsave
from pathlib import Path
from collections import Counter

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1

POS_MAP = {
    1: "GK", 4: "DR", 32: "DR", 16: "DC", 8: "DL", 64: "DM", 128: "DM",
    256: "MC", 512: "MC", 1024: "MC", 2048: "AMR", 4096: "AML", 8192: "AMC", 16384: "ST"
}

with fmsave.open(save_path) as save:
    all_d2_fixtures = [f for f in save.fixtures() if f.competition_id == BEL_D2_CID and f.home_goals is not None]
    virton_fixtures = [f for f in all_d2_fixtures if f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID]
    virton_fixtures.sort(key=lambda x: x.date)
    virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == VIRTON_CLUB_UID or getattr(p, 'team_id', None) == VIRTON_TEAM_ID}
    
    pms_by_date = {f.date: [] for f in virton_fixtures}
    for pms in save.player_match_stats():
        if pms.player_uid in virton_uids and pms.date in pms_by_date:
            pms_by_date[pms.date].append(pms)

    for i, f in enumerate(virton_fixtures, start=1):
        stats = pms_by_date[f.date]
        starters = [p for p in stats if p.entered_at_minute is None and (p.minutes or 0) > 0]
        pos_list = []
        for p in starters:
            raw_pos = getattr(p.position, 'raw', 0) if p.position else 0
            pos_list.append(POS_MAP.get(raw_pos, f"UNK({raw_pos})"))
        pos_counts = Counter(pos_list)
        print(f"Round {i:2d} ({f.date.strftime('%Y-%m-%d')}): {len(starters)} starters: {dict(pos_counts)}")
        if i >= 15:
            details = []
            for p in starters:
                raw_pos = getattr(p.position, 'raw', 0) if p.position else 0
                details.append((POS_MAP.get(raw_pos, f"UNK({raw_pos})"), p.player_name))
            print("   Details:", details)
