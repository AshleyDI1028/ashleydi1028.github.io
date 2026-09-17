from pathlib import Path

p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

style=r'''
<style id="v2853-schedule-projection">
/* 課後生活安排：教室投影大字版 */
.modal:has(.activities){
  width:min(1180px,96vw)!important;
  padding:28px 30px!important;
}
.modal:has(.activities) h2{
  font-size:34px!important;
  line-height:1.25!important;
  margin-bottom:12px!important;
}
.modal:has(.activities) h3{
  font-size:24px!important;
  line-height:1.35!important;
  margin:20px 0 12px!important;
}
.modal:has(.activities) p,
.modal:has(.activities) .checkpoint,
.modal:has(.activities) .healthHint,
.modal:has(.activities) .traitBox{
  font-size:19px!important;
  line-height:1.7!important;
}
.modal:has(.activities) .timeBudget{
  margin:16px 0!important;
  padding:17px 20px!important;
  border-radius:16px!important;
  font-size:22px!important;
  line-height:1.65!important;
}
.modal:has(.activities) .timeBudget b{
  font-size:28px!important;
  font-weight:1000!important;
}
.modal:has(.activities) .pickedList{
  gap:11px!important;
  margin:14px 0!important;
}
.modal:has(.activities) .pickedItem{
  min-height:58px!important;
  padding:13px 16px!important;
  border-radius:13px!important;
  font-size:19px!important;
  line-height:1.5!important;
}
.modal:has(.activities) .slots{
  gap:12px!important;
  margin:16px 0!important;
}
.modal:has(.activities) .slot{
  min-height:96px!important;
  padding:14px!important;
  font-size:18px!important;
  line-height:1.5!important;
}
.modal:has(.activities) .slot b{
  font-size:21px!important;
}
.modal:has(.activities) .activities{
  grid-template-columns:repeat(2,minmax(0,1fr))!important;
  gap:15px!important;
}
.modal:has(.activities) .activity{
  min-height:118px!important;
  padding:19px 21px!important;
  border-radius:16px!important;
  border-width:2px!important;
  display:flex!important;
  flex-direction:column!important;
  justify-content:center!important;
  gap:6px!important;
}
.modal:has(.activities) .activity strong{
  font-size:25px!important;
  line-height:1.32!important;
  font-weight:1000!important;
  letter-spacing:.01em!important;
}
.modal:has(.activities) .activity span{
  font-size:18px!important;
  line-height:1.55!important;
  color:#d7dfec!important;
}
.modal:has(.activities) .modalBtns{
  gap:12px!important;
  margin-top:20px!important;
}
.modal:has(.activities) .modalBtns button{
  min-height:58px!important;
  padding:14px 18px!important;
  font-size:20px!important;
  border-radius:14px!important;
}
@media (max-width:900px){
  .modal:has(.activities){padding:20px!important;}
  .modal:has(.activities) .activities{grid-template-columns:1fr!important;}
  .modal:has(.activities) .activity{min-height:104px!important;}
}
</style>
'''

if 'id="v2853-schedule-projection"' not in s:
    s=s.replace('</head>',style+'</head>',1)

for old in [
    'v28.5.2 劇情分歧・大字能力面板版',
    'v28.5.1 劇情分歧・能力面板修正版',
    'v28.5 劇情分歧・章節CG版'
]:
    if old in s:
        s=s.replace(old,'v28.5.3 課後生活・教室投影大字版',1)
        break

p.write_text(s,encoding='utf-8')
