import json
from pathlib import Path
import datetime
import fmsave

SAVE_PATH = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
FOLLOWED_PATH = Path(r"I:\fm26-virton-hub\web\src\data\followed_clubs.json")

ZH_NAME_MAP = {
    # Odra Opole
    "Kacper Przybyłko": "卡克佩尔·普日比乌科",
    "Jordy Soladio": "霍尔迪·索拉迪奥",
    "Patryk Szysz": "帕特里克·西什",
    "Babacar Dione": "巴巴卡尔·迪奥内",
    "Marin Pilj": "马林·皮尔伊",
    "Tomasz Gajda": "托马斯·加伊达",
    "Adrian Liber": "阿德里安·利贝尔",
    "Franciszek Franczak": "弗朗西斯泽克·弗朗恰克",
    "Jilmar": "希尔马",
    "Andrew Privett": "安德鲁·普里维特",
    "Junya Suzuki": "铃木淳也",
    "Mateusz Spychała": "马特乌什·斯皮哈瓦",
    "Krystian Palacz": "克里斯蒂安·帕拉茨",
    "Jakub Szrek": "雅库布·什雷克",
    "Miłosz Mleczko": "米沃什·姆莱奇科",
    "Artur Haluch": "阿尔图尔·哈卢赫",
    "Branislav Spáčil": "布拉尼斯拉夫·斯帕奇尔",
    "Joshua Pérez": "约书亚·佩雷斯",
    "Stanisław Gieroba": "斯坦尼斯瓦夫·吉耶罗巴",
    "Mathieu Scalet": "马修·斯卡莱",
    "Szymon Szkliński": "希蒙·什克林斯基",
    "Szymon Mida": "希蒙·米达",
    "Adam Wójcik": "亚当·沃伊奇克",
    "Jakub Pochcioł": "雅库布·波赫乔乌",
    "Jakub Nykiel": "雅库布·尼克尔",
    "Marcel Białowąs": "马塞尔·比亚沃翁斯",
    "Marcin Staś": "马尔钦·斯塔斯",
    "Nemanja Mijušković": "内马尼亚·米尤斯科维奇",
    "Cássio": "卡西奥",

    # Virton
    "Thomas Vincensini": "托马斯·文森辛尼",
    "Kelyan Cavelier": "凯利安·卡维利耶",
    "Arthur Drouart": "阿瑟·德鲁瓦特",
    "Florian Lesquoy": "弗洛里安·莱斯夸",
    "Srdjan Spiridonovic": "斯尔詹·斯皮里多诺维奇",
    "Baptiste Guillaume": "巴蒂斯特·吉约姆",
    "Karim Cissé": "卡里姆·西塞",
    "Moussa Sylla": "穆萨·西拉",
    "El Haddadi": "埃尔·哈达迪",
    "Paul Wade": "保罗·韦德",
    "Aymeric Amoussou": "艾梅里克·阿莫苏",
    "De Waele": "德瓦勒",
    "Verhulst": "维尔赫斯特",
    "Yanis Lentini": "亚尼斯·伦蒂尼",
    "Maxime Guillaume": "马克西姆·纪尧姆",
    "Sullivan Coulibaly": "沙利文·库利巴利",
    "Allan Tchaptchet": "阿兰·特查普切特",
    "Antoine Valério": "安托万·瓦莱里奥",
    "Aliou Dembélé": "阿卢·登贝莱"
}

NATION_MAP = {
    161: ("波兰", "circle-flags:pl"),
    145: ("德国", "circle-flags:de"),
    200: ("日本", "circle-flags:jp"),
    109: ("法国", "circle-flags:fr"),
    101: ("比利时", "circle-flags:be"),
    102: ("波黑", "circle-flags:ba"),
    110: ("格鲁吉亚", "circle-flags:ge"),
    115: ("爱尔兰", "circle-flags:ie"),
    120: ("科特迪瓦", "circle-flags:ci"),
    124: ("克罗地亚", "circle-flags:hr"),
    140: ("黑山", "circle-flags:me"),
    148: ("葡萄牙", "circle-flags:pt"),
    155: ("塞内加尔", "circle-flags:sn"),
    156: ("斯洛伐克", "circle-flags:sk"),
    159: ("西班牙", "circle-flags:es"),
    164: ("瑞典", "circle-flags:se"),
    165: ("瑞士", "circle-flags:ch"),
    173: ("美国", "circle-flags:us"),
    178: ("巴西", "circle-flags:br"),
    179: ("阿根廷", "circle-flags:ar"),
    183: ("哥伦比亚", "circle-flags:co"),
    772: ("萨尔瓦多", "circle-flags:sv"),
}

