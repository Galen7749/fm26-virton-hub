import json

# 1. Update news.json
news_path = "I:/fm26-virton-hub/web/src/data/news.json"
with open(news_path, "r", encoding="utf-8") as f:
    news_list = json.load(f)

for item in news_list:
    if item.get("round") == 32:
        article = item.get("dongqiudi_article", {})
        article["title"] = "【史诗级神迹！总比分4-3惊天大逆转绝杀！】因查德戴帽封神，阿森盖84分钟替补起球，因查德90+2'头槌绝杀！维尔通主场4-1逆转利尔斯冲甲成功！！！"
        article["summary"] = "首回合0-2落后！次回合狂轰4-1！马克斯·因查德天神下凡狂轰帽子戏法（9.8分封神），哈切姆破门，第84分钟替补奇兵阿森盖补时右路起球助攻因查德头槌绝杀！维尔通精英总比分4-3绝杀淘汰皇家利尔斯，夺得冲甲附加赛总冠军，历史性升入比利时甲级联赛！"
        
        # update body
        body = article.get("body", "")
        old_frag = "阿森盖右路生吃对手边后卫，下底送出撕裂防线的贴地倒三角！门前包抄的因查德凌空扫射破门——帽子戏法！！！4-1！总比分4-3大逆转！！！"
        new_frag = "伤停补时第90+2分钟，阿森盖右路强行生吃对手边后卫下底送出精准高弧度传中！门前因查德天神下凡力压两名中卫高高跃起，一记势大力沉的泰山压顶头球轰入死角——帽子戏法！！！90+2'读秒头球绝杀！！！4-1！总比分4-3惊天大逆转冲甲！！！"
        if old_frag in body:
            article["body"] = body.replace(old_frag, new_frag)
        elif "门前包抄的因查德" in body:
            # replace section
            article["body"] = body.replace("门前包抄的因查德凌空扫射破门", "门前因查德高高跃起泰山压顶头球轰入死角")
        
        if "头球绝杀" not in article.get("tags", []):
            article.setdefault("tags", []).insert(3, "头球绝杀")

        # hupu comments
        hupu = item.get("hupu_thread", {})
        if "comments" in hupu and len(hupu["comments"]) > 0:
            hupu["comments"][0]["content"] = "10分！满分已经不够打了！首回合0-2，次回合狂轰4-1，总比分4-3绝杀！因查德戴帽！第84分钟神换人阿森盖绝命传中，90+2补时头球破门绝杀那一刻整个看台几千人直接原地发疯！徐指导这辈子值了！载入世界足坛史册的逆转神迹！"
            hupu["comments"][1]["content"] = "因查德单场3球9.8分封神！最后补时那一记泰山压顶头槌简直是C罗附体，整个人几乎平视横梁！绝境时刻站出来的真男人！下赛季比甲看你怎么暴打五大联赛豪门！"

with open(news_path, "w", encoding="utf-8") as f:
    json.dump(news_list, f, ensure_ascii=False, indent=2)
print("Updated news.json successfully!")

# 2. Update community.json
comm_path = "I:/fm26-virton-hub/web/src/data/community.json"
with open(comm_path, "r", encoding="utf-8") as f:
    comm_data = json.load(f)

for t in comm_data.get("threads", []):
    if t.get("id") == 101:
        t["content"] = "兄弟们！我就在伊万·乔治球场现场！当主裁判吹响终场哨的那一刻，上千名球迷直接冲进了球场！把徐指导和因查德高高抛向空中！首回合客场0-2几乎把我们逼入死地，但今晚徐指导排出4-1-1-4双前锋狂攻体系，因查德单场狂轰3球帽子戏法，哈切姆打入关键一球！尤其是第84分钟替补登场的阿森盖在第90+2分钟送出绝命传中，因查德门前泰山压顶头槌绝杀！总比分4-3压哨绝杀！这就是足球！这就是奇迹！下赛季我们就是比甲球队了！！！"
        t["top_replies"] = [
            {
                "user": "现场看台第一排",
                "content": "我就在球门后面！阿森盖传中那一瞬间因查德高高跃起泰山压顶，那个头球砸进网窝的声音太震撼了！全场泪目！",
                "likes": 2100
            },
            {
                "user": "十年徐帅老死忠",
                "content": "满分！10分！中国教练带欧洲球队升入顶级联赛，绝杀还是补时头球破门，载入中国足球与比利时足球史册的神迹！",
                "likes": 1820
            },
            {
                "user": "坎特私人理财师",
                "content": "坎特在看台上直接抱着徐指导热泪盈眶！不仅当场宣布发放全队百万巨额奖金，还承诺下赛季比甲全面注资引援！",
                "likes": 1560
            }
        ]

with open(comm_path, "w", encoding="utf-8") as f:
    json.dump(comm_data, f, ensure_ascii=False, indent=2)
print("Updated community.json successfully!")
