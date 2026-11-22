import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    # Find all clubs in Bel D2
    d2_club_uids = set()
    for f in save.fixtures():
        if f.competition_id == BEL_D2_CID:
            if f.home_club_uid:
                d2_club_uids.add(f.home_club_uid)
            if f.away_club_uid:
                d2_club_uids.add(f.away_club_uid)
    print(f"D2 club UIDs: {d2_club_uids}")

    # Inspect player_season_stats for these clubs
    d2_pss = []
    for p in save.player_season_stats():
        if p.club_uid in d2_club_uids:
            d2_pss.append(p)
    print(f"Total D2 PSS records: {len(d2_pss)}")

    # Check top scorers
    d2_scorers = [p for p in d2_pss if (p.goals or 0) > 0]
    d2_scorers.sort(key=lambda x: (x.goals or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print("\nTop 15 Scorers in D2:")
    for p in d2_scorers[:15]:
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  {p.player_name} ({p.club_short_name or p.club_name}): {p.goals} goals, {apps} apps, {p.shots} shots, {p.penalties_scored} pen")

    # Check top assists
    d2_assisters = [p for p in d2_pss if (p.assists or 0) > 0]
    d2_assisters.sort(key=lambda x: x.assists or 0, reverse=True)
    print("\nTop 10 Assists in D2:")
    for p in d2_assisters[:10]:
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  {p.player_name} ({p.club_short_name or p.club_name}): {p.assists} assists, {apps} apps")
