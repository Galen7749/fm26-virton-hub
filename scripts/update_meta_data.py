import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

# 1. STANDINGS UPDATE
standings_path = DATA_DIR / "standings.json"
standings = json.loads(standings_path.read_text(encoding="utf-8"))

# Exact table after Round 8 from the FM save:
bel_d2_table = [
    {"position": 1, "team_name": "皇家马斯梅赫伦", "played": 8, "won": 6, "drawn": 1, "lost": 1, "gf": 13, "ga": 5, "gd": 8, "points": 19, "is_my_team": False},
    {"position": 2, "team_name": "皇家比尔肖特安特卫普", "played": 9, "won": 5, "drawn": 3, "lost": 1, "gf": 13, "ga": 8, "gd": 5, "points": 18, "is_my_team": False},
    {"position": 3, "team_name": "皇家洛克伦滕瑟", "played": 8, "won": 4, "drawn": 4, "lost": 0, "gf": 8, "ga": 3, "gd": 5, "points": 16, "is_my_team": False},
    {"position": 4, "team_name": "维尔通精英", "played": 8, "won": 4, "drawn": 3, "lost": 1, "gf": 16, "ga": 11, "gd": 5, "points": 15, "is_my_team": True},
    {"position": 5, "team_name": "皇家法兰波垒斯", "played": 9, "won": 4, "drawn": 2, "lost": 3, "gf": 13, "ga": 11, "gd": 2, "points": 14, "is_my_team": False},
    {"position": 6, "team_name": "皇家利尔斯", "played": 8, "won": 3, "drawn": 4, "lost": 1, "gf": 10, "ga": 6, "gd": 4, "points": 13, "is_my_team": False},
    {"position": 7, "team_name": "皇家欧本", "played": 7, "won": 4, "drawn": 1, "lost": 2, "gf": 11, "ga": 8, "gd": 3, "points": 13, "is_my_team": False},
    {"position": 8, "team_name": "登德", "played": 9, "won": 3, "drawn": 4, "lost": 2, "gf": 8, "ga": 8, "gd": 0, "points": 13, "is_my_team": False},
    {"position": 9, "team_name": "布鲁日青年", "played": 9, "won": 3, "drawn": 2, "lost": 4, "gf": 10, "ga": 10, "gd": 0, "points": 11, "is_my_team": False},
    {"position": 10, "team_name": "皇家列日", "played": 8, "won": 3, "drawn": 1, "lost": 4, "gf": 7, "ga": 12, "gd": -5, "points": 10, "is_my_team": False},
    {"position": 11, "team_name": "哈瑟尔特", "played": 8, "won": 2, "drawn": 2, "lost": 4, "gf": 7, "ga": 9, "gd": -2, "points": 8, "is_my_team": False},
    {"position": 12, "team_name": "皇家安德莱赫特未来", "played": 8, "won": 2, "drawn": 1, "lost": 5, "gf": 6, "ga": 9, "gd": -3, "points": 7, "is_my_team": False},
    {"position": 13, "team_name": "皇家瑟兰", "played": 8, "won": 1, "drawn": 2, "lost": 5, "gf": 7, "ga": 12, "gd": -5, "points": 5, "is_my_team": False},
    {"position": 14, "team_name": "根特青年", "played": 9, "won": 1, "drawn": 2, "lost": 6, "gf": 10, "ga": 17, "gd": -7, "points": 5, "is_my_team": False},
    {"position": 15, "team_name": "KRC亨克青年队", "played": 8, "won": 0, "drawn": 2, "lost": 6, "gf": 4, "ga": 14, "gd": -10, "points": 2, "is_my_team": False}
]

for lg in standings.get("leagues", []):
    if lg["id"] == "bel_d2":
        lg["table"] = bel_d2_table
        lg["round"] = 8

standings_path.write_text(json.dumps(standings, ensure_ascii=False, indent=2), encoding="utf-8")
print("1. Standings updated.")

