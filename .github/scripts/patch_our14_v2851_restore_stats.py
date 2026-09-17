from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

old='''  setEventSceneMode("play");
  renderEventDataBar();
  if(activeEvent.cinematic){
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
  }
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
new='''  setEventSceneMode("play");
  renderEventDataBar();
  document.querySelector("#game .topbar")?.classList.remove("cinematicHidden");
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
if old in s:
    s=s.replace(old,new,1)

old_exam='''    setVisual(activeEvent);
    setEventSceneMode("play");
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
    document.getElementById('speaker').textContent="旁白";'''
new_exam='''    setVisual(activeEvent);
    setEventSceneMode("play");
    renderEventDataBar();
    document.querySelector("#game .topbar")?.classList.remove("cinematicHidden");
    document.getElementById('speaker').textContent="旁白";'''
if old_exam in s:
    s=s.replace(old_exam,new_exam,1)

# Remove any remaining logic that hides the top ability/status bar in cinematic mode.
s=s.replace('document.querySelector("#game .topbar")?.classList.add("cinematicHidden");',
            'document.querySelector("#game .topbar")?.classList.remove("cinematicHidden");')

# Safety net: if a stale class remains from an older saved UI state, keep the bar visible.
style='''\n<style id="v2851-stat-fix">\n#game .topbar.cinematicHidden{opacity:1!important;visibility:visible!important;transform:none!important;pointer-events:auto!important;}\n</style>\n'''
if 'id="v2851-stat-fix"' not in s:
    s=s.replace('</head>',style+'</head>',1)

if 'v28.5.1 劇情分歧・能力面板修正版' not in s:
    s=s.replace('v28.5 劇情分歧・章節CG版','v28.5.1 劇情分歧・能力面板修正版',1)

p.write_text(s,encoding='utf-8')
