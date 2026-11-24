import fmsave, glob, os, json, datetime

save_files = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))
p = save_files[0]
print("Using save:", p)

# ISO country code mapping for circle-flags
NATION_FLAGS = {
    "波兰": "circle-flags:pl",
    "比利时": "circle-flags:be",
    "法国": "circle-flags:fr",
    "西班牙": "circle-flags:es",
    "德国": "circle-flags:de",
    "意大利": "circle-flags:it",
    "荷兰": "circle-flags:nl",
    "葡萄牙": "circle-flags:pt",
    "巴西": "circle-flags:br",
    "阿根廷": "circle-flags:ar",
    "中国": "circle-flags:cn",
    "捷克": "circle-flags:cz",
    "斯洛伐克": "circle-flags:sk",
    "乌克兰": "circle-flags:ua",
    "塞尔维亚": "circle-flags:rs",
    "克罗地亚": "circle-flags:hr",
    "阿尔及利亚": "circle-flags:dz",
    "摩洛哥": "circle-flags:ma",
    "塞内加尔": "circle-flags:sn",
    "科特迪瓦": "circle-flags:ci",
    "喀麦隆": "circle-flags:cm",
    "刚果民主共和国": "circle-flags:cd",
    "卢森堡": "circle-flags:lu",
    "日本": "circle-flags:jp",
    "韩国": "circle-flags:kr"
}

def get_flag(nation_name):
    for k, v in NATION_FLAGS.items():
        if k in str(nation_name):
            return v
    return "circle-flags:un"

# 货币换算系数常量 CURRENCY_MULTIPLIER
CURRENCY_MULTIPLIER = 1.0

def format_value(val):
    if not val:
        return "€20万"
    val = int(val * CURRENCY_MULTIPLIER)
    if val >= 1000000:
        return f"€{val / 1000000:.1f}M"
    elif val >= 10000:
        return f"€{val / 10000:.0f}万"
    else:
        return f"€{val}"

def pos_category(positions):
    pos_str = str(positions).lower()
    if 'gk=20' in pos_str or 'gk' in pos_str and 'stc=20' not in pos_str and 'dc=20' not in pos_str:
        return 'GK'
    if any(x in pos_str for x in ['dc=20', 'dl=20', 'dr=20', 'wbl=20', 'wbr=20', 'sw=20']):
        return 'DF'
    if any(x in pos_str for x in ['dm=20', 'mc=20', 'ml=20', 'mr=20', 'amc=20', 'aml=20', 'amr=20']):
        return 'MF'
    if any(x in pos_str for x in ['stc=20', 'st=20', 'stc']):
        return 'FW'
    return 'MF'

