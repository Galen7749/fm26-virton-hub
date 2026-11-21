from pathlib import Path
import datetime
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    virton_dates = {
        datetime.date(2025, 8, 10),
        datetime.date(2025, 8, 13),
        datetime.date(2025, 8, 17),
        datetime.date(2025, 8, 24),
        datetime.date(2025, 8, 31),
        datetime.date(2025, 9, 6),
        datetime.date(2025, 9, 14),
        datetime.date(2025, 9, 24),
        datetime.date(2025, 10, 5),
    }

    # First collect Virton player uids
    virton_uids = set()
    for p in save.players():
        if getattr(p, 'club_uid', None) == 292 or getattr(p, 'team_id', None) == 245:
            virton_uids.add(p.uid)

    print(f"Found {len(virton_uids)} Virton player uids.")

    match_players_by_date = {}
    for pms in save.player_match_stats():
        if pms.player_uid in virton_uids and pms.date in virton_dates:
            d = pms.date
            if d not in match_players_by_date:
                match_players_by_date[d] = []
            match_players_by_date[d].append(pms)

    print(f"Dates with player match stats: {len(match_players_by_date)}")
    for d in sorted(match_players_by_date.keys()):
        p_list = match_players_by_date[d]
        print(f"\nDate: {d} (Players count: {len(p_list)}) vs {p_list[0].opponent_club_name}")
        # Sort starters (entered_at_minute is None or 0) vs subs
        for p in p_list:
            pos = getattr(p, 'position', None)
            mins = getattr(p, 'minutes', None)
            entered = getattr(p, 'entered_at_minute', None)
            rating = getattr(p, 'rating', None)
            g = getattr(p, 'goals', 0)
            a = getattr(p, 'assists', 0)
            print(f"  {p.player_name:<22}: Pos={pos}, Min={mins}, SubIn={entered}, Rating={rating}, G={g}, A={a}")
