import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_TEAM_ID = 245
BEL_D2_CID = 1

with fmsave.open(save_path) as save:
    club_names = {}
    for c in save.clubs():
        for t in c.teams:
            club_names[t.team_id] = c.name

    for tbl in save.league_tables():
        if tbl.competition_id == BEL_D2_CID:
            print(f"Table rows count: {len(tbl.rows)}")
            for r in tbl.rows:
                cname = club_names.get(r.team_id, f"Team_{r.team_id}")
                is_me = (r.team_id == VIRTON_TEAM_ID)
                marker = " ★ MY TEAM" if is_me else ""
                print(f"  #{r.position:2d} | {cname:20s} | P={r.played} W={r.won} D={r.drawn} L={r.lost} GF={r.goals_for} GA={r.goals_against} GD={r.goals_for-r.goals_against:2d} Pts={r.points:2d}{marker}")
            break

    # Check top scorers for league kind
    d2_pss = [p for p in save.player_season_stats() if p.kind == 'league']
    virton_pss = [p for p in d2_pss if 'Virton' in str(getattr(p, 'club_name', '')) or getattr(p, 'club_uid', None) == 292]
    virton_pss.sort(key=lambda x: x.goals or 0, reverse=True)
    print("\nVirton top scorers (league):")
    for p in virton_pss[:10]:
        print(f"  {p.player_name}: {p.goals} goals, {p.assists} assists, {p.starts}+{p.substitute_appearances} apps")

    all_scorers = [p for p in d2_pss if (p.goals or 0) > 0]
    all_scorers.sort(key=lambda x: (x.goals or 0, -(x.starts or 0 + (x.substitute_appearances or 0))), reverse=True)
    print("\nTop 10 Scorers (D2 league):")
    for i, p in enumerate(all_scorers[:10], 1):
        apps = (p.starts or 0) + (p.substitute_appearances or 0)
        print(f"  #{i} {p.player_name} ({p.club_short_name or p.club_name}): {p.goals} goals ({apps} apps)")
