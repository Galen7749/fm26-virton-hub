import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

def build_community_data():
    return {
        "season_coach_summary": {
            "average_score": 9.2,
            "total_votes": 35600,
            "support_rate": "96.5%",
            "trend_label": "功勋名帅自由身 · 全欧夏窗引援热议",
            "round_scores": []
        },
        "threads": [
            {
                "id": "t_romano_do_scoop",
                "category": "transfer",
                "category_label": "转会中心 · 罗马诺&DO",
                "title": "🚨 罗马诺&DO联合跟进：徐指导正式与维尔通解约！荷乙及法丙两家俱乐部已启动接洽",
                "author": "老特拉福德看门人",
                "avatar": "📱",
                "tag": "曼联球迷",
                "time": "15分钟前",
                "is_hot": True,
                "views": 52400,
                "likes": 8420,
                "content": "刚刷到罗马诺的推特和The Athletic大卫·奥恩斯坦的联合专栏：\n\n“🚨 HERE WE GO！率维尔通在补时90+2绝杀冲甲的中国籍主教练耶稣·徐已与俱乐部协议解约。\n双方决裂主因系管理层推行极端U23建队政策并拒绝老将续约，同时拒绝承担欧足联高阶教练研习班学费。\nDavid Ornstein补充：徐指导团队的求职谈判底线非常明确，俱乐部必须出资担保其参加欧足联UEFA教练认证。荷乙埃因霍温FC及法丙冲乙队已进入接触阶段。”\n\n刚带队升甲就遇到这种过河拆桥的高层，辞职走人确实痛快。大家觉得下一站去哪最靠谱？",
                "reply_count": 586,
                "top_replies": [
                    {
                        "username": "Galen",
                        "tag": "球迷",
                        "content": "带保级弱旅一路轰进70球夺冠升甲，决赛落后时拼命逆转，回头俱乐部把老将全清洗了，连几千块报名费都卡着不给报，这管理层吃相太难看。支持徐指导掀桌子，换个良心队伍才是正道。",
                        "likes": 3280
                    },
                    {
                        "username": "阿森纳今天赢了吗",
                        "tag": "枪迷",
                        "content": "升班马不留骨干老将，全买U23小妖，下赛季比甲大概率是各路豪门提款机，留着也是第一年背锅下课。现在急流勇退，带着奇迹升甲履历在欧洲二级联赛很抢手！",
                        "likes": 2650
                    },
                    {
                        "username": "Kimi_7",
                        "tag": "资深FM玩家",
                        "content": "玩FM的都知道，遇到这种拒绝给老臣续约还卡教练证书的董事会，不辞职留着过年吗？去荷乙吧，荷乙节奏快进攻猛，适合徐指导的短传体系，而且荷兰足协对教练进修特别支持！",
                        "likes": 1940
                    },
                    {
                        "username": "Milanista_1899",
                        "tag": "AC米兰球迷",
                        "content": "零违约金+年轻有战术冲劲，对预算有限但志在冲级的欧洲俱乐部诱惑力太大了。去荷乙或者法丙带青年军，一边拿成绩一边把证考下来最实在。",
                        "likes": 1420
                    }
                ]
            },
            {
                "id": "t_cl_final_debate",
                "category": "matches",
                "category_label": "欧冠决赛",
                "title": "【欧冠决战前瞻】皇马vs曼城：安切洛蒂的杯赛玄学 vs 瓜迪奥拉的极致控球，大耳朵杯花落谁家？",
                "author": "伯纳乌纯白之魂",
                "avatar": "🏆",
                "tag": "皇马球迷",
                "time": "1小时前",
                "is_hot": True,
                "views": 68900,
                "likes": 9120,
                "content": "欧冠决赛明晚打响！BBC和马卡报都在大篇幅前瞻。\n曼城罗德里复出，中场控制力拉满；皇马维尼修斯和贝林厄姆反击刀刀致命。\n大家预测比分是多少？安帅能不能再拿一座大耳朵杯？",
                "reply_count": 724,
                "top_replies": [
                    {
                        "username": "蓝月亮荣耀",
                        "tag": "曼城球迷",
                        "content": "哈兰德今年状态调整得不错，只要中场能顶住皇马第一波压迫，曼城大概率2-1小胜捧杯！",
                        "likes": 2480
                    },
                    {
                        "username": "Kimi_7",
                        "tag": "资深FM玩家",
                        "content": "皇马打欧冠决赛玄学太强了，不到90分钟吹哨不敢下结论，看好拖进加时点球大战！",
                        "likes": 1820
                    }
                ]
            },
            {
                "id": "t_transfermarkt_coaches",
                "category": "coach",
                "category_label": "德转前沿",
                "title": "【德转盘点】今夏欧洲最具性价比自由身教练：除了克洛普图赫尔，带队奇迹升甲的徐指导成二线黑马？",
                "author": "荷甲挖掘机",
                "avatar": "📊",
                "tag": "荷乙老懂哥",
                "time": "3小时前",
                "is_hot": False,
                "views": 32800,
                "likes": 4210,
                "content": "德国转会市场（Transfermarkt）更新了夏窗无合约教练榜单。\n顶级名帅有克洛普、图赫尔等，而在二线联赛性价比一栏中，刚刚带维尔通完成比乙逆转冲甲的徐指导被多国球探提及。\n特点很鲜明：擅长4-1-1-4激进高压短传、激活东亚年轻球员（韩国朴昇秀10助攻+日本吉永梦希稳坐主力）、单赛季轰进70球。最关键的是完全自由身且不争薪资，只要俱乐部提供欧足联考证担保，简直是次级别球队的绝佳人选！",
                "reply_count": 312,
                "top_replies": [
                    {
                        "username": "低调的皮尔洛",
                        "tag": "球迷",
                        "content": "能在欧洲次级联赛打出场均2球以上的进攻，战术肯定有独到之处。期待下一站官宣！",
                        "likes": 1280
                    }
                ]
            },
            {
                "id": "t_national_team_talk",
                "category": "offpitch",
                "category_label": "国内足球观察",
                "title": "【体坛周报】专栏热评：欧洲底层打拼出的奇迹少帅，能否为国内教练培养带来新思路？",
                "author": "国足不进世界杯不改名",
                "avatar": "🇨🇳",
                "tag": "中国足球老粉",
                "time": "5小时前",
                "is_hot": False,
                "views": 27400,
                "likes": 3680,
                "content": "体坛周报欧洲记者今天发了篇深度专栏，探讨徐指导在比利时的执教路径。\n没有国内人脉挂靠，完全凭战术分析和数据能力在欧洲底层起步，带一支身价倒数的升班马打到冲甲。即便因理念分歧辞职，也坚决要求俱乐部提供考证机会继续深造。\n这种脚踏实地走职业技术流的路线，才是真正的足球探索。",
                "reply_count": 245,
                "top_replies": [
                    {
                        "username": "低调的皮尔洛",
                        "tag": "球迷",
                        "content": "说得好！千万别回国内趟浑水，在欧洲二三级联赛慢慢打磨、把欧足联证书一步步考下来，走最纯粹的职业教练路！",
                        "likes": 1560
                    }
                ]
            }
        ]
    }

data = build_community_data()
for p in [DATA_DIR / "season_1" / "community.json", DATA_DIR / "season_2" / "community.json", DATA_DIR / "community.json"]:
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print("Living community forum updated across all data folders!")
