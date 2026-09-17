from pathlib import Path
import json, re
p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')
if 'v28.4 劇情・CG演出版' in s:
    print('already v28.4')
    raise SystemExit(0)
start=s.index('const GAME_DATA = ')+len('const GAME_DATA = ')
end=s.index(';\nconst ', start)
data=json.loads(s[start:end])

data['prologue']=[
  {"bg":"bg_gate","kick":"PROLOGUE｜九月・07:47","text":"九月，早上 7:47。\n\n你站在新的教室門口。\n裡面有人已經聊成一圈，有人低頭滑手機，也有人一個人看著座位表。"},
  {"bg":"bg_classroom","kick":"PROLOGUE｜新的座位","text":"你的名字被印在一張新的座位表上。\n\n從今天開始，旁邊坐誰、午休跟誰說話、放學去哪裡，很多事情都還沒有答案。"},
  {"bg":"bg_classroom","kick":"PROLOGUE｜14歲","text":"十四歲不是突然長大的那一天。\n\n它比較像很多很小的決定：要不要跟上大家、要不要說實話、要不要休息、要不要開口。\n這些選擇，會一點一點把生活推向不同的地方。"},
  {"bg":"bg_gate","kick":"CHAPTER 01｜開學後的七週","text":"第一章｜九月，新生活開始了\n\n這個主角沒有固定的臉，也沒有設定好的性別。\n因為接下來七週，主角會變成什麼樣的人——由全班一起決定。"}
]

events={e['label']:e for e in data['events']}
def edit_event(label, *, text=None, choices=None, cinematic=None, remove_sprite=False, unlock=None):
    e=events[label]
    if text is not None: e['text']=text
    if choices:
        for idx, patch in enumerate(choices):
            e['choices'][idx].update(patch)
    if cinematic is not None: e['cinematic']=cinematic
    if remove_sprite: e.pop('sprite',None)
    if unlock is not None: e['unlock']=unlock

edit_event('第1週・事件1｜新的座位',
 text='''第一節還沒開始。\n\n阿哲已經跟前後左右聊成一片，他拍了一下你的桌角：「走啦，我帶你去福利社。」\n\n你轉頭時，看見小晴還一個人坐在位置上。''',
 choices=[
  {"text":"先跟阿哲走，至少先認識一個人","cost":"比較不尷尬｜💰 -35","result":"你跟著阿哲走出教室。\n\n他一路講哪個窗口最快、哪個老師最嚴格。你還沒有真的融進班上，但至少已經有一個人會在走廊叫你的名字。"},
  {"text":"留下來跟小晴聊兩句","cost":"要先主動開口","result":"你問：「妳以前是哪間學校的？」\n\n小晴停了一下才回答。話沒有很多，但回座位時，你們已經不是完全的陌生人。"},
  {"text":"一個人逛校園，先把環境摸熟","cost":"暫時不站任何一邊","result":"你沿著走廊走到操場，記住合作社、圖書館和社團布告欄的位置。\n\n新學校還是陌生，但至少你知道自己可以先照自己的步調。"},
  {"text":"問阿哲：要不要也找小晴一起？","cost":"可能有一點尷尬","result":"阿哲愣了一秒：「喔……好啊。」\n\n小晴原本也有點意外，最後還是跟著一起走。你沒有突然變成社交高手，只是替三個人多開了一個位置。"}
 ])
edit_event('第1週・事件2｜班級群組',
 text='''晚上 8:36，班級群組突然爆出一排通知。\n\n家豪把老師上課時的一張照片做成梗圖，下面已經刷了二十幾個「哈哈」。\n有人標記你：「你一定有更好笑的版本吧？」''',
 choices=[
  {"text":"回一張更狠的梗圖，先融進氣氛","cost":"很有參與感｜也把照片再傳出去"},
  {"text":"按個 😂 就好，不再加工","cost":"有參與，但不把事情做大"},
  {"text":"回一句：這張留群內就好吧","cost":"可能被嫌有點掃興"},
  {"text":"先靜音，明天再看","cost":"保住自己的晚上｜可能漏訊息"}
 ])
