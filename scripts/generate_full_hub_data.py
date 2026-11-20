import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

# 1. LOAD EXISTING MATCHES (R1, R2, R3)
existing_matches = json.loads((DATA_DIR / "matches.json").read_text(encoding="utf-8"))[:3]

# Helper for radar and stats
def make_player(pos, name_zh, name_en, rating, min_played, is_mvp, stats_dict, radar_dict):
    radar_list = [{"subject": k, "value": v} for k, v in radar_dict.items()]
    return {
        "name": name_en,
        "name_en": name_en,
        "name_zh": name_zh,
        "pos": pos,
        "rating": rating,
        "min": min_played,
        "is_mvp": is_mvp,
        "stats": stats_dict,
        "radar": radar_list
    }

# Standard 11 lineup template
def make_virton_lineup(overrides, mvp_pos="AMR"):
    base_squad = [
        ("GK", "塞莱斯丁·德·施瑞沃", "Célestin De Schrevel", 6.8, 90, {
            "扑救次数": "4 次", "高空摘球": "2 次", "出击成功": "100%", "传球成功率": "79.1%", "长传到位": "12/17", "跑动距离": "5.4 km"
        }, {"门线扑救": 85, "出击果断": 80, "高空控制": 82, "后场出球": 75, "反应速度": 86, "指挥防线": 78}),
        ("DR", "斯蒂文·阿森盖", "Steeven Assengue", 7.0, 90, {
            "抢断/拦截": "4/3 次", "解围次数": "5 次", "传中成功率": "42%", "关键传球": "1 次", "地面对抗": "6/8", "跑动距离": "11.2 km"
        }, {"边路突击": 78, "防守拦截": 85, "传中创造": 80, "缠斗断球": 86, "前场插上": 79, "持球推进": 81}),
        ("DC", "阿兰·特查普切特", "Allan Tchaptchet", 7.1, 90, {
            "高空争顶": "7/9", "解围次数": "8 次", "封堵射门": "3 次", "传球成功率": "84.5%", "身体对抗": "88%", "跑动距离": "9.8 km"
        }, {"高空争顶": 92, "正面防守": 88, "卡位拦截": 85, "头球解围": 90, "贴身对抗": 89, "长传转移": 74}),
        ("DC", "泰迪·梅扎古", "Teddy Mezague", 7.0, 90, {
            "防守拦截": "4 次", "解围次数": "6 次", "造越位": "3 次", "长传准确": "9/12", "犯规/吃牌": "1/0", "跑动距离": "9.6 km"
        }, {"后防统领": 88, "正面拦截": 85, "位置感": 87, "高空解围": 84, "出球组织": 80, "硬碰硬": 86}),
        ("DL", "亚塞尼·本·哈米德", "Yassine Ben Hamed", 6.9, 90, {
            "铲断成功": "3/4", "边路套边": "5 次", "传中到位": "3 次", "关键传球": "1 次", "拦截回追": "3 次", "跑动距离": "11.4 km"
        }, {"边路突击": 80, "套边插上": 82, "传中脚法": 81, "回防补位": 79, "缠斗断球": 80, "速度冲刺": 84}),
        ("MC", "安托万·瓦莱里亚", "Antoine Valério", 7.1, 90, {
            "传球成功率": "86.2%", "向前输送": "14 次", "抢断拦截": "4/2 次", "争顶成功": "3 次", "关键传球": "2 次", "跑动距离": "12.1 km"
        }, {"中场调度": 88, "视野大局": 85, "拦截屏障": 82, "向前直塞": 86, "耐力跑动": 92, "压迫抢断": 83}),
        ("MC", "阿卢·登贝莱", "Aliou Dembélé", 7.2, 90, {
            "地面对抗": "8/10", "抢断拦截": "5/3 次", "后插上射门": "2 次", "传球到位": "45/51", "犯规战术": "2 次", "跑动距离": "12.4 km"
        }, {"中场扫荡": 90, "后插冲击": 85, "地面对抗": 88, "反抢延阻": 87, "全场覆盖": 94, "分球过渡": 80}),
        ("AMR", "泰伦·托明", "Tyrone Tormin", 7.6, 85, {
            "进球/助攻": "0球/1助", "关键传球": "4 次", "成功过人": "5 次", "射门(射正)": "3(2)", "传球成功率": "83%", "跑动距离": "11.7 km"
        }, {"边路突击": 96, "终结射门": 82, "传球创造": 90, "灵巧盘带": 94, "前场压迫": 85, "持球冲刺": 95}),
        ("AMC", "卢卡·迈奥拉诺", "Luca Maiorano", 7.2, 80, {
            "关键传球": "3 次", "前插射门": "3(1)", "受侵犯": "3 次", "传球成功率": "81.5%", "逼抢抢断": "2 次", "跑动距离": "11.3 km"
        }, {"前插终结": 86, "前腰策应": 85, "灵巧摆脱": 83, "禁区威胁": 87, "就地反抢": 80, "直塞渗透": 84}),
        ("AML", "阿卜杜勒萨马迪·哈切姆", "Abdelsamad Hachem", 7.5, 90, {
            "进球/助攻": "1球/0助", "射门(射正)": "3(2)", "内切突破": "4 次", "高位压迫": "5 次", "关键传球": "1 次", "跑动距离": "11.6 km"
        }, {"内切射门": 92, "抢点吃饼": 90, "无球跑位": 88, "边路起速": 86, "门前嗅觉": 93, "前场紧逼": 84}),
        ("ST", "保罗·韦德", "Paul Wade", 7.4, 90, {
            "进球/助攻": "1球/0助", "支点做球": "6 次", "高空争顶": "7/10", "射门(射正)": "4(2)", "吸引防守": "8 次", "跑动距离": "10.8 km"
        }, {"中锋支点": 92, "头球轰炸": 90, "终结射门": 87, "身体对抗": 91, "回撤做球": 84, "逼抢中卫": 83})
    ]

    lineup = []
    for item in base_squad:
        pos, name_zh, name_en, rating, mins, stats, radar = item
        if pos in overrides:
            ov = overrides[pos]
            name_zh = ov.get("name_zh", name_zh)
            name_en = ov.get("name_en", name_en)
            rating = ov.get("rating", rating)
            stats.update(ov.get("stats", {}))
            radar.update(ov.get("radar", {}))
        is_mvp = (pos == mvp_pos)
        lineup.append(make_player(pos, name_zh, name_en, rating, mins, is_mvp, stats, radar))
    return lineup

