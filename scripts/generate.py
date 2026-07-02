import json
import re
from pathlib import Path

GOAL = 150
RECENT_LIMIT = 10
MILESTONES = [25,50,75,100,150]
LANG_MAP={'.java':'Java ☕','.py':'Python 🐍','.cpp':'C++ ⚡','.js':'JavaScript 🟨','.ts':'TypeScript 🔷'}

def pretty_problem(slug):
    m=re.match(r'^(\d+)-(.*)$',slug)
    if not m:
        return slug, slug.replace('-', ' ').title()
    return str(int(m.group(1))), m.group(2).replace('-', ' ').title()

def languages(info):
    out=[]
    for n in info:
        for ext,label in LANG_MAP.items():
            if n.endswith(ext):
                out.append(label)
    return ' · '.join(dict.fromkeys(out)) or 'Unknown'

with open('stats.json',encoding='utf-8') as f:
    data=json.load(f)

lc=data.get('leetcode',{})
easy=lc.get('easy',0)
medium=lc.get('medium',0)
hard=lc.get('hard',0)
total=lc.get('solved',0)
pct=int(total*100/GOAL) if GOAL else 0
filled=min(20,pct//5)
bar='█'*filled+'░'*(20-filled)

rows=[]
for slug,info in reversed(list(lc.get('shas',{}).items())):
    if slug in ('README.md','stats.json'):
        continue
    num,title=pretty_problem(slug)
    diff=info.get('difficulty','Unknown').capitalize()
    em={'Easy':'🟢','Medium':'🟡','Hard':'🔴'}.get(diff,'⚪')
    rows.append(f'| {num} | [{title}](./{slug}) | {em} {diff} | {languages(info)} |')
rows='\n'.join(rows[:RECENT_LIMIT])

milestones='\n'.join([f"- [{'x' if total>=m else ' '}] {m} Problems{' ⭐' if m==GOAL else ''}" for m in MILESTONES])

readme=f"""# 🚀 LeetCode Solutions

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&center=true&vCenter=true&width=700&lines=Java+%7C+Python+%7C+DSA;150%2B+Problems+Goal;Learning+One+Problem+At+A+Time" />

[![LeetCode](https://img.shields.io/badge/LeetCode-Arito--cc-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/Arito-cc/)
[![GitHub](https://img.shields.io/badge/GitHub-Arito--cc-181717?style=for-the-badge&logo=github)](https://github.com/Arito-cc)
![Solved](https://img.shields.io/badge/Solved-{total}-success?style=for-the-badge)

</div>

## 📊 Statistics

| Total | Easy | Medium | Hard |
|---:|---:|---:|---:|
| **{total}** | 🟢 {easy} | 🟡 {medium} | 🔴 {hard} |

## 🎯 Goal Progress

```text
{bar}
{total}/{GOAL} ({pct}%)
```

## 🏆 Milestones

{milestones}

## ⚡ Languages

![Java](https://img.shields.io/badge/Java-Primary-orange?logo=openjdk)
![Python](https://img.shields.io/badge/Python-Learning-blue?logo=python)

## 🔥 Recent Submissions

| # | Problem | Difficulty | Languages |
|---|---|---|---|
{rows}

---

> The topic section below is automatically maintained by LeetHub.

"""

p=Path('README.md')
if p.exists():
    cur=p.read_text(encoding='utf-8')
    s='<!---LeetCode Topics Start-->'
    e='<!---LeetCode Topics End-->'
    if s in cur and e in cur:
        readme += cur[cur.index(s):cur.index(e)+len(e)] + '\n'

p.write_text(readme,encoding='utf-8')
