import json
from pathlib import Path

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

# 1. ticker_matches.json
ticker_matches = [
    {
        "id": "ticker_odra_01",
        "match_id": 1001,
        "league": "波甲",
        "league_short": "波甲",
        "status": "FT",
        "time": "完赛",
        "is_overseas": True,
        "home_team": "奥波莱奥德拉",
        "home_logo": "🔴",
        "away_team": "普沃茨克维斯瓦",
        "away_logo": "⚪",
        "score_home": 2,
        "score_away": 1,
        "highlights": "88'绝杀 · 奥波莱获波甲首胜"
    },
    {
        "id": "ticker_ucl_02",
        "match_id": 2001,
        "league": "欧冠",
        "league_short": "欧冠决赛",
        "status": "FT",
        "time": "完赛",
        "is_overseas": False,
        "home_team": "皇家马德里",
        "home_logo": "👑",
        "away_team": "曼彻斯特城",
        "away_logo": "🔵",
        "score_home": 2,
        "score_away": 1,
        "highlights": "维尼修斯传射 · 安切洛蒂捧杯"
    },
    {
        "id": "ticker_epl_03",
        "match_id": 3001,
        "league": "英超",
        "league_short": "英超",
        "status": "FT",
        "time": "完赛",
        "is_overseas": False,
        "home_team": "阿森纳",
        "home_logo": "🔴",
        "away_team": "埃弗顿",
        "away_logo": "🔵",
        "score_home": 2,
        "score_away": 0,
        "highlights": "萨卡世界波破门"
    },
    {
        "id": "ticker_jpl_04",
        "match_id": 4001,
        "league": "比甲",
        "league_short": "比甲",
        "status": "FT",
        "time": "完赛",
        "is_overseas": False,
        "home_team": "皇家布鲁日",
        "home_logo": "🔵",
        "away_team": "皇家安德莱赫特",
        "away_logo": "🟣",
        "score_home": 2,
        "score_away": 1,
        "highlights": "布鲁日成功卫冕比甲冠军"
    }
]