# 2. LEADERBOARDS UPDATE
leaderboards = {
    "scorers": [
        {"rank": 1, "player_zh": "卢卡斯·斯泰宁格", "player_en": "Lucas Stassin", "team": "皇家法兰波垒斯", "team_short": "法兰波垒斯", "goals": 6, "penalties": 2, "matches": 9, "shots": 22, "is_virton": False},
        {"rank": 2, "player_zh": "阿卜杜勒萨马迪·哈切姆", "player_en": "Abdelsamad Hachem", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 5, "penalties": 0, "matches": 7, "shots": 13, "is_virton": True},
        {"rank": 3, "player_zh": "托马斯·范博梅尔", "player_en": "Thomas Van Bommel", "team": "布鲁日青年足球俱乐部", "team_short": "布鲁日青年", "goals": 4, "penalties": 0, "matches": 9, "shots": 16, "is_virton": False},
        {"rank": 4, "player_zh": "尤纳斯·塞德尔", "player_en": "Jonas Seydoux", "team": "皇家比尔肖特安特卫普", "team_short": "比尔肖特", "goals": 4, "penalties": 1, "matches": 9, "shots": 15, "is_virton": False},
        {"rank": 5, "player_zh": "保罗·韦德", "player_en": "Paul Wade", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 3, "penalties": 0, "matches": 8, "shots": 15, "is_virton": True},
        {"rank": 6, "player_zh": "卢卡·迈奥拉诺", "player_en": "Luca Maiorano", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 3, "penalties": 0, "matches": 8, "shots": 20, "is_virton": True},
        {"rank": 7, "player_zh": "泰伦·托明", "player_en": "Tyrone Tormin", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 2, "penalties": 0, "matches": 8, "shots": 15, "is_virton": True},
        {"rank": 8, "player_zh": "阿卢·登贝莱", "player_en": "Aliou Dembélé", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 2, "penalties": 0, "matches": 8, "shots": 10, "is_virton": True},
        {"rank": 9, "player_zh": "朴昇秀", "player_en": "Park Seung-Soo", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 1, "penalties": 0, "matches": 3, "shots": 4, "is_virton": True},
        {"rank": 10, "player_zh": "吉永梦希", "player_en": "Yumeki Yoshinaga", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "goals": 1, "penalties": 0, "matches": 5, "shots": 4, "is_virton": True}
    ],
    "assists": [
        {"rank": 1, "player_zh": "泰伦·托明", "player_en": "Tyrone Tormin", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 4, "key_passes": 17, "matches": 8, "is_virton": True},
        {"rank": 2, "player_zh": "保罗·韦德", "player_en": "Paul Wade", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 3, "key_passes": 16, "matches": 8, "is_virton": True},
        {"rank": 3, "player_zh": "马丁·德尔瓦尔", "player_en": "Martin Delvalle", "team": "皇家马斯梅赫伦", "team_short": "马斯梅赫伦", "assists": 3, "key_passes": 14, "matches": 8, "is_virton": False},
        {"rank": 4, "player_zh": "卢卡·迈奥拉诺", "player_en": "Luca Maiorano", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 2, "key_passes": 16, "matches": 8, "is_virton": True},
        {"rank": 5, "player_zh": "马克斯·因查德", "player_en": "Marks Inchaud", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 2, "key_passes": 6, "matches": 7, "is_virton": True},
        {"rank": 6, "player_zh": "朴昇秀", "player_en": "Park Seung-Soo", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 1, "key_passes": 3, "matches": 3, "is_virton": True},
        {"rank": 7, "player_zh": "斯蒂文·阿森盖", "player_en": "Steeven Assengue", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 1, "key_passes": 7, "matches": 8, "is_virton": True},
        {"rank": 8, "player_zh": "亚当穆斯·迪奥普", "player_en": "Adama Diop", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "assists": 1, "key_passes": 11, "matches": 6, "is_virton": True}
    ],
    "discipline": [
        {"rank": 1, "player_zh": "扬·范德海登", "player_en": "Jan Van der Heyden", "team": "登德足球俱乐部", "team_short": "登德", "yellow": 4, "red": 1, "suspension_warning": "已停赛生效", "is_virton": False},
        {"rank": 2, "player_zh": "斯蒂文·阿森盖", "player_en": "Steeven Assengue", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "yellow": 2, "red": 0, "suspension_warning": "离停赛差3张", "is_virton": True},
        {"rank": 3, "player_zh": "泰迪·梅扎古", "player_en": "Teddy Mezague", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "yellow": 2, "red": 0, "suspension_warning": "离停赛差3张", "is_virton": True},
        {"rank": 4, "player_zh": "阿兰·特查普切特", "player_en": "Allan Tchaptchet", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "yellow": 1, "red": 0, "suspension_warning": "正常", "is_virton": True},
        {"rank": 5, "player_zh": "卢卡·迈奥拉诺", "player_en": "Luca Maiorano", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "yellow": 1, "red": 0, "suspension_warning": "正常", "is_virton": True},
        {"rank": 6, "player_zh": "亚当穆斯·迪奥普", "player_en": "Adama Diop", "team": "维尔通精英足球俱乐部", "team_short": "维尔通精英", "yellow": 1, "red": 0, "suspension_warning": "正常", "is_virton": True}
    ]
}

