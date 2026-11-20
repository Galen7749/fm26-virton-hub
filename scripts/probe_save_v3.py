"""
探针 v3：用已知信息精确提取维尔通的核心数据
- 维尔通 club_uid=292, team_id=245
- 通过 clubs.teams 建立 team_id → club_name 映射
- 提取维尔通在积分榜的排名
- 提取有实际数据的 player_match_stats（进球、助攻、评分）
- 探索 team_match_stats 获取球队级别赛后数据
"""
import fmsave

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\" + "耶稣 徐- 失\u200b业中.fm"
)
VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292

with fmsave.open(SAVE_PATH) as save:

    # ===== 1. 建立 team_id → club_name 映射 =====
    print("[1] 建立 team_id → club_name 映射")
    team_to_club = {}
    for c in save.clubs():
        for t in c.teams:
            team_to_club[t.team_id] = c.name
    print(f"  映射条目数: {len(team_to_club)}")
    # 验证维尔通
    print(f"  team_id=245 → {team_to_club.get(245, 'NOT FOUND')}")
    # 打印比乙常见球队
    for tid in [245]:
        print(f"  team_id={tid} → {team_to_club.get(tid)}")

    # ===== 2. 维尔通在所有积分榜中的位置 =====
    print("\n" + "=" * 60)
    print("[2] 维尔通在积分榜中的位置")
    for lt in save.league_tables():
        for row in lt.rows:
            if row.team_id == VIRTON_TEAM_ID:
                print(f"\n  ★ competition_id={lt.competition_id}, club_count={lt.club_count}")
                print(f"  排名: {row.position}/{lt.club_count}")
                print(f"  战绩: {row.played}场 {row.won}胜 {row.drawn}平 {row.lost}负")
                print(f"  进球: {row.goals_for} 失球: {row.goals_against} 净胜: {row.goals_for - row.goals_against}")
                print(f"  积分: {row.points}")
                print(f"\n  逐场记录:")
                for m in row.matches:
                    if m.outcome is not None:
                        opp = team_to_club.get(m.opponent_team_id, f"team_{m.opponent_team_id}")
                        print(f"    R{m.slot+1} [{m.home_or_away.value.upper():4s}] vs {opp}: "
                              f"{m.goals_for}-{m.goals_against} → {m.outcome.value.upper()}")

                # 也打印完整积分榜
                print(f"\n  完整积分榜:")
                for r in lt.rows:
                    club_name = team_to_club.get(r.team_id, f"team_{r.team_id}")
                    marker = " ◄◄ 维尔通" if r.team_id == VIRTON_TEAM_ID else ""
                    print(f"    {r.position}. {club_name}: "
                          f"{r.played}场 {r.won}W {r.drawn}D {r.lost}L | "
                          f"{r.goals_for}:{r.goals_against} | {r.points}分{marker}")

    # ===== 3. 维尔通球员有实际数据的比赛统计 =====
    print("\n" + "=" * 60)
    print("[3] 维尔通球员比赛统计（有实际数据的）")
    matches_by_date = {}
    for stat in save.player_match_stats():
        # player_match_stats 看起来只包含managed team的球员
        # 只看有数据的（has_stats=True 或 goals/rating 不为 None）
        key = str(stat.date)
        if key not in matches_by_date:
            matches_by_date[key] = {
                'opponent': stat.opponent_club_name,
                'opponent_short': stat.opponent_club_short_name,
                'players': []
            }
        if stat.has_stats or stat.goals is not None or stat.rating is not None:
            matches_by_date[key]['players'].append({
                'name': stat.player_name,
                'position': str(stat.position) if stat.position else None,
                'minutes': stat.minutes,
                'goals': stat.goals,
                'assists': stat.assists,
                'rating': stat.rating,
                'passes_att': stat.passes_attempted,
                'passes_comp': stat.passes_completed,
            })

    for date in sorted(matches_by_date.keys()):
        match = matches_by_date[date]
        players_with_data = match['players']
        print(f"\n  📅 {date} vs {match['opponent']} ({match['opponent_short']})")
        print(f"  有数据球员: {len(players_with_data)}人")
        if players_with_data:
            # 按评分排序
            sorted_players = sorted(players_with_data,
                                     key=lambda p: p['rating'] or 0, reverse=True)
            for p in sorted_players:
                goals_str = f" ⚽{p['goals']}" if p['goals'] and p['goals'] > 0 else ""
                assists_str = f" 🅰️{p['assists']}" if p['assists'] and p['assists'] > 0 else ""
                print(f"    {p['name']:25s} | {p['position'] or '?':8s} | "
                      f"{p['minutes'] or '?':>3}min | ⭐{p['rating'] or '?'}"
                      f"{goals_str}{assists_str}")

    # ===== 4. team_match_stats 探索 =====
    print("\n" + "=" * 60)
    print("[4] team_match_stats 探索")
    tms = save.team_match_stats()
    first_tms = None
    count = 0
    for t in tms:
        if count == 0:
            print(f"  dir: {[a for a in dir(t) if not a.startswith('_')]}")
        # 找维尔通的比赛
        tid = getattr(t, 'team_id', None)
        if tid == VIRTON_TEAM_ID:
            if count < 10:
                print(f"\n  维尔通 team_match_stats [{count}]:")
                print(f"    repr: {repr(t)[:600]}")
            count += 1
    print(f"\n  维尔通 team_match_stats 总数: {count}")

    # ===== 5. 维尔通的 fixtures =====
    print("\n" + "=" * 60)
    print("[5] 维尔通的 fixtures (赛程)")
    virton_fixtures = []
    for f in save.fixtures():
        if f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID:
            virton_fixtures.append(f)
    
    # 按日期排序
    virton_fixtures.sort(key=lambda x: x.date)
    print(f"  维尔通总赛程数: {len(virton_fixtures)}")
    for f in virton_fixtures[:15]:
        home = team_to_club.get(f.home_team_id, f"team_{f.home_team_id}")
        away = team_to_club.get(f.away_team_id, f"team_{f.away_team_id}")
        played_str = f"{f.home_goals}-{f.away_goals}" if f.played else "未赛"
        is_home = f.home_team_id == VIRTON_TEAM_ID
        marker = "🏠" if is_home else "✈️"
        print(f"    {marker} {f.date} | {home} {played_str} {away} | comp={f.competition_id} | {'已赛' if f.played else '待赛'}")

    # ===== 6. save.info 属性探索 =====
    print("\n" + "=" * 60)
    print("[6] save.info 属性")
    info = save.info
    print(f"  dir: {[a for a in dir(info) if not a.startswith('_')]}")
    for attr in [a for a in dir(info) if not a.startswith('_')]:
        try:
            val = getattr(info, attr)
            if not callable(val):
                print(f"    {attr} = {val}")
        except:
            pass

print("\n探针 v3 完成 ✅")
