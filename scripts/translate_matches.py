import json
import os

PLAYER_ZH = {
    "Célestin De Schrevel": "塞莱斯丁·德·施瑞沃",
    "Adama Diop": "亚当穆斯·迪奥普",
    "Allan Tchaptchet": "阿兰·特查普切特",
    "Teddy Mezague": "泰迪·梅扎古",
    "Yassine Ben Hamed": "亚塞尼·本·哈米德",
    "Antoine Valério": "安托万·瓦莱里亚",
    "Aliou Dembélé": "阿卢·登贝莱",
    "Tyrone Tormin": "泰伦·托明",
    "Luca Maiorano": "卢卡·迈奥拉诺",
    "Marks Inchaud": "马克斯·因查德",
    "Paul Wade": "保罗·韦德",
    "Steeven Assengue": "斯蒂文·阿森盖",
    "Abdelsamad Hachem": "阿卜杜勒萨马迪·哈切姆"
}

matches_file = r"I:\fm26-virton-hub\web\src\data\matches.json"
with open(matches_file, "r", encoding="utf-8") as f:
    matches = json.load(f)

for m in matches:
    # 翻译进球者与助攻者
    for sc in m.get("scorers", []):
        raw_p = sc["player"]
        sc["player_zh"] = PLAYER_ZH.get(raw_p, raw_p)
        if "assist" in sc and sc["assist"]:
            sc["assist_zh"] = PLAYER_ZH.get(sc["assist"], sc["assist"])

    # 翻译阵容球员名
    for p in m.get("lineup", []):
        raw_name = p["name"]
        clean_name = raw_name.replace(" (C)", "")
        p["name_en"] = raw_name
        zh_name = PLAYER_ZH.get(clean_name, clean_name)
        if " (C)" in raw_name:
            zh_name += " (队长)"
        p["name_zh"] = zh_name

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

print("[✓] matches.json 球员中文译名注入完成！")
