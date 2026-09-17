from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

style='''
<style id="v2854-event-projection">
/* Classroom projection typography for story / random / consequence events */
#game .dialogue.eventDialogueMode,
#game .dialogue.riskDialogueMode{
  max-height:min(78vh,620px)!important;
  padding:20px 22px!important;
}
#game .dialogue.eventDialogueMode .speaker,
#game .dialogue.riskDialogueMode .speaker{
  font-size:20px!important;
  line-height:1.25!important;
  padding:8px 14px!important;
  margin-bottom:10px!important;
}
#game .dialogue.eventDialogueMode .story,
#game .dialogue.riskDialogueMode .story{
  font-size:25px!important;
  line-height:1.72!important;
  min-height:120px!important;
  font-weight:650!important;
  letter-spacing:.01em!important;
}
#game .dialogue.eventDialogueMode .hint,
#game .dialogue.riskDialogueMode .hint{
  font-size:16px!important;
  line-height:1.55!important;
  margin-top:7px!important;
  color:#cbd5e1!important;
}
#game .dialogue.eventDialogueMode .widget,
#game .dialogue.riskDialogueMode .widget{
  margin-top:16px!important;
}
#game .dialogue.eventDialogueMode .choices,
#game .dialogue.riskDialogueMode .choices{
  gap:12px!important;
  margin-top:16px!important;
}
#game .dialogue.eventDialogueMode .choice,
#game .dialogue.riskDialogueMode .choice{
  min-height:78px!important;
  padding:15px 16px!important;
  border-radius:14px!important;
  font-size:22px!important;
  line-height:1.42!important;
  background:rgba(255,255,255,.075)!important;
}
#game .dialogue.eventDialogueMode .letter,
#game .dialogue.riskDialogueMode .letter{
  font-size:23px!important;
  line-height:1!important;
  margin-right:10px!important;
}
#game .dialogue.eventDialogueMode .cost,
#game .dialogue.riskDialogueMode .cost{
  font-size:17px!important;
  line-height:1.5!important;
  margin-top:6px!important;
  color:#d1d8e5!important;
}
#game .dialogue.eventDialogueMode .adopt,
#game .dialogue.riskDialogueMode .adopt{
  font-size:17px!important;
  line-height:1.15!important;
  padding:10px 13px!important;
  border-radius:10px!important;
}
#game .dialogue.eventDialogueMode .resultBtns,
#game .dialogue.riskDialogueMode .resultBtns{
  gap:12px!important;
  margin-top:14px!important;
}
#game .dialogue.eventDialogueMode .resultBtns button,
#game .dialogue.riskDialogueMode .resultBtns button{
  font-size:18px!important;
  padding:13px 15px!important;
}
@media (max-width:800px){
  #game .dialogue.eventDialogueMode .story,
  #game .dialogue.riskDialogueMode .story{font-size:20px!important;}
  #game .dialogue.eventDialogueMode .choice,
  #game .dialogue.riskDialogueMode .choice{font-size:18px!important;min-height:68px!important;}
  #game .dialogue.eventDialogueMode .cost,
  #game .dialogue.riskDialogueMode .cost{font-size:15px!important;}
  #game .dialogue.eventDialogueMode .adopt,
  #game .dialogue.riskDialogueMode .adopt{font-size:15px!important;}
}
</style>
'''

if 'id="v2854-event-projection"' not in s:
    s=s.replace('</head>', style+'</head>', 1)

if 'v28.5.4 事件閱讀・教室投影大字版' not in s:
    s=s.replace('v28.5.3 課後生活・教室投影大字版','v28.5.4 事件閱讀・教室投影大字版',1)

p.write_text(s,encoding='utf-8')
