"""
真实转会同步脚本 (sync_real_transfers.py)
严格执行三项铁律：
1. 统一采用 CURRENCY_MULTIPLIER 汇率换算；
2. 严禁拿 transfer_value 冒充实际成交转会费（免签标'免签'、租借标'租借'、未确认普通转会标'估值 €XX万'）；
3. 优先读取 manual_overrides 手动/截图覆写数据，永不覆盖已确认真实转会费。
"""

import json
import sys
from pathlib import Path

# 添加当前目录以导入 transfer_config
sys.path.append(str(Path(__file__).parent))
from transfer_config import (
    CURRENCY_MULTIPLIER,
    resolve_fee,
    format_market_value,
    format_weekly_wage,
    TRANSFERS_JSON_PATH,
    FOLLOWED_PATH,
    STANDINGS_PATH,
)

def sync_transfers():
    with open(FOLLOWED_PATH, 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    # 1. 奥波莱奥德拉 (Odra Opole)
    odra = next((c for c in clubs if c['id'] in ['odra', 'odra_opole']), None)
    if odra:
        raw_odra_in = [
            {
                "player": "霍尔迪·索拉迪奥 (Jordy Soladio)",
                "name": "霍尔迪·索拉迪奥",
                "pos": "ST",
                "age": 28,
                "from_team": "自由身免签 (旧海弗莱鲁汶青训)",
                "raw_tval": 220429,
                "type": "free",
                "date": "2026-07-24",
                "raw_wage": 5186,
                "contract": "至 2029-06-30"
            },
            {
                "player": "铃木淳也 (Junya Suzuki)",
                "name": "铃木淳也",
                "pos": "DR/WBR",
                "age": 30,
                "from_team": "松本山雅足球俱乐部 (日本)",
                "raw_tval": 492632,
                "type": "fee",
                "date": "2026-07-24",
                "raw_wage": 5186,
                "contract": "至 2029-06-30"
            },
            {
                "player": "希尔马 (Jilmar)",
                "name": "希尔马",
                "pos": "DC",
                "age": 31,
                "from_team": "自由身免签 (前西班牙圣安德鲁)",
                "raw_tval": 314559,
                "type": "free",
                "date": "2026-07-24",
                "raw_wage": 2135,
                "contract": "至 2028-06-30"
            },
            {
                "player": "巴巴卡尔·迪奥内 (Babacar Dione)",
                "name": "巴巴卡尔·迪奥内",
                "pos": "AML/AMR",
                "age": 29,
                "from_team": "自由身免签 (前瓦雷根/穆斯克龙)",
                "raw_tval": 172743,
                "type": "free",
                "date": "2026-07-19",
                "raw_wage": 2852,
                "contract": "至 2029-06-30"
            },
            {
                "player": "马林·皮尔伊 (Marin Pilj)",
                "name": "马林·皮尔伊",
                "pos": "DM/MC",
                "age": 29,
                "from_team": "自由身免签 (克罗地亚前腰/后腰)",
                "raw_tval": 436392,
                "type": "free",
                "date": "2026-07-19",
                "raw_wage": 3803,
                "contract": "至 2029-06-30"
            },
            {
                "player": "安德鲁·普里维特 (Andrew Privett)",
                "name": "安德鲁·普里维特",
                "pos": "DC",
                "age": 25,
                "from_team": "查洛特FC (美职联 MLS)",
                "raw_tval": 564878,
                "type": "fee",
                "date": "2026-07-19",
                "raw_wage": 4321,
                "contract": "至 2029-06-30"
            },
            {
                "player": "马库斯·基希海纳 (Marcus Kirchheiner)",
                "name": "马库斯·基希海纳",
                "pos": "MC",
                "age": 26,
                "from_team": "自由身免签",
                "raw_tval": 13335,
                "type": "free",
                "date": "2026-06-19",
                "raw_wage": 2200,
                "contract": "至 2028-06-30"
            }
        ]

        raw_odra_out = [
            {
                "player": "比利·库梅蒂奥 (Billy Koumetio)",
                "name": "比利·库梅蒂奥",
                "pos": "DC",
                "age": 23,
                "to_team": "查尔顿竞技足球俱乐部 (英冠/英甲)",
                "raw_tval": 2658962,
                "type": "fee",
                "date": "2026-07-10"
            },
            {
                "player": "路易斯·席尔瓦 (Luís Silva)",
                "name": "路易斯·席尔瓦",
                "pos": "DC/DM",
                "age": 27,
                "to_team": "蒂黑 (GKS Tychy, 波甲同级)",
                "raw_tval": 22299,
                "type": "fee",
                "date": "2026-07-08"
            },
            {
                "player": "阿图尔·阿瓦希米扬 (Artur Avahimian)",
                "name": "阿图尔·阿瓦希米扬",
                "pos": "MC",
                "age": 29,
                "to_team": "马萨特兰足球俱乐部 (墨超)",
                "raw_tval": 2072621,
                "type": "fee",
                "date": "2026-07-02"
            },
            {
                "player": "卡克佩尔·斯莫林斯基 (Kacper Smoliński)",
                "name": "卡克佩尔·斯莫林斯基",
                "pos": "MC",
                "age": 25,
                "to_team": "卡尔维纳 (捷克甲)",
                "raw_tval": 201176,
                "type": "fee",
                "date": "2026-06-30"
            },
            {
                "player": "马塞尔·皮琴切克 (Marcel Pięczek)",
                "name": "马塞尔·皮琴切克",
                "pos": "DL",
                "age": 24,
                "to_team": "凯尔采科罗纳足球俱乐部 (波超)",
                "raw_tval": 351027,
                "type": "free",
                "date": "2026-06-30"
            },
            {
                "player": "佩塔尔·博格达诺维奇 (Petar Bogdanović)",
                "name": "佩塔尔·博格达诺维奇",
                "pos": "MC",
                "age": 24,
                "to_team": "伊万尼察枫树足球俱乐部 (塞尔维亚)",
                "raw_tval": 156660,
                "type": "fee",
                "date": "2026-07-15"
            },
            {
                "player": "诺伯特·库齐耶姆斯基 (Norbert Kuziemski)",
                "name": "诺伯特·库齐耶姆斯基",
                "pos": "MF",
                "age": 20,
                "to_team": "加尔巴尼亚 (Garbarnia Kraków)",
                "raw_tval": 8371,
                "type": "loan",
                "date": "2026-07-01"
            }
        ]

        odra_transfers_in = []
        for item in raw_odra_in:
            fee_label = resolve_fee(
                player_name=item["name"],
                club_id="odra",
                direction="in",
                raw_tval=item["raw_tval"],
                default_from_team=item["from_team"],
                default_type=item["type"]
            )
            odra_transfers_in.append({
                "player": item["player"],
                "name": item["name"],
                "pos": item["pos"],
                "age": item["age"],
                "from_team": item["from_team"],
                "fee": fee_label,
                "date": item["date"],
                "wage": format_weekly_wage(item["raw_wage"]),
                "contract": item["contract"]
            })

        odra_transfers_out = []
        for item in raw_odra_out:
            fee_label = resolve_fee(
                player_name=item["name"],
                club_id="odra",
                direction="out",
                raw_tval=item["raw_tval"],
                default_from_team=item["to_team"],
                default_type=item["type"]
            )
            odra_transfers_out.append({
                "player": item["player"],
                "name": item["name"],
                "pos": item["pos"],
                "age": item["age"],
                "to_team": item["to_team"],
                "fee": fee_label,
                "date": item["date"]
            })

        odra['transfers'] = {
            "in": odra_transfers_in,
            "out": odra_transfers_out
        }

    # 2. 维尔通精英 (R.E. Virton)
    virton = next((c for c in clubs if c['id'] == 'virton'), None)
    if virton:
        raw_virton_in = [
            {
                "player": "保罗·韦德 (Paul Wade)",
                "name": "保罗·韦德",
                "pos": "ST/AML",
                "age": 26,
                "from_team": "自由身免签 (前尼斯青训)",
                "raw_tval": 180000,
                "type": "free",
                "date": "2026-01-31",
                "raw_wage": 1800,
                "contract": "至 2027-06-30"
            },
            {
                "player": "泰伦·托明 (Tyrone Tormin)",
                "name": "泰伦·托明",
                "pos": "AMR",
                "age": 25,
                "from_team": "自由身免签 (前圣埃蒂安青训)",
                "raw_tval": 160000,
                "type": "free",
                "date": "2026-02-12",
                "raw_wage": 1600,
                "contract": "至 2027-06-30"
            },
            {
                "player": "马克斯·因查德 (Marks Inchaud)",
                "name": "马克斯·因查德",
                "pos": "ST",
                "age": 24,
                "from_team": "自由身免签",
                "raw_tval": 140000,
                "type": "free",
                "date": "2026-02-10",
                "raw_wage": 1400,
                "contract": "至 2027-06-30"
            },
            {
                "player": "威廉·辛巴 (William Simba)",
                "name": "威廉·辛巴",
                "pos": "DM",
                "age": 25,
                "from_team": "自由身免签",
                "raw_tval": 150000,
                "type": "free",
                "date": "2026-03-06",
                "raw_wage": 1500,
                "contract": "至 2027-06-30"
            }
        ]

        raw_virton_out = [
            {
                "player": "马科斯·莫雷诺 (Marcos Moreno)",
                "name": "马科斯·莫雷诺",
                "pos": "ST",
                "age": 22,
                "to_team": "阿尔瓦塞特 (西班牙西乙)",
                "raw_tval": 443338,
                "type": "fee",
                "date": "2026-07-01"
            },
            {
                "player": "曼德拉·维拉卡蒂 (Mandla Vilakati)",
                "name": "曼德拉·维拉卡蒂",
                "pos": "MF",
                "age": 24,
                "to_team": "西韦莱莱足球俱乐部 (南非超)",
                "raw_tval": 18876,
                "type": "fee",
                "date": "2026-07-12"
            }
        ]

        virton_transfers_in = []
        for item in raw_virton_in:
            fee_label = resolve_fee(
                player_name=item["name"],
                club_id="virton",
                direction="in",
                raw_tval=item["raw_tval"],
                default_from_team=item["from_team"],
                default_type=item["type"]
            )
            virton_transfers_in.append({
                "player": item["player"],
                "name": item["name"],
                "pos": item["pos"],
                "age": item["age"],
                "from_team": item["from_team"],
                "fee": fee_label,
                "date": item["date"],
                "wage": format_weekly_wage(item["raw_wage"]),
                "contract": item["contract"]
            })

        virton_transfers_out = []
        for item in raw_virton_out:
            fee_label = resolve_fee(
                player_name=item["name"],
                club_id="virton",
                direction="out",
                raw_tval=item["raw_tval"],
                default_from_team=item["to_team"],
                default_type=item["type"]
            )
            virton_transfers_out.append({
                "player": item["player"],
                "name": item["name"],
                "pos": item["pos"],
                "age": item["age"],
                "to_team": item["to_team"],
                "fee": fee_label,
                "date": item["date"]
            })

        virton['transfers'] = {
            "in": virton_transfers_in,
            "out": virton_transfers_out
        }

    with open(FOLLOWED_PATH, 'w', encoding='utf-8') as f:
        json.dump(clubs, f, ensure_ascii=False, indent=2)

    # 3. 同步更新 standings_multi.json 中的波甲转会动态，保持数据完全一致
    if STANDINGS_PATH.exists():
        with open(STANDINGS_PATH, 'r', encoding='utf-8') as sf:
            sdata = json.load(sf)
        
        leagues_list = sdata.get('leagues', []) if isinstance(sdata, dict) else sdata
        pol_league = next((lg for lg in leagues_list if lg.get('key') == 'pol_d1'), None)
        if pol_league and 'transfers' in pol_league:
            for tr in pol_league['transfers']:
                p_name = tr.get('player', '')
                if '索拉迪奥' in p_name or '希尔马' in p_name:
                    tr['fee'] = '免签'
                elif '铃木淳也' in p_name:
                    tr['fee'] = resolve_fee('铃木淳也', 'odra', 'in', raw_tval=492632)
                elif '普里维特' in p_name:
                    tr['fee'] = resolve_fee('安德鲁·普里维特', 'odra', 'in', raw_tval=564878)
            with open(STANDINGS_PATH, 'w', encoding='utf-8') as sf:
                json.dump(sdata, sf, ensure_ascii=False, indent=2)

    print("Successfully synchronized 100% REAL transfers with CURRENCY_MULTIPLIER and manual_overrides support!")

if __name__ == '__main__':
    sync_transfers()
