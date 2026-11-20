import fmsave

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)

with fmsave.open(SAVE_PATH) as save:
    print("=== nations 表 ===")
    first_n = None
    for n in save.nations():
        first_n = n
        break
    print(f"dir(n): {[a for a in dir(first_n) if not a.startswith('_')]}")
    print(f"repr: {repr(first_n)[:300]}")

    nations_map = {}
    for n in save.nations():
        nname = getattr(n, 'name', '') or ''
        nid = getattr(n, 'nation_id', None) or getattr(n, 'id', None) or getattr(n, 'uid', None)
        if nid is not None and nname:
            nations_map[nid] = nname
            if any(kw in nname for kw in ['英格', '西班', '意大', '德', '法', '比利时']):
                print(f"  nid={nid}: {nname}")

