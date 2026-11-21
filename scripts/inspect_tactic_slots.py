from pathlib import Path
import fmsave

save_path = Path(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\耶稣 徐- 失​业中.fm")
with fmsave.open(str(save_path)) as save:
    for i, t in enumerate(save.tactics()):
        print(f"\n================ TACTIC {i}: {t.name} ================")
        print("Mentality:", t.mentality)
        print("Style name:", getattr(t, 'style_name', ''))
        slots = getattr(t, 'slots', [])
        print(f"Slots count: {len(slots)}")
        for idx, s in enumerate(slots):
            attrs = [a for a in dir(s) if not a.startswith('_')]
            info = {k: getattr(s, k) for k in attrs if hasattr(s, k) and not callable(getattr(s, k))}
            print(f"  Slot {idx:2d}: {info}")
