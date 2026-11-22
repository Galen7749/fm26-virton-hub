import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    d2_club_uids = set()
    for f in save.fixtures():
        if f.competition_id == BEL_D2_CID:
            if f.home_club_uid: d2_club_uids.add(f.home_club_uid)
            if f.away_club_uid: d2_club_uids.add(f.away_club_uid)

    league_pss = [p for p in save.player_season_stats() if p.club_uid in d2_club_uids and p.kind == 'league']
    print(f"Total D2 league PSS records: {len(league_pss)}")

    scorers = [p for p in league_pss if (p.goals or 0) > 0]
    scorers.sort(key=lambda x: (x.goals or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print("\nTop 10 Scorers (kind='league'):")
    for i, p in enumerate(scorers[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  #{i} {p.player_name} ({p.club_short_name or p.club_name}): {p.goals}球 ({apps}场, {p.shots}射, {p.penalties_scored}点)")

    assists = [p for p in league_pss if (p.assists or 0) > 0]
    assists.sort(key=lambda x: (x.assists or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print("\nTop 10 Assists (kind='league'):")
    for i, p in enumerate(assists[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  #{i} {p.player_name} ({p.club_short_name or p.club_name}): {p.assists}助 ({apps}场, {p.key_passes}关键传球)")

    cards = [p for p in league_pss if (p.yellow_cards or 0) > 0 or (p.red_cards or 0) > 0]
    cards.sort(key=lambda x: (x.yellow_cards or 0, x.red_cards or 0), reverse=True)
    print("\nTop 10 Cards (kind='league'):")
    for i, p in enumerate(cards[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  #{i} {p.player_name} ({p.club_short_name or p.club_name}): {p.yellow_cards}黄, {p.red_cards}红 ({apps}场)")