edit_event('第1週・事件3｜忘記帶作業',
 text='''早自習，老師從第一排開始收作業。\n\n你打開書包，摸到最底層時才想起來：昨天明明寫完了，但作業本還躺在家裡書桌上。\n\n老師已經收到你前面那一桌。''',
 choices=[
  {"text":"現在就說：我寫了，但忘在家","cost":"當下會有點糗"},
  {"text":"借同學的先抄一份交出去","cost":"眼前能過｜之後可能更麻煩"},
  {"text":"先拖著，也許老師等等忘了","cost":"現在不用面對｜壓力留著"},
  {"text":"問家人能不能順路送來","cost":"能補救｜但會麻煩家人"}
 ])

edit_event('第2週・事件1｜大家都要去',
 text='''週五放學前，群組開始約週末出去。\n\n六個人很快都說「+1」。阿哲直接傳：「你一定會來吧？」\n\n你想去，也想起這週的零用錢不是只要撐這一天。''',
 cinematic=True, remove_sprite=True)
edit_event('第2週・事件2｜可以借我100嗎？',
 text='''午休鐘剛響，阿哲摸遍外套和書包。\n\n「完了，我今天真的沒帶錢。」\n他看向你：「可以先借我 100 嗎？我明天還你。」\n\n你知道他不是陌生人，但 100 元也不是完全不用想的小錢。''',
 choices=[
  {"text":"直接借他 100，朋友先吃飯比較重要","cost":"💰 -100｜明天能不能拿回來還不知道"},
  {"text":"幫他買午餐，不直接給現金","cost":"💰 -60｜幫忙但把範圍縮小"},
  {"text":"說自己這週也有預算，沒辦法借","cost":"💰 0｜可能有一點不好意思"},
  {"text":"先問：你明天真的方便還嗎？","cost":"多確認一步｜可能顯得很計較"}
 ])
edit_event('第2週・事件3｜凌晨12點的群組',
 text='''晚上 11:58。\n\n班群還在跳：有人問明天作業、有人補充老師交代的事，也有人開始洗迷因。\n\n你明天第一節有英文小考。手機每亮一次，你就會想：會不會剛好漏掉重要的？''',
 choices=[
  {"text":"繼續看，等群組真的安靜再睡","cost":"比較安心｜睡眠會被吃掉"},
  {"text":"只確認作業資訊，然後靜音","cost":"可能還是漏掉半夜補充"},
  {"text":"現在就不看了，明天到校再問","cost":"睡得到｜明早要自己補資訊"},
  {"text":"回一句『我先睡，有重要的明天提醒我』","cost":"把界線說出來｜也要相信朋友"}
 ])

edit_event('第3週・事件1｜晚上9:47',
 text='''晚上 9:47，你才剛把鞋脫掉。\n\n媽媽從餐桌那邊抬頭：\n「今天怎麼那麼晚？」\n「跟誰？」\n「去哪？」\n「功課寫完了嗎？」\n\n你知道她在擔心，但現在每一個問題都像下一個問題的前奏。''',
 choices=[
  {"text":"忍不住回：可以不要一直問嗎？","cost":"當下很真實｜氣氛可能直接炸掉"},
  {"text":"先把『去哪、跟誰』說清楚","cost":"最快結束不確定｜隱私少一點"},
  {"text":"先回房間，今晚不想講","cost":"先保住自己｜事情會留到之後"},
  {"text":"說自己很累，十分鐘後再談","cost":"先停一下｜但答應等等要回來"}
 ], cinematic=True, remove_sprite=True)
edit_event('第3週・事件2｜手機可以給我看嗎？',
 text='''隔天晚上，媽媽又提到新聞裡的網路事件。\n\n「你們班群有沒有奇怪的人？手機借我看一下。」\n\n她的表情不像在抓你犯錯，可是你的聊天紀錄裡，也有一些你不想逐條被翻看的東西。''',
 choices=[
  {"text":"直接給她看，至少讓她放心","cost":"家庭信任可能↑｜自己的隱私會讓出去"},
  {"text":"可以談安全，但不想開放全部聊天","cost":"要把界線說得很清楚"},
  {"text":"把手機拿回來：這是我的隱私","cost":"界線很清楚｜衝突也可能很直接"},
  {"text":"只打開她真正擔心的班群","cost":"折衷｜她不一定覺得夠"}
 ])
