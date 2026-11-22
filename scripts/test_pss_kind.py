import fmsave

save_path = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm"
VIRTON_CLUB_UID = 292

with fmsave.open(save_path) as save:
    for p in save.player_season_stats():
        if p.club_uid == VIRTON_CLUB_UID and 'Hachem' in (p.player_name or ''):
            print(f"Hachem row: kind={getattr(p, 'kind', None)}, goals={p.goals}, assists={p.assists}, apps={p.starts}+{p.substitute_appearances}, minutes={p.minutes}")
