import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

# Real starting 11 based on save.selections() and save.tactics()
# Slot 0: Célestin De Schrevel (GK)
# Slot 1: Steeven Assengue (DR)
# Slot 2: Teddy Mezague (DC1)
# Slot 3: Allan Tchaptchet (DC2)
# Slot 4: Yumeki Yoshinaga (DL)
# Slot 5: Aliou Dembélé (MC)
# Slot 6: Antoine Valério (DM)
# Slot 7: Luca Maiorano (AMR)
# Slot 8: Paul Wade (AMC)
# Slot 9: Park Seung-Soo (AML)
# Slot 10: Abdelsamad Hachem (ST)

real_squad_template = [
    {
        "pos": "GK",
        "name": "Célestin De Schrevel",
        "name_en": "Célestin De Schrevel",
        "name_zh": "塞莱斯丁·德·施瑞沃",
        "rating": 6.9,
        "min": 90,
        "is_mvp": False,
        "stats": {"扑救次数": "5 次", "出击成功": "100%", "短传组织": "28/31", "长传到位": "11/14", "高空摘球": "3 次", "跑动距离": "5.6 km"},
        "radar": [{"subject": "门线扑救", "value": 88}, {"subject": "出击果断", "value": 82}, {"subject": "短传脚法", "value": 85}, {"subject": "后场出球", "value": 84}, {"subject": "反应速度", "value": 86}, {"subject": "防线指挥", "value": 80}]
    },
    {
        "pos": "DR",
        "name": "Steeven Assengue",
        "name_en": "Steeven Assengue",
        "name_zh": "斯蒂文·阿森盖",
        "rating": 7.1,
        "min": 90,
        "is_mvp": False,
        "stats": {"右路插上": "6 次", "传中到位": "4 次", "拦截抢断": "4/3 次", "地面对抗": "7/9", "短传渗透": "42/47", "跑动距离": "11.6 km"},
        "radar": [{"subject": "右路套边", "value": 88}, {"subject": "短传配合", "value": 84}, {"subject": "防守拦截", "value": 85}, {"subject": "传中脚法", "value": 82}, {"subject": "前插助攻", "value": 80}, {"subject": "缠斗断球", "value": 86}]
    },
    {
        "pos": "DC1",
        "name": "Teddy Mezague",
        "name_en": "Teddy Mezague",
        "name_zh": "泰迪·梅扎古",
        "rating": 7.1,
        "min": 90,
        "is_mvp": False,
        "stats": {"后场倒脚": "56/60", "关键拦截": "5 次", "解围次数": "6 次", "高空争顶": "6/8", "造越位": "3 次", "跑动距离": "9.8 km"},
        "radar": [{"subject": "短传组织", "value": 86}, {"subject": "正面拦截", "value": 88}, {"subject": "防线统帅", "value": 89}, {"subject": "高空解围", "value": 85}, {"subject": "沉着冷静", "value": 87}, {"subject": "战术执行", "value": 90}]
    },
    {
        "pos": "DC2",
        "name": "Allan Tchaptchet",
        "name_en": "Allan Tchaptchet",
        "name_zh": "阿兰·特查普切特",
        "rating": 7.2,
        "min": 90,
        "is_mvp": False,
        "stats": {"头球解围": "8 次", "封堵射门": "3 次", "身体对抗": "9/10", "出球成功率": "89.2%", "精准回传": "18 次", "跑动距离": "10.0 km"},
        "radar": [{"subject": "硬碰硬对抗", "value": 94}, {"subject": "高空争顶", "value": 92}, {"subject": "后场出球", "value": 84}, {"subject": "禁区保护", "value": 90}, {"subject": "卡位抢断", "value": 88}, {"subject": "位置感", "value": 85}]
    },
    {
        "pos": "DL",
        "name": "Yumeki Yoshinaga",
        "name_en": "Yumeki Yoshinaga",
        "name_zh": "吉永梦希",
        "rating": 7.2,
        "min": 90,
        "is_mvp": False,
        "stats": {"左路助攻": "1 次", "关键传球": "3 次", "成功过人": "4 次", "短传渗透": "45/50", "抢断拦截": "3/2 次", "跑动距离": "12.1 km"},
        "radar": [{"subject": "左翼飞奔", "value": 92}, {"subject": "短传串联", "value": 88}, {"subject": "灵巧盘带", "value": 86}, {"subject": "传中创造", "value": 85}, {"subject": "前场插上", "value": 90}, {"subject": "回防补位", "value": 80}]
    },
    {
        "pos": "DM",
        "name": "Antoine Valério",
        "name_en": "Antoine Valério",
        "name_zh": "安托万·瓦莱里亚",
        "rating": 7.3,
        "min": 90,
        "is_mvp": False,
        "stats": {"中场节拍": "68/73", "向前输送": "19 次", "扫荡抢断": "5/3 次", "战术犯规": "2 次", "拦截反击": "4 次", "跑动距离": "12.5 km"},
        "radar": [{"subject": "短传节拍", "value": 92}, {"subject": "视野大局", "value": 90}, {"subject": "单后腰扫荡", "value": 88}, {"subject": "向前直塞", "value": 87}, {"subject": "耐力覆盖", "value": 94}, {"subject": "中场屏障", "value": 86}]
    },
    {
        "pos": "MC",
        "name": "Aliou Dembélé",
        "name_en": "Aliou Dembélé",
        "name_zh": "阿卢·登贝莱",
        "rating": 7.4,
        "min": 85,
        "is_mvp": False,
        "stats": {"非对称游弋": "活跃", "后插上射门": "3(2)", "进球/助攻": "1球/0助", "地面对抗": "8/10", "关键传球": "2 次", "跑动距离": "12.2 km"},
        "radar": [{"subject": "肋部穿插", "value": 90}, {"subject": "后插上终结", "value": 86}, {"subject": "地面对抗", "value": 89}, {"subject": "短传接应", "value": 88}, {"subject": "全能B2B", "value": 91}, {"subject": "前场施压", "value": 84}]
    },
    {
        "pos": "AMR",
        "name": "Luca Maiorano",
        "name_en": "Luca Maiorano",
        "name_zh": "卢卡·迈奥拉诺",
        "rating": 7.5,
        "min": 80,
        "is_mvp": False,
        "stats": {"进球/助攻": "1球/1助", "关键传球": "4 次", "突破过人": "4 次", "射门(射正)": "3(2)", "短传成功": "34/39", "跑动距离": "11.5 km"},
        "radar": [{"subject": "右路突击", "value": 88}, {"subject": "门前抢点", "value": 87}, {"subject": "短传渗透", "value": 89}, {"subject": "创造机会", "value": 88}, {"subject": "灵巧摆脱", "value": 85}, {"subject": "无球跑位", "value": 90}]
    },
    {
        "pos": "AMC",
        "name": "Paul Wade",
        "name_en": "Paul Wade",
        "name_zh": "保罗·韦德",
        "rating": 7.8,
        "min": 90,
        "is_mvp": False,
        "stats": {"前腰做球": "12 次", "关键传球": "5 次", "进球/助攻": "1球/1助", "高空摆渡": "8/10", "禁区前沿回敲": "7 次", "跑动距离": "11.4 km"},
        "radar": [{"subject": "前腰支点策应", "value": 95}, {"subject": "致命直塞", "value": 91}, {"subject": "后插上射门", "value": 88}, {"subject": "空中优势", "value": 92}, {"subject": "身体护球", "value": 93}, {"subject": "短传串联", "value": 89}]
    },
    {
        "pos": "AML",
        "name": "Park Seung-Soo",
        "name_en": "Park Seung-Soo",
        "name_zh": "朴昇秀",
        "rating": 7.6,
        "min": 85,
        "is_mvp": False,
        "stats": {"左路内切": "5 次", "射门(射正)": "3(2)", "进球/助攻": "1球/0助", "突破成功": "4/5", "短传到位": "31/35", "跑动距离": "11.7 km"},
        "radar": [{"subject": "内切抽射", "value": 91}, {"subject": "灵巧变向", "value": 93}, {"subject": "短传配合", "value": 87}, {"subject": "速度冲刺", "value": 92}, {"subject": "前插抢点", "value": 85}, {"subject": "传球创造", "value": 84}]
    },
    {
        "pos": "ST",
        "name": "Abdelsamad Hachem",
        "name_en": "Abdelsamad Hachem",
        "name_zh": "阿卜杜勒萨马迪·哈切姆",
        "rating": 8.2,
        "min": 90,
        "is_mvp": True,
        "stats": {"进球/助攻": "2球/0助", "门前单刀": "3 次", "射门(射正)": "5(4)", "预期进球xG": "1.82", "反越位冲刺": "7 次", "跑动距离": "11.8 km"},
        "radar": [{"subject": "单前锋终结", "value": 96}, {"subject": "门前嗅觉", "value": 95}, {"subject": "反越位突刺", "value": 94}, {"subject": "把握机会", "value": 93}, {"subject": "禁区抢点", "value": 92}, {"subject": "短传配合", "value": 82}]
    }
]