edit_event('第3週・事件3｜昨天那句話',
 text='''早餐桌比平常安靜。\n\n昨天那段對話沒有再被提起，但你們都知道它沒有完全消失。\n\n出門前只剩幾分鐘，你可以把它留著，也可以做一點什麼。''',
 choices=[
  {"text":"先不要提，等氣氛自己恢復","cost":"最省力｜那個疙瘩可能還在"},
  {"text":"只說一句：昨天我口氣不好","cost":"先承認自己的部分｜不代表全是你的錯"},
  {"text":"到學校後用訊息講，比當面容易","cost":"比較能整理語氣｜少了當面反應"},
  {"text":"先找家裡比較好說話的人聊","cost":"多一個人介入｜也多一個支持"}
 ])

edit_event('第4週・事件1｜分組報告',
 text='''「四個人一組，下週上台。」\n\n教室立刻開始搬椅子。阿哲朝你招手：「我們這邊還差一個！」\n家豪站在另一邊，還沒有組。\n\n分組看起來像是在選朋友，但你知道一週後還要一起把東西做完。''',
 choices=[
  {"text":"跟阿哲那組，至少合作起來不尷尬","cost":"人際最輕鬆｜做事方式還不知道"},
  {"text":"主動找小晴、家豪組一組","cost":"需要先開口｜可能比較陌生"},
  {"text":"先等等，看誰最後來找你","cost":"不用主動｜選擇會越來越少"},
  {"text":"先問大家想做什麼，再決定跟誰組","cost":"比較慢｜但比較知道合作風格"}
 ])
edit_event('第4週・事件2｜有人沒做',
 text='''報告前一天晚上 9:12，小晴把最新版簡報丟進群組。\n\n她只打：「我把還沒完成的先補起來了。」\n\n你點開後才發現，家豪原本那一頁幾乎整張被重做。\n現在簡報完成了，但群組安靜得有點不自然。''',
 choices=[
  {"text":"先別碰了，至少明天能交","cost":"最快結束｜問題可能留到下一次"},
  {"text":"同時問小晴累不累，也問家豪卡在哪","cost":"要處理尷尬｜可能找到真正原因"},
  {"text":"直接把工作退回家豪，叫他自己做完","cost":"責任很清楚｜關係可能變硬"},
  {"text":"把家豪的工作拆小，再叫小晴不要全包","cost":"你要多花時間協調"}
 ])
edit_event('第4週・事件3｜上台前五分鐘',
 text='''下一節就要上台。\n\n家豪一直盯著手上的講稿，突然很小聲地說：\n「我等等真的不想講。我一站上去腦袋就會空白。」\n\n距離上課還有五分鐘。你們可以救這一次，但不可能把所有問題都一次解決。''',
 choices=[
  {"text":"叫他先撐過去：都做到這裡了","cost":"不用重排｜他可能更緊張"},
  {"text":"把他的內容縮成三句重點","cost":"臨時改分工｜但任務變小"},
  {"text":"這次幫他講一小段，但約好下次要早說","cost":"你多扛一點｜也把界線說清楚"},
  {"text":"先在教室後面陪他完整講一次","cost":"用掉最後幾分鐘｜不一定來得及改"}
 ])

edit_event('第5週・事件1｜48分',
 text='''數學考卷一張一張往後傳。\n\n你看到右上角的紅字：48。\n\n阿哲 71，小晴 94，家豪 52。沒有人笑你，也沒有人特別看你，但那個「48」就是一直留在視線裡。\n\n今天放學後，你要先處理哪一件事？''',
 choices=[
  {"text":"今晚就把錯題重算一輪","cost":"進度會前進｜⚡ -8、😵 +2"},
  {"text":"今天先不要碰，讓自己休息一晚","cost":"心情先喘口氣｜問題還在"},
  {"text":"先找人問：我到底是哪些觀念不會？","cost":"要承認自己卡住｜但更快知道問題"},
  {"text":"先把考卷收好，暫時不要讓家裡看到","cost":"今晚比較安靜｜😵 壓力會留下"}
 ], cinematic=True)
