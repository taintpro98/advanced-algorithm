# Combinatorics

## What This Subtopic Is About

Combinatorics solves counting problems using permutations, combinations, and combinatorial identities. This pattern combines factorial precomputation, Pascal's triangle, inclusion-exclusion principle, and generating functions.

## Typical Patterns & Invariants

- **Factorial precomputation**: Compute n! mod m for all n up to limit
- **Binomial coefficients**: C(n, k) = n! / (k! × (n-k)!)
- **Pascal's triangle**: C(n, k) = C(n-1, k-1) + C(n-1, k)
- **Inclusion-Exclusion**: Count by adding/subtracting overlapping sets
- **Stars and bars**: Distribute identical items into distinct bins

## How to Recognize This Type of Problem

- Counting arrangements, selections, or distributions
- "How many ways to..." questions
- Choosing k items from n items
- Partition problems with constraints
- Path counting on grids with obstacles

## LeetCode Problems

- [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)
- [1735. Count Ways to Make Array With Product](https://leetcode.com/problems/count-ways-to-make-array-with-product/)
