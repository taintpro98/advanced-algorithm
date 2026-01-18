I have an existing repository with this structure inside `leetcode/`:

01_core_ds
02_stack_queue
03_heap_greedy
04_dynamic_programming
05_graph
06_number_theory
07_advanced
(plus some markdown files like README.md and binary_search_templates_with_examples.md)

I want to refactor the repo to separate:
- `patterns/` (systematic learning by topic)
- `practice/` (playlists like Top Interview 150, free style, etc.)

IMPORTANT CONSTRAINTS:
1) I want to KEEP all existing code files exactly as they are.
   - Do NOT delete any `.py` files.
   - Do NOT rewrite any `.py` content.
   - Do NOT rename any existing `.py` files.
   - Do NOT change notes content besides moving files.
2) I want the existing topic folders (the original 7 folders) to remain the “source of truth” for the code I already wrote.
   - After refactor, those existing files must still exist under `leetcode/patterns/...`
3) I do NOT want duplicated copies of those already-coded files unless absolutely necessary.
4) Do NOT regenerate the repository or add solutions.

TARGET STRUCTURE:

leetcode/
├── patterns/
│   ├── 01_core_ds/
│   ├── 02_stack_queue/
│   ├── 03_heap_greedy/
│   ├── 04_dynamic_programming/
│   ├── 05_graph/
│   ├── 06_number_theory/
│   └── 07_advanced/
│
├── practice/
│   ├── top_interview_150/
│   │   ├── README.md
│   │   └── notes.md
│   ├── leetcode_75/
│   │   ├── README.md
│   │   └── notes.md
│   ├── company_tags/
│   │   ├── README.md
│   │   └── notes.md
│   └── free_style/
│       ├── README.md
│       └── notes.md
│
├── cheatsheets/
│   ├── binary_search_templates_with_examples.md
│   └── (other cheat sheets can go here later)
│
└── README.md

TASKS:
A) Create the new folders: `leetcode/patterns`, `leetcode/practice`, `leetcode/cheatsheets`.
B) Move the existing 7 topic folders under `leetcode/patterns/` without modifying file contents:
   - leetcode/01_core_ds          -> leetcode/patterns/01_core_ds
   - leetcode/02_stack_queue      -> leetcode/patterns/02_stack_queue
   - leetcode/03_heap_greedy      -> leetcode/patterns/03_heap_greedy
   - leetcode/04_dynamic_programming -> leetcode/patterns/04_dynamic_programming
   - leetcode/05_graph            -> leetcode/patterns/05_graph
   - leetcode/06_number_theory    -> leetcode/patterns/06_number_theory
   - leetcode/07_advanced         -> leetcode/patterns/07_advanced

C) Move existing cheat sheet markdown files into `leetcode/cheatsheets/`:
   - binary_search_templates_with_examples.md -> leetcode/cheatsheets/
   - PROMPT_FOR_CLAUDE.md -> leetcode/cheatsheets/ (or keep at root if you think it’s better; choose one and be consistent)
   Do NOT change their content.

D) Create the practice folders listed above with minimal README.md + notes.md files.
   - README.md: describe purpose in 5-8 lines (no solutions)
   - notes.md: empty template with a few bullet placeholders (no solutions)

E) Update the root `leetcode/README.md` (create if missing) to explain:
   - what `patterns/` is for
   - what `practice/` is for
   - what `cheatsheets/` is for
   Keep it concise.

OUTPUT FORMAT:
- Print the final folder tree.
- Provide the full content for any NEW files you create (README.md and notes.md only).
- Do NOT output the contents of existing moved files.
- Do NOT include any solution code.

Do not propose alternatives. Follow tasks A–E exactly.