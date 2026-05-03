# LeetCode Contests

Track contest performance and practice problems from past rounds.

## Structure

```
contests/
├── weekly/        ← Weekly Contest problems (every Sunday)
├── biweekly/      ← Biweekly Contest problems (every other Saturday)
└── notes.md       ← Personal performance log
```

## How to Use

1. After each contest, create a folder: `weekly/contest_<number>/` or `biweekly/contest_<number>/`
2. Add `.py` stubs for each problem you want to revisit (follow repo templates)
3. Log your result in `notes.md`

## Contest Problem Naming

```
q1_<snake_case_title>.py
q2_<snake_case_title>.py
q3_<snake_case_title>.py
q4_<snake_case_title>.py
```

No LeetCode ID prefix needed — contest problems are identified by round + question number.

## Folder Example

```
weekly/
└── contest_400/
    ├── q1_find_the_k_th_character.py
    ├── q2_maximum_subarray_sum.py
    ├── q3_count_valid_sequences.py
    └── q4_minimum_cost_path.py
```
