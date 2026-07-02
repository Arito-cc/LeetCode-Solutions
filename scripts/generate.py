import json
from pathlib import Path

GOAL = 150

with open("stats.json", "r") as f:
    data = json.load(f)

leetcode = data["leetcode"]

easy = leetcode["easy"]
medium = leetcode["medium"]
hard = leetcode["hard"]
total = data["solved"]

percentage = int((total / GOAL) * 100)

filled = int(percentage / 5)
progress_bar = "█" * filled + "░" * (20 - filled)

recent = []

for problem, info in reversed(list(leetcode["shas"].items())):
    if problem in ["README.md", "stats.json"]:
        continue

    difficulty = info.get("difficulty", "unknown").capitalize()

    lang = "Unknown"
    for file in info:
        if file.endswith(".java"):
            lang = "Java ☕"
        elif file.endswith(".py"):
            lang = "Python 🐍"

    recent.append((problem, difficulty, lang))

recent = recent[:5]

recent_rows = "\n".join(
    f"| `{name}` | {difficulty} | {lang} |"
    for name, difficulty, lang in recent
)

content = f"""# 🚀 LeetCode Solutions

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-Arito--cc-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/Arito-cc/)
[![GitHub](https://img.shields.io/badge/GitHub-Arito--cc-181717?style=for-the-badge&logo=github)](https://github.com/Arito-cc)

</div>

---

# 📈 Progress

| Difficulty | Solved |
|------------|---------|
| 🟢 Easy | {easy} |
| 🟡 Medium | {medium} |
| 🔴 Hard | {hard} |
| **Total** | **{total}** |

## 🎯 Goal: {GOAL} Problems

```text
{progress_bar}
{total}/{GOAL} ({percentage}%)
