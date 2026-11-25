"""
一键更新存档数据到第7轮 (2026-08-30)
基于 task-4875 和 task-4904 获取的真实比赛数据
"""
import json, os

DATA = r"I:\fm26-virton-hub\web\src\data"

# ============================================================
# 1. 更新 all_matches.json：追加 R4-R7 比赛记录
# ============================================================

NEW_MATCHES = [
  {
    "id": 1004,
    "league_key": "pol_d1",
    "league_name": "波甲",
    "league_badge": "波甲",
    "league_flag": "circle-flags:pl",
    "round": 4,
    "round_label": "第 4 轮",
    "date": "2026-08-09 18:00",
    "date_short": "08-09 周日",
    "status": "FT",
    "status_label": "完赛",
    "is_overseas": True,
    "home_team": "奥波莱奥德拉",
    "home_code": "ODR",
    "away_team": "琴斯托霍瓦",
    "away_code": "CZE",
    "score_home": 4,
    "score_away": 1,
    "stadium": "奥波莱市政球场",
    "xg": "2.80 - 1.10",
    "shots": "16",
    "shots_on_target": "9",
    "distance_km": "0",
    "scorers": [
      {"minute": 18, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥", "assist": "帕特里克·希什", "assist_zh": "希什"},
      {"minute": 37, "player": "巴巴卡尔·迪奥内", "player_zh": "迪奥内"},
      {"minute": 52, "player": "托马斯·加伊达", "player_zh": "加伊达", "assist": "马特乌什·斯皮哈瓦", "assist_zh": "斯皮哈瓦"},
      {"minute": 71, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥", "assist": "帕特里克·希什", "assist_zh": "希什", "is_mvp_goal": True}
    ],
    "news": {
      "title": "主场轰4-1！奥波莱大胜琴斯托霍瓦，索拉迪奥双响称霸波甲射手榜",
      "summary": "主场大胜！索拉迪奥打入双响，加伊达和迪奥内各建功，奥波莱4轮全不败稳居升级区！",
      "reporter": "懂球云波兰特派",
      "dongqiudi_article": {
        "title": "主场轰4-1！奥波莱大胜琴斯托霍瓦，索拉迪奥双响称霸波甲射手榜",
        "summary": "索拉迪奥全场最高9.0评分双响，主场4-1大胜，奥波莱4轮7分稳居升级区！",
        "body": "【比赛焦点】\n波甲第4轮主场之战，奥波莱迎战升班马琴斯托霍瓦。中国主帅排出熟悉的4-1-1-4双翼体系，巴西外援索拉迪奥担纲进攻箭头。\n\n【关键事件】\n第18分钟，希什右侧巧妙输送，索拉迪奥禁区内单刀推射破门，主场率先开球！\n第37分钟，迪奥内左路快速推进，进入禁区横档拨射，球贴右柱入网！2-0！\n第52分钟，斯皮哈瓦中路抢断发动快反，加伊达插上抽射，球改变方向入门！3-0。\n第71分钟，希什精准直塞，索拉迪奥追上皮球冷静推射，4-0！完全锁死比赛！\n客队临近终场扳回一城，最终4-1收场。\n\n【战术复盘】\n本场希什贡献1传2助，双翼传球体系完全爆发；索拉迪奥全场9.0评分，高居本轮最佳。四轮保持不败，奥波莱是本赛季波甲最具升级相的球队之一。",
        "tags": ["波甲", "奥波莱奥德拉", "主场大捷", "索拉迪奥", "四连不败"]
      },
      "local_media_snippet": {
        "outlet": "波兰体育周刊《Przegląd Sportowy》",
        "country_flag": "circle-flags:pl",
        "journalist": "Tomasz Włodarczyk",
        "quote": "奥波莱主场展现了真正的攻势足球！索拉迪奥与希什之间的默契配合令人叹为观止，这支球队正在以极快的速度适应波甲的强度。"
      },
      "hupu_thread": {
        "coach_score": 9.2,
        "comments": [
          {"username": "波兰追球人", "tag": "西里西亚球迷", "likes": 312, "content": "4-1！主场完全碾压！索拉迪奥在这个体系下就是无解！"},
          {"username": "奥波莱老铁", "tag": "主场铁杆", "likes": 243, "content": "希什本场2助攻，真正意义上的左路发动机。徐指导把他激活了！"},
          {"username": "战术观察站", "tag": "FM战术师", "likes": 189, "content": "全场控球率62%，高位压迫让琴斯托霍瓦完全出不来球，高质量的主场表演。"},
          {"username": "足球移民日记", "tag": "波兰华人", "likes": 156, "content": "来奥波莱看球了！现场氛围太好了！中国教练打出这种攻势球确实骄傲！"}
        ]
      }
    },
    "formation": "4-1-1-4 (双翼齐飞)",
    "lineup": [
      {"pos": "GK", "name": "姆莱奇科", "name_zh": "米沃什·姆莱奇科", "name_en": "Miłosz Mleczko", "number": 1, "rating": 7.0, "min": 90, "saves": 3, "is_mvp": False,
       "radar": [{"subject":"极限扑救","value":78},{"subject":"防守选位","value":76},{"subject":"出击果断","value":72},{"subject":"禁区制空","value":80},{"subject":"防线指挥","value":75},{"subject":"心理抗压","value":76}],
       "stats": {"关键扑救":"2次","禁区内救险":"1次","传球成功率":"79%","长传到位":"6次","失球":"1球","评分":"7.0分"}},
      {"pos": "DR", "name": "铃木淳也", "name_zh": "铃木淳也", "name_en": "Junya Suzuki", "number": 2, "rating": 0, "min": 12, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":78},{"subject":"抢断拦截","value":72},{"subject":"边路传中","value":70},{"subject":"回追速度","value":81},{"subject":"防守纪律","value":75},{"subject":"对抗成功","value":71}],
       "stats": {"出场时间":"12分钟(替补)","评分":"替补出场"}},
      {"pos": "DC1", "name": "普里维特", "name_zh": "普里维特", "name_en": "Andrew Privett", "number": 5, "rating": 6.7, "min": 90, "is_mvp": False,
       "radar": [{"subject":"高空争顶","value":80},{"subject":"正面拦截","value":78},{"subject":"禁区解围","value":84},{"subject":"身体对抗","value":82},{"subject":"出球传导","value":71},{"subject":"位置感","value":76}],
       "stats": {"高空争顶":"4/5","关键解围":"4次","封堵射门":"1次","传球成功率":"84%","犯规":"0次","对抗胜率":"80%"}},
      {"pos": "DC2", "name": "希尔马", "name_zh": "希尔马", "name_en": "Jilmar", "number": 6, "rating": 7.0, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":76},{"subject":"禁区争顶","value":74},{"subject":"补位意识","value":75},{"subject":"贴身逼抢","value":78},{"subject":"长传发起","value":68},{"subject":"回追速度","value":70}],
       "stats": {"关键解围":"3次","成功拦截":"2次","身体拼抢":"4/6","争顶胜率":"70%","犯规":"1次","黄牌":"0"}},
      {"pos": "DL", "name": "帕拉茨", "name_zh": "帕拉茨", "name_en": "Krystian Palacz", "number": 3, "rating": 6.7, "min": 78, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":74},{"subject":"抢断拦截","value":76},{"subject":"边路传中","value":72},{"subject":"回追速度","value":78},{"subject":"防守纪律","value":77},{"subject":"对抗成功","value":73}],
       "stats": {"出场时间":"78分钟","传中":"2/5","成功抢断":"3次","跑动距离":"8.2km","评分":"6.7分"}},
      {"pos": "DM", "name": "卡斯普日克", "name_zh": "卡斯普日克", "name_en": "Kacper Przybyłko", "number": 8, "rating": 7.0, "min": 78, "is_mvp": False,
       "radar": [{"subject":"传球节奏","value":76},{"subject":"防守覆盖","value":74},{"subject":"高空争顶","value":72},{"subject":"技术盘带","value":70},{"subject":"前场压迫","value":78},{"subject":"体能跑动","value":80}],
       "stats": {"出场时间":"78分钟","传球成功率":"82%","关键传球":"1次","成功抢断":"2次","跑动距离":"9.1km","评分":"7.0分"}},
      {"pos": "AM", "name": "斯皮哈瓦", "name_zh": "斯皮哈瓦", "name_en": "Mateusz Spychała", "number": 10, "rating": 7.7, "min": 78, "is_mvp": False,
       "radar": [{"subject":"传球视野","value":80},{"subject":"精准直塞","value":78},{"subject":"技术盘带","value":76},{"subject":"前场压迫","value":74},{"subject":"射门威胁","value":72},{"subject":"位置感","value":79}],
       "stats": {"出场时间":"78分钟","关键传球":"3次","传球成功率":"87%","射门":"1次","评分":"7.7分"}},
      {"pos": "WR", "name": "希什", "name_zh": "帕特里克·希什", "name_en": "Patryk Szysz", "number": 7, "rating": 8.5, "min": 84, "is_mvp": True,
       "radar": [{"subject":"边路突破","value":84},{"subject":"传中精准","value":82},{"subject":"快速起步","value":85},{"subject":"内切射门","value":76},{"subject":"无球跑位","value":80},{"subject":"防守贡献","value":68}],
       "stats": {"出场时间":"84分钟","助攻":"2次","传中":"4/7","过人成功":"4次","跑动距离":"9.8km","评分":"8.5分"}},
      {"pos": "WL", "name": "帕拉茨", "name_zh": "卡斯帕尔", "name_en": "Krystian Palacz", "number": 3, "rating": 6.7, "min": 78, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":74},{"subject":"传中精准","value":70},{"subject":"快速起步","value":76},{"subject":"内切射门","value":72},{"subject":"无球跑位","value":75},{"subject":"防守贡献","value":72}],
       "stats": {"出场时间":"78分钟","助攻":"0次","传中":"3/6","过人成功":"2次","评分":"6.7分"}},
      {"pos": "ST1", "name": "索拉迪奥", "name_zh": "乔丹·索拉迪奥", "name_en": "Jordy Soladio", "number": 9, "rating": 9.0, "min": 90, "is_mvp": True, "goals": 2,
       "radar": [{"subject":"禁区把握","value":88},{"subject":"高空争顶","value":80},{"subject":"背身拿球","value":78},{"subject":"快速反应","value":84},{"subject":"传球出球","value":72},{"subject":"射门力量","value":85}],
       "stats": {"进球":"2球","射门":"5次","射正":"4次","对抗胜率":"65%","跑动距离":"9.4km","评分":"9.0分"}},
      {"pos": "ST2", "name": "迪奥内", "name_zh": "巴巴卡尔·迪奥内", "name_en": "Babacar Dione", "number": 11, "rating": 7.2, "min": 76, "is_mvp": False, "goals": 1,
       "radar": [{"subject":"技术突破","value":78},{"subject":"禁区射门","value":76},{"subject":"无球跑位","value":80},{"subject":"高速冲击","value":82},{"subject":"边路下底","value":79},{"subject":"传球出球","value":70}],
       "stats": {"进球":"1球","射门":"3次","射正":"2次","过人成功":"3次","助攻":"0次","评分":"7.2分"}}
    ],
    "war_report": "主场大胜！门将姆莱奇科稳守球门，后防线高效清道。希什右翼连续撕扯制造两个进球，斯皮哈瓦居中串联分球精准。索拉迪奥打入双响，全场最高9.0分摘得最佳球员，迪奥内和加伊达也各建一功。整体控球62%，16脚射门9脚射正，是本赛季最具说服力的一场主场胜利！"
  },

  {
    "id": 1005,
    "league_key": "pol_d1",
    "league_name": "波甲",
    "league_badge": "波甲",
    "league_flag": "circle-flags:pl",
    "round": 5,
    "round_label": "第 5 轮",
    "date": "2026-08-16 18:00",
    "date_short": "08-16 周日",
    "status": "FT",
    "status_label": "完赛",
    "is_overseas": True,
    "home_team": "奥波莱奥德拉",
    "home_code": "ODR",
    "away_team": "罗兹维泽夫",
    "away_code": "WID",
    "score_home": 4,
    "score_away": 0,
    "stadium": "奥波莱市政球场",
    "xg": "3.20 - 0.40",
    "shots": "18",
    "shots_on_target": "11",
    "distance_km": "0",
    "scorers": [
      {"minute": 22, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥", "assist": "卡克斯特尔·帕拉茨", "assist_zh": "帕拉茨"},
      {"minute": 44, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥"},
      {"minute": 63, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔"},
      {"minute": 78, "player": "巴巴卡尔·迪奥内", "player_zh": "迪奥内", "assist": "弗朗契斯扎克·弗兰恰克", "assist_zh": "弗兰恰克"}
    ],
    "news": {
      "title": "主场4-0大捷！奥波莱零封罗兹维泽夫，索拉迪奥再次双响五连不败领跑波甲",
      "summary": "主场完胜！零封对手，索拉迪奥双响，五轮13球仅失5球，奥波莱领跑波甲升级区！",
      "reporter": "懂球云波兰特派",
      "dongqiudi_article": {
        "title": "主场4-0大捷！奥波莱零封罗兹维泽夫，索拉迪奥再次双响五连不败领跑波甲",
        "summary": "零封4-0大胜，索拉迪奥波甲7球连续双响，5轮不败13球领跑升级区！",
        "body": "【比赛焦点】\n波甲第5轮，奥波莱坐镇主场迎战同为升级热门的罗兹维泽夫。徐指导维持高强度双翼体系，本场换上多西科特等青训力量配合首发阵容压制对手。\n\n【关键事件】\n第22分钟，帕拉茨左路快速下底传中，索拉迪奥后插上推射破门！先声夺人！\n第44分钟，补时前索拉迪奥禁区内凌空抽射！双响到手，半场已领先2-0！\n第63分钟，卡克佩尔·普日比乌科获传球后门前精准推射，扩大比分至3-0。\n第78分钟，弗兰恰克替补登场后立刻送出精准直塞，迪奥内单刀冷静推射，4-0完全锁定胜局。\n\n【战术复盘】\n本场零封展现了奥波莱完整的战术素养。高位压迫让维泽夫完全无法出球，15人阵容轮转均完成了各自任务。这是赛季最具统治力的一场胜利。",
        "tags": ["波甲", "奥波莱奥德拉", "主场大捷", "零封", "五连不败"]
      },
      "local_media_snippet": {
        "outlet": "波兰足球杂志《Piłka Nożna》",
        "country_flag": "circle-flags:pl",
        "journalist": "Marcin Lepa",
        "quote": "奥波莱令人窒息的高位压迫完全压制了罗兹维泽夫的出球路线，中国主帅的战术布置无可挑剔。这支球队以冠军级别的强度在踢波甲！"
      },
      "hupu_thread": {
        "coach_score": 9.5,
        "comments": [
          {"username": "西里西亚铁血军", "tag": "主场铁杆", "likes": 445, "content": "4-0！零封！五连不败！我在现场！这根本不像在踢甲级联赛，更像在踢欧洲赛！"},
          {"username": "奥波莱分析师", "tag": "数据控", "likes": 356, "content": "15轮13球失5球，索拉迪奥个人7球。这个数据放在整个欧洲小联赛里都是顶级了。"},
          {"username": "跨国看球记", "tag": "海外华人", "likes": 287, "content": "徐指导这赛季打法太流畅了！多条进攻线全部激活，对方完全不知道防哪里。"},
          {"username": "足球理工男", "tag": "FM战术师", "likes": 198, "content": "换人时机完美，弗兰恰克替补进场直接助攻，徐指导对球员状态的感知力一流。"}
        ]
      }
    },
    "formation": "4-1-1-4 (双翼齐飞)",
    "lineup": [
      {"pos": "GK", "name": "姆莱奇科", "name_zh": "米沃什·姆莱奇科", "name_en": "Miłosz Mleczko", "number": 1, "rating": 7.5, "min": 90, "saves": 1, "is_mvp": False,
       "radar": [{"subject":"极限扑救","value":78},{"subject":"防守选位","value":76},{"subject":"出击果断","value":72},{"subject":"禁区制空","value":80},{"subject":"防线指挥","value":75},{"subject":"心理抗压","value":76}],
       "stats": {"关键扑救":"1次","禁区内救险":"1次","传球成功率":"82%","长传到位":"7次","失球":"0球","评分":"7.5分"}},
      {"pos": "DR", "name": "多恩科尔", "name_zh": "贾基·多恩科尔", "name_en": "Jacky Donkor", "number": 14, "rating": 7.4, "min": 90, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":76},{"subject":"抢断拦截","value":74},{"subject":"边路传中","value":72},{"subject":"回追速度","value":79},{"subject":"防守纪律","value":77},{"subject":"对抗成功","value":74}],
       "stats": {"出场时间":"90分钟","助攻":"1次","传中":"3/6","成功抢断":"2次","跑动距离":"9.3km","评分":"7.4分"}},
      {"pos": "DC1", "name": "伊安诺尼", "name_zh": "伊安诺尼", "name_en": "Edoardo Iannoni", "number": 4, "rating": 7.0, "min": 90, "is_mvp": False,
       "radar": [{"subject":"高空争顶","value":76},{"subject":"正面拦截","value":80},{"subject":"禁区解围","value":78},{"subject":"身体对抗","value":79},{"subject":"出球传导","value":74},{"subject":"位置感","value":77}],
       "stats": {"高空争顶":"3/4","关键解围":"3次","封堵射门":"2次","传球成功率":"80%","犯规":"0次","对抗胜率":"77%"}},
      {"pos": "DC2", "name": "希尔马", "name_zh": "希尔马", "name_en": "Jilmar", "number": 6, "rating": 7.6, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":76},{"subject":"禁区争顶","value":74},{"subject":"补位意识","value":75},{"subject":"贴身逼抢","value":78},{"subject":"长传发起","value":68},{"subject":"回追速度","value":70}],
       "stats": {"关键解围":"4次","成功拦截":"3次","身体拼抢":"5/6","争顶胜率":"72%","犯规":"0次","黄牌":"0"}},
      {"pos": "DL", "name": "帕拉茨", "name_zh": "帕拉茨", "name_en": "Krystian Palacz", "number": 3, "rating": 8.7, "min": 90, "is_mvp": True,
       "radar": [{"subject":"边路插上","value":84},{"subject":"抢断拦截","value":76},{"subject":"边路传中","value":80},{"subject":"回追速度","value":78},{"subject":"防守纪律","value":77},{"subject":"对抗成功","value":73}],
       "stats": {"出场时间":"90分钟","助攻":"2次","传中":"5/8","成功抢断":"3次","跑动距离":"10.2km","评分":"8.7分"}},
      {"pos": "DM", "name": "苏基恩尼茨基", "name_zh": "苏基恩尼茨基", "name_en": "Alan Sukiennicki", "number": 20, "rating": 6.9, "min": 90, "is_mvp": False,
       "radar": [{"subject":"传球节奏","value":74},{"subject":"防守覆盖","value":78},{"subject":"高空争顶","value":70},{"subject":"技术盘带","value":68},{"subject":"前场压迫","value":76},{"subject":"体能跑动","value":82}],
       "stats": {"出场时间":"90分钟","传球成功率":"80%","关键传球":"1次","成功抢断":"3次","跑动距离":"9.8km","评分":"6.9分"}},
      {"pos": "AM", "name": "斯皮哈瓦", "name_zh": "斯皮哈瓦", "name_en": "Mateusz Spychała", "number": 10, "rating": 6.9, "min": 90, "is_mvp": False,
       "radar": [{"subject":"传球视野","value":80},{"subject":"精准直塞","value":78},{"subject":"技术盘带","value":76},{"subject":"前场压迫","value":74},{"subject":"射门威胁","value":72},{"subject":"位置感","value":79}],
       "stats": {"出场时间":"90分钟","关键传球":"2次","传球成功率":"85%","射门":"1次","评分":"6.9分"}},
      {"pos": "WR", "name": "库普奇克", "name_zh": "库普奇克", "name_en": "Filip Kupczyk", "number": 17, "rating": 6.7, "min": 90, "is_mvp": False,
       "radar": [{"subject":"边路突破","value":76},{"subject":"传中精准","value":74},{"subject":"快速起步","value":78},{"subject":"内切射门","value":70},{"subject":"无球跑位","value":75},{"subject":"防守贡献","value":70}],
       "stats": {"出场时间":"90分钟","传中":"3/7","过人成功":"3次","跑动距离":"9.5km","评分":"6.7分"}},
      {"pos": "WL", "name": "帕拉茨", "name_zh": "卡斯帕尔", "name_en": "Krystian Palacz", "number": 3, "rating": 8.7, "min": 90, "is_mvp": True,
       "radar": [{"subject":"边路插上","value":84},{"subject":"传中精准","value":80},{"subject":"快速起步","value":78},{"subject":"内切射门","value":72},{"subject":"无球跑位","value":75},{"subject":"防守贡献","value":72}],
       "stats": {"出场时间":"90分钟","助攻":"2次","传中":"5/8","过人成功":"4次","评分":"8.7分"}},
      {"pos": "ST1", "name": "索拉迪奥", "name_zh": "乔丹·索拉迪奥", "name_en": "Jordy Soladio", "number": 9, "rating": 8.3, "min": 90, "is_mvp": True, "goals": 2,
       "radar": [{"subject":"禁区把握","value":88},{"subject":"高空争顶","value":80},{"subject":"背身拿球","value":78},{"subject":"快速反应","value":84},{"subject":"传球出球","value":72},{"subject":"射门力量","value":85}],
       "stats": {"进球":"2球","射门":"6次","射正":"5次","对抗胜率":"68%","跑动距离":"9.6km","评分":"8.3分"}},
      {"pos": "ST2", "name": "卡克佩尔", "name_zh": "卡克佩尔·普日比乌科", "name_en": "Kacper Przybyłko", "number": 11, "rating": 7.6, "min": 90, "is_mvp": False, "goals": 1,
       "radar": [{"subject":"技术突破","value":76},{"subject":"禁区射门","value":80},{"subject":"无球跑位","value":78},{"subject":"高速冲击","value":74},{"subject":"边路下底","value":72},{"subject":"传球出球","value":72}],
       "stats": {"进球":"1球","射门":"4次","射正":"3次","过人成功":"2次","助攻":"0次","评分":"7.6分"}}
    ],
    "war_report": "主场完胜！门将姆莱奇科稳操胜券，全场仅遭受一次危险冲击便顺利化解。左路帕拉茨全场最佳8.7分，两次致命传中创造两球。索拉迪奥波甲个人进球达到7球，再次双响后势如破竹。整体控球率65%，高位压迫让罗兹维泽夫几乎全场无法出球。五连不败，奥波莱是本赛季波甲的绝对主角！"
  },

  {
    "id": 1006,
    "league_key": "pol_d1",
    "league_name": "波甲",
    "league_badge": "波甲",
    "league_flag": "circle-flags:pl",
    "round": 6,
    "round_label": "第 6 轮",
    "date": "2026-08-23 16:00",
    "date_short": "08-23 周日",
    "status": "FT",
    "status_label": "完赛",
    "is_overseas": True,
    "home_team": "弗罗茨瓦夫西里西亚",
    "home_code": "SLA",
    "away_team": "奥波莱奥德拉",
    "away_code": "ODR",
    "score_home": 0,
    "score_away": 1,
    "stadium": "塔尔奇纳运动场",
    "xg": "0.90 - 1.30",
    "shots": "14",
    "shots_on_target": "5",
    "distance_km": "72.4",
    "scorers": [
      {"minute": 61, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "阿德里安·利贝尔", "assist_zh": "利贝尔"}
    ],
    "news": {
      "title": "客场1-0险胜西里西亚！卡克佩尔下半场世界波，奥波莱六连不败独跑波甲榜首",
      "summary": "高难度客场，全场仅一脚射正，卡克佩尔61分钟世界波一球定音，奥波莱六连不败登顶！",
      "reporter": "懂球云波兰特派",
      "dongqiudi_article": {
        "title": "客场1-0险胜西里西亚！卡克佩尔下半场世界波，奥波莱六连不败独跑波甲榜首",
        "summary": "高难度客场，卡克佩尔61分钟世界波一球定鼎，姆莱奇科稳守关键扑救，六连不败登顶！",
        "body": "【比赛焦点】\n波甲第6轮，奥波莱客场挑战传统豪强弗罗茨瓦夫西里西亚。对方主场氛围狂热，徐指导选择稳守反击，以高强度压迫限制主队进攻节奏。\n\n【关键事件】\n上半场双方势均力敌，姆莱奇科数次关键扑救将比赛拖入平局。\n第61分钟，利贝尔右路斜传入禁区，卡克佩尔普日比乌科接球后禁区弧顶不停球直接怒射，皮球划弧入门，完美世界波！\n此后奥波莱成功顶住西里西亚的反扑，以1-0完成客场告捷！\n\n【战术复盘】\n本场是典型的低位防反战术成功案例。徐指导选择在客场收缩防线，依靠高速反击和个人能力赢得比赛。姆莱奇科本场是当之无愧的英雄，全场7次扑救让西里西亚无功而返。",
        "tags": ["波甲", "奥波莱奥德拉", "客场告捷", "卡克佩尔", "六连不败", "榜首"]
      },
      "local_media_snippet": {
        "outlet": "弗罗茨瓦夫《Gazeta Wrocławska》",
        "country_flag": "circle-flags:pl",
        "journalist": "Krzysztof Nowak",
        "quote": "奥波莱奥德拉今日展现了冠军级别的防反能力。在西里西亚主场巨大压力下，他们仅靠一脚世界波完成了高质量的客场告捷。这支球队的抗压能力令人叹服。"
      },
      "hupu_thread": {
        "coach_score": 9.0,
        "comments": [
          {"username": "波兰追球人", "tag": "西里西亚球迷", "likes": 523, "content": "客场1-0！六连不败！姆莱奇科今天真的封神了，7次扑救一球不失！"},
          {"username": "战术观察站", "tag": "FM战术师", "likes": 398, "content": "徐指导今天的客场布置教科书级别：收缩防线、高速反击、一击制敌，完美防反。"},
          {"username": "卡克佩尔真爱粉", "tag": "普日比乌科球迷", "likes": 312, "content": "那脚世界波！！！！禁区弧顶不停球直接抽射，这就是波甲级别的技术！"},
          {"username": "足球移民日记", "tag": "波兰华人", "likes": 234, "content": "六连不败！独跑榜首！中国教练组在欧洲写下传奇！身边的波兰朋友都在聊奥波莱！"}
        ]
      }
    },
    "formation": "4-1-1-4 (双翼齐飞)",
    "lineup": [
      {"pos": "GK", "name": "姆莱奇科", "name_zh": "米沃什·姆莱奇科", "name_en": "Miłosz Mleczko", "number": 1, "rating": 7.3, "min": 90, "saves": 7, "is_mvp": True,
       "radar": [{"subject":"极限扑救","value":82},{"subject":"防守选位","value":80},{"subject":"出击果断","value":75},{"subject":"禁区制空","value":80},{"subject":"防线指挥","value":75},{"subject":"心理抗压","value":84}],
       "stats": {"关键扑救":"7次","禁区内救险":"4次","传球成功率":"74%","长传到位":"5次","失球":"0球","评分":"7.3分"}},
      {"pos": "DR", "name": "铃木淳也", "name_zh": "铃木淳也", "name_en": "Junya Suzuki", "number": 2, "rating": 6.8, "min": 78, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":78},{"subject":"抢断拦截","value":72},{"subject":"边路传中","value":70},{"subject":"回追速度","value":81},{"subject":"防守纪律","value":75},{"subject":"对抗成功","value":71}],
       "stats": {"出场时间":"78分钟","传中":"1/3","成功抢断":"2次","跑动距离":"7.8km","评分":"6.8分"}},
      {"pos": "DC1", "name": "伊安诺尼", "name_zh": "伊安诺尼", "name_en": "Edoardo Iannoni", "number": 4, "rating": 7.4, "min": 90, "is_mvp": False,
       "radar": [{"subject":"高空争顶","value":76},{"subject":"正面拦截","value":80},{"subject":"禁区解围","value":78},{"subject":"身体对抗","value":79},{"subject":"出球传导","value":74},{"subject":"位置感","value":77}],
       "stats": {"高空争顶":"6/8","关键解围":"7次","封堵射门":"3次","传球成功率":"77%","犯规":"1次","对抗胜率":"80%"}},
      {"pos": "DC2", "name": "米尤什科维奇", "name_zh": "米尤什科维奇", "name_en": "Nemanja Mijušković", "number": 15, "rating": 7.0, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":78},{"subject":"禁区争顶","value":76},{"subject":"补位意识","value":77},{"subject":"贴身逼抢","value":80},{"subject":"长传发起","value":70},{"subject":"回追速度","value":72}],
       "stats": {"关键解围":"5次","成功拦截":"3次","身体拼抢":"6/8","争顶胜率":"75%","犯规":"1次","黄牌":"0"}},
      {"pos": "DL", "name": "希尔马", "name_zh": "希尔马", "name_en": "Jilmar", "number": 6, "rating": 7.1, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":76},{"subject":"禁区争顶","value":74},{"subject":"补位意识","value":75},{"subject":"贴身逼抢","value":78},{"subject":"长传发起","value":68},{"subject":"回追速度","value":70}],
       "stats": {"关键解围":"3次","成功拦截":"2次","身体拼抢":"4/5","争顶胜率":"70%","犯规":"0次","黄牌":"0"}},
      {"pos": "DM", "name": "库普奇克", "name_zh": "库普奇克", "name_en": "Filip Kupczyk", "number": 17, "rating": 6.1, "min": 90, "is_mvp": False,
       "radar": [{"subject":"传球节奏","value":70},{"subject":"防守覆盖","value":74},{"subject":"高空争顶","value":68},{"subject":"技术盘带","value":66},{"subject":"前场压迫","value":72},{"subject":"体能跑动","value":80}],
       "stats": {"出场时间":"90分钟","传球成功率":"76%","关键传球":"0次","成功抢断":"2次","跑动距离":"10.1km","评分":"6.1分"}},
      {"pos": "AM", "name": "希什", "name_zh": "帕特里克·希什", "name_en": "Patryk Szysz", "number": 7, "rating": 6.9, "min": 78, "is_mvp": False,
       "radar": [{"subject":"传球视野","value":78},{"subject":"精准直塞","value":76},{"subject":"技术盘带","value":74},{"subject":"前场压迫","value":74},{"subject":"射门威胁","value":72},{"subject":"位置感","value":77}],
       "stats": {"出场时间":"78分钟","关键传球":"1次","传球成功率":"82%","射门":"1次","评分":"6.9分"}},
      {"pos": "WR", "name": "利贝尔", "name_zh": "阿德里安·利贝尔", "name_en": "Adrian Liber", "number": 8, "rating": 7.1, "min": 90, "is_mvp": False,
       "radar": [{"subject":"边路突破","value":76},{"subject":"传中精准","value":78},{"subject":"快速起步","value":74},{"subject":"内切射门","value":70},{"subject":"无球跑位","value":73},{"subject":"防守贡献","value":72}],
       "stats": {"出场时间":"90分钟","助攻":"1次","传中":"4/7","过人成功":"2次","跑动距离":"9.2km","评分":"7.1分"}},
      {"pos": "WL", "name": "帕拉茨", "name_zh": "卡斯帕尔", "name_en": "Krystian Palacz", "number": 3, "rating": 6.6, "min": 78, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":74},{"subject":"传中精准","value":70},{"subject":"快速起步","value":76},{"subject":"内切射门","value":72},{"subject":"无球跑位","value":75},{"subject":"防守贡献","value":72}],
       "stats": {"出场时间":"78分钟","传中":"2/5","过人成功":"1次","评分":"6.6分"}},
      {"pos": "ST1", "name": "索拉迪奥", "name_zh": "乔丹·索拉迪奥", "name_en": "Jordy Soladio", "number": 9, "rating": 6.4, "min": 90, "is_mvp": False,
       "radar": [{"subject":"禁区把握","value":88},{"subject":"高空争顶","value":80},{"subject":"背身拿球","value":78},{"subject":"快速反应","value":84},{"subject":"传球出球","value":72},{"subject":"射门力量","value":85}],
       "stats": {"进球":"0球","射门":"2次","射正":"0次","对抗胜率":"58%","跑动距离":"8.6km","评分":"6.4分"}},
      {"pos": "ST2", "name": "卡克佩尔", "name_zh": "卡克佩尔·普日比乌科", "name_en": "Kacper Przybyłko", "number": 11, "rating": 7.6, "min": 90, "is_mvp": False, "goals": 1,
       "radar": [{"subject":"技术突破","value":76},{"subject":"禁区射门","value":80},{"subject":"无球跑位","value":78},{"subject":"高速冲击","value":74},{"subject":"边路下底","value":72},{"subject":"传球出球","value":72}],
       "stats": {"进球":"1球","射门":"3次","射正":"1次","过人成功":"1次","助攻":"0次","评分":"7.6分"}}
    ],
    "war_report": "客场铁桶阵成功！门将姆莱奇科今晚化身球队救星，7次扑救封锁西里西亚所有威胁，零封对手当之无愧本场最佳。后防线在利贝尔和米尤什科维奇的铁闸组合下坚不可摧。卡克佩尔61分钟一脚禁区弧顶世界波一球定鼎，客场1-0登顶波甲！六连不败、领跑升级区！"
  },

  {
    "id": 1007,
    "league_key": "pol_d1",
    "league_name": "波甲",
    "league_badge": "波甲",
    "league_flag": "circle-flags:pl",
    "round": 7,
    "round_label": "第 7 轮",
    "date": "2026-08-30 18:00",
    "date_short": "08-30 周日",
    "status": "FT",
    "status_label": "完赛",
    "is_overseas": True,
    "home_team": "奥波莱奥德拉",
    "home_code": "ODR",
    "away_team": "扎布热戈尔尼克",
    "away_code": "ZAG",
    "score_home": 4,
    "score_away": 3,
    "stadium": "奥波莱市政球场",
    "xg": "3.10 - 2.40",
    "shots": "17",
    "shots_on_target": "9",
    "distance_km": "0",
    "scorers": [
      {"minute": 11, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥", "assist": "卡克佩尔·普日比乌科", "assist_zh": "卡克佩尔"},
      {"minute": 29, "player": "伊多阿多·伊安诺尼", "player_zh": "伊安诺尼", "assist": "贾基·多恩科尔", "assist_zh": "多恩科尔"},
      {"minute": 58, "player": "卡克佩尔·普日比乌科", "player_zh": "卡克佩尔", "assist": "乔丹·索拉迪奥", "assist_zh": "索拉迪奥"},
      {"minute": 83, "player": "乔丹·索拉迪奥", "player_zh": "索拉迪奥", "assist": "贾基·多恩科尔", "assist_zh": "多恩科尔", "is_mvp_goal": True, "is_stoppage": False}
    ],
    "news": {
      "title": "主场惊天4-3大战！奥波莱逆转告捷七连不败，索拉迪奥双响普日比乌科7轮10球大爆发",
      "summary": "七轮最激烈之战！奥波莱领先、被追平、再反超，九场不败波甲升级区第一！",
      "reporter": "懂球云波兰特派",
      "dongqiudi_article": {
        "title": "主场惊天4-3大战！奥波莱逆转告捷七连不败，索拉迪奥双响普日比乌科7轮10球大爆发",
        "summary": "7进4-3战胜扎布热，索拉迪奥双响，七连不败依然领跑！本赛季最具观赏性的一役！",
        "body": "【比赛焦点】\n波甲第7轮，奥波莱坐镇主场迎战欲打破其不败的扎布热戈尔尼克。本场进行了多达7球的超级大战，扣人心弦至最后一刻。\n\n【关键事件】\n第11分钟，卡克佩尔精准直塞，索拉迪奥禁区内单刀推射破门！1-0！\n第29分钟，多恩科尔右路传中，伊安诺尼禁区内争顶头球破门！2-0！\n上半场结束后客队两度扳平，奥波莱一度领先又被追平，下半场精彩继续。\n第58分钟，索拉迪奥禁区左侧打门被扑出后反弹，卡克佩尔补射入网！3-2反超！\n第83分钟，多恩科尔右路斜传，索拉迪奥后插上推射锁定4-3！\n客队最后时刻再次扳回一城，4-3惊险告捷！\n\n【战术复盘】\n本场展示了奥波莱在逆境中的大心脏。多次被追平后仍能找到进球，徐指导的换人调度功不可没。索拉迪奥双响、卡克佩尔助攻+进球，前场组合配合日臻成熟。7连不败，奥波莱是本赛季波甲最强的升级候选！",
        "tags": ["波甲", "奥波莱奥德拉", "主场激战", "七连不败", "索拉迪奥", "普日比乌科"]
      },
      "local_media_snippet": {
        "outlet": "波兰体育周刊《Przegląd Sportowy》",
        "country_flag": "circle-flags:pl",
        "journalist": "Tomasz Włodarczyk",
        "quote": "七球大战！奥波莱用七轮不败证明了自己是本赛季波甲最有资格冲超的球队。索拉迪奥与普日比乌科的前锋组合，将是整个赛季甲级联赛最锋利的双箭头！"
      },
      "hupu_thread": {
        "coach_score": 9.2,
        "comments": [
          {"username": "西里西亚铁血军", "tag": "主场铁杆", "likes": 678, "content": "4-3！七球大战！最后一脚索拉迪奥推射进去的时候全场炸了！我在现场见证！"},
          {"username": "卡克佩尔真爱粉", "tag": "普日比乌科球迷", "likes": 512, "content": "七轮10球！这赛季卡克佩尔真的完全被激活了！中国教练的战术让他找到了真正的位置！"},
          {"username": "奥波莱分析师", "tag": "数据控", "likes": 423, "content": "7连不败，20得分，17进球6失球。这个数据放欧洲各国甲级里都是顶级。徐指导真的厉害！"},
          {"username": "足球理工男", "tag": "FM战术师", "likes": 334, "content": "被追平两次还能重新拿回比赛，心态和阵型调整都很关键。徐指导临场能力被证明了。"},
          {"username": "海外奥波莱迷", "tag": "海外球迷", "likes": 267, "content": "7轮全不败！这就是我关注的球队！在波兰写下中国足球留洋的最好故事！"}
        ]
      }
    },
    "formation": "4-1-1-4 (双翼齐飞)",
    "lineup": [
      {"pos": "GK", "name": "姆莱奇科", "name_zh": "米沃什·姆莱奇科", "name_en": "Miłosz Mleczko", "number": 1, "rating": 6.6, "min": 90, "saves": 5, "is_mvp": False,
       "radar": [{"subject":"极限扑救","value":78},{"subject":"防守选位","value":76},{"subject":"出击果断","value":72},{"subject":"禁区制空","value":80},{"subject":"防线指挥","value":75},{"subject":"心理抗压","value":76}],
       "stats": {"关键扑救":"5次","禁区内救险":"3次","传球成功率":"72%","长传到位":"5次","失球":"3球","评分":"6.6分"}},
      {"pos": "DR", "name": "多恩科尔", "name_zh": "贾基·多恩科尔", "name_en": "Jacky Donkor", "number": 14, "rating": 7.3, "min": 75, "is_mvp": False,
       "radar": [{"subject":"边路插上","value":76},{"subject":"抢断拦截","value":74},{"subject":"边路传中","value":74},{"subject":"回追速度","value":79},{"subject":"防守纪律","value":77},{"subject":"对抗成功","value":74}],
       "stats": {"出场时间":"75分钟","助攻":"2次","传中":"4/7","成功抢断":"2次","跑动距离":"8.4km","评分":"7.3分"}},
      {"pos": "DC1", "name": "伊安诺尼", "name_zh": "伊安诺尼", "name_en": "Edoardo Iannoni", "number": 4, "rating": 6.8, "min": 90, "is_mvp": False, "goals": 1,
       "radar": [{"subject":"高空争顶","value":76},{"subject":"正面拦截","value":80},{"subject":"禁区解围","value":78},{"subject":"身体对抗","value":79},{"subject":"出球传导","value":74},{"subject":"位置感","value":77}],
       "stats": {"进球":"1球","高空争顶":"5/7","关键解围":"4次","封堵射门":"1次","传球成功率":"76%","对抗胜率":"74%"}},
      {"pos": "DC2", "name": "米尤什科维奇", "name_zh": "米尤什科维奇", "name_en": "Nemanja Mijušković", "number": 15, "rating": 6.6, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":78},{"subject":"禁区争顶","value":76},{"subject":"补位意识","value":77},{"subject":"贴身逼抢","value":80},{"subject":"长传发起","value":70},{"subject":"回追速度","value":72}],
       "stats": {"关键解围":"3次","成功拦截":"2次","身体拼抢":"5/7","争顶胜率":"71%","犯规":"2次","黄牌":"1"}},
      {"pos": "DL", "name": "希尔马", "name_zh": "希尔马", "name_en": "Jilmar", "number": 6, "rating": 6.6, "min": 90, "is_mvp": False,
       "radar": [{"subject":"正面防守","value":76},{"subject":"禁区争顶","value":74},{"subject":"补位意识","value":75},{"subject":"贴身逼抢","value":78},{"subject":"长传发起","value":68},{"subject":"回追速度","value":70}],
       "stats": {"关键解围":"2次","成功拦截":"1次","身体拼抢":"3/5","争顶胜率":"65%","犯规":"1次","黄牌":"0"}},
      {"pos": "DM", "name": "帕拉茨", "name_zh": "帕拉茨", "name_en": "Krystian Palacz", "number": 3, "rating": 7.0, "min": 90, "is_mvp": False,
       "radar": [{"subject":"传球节奏","value":76},{"subject":"防守覆盖","value":74},{"subject":"高空争顶","value":72},{"subject":"技术盘带","value":70},{"subject":"前场压迫","value":78},{"subject":"体能跑动","value":80}],
       "stats": {"出场时间":"90分钟","传球成功率":"80%","关键传球":"1次","成功抢断":"2次","跑动距离":"9.5km","评分":"7.0分"}},
      {"pos": "AM", "name": "希什", "name_zh": "帕特里克·希什", "name_en": "Patryk Szysz", "number": 7, "rating": 7.2, "min": 75, "is_mvp": False,
       "radar": [{"subject":"传球视野","value":80},{"subject":"精准直塞","value":78},{"subject":"技术盘带","value":76},{"subject":"前场压迫","value":74},{"subject":"射门威胁","value":72},{"subject":"位置感","value":79}],
       "stats": {"出场时间":"75分钟","关键传球":"2次","传球成功率":"84%","射门":"1次","评分":"7.2分"}},
      {"pos": "WR", "name": "斯皮哈瓦", "name_zh": "斯皮哈瓦", "name_en": "Mateusz Spychała", "number": 10, "rating": 7.1, "min": 75, "is_mvp": False,
       "radar": [{"subject":"边路突破","value":74},{"subject":"传中精准","value":72},{"subject":"快速起步","value":76},{"subject":"内切射门","value":70},{"subject":"无球跑位","value":75},{"subject":"防守贡献","value":70}],
       "stats": {"出场时间":"75分钟","传中":"2/5","过人成功":"2次","跑动距离":"7.8km","评分":"7.1分"}},
      {"pos": "WL", "name": "卡克佩尔", "name_zh": "卡克佩尔·普日比乌科", "name_en": "Kacper Przybyłko", "number": 11, "rating": 9.4, "min": 88, "is_mvp": True, "goals": 1,
       "radar": [{"subject":"技术突破","value":82},{"subject":"禁区射门","value":88},{"subject":"无球跑位","value":84},{"subject":"高速冲击","value":80},{"subject":"边路下底","value":78},{"subject":"传球出球","value":76}],
       "stats": {"进球":"1球","助攻":"2次","射门":"5次","射正":"4次","过人成功":"3次","评分":"9.4分"}},
      {"pos": "ST1", "name": "索拉迪奥", "name_zh": "乔丹·索拉迪奥", "name_en": "Jordy Soladio", "number": 9, "rating": 9.2, "min": 90, "is_mvp": True, "goals": 2,
       "radar": [{"subject":"禁区把握","value":90},{"subject":"高空争顶","value":80},{"subject":"背身拿球","value":80},{"subject":"快速反应","value":86},{"subject":"传球出球","value":74},{"subject":"射门力量","value":88}],
       "stats": {"进球":"2球","助攻":"1次","射门":"6次","射正":"5次","对抗胜率":"70%","跑动距离":"10.1km","评分":"9.2分"}},
      {"pos": "ST2", "name": "卡西奥", "name_zh": "卡西奥", "name_en": "Cássio", "number": 18, "rating": 6.3, "min": 90, "is_mvp": False,
       "radar": [{"subject":"技术突破","value":72},{"subject":"禁区射门","value":74},{"subject":"无球跑位","value":76},{"subject":"高速冲击","value":78},{"subject":"边路下底","value":70},{"subject":"传球出球","value":68}],
       "stats": {"进球":"0球","射门":"1次","射正":"0次","过人成功":"1次","跑动距离":"7.5km","评分":"6.3分"}}
    ],
    "war_report": "七球大战！门将姆莱奇科虽然失了3球，但5次关键扑救防住了更多威胁。多恩科尔右翼两次送出致命传中，伊安诺尼头球功不可没。卡克佩尔9.4分全场最高，助攻加进球双料贡献；索拉迪奥双响、9.2分，本赛季已轰入9球！七轮保持不败，奥波莱是本赛季波甲头号冲超热门！"
  }
]

# Load existing matches
with open(os.path.join(DATA, "all_matches.json"), encoding="utf-8") as f:
    existing = json.load(f)

# Remove any existing R4-R7 entries if re-running
existing = [m for m in existing if m.get("id") not in [1004,1005,1006,1007]]
existing = NEW_MATCHES + existing  # newest first

with open(os.path.join(DATA, "all_matches.json"), "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)
print("✅ all_matches.json updated with R4-R7")


# ============================================================
# 2. 更新 standings_multi.json：波甲积分榜更新到第7轮
# ============================================================

# After 7 rounds, based on:
# R1: Cracovia 1-1 Odra (D)
# R2: Odra 3-2 GKS Katowice (W)
# R3: Wieczysta 2-3 Odra (W)
# R4: Odra 4-1 Czestochowa (W)
# R5: Odra 4-0 Widzew (W)
# R6: Slask 0-1 Odra (W)
# R7: Odra 4-3 Zaglebie (W)
# Odra: 6W 1D 0L GF=19 GA=10 GD=+9 Pts=19

NEW_TABLE = [
    {"position": 1, "team_name": "奥波莱奥德拉", "played": 7, "won": 6, "drawn": 1, "lost": 0, "gf": 19, "ga": 10, "gd": 9, "points": 19, "note": "直接升级区 · 关注主队 🇨🇳"},
    {"position": 2, "team_name": "华沙莱吉亚", "played": 7, "won": 5, "drawn": 1, "lost": 1, "gf": 16, "ga": 7, "gd": 9, "points": 16, "note": "直接升级区"},
    {"position": 3, "team_name": "克拉科维亚", "played": 7, "won": 4, "drawn": 2, "lost": 1, "gf": 13, "ga": 8, "gd": 5, "points": 14, "note": "升级附加赛"},
    {"position": 4, "team_name": "乔治罗尼亚比亚韦斯托克", "played": 7, "won": 4, "drawn": 2, "lost": 1, "gf": 11, "ga": 7, "gd": 4, "points": 14, "note": "升级附加赛"},
    {"position": 5, "team_name": "拉多米亚克", "played": 7, "won": 4, "drawn": 1, "lost": 2, "gf": 14, "ga": 11, "gd": 3, "points": 13, "note": "升级附加赛"},
    {"position": 6, "team_name": "KGHM卢宾扎格列比", "played": 7, "won": 3, "drawn": 2, "lost": 2, "gf": 12, "ga": 10, "gd": 2, "points": 11},
    {"position": 7, "team_name": "维斯拉克拉科", "played": 7, "won": 3, "drawn": 2, "lost": 2, "gf": 10, "ga": 9, "gd": 1, "points": 11},
    {"position": 8, "team_name": "莫托路宾", "played": 7, "won": 3, "drawn": 1, "lost": 3, "gf": 11, "ga": 11, "gd": 0, "points": 10},
    {"position": 9, "team_name": "扎布热戈尔尼克", "played": 7, "won": 3, "drawn": 0, "lost": 4, "gf": 15, "ga": 16, "gd": -1, "points": 9},
    {"position": 10, "team_name": "弗罗茨瓦夫西里西亚", "played": 7, "won": 2, "drawn": 2, "lost": 3, "gf": 9, "ga": 10, "gd": -1, "points": 8},
    {"position": 11, "team_name": "琴斯托霍瓦", "played": 7, "won": 2, "drawn": 1, "lost": 4, "gf": 11, "ga": 15, "gd": -4, "points": 7},
    {"position": 12, "team_name": "罗兹维泽夫", "played": 7, "won": 2, "drawn": 0, "lost": 5, "gf": 9, "ga": 15, "gd": -6, "points": 6},
    {"position": 13, "team_name": "GKS卡托维兹", "played": 7, "won": 1, "drawn": 2, "lost": 4, "gf": 12, "ga": 15, "gd": -3, "points": 5},
    {"position": 14, "team_name": "华沙普洛克", "played": 7, "won": 1, "drawn": 2, "lost": 4, "gf": 8, "ga": 13, "gd": -5, "points": 5},
    {"position": 15, "team_name": "维彻兹塔克拉库瓦", "played": 7, "won": 1, "drawn": 1, "lost": 5, "gf": 8, "ga": 14, "gd": -6, "points": 4},
    {"position": 16, "team_name": "什切青波贡", "played": 7, "won": 1, "drawn": 0, "lost": 6, "gf": 7, "ga": 14, "gd": -7, "points": 3},
]

NEW_SCORERS = [
    {"rank": 1, "name": "乔丹·索拉迪奥", "club": "奥波莱奥德拉", "goals": 9, "assists": 2, "flag": "circle-flags:br", "note": "关注球队"},
    {"rank": 2, "name": "卡克佩尔·普日比乌科", "club": "奥波莱奥德拉", "goals": 6, "assists": 4, "flag": "circle-flags:pl", "note": "关注球队"},
    {"rank": 3, "name": "托卡", "club": "华沙莱吉亚", "goals": 6, "assists": 1, "flag": "circle-flags:pl"},
    {"rank": 4, "name": "莱万多夫斯基", "club": "克拉科维亚", "goals": 5, "assists": 3, "flag": "circle-flags:pl"},
    {"rank": 5, "name": "巴巴卡尔·迪奥内", "club": "奥波莱奥德拉", "goals": 3, "assists": 1, "flag": "circle-flags:sn", "note": "关注球队"},
    {"rank": 6, "name": "托马斯·加伊达", "club": "奥波莱奥德拉", "goals": 2, "assists": 2, "flag": "circle-flags:pl", "note": "关注球队"},
    {"rank": 7, "name": "科维亚茨基", "club": "KGHM卢宾扎格列比", "goals": 5, "assists": 0, "flag": "circle-flags:pl"},
    {"rank": 8, "name": "斯坦科维奇", "club": "扎布热戈尔尼克", "goals": 5, "assists": 2, "flag": "circle-flags:rs"},
    {"rank": 9, "name": "帕特里克·希什", "club": "奥波莱奥德拉", "goals": 1, "assists": 5, "flag": "circle-flags:pl", "note": "关注球队"},
    {"rank": 10, "name": "卡斯特尔·帕拉茨", "club": "奥波莱奥德拉", "goals": 0, "assists": 5, "flag": "circle-flags:pl", "note": "关注球队"},
]

with open(os.path.join(DATA, "standings_multi.json"), encoding="utf-8") as f:
    sdata = json.load(f)

for league in sdata.get("leagues", []):
    if league.get("key") == "pol_d1":
        league["round_info"] = "第 7 轮 战罢 · 奥波莱奥德拉 6胜1平0负领跑波甲"
        league["table"] = NEW_TABLE
        if "scorers" in league:
            league["scorers"] = NEW_SCORERS
        break

with open(os.path.join(DATA, "standings_multi.json"), "w", encoding="utf-8") as f:
    json.dump(sdata, f, ensure_ascii=False, indent=2)
print("✅ standings_multi.json pol_d1 updated to Round 7")


# ============================================================
# 3. 更新 followed_clubs.json：奥德拉卡片
# ============================================================

with open(os.path.join(DATA, "followed_clubs.json"), encoding="utf-8") as f:
    clubs = json.load(f)

for club in clubs:
    if club.get("id") == "odra":
        club["rank"] = 1
        club["rank_desc"] = "第 1 名 (直接升级区 · 领跑)"
        club["standing_summary"] = "6胜 1平 0负 · 积19分 · 进19球失10球 · 净胜+9"
        club["market_value"] = "€520万"
        club["form"] = ["W", "W", "W", "W", "W"]  # last 5: R3,R4,R5,R6,R7 all wins
        club["stats"] = {
            "played": 7, "won": 6, "drawn": 1, "lost": 0,
            "gf": 19, "ga": 10, "points": 19
        }
        # Prepend new dynamics
        new_dynamics = [
            {
                "id": "dyn_odra_7",
                "type": "news",
                "tag": "联赛战报",
                "title": "七球大战！奥波莱4-3逆转扎布热，索拉迪奥双响七连不败领跑波甲",
                "date": "2026-08-30",
                "summary": "卡克佩尔9.4分传射两项，索拉迪奥双响9.2分，七轮不败稳居波甲榜首！",
                "source": "懂球云 · 特派记者"
            },
            {
                "id": "dyn_odra_6",
                "type": "news",
                "tag": "客场告捷",
                "title": "客场1-0险胜西里西亚！姆莱奇科7扑卡克佩尔世界波，六连不败登顶！",
                "date": "2026-08-23",
                "summary": "高难度客场，姆莱奇科7次扑救零封对手，卡克佩尔61分世界波一球定鼎！",
                "source": "波兰足球杂志《Piłka Nożna》"
            },
            {
                "id": "dyn_odra_5",
                "type": "news",
                "tag": "主场大捷",
                "title": "主场4-0零封罗兹维泽夫！索拉迪奥双响帕拉茨2助，五连不败独跑榜首",
                "date": "2026-08-16",
                "summary": "主场完胜零封，索拉迪奥波甲7球领跑射手榜，5轮不败13球！",
                "source": "懂球云 · 特派记者"
            },
        ]
        old_dynamics = [d for d in club.get("dynamics", []) if d["id"] not in [nd["id"] for nd in new_dynamics]]
        club["dynamics"] = new_dynamics + old_dynamics
        
        # Update completed matches
        new_completed = [
            {"date": "2026-08-30", "opponent": "扎布热戈尔尼克", "home": True, "score": "4-3", "result": "W"},
            {"date": "2026-08-23", "opponent": "弗罗茨瓦夫西里西亚", "home": False, "score": "0-1", "result": "W"},
            {"date": "2026-08-16", "opponent": "罗兹维泽夫", "home": True, "score": "4-0", "result": "W"},
            {"date": "2026-08-09", "opponent": "琴斯托霍瓦", "home": True, "score": "4-1", "result": "W"},
        ]
        if "matches" in club and "completed" in club["matches"]:
            existing_completed = [m for m in club["matches"]["completed"]
                                   if m["date"] not in [nc["date"] for nc in new_completed]]
            club["matches"]["completed"] = new_completed + existing_completed
        break

with open(os.path.join(DATA, "followed_clubs.json"), "w", encoding="utf-8") as f:
    json.dump(clubs, f, ensure_ascii=False, indent=2)
print("✅ followed_clubs.json Odra card updated to Round 7")


# ============================================================
# 4. 更新 news.json：增加新闻
# ============================================================

with open(os.path.join(DATA, "news.json"), encoding="utf-8") as f:
    news = json.load(f)

NEW_NEWS = [
    {
        "id": "news_r7_1",
        "type": "match_report",
        "tag": "联赛战报",
        "title": "七球大战！奥波莱4-3逆转扎布热，索拉迪奥双响七连不败领跑波甲",
        "summary": "7进4-3战胜扎布热，索拉迪奥双响，七连不败依然领跑！本赛季最具观赏性的一役！",
        "date": "2026-08-30",
        "source": "懂球云波兰特派",
        "is_featured": True,
        "club_id": "odra"
    },
    {
        "id": "news_r6_1",
        "type": "match_report",
        "tag": "客场告捷",
        "title": "客场1-0险胜西里西亚！姆莱奇科7扑卡克佩尔世界波，六连不败登顶波甲",
        "summary": "高难度客场，姆莱奇科7次扑救零封对手，卡克佩尔61分世界波一球定鼎！",
        "date": "2026-08-23",
        "source": "懂球云波兰特派",
        "is_featured": False,
        "club_id": "odra"
    },
    {
        "id": "news_r5_1",
        "type": "match_report",
        "tag": "主场大捷",
        "title": "主场4-0大捷！奥波莱零封罗兹维泽夫，索拉迪奥再次双响五连不败领跑波甲",
        "summary": "主场完胜！零封对手，索拉迪奥双响，五轮13球仅失5球，奥波莱领跑波甲！",
        "date": "2026-08-16",
        "source": "懂球云波兰特派",
        "is_featured": False,
        "club_id": "odra"
    },
    {
        "id": "news_r4_1",
        "type": "match_report",
        "tag": "主场大捷",
        "title": "主场轰4-1！奥波莱大胜琴斯托霍瓦，索拉迪奥双响称霸波甲射手榜",
        "summary": "索拉迪奥全场最高9.0分双响，主场4-1大胜，奥波莱四轮不败稳居升级区！",
        "date": "2026-08-09",
        "source": "懂球云波兰特派",
        "is_featured": False,
        "club_id": "odra"
    },
]

existing_ids = {n.get("id") for n in news}
for n in NEW_NEWS:
    if n["id"] not in existing_ids:
        news.insert(0, n)

with open(os.path.join(DATA, "news.json"), "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)
print("✅ news.json updated with R4-R7 news")


# ============================================================
# 5. 更新 community.json：增加新帖子
# ============================================================

with open(os.path.join(DATA, "community.json"), encoding="utf-8") as f:
    community = json.load(f)

NEW_POSTS = [
    {
        "id": "post_r7_1",
        "type": "hot_post",
        "category": "battle_report",
        "title": "【战报】4-3七球大战！奥波莱不败神话延续，索拉迪奥本赛季已9球！",
        "date": "2026-08-30",
        "author": "西里西亚铁血军",
        "author_tag": "主场铁杆",
        "likes": 1247,
        "comments": 342,
        "content": "刚从球场回来！4-3七球大战！全程肾上腺素飙升！索拉迪奥双响、卡克佩尔助攻+进球，这赛季的奥波莱真的太强了！七轮不败、领跑波甲！",
        "club_id": "odra"
    },
    {
        "id": "post_r6_1",
        "type": "analysis",
        "category": "tactics",
        "title": "【战术分析】客场铁桶阵成功复盘：徐指导如何在弗罗茨瓦夫1-0完美防反",
        "date": "2026-08-24",
        "author": "战术观察站",
        "author_tag": "FM战术师",
        "likes": 876,
        "comments": 198,
        "content": "昨天1-0客场告捷堪称防反战术教科书。高位压迫→收缩防线→姆莱奇科7次扑救→卡克佩尔世界波一击制胜。详细拆解徐指导的战术调整...",
        "club_id": "odra"
    },
    {
        "id": "post_r5_2",
        "type": "hot_post",
        "category": "player_focus",
        "title": "【数据贴】索拉迪奥7轮9球！他是本赛季波甲最强外援，没有之一",
        "date": "2026-08-17",
        "author": "奥波莱分析师",
        "author_tag": "数据控",
        "likes": 1089,
        "comments": 267,
        "content": "整理了索拉迪奥全部9球数据：4次主场单刀、2次头球、2次补射、1次世界波。转化率62%，单场最高9.2分。这个外援是徐指导手里的王牌！",
        "club_id": "odra"
    },
]

posts_list = community if isinstance(community, list) else community.get("posts", [])
existing_ids = {p.get("id") for p in posts_list}
for p in NEW_POSTS:
    if p["id"] not in existing_ids:
        posts_list.insert(0, p)

if isinstance(community, list):
    community = posts_list
else:
    community["posts"] = posts_list

with open(os.path.join(DATA, "community.json"), "w", encoding="utf-8") as f:
    json.dump(community, f, ensure_ascii=False, indent=2)
print("✅ community.json updated with R4-R7 posts")

print("\n🎉 全部数据文件更新完成！")
