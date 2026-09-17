from pathlib import Path
import json

html_path=Path('our14-v28/index.html')
s=html_path.read_text(encoding='utf-8')
start=s.index('const GAME_DATA = ')+len('const GAME_DATA = ')
end=s.index(';\nconst A = GAME_DATA.assets;', start)
data=json.loads(s[start:end])

data['assets']['cg_opening']='cg_opening_v285.webp'
data['prologue'][0]['bg']='cg_opening'
data['prologue'][0]['kick']='PROLOGUE｜九月・07:47｜第一天'
data['prologue'][0]['text']='''九月，早上 7:47。\n\n你站在新的教室門口。\n裡面有人已經聊成一圈，有人低頭滑手機，也有人一個人看著座位表。\n\n你還不知道，接下來七週會發生什麼。'''

by={e['label']:e for e in data['events']}
def set_choices(label, choices):
    e=by[label]
    assert len(choices)==len(e['choices'])==4
    for old,new in zip(e['choices'],choices): old.update(new)

set_choices('第1週・事件2｜班級群組',[
    {'text':'跟著再做一張更狠的，現在大家正嗨','cost':'最快融進氣氛｜也讓照片繼續被傳','result':'你做的那張很快被洗上去。\n\n幾分鐘內又多了十幾個笑臉。你也真的融進了那個晚上。','log':'在班群跟著做了更狠的梗圖。'},
    {'text':'只按個 😂，不再加工','cost':'有參與｜但也等於默默跟著','result':'你按了一個表情。\n\n沒有人特別注意你，但你也沒有讓事情再多一層。','log':'在梗圖事件中只按表情，沒有再加工。'},
    {'text':'私訊家豪：這張有點危險，要不要先收？','cost':'不在群裡掃興｜他可能覺得你太認真','result':'家豪過了一下才回：「有那麼嚴重喔？」\n\n幾分鐘後，那張圖真的被他收回了。','log':'私訊家豪提醒梗圖可能越界。'},
    {'text':'先不回，把群組靜音到明天','cost':'保住自己的晚上｜事情會照樣發展','result':'你把通知關掉。\n\n房間安靜了，但群組裡發生什麼，你今晚不會知道。','log':'把班群靜音，暫時退出梗圖事件。'}
])

set_choices('第1週・事件3｜忘記帶作業',[
    {'text':'現在就說：我寫了，但忘在家','cost':'當下會有點糗｜接受晚交或缺交紀錄','result':'你在老師走到面前前先開口。\n\n老師沒有很高興，但至少你不用再想怎麼掩飾。','log':'主動說明作業忘在家。'},
    {'text':'傳訊息請家人拍作業照片，下午再補交','cost':'能證明有寫｜會麻煩家人一下','result':'你先把狀況說清楚，再傳訊息回家。\n\n事情沒有立刻消失，但你多了一個補救的方法。','log':'請家人拍作業照片並約好補交。'},
    {'text':'先問老師：可不可以下一節前補處理？','cost':'要自己去想補救｜老師不一定答應','result':'老師看了你一眼：「下節前拿方案來跟我說。」\n\n你沒有直接過關，但也沒有只能站著等結果。','log':'向老師爭取一個短時間補救作業。'},
    {'text':'借同學的照著重寫一份先交出去','cost':'眼前最像有交｜被看出來會更麻煩','result':'你把同學的作業拉到旁邊。\n\n寫得越快，你越注意老師有沒有往這裡看。','log':'借同學作業照著重寫。'}
])

set_choices('第2週・事件2｜可以借我100嗎？',[
    {'text':'直接借他100，朋友先吃飯比較重要','cost':'最爽快｜明天能不能拿回來還不知道'},
    {'text':'我幫你買午餐，其他的你自己想辦法','cost':'💰 -60｜幫忙，但把範圍縮小'},
    {'text':'說自己這週也有預算，今天沒辦法借','cost':'保住預算｜可能有一點不好意思'},
    {'text':'先講好明天怎麼還，再決定要不要借','cost':'界線比較清楚｜也可能顯得很計較'}
])

set_choices('第2週・事件3｜凌晨12點的群組',[
    {'text':'繼續看，等群組真的安靜再睡','cost':'最不怕漏消息｜睡眠會一直被切碎'},
    {'text':'只確認作業資訊，然後靜音','cost':'資訊先顧到｜半夜補充可能會漏'},
    {'text':'現在就不看了，明早到校再問','cost':'睡得比較完整｜明早要自己補資訊'},
    {'text':'請一個熟的同學有大事再標你，然後下線','cost':'把重要消息交給朋友｜需要信任對方'}
])

