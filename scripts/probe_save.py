"""
探针脚本：读取 FM26 存档，验证 fmsave 能提取哪些关键表。
目标：fixtures（赛程赛果）、league-tables（积分榜）、players（球员）、managed_clubs（执教球队）
"""
import sys
import os

# 存档路径（文件名中"失"和"业"之间有零宽空格 U+200B）
SAVE_PATH = r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games" + "\\" + "耶稣 徐- 失\u200b业中.fm"

print(f"[1] 存档路径: {SAVE_PATH}")
print(f"[2] 文件是否存在: {os.path.exists(SAVE_PATH)}")
print(f"[3] 文件大小: {os.path.getsize(SAVE_PATH) / 1024 / 1024:.1f} MB")
print("=" * 60)

import fmsave

try:
    with fmsave.open(SAVE_PATH) as save:
        # --- 执教球队 ---
        print("\n[4] ===== 执教球队 (managed_clubs) =====")
        try:
            managed = save.managed_clubs()
            for club in managed:
                print(f"  俱乐部: {club.name} | UID: {club.club_uid}")
        except Exception as e:
            print(f"  managed_clubs() 失败: {e}")

        # --- 列出所有可用表 ---
        print("\n[5] ===== 可用表列表 =====")
        try:
            tables = save.tables()
            for t in tables:
                print(f"  - {t}")
        except Exception as e:
            print(f"  tables() 失败: {e}")
            # 尝试其他方式探索
            print("  尝试 dir(save) 探索...")
            for attr in sorted(dir(save)):
                if not attr.startswith('_'):
                    print(f"    {attr}")

        # --- 赛程赛果 ---
        print("\n[6] ===== 赛程赛果 (fixtures) 前 10 条 =====")
        try:
            fixtures = save.fixtures()
            print(f"  类型: {type(fixtures)}")
            if hasattr(fixtures, '__len__'):
                print(f"  总数: {len(fixtures)}")
            # 尝试转 DataFrame
            try:
                df = fixtures.to_dataframe()
                print(f"  DataFrame 列: {list(df.columns)}")
                print(f"  前 5 行:")
                print(df.head().to_string())
            except:
                # 直接迭代
                for i, f in enumerate(fixtures):
                    if i >= 5: break
                    print(f"  {f}")
        except Exception as e:
            print(f"  fixtures() 失败: {e}")

        # --- 积分榜 ---
        print("\n[7] ===== 积分榜 (league_tables) =====")
        try:
            tables_data = save.league_tables()
            print(f"  类型: {type(tables_data)}")
            try:
                df = tables_data.to_dataframe()
                print(f"  DataFrame 列: {list(df.columns)}")
                print(df.head(10).to_string())
            except:
                for i, row in enumerate(tables_data):
                    if i >= 10: break
                    print(f"  {row}")
        except Exception as e:
            print(f"  league_tables() 失败: {e}")

        # --- 球员 ---
        print("\n[8] ===== 球员 (players) 前 5 条 =====")
        try:
            players = save.players()
            print(f"  类型: {type(players)}")
            try:
                df = players.to_dataframe()
                print(f"  DataFrame 列: {list(df.columns)}")
                print(f"  总人数: {len(df)}")
                print(df.head().to_string())
            except:
                for i, p in enumerate(players):
                    if i >= 5: break
                    print(f"  {p}")
        except Exception as e:
            print(f"  players() 失败: {e}")

        # --- 球员比赛统计 ---
        print("\n[9] ===== 球员比赛数据 (player_match_stats) =====")
        try:
            pms = save.player_match_stats()
            print(f"  类型: {type(pms)}")
            try:
                df = pms.to_dataframe()
                print(f"  DataFrame 列: {list(df.columns)}")
                print(df.head().to_string())
            except:
                for i, s in enumerate(pms):
                    if i >= 3: break
                    print(f"  {s}")
        except Exception as e:
            print(f"  player_match_stats() 失败: {e}")

except Exception as e:
    print(f"\n[ERROR] fmsave.open() 失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("探针完成。")
