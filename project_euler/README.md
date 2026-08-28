# Project Euler

Selected problems from [projecteuler.net](https://projecteuler.net/archives) — only the ones
worth writing code for. Many Euler problems are pure pen-and-paper math and get no file here.

Same philosophy as the rest of this repository: files hold the problem metadata and an API
scaffold — **no solutions**.

## Structure

Flat — one file per problem, directly in this folder. No ID buckets, no subfolders.

```
project_euler/
├── README.md
└── pe_0007_10001st_prime.py
```

## File Naming

`pe_<0-padded-id>_<snake_case_title>.py` — ID zero-padded to at least 4 digits, so the
flat listing sorts by problem number.

```
pe_0007_10001st_prime.py
pe_0014_longest_collatz_sequence.py
pe_0231_prime_factorisation_of_binomial_coefficients.py
```

## Template

The problem number and link go in the docstring. Euler problems state a small worked example
and then the real target value — parameterize the function so both can be run.

```python
"""
Project Euler <ID> - <Title>
https://projecteuler.net/problem=<ID>

Pattern:
<Topic / technique tags>
"""


def <function_name>(<param>: type) -> return_type:
	pass


# Example: <small case from the statement> -> <expected>
print(<function_name>(<small_input>))

# Answer
print(<function_name>(<real_input>))
```

Tab indentation (`\t`, width 4), as enforced by `.editorconfig` at the repo root.

## Topic Overlap

Many Euler problems reuse patterns already covered under
`leetcode/patterns/06_number_theory/` (sieves, modular arithmetic, combinatorics) and
`leetcode/patterns/04_dynamic_programming/`. Cross-reference with a `See:` line in the
docstring when a pattern folder already covers the technique.
