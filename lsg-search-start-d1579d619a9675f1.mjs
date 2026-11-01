let o=window.logseqGardenerInitSearch?.options||{},p=0,h=0,w,c,a=0,q='';
const d=document,s='[data-lsg-search]',B=()=>d.querySelectorAll(s),L=()=>d.head.querySelector('[rel=lsg-search]'),id=()=>L()?.href+':'+L()?.dataset.revision,E=['click','pointerover','focusin'];
function i(r,u={}){o={...o,...u};const v=id();if(v!==c){h=0;q='';}c=v;for(const b of B())b.hidden=!L()||location.protocol==='file:'||!window.HTMLDialogElement?.prototype.showModal;}
window.logseqGardenerInitSearch=i;i();
const t=d.createElement('span');t.id='lsg-search-load';t.role='status';
async function f(v){
const k=v.type==='keydown',e=!k&&v.type>'d',x=v.target.closest?.(s);
if(k&&p&&h){v.stopPropagation();if(v.isComposing||v.keyCode===229)return;if(v.key==='Escape'){v.preventDefault();h=0;q='';t.textContent='';return;}if(!v.ctrlKey&&!v.metaKey&&!v.altKey){if(v.key.length===1&&q.length<512)q+=v.key;else if(v.key==='Backspace')q=[...q].slice(0,-1).join('');v.preventDefault();return;}}
if(k&&(!(v.ctrlKey||v.metaKey)||v.key.toLowerCase()!=='k'||v.altKey||v.shiftKey||v.isComposing))return;
if(!k&&!x)return;
if(![...B()].some(b=>!b.hidden))return;
if(!e){v.preventDefault();h=1;w=id();t.textContent='Loading search…';}if(p)return;p=1;
d.body.append(t);
try{
const m=await import(new URL('lsg-search-ui-20d86616f46416af.mjs',import.meta.url)+(a++?'?retry='+a:''));
delete window.logseqGardenerInitSearch;m.installSearch(window,d);
for(const n of E)d.removeEventListener(n,f);d.removeEventListener('keydown',f,true);
window.logseqGardenerInitSearch(d,o);
if(h&&w===id()){d.dispatchEvent(new KeyboardEvent('keydown',{key:'k',ctrlKey:true,bubbles:true}));const z=d.getElementById('lsg-search-input');if(z){z.value=q;z.dispatchEvent(new Event('input',{bubbles:true}));}}
t.remove();
}catch{window.logseqGardenerInitSearch=i;t.textContent=h&&w===id()?'Search could not load. Retry Search or reload.':'';}
p=0;
}
for(const n of E)d.addEventListener(n,f);d.addEventListener('keydown',f,true);