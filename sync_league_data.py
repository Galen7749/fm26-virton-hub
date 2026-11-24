"""
sync_league_data.py
懂球云 · 全球 11 大联赛数据引擎与完整榜单同步系统
- 彻底移除比乙 (bel_d2)
- 覆盖三大欧战：欧冠 (ucl)、欧联 (uel)、欧协联 (uecl) (各 36 队完整瑞士轮联赛大榜单)
- 覆盖五大联赛 + 中超 + 波甲 + 比甲：全量 16~20 队完整大名单
- 支持数学自洽校验 (played == won + drawn + lost, gd == gf - ga, points == won * 3 + drawn)
- 支持 FM 外部导出文件批量解析导入与自动轮次同步
"""

import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "web" / "src" / "data"

def get_complete_leagues():
    return [
        # ──────────────────────────────────────────────────────────
        # 1. 欧洲冠军联赛 (欧冠, 36 队新赛制联赛阶段大榜单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "ucl",
            "name": "欧洲冠军联赛 (欧冠)",
            "label": "欧冠",
            "short_name": "欧冠",
            "flag_icon": "circle-flags:eu",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "温布利决赛 · 皇马捧得第16座大耳朵杯",
            "table": [
                { "position": 1, "team_name": "皇家马德里", "played": 8, "won": 7, "drawn": 1, "lost": 0, "gf": 22, "ga": 6, "gd": 16, "points": 22, "note": "直接晋级16强" },
                { "position": 2, "team_name": "利物浦", "played": 8, "won": 7, "drawn": 0, "lost": 1, "gf": 19, "ga": 5, "gd": 14, "points": 21, "note": "直接晋级16强" },
                { "position": 3, "team_name": "曼彻斯特城", "played": 8, "won": 6, "drawn": 2, "lost": 0, "gf": 24, "ga": 8, "gd": 16, "points": 20, "note": "直接晋级16强" },
                { "position": 4, "team_name": "拜仁慕尼黑", "played": 8, "won": 6, "drawn": 1, "lost": 1, "gf": 20, "ga": 7, "gd": 13, "points": 19, "note": "直接晋级16强" },
                { "position": 5, "team_name": "巴塞罗那", "played": 8, "won": 6, "drawn": 0, "lost": 2, "gf": 21, "ga": 9, "gd": 12, "points": 18, "note": "直接晋级16强" },
                { "position": 6, "team_name": "阿森纳", "played": 8, "won": 5, "drawn": 2, "lost": 1, "gf": 16, "ga": 5, "gd": 11, "points": 17, "note": "直接晋级16强" },
                { "position": 7, "team_name": "勒沃库森", "played": 8, "won": 5, "drawn": 2, "lost": 1, "gf": 17, "ga": 8, "gd": 9, "points": 17, "note": "直接晋级16强" },
                { "position": 8, "team_name": "国际米兰", "played": 8, "won": 5, "drawn": 1, "lost": 2, "gf": 13, "ga": 5, "gd": 8, "points": 16, "note": "直接晋级16强" },
                { "position": 9, "team_name": "多特蒙德", "played": 8, "won": 5, "drawn": 0, "lost": 3, "gf": 18, "ga": 11, "gd": 7, "points": 15, "note": "淘汰赛附加赛 (种子)" },
                { "position": 10, "team_name": "马德里竞技", "played": 8, "won": 5, "drawn": 0, "lost": 3, "gf": 15, "ga": 10, "gd": 5, "points": 15, "note": "淘汰赛附加赛 (种子)" },
                { "position": 11, "team_name": "亚特兰大", "played": 8, "won": 4, "drawn": 2, "lost": 2, "gf": 14, "ga": 7, "gd": 7, "points": 14, "note": "淘汰赛附加赛 (种子)" },
                { "position": 12, "team_name": "尤文图斯", "played": 8, "won": 4, "drawn": 2, "lost": 2, "gf": 12, "ga": 8, "gd": 4, "points": 14, "note": "淘汰赛附加赛 (种子)" },
                { "position": 13, "team_name": "巴黎圣日耳曼", "played": 8, "won": 4, "drawn": 1, "lost": 3, "gf": 14, "ga": 11, "gd": 3, "points": 13, "note": "淘汰赛附加赛 (种子)" },
                { "position": 14, "team_name": "阿斯顿维拉", "played": 8, "won": 4, "drawn": 1, "lost": 3, "gf": 11, "ga": 9, "gd": 2, "points": 13, "note": "淘汰赛附加赛 (种子)" },
                { "position": 15, "team_name": "里斯本竞技", "played": 8, "won": 4, "drawn": 1, "lost": 3, "gf": 13, "ga": 12, "gd": 1, "points": 13, "note": "淘汰赛附加赛 (种子)" },
                { "position": 16, "team_name": "摩纳哥", "played": 8, "won": 3, "drawn": 3, "lost": 2, "gf": 12, "ga": 11, "gd": 1, "points": 12, "note": "淘汰赛附加赛 (种子)" },
                { "position": 17, "team_name": "布鲁日", "played": 8, "won": 3, "drawn": 2, "lost": 3, "gf": 10, "ga": 10, "gd": 0, "points": 11, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 18, "team_name": "里尔", "played": 8, "won": 3, "drawn": 2, "lost": 3, "gf": 11, "ga": 12, "gd": -1, "points": 11, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 19, "team_name": "本菲卡", "played": 8, "won": 3, "drawn": 1, "lost": 4, "gf": 12, "ga": 13, "gd": -1, "points": 10, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 20, "team_name": "费耶诺德", "played": 8, "won": 3, "drawn": 1, "lost": 4, "gf": 13, "ga": 16, "gd": -3, "points": 10, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 21, "team_name": "埃因霍温", "played": 8, "won": 2, "drawn": 3, "lost": 3, "gf": 12, "ga": 14, "gd": -2, "points": 9, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 22, "team_name": "AC米兰", "played": 8, "won": 3, "drawn": 0, "lost": 5, "gf": 10, "ga": 13, "gd": -3, "points": 9, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 23, "team_name": "萨格勒布迪纳摩", "played": 8, "won": 2, "drawn": 2, "lost": 4, "gf": 9, "ga": 15, "gd": -6, "points": 8, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 24, "team_name": "斯图加特", "played": 8, "won": 2, "drawn": 2, "lost": 4, "gf": 9, "ga": 16, "gd": -7, "points": 8, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 25, "team_name": "顿涅茨克矿工", "played": 8, "won": 2, "drawn": 1, "lost": 5, "gf": 8, "ga": 15, "gd": -7, "points": 7, "note": "淘汰出局" },
                { "position": 26, "team_name": "布拉格斯巴达", "played": 8, "won": 2, "drawn": 1, "lost": 5, "gf": 7, "ga": 16, "gd": -9, "points": 7, "note": "淘汰出局" },
                { "position": 27, "team_name": "凯尔特人", "played": 8, "won": 2, "drawn": 0, "lost": 6, "gf": 9, "ga": 19, "gd": -10, "points": 6, "note": "淘汰出局" },
                { "position": 28, "team_name": "萨尔茨堡红牛", "played": 8, "won": 1, "drawn": 2, "lost": 5, "gf": 6, "ga": 17, "gd": -11, "points": 5, "note": "淘汰出局" },
                { "position": 29, "team_name": "博洛尼亚", "played": 8, "won": 1, "drawn": 2, "lost": 5, "gf": 4, "ga": 15, "gd": -11, "points": 5, "note": "淘汰出局" },
                { "position": 30, "team_name": "赫罗纳", "played": 8, "won": 1, "drawn": 1, "lost": 6, "gf": 6, "ga": 17, "gd": -11, "points": 4, "note": "淘汰出局" },
                { "position": 31, "team_name": "莱比锡RB", "played": 8, "won": 1, "drawn": 0, "lost": 7, "gf": 7, "ga": 18, "gd": -11, "points": 3, "note": "淘汰出局" },
                { "position": 32, "team_name": "贝尔格莱德红星", "played": 8, "won": 1, "drawn": 0, "lost": 7, "gf": 8, "ga": 21, "gd": -13, "points": 3, "note": "淘汰出局" },
                { "position": 33, "team_name": "布雷斯特", "played": 8, "won": 0, "drawn": 2, "lost": 6, "gf": 5, "ga": 19, "gd": -14, "points": 2, "note": "淘汰出局" },
                { "position": 34, "team_name": "格拉茨风暴", "played": 8, "won": 0, "drawn": 2, "lost": 6, "gf": 4, "ga": 19, "gd": -15, "points": 2, "note": "淘汰出局" },
                { "position": 35, "team_name": "伯尔尼年轻人", "played": 8, "won": 0, "drawn": 1, "lost": 7, "gf": 4, "ga": 22, "gd": -18, "points": 1, "note": "淘汰出局" },
                { "position": 36, "team_name": "布拉迪斯拉发", "played": 8, "won": 0, "drawn": 0, "lost": 8, "gf": 3, "ga": 25, "gd": -22, "points": 0, "note": "淘汰出局" }
            ],
            "scorers": [
                { "rank": 1, "player": "基利安·姆巴佩", "team": "皇家马德里", "goals": 10, "penalties": 2, "matches": 12 },
                { "rank": 2, "player": "哈里·凯恩", "team": "拜仁慕尼黑", "goals": 8, "penalties": 3, "matches": 12 },
                { "rank": 3, "player": "维尼修斯", "team": "皇家马德里", "goals": 7, "penalties": 0, "matches": 11 },
                { "rank": 4, "player": "哈兰德", "team": "曼彻斯特城", "goals": 6, "penalties": 1, "matches": 8 },
                { "rank": 5, "player": "拉菲尼亚", "team": "巴塞罗那", "goals": 6, "penalties": 0, "matches": 10 }
            ],
            "assists": [
                { "rank": 1, "player": "维尼修斯", "team": "皇家马德里", "assists": 6, "matches": 11 },
                { "rank": 2, "player": "贝林厄姆", "team": "皇家马德里", "assists": 5, "matches": 12 },
                { "rank": 3, "player": "德布劳内", "team": "曼彻斯特城", "assists": 4, "matches": 7 },
                { "rank": 4, "player": "萨卡", "team": "阿森纳", "assists": 4, "matches": 9 },
                { "rank": 5, "player": "亚马尔", "team": "巴塞罗那", "assists": 4, "matches": 10 }
            ],
            "transfers": [
                { "date": "2026-06-03", "type": "重磅官宣", "player": "基利安·姆巴佩", "from": "巴黎圣日耳曼", "to": "皇家马德里", "fee": "自由身免签加盟" },
                { "date": "2026-07-02", "type": "官宣", "player": "阿尔瓦雷斯", "from": "曼彻斯特城", "to": "马德里竞技", "fee": "转会费 7500万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 2. 欧洲联赛 (欧联/欧联杯, 36 队新赛制联赛阶段大榜单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "uel",
            "name": "欧足联欧洲联赛 (欧联)",
            "label": "欧联",
            "short_name": "欧联",
            "flag_icon": "circle-flags:eu",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "都柏林竞技场 · 热刺登顶欧联之巅",
            "table": [
                { "position": 1, "team_name": "托特纳姆热刺", "played": 8, "won": 7, "drawn": 1, "lost": 0, "gf": 20, "ga": 6, "gd": 14, "points": 22, "note": "直接晋级16强" },
                { "position": 2, "team_name": "曼彻斯特联", "played": 8, "won": 6, "drawn": 2, "lost": 0, "gf": 19, "ga": 7, "gd": 12, "points": 20, "note": "直接晋级16强" },
                { "position": 3, "team_name": "拉齐奥", "played": 8, "won": 6, "drawn": 1, "lost": 1, "gf": 17, "ga": 6, "gd": 11, "points": 19, "note": "直接晋级16强" },
                { "position": 4, "team_name": "毕尔巴鄂竞技", "played": 8, "won": 6, "drawn": 1, "lost": 1, "gf": 16, "ga": 7, "gd": 9, "points": 19, "note": "直接晋级16强" },
                { "position": 5, "team_name": "法兰克福", "played": 8, "won": 5, "drawn": 2, "lost": 1, "gf": 18, "ga": 10, "gd": 8, "points": 17, "note": "直接晋级16强" },
                { "position": 6, "team_name": "里昂", "played": 8, "won": 5, "drawn": 1, "lost": 2, "gf": 16, "ga": 9, "gd": 7, "points": 16, "note": "直接晋级16强" },
                { "position": 7, "team_name": "波尔图", "played": 8, "won": 5, "drawn": 1, "lost": 2, "gf": 15, "ga": 9, "gd": 6, "points": 16, "note": "直接晋级16强" },
                { "position": 8, "team_name": "阿贾克斯", "played": 8, "won": 4, "drawn": 3, "lost": 1, "gf": 14, "ga": 8, "gd": 6, "points": 15, "note": "直接晋级16强" },
                { "position": 9, "team_name": "皇家社会", "played": 8, "won": 4, "drawn": 2, "lost": 2, "gf": 13, "ga": 8, "gd": 5, "points": 14, "note": "淘汰赛附加赛 (种子)" },
                { "position": 10, "team_name": "罗马", "played": 8, "won": 4, "drawn": 2, "lost": 2, "gf": 12, "ga": 8, "gd": 4, "points": 14, "note": "淘汰赛附加赛 (种子)" },
                { "position": 11, "team_name": "加拉塔萨雷", "played": 8, "won": 4, "drawn": 1, "lost": 3, "gf": 15, "ga": 13, "gd": 2, "points": 13, "note": "淘汰赛附加赛 (种子)" },
                { "position": 12, "team_name": "费内巴切", "played": 8, "won": 4, "drawn": 1, "lost": 3, "gf": 13, "ga": 12, "gd": 1, "points": 13, "note": "淘汰赛附加赛 (种子)" },
                { "position": 13, "team_name": "阿尔克马尔", "played": 8, "won": 3, "drawn": 3, "lost": 2, "gf": 12, "ga": 10, "gd": 2, "points": 12, "note": "淘汰赛附加赛 (种子)" },
                { "position": 14, "team_name": "安德莱赫特", "played": 8, "won": 3, "drawn": 3, "lost": 2, "gf": 11, "ga": 10, "gd": 1, "points": 12, "note": "淘汰赛附加赛 (种子)" },
                { "position": 15, "team_name": "布拉加", "played": 8, "won": 3, "drawn": 2, "lost": 3, "gf": 11, "ga": 11, "gd": 0, "points": 11, "note": "淘汰赛附加赛 (种子)" },
                { "position": 16, "team_name": "霍芬海姆", "played": 8, "won": 3, "drawn": 2, "lost": 3, "gf": 13, "ga": 14, "gd": -1, "points": 11, "note": "淘汰赛附加赛 (种子)" },
                { "position": 17, "team_name": "格拉斯哥流浪者", "played": 8, "won": 3, "drawn": 1, "lost": 4, "gf": 10, "ga": 12, "gd": -2, "points": 10, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 18, "team_name": "布拉格斯拉维亚", "played": 8, "won": 3, "drawn": 1, "lost": 4, "gf": 9, "ga": 11, "gd": -2, "points": 10, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 19, "team_name": "奥林匹亚科斯", "played": 8, "won": 2, "drawn": 3, "lost": 3, "gf": 9, "ga": 10, "gd": -1, "points": 9, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 20, "team_name": "尼斯", "played": 8, "won": 2, "drawn": 3, "lost": 3, "gf": 10, "ga": 12, "gd": -2, "points": 9, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 21, "team_name": "中日德兰", "played": 8, "won": 2, "drawn": 3, "lost": 3, "gf": 8, "ga": 11, "gd": -3, "points": 9, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 22, "team_name": "圣吉罗斯联", "played": 8, "won": 2, "drawn": 2, "lost": 4, "gf": 9, "ga": 13, "gd": -4, "points": 8, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 23, "team_name": "特温特", "played": 8, "won": 2, "drawn": 2, "lost": 4, "gf": 8, "ga": 13, "gd": -5, "points": 8, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 24, "team_name": "博德闪耀", "played": 8, "won": 2, "drawn": 1, "lost": 5, "gf": 9, "ga": 15, "gd": -6, "points": 7, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 25, "team_name": "贝西克塔斯", "played": 8, "won": 2, "drawn": 1, "lost": 5, "gf": 8, "ga": 15, "gd": -7, "points": 7, "note": "淘汰出局" },
                { "position": 26, "team_name": "帕奥克", "played": 8, "won": 1, "drawn": 3, "lost": 4, "gf": 7, "ga": 13, "gd": -6, "points": 6, "note": "淘汰出局" },
                { "position": 27, "team_name": "普尔岑胜利", "played": 8, "won": 1, "drawn": 3, "lost": 4, "gf": 8, "ga": 15, "gd": -7, "points": 6, "note": "淘汰出局" },
                { "position": 28, "team_name": "马尔默", "played": 8, "won": 1, "drawn": 2, "lost": 5, "gf": 6, "ga": 14, "gd": -8, "points": 5, "note": "淘汰出局" },
                { "position": 29, "team_name": "特拉维夫马卡比", "played": 8, "won": 1, "drawn": 1, "lost": 6, "gf": 7, "ga": 17, "gd": -10, "points": 4, "note": "淘汰出局" },
                { "position": 30, "team_name": "埃尔夫斯堡", "played": 8, "won": 1, "drawn": 1, "lost": 6, "gf": 6, "ga": 17, "gd": -11, "points": 4, "note": "淘汰出局" },
                { "position": 31, "team_name": "卡拉巴赫", "played": 8, "won": 1, "drawn": 0, "lost": 7, "gf": 5, "ga": 18, "gd": -13, "points": 3, "note": "淘汰出局" },
                { "position": 32, "team_name": "卢多戈雷茨", "played": 8, "won": 0, "drawn": 3, "lost": 5, "gf": 4, "ga": 15, "gd": -11, "points": 3, "note": "淘汰出局" },
                { "position": 33, "team_name": "基辅迪纳摩", "played": 8, "won": 0, "drawn": 2, "lost": 6, "gf": 4, "ga": 18, "gd": -14, "points": 2, "note": "淘汰出局" },
                { "position": 34, "team_name": "里加FS", "played": 8, "won": 0, "drawn": 2, "lost": 6, "gf": 3, "ga": 18, "gd": -15, "points": 2, "note": "淘汰出局" },
                { "position": 35, "team_name": "圣吉罗斯", "played": 8, "won": 0, "drawn": 1, "lost": 7, "gf": 3, "ga": 20, "gd": -17, "points": 1, "note": "淘汰出局" },
                { "position": 36, "team_name": "贝斯塔", "played": 8, "won": 0, "drawn": 1, "lost": 7, "gf": 2, "ga": 22, "gd": -20, "points": 1, "note": "淘汰出局" }
            ],
            "scorers": [
                { "rank": 1, "player": "孙兴慜", "team": "托特纳姆热刺", "goals": 7, "penalties": 1, "matches": 9 },
                { "rank": 2, "player": "布鲁诺·费尔南德斯", "team": "曼彻斯特联", "goals": 6, "penalties": 2, "matches": 10 },
                { "rank": 3, "player": "奥斯梅恩", "team": "加拉塔萨雷", "goals": 6, "penalties": 0, "matches": 7 },
                { "rank": 4, "player": "马尔穆什", "team": "法兰克福", "goals": 5, "penalties": 1, "matches": 8 },
                { "rank": 5, "player": "拉卡泽特", "team": "里昂", "goals": 5, "penalties": 1, "matches": 8 }
            ],
            "assists": [
                { "rank": 1, "player": "布鲁诺·费尔南德斯", "team": "曼彻斯特联", "assists": 6, "matches": 10 },
                { "rank": 2, "player": "麦迪逊", "team": "托特纳姆热刺", "assists": 5, "matches": 9 },
                { "rank": 3, "player": "切尔基", "team": "里昂", "assists": 4, "matches": 8 }
            ],
            "transfers": [
                { "date": "2026-07-15", "type": "官宣", "player": "德里赫特", "from": "拜仁慕尼黑", "to": "曼彻斯特联", "fee": "转会费 4500万欧" },
                { "date": "2026-07-10", "type": "租借", "player": "奥斯梅恩", "from": "那不勒斯", "to": "加拉塔萨雷", "fee": "纯租借无买断" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 3. 欧足联欧洲协会联赛 (欧协联, 36 队新赛制联赛阶段大榜单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "uecl",
            "name": "欧足联协会联赛 (欧协联)",
            "label": "欧协联",
            "short_name": "欧协联",
            "flag_icon": "circle-flags:eu",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "弗罗茨瓦夫城市球场 · 切尔西捧杯登顶",
            "table": [
                { "position": 1, "team_name": "切尔西", "played": 6, "won": 6, "drawn": 0, "lost": 0, "gf": 22, "ga": 4, "gd": 18, "points": 18, "note": "直接晋级16强" },
                { "position": 2, "team_name": "佛罗伦萨", "played": 6, "won": 5, "drawn": 1, "lost": 0, "gf": 15, "ga": 5, "gd": 10, "points": 16, "note": "直接晋级16强" },
                { "position": 3, "team_name": "皇家贝蒂斯", "played": 6, "won": 4, "drawn": 2, "lost": 0, "gf": 13, "ga": 5, "gd": 8, "points": 14, "note": "直接晋级16强" },
                { "position": 4, "team_name": "海登海姆", "played": 6, "won": 4, "drawn": 1, "lost": 1, "gf": 12, "ga": 6, "gd": 6, "points": 13, "note": "直接晋级16强" },
                { "position": 5, "team_name": "华沙莱吉亚", "played": 6, "won": 4, "drawn": 0, "lost": 2, "gf": 11, "ga": 6, "gd": 5, "points": 12, "note": "直接晋级16强" },
                { "position": 6, "team_name": "维也纳快速", "played": 6, "won": 4, "drawn": 0, "lost": 2, "gf": 10, "ga": 6, "gd": 4, "points": 12, "note": "直接晋级16强" },
                { "position": 7, "team_name": "根特", "played": 6, "won": 3, "drawn": 2, "lost": 1, "gf": 9, "ga": 5, "gd": 4, "points": 11, "note": "直接晋级16强" },
                { "position": 8, "team_name": "亚盖隆尼亚", "played": 6, "won": 3, "drawn": 2, "lost": 1, "gf": 10, "ga": 7, "gd": 3, "points": 11, "note": "直接晋级16强" },
                { "position": 9, "team_name": "哥本哈根", "played": 6, "won": 3, "drawn": 1, "lost": 2, "gf": 9, "ga": 7, "gd": 2, "points": 10, "note": "淘汰赛附加赛 (种子)" },
                { "position": 10, "team_name": "色格拉布鲁日", "played": 6, "won": 3, "drawn": 1, "lost": 2, "gf": 8, "ga": 6, "gd": 2, "points": 10, "note": "淘汰赛附加赛 (种子)" },
                { "position": 11, "team_name": "帕纳辛奈科斯", "played": 6, "won": 3, "drawn": 1, "lost": 2, "gf": 8, "ga": 7, "gd": 1, "points": 10, "note": "淘汰赛附加赛 (种子)" },
                { "position": 12, "team_name": "吉马良斯", "played": 6, "won": 3, "drawn": 1, "lost": 2, "gf": 7, "ga": 6, "gd": 1, "points": 10, "note": "淘汰赛附加赛 (种子)" },
                { "position": 13, "team_name": "莫尔德", "played": 6, "won": 3, "drawn": 0, "lost": 3, "gf": 8, "ga": 8, "gd": 0, "points": 9, "note": "淘汰赛附加赛 (种子)" },
                { "position": 14, "team_name": "帕福斯", "played": 6, "won": 3, "drawn": 0, "lost": 3, "gf": 7, "ga": 7, "gd": 0, "points": 9, "note": "淘汰赛附加赛 (种子)" },
                { "position": 15, "team_name": "希腊人竞技", "played": 6, "won": 2, "drawn": 2, "lost": 2, "gf": 6, "ga": 6, "gd": 0, "points": 8, "note": "淘汰赛附加赛 (种子)" },
                { "position": 16, "team_name": "尤尔戈登", "played": 6, "won": 2, "drawn": 2, "lost": 2, "gf": 7, "ga": 8, "gd": -1, "points": 8, "note": "淘汰赛附加赛 (种子)" },
                { "position": 17, "team_name": "林茨", "played": 6, "won": 2, "drawn": 2, "lost": 2, "gf": 6, "ga": 7, "gd": -1, "points": 8, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 18, "team_name": "巴萨克赛尔", "played": 6, "won": 2, "drawn": 1, "lost": 3, "gf": 7, "ga": 8, "gd": -1, "points": 7, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 19, "team_name": "圣加仑", "played": 6, "won": 2, "drawn": 1, "lost": 3, "gf": 8, "ga": 10, "gd": -2, "points": 7, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 20, "team_name": "卢布尔雅那奥林匹亚", "played": 6, "won": 2, "drawn": 1, "lost": 3, "gf": 6, "ga": 8, "gd": -2, "points": 7, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 21, "team_name": "巴尼亚卢卡战士", "played": 6, "won": 2, "drawn": 1, "lost": 3, "gf": 5, "ga": 8, "gd": -3, "points": 7, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 22, "team_name": "采列", "played": 6, "won": 2, "drawn": 0, "lost": 4, "gf": 6, "ga": 10, "gd": -4, "points": 6, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 23, "team_name": "诺亚FC", "played": 6, "won": 1, "drawn": 2, "lost": 3, "gf": 5, "ga": 9, "gd": -4, "points": 5, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 24, "team_name": "赫尔辛基", "played": 6, "won": 1, "drawn": 2, "lost": 3, "gf": 4, "ga": 9, "gd": -5, "points": 5, "note": "淘汰赛附加赛 (非种子)" },
                { "position": 25, "team_name": "明斯克迪纳摩", "played": 6, "won": 1, "drawn": 1, "lost": 4, "gf": 4, "ga": 10, "gd": -6, "points": 4, "note": "淘汰出局" },
                { "position": 26, "team_name": "莫斯塔尔兹林伊斯基", "played": 6, "won": 1, "drawn": 1, "lost": 4, "gf": 4, "ga": 10, "gd": -6, "points": 4, "note": "淘汰出局" },
                { "position": 27, "team_name": "姆拉达博莱斯拉夫", "played": 6, "won": 1, "drawn": 1, "lost": 4, "gf": 3, "ga": 10, "gd": -7, "points": 4, "note": "淘汰出局" },
                { "position": 28, "team_name": "佩特罗库布", "played": 6, "won": 1, "drawn": 0, "lost": 5, "gf": 4, "ga": 12, "gd": -8, "points": 3, "note": "淘汰出局" },
                { "position": 29, "team_name": "巴奇卡托波拉", "played": 6, "won": 1, "drawn": 0, "lost": 5, "gf": 3, "ga": 12, "gd": -9, "points": 3, "note": "淘汰出局" },
                { "position": 30, "team_name": "塞浦路斯阿波罗", "played": 6, "won": 0, "drawn": 2, "lost": 4, "gf": 3, "ga": 11, "gd": -8, "points": 2, "note": "淘汰出局" },
                { "position": 31, "team_name": "维京古尔", "played": 6, "won": 0, "drawn": 2, "lost": 4, "gf": 3, "ga": 12, "gd": -9, "points": 2, "note": "淘汰出局" },
                { "position": 32, "team_name": "新圣徒", "played": 6, "won": 0, "drawn": 2, "lost": 4, "gf": 2, "ga": 12, "gd": -10, "points": 2, "note": "淘汰出局" },
                { "position": 33, "team_name": "拉恩", "played": 6, "won": 0, "drawn": 1, "lost": 5, "gf": 2, "ga": 13, "gd": -11, "points": 1, "note": "淘汰出局" },
                { "position": 34, "team_name": "阿斯塔纳", "played": 6, "won": 0, "drawn": 1, "lost": 5, "gf": 2, "ga": 14, "gd": -12, "points": 1, "note": "淘汰出局" },
                { "position": 35, "team_name": "贝斯塔", "played": 6, "won": 0, "drawn": 1, "lost": 5, "gf": 1, "ga": 15, "gd": -14, "points": 1, "note": "淘汰出局" },
                { "position": 36, "team_name": "地拉那游击队", "played": 6, "won": 0, "drawn": 0, "lost": 6, "gf": 1, "ga": 17, "gd": -16, "points": 0, "note": "淘汰出局" }
            ],
            "scorers": [
                { "rank": 1, "player": "恩昆库", "team": "切尔西", "goals": 6, "penalties": 2, "matches": 6 },
                { "rank": 2, "player": "基恩", "team": "佛罗伦萨", "goals": 5, "penalties": 0, "matches": 6 },
                { "rank": 3, "player": "费利佩·安德森", "team": "华沙莱吉亚", "goals": 4, "penalties": 1, "matches": 5 }
            ],
            "assists": [
                { "rank": 1, "player": "穆德里克", "team": "切尔西", "assists": 4, "matches": 5 },
                { "rank": 2, "player": "伊斯科", "team": "皇家贝蒂斯", "assists": 3, "matches": 5 }
            ],
            "transfers": [
                { "date": "2026-07-08", "type": "官宣", "player": "内托", "from": "狼队", "to": "切尔西", "fee": "转会费 6000万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 4. 英格兰足球超级联赛 (英超, 20 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "pl",
            "name": "英格兰足球超级联赛 (英超)",
            "label": "英超",
            "short_name": "英超",
            "flag_icon": "circle-flags:gb-eng",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "第 38 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "曼彻斯特城", "played": 38, "won": 28, "drawn": 7, "lost": 3, "gf": 96, "ga": 34, "gd": 62, "points": 91, "note": "英超冠军 · 欧冠正赛" },
                { "position": 2, "team_name": "阿森纳", "played": 38, "won": 28, "drawn": 5, "lost": 5, "gf": 91, "ga": 29, "gd": 62, "points": 89, "note": "欧冠正赛" },
                { "position": 3, "team_name": "利物浦", "played": 38, "won": 24, "drawn": 10, "lost": 4, "gf": 86, "ga": 41, "gd": 45, "points": 82, "note": "欧冠正赛" },
                { "position": 4, "team_name": "阿斯顿维拉", "played": 38, "won": 20, "drawn": 8, "lost": 10, "gf": 76, "ga": 61, "gd": 15, "points": 68, "note": "欧冠正赛" },
                { "position": 5, "team_name": "托特纳姆热刺", "played": 38, "won": 20, "drawn": 6, "lost": 12, "gf": 74, "ga": 61, "gd": 13, "points": 66, "note": "欧联正赛" },
                { "position": 6, "team_name": "切尔西", "played": 38, "won": 18, "drawn": 9, "lost": 11, "gf": 77, "ga": 63, "gd": 14, "points": 63, "note": "欧联正赛" },
                { "position": 7, "team_name": "纽卡斯尔联", "played": 38, "won": 18, "drawn": 6, "lost": 14, "gf": 85, "ga": 62, "gd": 23, "points": 60, "note": "欧协联附加赛" },
                { "position": 8, "team_name": "曼彻斯特联", "played": 38, "won": 18, "drawn": 6, "lost": 14, "gf": 57, "ga": 58, "gd": -1, "points": 60 },
                { "position": 9, "team_name": "西汉姆联", "played": 38, "won": 14, "drawn": 10, "lost": 14, "gf": 60, "ga": 74, "gd": -14, "points": 52 },
                { "position": 10, "team_name": "水晶宫", "played": 38, "won": 13, "drawn": 10, "lost": 15, "gf": 57, "ga": 58, "gd": -1, "points": 49 },
                { "position": 11, "team_name": "布莱顿", "played": 38, "won": 12, "drawn": 12, "lost": 14, "gf": 55, "ga": 62, "gd": -7, "points": 48 },
                { "position": 12, "team_name": "伯恩茅斯", "played": 38, "won": 13, "drawn": 9, "lost": 16, "gf": 54, "ga": 67, "gd": -13, "points": 48 },
                { "position": 13, "team_name": "富勒姆", "played": 38, "won": 13, "drawn": 8, "lost": 17, "gf": 55, "ga": 61, "gd": -6, "points": 47 },
                { "position": 14, "team_name": "狼队", "played": 38, "won": 13, "drawn": 7, "lost": 18, "gf": 50, "ga": 65, "gd": -15, "points": 46 },
                { "position": 15, "team_name": "埃弗顿", "played": 38, "won": 13, "drawn": 9, "lost": 16, "gf": 40, "ga": 51, "gd": -11, "points": 40, "deduction": 8, "note": "财务PSR违规扣8分" },
                { "position": 16, "team_name": "布伦特福德", "played": 38, "won": 10, "drawn": 9, "lost": 19, "gf": 56, "ga": 65, "gd": -9, "points": 39 },
                { "position": 17, "team_name": "诺丁汉森林", "played": 38, "won": 9, "drawn": 9, "lost": 20, "gf": 49, "ga": 67, "gd": -18, "points": 32, "deduction": 4, "note": "财务PSR违规扣4分" },
                { "position": 18, "team_name": "卢顿", "played": 38, "won": 6, "drawn": 8, "lost": 24, "gf": 52, "ga": 85, "gd": -33, "points": 26, "note": "降入英冠" },
                { "position": 19, "team_name": "伯恩利", "played": 38, "won": 5, "drawn": 9, "lost": 24, "gf": 41, "ga": 78, "gd": -37, "points": 24, "note": "降入英冠" },
                { "position": 20, "team_name": "谢菲尔德联", "played": 38, "won": 3, "drawn": 7, "lost": 28, "gf": 35, "ga": 104, "gd": -69, "points": 16, "note": "降入英冠" }
            ],
            "scorers": [
                { "rank": 1, "player": "埃尔林·哈兰德", "team": "曼彻斯特城", "goals": 27, "penalties": 5, "matches": 35 },
                { "rank": 2, "player": "科尔·帕尔默", "team": "切尔西", "goals": 22, "penalties": 8, "matches": 34 },
                { "rank": 3, "player": "亚历山大·伊萨克", "team": "纽卡斯尔联", "goals": 21, "penalties": 4, "matches": 32 },
                { "rank": 4, "player": "菲尔·福登", "team": "曼彻斯特城", "goals": 19, "penalties": 0, "matches": 35 },
                { "rank": 5, "player": "奥利·沃特金斯", "team": "阿斯顿维拉", "goals": 19, "penalties": 0, "matches": 37 }
            ],
            "assists": [
                { "rank": 1, "player": "奥利·沃特金斯", "team": "阿斯顿维拉", "assists": 13, "matches": 37 },
                { "rank": 2, "player": "科尔·帕尔默", "team": "切尔西", "assists": 11, "matches": 34 },
                { "rank": 3, "player": "德布劳内", "team": "曼彻斯特城", "assists": 10, "matches": 18 },
                { "rank": 4, "player": "萨拉赫", "team": "利物浦", "assists": 10, "matches": 32 },
                { "rank": 5, "player": "吉布斯-怀特", "team": "诺丁汉森林", "assists": 10, "matches": 37 }
            ],
            "transfers": [
                { "date": "2026-07-20", "type": "官宣", "player": "萨维尼奥", "from": "特鲁瓦", "to": "曼彻斯特城", "fee": "转会费 3500万欧" },
                { "date": "2026-07-18", "type": "官宣", "player": "卡拉菲奥里", "from": "博洛尼亚", "to": "阿森纳", "fee": "转会费 4500万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 5. 西班牙足球甲级联赛 (西甲, 20 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "laliga",
            "name": "西班牙足球甲级联赛 (西甲)",
            "label": "西甲",
            "short_name": "西甲",
            "flag_icon": "circle-flags:es",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "第 38 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "皇家马德里", "played": 38, "won": 29, "drawn": 8, "lost": 1, "gf": 87, "ga": 26, "gd": 61, "points": 95, "note": "西甲冠军 · 欧冠正赛" },
                { "position": 2, "team_name": "巴塞罗那", "played": 38, "won": 26, "drawn": 7, "lost": 5, "gf": 79, "ga": 44, "gd": 35, "points": 85, "note": "欧冠正赛" },
                { "position": 3, "team_name": "赫罗纳", "played": 38, "won": 25, "drawn": 6, "lost": 7, "gf": 85, "ga": 46, "gd": 39, "points": 81, "note": "欧冠正赛" },
                { "position": 4, "team_name": "马德里竞技", "played": 38, "won": 24, "drawn": 4, "lost": 10, "gf": 70, "ga": 43, "gd": 27, "points": 76, "note": "欧冠正赛" },
                { "position": 5, "team_name": "毕尔巴鄂竞技", "played": 38, "won": 19, "drawn": 11, "lost": 8, "gf": 61, "ga": 37, "gd": 24, "points": 68, "note": "欧联正赛" },
                { "position": 6, "team_name": "皇家社会", "played": 38, "won": 16, "drawn": 12, "lost": 10, "gf": 51, "ga": 39, "gd": 12, "points": 60, "note": "欧联正赛" },
                { "position": 7, "team_name": "皇家贝蒂斯", "played": 38, "won": 14, "drawn": 15, "lost": 9, "gf": 48, "ga": 45, "gd": 3, "points": 57, "note": "欧协联附加赛" },
                { "position": 8, "team_name": "比利亚雷亚尔", "played": 38, "won": 14, "drawn": 11, "lost": 13, "gf": 65, "ga": 65, "gd": 0, "points": 53 },
                { "position": 9, "team_name": "瓦伦西亚", "played": 38, "won": 13, "drawn": 10, "lost": 15, "gf": 40, "ga": 45, "gd": -5, "points": 49 },
                { "position": 10, "team_name": "阿拉维斯", "played": 38, "won": 12, "drawn": 10, "lost": 16, "gf": 36, "ga": 46, "gd": -10, "points": 46 },
                { "position": 11, "team_name": "奥萨苏纳", "played": 38, "won": 12, "drawn": 9, "lost": 17, "gf": 45, "ga": 56, "gd": -11, "points": 45 },
                { "position": 12, "team_name": "赫塔费", "played": 38, "won": 10, "drawn": 13, "lost": 15, "gf": 42, "ga": 54, "gd": -12, "points": 43 },
                { "position": 13, "team_name": "塞尔塔", "played": 38, "won": 10, "drawn": 11, "lost": 17, "gf": 46, "ga": 57, "gd": -11, "points": 41 },
                { "position": 14, "team_name": "塞维利亚", "played": 38, "won": 10, "drawn": 11, "lost": 17, "gf": 48, "ga": 54, "gd": -6, "points": 41 },
                { "position": 15, "team_name": "马略卡", "played": 38, "won": 8, "drawn": 16, "lost": 14, "gf": 33, "ga": 44, "gd": -11, "points": 40 },
                { "position": 16, "team_name": "拉斯帕尔马斯", "played": 38, "won": 10, "drawn": 10, "lost": 18, "gf": 33, "ga": 47, "gd": -14, "points": 40 },
                { "position": 17, "team_name": "巴列卡诺", "played": 38, "won": 8, "drawn": 14, "lost": 16, "gf": 29, "ga": 48, "gd": -19, "points": 38 },
                { "position": 18, "team_name": "加的斯", "played": 38, "won": 6, "drawn": 15, "lost": 17, "gf": 26, "ga": 55, "gd": -29, "points": 33, "note": "降入西乙" },
                { "position": 19, "team_name": "阿尔梅里亚", "played": 38, "won": 3, "drawn": 12, "lost": 23, "gf": 43, "ga": 75, "gd": -32, "points": 21, "note": "降入西乙" },
                { "position": 20, "team_name": "格拉纳达", "played": 38, "won": 4, "drawn": 9, "lost": 25, "gf": 38, "ga": 79, "gd": -41, "points": 21, "note": "降入西乙" }
            ],
            "scorers": [
                { "rank": 1, "player": "阿尔乔姆·多夫比克", "team": "赫罗纳", "goals": 24, "penalties": 7, "matches": 36 },
                { "rank": 2, "player": "亚历山大·索尔洛特", "team": "比利亚雷亚尔", "goals": 23, "penalties": 0, "matches": 34 },
                { "rank": 3, "player": "贝林厄姆", "team": "皇家马德里", "goals": 19, "penalties": 1, "matches": 28 },
                { "rank": 4, "player": "莱万多夫斯基", "team": "巴塞罗那", "goals": 19, "penalties": 4, "matches": 35 },
                { "rank": 5, "player": "格列兹曼", "team": "马德里竞技", "goals": 16, "penalties": 4, "matches": 33 }
            ],
            "assists": [
                { "rank": 1, "player": "阿莱克斯·巴埃纳", "team": "比利亚雷亚尔", "assists": 14, "matches": 34 },
                { "rank": 2, "player": "尼科·威廉姆斯", "team": "毕尔巴鄂竞技", "assists": 11, "matches": 31 },
                { "rank": 3, "player": "萨维尼奥", "team": "赫罗纳", "assists": 10, "matches": 37 }
            ],
            "transfers": [
                { "date": "2026-06-12", "type": "官宣", "player": "恩德里克", "from": "帕尔梅拉斯", "to": "皇家马德里", "fee": "转会费 4750万欧" },
                { "date": "2026-07-28", "type": "官宣", "player": "奥尔莫", "from": "莱比锡RB", "to": "巴塞罗那", "fee": "转会费 5500万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 6. 意大利足球甲级联赛 (意甲, 20 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "serie_a",
            "name": "意大利足球甲级联赛 (意甲)",
            "label": "意甲",
            "short_name": "意甲",
            "flag_icon": "circle-flags:it",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "第 38 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "国际米兰", "played": 38, "won": 29, "drawn": 7, "lost": 2, "gf": 89, "ga": 22, "gd": 67, "points": 94, "note": "意甲冠军 · 欧冠正赛" },
                { "position": 2, "team_name": "AC米兰", "played": 38, "won": 22, "drawn": 9, "lost": 7, "gf": 76, "ga": 49, "gd": 27, "points": 75, "note": "欧冠正赛" },
                { "position": 3, "team_name": "尤文图斯", "played": 38, "won": 19, "drawn": 14, "lost": 5, "gf": 54, "ga": 31, "gd": 23, "points": 71, "note": "欧冠正赛" },
                { "position": 4, "team_name": "亚特兰大", "played": 38, "won": 21, "drawn": 6, "lost": 11, "gf": 72, "ga": 42, "gd": 30, "points": 69, "note": "欧冠正赛" },
                { "position": 5, "team_name": "博洛尼亚", "played": 38, "won": 18, "drawn": 14, "lost": 6, "gf": 54, "ga": 32, "gd": 22, "points": 68, "note": "欧冠正赛 (意甲欧战红利)" },
                { "position": 6, "team_name": "罗马", "played": 38, "won": 18, "drawn": 9, "lost": 11, "gf": 65, "ga": 46, "gd": 19, "points": 63, "note": "欧联正赛" },
                { "position": 7, "team_name": "拉齐奥", "played": 38, "won": 18, "drawn": 7, "lost": 13, "gf": 49, "ga": 39, "gd": 10, "points": 61, "note": "欧联正赛" },
                { "position": 8, "team_name": "佛罗伦萨", "played": 38, "won": 17, "drawn": 9, "lost": 12, "gf": 61, "ga": 46, "gd": 15, "points": 60, "note": "欧协联附加赛" },
                { "position": 9, "team_name": "都灵", "played": 38, "won": 13, "drawn": 14, "lost": 11, "gf": 36, "ga": 36, "gd": 0, "points": 53 },
                { "position": 10, "team_name": "那不勒斯", "played": 38, "won": 13, "drawn": 14, "lost": 11, "gf": 55, "ga": 48, "gd": 7, "points": 53 },
                { "position": 11, "team_name": "热那亚", "played": 38, "won": 12, "drawn": 13, "lost": 13, "gf": 45, "ga": 45, "gd": 0, "points": 49 },
                { "position": 12, "team_name": "蒙扎", "played": 38, "won": 11, "drawn": 12, "lost": 15, "gf": 39, "ga": 51, "gd": -12, "points": 45 },
                { "position": 13, "team_name": "维罗纳", "played": 38, "won": 9, "drawn": 11, "lost": 18, "gf": 38, "ga": 51, "gd": -13, "points": 38 },
                { "position": 14, "team_name": "莱切", "played": 38, "won": 8, "drawn": 14, "lost": 16, "gf": 32, "ga": 54, "gd": -22, "points": 38 },
                { "position": 15, "team_name": "乌迪内斯", "played": 38, "won": 6, "drawn": 19, "lost": 13, "gf": 37, "ga": 53, "gd": -16, "points": 37 },
                { "position": 16, "team_name": "卡利亚里", "played": 38, "won": 8, "drawn": 12, "lost": 18, "gf": 42, "ga": 68, "gd": -26, "points": 36 },
                { "position": 17, "team_name": "恩波利", "played": 38, "won": 9, "drawn": 9, "lost": 20, "gf": 29, "ga": 54, "gd": -25, "points": 36 },
                { "position": 18, "team_name": "弗罗西诺内", "played": 38, "won": 8, "drawn": 11, "lost": 19, "gf": 44, "ga": 69, "gd": -25, "points": 35, "note": "降入意乙" },
                { "position": 19, "team_name": "萨索洛", "played": 38, "won": 7, "drawn": 9, "lost": 22, "gf": 43, "ga": 75, "gd": -32, "points": 30, "note": "降入意乙" },
                { "position": 20, "team_name": "萨勒尼塔纳", "played": 38, "won": 2, "drawn": 11, "lost": 25, "gf": 32, "ga": 81, "gd": -49, "points": 17, "note": "降入意乙" }
            ],
            "scorers": [
                { "rank": 1, "player": "劳塔罗·马丁内斯", "team": "国际米兰", "goals": 24, "penalties": 2, "matches": 33 },
                { "rank": 2, "player": "弗拉霍维奇", "team": "尤文图斯", "goals": 16, "penalties": 2, "matches": 33 },
                { "rank": 3, "player": "奥斯梅恩", "team": "那不勒斯", "goals": 15, "penalties": 3, "matches": 25 },
                { "rank": 4, "player": "吉鲁", "team": "AC米兰", "goals": 15, "penalties": 4, "matches": 35 },
                { "rank": 5, "player": "古德蒙德森", "team": "热那亚", "goals": 14, "penalties": 4, "matches": 35 }
            ],
            "assists": [
                { "rank": 1, "player": "迪巴拉", "team": "罗马", "assists": 9, "matches": 28 },
                { "rank": 2, "player": "莱奥", "team": "AC米兰", "assists": 9, "matches": 34 },
                { "rank": 3, "player": "姆希塔良", "team": "国际米兰", "assists": 8, "matches": 36 }
            ],
            "transfers": [
                { "date": "2026-07-12", "type": "官宣", "player": "齐尔克泽", "from": "博洛尼亚", "to": "曼彻斯特联", "fee": "转会费 4250万欧" },
                { "date": "2026-07-06", "type": "官宣", "player": "道格拉斯·路易斯", "from": "阿斯顿维拉", "to": "尤文图斯", "fee": "转会费 5150万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 7. 德国足球甲级联赛 (德甲, 18 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "bundesliga",
            "name": "德国足球甲级联赛 (德甲)",
            "label": "德甲",
            "short_name": "德甲",
            "flag_icon": "circle-flags:de",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "第 34 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "勒沃库森", "played": 34, "won": 28, "drawn": 6, "lost": 0, "gf": 89, "ga": 24, "gd": 65, "points": 90, "note": "不败夺冠 · 欧冠正赛" },
                { "position": 2, "team_name": "斯图加特", "played": 34, "won": 23, "drawn": 4, "lost": 7, "gf": 78, "ga": 39, "gd": 39, "points": 73, "note": "欧冠正赛" },
                { "position": 3, "team_name": "拜仁慕尼黑", "played": 34, "won": 23, "drawn": 3, "lost": 8, "gf": 94, "ga": 45, "gd": 49, "points": 72, "note": "欧冠正赛" },
                { "position": 4, "team_name": "莱比锡RB", "played": 34, "won": 19, "drawn": 8, "lost": 7, "gf": 77, "ga": 39, "gd": 38, "points": 65, "note": "欧冠正赛" },
                { "position": 5, "team_name": "多特蒙德", "played": 34, "won": 18, "drawn": 9, "lost": 7, "gf": 68, "ga": 43, "gd": 25, "points": 63, "note": "欧冠正赛 (德甲欧战红利)" },
                { "position": 6, "team_name": "法兰克福", "played": 34, "won": 11, "drawn": 14, "lost": 9, "gf": 51, "ga": 50, "gd": 1, "points": 47, "note": "欧联正赛" },
                { "position": 7, "team_name": "霍芬海姆", "played": 34, "won": 13, "drawn": 7, "lost": 14, "gf": 66, "ga": 66, "gd": 0, "points": 46, "note": "欧联正赛" },
                { "position": 8, "team_name": "海登海姆", "played": 34, "won": 10, "drawn": 12, "lost": 12, "gf": 50, "ga": 55, "gd": -5, "points": 42, "note": "欧协联附加赛" },
                { "position": 9, "team_name": "云达不莱梅", "played": 34, "won": 11, "drawn": 9, "lost": 14, "gf": 48, "ga": 54, "gd": -6, "points": 42 },
                { "position": 10, "team_name": "弗赖堡", "played": 34, "won": 11, "drawn": 9, "lost": 14, "gf": 45, "ga": 58, "gd": -13, "points": 42 },
                { "position": 11, "team_name": "奥格斯堡", "played": 34, "won": 10, "drawn": 9, "lost": 15, "gf": 50, "ga": 60, "gd": -10, "points": 39 },
                { "position": 12, "team_name": "沃尔夫斯堡", "played": 34, "won": 10, "drawn": 7, "lost": 17, "gf": 41, "ga": 56, "gd": -15, "points": 37 },
                { "position": 13, "team_name": "美因茨", "played": 34, "won": 7, "drawn": 14, "lost": 13, "gf": 39, "ga": 51, "gd": -12, "points": 35 },
                { "position": 14, "team_name": "门兴格拉德巴赫", "played": 34, "won": 7, "drawn": 13, "lost": 14, "gf": 56, "ga": 67, "gd": -11, "points": 34 },
                { "position": 15, "team_name": "柏林联合", "played": 34, "won": 9, "drawn": 6, "lost": 19, "gf": 33, "ga": 58, "gd": -25, "points": 33 },
                { "position": 16, "team_name": "波鸿", "played": 34, "won": 7, "drawn": 12, "lost": 15, "gf": 42, "ga": 74, "gd": -32, "points": 33, "note": "保级附加赛 (保级成功)" },
                { "position": 17, "team_name": "科隆", "played": 34, "won": 5, "drawn": 12, "lost": 17, "gf": 28, "ga": 60, "gd": -32, "points": 27, "note": "降入德乙" },
                { "position": 18, "team_name": "达姆施塔特", "played": 34, "won": 3, "drawn": 8, "lost": 23, "gf": 30, "ga": 86, "gd": -56, "points": 17, "note": "降入德乙" }
            ],
            "scorers": [
                { "rank": 1, "player": "哈里·凯恩", "team": "拜仁慕尼黑", "goals": 36, "penalties": 5, "matches": 32 },
                { "rank": 2, "player": "塞尔胡·吉拉西", "team": "斯图加特", "goals": 28, "penalties": 4, "matches": 28 },
                { "rank": 3, "player": "路易斯·奥蓬达", "team": "莱比锡RB", "goals": 24, "penalties": 2, "matches": 34 },
                { "rank": 4, "player": "德尼兹·翁达夫", "team": "斯图加特", "goals": 18, "penalties": 0, "matches": 30 }
            ],
            "assists": [
                { "rank": 1, "player": "弗林蓬", "team": "勒沃库森", "assists": 9, "matches": 31 },
                { "rank": 2, "player": "维尔茨", "team": "勒沃库森", "assists": 11, "matches": 32 },
                { "rank": 3, "player": "格里马尔多", "team": "勒沃库森", "assists": 13, "matches": 33 }
            ],
            "transfers": [
                { "date": "2026-07-16", "type": "官宣", "player": "吉拉西", "from": "斯图加特", "to": "多特蒙德", "fee": "转会费 1800万欧" },
                { "date": "2026-07-04", "type": "官宣", "player": "帕利尼亚", "from": "富勒姆", "to": "拜仁慕尼黑", "fee": "转会费 5100万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 8. 法国足球甲级联赛 (法甲, 18 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "ligue1",
            "name": "法国足球甲级联赛 (法甲)",
            "label": "法甲",
            "short_name": "法甲",
            "flag_icon": "circle-flags:fr",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "第 34 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "巴黎圣日耳曼", "played": 34, "won": 22, "drawn": 10, "lost": 2, "gf": 81, "ga": 33, "gd": 48, "points": 76, "note": "法甲冠军 · 欧冠正赛" },
                { "position": 2, "team_name": "摩纳哥", "played": 34, "won": 20, "drawn": 7, "lost": 7, "gf": 68, "ga": 42, "gd": 26, "points": 67, "note": "欧冠正赛" },
                { "position": 3, "team_name": "布雷斯特", "played": 34, "won": 17, "drawn": 10, "lost": 7, "gf": 53, "ga": 34, "gd": 19, "points": 61, "note": "欧冠正赛" },
                { "position": 4, "team_name": "里尔", "played": 34, "won": 16, "drawn": 11, "lost": 7, "gf": 52, "ga": 34, "gd": 18, "points": 59, "note": "欧冠资格赛" },
                { "position": 5, "team_name": "尼斯", "played": 34, "won": 15, "drawn": 10, "lost": 9, "gf": 40, "ga": 29, "gd": 11, "points": 55, "note": "欧联正赛" },
                { "position": 6, "team_name": "里昂", "played": 34, "won": 16, "drawn": 5, "lost": 13, "gf": 61, "ga": 55, "gd": 6, "points": 53, "note": "欧联正赛" },
                { "position": 7, "team_name": "朗斯", "played": 34, "won": 15, "drawn": 6, "lost": 13, "gf": 45, "ga": 37, "gd": 8, "points": 51, "note": "欧协联附加赛" },
                { "position": 8, "team_name": "马赛", "played": 34, "won": 13, "drawn": 11, "lost": 10, "gf": 52, "ga": 41, "gd": 11, "points": 50 },
                { "position": 9, "team_name": "兰斯", "played": 34, "won": 13, "drawn": 8, "lost": 13, "gf": 42, "ga": 47, "gd": -5, "points": 47 },
                { "position": 10, "team_name": "雷恩", "played": 34, "won": 12, "drawn": 10, "lost": 12, "gf": 53, "ga": 46, "gd": 7, "points": 46 },
                { "position": 11, "team_name": "图卢兹", "played": 34, "won": 11, "drawn": 10, "lost": 13, "gf": 42, "ga": 46, "gd": -4, "points": 43 },
                { "position": 12, "team_name": "蒙彼利埃", "played": 34, "won": 10, "drawn": 12, "lost": 12, "gf": 43, "ga": 48, "gd": -5, "points": 41, "deduction": 1, "note": "烟花事件扣除1分" },
                { "position": 13, "team_name": "斯特拉斯堡", "played": 34, "won": 10, "drawn": 9, "lost": 15, "gf": 38, "ga": 50, "gd": -12, "points": 39 },
                { "position": 14, "team_name": "南特", "played": 34, "won": 9, "drawn": 6, "lost": 19, "gf": 30, "ga": 55, "gd": -25, "points": 33 },
                { "position": 15, "team_name": "勒阿弗尔", "played": 34, "won": 7, "drawn": 11, "lost": 16, "gf": 34, "ga": 45, "gd": -11, "points": 32 },
                { "position": 16, "team_name": "梅斯", "played": 34, "won": 8, "drawn": 5, "lost": 21, "gf": 35, "ga": 58, "gd": -23, "points": 29, "note": "保级附加赛 (降级)" },
                { "position": 17, "team_name": "洛里昂", "played": 34, "won": 7, "drawn": 8, "lost": 19, "gf": 43, "ga": 66, "gd": -23, "points": 29, "note": "降入法乙" },
                { "position": 18, "team_name": "克莱蒙", "played": 34, "won": 5, "drawn": 10, "lost": 19, "gf": 26, "ga": 60, "gd": -34, "points": 25, "note": "降入法乙" }
            ],
            "scorers": [
                { "rank": 1, "player": "基利安·姆巴佩", "team": "巴黎圣日耳曼", "goals": 27, "penalties": 6, "matches": 29 },
                { "rank": 2, "player": "乔纳森·戴维", "team": "里尔", "goals": 19, "penalties": 2, "matches": 34 },
                { "rank": 3, "player": "拉卡泽特", "team": "里昂", "goals": 19, "penalties": 2, "matches": 29 },
                { "rank": 4, "player": "奥巴梅扬", "team": "马赛", "goals": 17, "penalties": 4, "matches": 34 }
            ],
            "assists": [
                { "rank": 1, "player": "登贝莱", "team": "巴黎圣日耳曼", "assists": 8, "matches": 26 },
                { "rank": 2, "player": "戈洛温", "team": "摩纳哥", "assists": 6, "matches": 25 }
            ],
            "transfers": [
                { "date": "2026-07-22", "type": "官宣", "player": "若昂·内维斯", "from": "本菲卡", "to": "巴黎圣日耳曼", "fee": "转会费 6000万欧" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 9. 中国足球协会超级联赛 (中超, 16 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "csl",
            "name": "中国足球协会超级联赛 (中超)",
            "label": "中超",
            "short_name": "中超",
            "flag_icon": "circle-flags:cn",
            "group": "popular",
            "group_label": "欧战与顶级赛事",
            "has_live_data": True,
            "season": "2026 赛季",
            "round_info": "第 22 轮 战罢",
            "table": [
                { "position": 1, "team_name": "上海海港", "played": 22, "won": 18, "drawn": 3, "lost": 1, "gf": 72, "ga": 20, "gd": 52, "points": 57, "note": "亚冠精英联赛" },
                { "position": 2, "team_name": "上海申花", "played": 22, "won": 17, "drawn": 4, "lost": 1, "gf": 56, "ga": 14, "gd": 42, "points": 55, "note": "亚冠精英联赛" },
                { "position": 3, "team_name": "成都蓉城", "played": 22, "won": 14, "drawn": 3, "lost": 5, "gf": 49, "ga": 22, "gd": 27, "points": 45, "note": "亚冠2联赛" },
                { "position": 4, "team_name": "北京国安", "played": 22, "won": 12, "drawn": 5, "lost": 5, "gf": 45, "ga": 27, "gd": 18, "points": 41 },
                { "position": 5, "team_name": "山东泰山", "played": 22, "won": 10, "drawn": 7, "lost": 5, "gf": 40, "ga": 32, "gd": 8, "points": 37 },
                { "position": 6, "team_name": "天津津门虎", "played": 22, "won": 8, "drawn": 7, "lost": 7, "gf": 34, "ga": 31, "gd": 3, "points": 31 },
                { "position": 7, "team_name": "浙江队", "played": 22, "won": 9, "drawn": 4, "lost": 9, "gf": 39, "ga": 42, "gd": -3, "points": 31 },
                { "position": 8, "team_name": "河南队", "played": 22, "won": 7, "drawn": 7, "lost": 8, "gf": 29, "ga": 35, "gd": -6, "points": 28 },
                { "position": 9, "team_name": "武汉三镇", "played": 22, "won": 7, "drawn": 5, "lost": 10, "gf": 28, "ga": 36, "gd": -8, "points": 26 },
                { "position": 10, "team_name": "青岛西海岸", "played": 22, "won": 6, "drawn": 6, "lost": 10, "gf": 29, "ga": 43, "gd": -14, "points": 24 },
                { "position": 11, "team_name": "长春亚泰", "played": 22, "won": 5, "drawn": 7, "lost": 10, "gf": 27, "ga": 39, "gd": -12, "points": 22 },
                { "position": 12, "team_name": "沧州雄狮", "played": 22, "won": 5, "drawn": 6, "lost": 11, "gf": 24, "ga": 46, "gd": -22, "points": 21 },
                { "position": 13, "team_name": "深圳新鹏城", "played": 22, "won": 5, "drawn": 6, "lost": 11, "gf": 21, "ga": 42, "gd": -21, "points": 21 },
                { "position": 14, "team_name": "青岛海牛", "played": 22, "won": 5, "drawn": 4, "lost": 13, "gf": 20, "ga": 39, "gd": -19, "points": 19 },
                { "position": 15, "team_name": "梅州客家", "played": 22, "won": 4, "drawn": 6, "lost": 12, "gf": 19, "ga": 38, "gd": -19, "points": 18, "note": "降级区" },
                { "position": 16, "team_name": "南通支云", "played": 22, "won": 3, "drawn": 5, "lost": 14, "gf": 23, "ga": 49, "gd": -26, "points": 14, "note": "降级区" }
            ],
            "scorers": [
                { "rank": 1, "player": "武磊", "team": "上海海港", "goals": 28, "penalties": 0, "matches": 22 },
                { "rank": 2, "player": "古斯塔沃", "team": "上海海港", "goals": 18, "penalties": 1, "matches": 20 },
                { "rank": 3, "player": "费利佩", "team": "成都蓉城", "goals": 13, "penalties": 2, "matches": 21 },
                { "rank": 4, "player": "路易斯", "team": "上海申花", "goals": 13, "penalties": 1, "matches": 21 },
                { "rank": 5, "player": "莱昂纳多", "team": "浙江队", "goals": 12, "penalties": 3, "matches": 22 }
            ],
            "assists": [
                { "rank": 1, "player": "奥斯卡", "team": "上海海港", "assists": 16, "matches": 21 },
                { "rank": 2, "player": "巴尔加斯", "team": "上海海港", "assists": 10, "matches": 22 },
                { "rank": 3, "player": "特谢拉", "team": "上海申花", "assists": 8, "matches": 19 }
            ],
            "transfers": [
                { "date": "2026-07-15", "type": "官宣", "player": "韦世豪", "from": "武汉三镇", "to": "成都蓉城", "fee": "转会费 5000万人民币" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 10. 波兰甲级联赛 (波甲, 18 队完整大名单，留洋主队奥波莱)
        # ──────────────────────────────────────────────────────────
        {
            "key": "pol_d1",
            "name": "波兰甲级联赛 (波甲)",
            "label": "波甲",
            "short_name": "波甲",
            "flag_icon": "circle-flags:pl",
            "group": "european",
            "group_label": "欧洲主要联赛",
            "has_live_data": True,
            "season": "2026/27 赛季",
            "round_info": "第 3 轮 战罢 · 奥波莱奥德拉 2胜1平保持不败跃居冲超区次席",
            "table": [
                { "position": 1, "team_name": "华沙莱吉亚", "played": 3, "won": 2, "drawn": 1, "lost": 0, "gf": 6, "ga": 1, "gd": 5, "points": 7, "note": "直接升级区" },
                { "position": 2, "team_name": "奥波莱奥德拉", "played": 3, "won": 2, "drawn": 1, "lost": 0, "gf": 7, "ga": 5, "gd": 2, "points": 7, "note": "直接升级区 · 留洋主队 🇨🇳" },
                { "position": 3, "team_name": "罗兹维泽夫", "played": 3, "won": 2, "drawn": 0, "lost": 1, "gf": 9, "ga": 7, "gd": 2, "points": 6, "note": "升级附加赛" },
                { "position": 4, "team_name": "琴斯托霍瓦", "played": 3, "won": 2, "drawn": 0, "lost": 1, "gf": 8, "ga": 7, "gd": 1, "points": 6, "note": "升级附加赛" },
                { "position": 5, "team_name": "拉多米亚克", "played": 3, "won": 2, "drawn": 0, "lost": 1, "gf": 6, "ga": 6, "gd": 0, "points": 6, "note": "升级附加赛" },
                { "position": 6, "team_name": "克拉科维亚", "played": 3, "won": 1, "drawn": 2, "lost": 0, "gf": 5, "ga": 3, "gd": 2, "points": 5, "note": "升级附加赛" },
                { "position": 7, "team_name": "乔治罗尼亚比亚韦斯托克", "played": 3, "won": 1, "drawn": 2, "lost": 0, "gf": 4, "ga": 2, "gd": 2, "points": 5 },
                { "position": 8, "team_name": "KGHM卢宾扎格列比", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 5, "ga": 2, "gd": 3, "points": 4 },
                { "position": 9, "team_name": "莫托路宾", "played": 3, "won": 1, "drawn": 1, "lost": 1, "gf": 4, "ga": 3, "gd": 1, "points": 4 },
                { "position": 10, "team_name": "维斯拉克拉科", "played": 2, "won": 1, "drawn": 1, "lost": 0, "gf": 3, "ga": 2, "gd": 1, "points": 4 },
                { "position": 11, "team_name": "GKS卡托维兹", "played": 3, "won": 1, "drawn": 0, "lost": 2, "gf": 9, "ga": 9, "gd": 0, "points": 3 },
                { "position": 12, "team_name": "华沙普洛克", "played": 2, "won": 1, "drawn": 0, "lost": 1, "gf": 5, "ga": 5, "gd": 0, "points": 3 },
                { "position": 13, "team_name": "扎布热戈尔尼克", "played": 3, "won": 0, "drawn": 3, "lost": 0, "gf": 2, "ga": 2, "gd": 0, "points": 3 },
                { "position": 14, "team_name": "维彻兹塔克拉库瓦", "played": 3, "won": 1, "drawn": 0, "lost": 2, "gf": 7, "ga": 8, "gd": -1, "points": 3 },
                { "position": 15, "team_name": "波兹南莱赫", "played": 3, "won": 1, "drawn": 0, "lost": 2, "gf": 5, "ga": 7, "gd": -2, "points": 3 },
                { "position": 16, "team_name": "罗切霍茹夫", "played": 2, "won": 0, "drawn": 0, "lost": 2, "gf": 2, "ga": 6, "gd": -4, "points": 0, "note": "降级区" },
                { "position": 17, "team_name": "莱格尼察铜业", "played": 3, "won": 0, "drawn": 0, "lost": 3, "gf": 2, "ga": 7, "gd": -5, "points": 0, "note": "降级区" },
                { "position": 18, "team_name": "弗罗茨瓦夫西里西亚", "played": 3, "won": 0, "drawn": 0, "lost": 3, "gf": 4, "ga": 11, "gd": -7, "points": 0, "note": "降级区" }
            ],
            "scorers": [
                { "rank": 1, "player": "卡克佩尔·普日比乌科 (Przybyłko)", "team": "奥波莱奥德拉", "goals": 5, "penalties": 0, "matches": 3 },
                { "rank": 2, "player": "帕特里克·西什 (Patryk Szysz)", "team": "奥波莱奥德拉", "goals": 1, "penalties": 0, "matches": 3 },
                { "rank": 3, "player": "托马斯·加伊达 (Tomasz Gajda)", "team": "奥波莱奥德拉", "goals": 1, "penalties": 0, "matches": 3 },
                { "rank": 4, "player": "巴斯克斯", "team": "GKS卡托维兹", "goals": 2, "penalties": 0, "matches": 3 }
            ],
            "assists": [
                { "rank": 1, "player": "帕特里克·西什 (Patryk Szysz)", "team": "奥波莱奥德拉", "assists": 1, "matches": 3 },
                { "rank": 2, "player": "巴巴卡尔·迪奥内 (Babacar Dione)", "team": "奥波莱奥德拉", "assists": 1, "matches": 3 },
                { "rank": 3, "player": "马特乌什·斯皮哈瓦 (Mateusz Spychała)", "team": "奥波莱奥德拉", "assists": 1, "matches": 3 },
                { "rank": 4, "player": "雅库布·什雷克 (Jakub Szrek)", "team": "奥波莱奥德拉", "assists": 1, "matches": 3 },
                { "rank": 5, "player": "皮尔伊 (Marin Pilj)", "team": "奥波莱奥德拉", "assists": 1, "matches": 3 }
            ],
            "transfers": [
                { "date": "2026-07-20", "type": "主帅签约", "player": "中国籍少帅 (耶稣·徐)", "from": "自由身", "to": "奥波莱奥德拉", "fee": "签约至2028年 · 资助考证" },
                { "date": "2026-07-15", "type": "引援", "player": "卡克佩尔·普日比乌科", "from": "自由身", "to": "奥波莱奥德拉", "fee": "免签加盟" }
            ]
        },

        # ──────────────────────────────────────────────────────────
        # 11. 比利时甲级联赛 (比甲, 16 队完整大名单)
        # ──────────────────────────────────────────────────────────
        {
            "key": "bel_d1",
            "name": "比利时甲级联赛 (比甲)",
            "label": "比甲",
            "short_name": "比甲",
            "flag_icon": "circle-flags:be",
            "group": "european",
            "group_label": "欧洲主要联赛",
            "has_live_data": True,
            "season": "2025/26 赛季",
            "round_info": "冠军附加赛收官",
            "table": [
                { "position": 1, "team_name": "皇家布鲁日", "played": 30, "won": 19, "drawn": 7, "lost": 4, "gf": 62, "ga": 29, "gd": 33, "points": 64, "note": "比甲冠军 · 欧冠正赛" },
                { "position": 2, "team_name": "圣吉罗斯联", "played": 30, "won": 18, "drawn": 8, "lost": 4, "gf": 59, "ga": 28, "gd": 31, "points": 62, "note": "欧冠资格赛" },
                { "position": 3, "team_name": "安德莱赫特", "played": 30, "won": 17, "drawn": 9, "lost": 4, "gf": 58, "ga": 30, "gd": 28, "points": 60, "note": "欧联资格赛" },
                { "position": 4, "team_name": "色格拉布鲁日", "played": 30, "won": 15, "drawn": 7, "lost": 8, "gf": 50, "ga": 34, "gd": 16, "points": 52, "note": "欧协联附加赛" },
                { "position": 5, "team_name": "皇家根克", "played": 30, "won": 14, "drawn": 9, "lost": 7, "gf": 51, "ga": 31, "gd": 20, "points": 51 },
                { "position": 6, "team_name": "皇家安特卫普", "played": 30, "won": 14, "drawn": 8, "lost": 8, "gf": 55, "ga": 27, "gd": 28, "points": 50 },
                { "position": 7, "team_name": "皇家根特", "played": 30, "won": 12, "drawn": 11, "lost": 7, "gf": 53, "ga": 38, "gd": 15, "points": 47 },
                { "position": 8, "team_name": "梅赫伦", "played": 30, "won": 13, "drawn": 6, "lost": 11, "gf": 39, "ga": 34, "gd": 5, "points": 45 },
                { "position": 9, "team_name": "圣图尔登", "played": 30, "won": 10, "drawn": 10, "lost": 10, "gf": 35, "ga": 46, "gd": -11, "points": 40 },
                { "position": 10, "team_name": "皇家标准列日", "played": 30, "won": 8, "drawn": 10, "lost": 12, "gf": 33, "ga": 41, "gd": -8, "points": 34 },
                { "position": 11, "team_name": "韦斯特洛", "played": 30, "won": 7, "drawn": 9, "lost": 14, "gf": 42, "ga": 54, "gd": -12, "points": 30 },
                { "position": 12, "team_name": "鲁汶", "played": 30, "won": 7, "drawn": 8, "lost": 15, "gf": 34, "ga": 47, "gd": -13, "points": 29 },
                { "position": 13, "team_name": "沙勒罗瓦", "played": 30, "won": 7, "drawn": 8, "lost": 15, "gf": 26, "ga": 48, "gd": -22, "points": 29 },
                { "position": 14, "team_name": "欧本", "played": 30, "won": 7, "drawn": 3, "lost": 20, "gf": 24, "ga": 58, "gd": -34, "points": 24, "note": "保级附加赛" },
                { "position": 15, "team_name": "科特赖克", "played": 30, "won": 6, "drawn": 6, "lost": 18, "gf": 22, "ga": 57, "gd": -35, "points": 24, "note": "保级附加赛" },
                { "position": 16, "team_name": "RWDM布鲁塞尔", "played": 30, "won": 5, "drawn": 8, "lost": 17, "gf": 31, "ga": 67, "gd": -36, "points": 23, "note": "降级" }
            ],
            "scorers": [
                { "rank": 1, "player": "凯文·登基", "team": "色格拉布鲁日", "goals": 27, "penalties": 3, "matches": 38 },
                { "rank": 2, "player": "古斯塔沃·普埃尔塔", "team": "皇家安特卫普", "goals": 16, "penalties": 1, "matches": 35 }
            ],
            "assists": [
                { "rank": 1, "player": "卡梅伦·普埃塔斯", "team": "圣吉罗斯联", "assists": 17, "matches": 36 }
            ],
            "transfers": [
                { "date": "2026-07-02", "type": "官宣", "player": "蒂亚戈", "from": "皇家布鲁日", "to": "布伦特福德", "fee": "转会费 3700万欧" }
            ]
        }
    ]

def get_marquee_matches():
    return [
        # UCL
        {
            "id": 2001,
            "league_key": "ucl",
            "league_name": "欧冠",
            "league_badge": "欧冠",
            "league_flag": "circle-flags:eu",
            "round": 8,
            "round_label": "温布利总决赛",
            "date": "2026-06-01 03:00",
            "date_short": "06-01 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "皇家马德里",
            "home_code": "RMA",
            "away_team": "多特蒙德",
            "away_code": "BVB",
            "score_home": 2,
            "score_away": 0,
            "stadium": "温布利大球场",
            "xg": "1.82 - 1.15",
            "shots": "13",
            "shots_on_target": "6",
            "distance_km": "112.5",
            "scorers": [
                { "minute": 74, "player": "卡瓦哈尔", "player_zh": "卡瓦哈尔", "is_header": True },
                { "minute": 83, "player": "维尼修斯", "player_zh": "维尼修斯" }
            ],
            "news": {
                "title": "欧冠决赛：卡瓦哈尔头槌破僵维尼修斯锁定胜局，皇马2-0多特夺得队史第15冠！",
                "summary": "凭借下半场角球头球破门与致命反击，皇家马德里再次登顶欧洲！",
                "reporter": "懂球云欧洲特派"
            }
        },
        # UEL
        {
            "id": 2002,
            "league_key": "uel",
            "league_name": "欧联",
            "league_badge": "欧联",
            "league_flag": "circle-flags:eu",
            "round": 8,
            "round_label": "都柏林总决赛",
            "date": "2026-05-23 03:00",
            "date_short": "05-23 周五",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "亚特兰大",
            "home_code": "ATA",
            "away_team": "勒沃库森",
            "away_code": "B04",
            "score_home": 3,
            "score_away": 0,
            "stadium": "都柏林英杰华竞技场",
            "xg": "1.65 - 0.95",
            "shots": "12",
            "shots_on_target": "7",
            "distance_km": "118.0",
            "scorers": [
                { "minute": 12, "player": "卢克曼", "player_zh": "卢克曼" },
                { "minute": 26, "player": "卢克曼", "player_zh": "卢克曼" },
                { "minute": 75, "player": "卢克曼", "player_zh": "卢克曼" }
            ],
            "news": {
                "title": "欧联决赛：卢克曼帽子戏法封神！亚特兰大3-0勒沃库森，终结药厂不败神话捧杯",
                "summary": "卢克曼上演史诗级帽子戏法，加斯佩里尼率领真蓝黑夺得队史首座欧战奖杯！",
                "reporter": "法新社"
            }
        },
        # UECL
        {
            "id": 2003,
            "league_key": "uecl",
            "league_name": "欧协联",
            "league_badge": "欧协联",
            "league_flag": "circle-flags:eu",
            "round": 6,
            "round_label": "弗罗茨瓦夫总决赛",
            "date": "2026-05-30 03:00",
            "date_short": "05-30 周六",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "奥林匹亚科斯",
            "home_code": "OLY",
            "away_team": "佛罗伦萨",
            "away_code": "FIO",
            "score_home": 1,
            "score_away": 0,
            "stadium": "雅典AEK球场",
            "xg": "1.20 - 1.10",
            "shots": "9",
            "shots_on_target": "4",
            "distance_km": "115.4",
            "scorers": [
                { "minute": 116, "player": "卡埃比", "player_zh": "卡埃比", "is_header": True }
            ],
            "news": {
                "title": "欧协联决赛：卡埃比加时116分钟头球绝杀！奥林匹亚科斯1-0佛罗伦萨夺冠",
                "summary": "希腊豪门加时赛绝杀意甲劲旅，紫百合连续两年屈居欧协联亚军。",
                "reporter": "路透社"
            }
        },
        # PL
        {
            "id": 2004,
            "league_key": "pl",
            "league_name": "英超",
            "league_badge": "英超",
            "league_flag": "circle-flags:gb-eng",
            "round": 38,
            "round_label": "第 38 轮",
            "date": "2026-05-19 23:00",
            "date_short": "05-19 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "曼彻斯特城",
            "home_code": "MCI",
            "away_team": "西汉姆联",
            "away_code": "WHU",
            "score_home": 3,
            "score_away": 1,
            "stadium": "阿提哈德球场",
            "xg": "2.80 - 0.45",
            "shots": "22",
            "shots_on_target": "9",
            "distance_km": "113.8",
            "scorers": [
                { "minute": 2, "player": "福登", "player_zh": "福登" },
                { "minute": 18, "player": "福登", "player_zh": "福登" },
                { "minute": 42, "player": "库杜斯", "player_zh": "库杜斯" },
                { "minute": 59, "player": "罗德里", "player_zh": "罗德里" }
            ],
            "news": {
                "title": "英超收官战：福登双响罗德里锁定胜局，曼城3-1西汉姆实现英超史无前例四连冠！",
                "summary": "瓜迪奥拉率领蓝月军团以91分登顶，阿森纳两分之差屈居亚军。",
                "reporter": "BBC Sport"
            }
        },
        # La Liga
        {
            "id": 2005,
            "league_key": "laliga",
            "league_name": "西甲",
            "league_badge": "西甲",
            "league_flag": "circle-flags:es",
            "round": 32,
            "round_label": "第 32 轮",
            "date": "2026-04-22 03:00",
            "date_short": "04-22 周一",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "皇家马德里",
            "home_code": "RMA",
            "away_team": "巴塞罗那",
            "away_code": "FCB",
            "score_home": 3,
            "score_away": 2,
            "stadium": "圣地亚哥·伯纳乌球场",
            "xg": "2.35 - 1.80",
            "shots": "16",
            "shots_on_target": "8",
            "distance_km": "114.6",
            "scorers": [
                { "minute": 6, "player": "克里斯滕森", "player_zh": "克里斯滕森" },
                { "minute": 18, "player": "维尼修斯", "player_zh": "维尼修斯" },
                { "minute": 69, "player": "费尔明", "player_zh": "费尔明" },
                { "minute": 73, "player": "巴斯克斯", "player_zh": "巴斯克斯" },
                { "minute": "90+1", "player": "贝林厄姆", "player_zh": "贝林厄姆" }
            ],
            "news": {
                "title": "西班牙国家德比：贝林厄姆91分钟读秒绝杀！皇马3-2逆转巴萨锁定冠军点",
                "summary": "伯纳乌上演惊心动魄德比大战，贝林厄姆后点包抄攻入绝杀，皇马将领先优势扩大至11分。",
                "reporter": "马卡报"
            }
        },
        # Serie A
        {
            "id": 2006,
            "league_key": "serie_a",
            "league_name": "意甲",
            "league_badge": "意甲",
            "league_flag": "circle-flags:it",
            "round": 33,
            "round_label": "第 33 轮",
            "date": "2026-04-23 02:45",
            "date_short": "04-23 周二",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "AC米兰",
            "home_code": "MIL",
            "away_team": "国际米兰",
            "away_code": "INT",
            "score_home": 1,
            "score_away": 2,
            "stadium": "圣西罗球场",
            "xg": "1.30 - 1.95",
            "shots": "14",
            "shots_on_target": "5",
            "distance_km": "116.1",
            "scorers": [
                { "minute": 18, "player": "阿切尔比", "player_zh": "阿切尔比", "is_header": True },
                { "minute": 49, "player": "图拉姆", "player_zh": "图拉姆" },
                { "minute": 80, "player": "托莫里", "player_zh": "托莫里" }
            ],
            "news": {
                "title": "米兰德比：国米2-1力克米兰提前5轮夺冠！队史第20座意甲锦标绣上第二颗星",
                "summary": "圣西罗球场见证蓝黑军团历史时刻，小因扎吉率队加冕意甲冠军！",
                "reporter": "米兰体育报"
            }
        },
        # Bundesliga
        {
            "id": 2007,
            "league_key": "bundesliga",
            "league_name": "德甲",
            "league_badge": "德甲",
            "league_flag": "circle-flags:de",
            "round": 29,
            "round_label": "第 29 轮",
            "date": "2026-04-14 23:30",
            "date_short": "04-14 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "勒沃库森",
            "home_code": "B04",
            "away_team": "云达不莱梅",
            "away_code": "SVW",
            "score_home": 5,
            "score_away": 0,
            "stadium": "拜耳竞技场",
            "xg": "3.40 - 0.25",
            "shots": "24",
            "shots_on_target": "11",
            "distance_km": "115.0",
            "scorers": [
                { "minute": 25, "player": "博尼法斯", "player_zh": "博尼法斯" },
                { "minute": 60, "player": "扎卡", "player_zh": "扎卡" },
                { "minute": 68, "player": "维尔茨", "player_zh": "维尔茨" },
                { "minute": 83, "player": "维尔茨", "player_zh": "维尔茨" },
                { "minute": 90, "player": "维尔茨", "player_zh": "维尔茨" }
            ],
            "news": {
                "title": "勒沃库森5-0大胜不莱梅！队史120年首夺德甲冠军，维尔茨替补戴帽引爆拜耳竞技场",
                "summary": "阿隆索创造历史，勒沃库森提前5轮锁定德甲冠军，球迷涌入草皮狂欢！",
                "reporter": "图片报"
            }
        },
        # Ligue 1
        {
            "id": 2008,
            "league_key": "ligue1",
            "league_name": "法甲",
            "league_badge": "法甲",
            "league_flag": "circle-flags:fr",
            "round": 27,
            "round_label": "第 27 轮",
            "date": "2026-04-01 02:45",
            "date_short": "04-01 周一",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "马赛",
            "home_code": "OM",
            "away_team": "巴黎圣日耳曼",
            "away_code": "PSG",
            "score_home": 0,
            "score_away": 2,
            "stadium": "韦洛德罗姆球场",
            "xg": "1.10 - 1.85",
            "shots": "15",
            "shots_on_target": "4",
            "distance_km": "113.2",
            "scorers": [
                { "minute": 53, "player": "维蒂尼亚", "player_zh": "维蒂尼亚" },
                { "minute": 85, "player": "贡萨洛·拉莫斯", "player_zh": "拉莫斯" }
            ],
            "news": {
                "title": "法国国家德比：十人巴黎客场2-0力克马赛，维蒂尼亚拉莫斯破门锁定胜局",
                "summary": "贝拉尔多上半场染红，十人巴黎反击犀利连下两城攻克韦洛德罗姆。",
                "reporter": "队报"
            }
        },
        # CSL
        {
            "id": 2009,
            "league_key": "csl",
            "league_name": "中超",
            "league_badge": "中超",
            "league_flag": "circle-flags:cn",
            "round": 22,
            "round_label": "第 22 轮",
            "date": "2026-08-17 19:35",
            "date_short": "08-17 周一",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "上海申花",
            "home_code": "SHS",
            "away_team": "上海海港",
            "away_code": "SHP",
            "score_home": 3,
            "score_away": 1,
            "stadium": "上海体育场",
            "xg": "2.10 - 1.45",
            "shots": "15",
            "shots_on_target": "6",
            "distance_km": "117.2",
            "scorers": [
                { "minute": 12, "player": "王燊超", "player_zh": "王燊超" },
                { "minute": 79, "player": "于汉超", "player_zh": "于汉超" },
                { "minute": 82, "player": "路易斯", "player_zh": "路易斯" },
                { "minute": "90+5", "player": "路易斯", "player_zh": "路易斯" }
            ],
            "news": {
                "title": "上海德比惊天逆转！于汉超传射，申花3-1力破海港不败金身",
                "summary": "上海体育场见证激情德比战，申花在最后15分钟连入三球完成绝地大反击！",
                "reporter": "体坛周报"
            }
        },
        # Bel D1
        {
            "id": 2010,
            "league_key": "bel_d1",
            "league_name": "比甲",
            "league_badge": "比甲",
            "league_flag": "circle-flags:be",
            "round": 30,
            "round_label": "附加赛第 10 轮",
            "date": "2026-05-26 20:30",
            "date_short": "05-26 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": False,
            "home_team": "皇家布鲁日",
            "home_code": "CLU",
            "away_team": "色格拉布鲁日",
            "away_code": "CER",
            "score_home": 0,
            "score_away": 0,
            "stadium": "扬·布雷德尔球场",
            "xg": "1.45 - 0.85",
            "shots": "14",
            "shots_on_target": "4",
            "distance_km": "112.0",
            "scorers": [],
            "news": {
                "title": "布鲁日德比战平！皇家布鲁日力压圣吉罗斯夺得2025/26赛季比甲联赛冠军",
                "summary": "布鲁日凭借附加赛净胜球优势成功加冕比甲联赛冠军，锁定下赛季欧冠正赛资格。",
                "reporter": "晚报 (Le Soir)"
            }
        },
        # 波甲 Round 1 (真实 FM24 存档)
        {
            "id": 1001,
            "league_key": "pol_d1",
            "league_name": "波甲",
            "league_badge": "波甲",
            "league_flag": "circle-flags:pl",
            "round": 1,
            "round_label": "第 1 轮",
            "date": "2026-07-19 20:00",
            "date_short": "07-19 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": True,
            "home_team": "克拉科维亚",
            "home_code": "CRA",
            "away_team": "奥波莱奥德拉",
            "away_code": "ODR",
            "score_home": 1,
            "score_away": 1,
            "stadium": "克拉科夫约瑟夫·皮尔苏斯基球场",
            "xg": "1.35 - 1.20",
            "shots": "12",
            "shots_on_target": "5",
            "distance_km": "114.2",
            "scorers": [
                { "minute": 28, "player": "卡利曼 (Kallman)", "player_zh": "卡利曼" },
                { "minute": 62, "player": "卡克佩尔·普日比乌科 (Przybyłko)", "player_zh": "卡克佩尔", "assist": "皮尔伊 (Pilj)", "assist_zh": "皮尔伊" }
            ],
            "news": {
                "title": "波甲首轮客场逼平强敌！卡克佩尔推射建功，奥波莱奥德拉1-1客平克拉科维亚",
                "summary": "中国新帅迎来波兰正式比赛首秀，客场面对劲旅克拉科维亚下半场顽强扳平比分，斩获新赛季第一分！",
                "reporter": "懂球云波兰特派"
            }
        },
        # 波甲 Round 2 (真实 FM24 存档)
        {
            "id": 1002,
            "league_key": "pol_d1",
            "league_name": "波甲",
            "league_badge": "波甲",
            "league_flag": "circle-flags:pl",
            "round": 2,
            "round_label": "第 2 轮",
            "date": "2026-07-26 20:00",
            "date_short": "07-26 周日",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": True,
            "home_team": "奥波莱奥德拉",
            "home_code": "ODR",
            "away_team": "GKS卡托维兹",
            "away_code": "KAT",
            "score_home": 3,
            "score_away": 2,
            "stadium": "奥波莱市政球场",
            "xg": "2.40 - 1.65",
            "shots": "17",
            "shots_on_target": "8",
            "distance_km": "116.8",
            "scorers": [
                { "minute": 18, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "帕特里克·西什", "assist_zh": "西什" },
                { "minute": 39, "player": "贝格尔", "player_zh": "贝格尔" },
                { "minute": 55, "player": "罗加拉", "player_zh": "罗加拉" },
                { "minute": 71, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "克里斯蒂安·帕拉茨", "assist_zh": "帕拉茨", "is_header": True },
                { "minute": 84, "player": "帕特里克·西什", "player_zh": "西什" }
            ],
            "news": {
                "title": "奥波莱3-2险胜卡托维兹夺主场首胜！卡克佩尔双响，西什传射定胜局",
                "summary": "新帅主场首秀打出经典进攻战，卡克佩尔梅开二度，西什84分钟致命击杀全取三分！",
                "reporter": "懂球云波兰特派"
            }
        },
        # 波甲 Round 3 (真实 FM24 存档)
        {
            "id": 1003,
            "league_key": "pol_d1",
            "league_name": "波甲",
            "league_badge": "波甲",
            "league_flag": "circle-flags:pl",
            "round": 3,
            "round_label": "第 3 轮",
            "date": "2026-08-01 20:00",
            "date_short": "08-01 周六",
            "status": "FT",
            "status_label": "完赛",
            "is_overseas": True,
            "home_team": "维彻兹塔克拉库瓦",
            "home_code": "WIE",
            "away_team": "奥波莱奥德拉",
            "away_code": "ODR",
            "score_home": 2,
            "score_away": 3,
            "stadium": "克拉科夫市政球场",
            "xg": "1.75 - 2.10",
            "shots": "13",
            "shots_on_target": "7",
            "distance_km": "115.3",
            "scorers": [
                { "minute": 14, "player": "科比亚克", "player_zh": "科比亚克" },
                { "minute": 34, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "巴巴卡尔·迪奥内", "assist_zh": "迪奥内" },
                { "minute": 56, "player": "托马斯·加伊达", "player_zh": "加伊达", "assist": "马特乌什·斯皮哈瓦", "assist_zh": "斯皮哈瓦" },
                { "minute": 69, "player": "米斯利维茨", "player_zh": "米斯利维茨" },
                { "minute": 87, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "雅库布·什雷克", "assist_zh": "什雷克", "is_header": True, "is_stoppage": True }
            ],
            "news": {
                "title": "3场5球狂飙！奥波莱客场3-2绝杀维彻兹塔两连胜，中国少帅率队跃居波甲次席",
                "summary": "凭借卡克佩尔87分钟头球绝杀上演背靠背双响，奥波莱奥德拉3轮2胜1平保持不败，冲进波甲直接升级区次席！",
                "reporter": "体坛周报驻欧特派"
            }
        }
    ]

def build():
    leagues = get_complete_leagues()

    # Validate mathematical consistency for each table
    print("--- 校验数学自洽性与完整名单 ---")
    for lg in leagues:
        teams = lg["table"]
        print(f"[{lg['name']}] 球队总数: {len(teams)} 支")
        for t in teams:
            calc_pts = t["won"] * 3 + t["drawn"] - t.get("deduction", 0)
            calc_gd = t["gf"] - t["ga"]
            calc_pl = t["won"] + t["drawn"] + t["lost"]
            assert calc_pts == t["points"], f"Points mismatch in {lg['key']} for {t['team_name']}: {calc_pts} vs {t['points']}"
            assert calc_gd == t["gd"], f"GD mismatch in {lg['key']} for {t['team_name']}: {calc_gd} vs {t['gd']}"
            assert calc_pl == t["played"], f"Played mismatch in {lg['key']} for {t['team_name']}: {calc_pl} vs {t['played']}"

    output_payload = { "leagues": leagues }
    standings_path = DATA_DIR / "standings_multi.json"
    with open(standings_path, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"成功写入: {standings_path}")

    # Now update all_matches.json to include overseas matches + all marquee matches
    # Load existing all_matches.json to preserve Odra Opole / historical overseas matches
    all_matches_path = DATA_DIR / "all_matches.json"
    existing_matches = []
    if all_matches_path.exists():
        with open(all_matches_path, "r", encoding="utf-8") as f:
            existing_matches = json.load(f)

    # 严格过滤：彻底移除任何旧比乙 (bel_d2) 比赛记录，仅保留当前活跃波甲 (pol_d1)
    overseas_matches = [
        m for m in existing_matches
        if m.get("league_key") == "pol_d1"
    ]

    marquees = [m for m in get_marquee_matches() if m.get("league_key") != "bel_d2"]
    marquee_ids = {m["id"] for m in marquees}

    combined = marquees + [m for m in overseas_matches if m["id"] not in marquee_ids]
    with open(all_matches_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"成功写入比赛库 (共 {len(combined)} 场): {all_matches_path}")

if __name__ == "__main__":
    build()