# 2. news_articles.json (7:3 ratio: 10 world + 4 overseas = 14 total)
news_articles = [
    {
        "id": "news_odra_win_01",
        "category": "overseas",
        "is_overseas": True,
        "is_headline": True,
        "title": "🇨🇳 首秀绝杀开门红！奥波莱奥德拉 2-1 力克普沃茨克维斯瓦，中国少帅迎来波兰首胜",
        "source": "懂球云 · 特派记者",
        "author": "张晨",
        "time": "2小时前",
        "date": "2026-07-28",
        "reads": "142,500",
        "comments_count": 892,
        "tag": "留洋战报",
        "summary": "波甲首轮激战，由中国籍主教练执教的奥波莱奥德拉主场迎战普沃茨克维斯瓦。凭借第88分钟的角球包抄绝杀，奥波莱2-1力克劲敌，主教练取得执教波兰赛场的梦幻开门红！",
        "content": "北京时间7月28日晚，波兰甲级联赛（I liga）首轮全面开打，由中国主教练执掌帅印的奥波莱奥德拉（Odra Opole）坐镇主场迎来强敌普沃茨克维斯瓦。\n\n比赛开场后，奥波莱奥德拉迅速展现出高位反抢与两翼快速推进风格。第23分钟，奥波莱边锋内切低射打破僵局；客队在第65分钟通过定位球扳平比分。比赛第88分钟，奥波莱获得角球机会，中卫门前高高跃起头球冲顶绝杀！全场哨响，奥波莱奥德拉2-1力克劲敌，豪取新赛季开门红。\n\n赛后发布会上，主教练表示：“我们经历了一个非常充实的季前备战。俱乐部管理层给了全方位的支持，队员们在场上贯彻了每一个战术细节。波甲的对抗强度极高，这三分属于拼到抽筋的所有队员。”"
    },
    {
        "id": "news_cl_final_02",
        "category": "headline",
        "is_overseas": False,
        "is_headline": True,
        "title": "🏆 欧冠决战：皇马 2-1 逆转曼城捧起第16冠！维尼修斯传射，安切洛蒂封神",
        "source": "BBC Sport",
        "author": "Phil McNulty",
        "time": "昨天",
        "date": "2026-06-01",
        "reads": "560,000",
        "comments_count": 3450,
        "tag": "欧冠决赛",
        "summary": "2026赛季欧冠决赛在温布利上演巅峰对决。皇马在先失一球的情况下，依靠维尼修斯的传射建功与贝林厄姆的致命直塞，2-1力克曼城，再度问鼎欧洲之巅！",
        "content": "欧洲足坛最高荣誉战落下帷幕！皇家马德里在温布利球场2-1逆转击败曼城，夺得队史第16座欧洲冠军联赛冠军奖杯。\n\n曼城凭借哈兰德在第18分钟的抢点推射打破僵局，但银河战舰在下半场掀起狂潮。第62分钟，维尼修斯边路连过两人后挑传门前，罗德里戈垫射破门扳平；第84分钟，贝林厄姆中场摆脱后送出手术刀直塞，维尼修斯高速插上冷静单刀推射远角得手！瓜迪奥拉在最后时刻全力反扑未果，安切洛蒂再度改写欧冠历史纪录。"
    },
    {
        "id": "news_arsenal_transfer_03",
        "category": "transfer",
        "is_overseas": False,
        "is_headline": True,
        "title": "🚨 罗马诺夏窗独家：阿森纳正式递交6500万欧报价意甲主力中锋，谈判进入关键阶段",
        "source": "Fabrizio Romano · 独家",
        "author": "Fabrizio Romano",
        "time": "3小时前",
        "date": "2026-07-28",
        "reads": "230,000",
        "comments_count": 980,
        "tag": "转会头条",
        "summary": "知名记者罗马诺最新透露：英超阿森纳向意甲方面递交了超过6500万欧元的首轮正式报价，阿尔特塔希望在季前集训前敲定新赛季9号位主力。",
        "content": "知名记者罗马诺最新专栏披露英超最新转会动向：阿森纳管理层已向意甲方面递交了超过6500万欧元的首轮报价，阿尔特塔希望在季前热身赛前敲定主力9号位人选。球员团队已与枪手达成原则性个人协议，双方正就转会费结构与浮动条款展开细化协商。"
    },
    {
        "id": "news_odra_sign_04",
        "category": "overseas",
        "is_overseas": True,
        "is_headline": False,
        "title": "🚨 官宣！波甲劲旅奥波莱奥德拉签约中国籍主帅，俱乐部全资赞助攻读欧足联A/Pro执照",
        "source": "The Athletic · 国际足球",
        "author": "David Ornstein",
        "time": "2026-07-10",
        "date": "2026-07-10",
        "reads": "218,000",
        "comments_count": 1420,
        "tag": "帅位官宣",
        "summary": "波兰甲级联赛老牌劲旅奥波莱奥德拉官方宣布，聘请上赛季率维尔通完成冲甲的32岁中国教练担任球队主帅，签约2年。俱乐部承诺全额出资赞助其攻读欧足联高阶教练证书！",
        "content": "波兰甲级联赛（I liga）老牌劲旅奥波莱奥德拉（Odra Opole）官方宣布，32岁中国籍主教练正式出任球队新任主帅，双方签下一份为期两年的合同。\n\n据悉，在多份来自欧洲二线联赛的邀约中，奥波莱奥德拉最终脱颖而出的决定性因素在于董事会的诚意——俱乐部在合同中明确加入专项条款，全额承担主教练报读欧足联高阶教练进修班（UEFA A/Pro License）的全部学费与法务担保费用。这彻底解决了此前在比利时遭遇的资格认证痛点。"
    },
    {
        "id": "news_bayern_transfer_05",
        "category": "transfer",
        "is_overseas": False,
        "is_headline": False,
        "title": "大卫·奥恩斯坦专栏：德甲拜仁敲定法甲边路飞翼，转会费总价达5500万欧",
        "source": "The Athletic · DO专栏",
        "author": "David Ornstein",
        "time": "5小时前",
        "date": "2026-07-28",
        "reads": "168,000",
        "comments_count": 520,
        "tag": "转会独家",
        "summary": "The Athletic名记David Ornstein确认：德甲拜仁慕尼黑与法甲俱乐部就边锋转会达成全方位口头协议，体检安排在48小时内进行。",
        "content": "据The Athletic著名记者David Ornstein独家报道，拜仁慕尼黑俱乐部已经与法甲俱乐部就年轻边路攻击手的永久转会达成全面协议，转会费总额为4800万欧元固定外加700万浮动条款。球员本人已经同意了一份为期5年的合约，将在慕尼黑接受体检并正式亮相。"
    },
    {
        "id": "news_poland_ekstraklasa_06",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "波超焦点战：华沙莱吉亚 2-1 逆转波兹南莱赫，两队全场火爆领到8张黄牌",
        "source": "波兰《体育评论报》· Przegląd Sportowy",
        "author": "Maciej Kaliszuk",
        "time": "6小时前",
        "date": "2026-07-28",
        "reads": "112,000",
        "comments_count": 340,
        "tag": "波兰联赛",
        "summary": "波兰超级联赛首轮国家德比引爆波兰球坛。华沙莱吉亚在主场0-1落后局面下下半场连入两球逆转死敌波兹南莱赫，豪取新赛季开门红。",
        "content": "波兰超级联赛揭幕战上演传统国家德比。华沙莱吉亚坐镇波兰陆军球场迎战波兹南莱赫。上半场客队利用角球头球先拔头筹，下半场莱吉亚加强逼抢，第71分钟和第85分钟两度攻破对方大门完成逆转。全场对抗激烈，主裁判出示8张黄牌与1张红牌。"
    },
    {
        "id": "news_mbappe_real_07",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "西媒披露姆巴佩伯纳乌备战细节：已与维尼修斯形成进攻默契，安帅演练前场自由换位",
        "source": "西班牙《马卡报》· MARCA",
        "author": "José Félix Díaz",
        "time": "7小时前",
        "date": "2026-07-27",
        "reads": "310,000",
        "comments_count": 1280,
        "tag": "豪门动态",
        "summary": "马卡报探营皇马季前训练营：姆巴佩与维尼修斯在对抗赛中频繁换位配合，安切洛蒂正打造更具流动性的前场攻击三角。",
        "content": "马卡报最新消息：皇马在巴尔德贝巴斯基地展开新赛季第二阶段合练。新援姆巴佩状态出色，与维尼修斯、贝林厄姆的进攻配合日趋纯熟。安切洛蒂在战术演练中给予姆巴佩高度自由度，新赛季银河战舰的进攻极具爆发力。"
    },
    {
        "id": "news_virton_resign_08",
        "category": "overseas",
        "is_overseas": True,
        "is_headline": False,
        "title": "💥 功成身退！率队升入比甲仅一周，中国主帅正式向维尔通递交辞呈",
        "source": "法国《队报》· L'Équipe",
        "author": "Hugo Delom",
        "time": "2026-05-28",
        "date": "2026-05-28",
        "reads": "320,000",
        "comments_count": 2150,
        "tag": "深度报道",
        "summary": "率维尔通在附加赛读秒绝杀冲入比甲后，中国主帅宣布辞职。高层强推极端U23政策、拒绝兑现冲甲老将续约承诺并拒绝资助教练考证，促成了双方决裂。",
        "content": "刚刚带领比利时挑战者联赛升班马维尔通完成冲甲奇迹的中国籍主教练，于当地时间周四正式向俱乐部递交辞职信，结束了为期9个月的执教生涯。\n\n《队报》深入调查获悉，矛盾的根本根源在于俱乐部高层的战略违约。在冲甲成功后，俱乐部高层通知主教练，未来资源将全部向年轻新秀倾斜，此前向冲甲老将承诺的续约合同全部作废；面对主教练关于由俱乐部出资报读欧足联教练班以规避下赛季比甲巨额罚款的正常诉求，高层以“财政紧张”为由回绝。面对原则分歧，主帅选择昂首辞职体面离开。"
    },
    {
        "id": "news_man_city_pep_09",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "曼城官方宣布瓜迪奥拉续约至2027年！西班牙名帅开启伊蒂哈德执教新周期",
        "source": "天空体育 · Sky Sports",
        "author": "Kaveh Solhekol",
        "time": "8小时前",
        "date": "2026-07-27",
        "reads": "240,000",
        "comments_count": 860,
        "tag": "主帅动态",
        "summary": "曼城俱乐部官方宣布，与主教练佩普·瓜迪奥拉完成续约协议，新合同将持续至2027年夏天。瓜帅将带领蓝月亮向新赛季多线荣誉发起冲击。",
        "content": "天空体育现场报道：曼城主席穆巴拉克与瓜迪奥拉在阿布扎比完成新合约签署。瓜迪奥拉自2016年执教曼城以来已斩获包括欧冠、世俱杯在内的多座重量级奖杯。续约后瓜帅表示：“这里的管理体系和足球理念始终充满饥饿感，我们准备好了迎接新的挑战。”"
    },
    {
        "id": "news_virton_winner_10",
        "category": "overseas",
        "is_overseas": True,
        "is_headline": False,
        "title": "🔥 90+2分钟头球绝杀！维尔通总比分 4-1 大逆转利尔斯，奇迹冲入比甲联赛！",
        "source": "比利时《最新消息报》· HLN",
        "author": "Pieter-Jan Calcoen",
        "time": "2026-05-24",
        "date": "2026-05-24",
        "reads": "280,000",
        "comments_count": 1820,
        "tag": "奇迹之夜",
        "summary": "在首回合0-2落后的绝境下，维尔通次回合主场展开壮烈大反攻，老将梅扎格在补时第92分钟头球攻门锁定胜局，维尔通4-1逆风翻盘晋级比甲！",
        "content": "高姆山谷见证了近十年来比利时足球最壮丽的逆转奇迹！在比乙冲甲附加赛决赛次回合较量中，首回合0-2落后的维尔通精英在伊万·乔治球场爆发出惊人战斗力。\n\n全场比赛维尔通全线压上，疯狂轰出24脚射门。常规时间打成3-0将总比分改写为3-2；在伤停补时第92分钟，老将泰迪·梅扎格力压对方后卫，将皮球重重顶入球门死角！4-1！两回合总比分4-3！维尔通成功冲入比利时顶级联赛！"
    },
    {
        "id": "news_inter_transfer_11",
        "category": "transfer",
        "is_overseas": False,
        "is_headline": False,
        "title": "意甲转会动态：国际米兰锁定两名自由身实力悍将，马洛塔再次展现精妙引援操盘",
        "source": "《米兰体育报》· Gazzetta",
        "author": "Matteo Barzaghi",
        "time": "10小时前",
        "date": "2026-07-27",
        "reads": "154,000",
        "comments_count": 430,
        "tag": "意甲前沿",
        "summary": "《米兰体育报》报道，国米主席马洛塔在夏窗再次展现免签大师本色，已基本锁定两名来自西甲和葡超的自由身球星，即将官宣加盟。",
        "content": "国际米兰在新赛季夏窗保持稳健财务策略。马洛塔在接受采访时确认，球队在后腰与翼卫位置的引援进展顺利。因扎吉对目前的季前备战阵容厚度表示满意。"
    },
    {
        "id": "news_psv_dutch_12",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "荷甲卫冕冠军埃因霍温季前热身赛4-0大胜法甲劲旅，快速短传打法极具压迫感",
        "source": "荷兰《电讯报》· De Telegraaf",
        "author": "Jeroen Kapteijns",
        "time": "12小时前",
        "date": "2026-07-27",
        "reads": "98,000",
        "comments_count": 210,
        "tag": "欧战前瞻",
        "summary": "荷兰豪门埃因霍温在热身赛中展现恐怖攻击群火力，前场四人组连续传递破门，主教练博斯的新赛季提速战术初见成效。",
        "content": "埃因霍温在季前热身赛中迎战法甲球队，全场比赛控球率达到68%，高位逼抢彻底压制对手半场，四粒进球全部来自禁区内流畅的连续撞墙配合。球队将在两周后迎来新赛季荷甲揭幕战。"
    },
    {
        "id": "news_epl_opener_preview_13",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "2026/27 英超赛程公布：揭幕战阿森纳客战维拉，首轮即上演切尔西vs曼城强强对话",
        "source": "BBC Sport",
        "author": "Simon Stone",
        "time": "昨天",
        "date": "2026-07-26",
        "reads": "410,000",
        "comments_count": 1650,
        "tag": "英超前瞻",
        "summary": "英超官方正式公布新赛季完整赛程。揭幕战定于8月15日打响，首周末便迎来切尔西主场迎战卫冕冠军曼城的焦点天王山战役！",
        "content": "英格兰足球超级联赛2026/27赛季赛程出炉。首轮比赛中，阿尔特塔率领的阿森纳将远赴维拉公园球场，而斯坦福桥球场将迎来切尔西与曼城的重量级碰撞。各大豪门引援加速进行，新赛季争冠格局充满看点。"
    },
    {
        "id": "news_club_brugge_14",
        "category": "headline",
        "is_overseas": False,
        "is_headline": False,
        "title": "比甲季前综述：皇家布鲁日领衔欧战军团，安德莱赫特与圣吉罗斯联合扩充板凳",
        "source": "比利时《晚报》· Le Soir",
        "author": "Didier Schyns",
        "time": "2天前",
        "date": "2026-07-25",
        "reads": "87,000",
        "comments_count": 180,
        "tag": "比甲观察",
        "summary": "比利时甲级联赛夏窗动态：布鲁日留住中场核心范纳肯，多支欧战资格队伍积极补强，新赛季比甲争冠组竞争将更加白热化。",
        "content": "随着比利时各支球队陆续开启季前集训，新赛季比甲格局逐渐明朗。上赛季卫冕成功的皇家布鲁日成功留住核心骨干，而安德莱赫特则签入两名南美年轻潜力新星，联赛竞争呈现多强争霸态势。"
    }
]