edit_event('第5週・事件2｜94分也不開心？',
 text='''下課後，小晴把 94 分的考卷對折，再對折。\n\n「那兩題我明明都會。」\n她沒有哭，也沒有發脾氣，只是一直盯著桌面。\n\n你手上還拿著自己的 48。這一刻，你不一定有餘裕當一個很會安慰人的朋友。''',
 choices=[
  {"text":"忍不住說：妳 94 還不滿意喔？","cost":"很直覺｜也可能讓她覺得自己不該難過"},
  {"text":"問：妳是不是對自己要求很高？","cost":"多聽一點｜可能聽到更重的壓力"},
  {"text":"先不接這題，因為自己現在也很難受","cost":"先顧自己｜關係不一定會更靠近"},
  {"text":"交換一題：她教你，你陪她看她錯的地方","cost":"把兩個人的問題放在同一張桌上"}
 ], cinematic=True, remove_sprite=True, unlock='cg_qing_crisis1')
edit_event('第5週・事件3｜考卷要不要簽名',
 text='''晚上，書包放在房間地板上。\n\n老師說明天一定要交家長簽名。那張 48 分的考卷就夾在最上面。\n\n你甚至已經想像得到家人的第一句話會是什麼。''',
 choices=[
  {"text":"今晚就拿出去，不先排演答案","cost":"最早面對｜可能被問很多"},
  {"text":"先整理自己錯在哪，再拿出去談","cost":"要先做功課｜談話比較有方向"},
  {"text":"拖到明天出門前再拿","cost":"今晚先不用談｜壓力會跟著睡覺"},
  {"text":"自己模仿簽名，先把這關過掉","cost":"眼前最省事｜留下高風險後果"}
 ])

edit_event('第6週・事件1｜段考範圍公告',
 text='''午休前，老師把第一次段考範圍投在螢幕上。\n\n數學最長，社會也不少，英文看起來還能追。有人立刻拍照，有人已經開始說「完了」。\n\n你現在最需要的，不一定是「最努力」的選項，而是決定從哪裡開始。''',
 choices=[
  {"text":"先把整週讀書和休息排進時間表","cost":"先花時間規劃｜之後比較不亂"},
  {"text":"先救最弱的數學，其他科晚點再說","cost":"數學進度快｜其他科可能堆起來"},
  {"text":"約朋友一起讀，靠彼此把進度拉起來","cost":"比較不孤單｜效率不一定穩"},
  {"text":"先把截圖收好，週末再正式開始","cost":"現在壓力比較小｜之後可用時間更少"}
 ])
edit_event('第6週・事件2｜今天真的讀不下去',
 text='''放學前，教室已經快空了。\n\n小晴盯著同一頁筆記很久，最後把筆放下。\n「我今天真的什麼都讀不進去。」\n\n她笑了一下，那個笑比較像是在替自己圓場。''',
 choices=[
  {"text":"說：妳成績這麼好，真的不用那麼擔心","cost":"想讓她放心｜也可能讓她更難說下去"},
  {"text":"先離開座位走一圈，問她要不要一起","cost":"少一點讀書時間｜先把人拉回來"},
  {"text":"陪她把今天的待辦縮成只剩一件","cost":"不追求全部完成｜先找可做到的"},
  {"text":"告訴她：其實你最近也有點撐不住","cost":"沒有立刻解決問題｜但彼此不用裝沒事"}
 ], cinematic=True, remove_sprite=True, unlock='cg_qing_crisis2')
edit_event('第6週・事件3｜朋友找你打遊戲',
 text='''晚上 8:20。\n\n阿哲傳來：「上線啦！就打一場。」\n\n你原本打算今晚完成兩科，但其實也已經讀得有點煩。\n「打一場」可能真的只是一場，也可能不是。''',
 choices=[
  {"text":"先打一場，讓腦袋休息一下","cost":"心情會好一點｜時間可能一路往後拖"},
  {"text":"今天直接不打，把進度做完","cost":"比較穩｜跟朋友少一段時間"},
  {"text":"先完成一科，再重新決定","cost":"延後滿足｜保留之後玩的可能"},
  {"text":"拉阿哲一起讀 30 分鐘，再決定要不要玩","cost":"把朋友拉進計畫｜他不一定配合"}
 ])

edit_event('第7週・事件1｜只剩三天',
 text='''距離第一次段考只剩三天。\n\n桌上同時攤著英文單字、數學錯題、自然講義和還沒整理完的社會範圍。\n\n最可怕的不是「完全沒讀」，而是每一科都還有一點沒做完。''',
 choices=[
  {"text":"照原本計畫走，不因焦慮全部重排","cost":"可能還是有沒讀完的｜但節奏穩"},
  {"text":"哪一科最讓你焦慮，就先碰哪一科","cost":"比較像在救火｜容易一直換"},
  {"text":"先完成兩個最容易收尾的小任務","cost":"先換到進度感｜不一定先處理最弱科"},
  {"text":"取消所有休息，三天全部拿來讀","cost":"進度會衝很快｜⚡ -12、😵 +5"}
 ])
