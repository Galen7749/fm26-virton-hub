"""
全面同步资讯 (ticker_matches.json, news_articles.json) 和社区 (community_posts.json) 到第7轮 (2026-08-30)
"""
import json, os

DATA_DIR = r"I:\fm26-virton-hub\web\src\data"

# ============================================================
# 1. 更新 ticker_matches.json (顶部焦点战报滚动卡片)
# ============================================================
ticker_path = os.path.join(DATA_DIR, "ticker_matches.json")
new_tickers = [
  {
    "id": "ticker_odra_07",
    "match_id": 1007,
    "league": "波甲",
    "league_short": "波甲第7轮",
    "status": "FT",
    "time": "完赛",
    "is_overseas": True,
    "home_team": "奥波莱奥德拉",
    "home_logo": "",
    "away_team": "扎布热戈尔尼克",
    "away_logo": "",
    "score_home": 4,
    "score_away": 3,
    "highlights": "83'索拉迪奥双响+卡克佩尔传射 · 4-3逆转7轮不败领跑波甲",
    "home_code": "ODR",
    "away_code": "ZAG",
    "home_color": "#dc2626",
    "away_color": "#2563eb",
    "league_flag": "circle-flags:pl"
  },
  {
    "id": "ticker_odra_06",
    "match_id": 1006,
    "league": "波甲",
    "league_short": "波甲第6轮",
    "status": "FT",
    "time": "完赛",
    "is_overseas": True,
    "home_team": "弗罗茨瓦夫西里西亚",
    "home_logo": "",
    "away_team": "奥波莱奥德拉",
    "away_logo": "",
    "score_home": 0,
    "score_away": 1,
    "highlights": "61'卡克佩尔世界波 · 姆莱奇科7扑零封强敌",
    "home_code": "SLA",
    "away_code": "ODR",
    "home_color": "#16a34a",
    "away_color": "#dc2626",
    "league_flag": "circle-flags:pl"
  },
  {
    "id": "ticker_odra_05",
    "match_id": 1005,
    "league": "波甲",
    "league_short": "波甲第5轮",
    "status": "FT",
    "time": "完赛",
    "is_overseas": True,
    "home_team": "奥波莱奥德拉",
    "home_logo": "",
    "away_team": "罗兹维泽夫",
    "away_logo": "",
    "score_home": 4,
    "score_away": 0,
    "highlights": "索拉迪奥双响+帕拉茨2助 · 主场狂扫强敌",
    "home_code": "ODR",
    "away_code": "WID",
    "home_color": "#dc2626",
    "away_color": "#b91c1c",
    "league_flag": "circle-flags:pl"
  },
  {
    "id": "ticker_pol_big_07",
    "match_id": 2007,
    "league": "波甲",
    "league_short": "波甲第7轮",
    "status": "FT",
    "time": "完赛",
    "is_overseas": False,
    "home_team": "华沙莱吉亚",
    "home_logo": "",
    "away_team": "克拉科维亚",
    "away_logo": "",
    "score_home": 2,
    "score_away": 1,
    "highlights": "次席争夺战 · 莱吉亚力克克拉科维亚紧追榜首",
    "home_code": "LEG",
    "away_code": "CRA",
    "home_color": "#15803d",
    "away_color": "#e11d48",
    "league_flag": "circle-flags:pl"
  }
]

with open(ticker_path, "w", encoding="utf-8") as f:
    json.dump(new_tickers, f, ensure_ascii=False, indent=2)
print("✅ ticker_matches.json updated to Round 7")

