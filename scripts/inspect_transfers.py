import fmsave, glob, os, json

p = sorted(glob.glob(r"C:\Users\Administrator\Documents\Sports Interactive\Football Manager 2024\games\*.fm"), key=lambda x: -os.path.getmtime(x))[0]

with fmsave.open(p) as s:
    print("Classes in s related to transfers/players:", [a for a in dir(s) if 'transfer' in a or 'stat' in a or 'contract' in a])
