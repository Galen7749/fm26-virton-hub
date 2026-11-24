import json

with open('scripts/week_fixtures.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=== Polish League (Comp 188) Matches (2026-07-25 ~ 2026-08-01) ===')
for m in data:
    if m['competition_id'] == 188:
        print(f"{m['date']} | {m['home']} {m['home_goals']} - {m['away_goals']} {m['away']} | {m['stadium']}")

print('\n=== Notable European Top Club Fixtures (Friendlies / Summer Tours) ===')
notables = ['皇家马德里', '巴塞罗那', '曼彻斯特城', '阿森纳', '切尔西', '利物浦', '拜仁慕尼黑', '巴黎圣日耳曼', '国际米兰', 'AC米兰', '多特蒙德', '马德里竞技']
for m in data:
    h, a = m['home'], m['away']
    if any(n in h or n in a for n in notables):
        if not any(x in h or x in a for x in ['2队', '3队', '二队', '三队', 'B队', '青年', '朗多尼亚', '巴伊亚', '萨兰迪']):
            print(f"{m['date']} | {m['competition']} | {m['home']} {m['home_goals']} - {m['away_goals']} {m['away']} | {m['stadium']}")

print('\n=== Belgian League & Virton Fixtures ===')
for m in data:
    h, a = m['home'], m['away']
    if '维尔通' in h or '维尔通' in a or '布鲁日' in h or '安德莱赫特' in h or '标准列日' in h:
        if not any(x in h or x in a for x in ['2队', '3队', '二队', '三队', 'B队', '青年']):
            print(f"{m['date']} | {m['competition']} | {m['home']} {m['home_goals']} - {m['away_goals']} {m['away']} | {m['stadium']}")