# Update matches.json
matches_path = DATA_DIR / "matches.json"
matches = json.loads(matches_path.read_text(encoding="utf-8"))

for m in matches:
    # Set lineup to real squad
    m["lineup"] = json.loads(json.dumps(real_squad_template))
    # Adjust MVP per match
    if m["round"] == 8:
        for p in m["lineup"]:
            p["is_mvp"] = (p["pos"] == "ST")  # Hachem MVP
    elif m["round"] == 5:
        for p in m["lineup"]:
            p["is_mvp"] = (p["pos"] == "AML")  # Park Seung-Soo MVP
    elif m["round"] == 7:
        for p in m["lineup"]:
            p["is_mvp"] = (p["pos"] == "ST")  # Hachem MVP
    else:
        for p in m["lineup"]:
            p["is_mvp"] = (p["pos"] == "AMC" or p["pos"] == "ST")

matches_path.write_text(json.dumps(matches, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated {len(matches)} matches with true FM lineup in matches.json!")

# Update team_analysis.json with REAL user tactics
real_analysis = {
  "tactical_system": {
    "formation": "4-1-1-3-1 (非对称密集短传)",
    "style_name": "密集短传 Tiki-Taka / 翼卫拉边",
    "tempo": "极快节奏 / 密集短传传控",
    "mentality": "积极进取 (Positive)",
    "secondary_system": "5-2-3 翼卫拉边 (双翼齐飞备选)",
    "striker_role": "阿卜杜勒萨马迪·哈切姆 (单箭头突前中锋 · 7球射手王)",
    "playmaker_role": "保罗·韦德 (前腰 AMC · 影锋策应支点 · 3球3助独造6球)",
    "record": "8场 4胜3平1负 积15分 (比乙第4，进16球火力第一)"
  },
  "tactical_overview": {
    "formation": "4-1-1-3-1 (非对称密集短传)",
    "mentality": "积极进取 (Positive) / 密集短传 / 翼卫拉边",
    "philosophy": "徐指导在FM存档中的真实战术蓝图：彻底摒弃盲目盲冲的高位压迫，确立以【4-1-1-3-1 后腰 翼卫拉边 非对称中场(中右) - 密集短传】为核心的传控突刺哲学。战术最大亮点在于中锋与前腰的职责重构——哈切姆作为绝对单箭头中锋，利用反越位与灵敏门前嗅觉8战狂轰7球；高大强壮的保罗·韦德则后撤至前腰（AMC）策应做球，独造6球（3球3助），形成无解的‘韦德支点做球 + 哈切姆后插突刺’双核驱动！",
    "head_coach": "耶稣 徐 (FM26 真实战术大师)",
    "record": "8场 4胜3平1负 积15分 (联赛第4，冲甲区)"
  },
  "attack_channels": {
    "left_wing": 34,
    "center": 36,
    "right_wing": 30,
    "left": 34,
    "right": 30,
    "key_corridor": "中路韦德策应分球 + 左右翼卫吉永梦希/阿森盖拉边 (密集短传)"
  },
  "team_radar": [
    {
      "label": "密集短传传控",
      "value": 96,
      "league_avg": 70,
      "desc": "以瓦莱里亚为单后腰枢纽，全队后场就地短传倒脚推进"
    },
    {
      "label": "单箭头中锋终结",
      "value": 98,
      "league_avg": 68,
      "desc": "哈切姆7战5球(各项赛事7球)，门前单刀把握率顶尖"
    },
    {
      "label": "前腰策应与做球",
      "value": 95,
      "league_avg": 65,
      "desc": "韦德回撤前腰送出16次关键传球+3次助攻，完美串联"
    },
    {
      "label": "双翼卫拉边插上",
      "value": 90,
      "league_avg": 72,
      "desc": "日本吉永梦希(左)与阿森盖(右)两翼拉边套上提供横向宽度"
    },
    {
      "label": "非对称中场防守",
      "value": 72,
      "league_avg": 75,
      "desc": "瓦莱里亚单后腰+登贝莱中右偏位，防线身后有一定防守纵深风险"
    },
    {
      "label": "战术变阵弹性",
      "value": 92,
      "league_avg": 74,
      "desc": "随局势可随时平滑切换5-2-3双翼齐飞，中日韩新星全面激活"
    }
  ],
  "strengths": [
    "真实核心单箭头哈切姆：彻底摆脱传统站桩打法，利用速度与门前嗅觉化身致命杀手，各项赛事狂轰7球！",
    "保罗·韦德的前腰支点奇兵：后撤至前腰（AMC）担任策应核心，利用高空争顶与做球优势独造6球（3球3助）！",
    "4-1-1-3-1 非对称中场架构：单后腰瓦莱里亚负责调度梳理，中右中场登贝莱自由穿插，短传渗透行云流水",
    "翼卫拉边与东亚青春风暴：左翼卫吉永梦希与左前腰朴昇秀在左路形成无解连线，客场绝平洛克伦滕瑟",
    "积极进取的自信心态：落后时绝不保守，凭借短传穿透与肋部多点包抄保持全比乙第一进攻火力（16球）"
  ],
  "concerns": [
    "单后腰防守覆盖负荷重：瓦莱里亚在4-1-1-3-1单后腰位置需要极高防守跑动量，体能下降时需注意保护肋部",
    "后场倒脚失误风险：密集短传风格下两中卫（梅扎古与特查普切特）出球频率极高，面对极端逼抢需防止失误",
    "前场深度轮换考量：托明、因查德作为超级替补需合理分配出场时间，保障前场四人组持续输出"
  ],
  "analyst_quote": "《Sudinfo》专栏深度解密：‘许多人误以为徐在打粗暴的高位逼抢，但仔细剖析维尔通的战术板，你会发现这是一套极其考究的【4-1-1-3-1 非对称密集短传】艺术。他将保罗·韦德放在前腰作为中转站，真正突前的尖刀是哈切姆；左翼卫吉永梦希与右翼卫阿森盖极大拉开了场地宽度。这一套颠覆性的角色重置，直接创造了比乙最狂暴的16球进攻狂潮！’",
  "media_quote": {
    "source": "比利时《Sudinfo》专栏首席记者 菲利普·热拉尔",
    "content": "《Sudinfo》专栏深度解密：‘许多人误以为徐在打粗暴的高位逼抢，但仔细剖析维尔通的战术板，你会发现这是一套极其考究的【4-1-1-3-1 非对称密集短传】艺术。他将保罗·韦德放在前腰作为中转站，真正突前的尖刀是哈切姆；左翼卫吉永梦希与右翼卫阿森盖极大拉开了场地宽度。这一套颠覆性的角色重置，直接创造了比乙最狂暴的16球进攻狂潮！’"
  }
}

(DATA_DIR / "team_analysis.json").write_text(json.dumps(real_analysis, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated team_analysis.json with real user tactics!")