set_choices('第3週・事件2｜手機可以給我看嗎？',[
    {'text':'只打開她擔心的班群，給她看五分鐘','cost':'能讓她安心一些｜還是會讓出部分隱私','result':'你只打開她真正擔心的群組。\n\n她看完沒有再往下翻，但你還是覺得界線變得很具體。','log':'讓媽媽看特定班群。'},
    {'text':'先問她到底擔心什麼，再一起看那一部分','cost':'談得比較久｜但界線和安全都能說清楚','result':'你先問：「妳是怕陌生人，還是怕我們群裡有人亂傳東西？」\n\n話題慢慢從「交手機」變成「到底在擔心什麼」。','log':'先釐清家長擔心，再談手機安全。'},
    {'text':'把手機拿回來：這是我的隱私','cost':'界線最直接｜衝突也可能最直接'},
    {'text':'不給聊天內容，但一起檢查隱私與封鎖設定','cost':'不看訊息｜她不一定覺得這樣就夠','result':'你們一起看了隱私設定、陌生訊息和封鎖名單。\n\n媽媽還是想知道更多，但至少她看到你不是完全不管安全。','log':'用設定檢查取代開放全部聊天。'}
])

set_choices('第3週・事件3｜昨天那句話',[
    {'text':'先不要提，等氣氛自己恢復','cost':'最省力｜那個疙瘩可能還在'},
    {'text':'只說一句：昨天我口氣不好，但我還是想談界線','cost':'先承認自己的部分｜不把問題全部吞回去','result':'你說完後，媽媽沒有立刻回。\n\n但你至少把「道歉」和「我還有話想說」放在同一句裡。','log':'為語氣道歉，同時保留自己的界線。'},
    {'text':'到學校後用訊息講，比當面比較說得完整','cost':'比較能整理語氣｜少了當面反應'},
    {'text':'早上先照平常相處，晚上再找時間談','cost':'先讓生活回到日常｜真正的話題要記得回來','result':'你照平常說了聲「我出門了」。\n\n氣氛沒有立刻變好，但至少今天不是從冷戰開始。','log':'先恢復日常互動，晚點再談衝突。'}
])

set_choices('第4週・事件2｜有人沒做',[
    {'text':'先把明天交出去，報告後再談分工','cost':'期限最安全｜公平問題會被延後'},
    {'text':'現在就問：小晴為什麼全做、家豪卡在哪','cost':'可能讓群組更尷尬｜但原因會比較清楚'},
    {'text':'把剩下工作重新拆成很小的幾塊，今晚各自收尾','cost':'你要多花時間協調｜每個人都得再做一點'},
    {'text':'保留現在版本，但明天每個人只講自己原本負責的部分','cost':'不再重做｜成果不一定最漂亮','result':'你們決定不再改簡報。\n\n明天誰負責什麼，就照原本分工上台。完成度不一定最好，但責任變得很清楚。','log':'保留現況，讓每個人承擔原本分工。'}
])

set_choices('第5週・事件3｜考卷要不要簽名',[
    {'text':'今晚就拿出去，不先排演答案','cost':'最早面對｜可能被問很多'},
    {'text':'先整理自己錯在哪，再拿出去談','cost':'多花一點時間｜談話比較有方向'},
    {'text':'先用訊息跟家人說分數，等等再拿紙本出去','cost':'比較容易開口｜真正的談話還是躲不掉','result':'你先傳了一句：「我今天數學48，等一下拿考卷給你。」\n\n按下送出後，心跳還是很快，但至少第一句已經不用當面擠出來。','log':'先用訊息告知分數，再拿紙本給家人。'},
    {'text':'自己模仿簽名，先把這關過掉','cost':'眼前最省事｜留下高風險後果'}
])

set_choices('第6週・事件1｜段考範圍公告',[
    {'text':'先把整週讀書和休息都排進時間表','cost':'先花時間規劃｜之後比較不亂'},
    {'text':'今晚先救最弱的數學，其他科明天再排','cost':'弱科先動起來｜其他科會晚一點才進場'},
    {'text':'先完成兩個最容易開始的小任務','cost':'最快換到進度感｜不一定先處理最弱科','result':'你先把英文單字和社會一小段收掉。\n\n範圍沒有突然變少很多，但「我完全還沒開始」的感覺先消失了。','log':'段考範圍公告後先完成兩個小任務。'},
    {'text':'先問老師或同學：哪些範圍最值得先抓','cost':'能拿到方向｜最後還是得自己決定','result':'你先去問了最容易失分的地方。\n\n別人沒有替你讀書，但你比較知道第一步要放在哪。','log':'先詢問段考準備的優先順序。'}
])

set_choices('第6週・事件3｜朋友找你打遊戲',[
    {'text':'打一場，但開計時器，結束就下線','cost':'真的能休息一下｜要有辦法在時間到時停'},
    {'text':'今天不打，把原本兩科做完','cost':'進度最穩｜跟朋友少一段時間'},
    {'text':'先完成一個明確任務，再決定要不要玩','cost':'延後滿足｜今晚還是保留玩的可能'},
    {'text':'叫阿哲一起讀30分鐘，之後再開一場','cost':'把朋友拉進計畫｜他不一定想配合'}
])