# 3. all_matches.json (7:3 ratio: 10 world + 3 overseas = 13 total)
all_matches = [
    {
        "id": 1001,
        "league_key": "pol_d1",
        "league_name": "波甲",
        "league_badge": "🇵🇱 波甲",
        "round": 1,
        "round_label": "第 1 轮",
        "date": "2026-07-28 20:00",
        "date_short": "07-28 周二",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": True,
        "home_team": "奥波莱奥德拉",
        "home_logo": "🔴",
        "away_team": "普沃茨克维斯瓦",
        "away_logo": "⚪",
        "score_home": 2,
        "score_away": 1,
        "stadium": "奥波莱市政球场",
        "xg": "1.85 - 0.94",
        "shots": "14",
        "shots_on_target": "6",
        "distance_km": "114.2",
        "scorers": [
            { "minute": 23, "player": "卡克佩尔 (Kacper)", "player_zh": "卡克佩尔", "assist": "加拉兹卡", "assist_zh": "加拉兹卡" },
            { "minute": 65, "player": "塞库尔斯基 (Sekulski)", "player_zh": "塞库尔斯基" },
            { "minute": 88, "player": "皮罗格 (Pirog)", "player_zh": "皮罗格", "assist": "诺瓦克", "assist_zh": "诺瓦克", "goal_type": "头球", "is_header": True, "is_stoppage": True }
        ],
        "news": {
            "title": "奥波莱奥德拉 2-1 绝杀开门红！波甲首轮战报",
            "summary": "凭借88分钟角球头球破门，奥波莱奥德拉主场2-1力克劲旅，迎来波兰联赛首胜！",
            "reporter": "懂球云波兰特派",
            "post_comments": [
                { "username": "Galen", "tag": "球迷", "content": "首秀拿下三分，战术执行力很对味！波甲身体对抗很激烈，继续稳住！", "likes": 420 },
                { "username": "Kimi_7", "tag": "资深FM玩家", "content": "角球战术加上高位逼抢，这套打法在波甲很能打出反击穿透力！", "likes": 310 }
            ]
        }
    },
    {
        "id": 1002,
        "league_key": "pol_d1",
        "league_name": "波甲",
        "league_badge": "🇵🇱 波甲",
        "round": 1,
        "round_label": "第 1 轮",
        "date": "2026-07-28 22:00",
        "date_short": "07-28 周二",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "阿尔卡格丁尼亚",
        "home_logo": "🟡",
        "away_team": "斯维特",
        "away_logo": "🟢",
        "score_home": 3,
        "score_away": 0,
        "stadium": "格丁尼亚城市球场",
        "xg": "2.40 - 0.35",
        "shots": "18",
        "shots_on_target": "8",
        "distance_km": "109.8",
        "scorers": [
            { "minute": 15, "player": "切布拉", "player_zh": "切布拉" },
            { "minute": 52, "player": "戈博夫斯基", "player_zh": "戈博夫斯基" },
            { "minute": 76, "player": "马尔切夫斯基", "player_zh": "马尔切夫斯基" }
        ]
    },
    {
        "id": 1003,
        "league_key": "pol_d1",
        "league_name": "波甲",
        "league_badge": "🇵🇱 波甲",
        "round": 1,
        "round_label": "第 1 轮",
        "date": "2026-07-29 00:00",
        "date_short": "07-29 周三",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "莱吉亚格但斯克",
        "home_logo": "⚪",
        "away_team": "卡托维兹",
        "away_logo": "🟡",
        "score_home": 1,
        "score_away": 1,
        "stadium": "格但斯克能源体育场",
        "xg": "1.10 - 1.25",
        "shots": "10",
        "shots_on_target": "4",
        "distance_km": "111.0",
        "scorers": [
            { "minute": 38, "player": "卡皮奇", "player_zh": "卡皮奇" },
            { "minute": 71, "player": "巴尔加", "player_zh": "巴尔加" }
        ]
    },
    {
        "id": 2001,
        "league_key": "ucl",
        "league_name": "欧冠",
        "league_badge": "🇪🇺 欧冠",
        "round": 13,
        "round_label": "决赛",
        "date": "2026-06-01 03:00",
        "date_short": "06-01 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "皇家马德里",
        "home_logo": "👑",
        "away_team": "曼彻斯特城",
        "away_logo": "🔵",
        "score_home": 2,
        "score_away": 1,
        "stadium": "温布利球场",
        "xg": "1.92 - 1.76",
        "shots": "15",
        "shots_on_target": "7",
        "distance_km": "120.5",
        "scorers": [
            { "minute": 18, "player": "哈兰德", "player_zh": "哈兰德" },
            { "minute": 62, "player": "罗德里戈", "player_zh": "罗德里戈", "assist": "维尼修斯", "assist_zh": "维尼修斯" },
            { "minute": 84, "player": "维尼修斯", "player_zh": "维尼修斯", "assist": "贝林厄姆", "assist_zh": "贝林厄姆" }
        ],
        "news": {
            "title": "欧冠决赛：皇马 2-1 逆转曼城夺队史第16座欧冠奖杯",
            "summary": "维尼修斯传射建功，安切洛蒂战术换人显奇效，银河战舰再次登上欧洲之巅！",
            "reporter": "BBC Sport"
        }
    },
    {
        "id": 2002,
        "league_key": "ucl",
        "league_name": "欧冠",
        "league_badge": "🇪🇺 欧冠",
        "round": 12,
        "round_label": "半决赛次回合",
        "date": "2026-05-09 03:00",
        "date_short": "05-09 周六",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "皇家马德里",
        "home_logo": "👑",
        "away_team": "拜仁慕尼黑",
        "away_logo": "🔴",
        "score_home": 2,
        "score_away": 1,
        "stadium": "伯纳乌球场",
        "xg": "2.10 - 1.30",
        "shots": "17",
        "shots_on_target": "8",
        "distance_km": "118.0",
        "scorers": [
            { "minute": 68, "player": "阿方索·戴维斯", "player_zh": "戴维斯" },
            { "minute": 88, "player": "何塞卢", "player_zh": "何塞卢" },
            { "minute": "90+1", "player": "何塞卢", "player_zh": "何塞卢" }
        ]
    },
    {
        "id": 3001,
        "league_key": "pl",
        "league_name": "英超",
        "league_badge": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 英超",
        "round": 38,
        "round_label": "第 38 轮",
        "date": "2026-05-25 23:00",
        "date_short": "05-25 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "阿森纳",
        "home_logo": "🔴",
        "away_team": "埃弗顿",
        "away_logo": "🔵",
        "score_home": 2,
        "score_away": 0,
        "stadium": "酋长球场",
        "xg": "2.10 - 0.40",
        "shots": "16",
        "shots_on_target": "6",
        "distance_km": "115.3",
        "scorers": [
            { "minute": 34, "player": "萨卡", "player_zh": "萨卡" },
            { "minute": 78, "player": "哈弗茨", "player_zh": "哈弗茨" }
        ]
    },
    {
        "id": 3002,
        "league_key": "pl",
        "league_name": "英超",
        "league_badge": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 英超",
        "round": 38,
        "round_label": "第 38 轮",
        "date": "2026-05-25 23:00",
        "date_short": "05-25 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "曼彻斯特城",
        "home_logo": "🔵",
        "away_team": "西汉姆联",
        "away_logo": "⚒️",
        "score_home": 3,
        "score_away": 1,
        "stadium": "阿提哈德球场",
        "xg": "2.85 - 0.70",
        "shots": "22",
        "shots_on_target": "9",
        "distance_km": "116.8",
        "scorers": [
            { "minute": 2, "player": "福登", "player_zh": "福登" },
            { "minute": 18, "player": "福登", "player_zh": "福登" },
            { "minute": 42, "player": "库杜斯", "player_zh": "库杜斯" },
            { "minute": 59, "player": "罗德里", "player_zh": "罗德里" }
        ]
    },
    {
        "id": 3003,
        "league_key": "pl",
        "league_name": "英超",
        "league_badge": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 英超",
        "round": 38,
        "round_label": "第 38 轮",
        "date": "2026-05-25 23:00",
        "date_short": "05-25 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "切尔西",
        "home_logo": "🔵",
        "away_team": "伯恩茅斯",
        "away_logo": "🍒",
        "score_home": 2,
        "score_away": 1,
        "stadium": "斯坦福桥球场",
        "xg": "1.90 - 1.10",
        "shots": "15",
        "shots_on_target": "6",
        "distance_km": "113.2",
        "scorers": [
            { "minute": 17, "player": "凯塞多", "player_zh": "凯塞多" },
            { "minute": 48, "player": "斯特林", "player_zh": "斯特林" },
            { "minute": 49, "player": "乌纳尔", "player_zh": "乌纳尔" }
        ]
    },
    {
        "id": 4001,
        "league_key": "bel_d1",
        "league_name": "比甲",
        "league_badge": "🇧🇪 比甲",
        "round": 10,
        "round_label": "季后赛第10轮",
        "date": "2026-05-26 02:30",
        "date_short": "05-26 周二",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "皇家布鲁日",
        "home_logo": "🔵",
        "away_team": "皇家安德莱赫特",
        "away_logo": "🟣",
        "score_home": 2,
        "score_away": 1,
        "stadium": "扬·布雷德尔球场",
        "xg": "1.75 - 1.20",
        "shots": "13",
        "shots_on_target": "5",
        "distance_km": "112.4",
        "scorers": [
            { "minute": 29, "player": "范纳肯", "player_zh": "范纳肯" },
            { "minute": 60, "player": "多尔贝格", "player_zh": "多尔贝格" },
            { "minute": 82, "player": "奥尔森", "player_zh": "奥尔森" }
        ]
    },
    {
        "id": 4002,
        "league_key": "bel_d1",
        "league_name": "比甲",
        "league_badge": "🇧🇪 比甲",
        "round": 10,
        "round_label": "季后赛第10轮",
        "date": "2026-05-26 02:30",
        "date_short": "05-26 周二",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "皇家亨克",
        "home_logo": "🔵",
        "away_team": "圣吉罗斯联合",
        "away_logo": "🟡",
        "score_home": 1,
        "score_away": 0,
        "stadium": "结晶球场",
        "xg": "1.20 - 0.95",
        "shots": "11",
        "shots_on_target": "4",
        "distance_km": "111.0",
        "scorers": [
            { "minute": 44, "player": "托卢", "player_zh": "托卢" }
        ]
    },
    {
        "id": 5032,
        "league_key": "bel_d2",
        "league_name": "比乙",
        "league_badge": "🇧🇪 比乙",
        "round": 32,
        "round_label": "附加赛次回合",
        "date": "2026-05-24 21:00",
        "date_short": "05-24 周日",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": True,
        "home_team": "维尔通精英",
        "home_logo": "🟢",
        "away_team": "利尔斯",
        "away_logo": "🟡",
        "score_home": 4,
        "score_away": 1,
        "stadium": "伊万·乔治球场",
        "xg": "3.12 - 0.85",
        "shots": "24",
        "shots_on_target": "11",
        "distance_km": "118.5",
        "scorers": [
            { "minute": 14, "player": "朴昇秀", "player_zh": "朴昇秀" },
            { "minute": 38, "player": "吉永梦希", "player_zh": "吉永梦希" },
            { "minute": 62, "player": "范埃克", "player_zh": "范埃克" },
            { "minute": 77, "player": "马塞洛", "player_zh": "马塞洛" },
            { "minute": "90+2", "player": "泰迪·梅扎格", "player_zh": "泰迪·梅扎格", "goal_type": "头球", "is_header": True, "is_stoppage": True }
        ],
        "news": {
            "title": "90+2分钟绝杀！维尔通总比分4-1逆转利尔斯冲入比甲！",
            "summary": "梅扎格补时头球锁定胜局，维尔通完成比乙历史级绝地翻盘奇迹！",
            "reporter": "HLN 比利时最新消息报"
        }
    },
    {
        "id": 5031,
        "league_key": "bel_d2",
        "league_name": "比乙",
        "league_badge": "🇧🇪 比乙",
        "round": 31,
        "round_label": "附加赛首回合",
        "date": "2026-05-18 20:00",
        "date_short": "05-18 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": True,
        "home_team": "利尔斯",
        "home_logo": "🟡",
        "away_team": "维尔通精英",
        "away_logo": "🟢",
        "score_home": 2,
        "score_away": 0,
        "stadium": "赫尔曼·范德波滕球场",
        "xg": "1.65 - 1.10",
        "shots": "12",
        "shots_on_target": "5",
        "distance_km": "110.2",
        "scorers": [
            { "minute": 32, "player": "范克雷贝尔", "player_zh": "范克雷贝尔" },
            { "minute": 81, "player": "达格巴", "player_zh": "达格巴" }
        ]
    },
    {
        "id": 5028,
        "league_key": "bel_d2",
        "league_name": "比乙",
        "league_badge": "🇧🇪 比乙",
        "round": 28,
        "round_label": "第 28 轮",
        "date": "2026-04-20 20:00",
        "date_short": "04-20 周一",
        "status": "FT",
        "status_label": "完赛",
        "is_overseas": False,
        "home_team": "皇家马斯梅赫伦",
        "home_logo": "⚪",
        "away_team": "贝弗伦",
        "away_logo": "🟡",
        "score_home": 2,
        "score_away": 0,
        "stadium": "帕特罗球场",
        "xg": "1.80 - 0.60",
        "shots": "14",
        "shots_on_target": "6",
        "distance_km": "108.4",
        "scorers": [
            { "minute": 22, "player": "卡亚", "player_zh": "卡亚" },
            { "minute": 67, "player": "范登贝尔赫", "player_zh": "范登贝尔赫" }
        ]
    }
]

