import traceback
from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    for i, lt in enumerate(save.league_tables()):
        for row in lt.rows:
            if row.team_id == 245:
                print(f"Table index {i}, comp_id: {lt.competition_id}, played: {row.played}, pts: {row.points}, matches_len: {len(row.matches)}")
                for m in row.matches:
                    if m.outcome is not None:
                        opp = team_to_club.get(m.opponent_team_id, m.opponent_team_id)
                        print(f"    m.slot={m.slot}, vs {opp}, ({m.home_or_away.value}) {m.goals_for}-{m.goals_against}, outcome={m.outcome.value}")

    print("\n--- Checking fixtures directly ---")
    virton_fixtures = []
    for f in save.fixtures():
        if f.home_team_id == 245 or f.away_team_id == 245:
            virton_fixtures.append(f)
    print(f"Found {len(virton_fixtures)} total fixtures involving Virton.")
    for f in virton_fixtures:
        home_name = team_to_club.get(f.home_team_id, f.home_team_id)
        away_name = team_to_club.get(f.away_team_id, f.away_team_id)
        # Check if match was played
        date_str = str(getattr(f, 'date', ''))
        sh = getattr(f, 'home_goals', None)
        sa = getattr(f, 'away_goals', None)
        print(f"  Fixture: {home_name} vs {away_name}, date={date_str}, goals={sh}-{sa}, cid={getattr(f, 'competition_id', None)}")
