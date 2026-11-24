"""
转会费与货币换算统一配置模块 (transfer_config.py)
用于解决：
1. fmsave 原始货币单位到游戏显示货币的汇率换算 (CURRENCY_MULTIPLIER)
2. 严禁拿 transfer_value (市场估值) 冒充实际转会费 (免签标免签、租借标租借、普通转会未确认标估值)
3. 支持 manual_overrides 手动/截图覆写真实转会费，同步脚本永不覆盖
"""

import json
from pathlib import Path

# 1. 货币换算系数配置常量 (CURRENCY_MULTIPLIER)
# 说明：部分 FM 存档内部存储的金额以英镑或底层基准单位结算，如游戏显示欧元可按需调整（如 1.0 或 1.16 等）
CURRENCY_MULTIPLIER = 1.0
CURRENCY_SYMBOL = "€"

TRANSFERS_JSON_PATH = Path(r"I:\fm26-virton-hub\web\src\data\transfers.json")
FOLLOWED_PATH = Path(r"I:\fm26-virton-hub\web\src\data\followed_clubs.json")
STANDINGS_PATH = Path(r"I:\fm26-virton-hub\web\src\data\standings_multi.json")

def convert_currency(raw_amount):
    """根据汇率系数换算原始金额"""
    if raw_amount is None:
        return 0
    return raw_amount * CURRENCY_MULTIPLIER

def format_valuation(raw_amount):
    """
    严禁将估值冒充转会费：格式化为清晰的【估值 €XX万】
    """
    if not raw_amount:
        return "估值待定"
    conv = convert_currency(raw_amount)
    if conv >= 100000000:
        return f"估值 {CURRENCY_SYMBOL}{conv / 100000000:.2f}亿"
    elif conv >= 10000:
        return f"估值 {CURRENCY_SYMBOL}{conv / 10000:.1f}万"
    else:
        return f"估值 {CURRENCY_SYMBOL}{int(conv)}"

def format_market_value(raw_amount):
    """
    球员身价面板数值，格式化为 €XX.X万
    """
    if not raw_amount:
        return f"{CURRENCY_SYMBOL}10.0万"
    conv = convert_currency(raw_amount)
    if conv >= 100000000:
        return f"{CURRENCY_SYMBOL}{conv / 100000000:.2f}亿"
    elif conv >= 10000:
        return f"{CURRENCY_SYMBOL}{conv / 10000:.1f}万"
    else:
        return f"{CURRENCY_SYMBOL}{int(conv)}"

def format_weekly_wage(raw_wage):
    """
    周薪格式化为 €X,XXX/周
    """
    if not raw_wage:
        return f"{CURRENCY_SYMBOL}1,200/周"
    conv = convert_currency(raw_wage)
    return f"{CURRENCY_SYMBOL}{int(conv):,}/周"

def load_overrides():
    """读取 transfers.json 中的 manual_overrides"""
    if not TRANSFERS_JSON_PATH.exists():
        return {}
    try:
        with open(TRANSFERS_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("manual_overrides", {})
    except Exception as e:
        print(f"Warning: failed to load transfers.json: {e}")
        return {}

def resolve_fee(player_name, club_id, direction, raw_tval=None, default_from_team="", default_type=""):
    """
    解析转会费逻辑：
    1. 优先检查 manual_overrides：若存在手动填写的确切金额（如截图识别录入），直接采用，绝不覆盖；
    2. 若标记为免签或来源球队为自由身，返回 '免签'；
    3. 若为租借加盟/租借离队，返回 '租借'；
    4. 若为普通转会且尚无确切成交价，返回 '估值 €XX万'（绝不冒充真实转会费）。
    """
    overrides = load_overrides()
    club_overrides = overrides.get(club_id, {}).get(direction, {})
    
    # 精确匹配或子串匹配球员名字
    player_override = None
    for k, v in club_overrides.items():
        if k in player_name or player_name in k:
            player_override = v
            break

    if player_override:
        # 1. 存在手动/截图覆写的精确金额（非 None 且非空）
        if player_override.get("fee"):
            return player_override["fee"]
        # 2. 存在类型覆写
        fee_type = player_override.get("fee_type")
        if fee_type == "free":
            return "免签"
        if fee_type == "loan":
            return "租借"

    # 3. 默认来源判定
    if "自由身" in default_from_team or "免签" in default_type or "free" in default_type.lower():
        return "免签"
    if "租借" in default_from_team or "租借" in default_type or "loan" in default_type.lower():
        return "租借"

    # 4. 普通转会且无确切转会费：格式化为估值
    if raw_tval:
        return format_valuation(raw_tval)
    return "保密/待补录"
