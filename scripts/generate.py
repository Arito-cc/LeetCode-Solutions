import json, re
from pathlib import Path
GOAL=150; RECENT_LIMIT=10
LANG={'.java':'Java ☕','.py':'Python 🐍','.cpp':'C++ ⚡','.js':'JavaScript 🟨','.ts':'TypeScript 🔷'}
def pretty(s):
 m=re.match(r'^(\d+)-(.*)$',s);
 return (str(int(m.group(1))),m.group(2).replace('-',' ').title()) if m else (s,s)
def langs(info):
 a=[]

 for f in info:
  for e,l in LANG.items():
   if f.endswith(e): a.append(l)
 return ' · '.join(dict.fromkeys(a)) or 'Unknown'
data=json.load(open('stats.json',encoding='utf-8'))
lc=data.get('leetcode',{})
easy=lc.get('easy',0); medium=lc.get('medium',0); hard=lc.get('hard',0); total=lc.get('solved',0)
pct=int(total*100/GOAL) if GOAL else 0
bar='█'*min(20,pct//5)+'░'*(20-min(20,pct//5))
rows=[]
for slug,info in reversed(list(lc.get('shas',{}).items())):
 if slug in ('README.md','stats.json'): continue
 n,t=pretty(slug); d=info.get('difficulty','unknown').capitalize(); em={'Easy':'🟢','Medium':'🟡','Hard':'🔴'}.get(d,'⚪'); rows.append(f'| {n} | [{t}](./{slug}) | {em} {d} | {langs(info)} |')
rows='\n'.join(rows[:RECENT_LIMIT])
md=f'# 🚀 LeetCode Solutions\n\n## 📊 Progress\n\n| Total | Easy | Medium | Hard |\n|---:|---:|---:|---:|\n| **{total}** | 🟢 {easy} | 🟡 {medium} | 🔴 {hard} |\n\n```text\n{bar}\n{total}/{GOAL} ({pct}%)\n```\n\n## 🔥 Recent Submissions\n\n| # | Problem | Difficulty | Languages |\n|---|---|---|---|\n{rows}\n\n---\n\n> The topic index below is maintained automatically by LeetHub.\n\n'
p=Path('README.md')
if p.exists():
 cur=p.read_text(encoding='utf-8'); s='<!---LeetCode Topics Start-->'; e='<!---LeetCode Topics End-->';

 if s in cur and e in cur: md+=cur[cur.index(s):cur.index(e)+len(e)]+'\n'
p.write_text(md,encoding='utf-8')