def get_pos_label(p):
    nats = getattr(p, 'natural_positions', None) or ()
    if nats:
        first = str(nats[0]).upper()
        if 'GK' in first: return 'GK'
        if 'DR' in first or 'WBR' in first: return 'DR'
        if 'DL' in first or 'WBL' in first: return 'DL'
        if 'DC' in first or 'SW' in first: return 'DC'
        if 'DM' in first: return 'DM'
        if 'MC' in first: return 'MC'
        if 'ML' in first: return 'ML'
        if 'MR' in first: return 'MR'
        if 'AML' in first: return 'AML'
        if 'AMR' in first: return 'AMR'
        if 'AMC' in first: return 'AMC'
        if 'ST' in first: return 'ST'
    pos = getattr(p, 'positions', None)
    if pos:
        if pos.gk >= 15: return 'GK'
        if pos.stc >= 15: return 'ST'
        if pos.amr >= 15: return 'AMR'
        if pos.aml >= 15: return 'AML'
        if pos.amc >= 15: return 'AMC'
        if pos.mc >= 15: return 'MC'
        if pos.dm >= 15: return 'DM'
        if pos.dr >= 15 or pos.wbr >= 15: return 'DR'
        if pos.dl >= 15 or pos.wbl >= 15: return 'DL'
        if pos.dc >= 15: return 'DC'
    return 'MC'

def extract_player_data(p, squad_number):
    raw_name = p.name or p.full_name or "Unknown"
    zh_name = ZH_NAME_MAP.get(raw_name, raw_name)
    nation_info = NATION_MAP.get(p.nation_id, ("欧洲", "circle-flags:eu"))
    pos = get_pos_label(p)

    # Attributes
    attr = p.attributes
    is_gk = (pos == 'GK')

    # Contract & Value
    wage = p.contract.wage if hasattr(p, 'contract') and hasattr(p.contract, 'wage') else 1200
    end_date = str(p.contract.end) if hasattr(p, 'contract') and hasattr(p.contract.end, 'isoformat') else "2027-06-30"
    t_val = getattr(p, 'transfer_value', 100000) or 100000
    val_str = f"€{t_val / 10000:.1f}万" if t_val >= 10000 else f"€{t_val}"

    return {
        "uid": p.uid,
        "number": squad_number,
        "name": raw_name,
        "name_zh": zh_name,
        "name_en": raw_name,
        "age": p.age,
        "height_cm": getattr(p, 'height_cm', 182) or 182,
        "position": pos,
        "natural_positions": [str(x) for x in (getattr(p, 'natural_positions', None) or [pos])],
        "nation": nation_info[0],
        "flag": nation_info[1],
        "market_value": val_str,
        "wage_weekly": f"€{wage:,}/周",
        "contract_until": end_date,
        "ca": getattr(p.ability, 'current', 85) if hasattr(p, 'ability') else 85,
        "pa": getattr(p.ability, 'potential', 120) if hasattr(p, 'ability') else 120,
        "left_foot": getattr(p, 'left_foot', 10) or 10,
        "right_foot": getattr(p, 'right_foot', 20) or 20,
        "attributes": {
            "physical": {
                "acceleration": getattr(attr, 'acceleration', 10),
                "pace": getattr(attr, 'pace', 10),
                "stamina": getattr(attr, 'stamina', 10),
                "strength": getattr(attr, 'strength', 10),
                "jumping_reach": getattr(attr, 'jumping_reach', 10),
                "agility": getattr(attr, 'agility', 10),
                "balance": getattr(attr, 'balance', 10),
                "natural_fitness": getattr(attr, 'natural_fitness', 10)
            },
            "technical": {
                "finishing": getattr(attr, 'finishing', 10),
                "heading": getattr(attr, 'heading', 10),
                "dribbling": getattr(attr, 'dribbling', 10),
                "passing": getattr(attr, 'passing', 10),
                "first_touch": getattr(attr, 'first_touch', 10),
                "technique": getattr(attr, 'technique', 10),
                "tackling": getattr(attr, 'tackling', 10),
                "marking": getattr(attr, 'marking', 10),
                "crossing": getattr(attr, 'crossing', 10),
                "long_shots": getattr(attr, 'long_shots', 10),
                "corners": getattr(attr, 'corners', 10),
                "free_kicks": getattr(attr, 'free_kick_taking', 10),
                "penalty_taking": getattr(attr, 'penalty_taking', 10)
            },
            "mental": {
                "composure": getattr(attr, 'composure', 10),
                "concentration": getattr(attr, 'concentration', 10),
                "decisions": getattr(attr, 'decisions', 10),
                "anticipation": getattr(attr, 'anticipation', 10),
                "vision": getattr(attr, 'vision', 10),
                "work_rate": getattr(attr, 'work_rate', 10),
                "teamwork": getattr(attr, 'teamwork', 10),
                "off_the_ball": getattr(attr, 'off_the_ball', 10),
                "bravery": getattr(attr, 'bravery', 10),
                "aggression": getattr(attr, 'aggression', 10),
                "leadership": getattr(attr, 'leadership', 10),
                "determination": getattr(attr, 'determination', 10),
                "positioning": getattr(attr, 'positioning', 10),
                "flair": getattr(attr, 'flair', 10)
            },
            "goalkeeping": {
                "reflexes": getattr(attr, 'reflexes', 1),
                "one_on_ones": getattr(attr, 'one_on_ones', 1),
                "handling": getattr(attr, 'handling', 1),
                "aerial_reach": getattr(attr, 'aerial_reach', 1),
                "command_of_area": getattr(attr, 'command_of_area', 1),
                "communication": getattr(attr, 'communication', 1),
                "kicking": getattr(attr, 'kicking', 1),
                "throwing": getattr(attr, 'throwing', 1),
                "rushing_out": getattr(attr, 'rushing_out', 1),
                "punching": getattr(attr, 'punching', 1)
            }
        }
    }