edit_event('第7週・事件2｜考前一句話',
 text='''吃晚餐時，媽媽像隨口一樣說：\n\n「第一次段考，至少不要考得太難看喔。」\n\n她說完就繼續夾菜。你知道她可能只是提醒，但那句話已經進到腦袋裡。''',
 choices=[
  {"text":"先不回，這餐不要再多一件事","cost":"暫時沒有衝突｜壓力自己留著"},
  {"text":"直接說：妳這樣講，我壓力會更大","cost":"可能有點僵｜但她會知道影響"},
  {"text":"用玩笑把這句話帶掉","cost":"氣氛比較輕｜真正需求沒有被說出來"},
  {"text":"告訴她：今晚你最需要她怎麼做","cost":"要講得具體｜也給對方一個可做的方向"}
 ])
edit_event('第7週・事件3｜23:48',
 text='''時間：23:48。\n\n桌上的書還沒收，群組裡還有人傳「我社會還沒看完」。\n明天早上，就是第一次段考。\n\n現在多讀一點，可能多記一點；現在去睡，也等於放掉一些還沒完成的東西。''',
 choices=[
  {"text":"再撐兩小時，把能塞的都塞完","cost":"多一點進度｜⚡ -18、睡眠債 +"},
  {"text":"現在就睡，接受有些東西沒讀完","cost":"放掉最後內容｜換明天的清醒"},
  {"text":"只看最不熟的兩個地方，12:30 關燈","cost":"做取捨｜不是全部都顧到"},
  {"text":"看到大家還在讀，乾脆全部從頭再翻","cost":"最有『我有在努力』的感覺｜⚡ -22、😵 +10"}
 ], cinematic=True)

for label in ['第2週・事件1｜大家都要去','第3週・事件1｜晚上9:47','第5週・事件1｜48分','第5週・事件2｜94分也不開心？','第6週・事件2｜今天真的讀不下去','第7週・事件3｜23:48']:
    events[label]['cinematic']=True
    if events[label].get('bg','').startswith('cg_'):
        events[label].pop('sprite',None)

new_json=json.dumps(data, ensure_ascii=False, separators=(',',':'))
s=s[:start]+new_json+s[end:]

old='const WEEK_LABELS={1:"開學第一週",2:"開始熟悉班級",3:"關係慢慢成形",4:"合作與分組",5:"第一次成績壓力",6:"段考準備期",7:"第一次段考前"};'
new='const WEEK_LABELS={1:"我在這個班，是誰？",2:"跟上大家，還是照自己的步調？",3:"長大一點之後，家裡還能管多少？",4:"朋友不只是在一起玩",5:"第一次真的覺得自己不夠好",6:"開始撐不住的人，不只你一個",7:"第一次段考前的最後三天"};'
if old not in s: raise SystemExit('WEEK_LABELS source missing')
s=s.replace(old,new,1)

pattern_store=r'  if\(ev\.dynamic==="storeMoney"\) return `.*?`;'
replacement_store='''  if(ev.dynamic==="storeMoney") return `週五放學前，群組開始約週末出去。\n\n六個人很快都說「+1」。阿哲直接傳：「你一定會來吧？」\n\n你也想去。只是你看了一眼錢包：現在還有 ${state.money} 元，而這週還沒有結束。`;'''
s,n=re.subn(pattern_store,replacement_store,s,count=1)
if n!=1: raise SystemExit(f'dynamic store replacement count={n}')
pattern_group=r'  if\(ev\.dynamic==="grouping"\) return `.*?`;'
replacement_group='''  if(ev.dynamic==="grouping") return `「四個人一組，下週上台。」\n\n教室立刻開始搬椅子。阿哲朝你招手：「我們這邊還差一個！」\n家豪也還沒有組。${relationStage("qing").n>=1?"\n小晴抬頭看了你一眼，好像也在等你決定。":""}\n\n分組看起來像在選朋友，但一週後還要一起把東西做完。`;'''
s,n=re.subn(pattern_group,lambda m: replacement_group,s,count=1)
if n!=1: raise SystemExit(f'dynamic grouping replacement count={n}')
s=s.replace('?"\n小晴抬頭看了你一眼，好像也在等你決定。":""','?"\\n小晴抬頭看了你一眼，好像也在等你決定。":""',1)

