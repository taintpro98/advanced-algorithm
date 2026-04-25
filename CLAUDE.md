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
| 9 | **Contest files** — named `q1_<title>.py`, folder per round under `contests/weekly/` or `contests/biweekly/` |
| 10 | **Probability section** — notes-only markdown, no `.py` files |
| 11 | **worldquant cross-reference** — if a problem exists in `patterns/`, add `See: <path>` in the worldquant stub docstring; solve only in `patterns/` |
| 12 | **Test cases** — always add example test cases from the problem at the bottom of every `.py` template |
| 13 | **No unsolicited hints** — during discussion, never suggest solution approaches, insights, or next steps unless explicitly asked |

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


sol = Solution()

# Example 1: Output <expected>
print(sol.methodName(<input>))

# Example 2: Output <expected>
print(sol.methodName(<input>))
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


# Example 1
obj = DesignClass(<init_args>)
obj.method1(<args>)
print(obj.method2(<args>))  # expected output
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

## WorldQuant Cross-References

When a worldquant stub has a counterpart in `patterns/`, add a `See:` line inside the docstring after the Pattern value:

```python
"""
LeetCode 295 - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Pattern:
Two Heaps (Max Heap + Min Heap)

See: leetcode/patterns/03_heap_greedy/01_k_elements/lc_0295_find_median_from_data_stream.py
"""
```

- Solve only in the `patterns/` file — never duplicate the implementation
- The worldquant stub stays as-is (just `pass`) and serves as a checklist pointer
- If no counterpart exists in `patterns/`, leave the worldquant stub without a `See:` line

## Contest Files (`leetcode/practice/contests/`)

Name by question position, not LeetCode ID (ID may not exist yet during contest):

```
q1_<snake_case_title>.py
q2_<snake_case_title>.py
```

Folder per round: `weekly/contest_<number>/` or `biweekly/contest_<number>/`.
Same templates (A / B / C) and tab indentation apply.

## Probability Section (`probability/`)

Notes-only — no `.py` stubs. Each subtopic has a `notes.md` with theory, formulas, and problems in markdown.
Do not create `.py` files here.

## Notes Files (`notes.md`)

Follow the existing structure:
- **What This Subtopic Is About**
- **Typical Patterns & Invariants**
- **How to Recognize This Type of Problem**
- **LeetCode Problems** (links only, no solutions)
