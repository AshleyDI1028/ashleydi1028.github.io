from pathlib import Path

p=Path("our14-v28/index.html")
s=p.read_text(encoding="utf-8")

anchor='const AFTERMATH_CG_SPRITE="assets/cg_consequence_sprite.jpg";'
if anchor not in s:
    raise SystemExit("v28.5.5 CG anchor not found")

if 'AFTERMATH_CG_SPRITE_2' not in s:
    s=s.replace(anchor, anchor+'\nconst AFTERMATH_CG_SPRITE_2="assets/cg_aftermath_batch2_sprite.jpg";', 1)

old='''function eventCgPanel(ev){
  if(Number.isFinite(ev?.cgPanel))return ev.cgPanel;
  const label=String(ev?.label||"");
  if(label.includes("94分"))return 3;
  if(label.includes("23:48"))return 4;
  if(label.includes("考完之後")||label.includes("段考結束"))return 5;
  if(label.includes("48分"))return 2;
  return null;
}
function setVisual(ev){
  const visual=document.getElementById('visual');
  const cgPanel=eventCgPanel(ev);
  if(cgPanel!==null){
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE}")`;
    visual.style.backgroundSize="100% 600%";
    visual.style.backgroundPosition=`center ${cgPanel*20}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else{
    visual.style.backgroundImage=`url("${A[ev.bg||'bg_classroom']}")`;
    visual.style.backgroundSize="cover";
    visual.style.backgroundPosition="center";
    visual.style.backgroundRepeat="no-repeat";
  }
  const tag=document.getElementById('tag');'''

new='''function eventCgPanel(ev){
  if(Number.isFinite(ev?.cgPanel))return ev.cgPanel;
  const label=String(ev?.label||"");
  if(label.includes("94分"))return 3;
  if(label.includes("23:48"))return 4;
  if(label.includes("考完之後")||label.includes("段考結束"))return 5;
  if(label.includes("48分"))return 2;
  return null;
}
function eventCgPanel2(ev){
  if(Number.isFinite(ev?.cgPanel2))return ev.cgPanel2;
  const id=String(ev?.aftermathId||"");
  const label=String(ev?.label||"");

  // 0 群組壓力
  if(id==="meme_silent"||id==="meme_cleanup"||label.includes("群組梗圖傳到老師"))return 0;
  // 1 生活指導／作弊後果
  if(id.startsWith("cheat_")||label.includes("答案怎麼這麼像"))return 1;
  // 2 道歉／修復
  if(id==="joke_apologize"||label.includes("道歉")||label.includes("抱歉"))return 2;
  // 3 人際尷尬／孤立感
  if(id==="meme_warn"||id==="joke_ignore"||id==="joke_stop"||label.includes("綽號")||label.includes("尷尬"))return 3;
  // 4 熬夜／疲憊
  if(label.includes("只剩三天")||label.includes("熬夜")||label.includes("疲憊"))return 4;
  // 5 朋友也撐不住／無聲陪伴
  if(label.includes("今天怎麼這麼安靜")||label.includes("真的讀不下去")||label.includes("撐不住"))return 5;
  return null;
}
function setVisual(ev){
  const visual=document.getElementById('visual');
  const cgPanel2=eventCgPanel2(ev);
  const cgPanel=eventCgPanel(ev);
  if(cgPanel2!==null){
    const pos=[[0,0],[50,0],[100,0],[0,100],[50,100],[100,100]][cgPanel2]||[0,0];
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE_2}")`;
    visual.style.backgroundSize="300% 200%";
    visual.style.backgroundPosition=`${pos[0]}% ${pos[1]}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else if(cgPanel!==null){
    visual.style.backgroundImage=`url("${AFTERMATH_CG_SPRITE}")`;
    visual.style.backgroundSize="100% 600%";
    visual.style.backgroundPosition=`center ${cgPanel*20}%`;
    visual.style.backgroundRepeat="no-repeat";
  }else{
    visual.style.backgroundImage=`url("${A[ev.bg||'bg_classroom']}")`;
    visual.style.backgroundSize="cover";
    visual.style.backgroundPosition="center";
    visual.style.backgroundRepeat="no-repeat";
  }
  const tag=document.getElementById('tag');'''

if old not in s:
    raise SystemExit("setVisual v28.5.5 block not found")
s=s.replace(old,new,1)

s=s.replace("v28.5.5 後果CG・第一批掛載版","v28.5.6 後果CG・第二批掛載版",1)

p.write_text(s,encoding="utf-8")
