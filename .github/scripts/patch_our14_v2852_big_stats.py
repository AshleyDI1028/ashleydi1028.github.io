from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

style='''\n<style id="v2852-big-stats">\n/* Classroom/projector readability for the top-left ability strip */\n#game .eventDataBar{\n  left:18px!important; right:18px!important; top:16px!important;\n  gap:9px!important; row-gap:9px!important;\n}\n#game .eventDataGroup{\n  display:flex!important; gap:8px!important; flex-wrap:wrap!important; align-items:center!important;\n}\n#game .eventDataChip{\n  padding:9px 13px!important;\n  border-radius:999px!important;\n  font-size:14px!important;\n  line-height:1.2!important;\n  font-weight:800!important;\n  background:rgba(5,9,18,.90)!important;\n  border:1px solid rgba(255,255,255,.24)!important;\n  box-shadow:0 3px 12px rgba(0,0,0,.28)!important;\n}\n#game .eventDataChip b{\n  font-size:17px!important;\n  font-weight:1000!important;\n  letter-spacing:.01em!important;\n}\n#game .eventDataChip.relation b{font-size:16px!important;}\n@media (max-width:900px){\n  #game .eventDataChip{font-size:12.5px!important;padding:8px 10px!important;}\n  #game .eventDataChip b{font-size:15px!important;}\n}\n</style>\n'''
if 'id="v2852-big-stats"' not in s:
    s=s.replace('</head>',style+'</head>',1)

if 'v28.5.2 劇情分歧・大字能力面板版' not in s:
    s=s.replace('v28.5.1 劇情分歧・能力面板修正版','v28.5.2 劇情分歧・大字能力面板版',1)

p.write_text(s,encoding='utf-8')