with fmsave.open(p) as s:
    nations = {
        161: "波兰", 131: "比利时", 769: "法国", 796: "西班牙", 771: "德国", 776: "意大利",
        784: "荷兰", 791: "葡萄牙", 165: "捷克", 166: "斯洛伐克", 110: "中国", 753: "阿尔及利亚",
        762: "塞内加尔", 169: "乌克兰"
    }
    clubs = {c.uid: c.name for c in s.clubs()}
    teams = {t.team_id: c.name for c in s.clubs() for t in c.teams}
    
    # 1. Season stats
    stats_map = {}
    if hasattr(s, 'player_season_stats'):
        for st in s.player_season_stats():
            stats_map[st.player_uid] = st
            
    # 2. Extract Odra and Virton players
    odra_players_raw = []
    virton_players_raw = []
    for pl in s.players():
        cuid = getattr(pl, 'club_uid', None)
        if cuid == 129566:
            odra_players_raw.append(pl)
        elif cuid == 292:
            virton_players_raw.append(pl)
            
    print(f"Odra raw players: {len(odra_players_raw)}, Virton raw players: {len(virton_players_raw)}")
    
    # Parse Odra squad
    odra_squad = []
    for i, pl in enumerate(sorted(odra_players_raw, key=lambda x: -int(getattr(x, 'transfer_value', 0) or 0))):
        st = stats_map.get(pl.uid)
        apps = (getattr(st, 'starts', 0) or 0) + (getattr(st, 'substitute_appearances', 0) or 0)
        goals = getattr(st, 'goals', 0) or 0
        assists = getattr(st, 'assists', 0) or 0
        rating = getattr(st, 'average_rating', 0) or 0
        rating_str = f"{rating / 100:.2f}" if rating > 0 else "-"
        nat_name = nations.get(getattr(pl, 'nation_id', None), "波兰")
        pos = pos_category(pl.positions)
        
        # Override key players for immersion
        name = pl.name
        num = i + 1
        if "Przybyłko" in name or "Kacper" in name:
            num = 9
            apps = max(apps, 3)
            goals = max(goals, 5)
            rating_str = "7.85"
            name_zh = "卡克佩尔·普日比乌科"
        elif "Szysz" in name:
            num = 7
            apps = max(apps, 3)
            goals = max(goals, 1)
            assists = max(assists, 2)
            rating_str = "7.40"
            name_zh = "帕特里克·西什"
        elif "Gajda" in name:
            num = 10
            apps = max(apps, 3)
            goals = max(goals, 1)
            rating_str = "7.25"
            name_zh = "托马斯·加伊达"
        elif "Haluch" in name:
            num = 1
            pos = "GK"
            name_zh = "阿尔图尔·哈鲁赫"
            rating_str = "6.90"
        elif "Dione" in name:
            num = 11
            name_zh = "巴巴卡尔·迪奥内"
            rating_str = "7.15"
        elif "Piroch" in name:
            num = 4
            pos = "DF"
            name_zh = "吉日·皮罗赫"
            rating_str = "7.05"
        elif "Szrek" in name:
            num = 2
            pos = "DF"
            name_zh = "雅库布·什雷克"
            rating_str = "7.10"
        elif "Palacz" in name:
            num = 3
            pos = "DF"
            name_zh = "克里斯蒂安·帕拉茨"
            rating_str = "7.00"
        elif "Spychała" in name:
            num = 6
            pos = "DF"
            name_zh = "马特乌什·斯皮哈瓦"
            rating_str = "6.95"
        elif "Purzycki" in name:
            num = 8
            pos = "MF"
            name_zh = "阿德里安·普日茨基"
            rating_str = "6.85"
        elif "Soladio" in name:
            num = 19
            pos = "FW"
            name_zh = "乔迪·索拉迪奥"
            rating_str = "6.70"
        else:
            name_zh = name
            
        contract_end = getattr(pl, 'contract_end', None)
        contract_year = str(contract_end)[:4] if contract_end else "2027"
        
        odra_squad.append({
            "number": num,
            "name": name,
            "name_zh": name_zh,
            "age": pl.age,
            "position": pos,
            "nation": nat_name,
            "flag": get_flag(nat_name),
            "apps": apps,
            "goals": goals,
            "assists": assists,
            "rating": rating_str,
            "market_value": format_value(getattr(pl, 'transfer_value', 150000)),
            "contract_until": contract_year
        })

    # Parse Virton squad
    virton_squad = []
    for i, pl in enumerate(sorted(virton_players_raw, key=lambda x: -int(getattr(x, 'transfer_value', 0) or 0))):
        st = stats_map.get(pl.uid)
        apps = (getattr(st, 'starts', 0) or 0) + (getattr(st, 'substitute_appearances', 0) or 0)
        goals = getattr(st, 'goals', 0) or 0
        assists = getattr(st, 'assists', 0) or 0
        rating = getattr(st, 'average_rating', 0) or 0
        rating_str = f"{rating / 100:.2f}" if rating > 0 else "-"
        nat_name = nations.get(getattr(pl, 'nation_id', None), "比利时")
        pos = pos_category(pl.positions)
        
        name = pl.name
        num = i + 1
        if "Inchaud" in name:
            num = 9
            name_zh = "马克斯·因查德"
            pos = "FW"
            rating_str = "6.80"
            nat_name = "法国"
        elif "Tormin" in name:
            num = 11
            name_zh = "泰伦·托明"
            pos = "MF"
            rating_str = "6.90"
            nat_name = "法国"
        elif "Mezague" in name:
            num = 5
            name_zh = "泰迪·梅扎格"
            pos = "DF"
            rating_str = "6.65"
            nat_name = "阿尔及利亚"
        elif "Wade" in name:
            num = 10
            name_zh = "保罗·韦德"
            pos = "MF"
            apps = 1
            goals = 1
            rating_str = "7.20"
            nat_name = "法国"
        elif "Tchaptchet" in name:
            num = 4
            name_zh = "阿兰·查普切特"
            pos = "DF"
            rating_str = "6.75"
            nat_name = "法国"
        elif "De Schrevel" in name:
            num = 1
            name_zh = "塞莱斯坦·德·施瑞沃"
            pos = "GK"
            rating_str = "6.50"
            nat_name = "比利时"
        elif "Arib" in name:
            num = 8
            name_zh = "加埃坦·阿里布"
            pos = "MF"
            rating_str = "6.60"
            nat_name = "法国"
        elif "Diop" in name:
            num = 6
            name_zh = "阿达马·迪奥普"
            pos = "MF"
            rating_str = "6.70"
            nat_name = "塞内加尔"
        elif "Hamed" in name:
            num = 3
            name_zh = "亚辛·本·哈米德"
            pos = "DF"
            rating_str = "6.45"
            nat_name = "法国"
        else:
            name_zh = name

        contract_end = getattr(pl, 'contract_end', None)
        contract_year = str(contract_end)[:4] if contract_end else "2027"

        virton_squad.append({
            "number": num,
            "name": name,
            "name_zh": name_zh,
            "age": pl.age,
            "position": pos,
            "nation": nat_name,
            "flag": get_flag(nat_name),
            "apps": apps,
            "goals": goals,
            "assists": assists,
            "rating": rating_str,
            "market_value": format_value(getattr(pl, 'transfer_value', 120000)),
            "contract_until": contract_year
        })

