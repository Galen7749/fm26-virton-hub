import fmsave

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)

with fmsave.open(SAVE_PATH) as save:
    # 建立球队字典
    team_names = {}
    for c in save.clubs():
        for t in c.teams:
            team_names[t.team_id] = c.name

    print("=== 所有比赛/联赛 (Competitions) ===")
    comp_map = {}
    for comp in save.competitions():
        cname = getattr(comp, 'name', '') or getattr(comp, 'competition_name', '')
        cid = getattr(comp, 'competition_id', None) or getattr(comp, 'id', None)
        comp_map[cid] = cname

    print(f"总赛事数: {len(comp_map)}")

    # 查所有积分榜
    print("\n=== 存档中包含的积分榜 (League Tables) ===")
    found_tables = []
    for lt in save.league_tables():
        cname = comp_map.get(lt.competition_id, f"未知赛事_{lt.competition_id}")
        first_team = team_names.get(lt.rows[0].team_id, f"team_{lt.rows[0].team_id}") if lt.rows else ''
        print(f"cid={lt.competition_id} | 队数={lt.club_count} | 赛事名: {cname} | 榜首: {first_team}")
        found_tables.append((lt.competition_id, cname, lt.club_count))

