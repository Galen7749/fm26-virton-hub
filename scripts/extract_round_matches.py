from pathlib import Path
import json
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name

    # Group Belgian D2 fixtures by date/round
    d2_fixtures = []
    for f in save.fixtures():
        if f.competition_id == 1 and f.home_goals is not None:
            home = team_to_club.get(f.home_team_id, f"Team_{f.home_team_id}")
            away = team_to_club.get(f.away_team_id, f"Team_{f.away_team_id}")
            d2_fixtures.append({
                "date": str(f.date),
                "home": home,
                "away": away,
                "score": f"{f.home_goals} - {f.away_goals}",
                "home_team_id": f.home_team_id,
                "away_team_id": f.away_team_id
            })

    print(f"Total played D2 fixtures: {len(d2_fixtures)}")
    d2_fixtures.sort(key=lambda x: x['date'])
    
    # Let's map dates to round numbers
    # Virton dates:
    # R1: 2025-08-10
    # R2: 2025-08-13
    # R3: 2025-08-17
    # R4: 2025-08-24
    # R5: 2025-08-31
    # R6: 2025-09-14
    # R7: 2025-09-24
    # R8: 2025-10-05
    round_dates = {
        "1": ["2025-08-08", "2025-08-09", "2025-08-10"],
        "2": ["2025-08-12", "2025-08-13"],
        "3": ["2025-08-15", "2025-08-16", "2025-08-17"],
        "4": ["2025-08-22", "2025-08-23", "2025-08-24"],
        "5": ["2025-08-29", "2025-08-30", "2025-08-31"],
        "6": ["2025-09-12", "2025-09-13", "2025-09-14"],
        "7": ["2025-09-23", "2025-09-24", "2025-09-25"],
        "8": ["2025-10-03", "2025-10-04", "2025-10-05"]
    }
    
    round_matches = {}
    for r_num, dates in round_dates.items():
        m_list = [f for f in d2_fixtures if f['date'] in dates]
        round_matches[r_num] = m_list
        print(f"Round {r_num} matches count: {len(m_list)}")

    out_file = Path(r"I:\fm26-virton-hub\web\src\data\round_matches.json")
    out_file.write_text(json.dumps(round_matches, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round_matches.json written successfully.")
