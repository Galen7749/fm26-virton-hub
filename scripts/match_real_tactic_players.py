from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    # 1. Get selections
    selections = {}
    for s in save.selections():
        if getattr(s, 'club_uid', None) == 292 or getattr(s, 'team_id', None) == 245:
            if not getattr(s, 'substitute', False):
                selections[s.slot] = s.player_name

    # 2. Get tactics
    for i, t in enumerate(save.tactics()):
        print(f"\n--- Tactic {i}: {t.name} (Style: {getattr(t, 'style_name', '')}, Mentality: {t.mentality}) ---")
        for s in t.slots:
            in_pos = getattr(s, 'in_possession_positions', [None])[0]
            out_pos = getattr(s, 'out_possession_positions', [None])[0]
            player = selections.get(s.number, "Unknown")
            print(f"  Slot {s.number:2d}: Player: {player:<24} | In-pos: {in_pos} | Out-pos: {out_pos}")
