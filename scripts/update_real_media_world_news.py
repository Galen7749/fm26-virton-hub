import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

# 1. WORLD NEWS: Diverse domestic & international reputable media
world_news_data = [
    {
        "id": "wn_romano_001",
        "league": "Fabrizio Romano · 独家",
        "time": "15分钟前",
        "title": "🚨 罗马诺：徐指导已正式与维尔通解除合同！荷乙及法丙两队迅速展开接触",
        "summary": "Fabrizio Romano独家报道：“🚨 HERE WE GO！率维尔通在补时绝杀冲入比甲的32岁中国少帅耶稣·徐今日与俱乐部达成解约协议。管理层推行U23战略并缩减教练培养预算促成双方决裂。荷乙埃因霍温FC与法丙劲旅已向其经纪团队递交执教意向书。”"
    },
    {
        "id": "wn_ornstein_002",
        "league": "The Athletic · DO专栏",
        "time": "1小时前",
        "title": "大卫·奥恩斯坦：自由身主帅徐引多队评估，合同核心谈判点锁定欧足联证书资助",
        "summary": "The Athletic名记David Ornstein报道：自由身教头徐成为欧洲二线联赛夏窗重点考察对象。据悉其谈判底线明确要求俱乐部全额资助其参加欧足联UEFA高阶教练培训，相关意向俱乐部正对此项条款进行财务与法务核准。"
    },
    {
        "id": "wn_lequipe_003",
        "league": "法国《队报》· L'Équipe",
        "time": "3小时前",
        "title": "法甲与法丙夏窗前瞻：多支冲乙与中游球队换帅在即，传控高压打法备受青睐",
        "summary": "《队报》分析：法国联赛今夏掀起战术年轻化风潮。法丙冲乙集团积极关注在邻国比利时联赛打出快速反抢风格的新锐少帅，包括刚刚以场均超2球攻击力升甲的中国籍教练。"
    },
    {
        "id": "wn_bbc_004",
        "league": "BBC 体育 · 欧冠聚焦",
        "time": "4小时前",
        "title": "欧冠决赛倒计时：曼城迎战皇马，瓜迪奥拉确认罗德里首发出战",
        "summary": "BBC现场报道：2026欧冠决战一触即发。瓜迪奥拉在赛前发布会上表示全队已做好应对高强度反击的准备；安切洛蒂则称皇马在欧冠赛场具备独一无二的胜者DNA。"
    },
    {
        "id": "wn_titan_005",
        "league": "《体坛周报》· 留洋专栏",
        "time": "6小时前",
        "title": "体坛独家：中国少帅欧洲执教首季完美升甲后功成身退，足协内部高度关注",
        "summary": "《体坛周报》欧洲特派专稿：耶稣·徐在比利时低级别联赛的执教奇迹不仅震动欧洲足坛，也引来国内足球界的广泛讨论。据悉足协多位元老对其坚持在欧洲底层打拼并严格要求深造的态度给予高度评价。"
    },
    {
        "id": "wn_kicker_006",
        "league": "德国《踢球者》· Kicker",
        "time": "昨天",
        "title": "德转夏窗自由身教练评级：除克洛普、图赫尔外，次级别黑马少帅引多国球探研讨",
        "summary": "Kicker转会专栏：德国转会市场网公布最新无合约主教练评估报告，重点提到了刚刚辞职的维尔通升甲主帅，称其4-1-1-4在有限预算下的破局能力具有极高战术参考价值。"
    }
]

# Write to season_1, season_2, and root
(DATA_DIR / "season_1" / "world_news.json").write_text(json.dumps(world_news_data, ensure_ascii=False, indent=2), encoding="utf-8")
(DATA_DIR / "season_2" / "world_news.json").write_text(json.dumps(world_news_data, ensure_ascii=False, indent=2), encoding="utf-8")
(DATA_DIR / "world_news.json").write_text(json.dumps(world_news_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("World news updated with BBC, L'Équipe, Romano, DO, 体坛周报, Kicker.")
