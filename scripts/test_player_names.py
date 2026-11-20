import fmsave

SAVE_PATH = (
    r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games"
    + "\\"
    + "耶稣 徐- 失\u200b业中.fm"
)

with fmsave.open(SAVE_PATH) as save:
    summary_list = list(save.info.summary_strings)
    print("=== save.info.summary_strings 中包含的球员中文名 ===")
    chinese_names = [s for s in summary_list if any('\u4e00' <= char <= '\u9fff' for char in s)]
    for name in chinese_names:
        print(f"  {name}")

