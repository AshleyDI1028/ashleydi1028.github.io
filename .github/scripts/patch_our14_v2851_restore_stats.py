from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

# 1) Event intro: keep the numeric ability strip visible.
old_intro='''  if(mode==="intro"){
    layout?.classList.add("eventSceneMode");
    dialogue?.classList.add("cinematicHidden");
    intro?.classList.add("show");
    topbar?.classList.add("cinematicHidden");
  }else if(mode==="play"){'''
new_intro='''  if(mode==="intro"){
    layout?.classList.add("eventSceneMode");
    dialogue?.classList.add("cinematicHidden");
    intro?.classList.add("show");
    data?.classList.add("show");
    topbar?.classList.remove("cinematicHidden");
  }else if(mode==="play"){'''
if old_intro in s:
    s=s.replace(old_intro,new_intro,1)

old_show_intro='''function showEventIntro(){
  setEventSceneMode("intro");
  const kind=document.getElementById("eventIntroKind");'''
new_show_intro='''function showEventIntro(){
  renderEventDataBar();
  setEventSceneMode("intro");
  const kind=document.getElementById("eventIntroKind");'''
if old_show_intro in s:
    s=s.replace(old_show_intro,new_show_intro,1)

# 2) Cinematic events: do not hide the ability strip or the normal top bar.
old_event='''  setEventSceneMode("play");
  renderEventDataBar();
  if(activeEvent.cinematic){
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
  }
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
new_event='''  setEventSceneMode("play");
  renderEventDataBar();
  document.getElementById("eventDataBar")?.classList.add("show");
  document.querySelector("#game .topbar")?.classList.remove("cinematicHidden");
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
if old_event in s:
    s=s.replace(old_event,new_event,1)

# 3) Exam epilogue is also cinematic, but abilities should remain visible.
old_exam='''    setVisual(activeEvent);
    setEventSceneMode("play");
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
    document.getElementById('speaker').textContent="旁白";'''
new_exam='''    setVisual(activeEvent);
    setEventSceneMode("play");
    renderEventDataBar();
    document.getElementById("eventDataBar")?.classList.add("show");
    document.querySelector("#game .topbar")?.classList.remove("cinematicHidden");
    document.getElementById('speaker').textContent="旁白";'''
if old_exam in s:
    s=s.replace(old_exam,new_exam,1)

# Safety CSS: a stale cinematicHidden class must not be able to hide the top bar.
style='''\n<style id="v2851-stat-fix">\n#game .topbar.cinematicHidden{display:flex!important;opacity:1!important;visibility:visible!important;transform:none!important;pointer-events:auto!important;}\n</style>\n'''
if 'id="v2851-stat-fix"' not in s:
    s=s.replace('</head>',style+'</head>',1)

if 'v28.5.1 劇情分歧・能力面板修正版' not in s:
    s=s.replace('v28.5 劇情分歧・章節CG版','v28.5.1 劇情分歧・能力面板修正版',1)

p.write_text(s,encoding='utf-8')
