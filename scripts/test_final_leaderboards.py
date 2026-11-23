import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    d2_club_uids = set()
    for f in save.fixtures():
        if f.competition_id == BEL_D2_CID:
            if f.home_club_uid: d2_club_uids.add(f.home_club_uid)
            if f.away_club_uid: d2_club_uids.add(f.away_club_uid)

    league_pss = [p for p in save.player_season_stats() if p.club_uid in d2_club_uids and p.kind == 'league']
    
    scorers = [p for p in league_pss if (p.goals or 0) > 0]
    scorers.sort(key=lambda x: (x.goals or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print(f"Total D2 scorers: {len(scorers)}")
    print("Top 10 D2 Scorers:")
    for i, p in enumerate(scorers[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        is_virton = (p.club_uid == VIRTON_CLUB_UID)
        print(f"  #{i:2d} {p.player_name:24s} ({p.club_short_name or p.club_name:12s}): {p.goals:2d}球 ({apps}场, {p.shots}射) {'★' if is_virton else ''}")

    assists = [p for p in league_pss if (p.assists or 0) > 0]
    assists.sort(key=lambda x: (x.assists or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print("\nTop 10 D2 Assists:")
    for i, p in enumerate(assists[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        is_virton = (p.club_uid == VIRTON_CLUB_UID)
        print(f"  #{i:2d} {p.player_name:24s} ({p.club_short_name or p.club_name:12s}): {p.assists:2d}助 ({apps}场, {p.key_passes}关键传球) {'★' if is_virton else ''}")