# ROUND 4: 2-1 vs Hasselt (主胜)
r4_match = {
    "id": 4, "round": 4, "round_label": "第 4 轮", "date": "2025-08-24",
    "home_team": "维尔通精英", "away_team": "哈瑟尔特", "score_home": 2, "score_away": 1,
    "venue": "home", "stadium": "Stade Yvan Georges", "result": "W", "xg": 1.78, "shots": 16, "shots_on_target": 7, "distance_km": 122.4,
    "scorers": [
        {"player": "Abdelsamad Hachem", "minute": 28, "assist": "Tyrone Tormin", "player_zh": "阿卜杜勒萨马迪·哈切姆", "assist_zh": "泰伦·托明"},
        {"player": "Paul Wade", "minute": 67, "assist": "Aliou Dembélé", "player_zh": "保罗·韦德", "assist_zh": "阿卢·登贝莱"}
    ],
    "lineup": make_virton_lineup({
        "AMR": {"rating": 7.7, "stats": {"进球/助攻": "0球/1助", "关键传球": "4 次", "成功过人": "6 次", "跑动距离": "11.8 km"}},
        "AML": {"rating": 7.6, "stats": {"进球/助攻": "1球/0助", "射门(射正)": "3(2)", "跑动距离": "11.5 km"}},
        "ST": {"rating": 7.4, "stats": {"进球/助攻": "1球/0助", "高空争顶": "6/8", "跑动距离": "10.6 km"}}
    }, mvp_pos="AMR")
}