# ============================================================
# 2. 更新 news_articles.json (资讯头条与专区新闻)
# ============================================================
news_path = os.path.join(DATA_DIR, "news_articles.json")
new_articles = [
  {
    "id": "news_odra_r7_win",
    "category": "overseas",
    "is_overseas": True,
    "is_headline": True,
    "title": "七球惊天对飚！奥波莱4-3逆转扎布热戈尔尼克，豪取七轮不败积19分独占波甲榜首！",
    "source": "懂球云 · 特派记者",
    "author": "张晨",
    "time": "刚刚",
    "date": "2026-08-30",
    "reads": "285,400",
    "comments_count": 2180,
    "tag": "留洋头条",
    "summary": "波甲第7轮迎来本赛季最震撼的进攻大战！索拉迪奥梅开二度，普日比乌科单场1球2助攻获9.4分MVP，中国主帅率队4-3力克扎布热戈尔尼克，7战6胜1平积19分独占波甲榜首！",
    "content": "北京时间8月30日晚，波兰甲级联赛第7轮展开强强碰撞。奥波莱市政球场涌入满场球迷，现场见证了一场载入史册的七球进球大战！\n\n比赛开局第11分钟，普日比乌科中场精妙直塞，索拉迪奥冷静推射近角得手；第29分钟多恩科尔右路精准弧线传中，伊安诺尼抢点头槌破门！客队随后展现顽强韧性在上半场补时连扳两球。下半场双方彻底进入白热化对攻，第58分钟普日比乌科禁区乱战补射得手，随后扎布热再度扳平。关键的第83分钟，索拉迪奥接多恩科尔低平横扫推射入网锁定4-3！\n\n全场哨响，奥波莱奥德拉以4-3逆转豪取7轮不败（6胜1平0负），积分达到19分，力压传统豪门华沙莱吉亚独占波兰甲级联赛积分榜首位！中国籍主帅耶稣·徐率领的奥波莱已成为本赛季波兰足坛最具轰动效应的超级黑马！"
  },
  {
    "id": "news_odra_r6_win",
    "category": "overseas",
    "is_overseas": True,
    "is_headline": False,
    "title": "客场铁防！姆莱奇科7次神扑卡克佩尔世界波，奥波莱客场1-0力克西里西亚",
    "source": "波兰《体育评论报》· Przegląd Sportowy",
    "author": "Tomasz Włodarczyk",
    "time": "7天前",
    "date": "2026-08-23",
    "reads": "194,000",
    "comments_count": 1420,
    "tag": "留洋战报",
    "summary": "客场铁血防守展现冠军韧性！门将姆莱奇科全场奉献7次关键扑救力保球门不失，卡克佩尔第61分钟世界波一击制胜，奥波莱客场1-0力克西里西亚继续高歌猛进！",
    "content": "在8月23日进行的波甲第6轮角逐中，奥波莱奥德拉做客挑战弗罗茨瓦夫西里西亚。面对主队全场狂轰滥炸，主力门将米沃什·姆莱奇科（Miłosz Mleczko）化身叹息之墙，完成惊人的7次门线救险！下半场第61分钟，阿德里安·利贝尔边路策动，卡克佩尔·普日比乌科禁区弧顶拔脚怒射轰出世界波直挂死角。奥波莱客场1-0全身而退，攻防两端的极高纪律性引发波兰足坛广泛称赞。"
  },
  {
    "id": "news_odra_r5_win",
    "category": "overseas",
    "is_overseas": True,
    "is_headline": False,
    "title": "主场狂轰4-0！奥波莱零封横扫罗兹维泽夫，索拉迪奥双响领跑波甲射手榜",
    "source": "懂球云 · 特派记者",
    "author": "张晨",
    "time": "14天前",
    "date": "2026-08-16",
    "reads": "165,000",
    "comments_count": 980,
    "tag": "留洋战报",
    "summary": "攻防两端全面碾压！索拉迪奥上下半场各入一球，帕拉茨送出两记助攻获8.7分，奥波莱主场4-0大胜升级竞争对手罗兹维泽夫，豪取五轮不败！",
    "content": "波兰甲级联赛第5轮，奥波莱在主场展现了极具统治力的高位压迫体系。索拉迪奥在第22分钟和第44分钟连下两城，普日比乌科与迪奥内下半场锦上添花。全场奥波莱控球率达到65%，零封劲敌罗兹维泽夫，展现了完全超出外界预期的冲超势头。"
  },
  {
    "id": "news_poland_standings_r7",
    "category": "headline",
    "is_overseas": False,
    "is_headline": True,
    "title": "波甲第7轮综述：奥波莱19分领跑直接升级区，华沙莱吉亚16分居次，保级区战况胶着",
    "source": "波兰足球周刊",
    "author": "Marcin Lepa",
    "time": "3小时前",
    "date": "2026-08-30",
    "reads": "320,000",
    "comments_count": 1450,
    "tag": "联赛观察",
    "summary": "波甲7轮战罢积分榜格局初定：奥波莱奥德拉6胜1平积19分独占鳌头，华沙莱吉亚16分紧随其后，克拉科维亚与比亚韦斯托克分列3、4位挺进升级附加赛区。",
    "content": "波兰甲级联赛迎来赛季首个小高潮。奥波莱奥德拉以7战轰入19球的恐怖攻击力领跑积分榜，不仅成为唯一保持不败的队伍，前锋索拉迪奥以9球独居射手榜首位，普日比乌科以6球4助紧随其后。传统豪门华沙莱吉亚近期取得3连胜追至次席，波甲直升席位的竞争已进入白热化阶段。"
  },
  {
    "id": "news_transfer_august_deadline",
    "category": "transfer",
    "is_overseas": False,
    "is_headline": False,
    "title": "夏窗最后冲刺：全欧转会截止日临近，各大联赛豪门加速清理冗员与压哨签约",
    "source": "迪马济奥个人官网",
    "author": "Gianluca Di Marzio",
    "time": "5小时前",
    "date": "2026-08-30",
    "reads": "410,000",
    "comments_count": 1890,
    "tag": "转会动态",
    "summary": "2026年夏季转会窗口即将于9月1日正式关闭，英超、意甲及德甲豪门正进行多笔压哨租借与免签谈判，转会市场进入最后倒计时狂欢。",
    "content": "随着8月底的到来，欧洲主流联赛转会窗进入最后72小时倒计时。各家俱乐部在保证财政公平法案合规的前提下，积极运作压哨引援。波兰及东欧联赛同样有多笔实力派球员换队，奥波莱等队的引援工作已全部完成并已在联赛中产生立竿见影的效果。"
  }
]