# 4. community_posts.json (7:3 ratio: 5 world + 3 overseas = 8 total)
community_posts = [
    {
        "id": "post_ucl_final",
        "category": "国际足球",
        "category_badge": "国际足球",
        "title": "[赛后讨论] 皇马 2-1 曼城捧起第16座欧冠！维尼修斯传射，如何评价安切洛蒂的杯赛调整能力？",
        "author": "伯纳乌纯白之魂",
        "avatar": "👑",
        "tag": "皇马球迷",
        "time": "3天前",
        "created_at": 1721900000000,
        "reply_count": 2480,
        "likes": 13200,
        "is_hot": True,
        "content": "第16座大耳朵杯到手！落后一球不仅不慌，下半场换上罗德里戈和卡马文加瞬间扭转战局。维尼修斯大场面先生属性拉满，一传一射！\n安切洛蒂在欧冠淘汰赛的临场调整和心理建设，真的已经到了化境。如何看待皇马近十年在欧冠的统治力？",
        "replies": [
            {
                "id": "r_1",
                "username": "蓝月亮荣耀",
                "avatar": "🔵",
                "tag": "曼城球迷",
                "time": "3天前",
                "likes": 2890,
                "content": "曼城上半场机会没把握住拉开两球，下半场体力下来被皇马两翼冲垮了。恭喜皇马，安帅确实是欧冠之王。"
            },
            {
                "id": "r_2",
                "username": "Milanista_1899",
                "avatar": "🔴",
                "tag": "AC米兰球迷",
                "time": "3天前",
                "likes": 2100,
                "content": "安切洛蒂无论在米兰还是皇马，欧冠决战的气场永远是独一档。看他的比赛就知道什么是‘从容不迫’。"
            }
        ]
    },
    {
        "id": "post_odra_win",
        "category": "留洋专区",
        "category_badge": "留洋专区",
        "title": "[赛后] 奥波莱奥德拉 2-1 绝杀开门红！波兰甲级联赛首轮战报与赛后讨论",
        "author": "老特拉福德看门人",
        "avatar": "🔴",
        "tag": "曼联球迷",
        "time": "2小时前",
        "created_at": 1722168000000,
        "reply_count": 892,
        "likes": 6420,
        "is_hot": True,
        "content": "刚看完波甲首轮直播！奥波莱奥德拉主场 2-1 绝杀普沃茨克维斯瓦！\n第23分钟边路内切先进一个，下半场被扳平后主教练果断换人，第88分钟利用角球抢点绝杀！全场14脚射门，跑动距离114公里。\n波兰联赛首秀拿下开门红，高位反击体系依然丝滑！大家觉得新赛季奥波莱在波甲能冲前六吗？",
        "replies": [
            {
                "id": "r_3",
                "username": "Galen",
                "avatar": "⚽",
                "tag": "球迷",
                "time": "1小时前",
                "likes": 3280,
                "content": "熟悉的88分钟绝杀！不得不说定位球战术和最后15分钟搏命进攻真有一手，在维尔通也是附加赛92分钟头球绝杀，在波兰第一场又来个绝杀！"
            },
            {
                "id": "r_4",
                "username": "阿森纳今天赢了吗",
                "avatar": "🔴",
                "tag": "枪迷",
                "time": "1小时前",
                "likes": 2650,
                "content": "波甲的身体对抗比比乙硬不少，但战术组织普遍比较粗糙。这种细腻快速的地面传递打波甲球队很容易打穿肋部。这三分太关键了！"
            }
        ]
    },
    {
        "id": "post_arsenal_tactics",
        "category": "英超专区",
        "category_badge": "英超专区",
        "title": "[战术复盘] 阿森纳 2-0 埃弗顿：阿尔特塔的高位逼抢与肋部三角配合解析",
        "author": "枪手忠魂",
        "avatar": "🔴",
        "tag": "枪迷",
        "time": "1天前",
        "created_at": 1722080000000,
        "reply_count": 780,
        "likes": 4890,
        "is_hot": True,
        "content": "上赛季阿森纳虽然89分屈居亚军，但在防守端仅失29球为全英超最佳。阿尔特塔推行的高位封堵和边后卫内收体系日臻成熟，新赛季一旦补进正牌中锋，进攻终结效率将产生质变。",
        "replies": [
            {
                "id": "r_5",
                "username": "北伦敦纯红",
                "avatar": "🔴",
                "tag": "阿森纳球迷",
                "time": "1天前",
                "likes": 1820,
                "content": "赖斯加盟之后中场硬度直接上了一个档次，下赛季看好阿森纳力压曼城夺冠！"
            }
        ]
    },
    {
        "id": "post_romano_transfers",
        "category": "转会专区",
        "category_badge": "转会专区",
        "title": "🚨 罗马诺夏窗汇总：德甲拜仁敲定边锋，阿森纳6500万欧报价意甲主力中锋",
        "author": "转会情报站",
        "avatar": "📱",
        "tag": "资讯博主",
        "time": "5小时前",
        "created_at": 1722150000000,
        "reply_count": 670,
        "likes": 4520,
        "is_hot": False,
        "content": "罗马诺今早直播披露：\n1. 拜仁与法甲边锋就个人待遇达成协议，5500万欧转会费基本敲定。\n2. 阿森纳向意甲提交6500万欧中锋报价，正等待对方管理层最终批复。\n3. 波兰甲方面，奥波莱奥德拉在完成首胜后，正与俱乐部商讨夏窗后防线补强名单。",
        "replies": [
            {
                "id": "r_6",
                "username": "枪手忠魂",
                "avatar": "🔴",
                "tag": "枪迷",
                "time": "4小时前",
                "likes": 1250,
                "content": "阿森纳终于舍得砸钱买正牌中锋了！下赛季争冠阵容齐整了。"
            }
        ]
    },
    {
        "id": "post_mbappe_analysis",
        "category": "国际足球",
        "category_badge": "国际足球",
        "title": "姆巴佩加盟皇马首季数据预测：能在西甲轰进 30 球吗？",
        "author": "足球数据汪",
        "avatar": "📊",
        "tag": "数据控",
        "time": "2天前",
        "created_at": 1722000000000,
        "reply_count": 940,
        "likes": 5600,
        "is_hot": False,
        "content": "从巴黎转投皇马后，姆巴佩将得到贝林厄姆、巴尔韦德和维尼修斯等顶级配置的火力输送。大家预测他新赛季西甲进球数会在哪个区间？",
        "replies": [
            {
                "id": "r_7",
                "username": "伯纳乌纯白之魂",
                "avatar": "👑",
                "tag": "皇马球迷",
                "time": "2天前",
                "likes": 2100,
                "content": "只要不受伤，30球保底！皇马前场的反击速度是全欧第一档。"
            }
        ]
    },
    {
        "id": "post_virton_resign_truth",
        "category": "留洋专区",
        "category_badge": "留洋专区",
        "title": "[深度观察] 维尔通冲甲后阵容大重组：管理层战略转向U23，主帅与多名老将离队内幕",
        "author": "高姆山谷守夜人",
        "avatar": "🛡️",
        "tag": "比乙观察员",
        "time": "2天前",
        "created_at": 1722000000000,
        "reply_count": 1420,
        "likes": 8840,
        "is_hot": True,
        "content": "队报和比利时HLN深入披露了维尔通冲甲后的剧烈变动：\n俱乐部高层在成功升甲后全面推行极端年轻化政策，拒绝向梅扎格等冲甲功勋老将兑现续约承诺；同时在主帅执教资格进修费用上存在分歧，导致功勋教练组集体递交辞呈。\n这一事件在比利时足坛引发广泛讨论，升班马在顶级联赛的大换血充满巨大保级隐患。",
        "replies": [
            {
                "id": "r_8",
                "username": "倒立洗头协会会长",
                "avatar": "🍺",
                "tag": "吃瓜老懂哥",
                "time": "2天前",
                "likes": 4210,
                "content": "冲甲了立马清洗老臣，连主教练深造费用都卡着不批，这种经营方式在比甲很容易被豪门打崩。"
            },
            {
                "id": "r_9",
                "username": "战术显微镜",
                "avatar": "🔍",
                "tag": "数据博主",
                "time": "2天前",
                "likes": 3150,
                "content": "从职业发展看，主教练体面离任是正确选择。带一支更衣室心态受挫的升班马风险极大，现在转战波兰甲级联赛反而是全新平台！"
            }
        ]
    },
    {
        "id": "post_haaland_debate",
        "category": "国际足球",
        "category_badge": "国际足球",
        "title": "哈兰德近三场焦点战被皇马中卫限制，如何看待大中锋在杯赛淘汰赛的战术价值？",
        "author": "战术显微镜",
        "avatar": "🔍",
        "tag": "数据博主",
        "time": "3天前",
        "created_at": 1721920000000,
        "reply_count": 1150,
        "likes": 7200,
        "is_hot": False,
        "content": "吕迪格连续两季在欧冠对哈兰德采取贴身肉搏防守，哈兰德触球次数大幅减少。但与此同时曼城其他攻击手获得了大量外围空当。大中锋的‘牵制威慑’是否被外界低估了？",
        "replies": [
            {
                "id": "r_10",
                "username": "蓝月亮荣耀",
                "avatar": "🔵",
                "tag": "曼城球迷",
                "time": "3天前",
                "likes": 1950,
                "content": "哈兰德一个人带走两个中卫，福登和B席才有空间起脚。不能只看进球，战术价值毋庸置疑。"
            }
        ]
    },
    {
        "id": "post_uefa_license_talk",
        "category": "留洋专区",
        "category_badge": "留洋专区",
        "title": "【深度科普】欧足联职业教练执照（UEFA Pro）准入条件与欧洲联赛主帅资质要求",
        "author": "球探小李",
        "avatar": "🎓",
        "tag": "青训研究",
        "time": "1天前",
        "created_at": 1722050000000,
        "reply_count": 620,
        "likes": 4100,
        "is_hot": False,
        "content": "科普一下欧洲职业教练认证体系：\n欧足联UEFA A级和Pro级是全球含金量最高、准入最严苛的教练证书。报读高阶课程必须有欧洲职业联赛俱乐部出具官方担保与一线队实操岗位。奥波莱俱乐部为新帅全额资助攻读教练证书，不仅免除了无证执教罚款，更为教练员提供了正规的职业进修资质通道。",
        "replies": [
            {
                "id": "r_11",
                "username": "低调的皮尔洛",
                "avatar": "🍷",
                "tag": "球迷",
                "time": "1天前",
                "likes": 2180,
                "content": "干货满满！俱乐部官方担保名额非常稀缺，奥波莱高层确实给了足够的平台支持！"
            }
        ]
    }
]