# ROUND 5: 1-1 vs Lokeren-Temse (客平)
r5_match = {
    "id": 5, "round": 5, "round_label": "第 5 轮", "date": "2025-08-31",
    "home_team": "皇家洛克伦滕瑟", "away_team": "维尔通精英", "score_home": 1, "score_away": 1,
    "venue": "away", "stadium": "Daknamstadion", "result": "D", "xg": 1.25, "shots": 12, "shots_on_target": 5, "distance_km": 124.8,
    "scorers": [
        {"player": "Park Seung-Soo", "minute": 74, "assist": "Luca Maiorano", "player_zh": "朴昇秀", "assist_zh": "卢卡·迈奥拉诺"}
    ],
    "lineup": make_virton_lineup({
        "AML": {"name_zh": "朴昇秀", "name_en": "Park Seung-Soo", "rating": 7.8, "stats": {"进球/助攻": "1球/0助", "关键传球": "2 次", "内切射门": "3(2)", "跑动距离": "11.4 km"}, "radar": {"边路突击": 90, "终结射门": 88, "灵巧盘带": 92, "持球冲刺": 91}},
        "MC": {"rating": 7.3, "stats": {"抢断拦截": "6/4 次", "跑动距离": "12.8 km"}},
        "GK": {"rating": 7.4, "stats": {"扑救次数": "6 次", "高空摘球": "4 次"}}
    }, mvp_pos="AML")
}

# ROUND 6: 2-2 vs Lierse Kempenzonen (主平)
r6_match = {
    "id": 6, "round": 6, "round_label": "第 6 轮", "date": "2025-09-14",
    "home_team": "维尔通精英", "away_team": "皇家利尔斯", "score_home": 2, "score_away": 2,
    "venue": "home", "stadium": "Stade Yvan Georges", "result": "D", "xg": 2.15, "shots": 18, "shots_on_target": 8, "distance_km": 121.5,
    "scorers": [
        {"player": "Abdelsamad Hachem", "minute": 35, "assist": "Adama Diop", "player_zh": "阿卜杜勒萨马迪·哈切姆", "assist_zh": "亚当穆斯·迪奥普"},
        {"player": "Luca Maiorano", "minute": 81, "assist": "Steeven Assengue", "player_zh": "卢卡·迈奥拉诺", "assist_zh": "斯蒂文·阿森盖"}
    ],
    "lineup": make_virton_lineup({
        "AMC": {"rating": 7.6, "stats": {"进球/助攻": "1球/0助", "前插抢点": "3 次", "跑动距离": "11.7 km"}},
        "AML": {"rating": 7.5, "stats": {"进球/助攻": "1球/0助", "射门(射正)": "4(2)", "跑动距离": "11.2 km"}}
    }, mvp_pos="AMC")
}

# ROUND 7: 1-3 vs RFC Seraing (客胜)
r7_match = {
    "id": 7, "round": 7, "round_label": "第 7 轮", "date": "2025-09-24",
    "home_team": "皇家瑟兰", "away_team": "维尔通精英", "score_home": 1, "score_away": 3,
    "venue": "away", "stadium": "Stade du Pairay", "result": "W", "xg": 2.42, "shots": 19, "shots_on_target": 9, "distance_km": 125.6,
    "scorers": [
        {"player": "Abdelsamad Hachem", "minute": 19, "assist": "Tyrone Tormin", "player_zh": "阿卜杜勒萨马迪·哈切姆", "assist_zh": "泰伦·托明"},
        {"player": "Aliou Dembélé", "minute": 52, "assist": "Paul Wade", "player_zh": "阿卢·登贝莱", "assist_zh": "保罗·韦德"},
        {"player": "Paul Wade", "minute": 78, "assist": "Marks Inchaud", "player_zh": "保罗·韦德", "assist_zh": "马克斯·因查德"}
    ],
    "lineup": make_virton_lineup({
        "ST": {"rating": 7.8, "stats": {"进球/助攻": "1球/1助", "高空争顶": "8/11", "跑动距离": "10.9 km"}},
        "AMR": {"rating": 7.6, "stats": {"进球/助攻": "0球/1助", "关键传球": "4 次", "突破过人": "5 次", "跑动距离": "11.9 km"}},
        "AML": {"rating": 7.5, "stats": {"进球/助攻": "1球/0助", "射门(射正)": "3(2)", "跑动距离": "11.3 km"}}
    }, mvp_pos="ST")
}