# 保留原有非重复新闻
with open(news_path, "r", encoding="utf-8") as f:
    orig_news = json.load(f)

orig_filtered = [item for item in orig_news if item.get("id") not in [a["id"] for a in new_articles]]
combined_news = new_articles + orig_filtered

with open(news_path, "w", encoding="utf-8") as f:
    json.dump(combined_news, f, ensure_ascii=False, indent=2)
print("✅ news_articles.json updated to Round 7")

# ============================================================
# 3. 更新 community_posts.json (虎扑足球论坛球迷热议大盘)
# ============================================================
community_path = os.path.join(DATA_DIR, "community_posts.json")
new_posts = [
  {
    "id": "post_odra_r7_thriller",
    "category": "留洋专区",
    "category_badge": "留洋专区",
    "title": "[赛后] 4-3！七球大战惊天绝杀！奥波莱7轮全不败19分独占榜首！中国少帅真神了！",
    "author": "西里西亚铁血军",
    "avatar": "",
    "tag": "主场铁杆",
    "time": "15分钟前",
    "created_at": 1725040000000,
    "reply_count": 1840,
    "likes": 16800,
    "is_hot": True,
    "content": "刚从奥波莱市政球场出来，嗓子完全喊哑了！！太刺激了！\n比分全程：1-0 -> 2-0 -> 2-2 -> 3-2 -> 3-3 -> 4-3！\n索拉迪奥双响直接9球称霸波甲射手榜！普日比乌科单场造3球（1球2助）拿了9.4分MVP！多恩科尔右路两个传中也是顶级水准！\n重点是徐指导的临场：被追成3-3之后完全没有龟缩，反手压上生力军继续边路爆破，第83分钟绝杀！\n7轮6胜1平积19分，力压华沙莱吉亚独占波甲第一！这真的是中国教练在欧洲职业联赛带出来的成绩吗？谁敢想啊家人们！",
    "replies": [
      {
        "id": "r_odra_1",
        "username": "老球迷老张",
        "avatar": "",
        "tag": "资深球迷",
        "time": "10分钟前",
        "likes": 4210,
        "content": "上赛季带维尔通绝杀冲甲，这赛季接手波甲弱旅奥波莱，开季7轮轰19球独占第一！事实证明徐指导的战术水平在欧洲二级联赛是真的降维打击！"
      },
      {
        "id": "r_odra_2",
        "username": "FM战术板侦探",
        "avatar": "",
        "tag": "战术分析",
        "time": "8分钟前",
        "likes": 3150,
        "content": "这套4-1-1-4双翼齐飞太契合波兰联赛的节奏了。两翼有速度有传中，禁区里两个高中锋索拉迪奥+普日比乌科轮番轰炸，对方中卫下半场体能一空根本顶不住！"
      },
      {
        "id": "r_odra_3",
        "username": "海外看球老铁",
        "avatar": "",
        "tag": "波兰华人",
        "time": "5分钟前",
        "likes": 2680,
        "content": "我在华沙工作，波兰当地同事今天都在讨论奥波莱！都说这支升班马进攻火力比波超球队还猛，徐指导在当地球迷圈已经封神了！"
      }
    ]
  },
  {
    "id": "post_odra_tactics_r6_r7",
    "category": "留洋专区",
    "category_badge": "留洋专区",
    "title": "[战术深度] 从客场1-0铁防西里西亚到主场4-3进攻对飙，徐指导的临场调度到底有多强？",
    "author": "战术观察站",
    "avatar": "",
    "tag": "FM战术师",
    "time": "2小时前",
    "created_at": 1725020000000,
    "reply_count": 960,
    "likes": 8750,
    "is_hot": True,
    "content": "很多球迷只看到4-3大比分，我复盘了一下第6轮和第7轮的两场对比：\n第6轮客场打豪门西里西亚：徐指导摆出中位防守，姆莱奇科全场7次门线神扑，卡克佩尔反击一脚世界波拿走3分；\n第7轮主场对扎布热：全员压上62%控球率狂轰17脚，打出了赛季最高进攻烈度。\n能屈能伸、因地制宜，这才是成熟主帅的标志。奥波莱新赛季的冲超概率现在至少在75%以上了。",
    "replies": [
      {
        "id": "r_tac_1",
        "username": "数据流分析师",
        "avatar": "",
        "tag": "数据控",
        "time": "1小时前",
        "likes": 1820,
        "content": "门将姆莱奇科是真稳，虽然第7轮丢了3球，但第6轮客场那7次扑救个个都是必进球。门将+锋线双核立足，这队下限极高。"
      }
    ]
  },
  {
    "id": "post_poland_d1_title_race",
    "category": "国际足球",
    "category_badge": "国际足球",
    "title": "[大盘讨论] 波甲7轮战罢积分榜：奥波莱19分领跑、莱吉亚16分紧随，本赛季冲超格局大家怎么看？",
    "author": "欧战观察者",
    "avatar": "",
    "tag": "欧洲联赛",
    "time": "4小时前",
    "created_at": 1725000000000,
    "reply_count": 720,
    "likes": 6400,
    "is_hot": False,
    "content": "波兰甲级联赛7轮打完，积分榜第一档已经分化：\n1. 奥波莱奥德拉 6胜1平 19分 净胜+9\n2. 华沙莱吉亚 5胜1平1负 16分 净胜+9\n3. 克拉科维亚 4胜2平1负 14分 净胜+5\n4. 乔治罗尼亚 4胜2平1负 14分 净胜+4\n前两名直接升级，3-6名打附加赛。大家觉得奥波莱的榜首能守到冬歇期吗？",
    "replies": [
      {
        "id": "r_pol_1",
        "username": "Kimi_7",
        "avatar": "",
        "tag": "资深FM玩家",
        "time": "3小时前",
        "likes": 1450,
        "content": "只要索拉迪奥和普日比乌科不遭遇重大伤病，奥波莱的前场火力在波甲完全是独一档。冬歇期再补强一名轮换中卫，直升波超非常有戏！"
      }
    ]
  }
]

with open(community_path, "r", encoding="utf-8") as f:
    orig_posts = json.load(f)

orig_posts_filtered = [p for p in orig_posts if p.get("id") not in [np["id"] for np in new_posts]]
combined_posts = new_posts + orig_posts_filtered

with open(community_path, "w", encoding="utf-8") as f:
    json.dump(combined_posts, f, ensure_ascii=False, indent=2)
print("✅ community_posts.json updated to Round 7")

print("\n🎉 资讯与社区前端实际消费的全部 JSON 数据文件更新完成！")
