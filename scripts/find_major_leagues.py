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

    print("=== 探索赛事 ===")
    target_keywords = ['英格兰', '超级联赛', '西甲', '甲级', '比甲', '德甲', '意甲', '法甲', 'jupiler', 'premier', 'ligue', 'serie']
    
    # 看 competitions 的属性
    first_c = None
    for c in save.competitions():
        first_c = c
        break
    print(f"Competition dir: {[a for a in dir(first_c) if not a.startswith('_')]}")
    print(f"Competition repr: {repr(first_c)[:400]}")

    comps_found = []
    for c in save.competitions():
        name = getattr(c, 'name', '') or ''
        short = getattr(c, 'short_name', '') or ''
        cid = getattr(c, 'competition_id', None) or getattr(c, 'id', None)
        nation_id = getattr(c, 'nation_id', None)
        
        # 打印部分知名赛事
        full_str = f"{name} {short}".lower()
        if any(kw in full_str for kw in ['英超', '西甲', '意甲', '德甲', '法甲', 'jupiler', 'premier league', 'laliga', 'serie a', 'bundesliga', 'ligue 1', '比甲', '比乙', '挑战']):
            comps_found.append((cid, name, short, nation_id))
            print(f"  cid={cid} | {name} ({short}) | nation_id={nation_id}")

    print(f"\n匹配到赛事: {len(comps_found)}")