# ROUND 8: 3-1 vs Francs Borains (主胜，挑落大热冲上第4！)
r8_match = {
    "id": 8, "round": 8, "round_label": "第 8 轮", "date": "2025-10-05",
    "home_team": "维尔通精英", "away_team": "皇家法兰波垒斯", "score_home": 3, "score_away": 1,
    "venue": "home", "stadium": "Stade Yvan Georges", "result": "W", "xg": 2.68, "shots": 21, "shots_on_target": 10, "distance_km": 126.2,
    "scorers": [
        {"player": "Abdelsamad Hachem", "minute": 14, "assist": "Paul Wade", "player_zh": "阿卜杜勒萨马迪·哈切姆", "assist_zh": "保罗·韦德"},
        {"player": "Tyrone Tormin", "minute": 41, "assist": "Luca Maiorano", "player_zh": "泰伦·托明", "assist_zh": "卢卡·迈奥拉诺"},
        {"player": "Abdelsamad Hachem", "minute": 69, "assist": "Tyrone Tormin", "player_zh": "阿卜杜勒萨马迪·哈切姆", "assist_zh": "泰伦·托明"}
    ],
    "lineup": make_virton_lineup({
        "AMR": {"rating": 8.1, "stats": {"进球/助攻": "1球/1助", "关键传球": "5 次", "过人成功": "7 次", "传球成功率": "86%", "跑动距离": "12.0 km"}},
        "AML": {"rating": 8.0, "stats": {"进球/助攻": "2球/0助", "射门(射正)": "5(4)", "内切突破": "5 次", "跑动距离": "11.8 km"}},
        "ST": {"rating": 7.6, "stats": {"进球/助攻": "0球/1助", "支点做球": "8 次", "争顶胜率": "75%", "跑动距离": "11.1 km"}}
    }, mvp_pos="AMR")
}

