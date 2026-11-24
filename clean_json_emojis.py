import json
from pathlib import Path
import re

DATA_DIR = Path(r"I:\fm26-virton-hub\web\src\data")

emoji_regex = re.compile(r'[\U00010000-\U0010ffff\u2600-\u27bf\ufe0f\u200d]+')

def strip_emojis(obj):
    if isinstance(obj, str):
        # Strip emoji
        cleaned = emoji_regex.sub('', obj).strip()
        # Clean double spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned
    elif isinstance(obj, list):
        return [strip_emojis(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: strip_emojis(v) for k, v in obj.items()}
    return obj

# 1. ticker_matches.json
with open(DATA_DIR / "ticker_matches.json", "r", encoding="utf-8") as f:
    ticker = json.load(f)

for item in ticker:
    item["home_logo"] = ""
    item["away_logo"] = ""
    item["highlights"] = strip_emojis(item["highlights"])
    if item["id"] == "ticker_odra_01":
        item["home_code"] = "ODR"
        item["away_code"] = "WIS"
        item["home_color"] = "#dc2626"
        item["away_color"] = "#2563eb"
        item["league_flag"] = "circle-flags:pl"
    elif item["id"] == "ticker_ucl_02":
        item["home_code"] = "RMA"
        item["away_code"] = "MCI"
        item["home_color"] = "#eab308"
        item["away_color"] = "#0ea5e9"
        item["league_flag"] = "circle-flags:eu"
    elif item["id"] == "ticker_epl_03":
        item["home_code"] = "ARS"
        item["away_code"] = "EVE"
        item["home_color"] = "#ef4444"
        item["away_color"] = "#1d4ed8"
        item["league_flag"] = "circle-flags:gb-eng"
    elif item["id"] == "ticker_jpl_04":
        item["home_code"] = "CLU"
        item["away_code"] = "AND"
        item["home_color"] = "#0284c7"
        item["away_color"] = "#7c3aed"
        item["league_flag"] = "circle-flags:be"

with open(DATA_DIR / "ticker_matches.json", "w", encoding="utf-8") as f:
    json.dump(ticker, f, ensure_ascii=False, indent=2)

# 2. news_articles.json
with open(DATA_DIR / "news_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

articles = strip_emojis(articles)
with open(DATA_DIR / "news_articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

# 3. all_matches.json
with open(DATA_DIR / "all_matches.json", "r", encoding="utf-8") as f:
    matches = json.load(f)

flag_map = {
    "pol_d1": "circle-flags:pl",
    "bel_d1": "circle-flags:be",
    "bel_d2": "circle-flags:be",
    "pl": "circle-flags:gb-eng",
    "ucl": "circle-flags:eu"
}

matches = strip_emojis(matches)
for m in matches:
    m["league_flag"] = flag_map.get(m.get("league_key", ""), "circle-flags:eu")
    m["home_logo"] = ""
    m["away_logo"] = ""
    # create 3-letter codes for clean badges
    m["home_code"] = m["home_team"][:3]
    m["away_code"] = m["away_team"][:3]

with open(DATA_DIR / "all_matches.json", "w", encoding="utf-8") as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

# 4. community_posts.json
with open(DATA_DIR / "community_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

posts = strip_emojis(posts)
for p in posts:
    p["avatar"] = ""
    for r in p.get("replies", []):
        r["avatar"] = ""

with open(DATA_DIR / "community_posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

# 5. standings_multi.json
with open(DATA_DIR / "standings_multi.json", "r", encoding="utf-8") as f:
    standings = json.load(f)

standings = strip_emojis(standings)
for lg in standings["leagues"]:
    lg["flag_icon"] = flag_map.get(lg.get("key", ""), "circle-flags:eu")
    lg["flag"] = ""

with open(DATA_DIR / "standings_multi.json", "w", encoding="utf-8") as f:
    json.dump(standings, f, ensure_ascii=False, indent=2)

# 6. manager_phone.json
with open(DATA_DIR / "manager_phone.json", "r", encoding="utf-8") as f:
    phone = json.load(f)

phone = strip_emojis(phone)
for msg in phone.get("messages", []):
    msg["avatar"] = ""

with open(DATA_DIR / "manager_phone.json", "w", encoding="utf-8") as f:
    json.dump(phone, f, ensure_ascii=False, indent=2)

print("JSON files cleaned of emojis and enhanced with Iconify keys!")
