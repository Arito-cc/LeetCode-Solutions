import json
from pathlib import Path

GOAL = 150

with open("stats.json", "r", encoding="utf-8") as f:
    data = json.load(f)

leetcode = data.get("leetcode", {})

easy = leetcode.get("easy", 0)
medium = leetcode.get("medium", 0)
hard = leetcode.get("hard", 0)
total = leetcode.get("solved", 0)

percentage = int((total / GOAL) * 100) if GOAL else 0
filled = min(20, percentage // 5)
progress_bar = "█" * filled + "░" * (20 - filled)

recent = []
for problem, info in reversed(list(leetcode["shas"].items())):
    if problem in ["README.md", "stats.json"]:
        continue

    difficulty = info.get("difficulty", "unknown").capitalize()
    languages = []

for file_name in info:
    if file_name.endswith(".java"):
        languages.append("Java ☕")

    elif file_name.endswith(".py"):
        languages.append("Python 🐍")

    elif file_name.endswith(".cpp"):
        languages.append("C++ ⚡")

    elif file_name.endswith(".js"):
        languages.append("JavaScript 🟨")

    elif file_name.endswith(".ts"):
        languages.append("TypeScript 🔷")

# Remove duplicates while preserving order
languages = list(dict.fromkeys(languages))

lang = " · ".join(languages) if languages else "Unknown"

    recent.append((problem, difficulty, lang))

recent = recent[:5]
recent_rows = "\n".join(
    f"| `{name}` | {difficulty} | {lang} |"
    for name, difficulty, lang in recent
)

content = f"""# 🚀 LeetCode Solutions

<div align=\"center\"> 

[![LeetCode](https://img.shields.io/badge/LeetCode-Arito--cc-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/Arito-cc/)
[![GitHub](https://img.shields.io/badge/GitHub-Arito--cc-181717?style=for-the-badge&logo=github)](https://github.com/Arito-cc)
![Problems Solved](https://img.shields.io/badge/Problems-{total}-success?style=for-the-badge)

</div>

---

## 📈 Progress

| Difficulty | Solved |
|------------|---------|
| 🟢 Easy | {easy} |
| 🟡 Medium | {medium} |
| 🔴 Hard | {hard} |
| **Total** | **{total}** |

### 🎯 Goal: {GOAL} Problems

```text
{progress_bar}
{total}/{GOAL} ({percentage}%)
```

---

## ☕ Languages

- Java (Primary DSA Language)
- Python (Early Practice & Learning)

---

## 🔥 Recently Solved

| Problem | Difficulty | Language |
|----------|------------|-----------|
{recent_rows}

---

"""

readme_path = Path("README.md")
if readme_path.exists():
    current = readme_path.read_text(encoding="utf-8")
    start = "<!---LeetCode Topics Start-->"
    end = "<!---LeetCode Topics End-->"

    if start in current and end in current:
        section = current[current.index(start): current.index(end) + len(end)]
        content += section + "\n"

readme_path.write_text(content, encoding="utf-8")