all_matches = existing_matches + [r4_match, r5_match, r6_match, r7_match, r8_match]
(DATA_DIR / "matches.json").write_text(json.dumps(all_matches, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Matches written: {len(all_matches)} matches in matches.json")

# 2. NEWS UPDATE (ROUNDS 1-8 WITH SPICY SPECIAL COMMENTS)
existing_news = json.loads((DATA_DIR / "news.json").read_text(encoding="utf-8"))[:3]

r4_news = {
    "match_id": "20250824_virton_hasselt", "round": 4, "date": "2025-08-24", "fixture": "维尔通精英 2-1 哈瑟尔特",
    "dongqiudi_article": {
        "title": "两翼齐飞掀翻哈瑟尔特！徐指导主场两连胜，托明韦德再度连线",
        "summary": "凭借哈切姆与韦德在上下半场的各入一球，维尔通主场2-1力克哈瑟尔特。徐指导4-2-3-1高位逼抢体系显威，托明送出赛季第2次助攻，维尔通4轮斩获7分稳居联赛上半区。",
        "body": "北京时间8月24日晚，比乙第4轮在伊万·乔治球场打响。面对作风顽强的哈瑟尔特，维尔通开场便展开全场就地高压反抢。第28分钟，托明在右路晃开防守送出精确横传，哈切姆门前推射破门；第67分钟，后腰登贝莱直塞，中锋韦德抗开中卫推射死角！全场维尔通狂轰16脚射门，跑动距离达到122.4公里，展现出恐怖的前场压迫力。",
        "tags": ["比乙", "维尔通", "哈瑟尔特", "主场连胜", "战报"]
    },
    "hupu_thread": {
        "title": "[赛后评分] 比乙第4轮：维尔通 2-1 哈瑟尔特。4轮7分稳坐上半区，如何评价徐指导这场高位压迫？",
        "coach_score": 9.4,
        "comments": [
            {"username": "排队道歉登记处主任", "tag": "徐圣信徒", "content": "当初开赛前冷嘲热讽说‘无证教练带队4轮拿不到2分’的懂哥呢？滚出来给徐圣磕一个！4战7分，两翼直接突爆！", "likes": 688},
            {"username": "瓦隆大区战术研究员", "tag": "比乙球探", "content": "这套4231高位压迫太凶狠了，哈瑟尔特从后卫到门将被逼得狂开大脚。托明这赛季真的杀红了眼，右路一条龙！", "likes": 512},
            {"username": "留洋观察所", "tag": "中国足球海外党", "content": "徐指导每次赢球都在更衣室拉着老齐特利拍照，合规避险做得滴水不漏，情商智商全部拉满！", "likes": 420}
        ]
    },
    "belgian_media_snippet": "Sudinfo: 'Virton confirme son renouveau avec une victoire 2-1 face à Hasselt. L'intensité imposée par Xu surprend tout le monde.'"
}

r5_news = {
    "match_id": "20250831_lokeren_virton", "round": 5, "date": "2025-08-31", "fixture": "皇家洛克伦滕瑟 1-1 维尔通精英",
    "dongqiudi_article": {
        "title": "韩国新星朴昇秀替补救主！维尔通客场1-1逼平不败劲旅洛克伦滕瑟",
        "summary": "面对此前保持全胜且未丢一球的争冠热门洛克伦滕瑟，维尔通在落后局面下依靠中国少帅徐的神奇换人，韩国小将朴昇秀第74分钟内切抽射破门，客场顽强抢下关键1分！",
        "body": "北京时间8月31日，比乙第5轮迎来焦点战。维尔通客场挑战比乙防守最强劲旅皇家洛克伦滕瑟。在半场0-1落后的逆境下，徐指导果断换上韩国年轻新秀朴昇秀。第74分钟，迈奥拉诺送出肋部斜传，朴昇秀晃过后卫冷静抽射死角破门扳平！维尔通门将德·施瑞沃全场贡献6次神扑，成功打破对手全胜金身！",
        "tags": ["比乙", "维尔通", "洛克伦滕瑟", "朴昇秀", "绝平战报"]
    },
    "hupu_thread": {
        "title": "[赛后评分] 比乙第5轮：洛克伦滕瑟 1-1 维尔通。韩国小将朴昇秀救主，如何评价这场东亚风暴联动？",
        "coach_score": 9.5,
        "comments": [
            {"username": "首尔塔下喝青岛啤酒", "tag": "国际足球整活大师", "content": "【中韩足球历史性大和解】中国主帅妙手调遣，韩国18岁小将替补救主斩获处子球！徐指导是真懂怎么整合东亚力量啊！", "likes": 985},
            {"username": "比乙硬骨头观察哨", "tag": "战术狂魔", "content": "客场打洛克伦滕瑟这种全胜防守天花板能咬下一分，含金量甚至高过打根特！徐指导下半场的433变阵把对面的边路锁死了。", "likes": 732},
            {"username": "留欧青年军", "tag": "海外新星雷达", "content": "朴昇秀在水原三星的时候我就看好他，没想到被徐指导租过来直接当秘密武器使，这一脚内切抽射太有灵性了！", "likes": 560}
        ]
    },
    "belgian_media_snippet": "La Meuse: 'Le coup de poker de Xu : l'entrée du jeune Sud-Coréen Park Seung-Soo prive Lokeren d'une 5ème victoire d'affilée.'"
}

r6_news = {
    "match_id": "20250914_virton_lierse", "round": 6, "date": "2025-09-14", "fixture": "维尔通精英 2-2 皇家利尔斯",
    "dongqiudi_article": {
        "title": "81分钟迈奥拉诺头球绝平！维尔通2-2战平利尔斯，狂暴攻势延续",
        "summary": "在经历周中比利时杯6-4血战晋级后，体能受限的维尔通两度落后两度扳平。哈切姆首开纪录，迈奥拉诺第81分钟头球建功，维尔通保持各项赛事4场不败。",
        "body": "北京时间9月14日，比乙第6轮维尔通坐镇主场对决皇家利尔斯。此前在比利时杯中维尔通刚刚与蒂格姆打出6-4的进球狂欢，全队体能面临大考。本场比赛波澜壮阔，利尔斯两度取得领先，但维尔通全队展现出铁血斗志，哈切姆接迪奥普传球推射扳平；比赛尾声第81分钟，边后卫阿森盖右路起球，迈奥拉诺前插甩头攻门绝平比分！",
        "tags": ["比乙", "维尔通", "利尔斯", "绝平", "攻势足球"]
    },
    "hupu_thread": {
        "title": "[赛后评分] 比乙第6轮：维尔通 2-2 利尔斯。两度落后两度扳平，如何评价徐指导这支疯狗流球队的韧性？",
        "coach_score": 8.9,
        "comments": [
            {"username": "速效救心丸VIP批发商", "tag": "心肌梗塞级观赛体验", "content": "杯赛刚轰完6-4，联赛又来个2-2！徐指导你的战术字典里到底有没有‘苟住’这两个字？！看维尔通比赛真得自备氧气瓶！", "likes": 842},
            {"username": "疯狗流门徒", "tag": "重金属足球", "content": "虽然防线丢了2个，但落后时全员压上的那股狠劲真让人梦回当年贝尔萨的利兹联！81分钟绝平，血性拉满！", "likes": 619},
            {"username": "坎特后援会欧洲分会", "tag": "老板视察组", "content": "坎特投资维尔通真没看走眼，全场跑动又干到了121公里，就算累到抽筋也没人散步，这就是徐指导灌输的意志品质！", "likes": 477}
        ]
    },
    "belgian_media_snippet": "RTL Sport: 'Virton ne lâche rien : menés à deux reprises, les hommes de Xu arrachent le 2-2 face au Lierse dans une fin de match électrique.'"
}

r7_news = {
    "match_id": "20250924_seraing_virton", "round": 7, "date": "2025-09-24", "fixture": "皇家瑟兰 1-3 维尔通精英",
    "dongqiudi_article": {
        "title": "客场狂风骤雨！维尔通3-1瑟兰收获客场首胜，多点开花杀入前五",
        "summary": "维尔通迎来客场大胜！哈切姆第19分钟闪击得手，下半场登贝莱与保罗·韦德连下两城，托明送出赛季第3次助攻，维尔通客场3-1完胜瑟兰，积12分强势杀入积分榜前列。",
        "body": "北京时间9月24日，比乙第7轮。维尔通做客瑟兰球场。开场仅19分钟，边路核心托明边路人球分过突入禁区送出倒三角，哈切姆推射远角得手！下半场维尔通继续掀起进攻狂潮，登贝莱与高中锋韦德先后建功锁定胜局。全场维尔通轰出19脚射门，预期进球高达2.42，展现出摧枯拉朽的立体打击能力！",
        "tags": ["比乙", "维尔通", "瑟兰", "客场大胜", "三叉戟爆发"]
    },
    "hupu_thread": {
        "title": "[赛后评分] 比乙第7轮：瑟兰 1-3 维尔通。客场3-1强势碾压，如何评价徐指导这波客场爆发？",
        "coach_score": 9.6,
        "comments": [
            {"username": "留洋名帅观察员", "tag": "徐圣粉丝团团长", "content": "客场首胜直接轰了3个！哈切姆、登贝莱、韦德全开胡！徐指导把这套4231已经磨合得炉火纯青了，比乙谁碰谁头疼！", "likes": 915},
            {"username": "比利时足协请开恩", "tag": "合规请愿代表", "content": "外媒报道当地球迷已经开始给足协写信了：求求千万别在60天豁免期到后禁赛徐指导！这是瓦隆大区近十年最漂亮的攻势足球！", "likes": 780},
            {"username": "保罗韦德头号吹", "tag": "大中锋信仰", "content": "韦德今天单场1球1助攻，78分钟那个禁区内抗翻中卫抽射，支点作用直接拉满！这套中轴线太扎实了！", "likes": 562}
        ]
    },
    "belgian_media_snippet": "L'Avenir: 'Virton s'impose avec autorité à Seraing (1-3). L'attaque de feu imaginée par Xu fait trembler toute la Challenger Pro League.'"
}

r8_news = {
    "match_id": "20251005_virton_francs", "round": 8, "date": "2025-10-05", "fixture": "维尔通精英 3-1 皇家法兰波垒斯",
    "dongqiudi_article": {
        "title": "3-1挑落冲甲热门！维尔通豪取两连胜飙升至比乙第4，哈切姆双响托明独造两球",
        "summary": "震撼比乙！维尔通坐镇主场3-1干净利落击败此前排名前列的冲甲大热法兰波垒斯。哈切姆梅开二度，托明世界波破门+独造两球获评全场MVP（8.1分）。维尔通8轮狂轰16球，以进攻第一姿态强势杀入升级附加赛区！",
        "body": "北京时间10月5日，比乙第8轮迎来焦点大战。赛前排名靠前的皇家法兰波垒斯做客伊万·乔治球场。然而比赛完全进入了维尔通的进攻节奏！\n\n【进攻万花筒：哈切姆双响，托明长途奔袭】\n比赛第14分钟，保罗·韦德禁区内做球，哈切姆迎球怒射先拔头筹！第41分钟，托明上演个人秀，右路截球后连过两人轰出一脚石破天惊的世界波破门！下半场第69分钟，托明再次送出精准斜塞，哈切姆门前推射完成梅开二度！尽管法兰波垒斯扳回一球，但维尔通最终3-1完胜对手！\n\n【奇迹之路：8轮16球，保级队跃升至冲甲区第4】\n此役过后，维尔通8战4胜3平1负积15分，狂轰16球冠绝比乙全联盟，直接跃升至积分榜第4位（跻身升级附加赛区）。这位无证临危受命的中国年轻教头，正在比利时足坛谱写不可思议的足球神话！",
        "tags": ["比乙", "维尔通", "法兰波垒斯", "哈切姆双响", "托明世界波", "跻身前四"]
    },
    "hupu_thread": {
        "title": "[赛后评分] 比乙第8轮：维尔通 3-1 法兰波垒斯。豪取两连胜飙升至联赛第4！如何评价徐指导这波封神带队？",
        "coach_score": 9.9,
        "comments": [
            {"username": "徐圣全球后援会终身荣誉会员", "tag": "彻底跪服", "content": "【全网置顶】赛前媒体预测倒数第一降级大热门，8轮踢完轰入16球比乙进攻火力第一，直接干到联赛第4进升级附加赛区？！徐圣！请收下我的膝盖！从今天起我就是徐圣的死忠粉！", "likes": 1280},
            {"username": "各大论坛排队道歉处", "tag": "统一悔过书", "content": "曾经嘲讽徐指导‘走后门、没执照、活不过三轮’的黑子们，请在此楼统一打卡道歉！今天托明那个40米长途奔袭单刀挑射破门，直接把冲甲大热踢崩溃了！", "likes": 1056},
            {"username": "坎特海外理财顾问", "tag": "老板偷着乐", "content": "老板坎特在吉达看录播估计嘴都合不拢了！这哪是保级队啊，这分明是比乙多特蒙德！托明4次助攻全比乙第1，哈切姆5球杀进前3，身价全特么翻倍了！", "likes": 889},
            {"username": "欧足联特批办事处", "tag": "足协别不识抬举", "content": "听说比利时足协已经特批给徐指导延长执教豁免期并破格推荐进高阶研习班了！董事会赶紧把正式合同递上去，手慢了比甲球队就要来挖墙脚了！", "likes": 764},
            {"username": "东亚足球共同体", "tag": "中日韩联动", "content": "中国主帅带队，韩国朴昇秀进球，日本吉永梦希杯赛轰世界波，法国阿尔及利亚边锋双子星起飞，徐指导这更衣室凝聚力和用人眼光，不服不行！", "likes": 642}
        ]
    },
    "belgian_media_snippet": "Sudinfo: 'L'incroyable épopée de Xu : Virton surclasse les Francs Borains (3-1) et s'installe à la 4e place ! L'attaque la plus prolifique de D2 fait rêver toute la province de Luxembourg.'"
}

all_news = existing_news + [r4_news, r5_news, r6_news, r7_news, r8_news]
(DATA_DIR / "news.json").write_text(json.dumps(all_news, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"News written: {len(all_news)} rounds in news.json")
