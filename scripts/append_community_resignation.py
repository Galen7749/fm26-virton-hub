import json
from pathlib import Path

comm_file = Path(r"I:\fm26-virton-hub\web\src\data\season_1\community.json")
comm = json.loads(comm_file.read_text(encoding="utf-8"))

# Remove any old version of this thread
comm["threads"] = [t for t in comm.get("threads", []) if t.get("id") != "t_resignation_earthquake"]

new_thread = {
    "id": "t_resignation_earthquake",
    "category": "coach",
    "category_label": "主帅专区 · 突发大瓜",
    "title": "🔥 [流言板] 纯纯卸磨杀驴！曝徐指导带队冲甲后火速辞职：高层清洗功勋老将，连几千块考证费都舍不得出？",
    "author": "高姆山谷守夜人",
    "avatar": "💣",
    "tag": "全网吃瓜",
    "time": "刚刚",
    "is_hot": True,
    "views": 58900,
    "likes": 9820,
    "content": "兄弟们，今天比利时那边爆了个惊天大瓜！\n\n徐指导刚带维尔通绝杀冲甲，转头就跟高层彻底撕破脸辞职了！\n\n原因简直离谱到家了：\n1. 高层搞了个什么‘23岁以上全不要’的骚操作，梅扎格这些拼到吐血的冲甲老将一个不给续约，直接把徐指导在更衣室的承诺当成了废纸。\n2. 徐指导下赛季打比甲得去考欧足联教练证，学费也就几千欧，高层居然说‘俱乐部没钱，你自己解决’！\n\n刚把一支保级烂队带进顶级联赛，连几千块培训费都不给出？这管理层是真把咱中国人当免费黑工用啊！徐指导直接当场掀桌子，把辞职信压在咖啡杯下开润了！大伙儿怎么看？",
    "reply_count": 988,
    "top_replies": [
        {
            "username": "高姆山谷守夜人",
            "tag": "气到脑梗",
            "content": "我真特么看吐了！几千欧连比甲球场一场球的草皮维护费都不够吧？刚带队升甲，转头连个进修班学费都舍不得出？这狗逼管理层吃相简直难看到家了，纯把咱徐指导当免费黑奴啊！",
            "likes": 6821
        },
        {
            "username": "倒立洗头协会名誉会长",
            "tag": "铁血挺徐",
            "content": "之前还在想老将们续约的事，合着是高层在背后捅刀子！老将拼到吐血换来升级，赢了就搞‘U23全员清洗’？徐指导这波当场掀桌子辞职太爷们了，不伺候这帮短视孙子！",
            "likes": 5109
        },
        {
            "username": "战术显微镜",
            "tag": "理智分析",
            "content": "理性讨论，徐指导这波跑路其实赚麻了。带一支更衣室心态炸裂、又不准买老将的升班马去比甲，大概率开局连败直接背锅下课；现在‘无证奇迹名帅’的名气彻底打响，自由身手里大把筹码，去荷乙或者法丙找个良心老板把证书全包了，前途一片光明！",
            "likes": 3412
        },
        {
            "username": "比利时李毅",
            "tag": "幽默懂哥",
            "content": "笑死，维尔通这波属于捡了芝麻丢了西瓜。没了徐指导的Tiki-Taka大巴车，下赛季比甲保底被安德莱赫特和布鲁日打出翔来。徐指导赶紧开润，FM玩家都知道，这时候投荷乙中上游简历随便过的！",
            "likes": 2045
        },
        {
            "username": "巴黎在逃球探",
            "tag": "内部消息",
            "content": "荷乙那边已经有两家俱乐部在打听徐指导了，人家明确表示只要肯来，UEFA A级培训班名额直接奉上！良禽择木而栖，破维尔通活该下赛季降级！",
            "likes": 1820
        }
    ]
}

comm["threads"].insert(0, new_thread)
comm_file.write_text(json.dumps(comm, ensure_ascii=False, indent=2), encoding="utf-8")
(Path(r"I:\fm26-virton-hub\web\src\data\community.json")).write_text(json.dumps(comm, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated community.json with netizen-style threads!")
