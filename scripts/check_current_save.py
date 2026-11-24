import sys
from pathlib import Path
sys.path.append(r"I:\fm26-virton-hub\scripts")
import os

save_dir = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games")
save_files = list(save_dir.glob("*.fm"))
for sf in save_files:
    print(f"Save file: {sf.name}, size: {sf.stat().st_size / (1024*1024):.2f} MB, modified: {sf.stat().st_mtime}")

try:
    import fm_skin_parser
except ImportError:
    pass

# Check inspect_all_virton_fixtures.py
print("Looking at inspect_all_virton_fixtures.py...")
