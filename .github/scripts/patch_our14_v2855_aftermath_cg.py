from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

# Tag queued aftermath events with a CG panel. The sprite is 6 stacked 16:9 frames.
old='''  const id=typeof item==="string"?item:item.id;\n  if(!id||!AFTERMATH_EVENTS[id])return resumeFlow();\n  showEvent(AFTERMATH_EVENTS[id]());'''
new='''  const id=typeof item==="string"?item:item.id;\n  if(!id||!AFTERMATH_EVENTS[id])return resumeFlow();\n  const ev=AFTERMATH_EVENTS[id]();\n  ev.aftermathId=id;\n  if(id.startsWith("loan_"))ev.cgPanel=0;\n  else if(id.startsWith("fakeSign_"))ev.cgPanel=1;\n  else if(id.startsWith("hideScore_"))ev.cgPanel=2;\n  showEvent(ev);'''
if old in s:
    s=s.replace(old,new,1)

old_visual='''function setVisual(ev){\n  document.getElementById('visual').style.backgroundImage=`url("${A[ev.bg||'bg_classroom']}")`;\n  const tag=document.getElementById('tag');'''
new_visual='''const AFTERMATH_CG_SPRITE="assets/cg_consequence_sprite.jpg";\nfunction eventCgPanel(ev){\n  if(Number.isFinite(ev?.cgPanel))return ev.cgPanel;\n  const label=String(ev?.label||"");\n  if(label.includes("94分"))return 3;\n  if(label.includes("23:48"))return 4;\n  if(label.includes("考完之後")||label.includes("段考結束"))return 5;\n  if(label.includes("48分"))return 2;\n  return null;\n}\nfunction setVisual(ev){\n  const visual=document.getElementById('visual');\n  const cgPanel=eventCgPanel(ev);\n  if(cgPanel!==null){\n    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE}")`;\n    visual.style.backgroundSize="100% 600%";\n    visual.style.backgroundPosition=`center ${cgPanel*20}%`;\n    visual.style.backgroundRepeat="no-repeat";\n  }else{\n    visual.style.backgroundImage=`url("${A[ev.bg||'bg_classroom']}")`;\n    visual.style.backgroundSize="cover";\n    visual.style.backgroundPosition="center";\n    visual.style.backgroundRepeat="no-repeat";\n  }\n  const tag=document.getElementById('tag');'''
if old_visual in s:
    s=s.replace(old_visual,new_visual,1)
else:
    raise SystemExit('setVisual anchor not found')

s=s.replace('v28.5.4 事件閱讀・教室投影大字版','v28.5.5 後果CG・第一批掛載版',1)

p.write_text(s,encoding='utf-8')
