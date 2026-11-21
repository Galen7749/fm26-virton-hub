from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    print("--- Real Selected Lineup in FM Save ---")
    selections = []
    for s in save.selections():
        if getattr(s, 'club_uid', None) == 292 or getattr(s, 'team_id', None) == 245:
            selections.append({
                "slot": getattr(s, 'slot', None),
                "substitute": getattr(s, 'substitute', None),
                "player_name": getattr(s, 'player_name', None),
                "player_uid": getattr(s, 'player_uid', None),
            })

    selections.sort(key=lambda x: (1 if x['substitute'] else 0, x['slot'] if x['slot'] is not None else 99))
    for s in selections:
        status = "替补" if s['substitute'] else f"首发(Slot {s['slot']})"
        print(f"  {status:<15}: {s['player_name']} (uid: {s['player_uid']})")
