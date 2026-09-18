from pathlib import Path
p=Path("our14-v28/index.html")
s=p.read_text(encoding="utf-8")
old='''function completeDayForEvent(ev){
  if(ev.isConsequence)return;
  state.daySerial=(state.daySerial||0)+1;
  chargeDailyBasicExpense();'''
new='''function completeDayForEvent(ev){
  if(ev.isConsequence)return;
  state.daySerial=(state.daySerial||0)+1;
  const isOpeningSeatEvent=(ev.week===1 && ev.label==="第1週・事件1｜新的座位");
  if(!isOpeningSeatEvent)chargeDailyBasicExpense();'''
if old not in s:
    raise SystemExit("completeDayForEvent anchor not found")
s=s.replace(old,new,1)
s=s.replace("v28.5.6 後果CG・第二批掛載版","v28.5.7 開場金錢修正版",1)
p.write_text(s,encoding="utf-8")
