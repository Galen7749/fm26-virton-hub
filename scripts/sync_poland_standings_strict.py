"""
严格从 FM 存档 100% 真实同步波兰联赛积分榜、射手榜、助攻榜 (含强制 Sanity Check)
严禁任何手写、补全或估算数字！
"""
import glob
import json
import os
import fmsave

DATA_DIR = r"I:\fm26-virton-hub\web\src\data"

# 全站统一俱乐部中文译名映射 (key 为 club_uid)
CLUB_ZH_MAP = {
    129566: "奥波莱奥德拉",
    717323: "拉多米亚克",
    1456: "华沙莱吉亚",
    1300880: "维斯拉克拉科",
    722113: "琴斯托霍瓦",
    710033: "乔治罗尼亚比亚韦斯托克",
    1452: "扎布热戈尔尼克",
    1469: "KGHM卢宾扎格列比",
    1455: "波兹南莱赫",
    1451: "GKS卡托维兹",
    129581: "克拉科维亚",
    1467: "罗兹维泽夫",
    714217: "莫托路宾",
    1300882: "弗罗茨瓦夫西里西亚",
    1457: "普沃茨克维斯瓦",  # 纠正 FM 原生误译 "华沙普洛克"
    2000028448: "维彻兹塔克拉库瓦",
    1460: "罗切霍茹夫",
    710013: "莱格尼察铜业",
}

# 常用球员中文译名补充映射 (保持全站一致)
PLAYER_ZH_MAP = {
    "Jordy Soladio": "乔丹·索拉迪奥",
    "Kacper Przybyłko": "卡克佩尔·普日比乌科",
    "Patryk Szysz": "帕特里克·希什",
    "Babacar Dione": "巴巴卡尔·迪奥内",
    "Tomasz Gajda": "托马斯·加伊达",
    "Adrian Liber": "阿德里安·利贝尔",
    "Edoardo Iannoni": "伊多阿多·伊安诺尼",
    "Krystian Palacz": "克里斯蒂安·帕拉茨",
    "Mateusz Spychała": "马特乌什·斯皮哈瓦",
    "Jacky Donkor": "贾基·多恩科尔",
    "Jakub Szrek": "雅库布·什雷克",
    "Marin Pilj": "马林·皮尔伊",
    "Franciszek Franczak": "弗朗契斯扎克·弗兰恰克",
}


def get_latest_save():
    saves = sorted(
        glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"),
        key=lambda x: -os.path.getmtime(x),
    )
    if not saves:
        raise FileNotFoundError("未找到任何 .fm 存档文件")
    return saves[0]


def validate_league_table(table_rows, raw_rows):
    """强制完整性校验：闭环联赛必须满足总胜==总负、总进==总失、净胜球之和==0"""
    if len(table_rows) != 18:
        print("原始 league-tables 行数据:")
        for r in raw_rows:
            print(" ", r)
        raise ValueError(f"Sanity Check 失败: 联赛球队数应为 18 支，实际读取到 {len(table_rows)} 支！")

    total_w = sum(r["won"] for r in table_rows)
    total_l = sum(r["lost"] for r in table_rows)
    total_gf = sum(r["gf"] for r in table_rows)
    total_ga = sum(r["ga"] for r in table_rows)
    total_gd = sum(r["gd"] for r in table_rows)

    if total_w != total_l or total_gf != total_ga or total_gd != 0:
        print("原始 league-tables 行数据:")
        for r in raw_rows:
            print(" ", r)
        raise ValueError(
            f"Sanity Check 失败: 胜({total_w})!=负({total_l}) 或 进({total_gf})!=失({total_ga}) 或 净胜总和({total_gd})!=0"
        )

    print(
        f"✅ Sanity Check 通过: {len(table_rows)} 支球队 | "
        f"总胜=总负={total_w} | 总进=总失={total_gf} | 净胜总和={total_gd}"
    )


