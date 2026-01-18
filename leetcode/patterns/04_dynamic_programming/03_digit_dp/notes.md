# Digit Dynamic Programming

## What This Subtopic Is About

Digit DP counts numbers in a range [L, R] satisfying specific digit-based constraints. This pattern builds numbers digit by digit while tracking whether the current number is still bounded by the range limits, enabling efficient counting without enumeration.

## Typical Patterns & Invariants

- **Position tracking**: Process digits from most significant to least
- **Tight bound flag**: Track if current prefix equals bound (determines available digits)
- **Constraint state**: Track properties like digit sum, previous digit, etc.
- **Memoization**: Cache states (position, tight, constraint_state)
- **Range query**: count(R) - count(L-1) for range [L, R]

## How to Recognize This Type of Problem

- Count numbers in range [L, R] with digit properties
- "How many numbers have property P in range..."
- Constraints on digit values, sums, or patterns
- No direct enumeration possible due to large range
- Properties checkable digit by digit

## LeetCode Problems

- [902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)
- [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)
- [600. Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/)