# 5. standings_multi.json
standings_multi = {
    "leagues": [
        {
            "key": "pol_d1",
            "name": "波兰甲级联赛 (I liga)",
            "label": "🇵🇱 波甲",
            "flag": "🇵🇱",
            "season": "2026/27 赛季",
            "round_info": "第 1 轮 完赛",
            "table": [
                { "position": 1, "team_name": "阿尔卡格丁尼亚", "played": 1, "won": 1, "drawn": 0, "lost": 0, "gf": 3, "ga": 0, "gd": 3, "points": 3 },
                { "position": 2, "team_name": "克拉科夫维斯瓦", "played": 1, "won": 1, "drawn": 0, "lost": 0, "gf": 2, "ga": 0, "gd": 2, "points": 3 },
                { "position": 3, "team_name": "奥波莱奥德拉", "played": 1, "won": 1, "drawn": 0, "lost": 0, "gf": 2, "ga": 1, "gd": 1, "points": 3, "is_overseas": True },
                { "position": 4, "team_name": "戈尔尼克莱奇纳", "played": 1, "won": 1, "drawn": 0, "lost": 0, "gf": 2, "ga": 1, "gd": 1, "points": 3 },
                { "position": 5, "team_name": "莱吉亚格但斯克", "played": 1, "won": 0, "drawn": 1, "lost": 0, "gf": 1, "ga": 1, "gd": 0, "points": 1 },
                { "position": 6, "team_name": "卡托维兹", "played": 1, "won": 0, "drawn": 1, "lost": 0, "gf": 1, "ga": 1, "gd": 0, "points": 1 },
                { "position": 7, "team_name": "蒂希", "played": 1, "won": 0, "drawn": 1, "lost": 0, "gf": 0, "ga": 0, "gd": 0, "points": 1 },
                { "position": 8, "team_name": "涅切恰", "played": 1, "won": 0, "drawn": 1, "lost": 0, "gf": 0, "ga": 0, "gd": 0, "points": 1 },
                { "position": 9, "team_name": "普沃茨克维斯瓦", "played": 1, "won": 0, "drawn": 0, "lost": 1, "gf": 1, "ga": 2, "gd": -1, "points": 0 },
                { "position": 10, "team_name": "斯捷齐纳波贡", "played": 1, "won": 0, "drawn": 0, "lost": 1, "gf": 0, "ga": 2, "gd": -2, "points": 0 },
                { "position": 11, "team_name": "斯维特", "played": 1, "won": 0, "drawn": 0, "lost": 1, "gf": 0, "ga": 3, "gd": -3, "points": 0 }
            ],
            "scorers": [
                { "rank": 1, "player": "切布拉", "team": "阿尔卡格丁尼亚", "goals": 2, "penalties": 0, "matches": 1 },
                { "rank": 2, "player": "皮罗格", "team": "奥波莱奥德拉", "goals": 1, "penalties": 0, "matches": 1, "is_overseas": True },
                { "rank": 3, "player": "卡克佩尔", "team": "奥波莱奥德拉", "goals": 1, "penalties": 0, "matches": 1, "is_overseas": True },
                { "rank": 4, "player": "塞库尔斯基", "team": "普沃茨克维斯瓦", "goals": 1, "penalties": 0, "matches": 1 }
            ],
            "assists": [
                { "rank": 1, "player": "加拉兹卡", "team": "奥波莱奥德拉", "assists": 1, "matches": 1, "is_overseas": True },
                { "rank": 2, "player": "诺瓦克", "team": "奥波莱奥德拉", "assists": 1, "matches": 1, "is_overseas": True },
                { "rank": 3, "player": "戈博夫斯基", "team": "阿尔卡格丁尼亚", "assists": 1, "matches": 1 }
            ],
            "transfers": [
                { "date": "2026-07-10", "type": "换帅", "player": "中国籍教练 (新帅)", "from": "自由身", "to": "奥波莱奥德拉", "fee": "签约2年" },
                { "date": "2026-07-15", "type": "转入", "player": "诺瓦克 (前腰)", "from": "莱吉亚二队", "to": "奥波莱奥德拉", "fee": "租借加盟" },
                { "date": "2026-07-08", "type": "转入", "player": "切布拉 (前锋)", "from": "琴斯托霍瓦", "to": "阿尔卡格丁尼亚", "fee": "自由转会" }
            ]
        },
        {
            "key": "bel_d1",
            "name": "比利时甲级联赛 (比甲)",
            "label": "🇧🇪 比甲",
            "flag": "🇧🇪",
            "season": "2025/26 赛季 (已完结)",
            "round_info": "冠军附加赛完结",
            "table": [
                { "position": 1, "team_name": "皇家布鲁日", "played": 10, "won": 7, "drawn": 2, "lost": 1, "gf": 21, "ga": 9, "gd": 12, "points": 50, "note": "欧冠正赛" },
                { "position": 2, "team_name": "皇家安德莱赫特", "played": 10, "won": 6, "drawn": 1, "lost": 3, "gf": 18, "ga": 12, "gd": 6, "points": 46, "note": "欧冠资格赛" },
                { "position": 3, "team_name": "圣吉罗斯联合", "played": 10, "won": 5, "drawn": 2, "lost": 3, "gf": 16, "ga": 11, "gd": 5, "points": 44, "note": "欧联资格赛" },
                { "position": 4, "team_name": "皇家亨克", "played": 10, "won": 4, "drawn": 1, "lost": 5, "gf": 14, "ga": 15, "gd": -1, "points": 37, "note": "欧协联附加赛" },
                { "position": 5, "team_name": "安特卫普", "played": 10, "won": 3, "drawn": 0, "lost": 7, "gf": 11, "ga": 18, "gd": -7, "points": 31 },
                { "position": 6, "team_name": "根特", "played": 10, "won": 1, "drawn": 2, "lost": 7, "gf": 8, "ga": 23, "gd": -15, "points": 26 }
            ],
            "scorers": [
                { "rank": 1, "player": "多尔贝格", "team": "皇家安德莱赫特", "goals": 18, "penalties": 3, "matches": 32 },
                { "rank": 2, "player": "奥尔森", "team": "皇家布鲁日", "goals": 16, "penalties": 1, "matches": 30 },
                { "rank": 3, "player": "阿莫拉", "team": "圣吉罗斯联合", "goals": 15, "penalties": 0, "matches": 28 }
            ],
            "assists": [
                { "rank": 1, "player": "范纳肯", "team": "皇家布鲁日", "assists": 12, "matches": 34 },
                { "rank": 2, "player": "德萨伊尔", "team": "皇家布鲁日", "assists": 9, "matches": 31 }
            ],
            "transfers": [
                { "date": "2026-06-20", "type": "转出", "player": "德凯特拉雷", "from": "布鲁日", "to": "亚特兰大", "fee": "买断条款生效 2200万欧" },
                { "date": "2026-06-18", "type": "转入", "player": "贝尔特拉梅", "from": "葡超", "to": "安德莱赫特", "fee": "自由转会" }
            ]
        },
        {
            "key": "bel_d2",
            "name": "比利时挑战者联赛 (比乙)",
            "label": "🇧🇪 比乙",
            "flag": "🇧🇪",
            "season": "2025/26 赛季 (已完结)",
            "round_info": "冲甲附加赛结束 · 维尔通成功冲甲",
            "table": [
                { "position": 1, "team_name": "皇家马斯梅赫伦", "played": 28, "won": 18, "drawn": 7, "lost": 3, "gf": 55, "ga": 22, "gd": 33, "points": 61, "note": "直接升甲" },
                { "position": 2, "team_name": "维尔通精英", "played": 28, "won": 16, "drawn": 9, "lost": 3, "gf": 61, "ga": 37, "gd": 24, "points": 57, "note": "附加赛冠军·成功升甲 🏆", "is_overseas": True },
                { "position": 3, "team_name": "皇家比尔肖特", "played": 28, "won": 15, "drawn": 5, "lost": 8, "gf": 43, "ga": 32, "gd": 11, "points": 50, "note": "附加赛" },
                { "position": 4, "team_name": "聚尔特瓦勒海姆", "played": 28, "won": 14, "drawn": 6, "lost": 8, "gf": 48, "ga": 34, "gd": 14, "points": 48, "note": "附加赛" },
                { "position": 5, "team_name": "利尔斯", "played": 28, "won": 13, "drawn": 6, "lost": 9, "gf": 45, "ga": 39, "gd": 6, "points": 45, "note": "附加赛亚军" },
                { "position": 6, "team_name": "洛默尔", "played": 28, "won": 12, "drawn": 7, "lost": 9, "gf": 40, "ga": 33, "gd": 7, "points": 43 }
            ],
            "scorers": [
                { "rank": 1, "player": "卡亚 (Kaya)", "team": "皇家马斯梅赫伦", "goals": 19, "penalties": 4, "matches": 27 },
                { "rank": 2, "player": "吉永梦希 (Yuminoki)", "team": "维尔通精英", "goals": 14, "penalties": 0, "matches": 28, "is_overseas": True },
                { "rank": 3, "player": "朴昇秀 (Seung-soo)", "team": "维尔通精英", "goals": 11, "penalties": 2, "matches": 26, "is_overseas": True }
            ],
            "assists": [
                { "rank": 1, "player": "朴昇秀 (Seung-soo)", "team": "维尔通精英", "assists": 10, "matches": 26, "is_overseas": True },
                { "rank": 2, "player": "范埃克", "team": "利尔斯", "assists": 8, "matches": 28 }
            ],
            "transfers": [
                { "date": "2026-05-28", "type": "离任", "player": "中国籍教练 (主教练)", "from": "维尔通精英", "to": "自由身", "fee": "达成解约协议" },
                { "date": "2026-06-15", "type": "离队", "player": "泰迪·梅扎格", "from": "维尔通精英", "to": "自由身", "fee": "合同到期未获续约" }
            ]
        },
        {
            "key": "pl",
            "name": "英格兰足球超级联赛 (英超)",
            "label": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 英超",
            "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
            "season": "2025/26 赛季 (已完结)",
            "round_info": "第 38 轮 赛季收官",
            "table": [
                { "position": 1, "team_name": "曼彻斯特城", "played": 38, "won": 28, "drawn": 7, "lost": 3, "gf": 96, "ga": 34, "gd": 62, "points": 91, "note": "英超冠军 🏆" },
                { "position": 2, "team_name": "阿森纳", "played": 38, "won": 28, "drawn": 5, "lost": 5, "gf": 91, "ga": 29, "gd": 62, "points": 89, "note": "欧冠正赛" },
                { "position": 3, "team_name": "利物浦", "played": 38, "won": 24, "drawn": 10, "lost": 4, "gf": 86, "ga": 41, "gd": 45, "points": 82, "note": "欧冠正赛" },
                { "position": 4, "team_name": "阿斯顿维拉", "played": 38, "won": 20, "drawn": 8, "lost": 10, "gf": 76, "ga": 61, "gd": 15, "points": 68, "note": "欧冠正赛" },
                { "position": 5, "team_name": "托特纳姆热刺", "played": 38, "won": 20, "drawn": 6, "lost": 12, "gf": 74, "ga": 61, "gd": 13, "points": 66, "note": "欧联正赛" },
                { "position": 6, "team_name": "切尔西", "played": 38, "won": 18, "drawn": 9, "lost": 11, "gf": 77, "ga": 63, "gd": 14, "points": 63, "note": "欧协联附加赛" }
            ],
            "scorers": [
                { "rank": 1, "player": "埃尔林·哈兰德", "team": "曼彻斯特城", "goals": 27, "penalties": 5, "matches": 35 },
                { "rank": 2, "player": "科尔·帕尔默", "team": "切尔西", "goals": 22, "penalties": 8, "matches": 34 },
                { "rank": 3, "player": "亚历山大·伊萨克", "team": "纽卡斯尔联", "goals": 21, "penalties": 4, "matches": 32 }
            ],
            "assists": [
                { "rank": 1, "player": "沃特金斯", "team": "阿斯顿维拉", "assists": 13, "matches": 37 },
                { "rank": 2, "player": "科尔·帕尔默", "team": "切尔西", "assists": 11, "matches": 34 },
                { "rank": 3, "player": "德布劳内", "team": "曼彻斯特城", "assists": 10, "matches": 24 }
            ],
            "transfers": [
                { "date": "2026-07-20", "type": "官宣", "player": "萨维尼奥", "from": "特鲁瓦", "to": "曼彻斯特城", "fee": "转会费 3500万欧" },
                { "date": "2026-07-18", "type": "官宣", "player": "卡拉菲奥里", "from": "博洛尼亚", "to": "阿森纳", "fee": "转会费 4500万欧" }
            ]
        },
        {
            "key": "ucl",
            "name": "欧洲冠军联赛 (欧冠)",
            "label": "🇪🇺 欧冠",
            "flag": "🇪🇺",
            "season": "2025/26 赛季 (已完结)",
            "round_info": "温布利决赛 · 皇马夺冠",
            "table": [
                { "position": 1, "team_name": "皇家马德里", "played": 13, "won": 9, "drawn": 4, "lost": 0, "gf": 28, "ga": 15, "gd": 13, "points": 31, "note": "欧冠冠军 🏆 (第16冠)" },
                { "position": 2, "team_name": "曼彻斯特城", "played": 13, "won": 8, "drawn": 4, "lost": 1, "gf": 33, "ga": 14, "gd": 19, "points": 28, "note": "欧冠亚军" },
                { "position": 3, "team_name": "拜仁慕尼黑", "played": 12, "won": 7, "drawn": 3, "lost": 2, "gf": 24, "ga": 13, "gd": 11, "points": 24, "note": "四强" },
                { "position": 4, "team_name": "巴黎圣日耳曼", "played": 12, "won": 6, "drawn": 2, "lost": 4, "gf": 20, "ga": 16, "gd": 4, "points": 20, "note": "四强" }
            ],
            "scorers": [
                { "rank": 1, "player": "基利安·姆巴佩", "team": "皇家马德里/巴黎", "goals": 10, "penalties": 2, "matches": 12 },
                { "rank": 2, "player": "哈里·凯恩", "team": "拜仁慕尼黑", "goals": 8, "penalties": 3, "matches": 12 },
                { "rank": 3, "player": "维尼修斯", "team": "皇家马德里", "goals": 7, "penalties": 0, "matches": 11 }
            ],
            "assists": [
                { "rank": 1, "player": "维尼修斯", "team": "皇家马德里", "assists": 6, "matches": 11 },
                { "rank": 2, "player": "贝林厄姆", "team": "皇家马德里", "assists": 5, "matches": 12 }
            ],
            "transfers": [
                { "date": "2026-06-03", "type": "震撼官宣", "player": "基利安·姆巴佩", "from": "巴黎圣日耳曼", "to": "皇家马德里", "fee": "自由身签约5年" }
            ]
        }
    ]
}

# Write files
with open(DATA_DIR / "ticker_matches.json", "w", encoding="utf-8") as f:
    json.dump(ticker_matches, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "news_articles.json", "w", encoding="utf-8") as f:
    json.dump(news_articles, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "all_matches.json", "w", encoding="utf-8") as f:
    json.dump(all_matches, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "community_posts.json", "w", encoding="utf-8") as f:
    json.dump(community_posts, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "standings_multi.json", "w", encoding="utf-8") as f:
    json.dump(standings_multi, f, ensure_ascii=False, indent=2)

print("All 5 clean JSON files updated successfully!")
