import json
from pathlib import Path

COMM_PATH = Path(r"I:\fm26-virton-hub\web\src\data\community.json")
comm = json.loads(COMM_PATH.read_text(encoding="utf-8"))

epic_threads = [
    {
      "id": 101,
      "title": "【载入史册！总比分4-3绝杀冲甲！】首回合0-2濒死绝境，次回合4-1惊天大反扑！因查德戴帽封神，全城无眠狂欢！",
      "author": "卢森堡边境现场球迷",
      "avatar": "🦁",
      "tag": "冲场见证者",
      "time": "刚刚",
      "category": "matches",
      "category_label": "比赛复盘",
      "content": "兄弟们！我就在伊万·乔治球场现场！当主裁判吹响终场哨的那一刻，上千名球迷直接冲进了球场！把徐指导和因查德高高抛向空中！首回合客场0-2几乎把我们逼入死地，所有媒体都看好利尔斯升级。但今晚，徐指导排出4-1-1-4双前锋狂攻体系，因查德单场狂轰3球帽子戏法，哈切姆打入关键一球，第84分钟神换人阿森盖替补压哨助攻！总比分4-3压哨绝杀！这就是足球！这就是奇迹！下赛季我们就是比甲球队了！！！",
      "views": 28450,
      "likes": 5620,
      "reply_count": 892,
      "is_hot": True,
      "top_replies": [
        {
          "user": "十年徐帅老死忠",
          "content": "满分！10分！中国教练带欧洲球队升入顶级联赛，载入中国足球与比利时足球史册的神迹！",
          "likes": 1820
        },
        {
          "user": "坎特私人理财师",
          "content": "坎特在看台上直接抱着徐指导热泪盈眶！不仅当场宣布发放全队百万巨额奖金，还承诺下赛季比甲全面注资引援！",
          "likes": 1560
        }
      ]
    },
    {
      "id": 102,
      "title": "【比乙官方终极表彰】双冠王霸榜！哈切姆21球荣获金靴，朴昇秀10助夺助攻王！因查德决胜战戴帽9.8分！",
      "author": "比乙数据权威分析师",
      "avatar": "⚽",
      "tag": "官方观察员",
      "time": "1小时前",
      "category": "tactics",
      "category_label": "硬核战术",
      "content": "本赛季比利时挑战者联赛全部奖项出炉：\n1. 官方金靴射手王：哈切姆（维尔通精英）· 21球（领先第2名多达7球，断档领跑！）\n2. 官方助攻王：朴昇秀（维尔通精英）· 10助攻（21场送出10次致命直塞！）\n3. 冲甲附加赛MVP：马克斯·因查德（决赛次回合帽子戏法+9.8分封神）！\n徐指导打造的4-1-1-4双前锋立体压迫体系，全赛季狂轰70球，全比乙进攻火力第一无可争议！",
      "views": 19800,
      "likes": 3480,
      "reply_count": 412,
      "is_hot": True,
      "top_replies": [
        {
          "user": "韩国足球欧陆观察哨",
          "content": "朴昇秀在徐指导手下打出两双数据（6球10助攻），助攻王到手！韩国足协国家队教练已经买机票飞来看他了！",
          "likes": 980
        },
        {
          "user": "哈切姆金靴护送团",
          "content": "哈切姆21球力压全联盟，25场80次射门进21球，转化率极高！五大联赛保级队球探已经踏破俱乐部大门了！",
          "likes": 840
        }
      ]
    },
    {
      "id": 103,
      "title": "【比甲新纪元前瞻】从比乙升班马直接跃升顶级豪门舞台！下赛季直面安德莱赫特、布鲁日、根特等欧冠级别劲旅！",
      "author": "欧洲足球前线特派员",
      "avatar": "🏆",
      "tag": "特派观察员",
      "time": "2小时前",
      "category": "coach",
      "category_label": "主帅帅位",
      "content": "谁能想到一年之前，维尔通还在比利时第三级别联赛挣扎；一年之后，在中国籍少帅耶稣·徐与投资人坎特的带领下，球队以升班马姿态豪取比乙亚军，并一路从冲甲附加赛杀进比利时顶级联赛（比甲 / Jupiler Pro League）！下赛季，伊万·乔治球场将迎来安德莱赫特、皇家布鲁日、根特等欧冠级豪门的检验！中国籍主帅将在欧洲顶级联赛指点江山！",
      "views": 16400,
      "likes": 2890,
      "reply_count": 328,
      "is_hot": False,
      "top_replies": [
        {
          "user": "比利时留学生小林",
          "content": "下赛季主场对布鲁日和安德莱赫特的季票我买定了！支持徐指导在比甲掀翻传统豪强！",
          "likes": 760
        }
      ]
    }
]

comm["threads"] = epic_threads + comm.get("threads", [])
COMM_PATH.write_text(json.dumps(comm, ensure_ascii=False, indent=2), encoding="utf-8")
print("[✓] community.json 论坛新增 3 篇冲甲绝杀热帖！")