def main():
    save_path = get_latest_save()
    print("正在读取存档:", save_path)

    with fmsave.open(save_path) as s:
        team_to_club = {}
        odra_team_ids = set()
        for c in s.clubs():
            for t in getattr(c, "teams", []):
                team_to_club[t.team_id] = (c.uid, c.name)
                if c.uid == 129566:
                    odra_team_ids.add(t.team_id)

        # 1. 查找 comp_id == 188 且包含奥波莱奥德拉的真实联赛表
        target_lt = None
        for lt in s.league_tables():
            if getattr(lt, "competition_id", None) == 188:
                row_tids = {r.team_id for r in lt.rows}
                if row_tids & odra_team_ids:
                    target_lt = lt
                    break

        if target_lt is None:
            raise RuntimeError("未能从存档 league_tables 中找到 comp_id=188 且包含奥波莱奥德拉的积分榜")

        # 2. 构建完整积分榜 (100% 源自 target_lt.rows)
        league_team_ids = set()
        table_rows = []
        odra_row = None

        for idx, r in enumerate(target_lt.rows, start=1):
            league_team_ids.add(r.team_id)
            club_uid, raw_name = team_to_club.get(r.team_id, (None, f"team_{r.team_id}"))
            zh_name = CLUB_ZH_MAP.get(club_uid, raw_name.replace("足球俱乐部", ""))
            gd = r.goals_for - r.goals_against

            entry = {
                "position": idx,
                "team_name": zh_name,
                "played": int(r.played),
                "won": int(r.won),
                "drawn": int(r.drawn),
                "lost": int(r.lost),
                "gf": int(r.goals_for),
                "ga": int(r.goals_against),
                "gd": int(gd),
                "points": int(r.points),
            }
            if club_uid == 129566:
                entry["note"] = "直接升级区 · 关注主队 🇨🇳"
                odra_row = entry
            elif idx <= 2:
                entry["note"] = "直接升级区"
            elif idx <= 6:
                entry["note"] = "升级附加赛"
            elif idx >= 16:
                entry["note"] = "降级区"

            table_rows.append(entry)

        # 强制 Sanity Check
        validate_league_table(table_rows, target_lt.rows)

        # 3. 从 player_season_stats 100% 真实提取该联赛 18 支球队的联赛数据
        # 注意: kind.value == 'league' 对应联赛统计
        players_info = {
            pl.uid: (pl.name or pl.full_name or "", pl.club_uid)
            for pl in s.players()
        }

        league_pss = [
            pss
            for pss in s.player_season_stats()
            if pss.team_id in league_team_ids
            and getattr(getattr(pss, "kind", None), "value", None) == "league"
        ]
        print(f"匹配到本联赛球员赛季统计记录数: {len(league_pss)}")

        # 射手榜 Top 15 (按进球 desc, 点球 asc, 助攻 desc)
        scorer_stats = [p for p in league_pss if (getattr(p, "goals", 0) or 0) > 0]
        scorer_stats.sort(
            key=lambda p: (
                -(getattr(p, "goals", 0) or 0),
                (getattr(p, "penalties_scored", 0) or 0),
                -(getattr(p, "assists", 0) or 0),
            )
        )

        scorers_out = []
        for rank, p in enumerate(scorer_stats[:15], start=1):
            raw_pname, cid = players_info.get(p.player_uid, (getattr(p, "player_name", "?"), getattr(p, "club_uid", None)))
            if not raw_pname:
                raw_pname = getattr(p, "player_name", "?")
            pname = PLAYER_ZH_MAP.get(raw_pname, raw_pname)
            club_uid_resolved = team_to_club.get(p.team_id, (cid, ""))[0]
            team_zh = CLUB_ZH_MAP.get(club_uid_resolved, getattr(p, "club_short_name", "") or getattr(p, "club_name", ""))
            scorers_out.append(
                {
                    "rank": rank,
                    "player": pname,
                    "team": team_zh,
                    "goals": int(getattr(p, "goals", 0) or 0),
                    "penalties": int(getattr(p, "penalties_scored", 0) or 0),
                }
            )

        # 助攻榜 Top 15 (按助攻 desc, 进球 desc)
        assist_stats = [p for p in league_pss if (getattr(p, "assists", 0) or 0) > 0]
        assist_stats.sort(
            key=lambda p: (
                -(getattr(p, "assists", 0) or 0),
                -(getattr(p, "goals", 0) or 0),
            )
        )

        assists_out = []
        for rank, p in enumerate(assist_stats[:15], start=1):
            raw_pname, cid = players_info.get(p.player_uid, (getattr(p, "player_name", "?"), getattr(p, "club_uid", None)))
            if not raw_pname:
                raw_pname = getattr(p, "player_name", "?")
            pname = PLAYER_ZH_MAP.get(raw_pname, raw_pname)
            club_uid_resolved = team_to_club.get(p.team_id, (cid, ""))[0]
            team_zh = CLUB_ZH_MAP.get(club_uid_resolved, getattr(p, "club_short_name", "") or getattr(p, "club_name", ""))
            assists_out.append(
                {
                    "rank": rank,
                    "player": pname,
                    "team": team_zh,
                    "assists": int(getattr(p, "assists", 0) or 0),
                }
            )

        print("\n=== 真实射手榜 Top 10 ===")
        for s_item in scorers_out[:10]:
            print(f"  {s_item['rank']:2d}. {s_item['player']} ({s_item['team']}) - {s_item['goals']}球 (点球{s_item['penalties']})")

        print("\n=== 真实助攻榜 Top 10 ===")
        for a_item in assists_out[:10]:
            print(f"  {a_item['rank']:2d}. {a_item['player']} ({a_item['team']}) - {a_item['assists']}助")

    # 4. 写入 standings_multi.json
    standings_path = os.path.join(DATA_DIR, "standings_multi.json")
    with open(standings_path, "r", encoding="utf-8") as f:
        sdata = json.load(f)

    max_played = max(r["played"] for r in table_rows)
    for league in sdata.get("leagues", []):
        if league.get("key") == "pol_d1":
            league["round_info"] = (
                f"第 {max_played} 轮 战罢 · 奥波莱奥德拉 "
                f"{odra_row['won']}胜{odra_row['drawn']}平{odra_row['lost']}负积{odra_row['points']}分领跑"
            )
            league["table"] = table_rows
            league["scorers"] = scorers_out
            league["assists"] = assists_out
            break

    with open(standings_path, "w", encoding="utf-8") as f:
        json.dump(sdata, f, ensure_ascii=False, indent=2)
    print("\n✅ standings_multi.json 已 100% 真实更新")

    # 5. 同步修正 followed_clubs.json 中奥德拉战绩 (GF=20, GA=9, GD=+11)
    followed_path = os.path.join(DATA_DIR, "followed_clubs.json")
    with open(followed_path, "r", encoding="utf-8") as f:
        clubs_data = json.load(f)

    for club in clubs_data:
        if club.get("id") == "odra" and odra_row:
            club["rank"] = odra_row["position"]
            club["rank_desc"] = f"第 {odra_row['position']} 名 (直接升级区 · 领跑)"
            club["standing_summary"] = (
                f"{odra_row['won']}胜 {odra_row['drawn']}平 {odra_row['lost']}负 · "
                f"积{odra_row['points']}分 · 进{odra_row['gf']}球失{odra_row['ga']}球 · 净胜+{odra_row['gd']}"
            )
            club["stats"] = {
                "played": odra_row["played"],
                "won": odra_row["won"],
                "drawn": odra_row["drawn"],
                "lost": odra_row["lost"],
                "gf": odra_row["gf"],
                "ga": odra_row["ga"],
                "points": odra_row["points"],
            }
            break

    with open(followed_path, "w", encoding="utf-8") as f:
        json.dump(clubs_data, f, ensure_ascii=False, indent=2)
    print("✅ followed_clubs.json 已同步真实进失球与积分")


if __name__ == "__main__":
    main()