def main():
    with open(FOLLOWED_PATH, 'r', encoding='utf-8') as f:
        followed_data = json.load(f)

    with fmsave.open(str(SAVE_PATH)) as save:
        all_players = list(save.players())
        print(f"Total players in save: {len(all_players)}")

        # 1. Odra Opole (club_uid = 129566)
        odra_club = next((c for c in followed_data if c['id'] == 'odra' or c['id'] == 'odra_opole'), None)
        if odra_club:
            odra_fm = [p for p in all_players if p.club_uid == 129566 and getattr(p.ability, 'current', 0) >= 40]
            # sort by CA desc
            odra_fm.sort(key=lambda p: getattr(p.ability, 'current', 0), reverse=True)
            print(f"First team Odra Opole players: {len(odra_fm)}")
            
            squad_list = []
            assigned_nums = set()
            for idx, p in enumerate(odra_fm[:26]):
                num = idx + 1
                squad_list.append(extract_player_data(p, num))
            
            odra_club['squad'] = squad_list

        # 2. Virton (club_uid = 292)
        virton_club = next((c for c in followed_data if c['id'] == 'virton'), None)
        if virton_club:
            virton_fm = [p for p in all_players if p.club_uid == 292]
            virton_fm.sort(key=lambda p: getattr(p.ability, 'current', 0), reverse=True)
            print(f"Virton players: {len(virton_fm)}")
            
            squad_list = []
            for idx, p in enumerate(virton_fm[:24]):
                num = idx + 1
                squad_list.append(extract_player_data(p, num))
            
            virton_club['squad'] = squad_list

    with open(FOLLOWED_PATH, 'w', encoding='utf-8') as f:
        json.dump(followed_data, f, ensure_ascii=False, indent=2)

    print("Successfully built rich squad with real FM attributes into followed_clubs.json!")

if __name__ == '__main__':
    main()