pattern=r'  if\(ev\.dynamic==="night"\)\{let line="還有好多。";.*?return `\$\{line\}\\n\\n時間：23:48。\\n桌上的書還沒收，明天早上就是第一次段考。`;\}'
replacement='''  if(ev.dynamic==="night"){let line="還有好多。"; if((state.hidden.mathPrep||0)>=5 && state.stress<55) line="還有一些沒看完，但你知道自己不是完全沒準備。"; else if(state.stress>=55) line="每翻一頁，都覺得還有另一頁更重要。"; else if((state.hidden.avoidance||0)>=5) line="你開始想到前幾天那些『明天再說』。"; return `${line}\n\n時間：23:48。群組裡還有人傳「我社會還沒看完」。\n明天早上，就是第一次段考。`; }'''
s,n=re.subn(pattern,replacement,s,count=1)
if n!=1: raise SystemExit(f'dynamic night replacement count={n}')

s=s.replace(
'''function eventKindLabel(ev){
  if(ev?.isAftermath)return "AFTERMATH｜後續影響";''',
'''function eventKindLabel(ev){
  if(ev?.cinematic)return "CG MOMENT｜關鍵場景";
  if(ev?.isAftermath)return "AFTERMATH｜後續影響";''',1)
old_enter='''  setEventSceneMode("play");
  renderEventDataBar();
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
new_enter='''  setEventSceneMode("play");
  renderEventDataBar();
  if(activeEvent.cinematic){
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
  }
  document.getElementById('speaker').textContent=activeEvent.speaker||"旁白";'''
if old_enter not in s: raise SystemExit('enterCurrentEvent source missing')
s=s.replace(old_enter,new_enter,1)

old_show='function showExam(){\n  switchScreen(\'game\'); renderSide(); unlock(\'bg_gate\');'
if old_show not in s: raise SystemExit('showExam source missing')
s=s.replace(old_show,"function showExamResults(){\n  switchScreen('game'); renderSide(); unlock('bg_gate');",1)
wrapper=r'''function showExam(){
  if(!state.examEpilogueSeen){
    state.examEpilogueSeen=true;
    switchScreen('game');
    renderSide();
    unlock('bg_gate');
    activeEvent={label:"第一章｜考完之後",speaker:"旁白",bg:"bg_gate",cinematic:true};
    setVisual(activeEvent);
    setEventSceneMode("play");
    document.getElementById("eventDataBar")?.classList.remove("show");
    document.querySelector("#game .topbar")?.classList.add("cinematicHidden");
    document.getElementById('speaker').textContent="旁白";
    document.getElementById('widget').innerHTML="";
    document.getElementById('story').textContent="鐘聲響了。\n\n有人立刻開始對答案，有人趴在桌上，也有人笑著喊『終於考完了』。\n\n你把筆收進鉛筆盒，跟著人群走出教室。\n\n七週前，你第一次坐到那個位置。現在的你，已經跟那天不太一樣了。";
    document.getElementById('hint').textContent="先不要急著看分數。回頭看看，這七週留下了什麼。";
    document.getElementById('choices').innerHTML='<button class="choice" onclick="setEventSceneMode(\'off\');showExamResults()"><div><span class="letter">01</span>看看這七週留下的結果</div><span class="adopt">繼續</span></button>';
    saveLocal(false);
    return;
  }
  showExamResults();
}
'''
idx=s.index('function showExamResults(){')
s=s[:idx]+wrapper+s[idx:]

s=s.replace('prologueSeen:false,finished:false,chapter1Review:null,sickTurns:0,healthCooldown:0,',
            'prologueSeen:false,finished:false,examEpilogueSeen:false,chapter1Review:null,sickTurns:0,healthCooldown:0,',1)
s=s.replace('v28.3 老師總網址雲端版：','v28.4 劇情・CG演出版：',1)

out=p
out.write_text(s,encoding='utf-8')
for needle in ['v28.4 劇情・CG演出版','CG MOMENT｜關鍵場景','第一章｜考完之後','我在這個班，是誰？','examEpilogueSeen:false']:
    assert needle in s, needle
print('OK v28.4')