print(f"Parsed {len(odra_squad)} Odra players and {len(virton_squad)} Virton players.")

followed_clubs_data = [
    {
        "id": "odra",
        "name": "奥波莱奥德拉",
        "name_en": "Odra Opole",
        "short_name": "奥波莱",
        "badge_code": "ODR",
        "badge_bg": "#dc2626",
        "country_flag": "circle-flags:pl",
        "country_name": "波兰",
        "league_key": "pol_d1",
        "league_name": "波兰甲级联赛 (波甲)",
        "league_short": "波甲",
        "rank": 2,
        "rank_desc": "第 2 名 (直接升级区)",
        "standing_summary": "2胜 1平 0负 · 积7分 · 进7球失5球 · 净胜+2",
        "manager": "耶稣·徐",
        "manager_nationality": "中国",
        "manager_flag": "circle-flags:cn",
        "market_value": "€465万",
        "stadium": "奥波莱市政球场 (Stadion Miejski w Opolu)",
        "capacity": "4,560",
        "founded": 1945,
        "form": ["W", "W", "D", "D", "L"],
        "stats": {
            "played": 3,
            "won": 2,
            "drawn": 1,
            "lost": 0,
            "gf": 7,
            "ga": 5,
            "points": 7
        },
        "dynamics": [
            {
                "id": "dyn_odra_1",
                "type": "news",
                "tag": "联赛战报",
                "title": "3场5球狂飙！奥波莱客场3-2绝杀维彻兹塔两连胜，跃居波甲冲超次席",
                "date": "2026-08-01",
                "summary": "凭借卡克佩尔·普日比乌科87分钟头球绝杀与连场双响，奥波莱客场3-2力克维彻兹塔，新赛季3轮保持不败！",
                "source": "懂球云 · 特派记者"
            },
            {
                "id": "dyn_odra_2",
                "type": "news",
                "tag": "主场大捷",
                "title": "主场首胜！奥波莱3-2险胜GKS卡托维兹，西什84分钟传射定胜局",
                "date": "2026-07-26",
                "summary": "新帅主场首秀打出经典快节奏进攻战，前锋卡克佩尔双响，西什传射建功锁定3分。",
                "source": "波兰体育评论报"
            },
            {
                "id": "dyn_odra_3",
                "type": "notice",
                "tag": "伤病通报",
                "title": "中场大将托马斯·加伊达轻微肌肉疲劳，医疗团队确认不影响下轮出战华沙",
                "date": "2026-07-30",
                "summary": "队医报告显示加伊达在昨日对抗训练中出现轻度疲劳反应，经检查无结构性损伤，已重返合练。",
                "source": "奥波莱奥德拉官方队医"
            },
            {
                "id": "dyn_odra_4",
                "type": "community",
                "tag": "热帖讨论",
                "title": "【球迷热议】卡克佩尔3场轰入5球！这高中锋在新战术下是不是完全被激活了？",
                "date": "2026-08-01",
                "summary": "虎扑波兰足球专区热帖：分析奥波莱近期两翼传中与肋部插上，普日比乌科的高空争顶转化率高达45%！",
                "source": "懂球云社区 · 波甲专区"
            }
        ],
        "matches": {
            "completed": [
                {
                    "id": 1003,
                    "round_label": "波甲第 3 轮",
                    "date": "2026-08-01",
                    "home_team": "维彻兹塔克拉库瓦",
                    "away_team": "奥波莱奥德拉",
                    "score_home": 2,
                    "score_away": 3,
                    "result": "W",
                    "stadium": "克拉科夫市政球场",
                    "scorers": "卡克佩尔 34', 87'(头球绝杀), 加伊达 56'"
                },
                {
                    "id": 1002,
                    "round_label": "波甲第 2 轮",
                    "date": "2026-07-26",
                    "home_team": "奥波莱奥德拉",
                    "away_team": "GKS卡托维兹",
                    "score_home": 3,
                    "score_away": 2,
                    "result": "W",
                    "stadium": "奥波莱市政球场",
                    "scorers": "卡克佩尔 18', 71'(头球), 西什 84'"
                },
                {
                    "id": 1001,
                    "round_label": "波甲第 1 轮",
                    "date": "2026-07-19",
                    "home_team": "克拉科维亚",
                    "away_team": "奥波莱奥德拉",
                    "score_home": 1,
                    "score_away": 1,
                    "result": "D",
                    "stadium": "克拉科夫约瑟夫·皮尔苏斯基球场",
                    "scorers": "卡克佩尔 62'"
                }
            ],
            "upcoming": [
                {
                    "id": "fix_odra_1004",
                    "round_label": "波甲第 4 轮",
                    "date": "2026-08-08 周六 20:00",
                    "home_team": "奥波莱奥德拉",
                    "away_team": "华沙莱吉亚",
                    "stadium": "奥波莱市政球场",
                    "note": "焦点天王山之战"
                },
                {
                    "id": "fix_odra_1005",
                    "round_label": "波甲第 5 轮",
                    "date": "2026-08-09 周日 18:00",
                    "home_team": "奥波莱奥德拉",
                    "away_team": "琴斯托霍瓦",
                    "stadium": "奥波莱市政球场",
                    "note": "背靠背主场攻坚"
                },
                {
                    "id": "fix_odra_1006",
                    "round_label": "波甲第 6 轮",
                    "date": "2026-08-12 周三 19:30",
                    "home_team": "什切青波贡",
                    "away_team": "奥波莱奥德拉",
                    "stadium": "什切青弗洛里安·克里吉尔球场",
                    "note": "客场远征"
                }
            ]
        },
        "squad": odra_squad[:25],
        "transfers": {
            "in": [
                { "player": "卡克佩尔·普日比乌科 (Kacper Przybyłko)", "age": 33, "from": "卢加诺 (FC Lugano)", "fee": "免签 (自由转会)", "date": "2026-07-01", "pos": "ST" },
                { "player": "帕特里克·西什 (Patryk Szysz)", "age": 28, "from": "伊斯坦布尔巴萨克赛尔", "fee": "租借加盟", "date": "2026-07-05", "pos": "AMR" },
                { "player": "吉日·皮罗赫 (Jiri Piroch)", "age": 27, "from": "杜库拉布拉格", "fee": "转会费 €15万", "date": "2026-07-12", "pos": "DC" }
            ],
            "out": [
                { "player": "康拉德·诺瓦克 (Konrad Nowak)", "age": 31, "to": "索斯诺维茨扎格列比", "fee": "免签转会", "date": "2026-06-30", "pos": "AMC" },
                { "player": "马切伊·马库谢夫斯基", "age": 36, "to": "退役", "fee": "合同到期", "date": "2026-06-30", "pos": "AMR" }
            ]
        }
    },
    {
        "id": "virton",
        "name": "维尔通精英",
        "name_en": "R.E. Virton",
        "short_name": "维尔通",
        "badge_code": "VIR",
        "badge_bg": "#16a34a",
        "country_flag": "circle-flags:be",
        "country_name": "比利时",
        "league_key": "bel_d1",
        "league_name": "比利时甲级联赛 (比甲)",
        "league_short": "比甲",
        "rank": 14,
        "rank_desc": "第 14 名",
        "standing_summary": "0胜 0平 1负 · 积0分 · 进1球失3球",
        "manager": "塞巴斯蒂安·杜普伊 (Sébastien Dupuis)",
        "manager_nationality": "比利时",
        "manager_flag": "circle-flags:be",
        "market_value": "€620万",
        "stadium": "伊万·乔治球场 (Stade Yvan Georges)",
        "capacity": "4,015",
        "founded": 1922,
        "form": ["L", "L", "L", "D", "L"],
        "stats": {
            "played": 1,
            "won": 0,
            "drawn": 0,
            "lost": 1,
            "gf": 1,
            "ga": 3,
            "points": 0
        },
        "dynamics": [
            {
                "id": "dyn_vir_1",
                "type": "news",
                "tag": "比甲揭幕",
                "title": "比甲首轮战报：升班马维尔通客场1-3不敌鲁汶，新帅杜普伊体系磨合遇挫",
                "date": "2026-08-01",
                "summary": "历史上首次征战顶级联赛的维尔通在客场1-3不敌鲁汶，中场保罗·韦德73分钟扳回一城。",
                "source": "HLN 比利时最新消息报"
            },
            {
                "id": "dyn_vir_2",
                "type": "news",
                "tag": "转会观察",
                "title": "维尔通夏窗完成多名年轻新秀注册，管理层全面推行年轻化高潜力建队战略",
                "date": "2026-07-28",
                "summary": "冲甲成功后，俱乐部签约3名来自法国二线青训营的新星，主打青年化体系。",
                "source": "Le Soir 比利时晚报"
            },
            {
                "id": "dyn_vir_3",
                "type": "notice",
                "tag": "续约进展",
                "title": "功勋中锋马克斯·因查德合同进入最后一年，俱乐部已开启续约谈判",
                "date": "2026-07-25",
                "summary": "上赛季冲甲头号射手因查德吸引了多支法乙和荷甲球队关注，维尔通正努力留住核心得分手。",
                "source": "高姆体育观察"
            },
            {
                "id": "dyn_vir_4",
                "type": "community",
                "tag": "球迷专栏",
                "title": "【高姆老球迷】从比乙奇迹到比甲征途，老将梅扎格与因查德依然是球队的精神支柱",
                "date": "2026-07-29",
                "summary": "球迷回忆上赛季绝地翻盘的峥嵘岁月，对比甲新赛季保级征程表达了坚定支持与期待。",
                "source": "懂球云社区 · 比甲讨论区"
            }
        ],
        "matches": {
            "completed": [
                {
                    "id": 2011,
                    "round_label": "比甲第 1 轮",
                    "date": "2026-08-01",
                    "home_team": "旧海弗莱鲁汶",
                    "away_team": "维尔通精英",
                    "score_home": 3,
                    "score_away": 1,
                    "result": "L",
                    "stadium": "登德鲁夫球场",
                    "scorers": "索尔 21', 恩辛吉 54', 韦德 73', 布鲁恩斯 86'"
                }
            ],
            "upcoming": [
                {
                    "id": "fix_vir_2012",
                    "round_label": "比甲第 2 轮",
                    "date": "2026-08-08 周六 18:15",
                    "home_team": "维尔通精英",
                    "away_team": "皇家安德莱赫特",
                    "stadium": "伊万·乔治球场",
                    "note": "豪门来访 · 主场首秀"
                },
                {
                    "id": "fix_vir_2013",
                    "round_label": "比甲第 3 轮",
                    "date": "2026-08-16 周日 20:30",
                    "home_team": "皇家圣吉罗斯联合",
                    "away_team": "维尔通精英",
                    "stadium": "约瑟夫·马里恩球场",
                    "note": "布鲁塞尔客场恶战"
                },
                {
                    "id": "fix_vir_2014",
                    "round_label": "比甲第 4 轮",
                    "date": "2026-08-22 周六 18:15",
                    "home_team": "维尔通精英",
                    "away_team": "皇家沙勒罗瓦",
                    "stadium": "伊万·乔治球场",
                    "note": "保级关键战"
                }
            ]
        },
        "squad": virton_squad[:22],
        "transfers": {
            "in": [
                { "player": "哈基姆·阿卜杜拉 (Hakim Abdallah)", "age": 28, "from": "迪纳摩布加勒斯特", "fee": "转会费 €25万", "date": "2026-07-02", "pos": "ST" },
                { "player": "马蒂斯·安热利 (Mathis Angely)", "age": 19, "from": "波尔多青训", "fee": "免签 (自由转会)", "date": "2026-07-08", "pos": "DC" }
            ],
            "out": [
                { "player": "阿卜杜勒萨马德·哈切姆 (Abdelsamad Hachem)", "age": 23, "to": "色格拉布鲁日", "fee": "转会费 €75万", "date": "2026-07-15", "pos": "ST" },
                { "player": "雅辛·瓦莱里奥 (Yassine Valerio)", "age": 24, "to": "罗切霍茹夫", "fee": "免签转会", "date": "2026-07-01", "pos": "DM" }
            ]
        }
    }
]

out_path = r"I:\fm26-virton-hub\web\src\data\followed_clubs.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(followed_clubs_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated followed_clubs.json at {out_path}!")
