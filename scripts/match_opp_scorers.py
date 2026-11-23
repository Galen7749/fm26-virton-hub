import fmsave
import json

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"

with open("I:/fm26-virton-hub/web/src/data/matches.json", encoding="utf-8") as f:
    matches = json.load(f)

with fmsave.open(save_path) as save:
    club_top_scorers = {}
    for p in save.player_season_stats():
        if (p.goals or 0) > 0 and p.club_name:
            club_top_scorers.setdefault(p.club_name, []).append({
                "name": p.player_name,
                "goals": p.goals,
                "kind": p.kind
            })

    # For each club, get top scorers
    for club in club_top_scorers:
        club_top_scorers[club].sort(key=lambda x: x["goals"], reverse=True)

    print("Found scorers for clubs:", len(club_top_scorers))
    for m in matches:
        is_home = (m["venue"] == "home")
        opp_name = m["away_team"] if is_home else m["home_team"]
        opp_score = m["score_away"] if is_home else m["score_home"]
        virton_score = m["score_home"] if is_home else m["score_away"]
        
        # Match club name in club_top_scorers
        matched_club = None
        for c in club_top_scorers:
            if c in opp_name or opp_name in c or opp_name.replace("皇家", "") in c:
                matched_club = c
                break
        
        scorers = club_top_scorers.get(matched_club, [])[:3] if matched_club else []
        scorer_names = [f"{s['name']} ({s['goals']}G)" for s in scorers]
        print(f"R{m['round']:02d}: Virton {virton_score} - {opp_score} {opp_name} (Matched: {matched_club}) -> Top Scorers: {scorer_names}")