(DATA_DIR / "leaderboards.json").write_text(json.dumps(leaderboards, ensure_ascii=False, indent=2), encoding="utf-8")
print("2. Leaderboards updated.")

# 3. TEAM ANALYSIS UPDATE
analysis = {
    "tactical_overview": {
        "formation": "4-2-3-1 (高位反抢 Gegenpressing)",
        "mentality": "极快节奏 / 强力压迫 / 快速两翼纵深渗透",
        "philosophy": "徐指导带队8轮狂轰16球，以场均2球冠绝比乙联赛。战术核心在于前场就地反抢，并在右路依靠托明的个人突击与韦德的支点做球，结合边锋哈切姆的高效内切吃饼，形成恐怖的快速立体打击。同时杯赛客场6-4更印证了球队大开大合的极致攻势足球。",
        "head_coach": "耶稣 徐 (无执照但拥有战术奇才美誉)",
        "record": "8场 4胜3平1负 积15分 (联赛第4，冲甲区)"
    },
    "attack_channels": {
        "left": 29,
        "center": 28,
        "right": 43,
        "key_corridor": "右路托明走廊 + 朴昇秀内切 (占比 43%)"
    },
    "core_metrics": [
        {"name": "全场进攻火力", "team_val": 98, "league_avg": 70, "unit": "分 (联赛第1, 场均2.0球)"},
        {"name": "高位逼抢强度", "team_val": 92, "league_avg": 68, "unit": "分 (前场压迫抢断率)"},
        {"name": "右路爆点突击", "team_val": 95, "league_avg": 65, "unit": "分 (托明4次助攻全联盟领跑)"},
        {"name": "前场终结效率", "team_val": 88, "league_avg": 72, "unit": "分 (哈切姆7战5球)"},
        {"name": "防线体能抗压", "team_val": 65, "league_avg": 76, "unit": "分 (大开大合，丢11球偏高)"},
        {"name": "阵容轮换深度", "team_val": 72, "league_avg": 75, "unit": "分 (中日韩东亚外援注入活力)"}
    ],
    "strengths": [
        "比乙最狂暴进攻火网：8轮狂轰16球，两翼齐飞与中路跟进形成潮水般攻势",
        "右路助攻王托明：全联盟第一的助攻（4次）与关键传球（17次），边路一对一无人能挡",
        "哈切姆化身高效杀手：联赛5球+杯赛2球共轰7球，跑位鬼魅门前嗅觉极其敏锐",
        "东亚引援眼光独到：韩国小将朴昇秀客场斩获关键进球，日本飞翼吉永梦希杯赛斩获世界波",
        "逆境抗压韧性：对阵洛克伦滕瑟与利尔斯在被动局面下展现出极强韧性顽强扳平"
    ],
    "concerns": [
        "防守大开大合：8轮丢11球，比利时杯更被打入4球，防线在全员狂攻后容易留出身后巨大空档",
        "主力体能红线：连续双线作战下，托明、韦德、瓦莱里亚等核心跑动负荷极高，需防止后程拉伤",
        "主教练执照倒计时：60天执教豁免期已过大半，能否在足协限期前完成合规手续成潜在考题"
    ],
    "media_quote": {
        "source": "比利时《Sudinfo》专栏首席记者 菲利普·热拉尔",
        "content": "当维尔通夏天宣布任命一位连欧足联执照都没有的中国主教练时，整个瓦隆大区都在嗤之以鼻。然而8轮过去，这支原本的降级热门却以全联盟第一的进攻火力坐稳冲甲附加赛区。他的战术没有保守妥协，只有向前撕裂，徐正把这支边陲小城球队变成比乙最令人兴奋的摇滚乐队。"
    }
}

(DATA_DIR / "team_analysis.json").write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
print("3. Team analysis updated.")

