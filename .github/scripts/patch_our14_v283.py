from pathlib import Path
p=Path('our14-v28/index.html')
s=p.read_text(encoding='utf-8')

def ro(old,new,label):
    global s
    if old not in s:
        raise SystemExit(f'missing expected source for {label}')
    s=s.replace(old,new,1)

if 'id="teacherCloudList"' not in s:
    ro('<div id="menuClassHint" class="menuClassHint"></div>', '''<div id="menuClassHint" class="menuClassHint"></div>
    <div style="margin-top:14px">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px">
        <b>☁ 我的雲端班級</b>
        <button class="ghost" onclick="refreshTeacherCloudList(true)">重新整理</button>
      </div>
      <div id="teacherCloudList" class="classManagerList"><div class="menuClassHint">正在讀取雲端班級……</div></div>
    </div>''', 'teacher cloud list')
if 'onclick="copyTeacherUrl()"' not in s:
    ro('<button class="ghost" onclick="openClassManager()">🏫 選擇／管理班級</button>', '<button class="ghost" onclick="openClassManager()">🏫 選擇／管理班級</button>\n      <button class="ghost" onclick="copyTeacherUrl()">🔗 複製老師總網址</button>', 'copy teacher url')
old_menu='<button class="ghost" onclick="cloudReloadCurrent()">☁ 從雲端重新讀取</button>'
if old_menu in s:
    s=s.replace(old_menu,'<button class="ghost" onclick="refreshTeacherCloudList(true)">☁ 讀取雲端班級</button>',1)
if 'id="classManagerCloudList"' not in s:
    ro('<div id="classManagerList" class="classManagerList"></div>', '<h3>☁ 雲端班級</h3>\n  <div id="classManagerCloudList" class="classManagerList"><div class="menuClassHint">正在讀取雲端班級……</div></div>\n  <h3 style="margin-top:18px">💻 這台電腦的班級</h3>\n  <div id="classManagerList" class="classManagerList"></div>', 'cloud list in manager')

helpers='''const TEACHER_TOKEN_KEY="our14_teacher_token_v1";
function validTeacherToken(token){return /^[A-Za-z0-9_-]{32,160}$/.test(String(token||""));}
function teacherTokenFromUrl(input=location.href){
  try{return new URL(input,location.href).searchParams.get("teacher")||"";}catch(e){return "";}
}
function currentTeacherToken(){
  const fromUrl=teacherTokenFromUrl();
  if(validTeacherToken(fromUrl))return fromUrl;
  const local=localStorage.getItem(TEACHER_TOKEN_KEY)||"";
  return validTeacherToken(local)?local:"";
}
function teacherUrlFor(token){
  const u=new URL(location.href);
  u.searchParams.set("teacher",token);
  u.searchParams.delete("cloud");
  u.hash="";
  return u.toString();
}
async function ensureTeacherSpace(){
  let token=currentTeacherToken();
  if(!token){
    const data=await cloudRequest({action:"teacher_create"});
    token=data.teacher_token||"";
    if(!validTeacherToken(token))throw new Error("無法建立老師雲端空間");
  }
  localStorage.setItem(TEACHER_TOKEN_KEY,token);
  const u=new URL(location.href);
  if(u.searchParams.get("teacher")!==token){
    u.searchParams.set("teacher",token);
    history.replaceState(null,"",u.toString());
  }
  return token;
}
async function copyTeacherUrl(){
  try{
    const token=await ensureTeacherSpace();
    const url=teacherUrlFor(token);
    try{await navigator.clipboard.writeText(url);cloudToast("🔗 已複製老師總網址");}
    catch(e){prompt("請複製這個老師總網址：",url);}
  }catch(e){alert("無法取得老師總網址："+(e?.message||e));}
}
'''
if 'const TEACHER_TOKEN_KEY=' not in s:
    marker='async function ensureCloudLink(showToast=false){'
    if marker not in s: raise SystemExit('ensureCloudLink marker missing')
    s=s.replace(marker,helpers+marker,1)
if 'teacher_token:teacherToken,class_name:state.className' not in s:
    ro('  const data=await cloudRequest({action:"link_create",class_name:state.className,save_data:state});','  const teacherToken=await ensureTeacherSpace();\n  const data=await cloudRequest({action:"link_create",teacher_token:teacherToken,class_name:state.className,save_data:state});','link_create teacher token')
if 'action:"link_save",teacher_token:teacherToken' not in s:
    ro('    await cloudRequest({action:"link_save",save_token:token,class_name:state.className,save_data:state});','    const teacherToken=await ensureTeacherSpace();\n    await cloudRequest({action:"link_save",teacher_token:teacherToken,save_token:token,class_name:state.className,save_data:state});','link_save teacher token')

