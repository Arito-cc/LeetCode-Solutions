import json
from pathlib import Path

GOAL = 150
RECENT_LIMIT = 10

def get_languages(info):
    langs=[]
    mp={'.java':'Java ☕','.py':'Python 🐍','.cpp':'C++ ⚡','.js':'JavaScript 🟨','.ts':'TypeScript 🔷'}
    for f in info:
        for ext,label in mp.items():
            if f.endswith(ext): langs.append(label)
    return ' · '.join(dict.fromkeys(langs)) if langs else 'Unknown'

with open('stats.json',encoding='utf-8') as f:
    data=json.load(f)
lc=data.get('leetcode',{})
easy=lc.get('easy',0)
medium=lc.get('medium',0)
hard=lc.get('hard',0)
total=lc.get('solved',0)
pct=int(total*100/GOAL) if GOAL else 0
bar='█'*min(20,pct//5)+'░'*(20-min(20,pct//5))
recent=[]
for p,info in reversed(list(lc.get('shas',{}).items())):
    if p in ('README.md','stats.json'): continue
    recent.append((p,info.get('difficulty','unknown').capitalize(),get_languages(info)))
recent=recent[:RECENT_LIMIT]
rows='\n'.join(f'| `{p}` | {d} | {l} |' for p,d,l in recent)
content=f'''# 🚀 LeetCode Solutions

## 📈 Progress

| Difficulty | Solved |
|------------|---------|
| 🟢 Easy | {easy} |
| 🟡 Medium | {medium} |
| 🔴 Hard | {hard} |
| **Total** | **{total}** |

```text
{bar}
{total}/{GOAL} ({pct}%)
```

## 🔥 Recent Submissions

| Problem | Difficulty | Language |
|----------|------------|-----------|
{rows}

---

'''
rp=Path('README.md')
if rp.exists():
    cur=rp.read_text(encoding='utf-8')
    s='<!---LeetCode Topics Start-->'
    e='<!---LeetCode Topics End-->'
    if s in cur and e in cur:
        content+=cur[cur.index(s):cur.index(e)+len(e)]+'\n'
rp.write_text(content,encoding='utf-8')
