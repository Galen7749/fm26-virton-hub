"""
探针 v2：
1. 探索 managed_clubs 属性找到维尔通
2. 通过 clubs 表建立 team_id → club_name 映射
3. 找到比乙 (Challenger Pro League) 的积分榜和维尔通的赛程
4. 提取维尔通球员的前 3 场比赛数据
"""
import fmsave
import json

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)

with fmsave.open(SAVE_PATH) as save:

    # ===== 1. managed_clubs 属性探索 =====
    print("=" * 60)
    print("[1] managed_clubs 属性探索")
    managed = save.managed_clubs()
    for mc in managed:
        print(f"  dir(mc): {[a for a in dir(mc) if not a.startswith('_')]}")
        # 尝试常见属性
        for attr in ['club_uid', 'club_name', 'club_short_name', 'team_id', 'name',
                      'short_name', 'club', 'uid', 'competition_id']:
            if hasattr(mc, attr):
                print(f"    {attr} = {getattr(mc, attr)}")
        print(f"  repr: {repr(mc)}")
        break  # 只看第一个

    # ===== 2. clubs 表：建立 team_id → club_name 映射 =====
    print("\n" + "=" * 60)
    print("[2] clubs 表探索")
    clubs = save.clubs()
    # 先看第一条的结构
    first_club = None
    for c in clubs:
        first_club = c
        break
    print(f"  dir(club): {[a for a in dir(first_club) if not a.startswith('_')]}")
    print(f"  repr: {repr(first_club)[:500]}")

    # 建立映射表
    team_to_club = {}
    club_uid_to_name = {}
    virton_data = None
    for c in clubs:
        cname = getattr(c, 'name', None) or getattr(c, 'club_name', None) or ''
        cuid = getattr(c, 'club_uid', None) or getattr(c, 'uid', None)
        tid = getattr(c, 'team_id', None)
        short = getattr(c, 'short_name', None) or getattr(c, 'club_short_name', None) or ''

        if tid is not None:
            team_to_club[tid] = cname or short
        if cuid is not None:
            club_uid_to_name[cuid] = cname or short

        # 找维尔通
        name_lower = (cname + short).lower()
        if 'virton' in name_lower or '维尔通' in name_lower:
            virton_data = c
            print(f"\n  [找到维尔通!] name={cname}, short={short}, uid={cuid}, team_id={tid}")
            print(f"  repr: {repr(c)[:800]}")

    print(f"\n  clubs 总数: {len(team_to_club)}")

    # ===== 3. 存档基本信息 =====
    print("\n" + "=" * 60)
    print("[3] 存档基本信息 (save.info())")
    try:
        info = save.info()
        print(f"  dir: {[a for a in dir(info) if not a.startswith('_')]}")
        print(f"  repr: {repr(info)[:500]}")
    except Exception as e:
        print(f"  info() 失败: {e}")

    # ===== 4. competitions 表：找比乙 =====
    print("\n" + "=" * 60)
    print("[4] competitions 表探索")
    comps = save.competitions()
    target_comp_ids = []
    for comp in comps:
        cname = getattr(comp, 'name', '') or getattr(comp, 'competition_name', '') or ''
        cid = getattr(comp, 'competition_id', None) or getattr(comp, 'id', None)
        name_lower = cname.lower()
        if any(kw in name_lower for kw in ['challenger', 'belg', '比利时', 'jupiler', 'eerste']):
            print(f"  comp_id={cid}: {cname}")
            target_comp_ids.append(cid)
        elif any(kw in name_lower for kw in ['virton', '维尔通']):
            print(f"  [维尔通相关] comp_id={cid}: {cname}")
            target_comp_ids.append(cid)

    # ===== 5. 找维尔通球员的比赛数据（前 3 轮） =====
    print("\n" + "=" * 60)
    print("[5] player_match_stats：维尔通球员的前 3 场比赛")
    pms = save.player_match_stats()
    virton_matches = {}  # date → list of player stats
    count = 0
    for stat in pms:
        # player_match_stats 包含 opponent_club_name，
        # 我们需要找到属于维尔通的球员
        # 从探针 v1 知道第一条是 Arthur Cremer vs 登德
        # 如果 Cremer 是维尔通球员，那所有 opponent 就是维尔通的对手
        if count < 3:
            print(f"  stat[{count}]: player={stat.player_name}, date={stat.date}, "
                  f"opponent={stat.opponent_club_name}, "
                  f"goals={stat.goals}, assists={stat.assists}, rating={stat.rating}, "
                  f"minutes={stat.minutes}, position={stat.position}")
            count += 1

    # 收集前 50 条数据来看看都有哪些球员和对手
    pms2 = save.player_match_stats()
    players_seen = set()
    opponents_seen = set()
    dates_seen = set()
    sample_count = 0
    for stat in pms2:
        if sample_count >= 200:
            break
        players_seen.add(stat.player_name)
        if stat.opponent_club_name:
            opponents_seen.add(stat.opponent_club_name)
        dates_seen.add(str(stat.date))
        sample_count += 1

    print(f"\n  前 200 条 player_match_stats 中：")
    print(f"    球员: {sorted(players_seen)}")
    print(f"    对手: {sorted(opponents_seen)}")
    print(f"    日期: {sorted(dates_seen)}")

    # ===== 6. 如果找到维尔通 team_id，查积分榜 =====
    if virton_data:
        virton_tid = getattr(virton_data, 'team_id', None)
        print(f"\n" + "=" * 60)
        print(f"[6] 维尔通 (team_id={virton_tid}) 在积分榜中的位置")
        for lt in save.league_tables():
            for row in lt.rows:
                if row.team_id == virton_tid:
                    print(f"  competition_id={lt.competition_id}")
                    print(f"  position={row.position}, played={row.played}, "
                          f"W={row.won} D={row.drawn} L={row.lost}, "
                          f"GF={row.goals_for} GA={row.goals_against}, "
                          f"points={row.points}")
                    # 打印逐场结果
                    for m in row.matches:
                        if m.outcome is not None:
                            opp_name = team_to_club.get(m.opponent_team_id, f"team_{m.opponent_team_id}")
                            print(f"    slot={m.slot} {m.home_or_away} vs {opp_name}: "
                                  f"{m.goals_for}-{m.goals_against} ({m.outcome})")

print("\n" + "=" * 60)
print("探针 v2 完成。")
