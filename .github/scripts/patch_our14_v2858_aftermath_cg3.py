from pathlib import Path
p=Path("our14-v28/index.html")
s=p.read_text(encoding="utf-8")

anchor='const AFTERMATH_CG_SPRITE_2="assets/cg_aftermath_batch2_sprite.jpg";'
if anchor not in s:
    raise SystemExit("batch2 sprite anchor not found")
if 'AFTERMATH_CG_SPRITE_3' not in s:
    s=s.replace(anchor,anchor+'\nconst AFTERMATH_CG_SPRITE_3="assets/cg_aftermath_batch3_sprite.jpg";',1)

old='''function setVisual(ev){
  const visual=document.getElementById('visual');
  const cgPanel2=eventCgPanel2(ev);
  const cgPanel=eventCgPanel(ev);
  if(cgPanel2!==null){
    const pos=[[0,0],[50,0],[100,0],[0,100],[50,100],[100,100]][cgPanel2]||[0,0];
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE_2}")`;
    visual.style.backgroundSize="300% 200%";
    visual.style.backgroundPosition=`${pos[0]}% ${pos[1]}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else if(cgPanel!==null){'''

insert='''function eventCgPanel3(ev){
  const id=String(ev?.aftermathId||"");
  const map={
    meme_warn:0,
    loan_direct:0,
    loan_soft:0,
    joke_stop:0,

    meme_silent:1,
    loan_silent:1,
    joke_ignore:1,

    meme_cleanup:2,
    fakeSign_accept:2,
    cheat_admit:2,

    hideScore_admit:3,
    hideScore_plan:3,

    hideScore_argue:4,

    cheat_redo:5,

    fakeSign_deny:6,
    cheat_deny:6,

    fakeSign_explain:7,
    joke_apologize:7
  };
  return Object.prototype.hasOwnProperty.call(map,id)?map[id]:null;
}
function setVisual(ev){
  const visual=document.getElementById('visual');
  const cgPanel3=eventCgPanel3(ev);
  const cgPanel2=eventCgPanel2(ev);
  const cgPanel=eventCgPanel(ev);
  if(cgPanel3!==null){
    const pos=[[0,0],[33.333,0],[66.667,0],[100,0],[0,100],[33.333,100],[66.667,100],[100,100]][cgPanel3]||[0,0];
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE_3}")`;
    visual.style.backgroundSize="400% 200%";
    visual.style.backgroundPosition=`${pos[0]}% ${pos[1]}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else if(cgPanel2!==null){
    const pos=[[0,0],[50,0],[100,0],[0,100],[50,100],[100,100]][cgPanel2]||[0,0];
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE_2}")`;
    visual.style.backgroundSize="300% 200%";
    visual.style.backgroundPosition=`${pos[0]}% ${pos[1]}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else if(cgPanel!==null){'''

if old not in s:
    raise SystemExit("setVisual batch2 block not found")
s=s.replace(old,insert,1)
s=s.replace("v28.5.7 開場金錢修正版","v28.5.8 後果CG補齊版",1)
p.write_text(s,encoding="utf-8")
