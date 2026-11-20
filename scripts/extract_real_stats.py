from pathlib import Path
import json
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    virton_stats = []
    for pss in save.player_season_stats():
        cuid = getattr(pss, 'club_uid', None)
        tid = getattr(pss, 'team_id', None)
        cname = getattr(pss, 'club_name', '') or ''
        
        if cuid == 292 or tid == 245 or "virton" in cname.lower():
            item = {
                "name": getattr(pss, 'player_name', ''),
                "club_uid": cuid,
                "club_name": cname,
                "starts": getattr(pss, 'starts', 0) or 0,
                "subs": getattr(pss, 'substitute_appearances', 0) or 0,
                "goals": getattr(pss, 'goals', 0) or 0,
                "assists": getattr(pss, 'assists', 0) or 0,
                "rating": getattr(pss, 'average_rating', 0.0) or 0.0,
                "mvp": getattr(pss, 'player_of_the_match', 0) or 0,
                "xg": getattr(pss, 'expected_goals', 0.0) or 0.0,
                "xa": getattr(pss, 'expected_assists', 0.0) or 0.0,
                "shots": getattr(pss, 'shots', 0) or 0,
                "shots_on_target": getattr(pss, 'shots_on_target', 0) or 0,
                "key_passes": getattr(pss, 'key_passes', 0) or 0,
                "tackles": getattr(pss, 'tackles_completed', 0) or 0,
                "interceptions": getattr(pss, 'interceptions', 0) or 0,
                "pass_pct": getattr(pss, 'pass_completion_percent', 0) or 0,
                "distance_km": getattr(pss, 'distance_km', 0.0) or 0.0,
                "yellow_cards": getattr(pss, 'yellow_cards', 0) or 0,
                "red_cards": getattr(pss, 'red_cards', 0) or 0,
            }
            if item['starts'] + item['subs'] > 0:
                virton_stats.append(item)

    virton_stats.sort(key=lambda x: (x['goals'], x['assists'], x['rating']), reverse=True)
    out_file = Path(r"I:\fm26-virton-hub\scripts\virton_players_season.json")
    out_file.write_text(json.dumps(virton_stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(virton_stats)} active Virton players to {out_file}!")
    for p in virton_stats[:15]:
        print(f"  {p['name']:<25} Apps:{p['starts']}(+{p['subs']}) G:{p['goals']} A:{p['assists']} Rating:{p['rating']:.2f} MVP:{p['mvp']} Yellow:{p['yellow_cards']}")
