import json
from pathlib import Path

FOLLOWED_PATH = Path(r"I:\fm26-virton-hub\web\src\data\followed_clubs.json")

def sync_transfers():
    with open(FOLLOWED_PATH, 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    # 1. Odra Opole
    odra = next((c for c in clubs if c['id'] in ['odra', 'odra_opole']), None)
    if odra:
        odra['transfers'] = {
            "in": [
                {
                    "player": "霍尔迪·索拉迪奥 (Jordy Soladio)",
                    "name": "霍尔迪·索拉迪奥",
                    "pos": "ST",
                    "age": 28,
                    "from_team": "自由身免签 (旧海弗莱鲁汶青训)",
                    "fee": "免签 (自由转会)",
                    "date": "2026-07-24",
                    "wage": "€5,186/周",
                    "contract": "至 2029-06-30"
                },
                {
                    "player": "铃木淳也 (Junya Suzuki)",
                    "name": "铃木淳也",
                    "pos": "GK/DR",
                    "age": 25,
                    "from_team": "松本山雅足球俱乐部 (日本)",
                    "fee": "转会费签约",
                    "date": "2026-07-24",
                    "wage": "€5,186/周",
                    "contract": "至 2029-06-30"
                },
                {
                    "player": "希尔马 (Jilmar)",
                    "name": "希尔马",
                    "pos": "DC",
                    "age": 31,
                    "from_team": "自由身免签 (前西班牙圣安德鲁)",
                    "fee": "免签 (自由转会)",
                    "date": "2026-07-24",
                    "wage": "€2,135/周",
                    "contract": "至 2028-06-30"
                },
                {
                    "player": "巴巴卡尔·迪奥内 (Babacar Dione)",
                    "name": "巴巴卡尔·迪奥内",
                    "pos": "AML/AMR",
                    "age": 29,
                    "from_team": "自由身免签 (前瓦雷根/穆斯克龙)",
                    "fee": "免签 (自由转会)",
                    "date": "2026-07-19",
                    "wage": "€2,852/周",
                    "contract": "至 2029-06-30"
                },
                {
                    "player": "马林·皮尔伊 (Marin Pilj)",
                    "name": "马林·皮尔伊",
                    "pos": "DM/MC",
                    "age": 29,
                    "from_team": "自由身免签 (克罗地亚前腰/后腰)",
                    "fee": "免签 (自由转会)",
                    "date": "2026-07-19",
                    "wage": "€3,803/周",
                    "contract": "至 2029-06-30"
                },
                {
                    "player": "安德鲁·普里维特 (Andrew Privett)",
                    "name": "安德鲁·普里维特",
                    "pos": "DC",
                    "age": 25,
                    "from_team": "查洛特FC (美职联 MLS)",
                    "fee": "转会费签约",
                    "date": "2026-07-19",
                    "wage": "€4,321/周",
                    "contract": "至 2029-06-30"
                },
                {
                    "player": "马库斯·基希海纳 (Marcus Kirchheiner)",
                    "name": "马库斯·基希海纳",
                    "pos": "MC",
                    "age": 26,
                    "from_team": "自由身免签",
                    "fee": "免签 (自由转会)",
                    "date": "2026-06-19",
                    "wage": "€2,200/周",
                    "contract": "至 2028-06-30"
                }
            ],
            "out": [
                {
                    "player": "比利·库梅蒂奥 (Billy Koumetio)",
                    "name": "比利·库梅蒂奥",
                    "pos": "DC",
                    "age": 23,
                    "to_team": "查尔顿竞技足球俱乐部 (英甲/英冠)",
                    "fee": "转会离队",
                    "date": "2026-07-10"
                },
                {
                    "player": "路易斯·席尔瓦 (Luís Silva)",
                    "name": "路易斯·席尔瓦",
                    "pos": "DC/DM",
                    "age": 27,
                    "to_team": "蒂黑 (GKS Tychy, 波甲同级)",
                    "fee": "转会离队",
                    "date": "2026-07-08"
                },
                {
                    "player": "阿图尔·阿瓦希米扬 (Artur Avahimian)",
                    "name": "阿图尔·阿瓦希米扬",
                    "pos": "MC",
                    "age": 29,
                    "to_team": "马萨特兰足球俱乐部 (墨超)",
                    "fee": "转会离队",
                    "date": "2026-07-02"
                },
                {
                    "player": "卡克佩尔·斯莫林斯基 (Kacper Smoliński)",
                    "name": "卡克佩尔·斯莫林斯基",
                    "pos": "MC",
                    "age": 25,
                    "to_team": "卡尔维纳 (捷克甲)",
                    "fee": "转会离队",
                    "date": "2026-06-30"
                },
                {
                    "player": "马塞尔·皮琴切克 (Marcel Pięczek)",
                    "name": "马塞尔·皮琴切克",
                    "pos": "DL",
                    "age": 24,
                    "to_team": "凯尔采科罗纳足球俱乐部 (波超)",
                    "fee": "免签离队",
                    "date": "2026-06-30"
                },
                {
                    "player": "佩塔尔·博格达诺维奇 (Petar Bogdanović)",
                    "name": "佩塔尔·博格达诺维奇",
                    "pos": "MC",
                    "age": 24,
                    "to_team": "伊万尼察枫树足球俱乐部 (塞尔维亚)",
                    "fee": "转会离队",
                    "date": "2026-07-15"
                },
                {
                    "player": "诺伯特·库齐耶姆斯基 (Norbert Kuziemski)",
                    "name": "诺伯特·库齐耶姆斯基",
                    "pos": "MF",
                    "age": 20,
                    "to_team": "加尔巴尼亚 (Garbarnia Kraków)",
                    "fee": "租借离队",
                    "date": "2026-07-01"
                }
            ]
        }

    # 2. Virton
    virton = next((c for c in clubs if c['id'] == 'virton'), None)
    if virton:
        virton['transfers'] = {
            "in": [
                {
                    "player": "保罗·韦德 (Paul Wade)",
                    "name": "保罗·韦德",
                    "pos": "ST/AML",
                    "age": 26,
                    "from_team": "自由身免签 (前尼斯青训)",
                    "fee": "免签签约",
                    "date": "2026-01-31",
                    "wage": "€1,800/周",
                    "contract": "至 2027-06-30"
                },
                {
                    "player": "泰伦·托明 (Tyrone Tormin)",
                    "name": "泰伦·托明",
                    "pos": "AMR",
                    "age": 25,
                    "from_team": "自由身免签 (前圣埃蒂安青训)",
                    "fee": "免签加盟",
                    "date": "2026-02-12",
                    "wage": "€1,600/周",
                    "contract": "至 2027-06-30"
                },
                {
                    "player": "马克斯·因查德 (Marks Inchaud)",
                    "name": "马克斯·因查德",
                    "pos": "ST",
                    "age": 24,
                    "from_team": "自由身免签",
                    "fee": "免签签约",
                    "date": "2026-02-10",
                    "wage": "€1,400/周",
                    "contract": "至 2027-06-30"
                },
                {
                    "player": "威廉·辛巴 (William Simba)",
                    "name": "威廉·辛巴",
                    "pos": "DM",
                    "age": 25,
                    "from_team": "自由身免签",
                    "fee": "免签签约",
                    "date": "2026-03-06",
                    "wage": "€1,500/周",
                    "contract": "至 2027-06-30"
                }
            ],
            "out": [
                {
                    "player": "马科斯·莫雷诺 (Marcos Moreno)",
                    "name": "马科斯·莫雷诺",
                    "pos": "ST",
                    "age": 22,
                    "to_team": "阿尔瓦塞特 (西班牙西乙)",
                    "fee": "转会离队",
                    "date": "2026-07-01"
                },
                {
                    "player": "曼德拉·维拉卡蒂 (Mandla Vilakati)",
                    "name": "曼德拉·维拉卡蒂",
                    "pos": "MF",
                    "age": 24,
                    "to_team": "西韦莱莱足球俱乐部 (南非超)",
                    "fee": "转会离队",
                    "date": "2026-07-12"
                }
            ]
        }

    with open(FOLLOWED_PATH, 'w', encoding='utf-8') as f:
        json.dump(clubs, f, ensure_ascii=False, indent=2)
    print("Successfully synchronized 100% REAL FM save transfer data into followed_clubs.json!")

if __name__ == '__main__':
    sync_transfers()
