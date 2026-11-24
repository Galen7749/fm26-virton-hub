import json
from pathlib import Path

news_file = Path(r"I:\fm26-virton-hub\web\src\data\season_1\news.json")
news = json.loads(news_file.read_text(encoding="utf-8"))

# Filter out previous epilogue if any
news = [n for n in news if n.get("match_id") != "20260528_season_epilogue"]

epilogue_entry = {
    "match_id": "20260528_season_epilogue",
    "round": 33,
    "date": "2026-05-28",
    "fixture": "维尔通精英 · 季末突发特辑",
    "dongqiudi_article": {
        "title": "💥 突发！刚带维尔通奇迹冲甲，徐指导直接掀桌子辞职了！原因竟然是……",
        "summary": "吃大瓜！比利时媒体曝出惊天内幕，维尔通高层不仅强制推行'只买U23'清洗冲甲老将，甚至连几千欧的欧足联教练班学费都不肯给徐指导报销！徐指导直接当场辞职走人，更衣室直接炸锅！",
        "body": "北京时间5月28日讯，据比利时当地媒体《L'Avenir》与多家体育电台突发爆料，刚刚率领维尔通精英在冲甲附加赛90+2分钟头球绝杀利尔斯、以总比分4-3奇迹升入比甲的中国少帅耶稣·徐，已于今日正式向俱乐部递交辞呈！\n\n【决裂导火索：高层过河拆桥】\n据多位知情人士透露，冲甲狂欢的香槟气味还没散去，维尔通总经理哈凯姆就在办公室找徐指导谈话。董事会明确下达死命令：升入比甲后实行极端的‘年轻化战略’，未来所有引援和续约严格限制在23岁以下！这意味着包括后防定海神针梅扎格在内的多名功勋老将，全部被俱乐部单方面拒绝续约，徐指导在决赛落后时亲口对全队做出的承诺彻底被高层当成了废纸！\n\n【离谱至极：连几千块考证学费都舍不得出？】\n更让人目瞪口呆的是，徐指导至今尚未取得欧足联顶级职业教练证书。为了下赛季征战比甲合规，徐指导向俱乐部申请出面担保并报销下一期欧足联高阶教练研习班——学费不过区区几千欧元。然而总经理哈凯姆竟以‘打比甲开支剧增、财政吃紧’为由当场回绝！\n\n【当场掀桌子：辞职信压在咖啡杯下，直接开润！】\n据了解，面对管理层的算计与背刺，徐指导没有做任何妥协，回更衣室告知大家真相后，当即将一封言辞决绝的辞职信压在了总经理办公桌的咖啡杯下，拎起背包驾车离开了球场。目前包括罗马诺、David Ornstein等欧洲知名媒体人均已跟进报道，维尔通死忠球迷更是群情激愤，全网都在痛骂管理层‘纯纯草台班子过河拆桥’！",
        "tags": [
            "徐指导辞职",
            "维尔通大地震",
            "罗马诺爆料",
            "欧洲教练流言",
            "无证名帅求职"
        ]
    },
    "hupu_thread": {
        "title": "🔥 [流言板] 纯纯卸磨杀驴！曝徐指导带队冲甲后火速辞职：高层清洗功勋老将，连几千块考证费都舍不得出？",
        "coach_score": 10.0,
        "comments": [
            {
                "username": "Galen",
                "tag": "球迷",
                "content": "冲甲决赛0-2落后的时候全队拼命，赢了回头就把功勋老臣踢了，连几千块教练班学费都不给出，这管理层纯纯恶心人。支持徐指导掀桌子，换个良心队伍才是正道。",
                "likes": 6821
            },
            {
                "username": "阿森纳今天赢了吗",
                "tag": "枪迷",
                "content": "走得太对了！升班马不让留老将，全买U23小妖，下赛季比甲大概率是各路豪门提款机，留着也是第一年就被解雇背锅。现在急流勇退，奇迹名帅履历到手！",
                "likes": 5109
            },
            {
                "username": "Kimi_7",
                "tag": "资深FM玩家",
                "content": "玩FM的都知道，遇到这种拒绝给老将续约还卡教练证书的董事会，不辞职留着过年吗？去荷乙吧，荷乙崇尚进攻、比赛节奏快，对主帅考证非常宽容！",
                "likes": 3412
            },
            {
                "username": "老特拉福德吹风机",
                "tag": "曼联球迷",
                "content": "罗马诺和DO都跟进独家了，荷兰法国俱乐部已经有初步接触了，支持徐指导走出来，这破维尔通活该下赛季降级。",
                "likes": 2045
            },
            {
                "username": "诺坎普清洁工",
                "tag": "巴萨球迷",
                "content": "DO在The Athletic也发专栏分析了，说荷乙两家俱乐部已经在联系了，条件就是包办欧足联证书。良禽择木而栖，破维尔通管理层吃相太难看！",
                "likes": 1820
            }
        ]
    }
}

news.append(epilogue_entry)
news_file.write_text(json.dumps(news, ensure_ascii=False, indent=2), encoding="utf-8")
(Path(r"I:\fm26-virton-hub\web\src\data\news.json")).write_text(json.dumps(news, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated news.json successfully. Total items: {len(news)}")
