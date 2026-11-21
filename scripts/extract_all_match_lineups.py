from pathlib import Path
import datetime
import json
import fmsave

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

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    virton_dates = [
        datetime.date(2025, 8, 10),
        datetime.date(2025, 8, 13),
        datetime.date(2025, 8, 17),
        datetime.date(2025, 8, 24),
        datetime.date(2025, 8, 31),
        datetime.date(2025, 9, 6),
        datetime.date(2025, 9, 14),
        datetime.date(2025, 9, 24),
        datetime.date(2025, 10, 5),
    ]

    virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == 292 or getattr(p, 'team_id', None) == 245}

    match_stats = {d: [] for d in virton_dates}
    for pms in save.player_match_stats():
        if pms.player_uid in virton_uids and pms.date in match_stats:
            match_stats[pms.date].append(pms)

    for idx, d in enumerate(virton_dates, 1):
        p_list = match_stats[d]
        starters = [p for p in p_list if p.entered_at_minute is None and p.minutes is not None and p.minutes > 0]
        subs = [p for p in p_list if p.entered_at_minute is not None and p.minutes is not None and p.minutes > 0]
        print(f"\n================ MATCH {idx} ({d}) Starters: {len(starters)}, Subs: {len(subs)} ================")
        starters.sort(key=lambda p: getattr(p.position, 'raw', 0) if p.position else 0)
        for p in starters:
            raw_pos = getattr(p.position, 'raw', 0) if p.position else 0
            pos_label = POS_MAP.get(raw_pos, f"RAW_{raw_pos}")
            g_str = f" G:{p.goals}" if p.goals else ""
            a_str = f" A:{p.assists}" if p.assists else ""
            print(f"  [{pos_label:<4}] {p.player_name:<24} | Min:{p.minutes:2d} | Rating:{p.rating}{g_str}{a_str}")
        if subs:
            print("  --- 替补登场 ---")
            for p in subs:
                raw_pos = getattr(p.position, 'raw', 0) if p.position else 0
                pos_label = POS_MAP.get(raw_pos, f"RAW_{raw_pos}")
                g_str = f" G:{p.goals}" if p.goals else ""
                a_str = f" A:{p.assists}" if p.assists else ""
                print(f"  [{pos_label:<4}] {p.player_name:<24} | 替补换上:{p.entered_at_minute}' | Rating:{p.rating}{g_str}{a_str}")
