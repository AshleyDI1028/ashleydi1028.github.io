from pathlib import Path
import re

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')
patterns=[r'isAftermath\s*:\s*true',r'isConsequence\s*:\s*true',r'isConsequence',r'AFTERMATH',r'後果',r'延遲']
positions=[]
for pat in patterns:
    for m in re.finditer(pat,s,re.I):
        positions.append((m.start(),pat))
positions=sorted(positions)
kept=[]
for pos,pat in positions:
    if not kept or pos-kept[-1][0]>1600:
        kept.append((pos,pat))
out=[]
for i,(pos,pat) in enumerate(kept,1):
    a=max(0,pos-2200); b=min(len(s),pos+4200)
    out.append(f'\n===== #{i} {pat} @ {pos} =====\n{s[a:b]}')
Path('.github/aftermath_dump.txt').write_text('\n'.join(out),encoding='utf-8')
print(f'found={len(positions)} grouped={len(kept)}')
