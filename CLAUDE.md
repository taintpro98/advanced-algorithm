# CLAUDE.md — Rules for This Repository

## Rules Summary

| # | Rule |
|---|------|
| 1 | **No git without permission** — never run `git add/commit/push` without explicit user approval |
| 2 | **No solutions** — `.py` files contain only docstring + API signatures with `pass` |
| 3 | **Tab indentation** — use `\t` (tab width = 4 spaces), never spaces |
| 4 | **File naming** — `lc_<0-padded-id>_<snake_case>.py` or `cf_<id>_<title>.py` |
| 5 | **Template A** — single-function problems: `class Solution` with one method |
| 6 | **Template B** — design problems: class with `__init__` + multiple methods |
| 7 | **Template C** — stub only (docstring, no scaffold), used in `patterns/` |
| 8 | **notes.md structure** — What / Patterns & Invariants / How to Recognize / Problem links |

## Git

- **Never commit or push without explicit permission from the user.**
- Always show what you plan to stage and ask before running any `git add`, `git commit`, or `git push`.

## Python Style

- **Indentation: tab characters (`\t`), displayed as 4 spaces wide.** Never use spaces for indentation in `.py` files.
- This is enforced by `.editorconfig` at the repo root.

## Code Files — No Solutions

- **Never write solution logic.** The user implements all solutions themselves.
- When creating a `.py` file, provide only:
  1. The problem docstring (metadata)
  2. The API scaffold (class/function signatures with `pass`)
- Do not add hints, comments explaining approach, or partial logic inside method bodies.

## How to Create a Code File

Read existing files and follow these templates exactly.

### Template A — Single function (most common)

```python
"""
LeetCode <ID> - <Title>
https://leetcode.com/problems/<slug>/

Pattern:
<Pattern Name>
"""
from typing import List, Optional  # only import what the signature needs


class Solution:
    def methodName(self, param: type) -> return_type:
        pass
```

### Template B — Design problem (multiple methods)

```python
"""
LeetCode <ID> - <Title>
https://leetcode.com/problems/<slug>/

Pattern:
<Pattern Name>
"""

class DesignClass:

    def __init__(self, param: type) -> None:
        pass

    def method1(self, param: type) -> return_type:
        pass

    def method2(self, param: type) -> return_type:
        pass
```

### Template C — Stub only (no API needed yet)

Used in `patterns/` when only tracking the problem, not scaffolding it yet:

```python
"""
LeetCode <ID> - <Title>
https://leetcode.com/problems/<slug>/

Pattern:
<Pattern Name>
"""
```

## File Naming Convention

Prefix depends on the platform:

| Platform | Prefix | Example |
|---|---|---|
| LeetCode | `lc_` | `lc_0146_lru_cache.py` |
| Codeforces | `cf_` | `cf_1234A_two_rounds.py` |

Always zero-pad the ID to at least 4 digits for LeetCode. Codeforces IDs use the contest+letter format as-is (e.g. `1234A`).

The docstring URL line changes per platform:
- LeetCode: `https://leetcode.com/problems/<slug>/`
- Codeforces: `https://codeforces.com/problemset/problem/<contest>/<letter>`

Everything else (templates A / B / C, `pass` bodies, no solutions) stays the same regardless of platform.

## Notes Files (`notes.md`)

Follow the existing structure:
- **What This Subtopic Is About**
- **Typical Patterns & Invariants**
- **How to Recognize This Type of Problem**
- **LeetCode Problems** (links only, no solutions)
