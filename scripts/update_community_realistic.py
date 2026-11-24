import json
from pathlib import Path

comm_file = Path(r"I:\fm26-virton-hub\web\src\data\season_1\community.json")
comm = json.loads(comm_file.read_text(encoding="utf-8"))

# Replace threads with realistic, authentic netizen & media discussions
comm["threads"] = [
    {
        "id": "t_romano_exclusive",
        "category": "coach",
        "category_label": "名记爆料 · 转会流言",
        "title": "🚨【罗马诺Here we go】徐指导已正式与维尔通解约！下家直接锁定荷乙/法丙？",
        "author": "米兰圈搬运工",
        "avatar": "📱",
        "tag": "转会速递",
        "time": "10分钟前",
        "is_hot": True,
        "views": 48200,
        "likes": 7820,
        "content": "刚刷到罗马诺的推特：\n\n“🚨 EXCLUSIVE: Chinese manager Jesus Xu has officially parted ways with RE Virton following historic promotion to Belgian Jupiler Pro League.\n\nUnderstand decision was made after board insisted on radical U-23 only squad policy and refused to sponsor his UEFA Pro/A coaching license course.\n\nSeveral clubs from Dutch Eerste Divisie and French Championnat National have already approached his camp. Here we go confirmed.”\n\n连罗马诺都发Here we go了，看来事情完全实锤了！大家怎么看这波操作？",
        "reply_count": 512,
        "top_replies": [
            {
                "username": "Galen",
                "tag": "球迷",
                "content": "冲甲决赛0-2落后的时候全队拼命，赢了回头就把功勋老臣踢了，连几千块教练班学费都不给出，这管理层纯纯恶心人。支持徐指导掀桌子，换个良心队伍才是正道。",
                "likes": 3280
            },
            {
                "username": "阿森纳今天赢了吗",
                "tag": "枪迷",
                "content": "走得太对了！升班马不让留老将，全买U23小妖，下赛季比甲大概率是各路豪门提款机，留着也是第一年就被解雇背锅。现在急流勇退，奇迹名帅履历到手！",
                "likes": 2650
            },
            {
                "username": "Kimi_7",
                "tag": "资深FM玩家",
                "content": "玩FM的都知道，遇到这种拒绝给老将续约还卡教练证书的董事会，不辞职留着过年吗？去荷乙吧，荷乙崇尚进攻、比赛节奏快，对主帅考证非常宽容！",
                "likes": 1940
            },
            {
                "username": "诺坎普清洁工",
                "tag": "巴萨球迷",
                "content": "The Athletic的DO也发文了，说荷兰两家俱乐部已经在联系了，条件就是包办欧足联证书。破维尔通高层这下真是自作聪明，下赛季比甲见真章吧。",
                "likes": 1420
            }
        ]
    },
    {
        "id": "t_tactics_depth",
        "category": "tactics",
        "category_label": "战术研讨",
        "title": "【深度复盘】常规赛到冲甲决赛全复盘：徐指导这套 4-1-1-4 双前锋强攻流到底强在哪？",
        "author": "战术显微镜",
        "avatar": "🔍",
        "tag": "战术观察",
        "time": "昨天",
        "is_hot": False,
        "views": 21500,
        "likes": 1980,
        "content": "从常规赛后半程的连续大胜，到冲甲决赛次回合4-1狂胜利尔斯，徐指导的战术思路非常清晰：\n1. 放弃中场无意义缠斗，单后腰德隆负责中路第一道拦截；\n2. 朴昇秀与托明两翼齐飞，兼具速度与突破传中能力；\n3. 韦德作为高支点压迫对方双中卫，给因查德和哈切姆创造肋部插上空当。\n这套打法在次级别联赛极具冲击力。去到新东家只要中锋支点立得住，随时可以复制成功经验！",
        "reply_count": 218,
        "top_replies": [
            {
                "username": "Milanista_1899",
                "tag": "AC米兰球迷",
                "content": "前场跑动和反抢确实狠，冲甲决战次回合前场逼抢把利尔斯后卫都逼得直接开大脚出界了，战术执行力很到位。",
                "likes": 512
            }
        ]
    },
    {
        "id": "t_kante_boss",
        "category": "offpitch",
        "category_label": "场外日常",
        "title": "【球迷现场】维尔通死忠会在市政厅外抗议：要求高层对主帅及功臣离队作出说明",
        "author": "低调的皮尔洛",
        "avatar": "☕",
        "tag": "欧洲足球观察",
        "time": "2天前",
        "is_hot": False,
        "views": 15600,
        "likes": 1680,
        "content": "据当地球迷社群消息，今天下午已有两百多名维尔通死忠球迷聚集在球场外抗议。大家对好不容易拼下的比甲资格却在休赛期第一周就闹出教练组解体感到极度失望，多位老球迷已表示将抵制购买新赛季套票。",
        "reply_count": 182,
        "top_replies": [
            {
                "username": "老特拉福德吹风机",
                "tag": "曼联球迷",
                "content": "升班马第一年最重要的就是更衣室稳定和军心，这么搞简直是自废武功，拭目以待新赛季比甲表现吧。",
                "likes": 420
            }
        ]
    }
]

comm_file.write_text(json.dumps(comm, ensure_ascii=False, indent=2), encoding="utf-8")
(Path(r"I:\fm26-virton-hub\web\src\data\community.json")).write_text(json.dumps(comm, ensure_ascii=False, indent=2), encoding="utf-8")
print("Cleaned up and upgraded season_1 community.json successfully!")