# 4. MAILBOX UPDATE
mailbox = {
    "manager_profile": {
        "name": "耶稣 徐",
        "nationality": "中国",
        "club_name": "维尔通精英足球俱乐部 (RE Virton)",
        "role": "临时主教练 (战术总指挥)",
        "assistant_name": "大卫·齐特利 (David Zitelli, 欧足联持证)",
        "waiver_days_used": 56,
        "waiver_days_total": 60,
        "contract_end": "2026-06-30",
        "career_stage": "欧洲职业流浪 · 第 1 站 (比乙 · 排名第4)"
    },
    "messages": [
        {
            "id": "msg_007",
            "date": "2025-10-06 09:15",
            "from": "Rebeai Khabtane (俱乐部主席)",
            "avatar": "🏛️",
            "type": "高层特函",
            "subject": "冲进联赛前四！董事会正式启动转正评估与执照绿色通道",
            "content": "徐，昨天主场3-1干净利落击败法兰波垒斯后，整个更衣室都在为你欢呼！8轮15分、排名联赛第4，这不仅超越了保级目标，甚至直接杀进了升级附加赛区！另外关于60天豁免期即将到期的问题，比利时足协（KBVB）鉴于你的轰动性带队成绩与齐特利教练的深度搭档，已原则上同意为你延长执教特许期，并破格推荐你进入下个月在布鲁塞尔开班的欧足联高阶教练研习班。俱乐部已经为你备好正式续约合同，打完布鲁日青年后我们随时签约！"
        },
        {
            "id": "msg_006",
            "date": "2025-09-25 10:30",
            "from": "RTBF 比利时国家电视台体育频道",
            "avatar": "📺",
            "type": "媒体专访邀请",
            "subject": "《比乙奇迹与东方密码：独家专访维尔通主帅徐》",
            "content": "尊敬的徐教练：您带领维尔通在过去几周打出了令人叹为观止的攻势足球，客场3-1挑落瑟兰、杯赛6-4狂扫蒂格姆，同时您对东亚年轻新星（韩国朴昇秀、日本吉永梦希）的成功激活在欧洲足坛引发热议。RTBF诚邀您在国际比赛日期间录制一期专访，探讨您的反抢哲学与足球流浪之路。"
        },
        {
            "id": "msg_005",
            "date": "2025-09-15 08:45",
            "from": "俱乐部首席运动医学顾问",
            "avatar": "🩺",
            "type": "医疗与体能通报",
            "subject": "全队体能负荷监控预警与轮换建议",
            "content": "徐指导：在连续经历高强度联赛与客场6-4的杯赛拉锯战后，GPS数据显示全队场均跑动仍保持在123公里以上。托明和韦德的肌肉疲劳指数接近警戒阈值，好在韩国边锋朴昇秀与日本左后卫吉永梦希展现出了极其出色的体能储备，建议在后续两轮适当给予轮换首发，以防肌肉拉伤。"
        },
        {
            "id": "msg_004",
            "date": "2025-09-07 11:20",
            "from": "Mohamed Hakem (俱乐部总经理)",
            "avatar": "👔",
            "type": "杯赛祝报",
            "subject": "客场6-4惊险晋级比利时杯下一轮！老板坎特发来越洋贺电",
            "content": "昨天客场跟蒂格姆轰出6-4的比分，看台上的随队球迷嗓子都喊哑了！这场进球大战让全比利时媒体都在讨论维尔通。坎特先生刚从沙特吉达发来贺信，他为全队的求胜欲望感到自豪，同时提醒我们杯赛下一轮可能会遭遇比甲对手，奖金池已设立，期待徐指导继续带队创造奇迹！"
        },
        {
            "id": "msg_003",
            "date": "2025-08-17 19:30",
            "from": "Mohamed Hakem (俱乐部总经理)",
            "avatar": "👔",
            "type": "高层通报",
            "subject": "客战马斯梅赫伦赛后沟通与下轮动员",
            "content": "徐，客场打马斯梅赫伦向来是比乙最恶心的比赛之一，输球不必气馁。下周主场打哈瑟尔特是关键战，管理层全力支持你进行战术调整。"
        },
        {
            "id": "msg_002",
            "date": "2025-08-13 23:15",
            "from": "Rebeai Khabtane (俱乐部主席)",
            "avatar": "🏛️",
            "type": "董事会嘉奖",
            "subject": "祝贺主场首秀告捷及拿下新赛季首胜",
            "content": "徐，3-2战胜根特青年队展现了我们新阵容的活力。坎特先生对全队跑动非常赞赏，继续保持。"
        },
        {
            "id": "msg_001",
            "date": "2025-08-10 20:00",
            "from": "Mohamed Hakem (俱乐部总经理)",
            "avatar": "👔",
            "type": "紧急备忘录",
            "subject": "首秀逼平登德赛后反馈 & 足协60天报备",
            "content": "客场1-1逼平降班马登德，干得漂亮！60天临时豁免正式生效，请继续加油。"
        }
    ]
}

(DATA_DIR / "mailbox.json").write_text(json.dumps(mailbox, ensure_ascii=False, indent=2), encoding="utf-8")
print("4. Mailbox updated.")