set_choices('第7週・事件1｜只剩三天',[
    {'text':'照原本計畫走，不因焦慮全部重排','cost':'可能還是有沒讀完的｜但節奏穩'},
    {'text':'先碰最讓你焦慮的那一科，讀到一個停損點','cost':'先處理最大的壓力｜容易在那科花太久','result':'你直接打開最不想碰的那一科。\n\n讀到設定的時間，你停了下來。它沒有變簡單，但至少沒有再整晚躲著它。','log':'先處理最焦慮的科目並設定停損點。'},
    {'text':'先完成兩個最容易收尾的小任務','cost':'先換到進度感｜不一定先處理最弱科'},
    {'text':'找同學互問30分鐘重點，再各自補自己的弱科','cost':'能快速發現盲點｜也可能聊到超時','result':'你們快速互問一輪。\n\n有幾題你原本以為會，真的被問時才發現答不完整。','log':'考前三天和同學互問題目。'}
])

set_choices('第7週・事件3｜23:48',[
    {'text':'把眼前這一個章節收完，最晚1:00睡','cost':'多完成一塊｜⚡ -12、會欠一點睡眠','effect':{'stats':{'study':3},'energy':-12,'stress':3,'hidden':{'sleepDebt':2,'lateCram':1,'studyEffort':1}},'result':'你沒有再開新的範圍，只把眼前這章收尾。\n\n時間走到 00:57，你把書闔上。','log':'考前把一個章節收完後睡覺。'},
    {'text':'現在就睡，接受有些東西沒讀完','cost':'放掉最後內容｜換明天比較清醒的自己'},
    {'text':'只看最不熟的兩個地方，12:30關燈','cost':'做取捨｜不是全部都顧到'},
    {'text':'跟同學語音快問30分鐘，時間到就一起下線','cost':'可以互相補洞｜也可能越聊越晚','effect':{'stats':{'study':2,'social':2},'energy':-6,'stress':1,'hidden':{'friendTrust':1,'studyEffort':1}},'result':'你們約好一人出幾題。\n\n有幾題真的補到了，也有幾題誰都不確定。12:20，你們一起說「好了，睡覺」。','log':'考前和同學快速互問後下線。'}
])

by['第1週・事件1｜新的座位']['cinematic']=True
by['第1週・事件1｜新的座位']['bg']='cg_opening'
by['第1週・事件1｜新的座位']['unlock']='cg_opening'

new_blob=json.dumps(data, ensure_ascii=False, separators=(',',':'))
s=s[:start]+new_blob+s[end:]

needle='const memories=[\n  {key:"cg_store",name:"放學後的邀約"},'
if needle in s:
    s=s.replace(needle,'const memories=[\n  {key:"cg_opening",name:"開學第一天｜站在新教室門口"},\n  {key:"cg_store",name:"放學後的邀約"},',1)
else: raise SystemExit('memories marker missing')

old='''function showEventIntro(){\n  setEventSceneMode("intro");\n  const kind=document.getElementById("eventIntroKind");\n  const title=document.getElementById("eventIntroTitle");\n  if(kind)kind.textContent=eventKindLabel(activeEvent);\n  if(title)title.textContent=activeEvent?.label||"事件";\n}'''
new='''function showEventIntro(){\n  setEventSceneMode("intro");\n  const kind=document.getElementById("eventIntroKind");\n  const title=document.getElementById("eventIntroTitle");\n  const isMain=activeEvent&&Number.isFinite(activeEvent.week)&&!activeEvent.isExtra&&!activeEvent.isAftermath&&!activeEvent.isHealth&&!activeEvent.isConsequence;\n  if(kind)kind.textContent=isMain?`WEEK ${activeEvent.week}｜${WEEK_LABELS[activeEvent.week]||"主線故事"}`:eventKindLabel(activeEvent);\n  if(title)title.textContent=activeEvent?.label||"事件";\n}'''
if old not in s: raise SystemExit('showEventIntro marker missing')
s=s.replace(old,new,1)

old='function startPrologue(){ proI=0; document.getElementById(\'prologue\').classList.add(\'show\'); showPro(); }'
new='function startPrologue(){ proI=0; unlock(\'cg_opening\'); document.getElementById(\'prologue\').classList.add(\'show\'); showPro(); }'
if old not in s: raise SystemExit('startPrologue marker missing')
s=s.replace(old,new,1)

old_text='鐘聲響了。\\n\\n有人立刻開始對答案，有人趴在桌上，也有人笑著喊『終於考完了』。\\n\\n你把筆收進鉛筆盒，跟著人群走出教室。\\n\\n七週前，你第一次坐到那個位置。現在的你，已經跟那天不太一樣了。'
new_text='鐘聲響了。\\n\\n有人立刻開始對答案，有人趴在桌上，也有人只想先去買杯飲料。\\n\\n你把筆收進鉛筆盒。這張考卷會有分數，但這七週留下來的，不只有分數。\\n\\n七週前，你第一次站在這個班的門口。現在，你已經做過很多只有自己才知道代價的選擇。'
if old_text not in s: raise SystemExit('epilogue copy marker missing')
s=s.replace(old_text,new_text,1)

s=s.replace('v28.4 劇情・CG演出版：','v28.5 劇情分歧・章節CG版：',1)
html_path.write_text(s,encoding='utf-8')
print('patched',html_path,html_path.stat().st_size)
