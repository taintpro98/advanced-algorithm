# Parentheses Matching

## What This Subtopic Is About

Parentheses matching problems use stacks to track opening brackets and validate proper nesting. This pattern extends beyond simple validation to problems involving optimal bracket removal, generation of valid combinations, and score computation.

## Typical Patterns & Invariants

- **Stack invariant**: Opening brackets pushed, matching closing brackets pop
- **Balance tracking**: Count net opening vs closing brackets
- **Greedy removal**: Remove invalid brackets while preserving maximum valid substring
- **Backtracking generation**: Generate all valid combinations systematically
- **Nested score computation**: Calculate scores based on nesting depth

## How to Recognize This Type of Problem

- Validating bracket sequences
- Removing minimum brackets to make valid
- Generating all valid parentheses combinations
- Computing scores based on bracket structure
- Longest valid parentheses substring

## LeetCode Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
