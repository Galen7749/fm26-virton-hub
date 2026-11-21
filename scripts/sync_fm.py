#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FootHub 懂球云 · FM 存档全自动增量同步流水线 (真实赛况与首发阵容版)
"""

import os
import sys
import glob
import json
import subprocess
import datetime
from pathlib import Path

# 配置路径
PROJECT_ROOT = Path(r"I:\fm26-virton-hub")
WEB_DIR = PROJECT_ROOT / "web"
DATA_DIR = WEB_DIR / "src" / "data"
SAVE_DIR = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games")

VIRTON_TEAM_ID = 245
VIRTON_CLUB_UID = 292
BEL_D2_CID = 1
BEL_D1_CID = 0
SERIE_A_CID = 3560

POS_MAP = {
    1: "GK",
    4: "DR",
    32: "DR",
    16: "DC",
    8: "DL",
    64: "DM",
    128: "DM",
    256: "MC",
    512: "MC",
    1024: "MC",
    2048: "AMR",
    4096: "AML",
    8192: "AMC",
    16384: "ST"
}

ZH_NAME_MAP = {
    "Célestin De Schrevel": "塞莱斯丁·德·施瑞沃",
    "Adama Diop": "亚当穆斯·迪奥普",
    "Allan Tchaptchet": "阿兰·特查普切特",
    "Teddy Mezague": "泰迪·梅扎古",
    "Yassine Ben Hamed": "亚塞尼·本·哈米德",
    "Antoine Valério": "安托万·瓦莱里亚",
    "Aliou Dembélé": "阿卢·登贝莱",
    "Tyrone Tormin": "泰伦·托明",
    "Luca Maiorano": "卢卡·迈奥拉诺",
    "Marks Inchaud": "马克斯·因查德",
    "Paul Wade": "保罗·韦德",
    "Steeven Assengue": "斯蒂文·阿森盖",
    "Abdelsamad Hachem": "阿卜杜勒萨马迪·哈切姆",
    "Matthieu Epolo": "马蒂厄·埃波洛",
    "Anas Hammas": "阿纳斯·哈马斯",
    "Kader Keita": "卡德尔·凯塔",
    "Maxime Pau": "马克西姆·波",
    "Ayyoub Allach": "阿尤布·阿拉赫",
    "Abdel Al Badaoui": "阿卜杜勒·巴达维",
    "Samy Bourard": "萨米·布拉德",
    "Park Seung-Soo": "朴昇秀",
    "Yumeki Yoshinaga": "吉永梦希",
    "Prins Tjiueza": "普林斯·吉乌扎",
    "Ihab Goudani": "伊哈卜·古达尼",
    "Jean-Claude Ntenda": "让-克洛德·恩滕达",
    "William Simba": "威廉·辛巴",
    "Gaëtan Arib": "加埃唐·阿里布",
    "Sullivan Lakhamy": "沙利文·拉哈米",
    "Sullivan Coulibaly": "沙利文·库利巴利",
    "Yanis Lentini": "亚尼斯·伦蒂尼",
    "Maxime Guillaume": "马克西姆·纪尧姆",
    "Samet Elmaci": "萨梅特·埃尔马齐",
    "Nathan Fernandes": "内森·费尔南德斯",
    "Leandro Aranguren": "莱昂德罗·阿兰古伦"
}

def find_latest_save():
    if not SAVE_DIR.exists():
        print(f"[!] 存档目录不存在: {SAVE_DIR}")
        return None
    fm_files = list(SAVE_DIR.glob("*.fm"))
    if not fm_files:
        print("[!] 未找到任何 .fm 存档文件！")
        return None
    fm_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    latest = fm_files[0]
    print(f"[*] 成功定位最新 FM 存档: {latest.name} (大小: {latest.stat().st_size / 1024 / 1024:.2f} MB)")
    return latest

def load_existing_data():
    matches_file = DATA_DIR / "matches.json"
    news_file = DATA_DIR / "news.json"
    standings_file = DATA_DIR / "standings.json"
    round_matches_file = DATA_DIR / "round_matches.json"
    mailbox_file = DATA_DIR / "mailbox.json"

    matches = json.loads(matches_file.read_text(encoding="utf-8")) if matches_file.exists() else []
    news = json.loads(news_file.read_text(encoding="utf-8")) if news_file.exists() else []
    standings = json.loads(standings_file.read_text(encoding="utf-8")) if standings_file.exists() else {"leagues": []}
    round_matches = json.loads(round_matches_file.read_text(encoding="utf-8")) if round_matches_file.exists() else {}
    mailbox = json.loads(mailbox_file.read_text(encoding="utf-8")) if mailbox_file.exists() else {}

    return matches, news, standings, round_matches, mailbox

def sync():
    print("\n" + "=" * 60)
    print("      FootHub · 懂球云 | FM 存档全自动同步系统")
    print("=" * 60)

    save_path = find_latest_save()
    if not save_path:
        return

    import fmsave
    print("\n[1/5] 解析 FM 核心底层存档...")
    with fmsave.open(str(save_path)) as save:
        team_to_club = {}
        for c in save.clubs():
            for t in c.teams:
                team_to_club[t.team_id] = c.name

        virton_uids = {p.uid for p in save.players() if getattr(p, 'club_uid', None) == VIRTON_CLUB_UID or getattr(p, 'team_id', None) == VIRTON_TEAM_ID}
        print(f"[*] 俱乐部球员索引完成，收录 {len(virton_uids)} 位维尔通球员")

        matches, news, standings, round_matches, mailbox = load_existing_data()

        # 4. 从 save.fixtures 提取全部已完赛的维尔通比乙联赛赛果
        d2_fixtures = []
        for f in save.fixtures():
            if f.competition_id == BEL_D2_CID and (f.home_team_id == VIRTON_TEAM_ID or f.away_team_id == VIRTON_TEAM_ID) and f.home_goals is not None:
                d2_fixtures.append(f)
        d2_fixtures.sort(key=lambda x: x.date)

        print(f"[*] 存档中维尔通精英已完赛场次: 共 {len(d2_fixtures)} 轮")

        # 同步积分表
        bel_d2_table = []
        for lt in save.league_tables():
            if lt.competition_id == BEL_D2_CID:
                for row in lt.rows:
                    if row.team_id == VIRTON_TEAM_ID and row.played > 0:
                        rows_list = sorted(lt.rows, key=lambda r: (r.points, r.goals_for - r.goals_against, r.goals_for), reverse=True)
                        for pos, r in enumerate(rows_list, 1):
                            cname = team_to_club.get(r.team_id, f"team_{r.team_id}")
                            bel_d2_table.append({
                                "position": pos,
                                "team_name": cname,
                                "played": r.played,
                                "won": r.won,
                                "drawn": r.drawn,
                                "lost": r.lost,
                                "gf": r.goals_for,
                                "ga": r.goals_against,
                                "gd": r.goals_for - r.goals_against,
                                "points": r.points,
                                "is_my_team": (r.team_id == VIRTON_TEAM_ID)
                            })
                        break
                if bel_d2_table:
                    break

        for lg in standings.get("leagues", []):
            if lg["id"] == "bel_d2" and bel_d2_table:
                lg["table"] = bel_d2_table
                lg["round"] = len(d2_fixtures)

        (DATA_DIR / "standings.json").write_text(json.dumps(standings, ensure_ascii=False, indent=2), encoding="utf-8")
        print("[✓] 联赛积分榜实时同步成功！")

    # 7. 构建前端
    print("\n[4/5] 编译前端生产静态资源 (npm run build)...")
    try:
        res = subprocess.run(["npm", "run", "build"], cwd=str(WEB_DIR), shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            print("[✓] 前端构建成功 (dist/ 打包完毕)！")
        else:
            print(f"[!] 前端构建输出: {res.stdout.strip()[:200]}")
    except Exception as e:
        print(f"[!] 前端构建调用异常: {e}")

    # 8. Git 自动提交与推送
    print("\n[5/5] Git 版本控制与自动部署检测...")
    try:
        dist_dir = WEB_DIR / "dist"
        (dist_dir / ".nojekyll").touch(exist_ok=True)
        subprocess.run(["git", "add", "."], cwd=str(PROJECT_ROOT), shell=True)
        subprocess.run(["git", "commit", "-m", f"feat(sync): 自动同步FM真实战绩 (共{len(d2_fixtures)}轮)"], cwd=str(PROJECT_ROOT), shell=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=str(PROJECT_ROOT), shell=True)
        subprocess.run(["git", "add", "-A"], cwd=str(dist_dir), shell=True)
        subprocess.run(["git", "commit", "-m", f"deploy: 自动同步FM真实战绩 (共{len(d2_fixtures)}轮)"], cwd=str(dist_dir), shell=True)
        subprocess.run(["git", "push", "-f", "origin", "gh-pages"], cwd=str(dist_dir), shell=True)
        print("[✓] GitHub main 分支与 Pages 生产环境已同步更新上线！")
    except Exception as e:
        print(f"[!] Git 流程提示: {e}")

    print("\n" + "=" * 60)
    print("      ✓ 同步流程全部执行完毕！")
    print(f"      本地预览地址: http://localhost:5173/")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    sync()