list_funcs='''let teacherCloudClasses=[];
function teacherClassTime(value){
  if(!value)return "";
  try{return new Date(value).toLocaleString("zh-TW",{hour12:false});}catch(e){return String(value);}
}
function teacherClassRow(c){
  const token=String(c.save_token||"");
  const name=escapeHtml(c.class_name||"未命名班級");
  const progress=c.finished?"第一章已告一段落":"第 "+(c.week||1)+" 週";
  const grade=c.grade?"｜階段評價 "+escapeHtml(c.grade):"";
  return `<div class="classSaveRow">
    <div>
      <div class="classSaveName">${name}</div>
      <div class="classSaveMeta">${progress}${grade}<br>雲端最後儲存：${teacherClassTime(c.updated_at)}</div>
    </div>
    <div class="classSaveBtns">
      <button class="primary" onclick="openTeacherClass('${token}')">開啟</button>
      <button class="ghost" onclick="deleteTeacherCloudClass('${token}')">刪除雲端</button>
    </div>
  </div>`;
}
function renderTeacherCloudClasses(classes){
  teacherCloudClasses=Array.isArray(classes)?classes:[];
  const html=teacherCloudClasses.length?teacherCloudClasses.map(teacherClassRow).join(""):'<div class="menuClassHint">雲端目前沒有正式班級。按「建立新班級」後會自動出現在這裡。</div>';
  const menu=document.getElementById("teacherCloudList");
  const manager=document.getElementById("classManagerCloudList");
  if(menu)menu.innerHTML=html;
  if(manager)manager.innerHTML=html;
}
async function refreshTeacherCloudList(showToast=false){
  try{
    const token=await ensureTeacherSpace();
    const data=await cloudRequest({action:"teacher_list",teacher_token:token});
    renderTeacherCloudClasses(data.classes||[]);
    if(showToast)cloudToast("☁ 雲端班級清單已更新");
    return data.classes||[];
  }catch(e){
    const msg='<div class="menuClassHint">雲端班級讀取失敗：'+escapeHtml(e?.message||String(e))+'</div>';
    const menu=document.getElementById("teacherCloudList");
    const manager=document.getElementById("classManagerCloudList");
    if(menu)menu.innerHTML=msg;
    if(manager)manager.innerHTML=msg;
    return [];
  }
}
async function openTeacherClass(token){
  try{await loadCloudToken(token,true);await refreshTeacherCloudList(false);}catch(e){alert("雲端班級讀取失敗："+(e?.message||e));}
}
async function deleteTeacherCloudClass(token){
  const info=teacherCloudClasses.find(c=>c.save_token===token);
  const name=info?.class_name||"這個班級";
  if(!confirm(`確定刪除「${name}」的雲端進度？\n\n刪除後無法復原。`))return;
  try{
    await cloudRequest({action:"link_delete",save_token:token});
    const keep=[];
    for(const meta of getClassIndex()){
      const raw=localStorage.getItem(classKey(meta.id));
      let same=false;
      try{same=!!raw&&JSON.parse(raw).cloudToken===token;}catch(e){}
      if(same)localStorage.removeItem(classKey(meta.id));else keep.push(meta);
    }
    setClassIndex(keep);
    if(state&&state.cloudToken===token){state=freshState();const u=new URL(location.href);u.hash="";history.replaceState(null,"",u.toString());switchScreen("menu");}
    refreshMenu();
    await refreshTeacherCloudList(false);
    cloudToast("已刪除雲端班級");
  }catch(e){alert("刪除失敗："+(e?.message||e));}
}
'''
if 'let teacherCloudClasses=[];' not in s:
    marker='function refreshMenu(){'
    if marker not in s: raise SystemExit('refreshMenu marker missing')
    s=s.replace(marker,list_funcs+marker,1)

old='''function openClassManager(){
  if(state.classId)saveLocal(false);
  renderClassManager();
  document.getElementById("classManagerOverlay").classList.add("show");
}'''
new='''function openClassManager(){
  if(state.classId)saveLocal(false);
  renderClassManager();
  refreshTeacherCloudList(false);
  document.getElementById("classManagerOverlay").classList.add("show");
}'''
if old in s: s=s.replace(old,new,1)
elif new not in s: raise SystemExit('openClassManager source not found')

old_ng='  try{await ensureCloudLink(true);await cloudSaveNow(true);}catch(e){console.warn("首次雲端建立失敗，之後會再自動嘗試",e);toast("目前先存本機；連線恢復後會再同步雲端");}'
new_ng='  try{await ensureCloudLink(true);await cloudSaveNow(true);await refreshTeacherCloudList(false);}catch(e){console.warn("首次雲端建立失敗，之後會再自動嘗試",e);toast("目前先存本機；連線恢復後會再同步雲端");}'
if old_ng in s: s=s.replace(old_ng,new_ng,1)
elif new_ng not in s: raise SystemExit('newGame cloud source not found')

old_init='''async function initOur14(){
  migrateLegacyV11();
  refreshMenu();
  const loaded=await loadFromHash();
  if(!loaded)switchScreen('menu');
}'''
new_init='''async function initOur14(){
  migrateLegacyV11();
  try{await ensureTeacherSpace();}catch(e){console.warn("老師雲端空間初始化失敗",e);}
  refreshMenu();
  await refreshTeacherCloudList(false);
  const loaded=await loadFromHash();
  if(!loaded)switchScreen('menu');
}'''
if old_init in s: s=s.replace(old_init,new_init,1)
elif new_init not in s: raise SystemExit('init source not found')

s=s.replace('v28.2 多班級雲端存檔版：','v28.3 老師總網址雲端版：',1)
s=s.replace('<b>同一個網址就是同一份雲端進度</b>：不需要老師密碼、不需要班級代碼，換任何電腦開同一網址即可繼續','<b>一個老師總網址即可管理全部班級</b>：不需要老師密碼、不需要班級代碼，換任何電腦開老師總網址即可讀取雲端班級',1)

p.write_text(s,encoding='utf-8')
