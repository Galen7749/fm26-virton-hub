import fmsave, glob, os, datetime

saves = sorted(
    glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"),
    key=lambda x: -os.path.getmtime(x),
)
p = saves[0]

with fmsave.open(p) as s:
    team_to_club = {}
    for c in s.clubs():
        for t in getattr(c, "teams", []):
            team_to_club[t.team_id] = (c.uid, c.name)

    # 1. Check Odra fixtures in comp 188
    print("=== ODRA COMP 188 FIXTURES ===")
    for f in sorted(
        [fx for fx in s.fixtures() if fx.competition_id == 188 and (fx.home_team_id == 3073 or fx.away_team_id == 3073) and fx.home_goals is not None],
        key=lambda x: x.date,
    ):
        hc, hn = team_to_club.get(f.home_team_id, (None, str(f.home_team_id)))
        ac, an = team_to_club.get(f.away_team_id, (None, str(f.away_team_id)))
        print(f"  {f.date} | {hn} ({hc}) {f.home_goals} - {f.away_goals} {an} ({ac})")

    # 2. Check player_season_stats structure
    pss_list = list(s.player_season_stats())
    print("\nTotal player_season_stats:", len(pss_list))
    if pss_list:
        print("Sample attrs:", [a for a in dir(pss_list[0]) if not a.startswith("_")])
        print("Sample:", pss_list[0])

    # Filter pss for comp 188 or Odra players
    comp188_pss = [x for x in pss_list if getattr(x, "competition_id", None) == 188]
    print("pss with competition_id == 188:", len(comp188_pss))
    if comp188_pss:
        players = {pl.uid: (pl.name or pl.full_name or "", pl.club_uid, getattr(pl, "nationality_id", None)) for pl in s.players()}
        clubs = {c.uid: c.name for c in s.clubs()}
        top_g = sorted(comp188_pss, key=lambda x: (-(getattr(x, "goals", 0) or 0), -(getattr(x, "assists", 0) or 0)))[:15]
        print("\n=== TOP SCORERS (comp 188) ===")
        for x in top_g:
            pn, cid, nid = players.get(x.player_uid, ("?", None, None))
            print(f"  {pn:<25} | club={clubs.get(cid, cid)} | apps={getattr(x,'appearances',None)} | G={getattr(x,'goals',0)} | A={getattr(x,'assists',0)} | rating={getattr(x,'average_rating',None)}")
        top_a = sorted(comp188_pss, key=lambda x: (-(getattr(x, "assists", 0) or 0), -(getattr(x, "goals", 0) or 0)))[:15]
        print("\n=== TOP ASSISTS (comp 188) ===")
        for x in top_a:
            pn, cid, nid = players.get(x.player_uid, ("?", None, None))
            print(f"  {pn:<25} | club={clubs.get(cid, cid)} | apps={getattr(x,'appearances',None)} | G={getattr(x,'goals',0)} | A={getattr(x,'assists',0)} | rating={getattr(x,'average_rating',None)}")
