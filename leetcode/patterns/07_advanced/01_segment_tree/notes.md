# Segment Tree

## What This Subtopic Is About

Segment trees enable efficient range queries and updates on arrays. This pattern supports operations like range sum, min/max, GCD in O(log n) time, with applications to dynamic programming optimization and computational geometry.

## Typical Patterns & Invariants

- **Tree structure**: Binary tree where each node represents an interval
- **Lazy propagation**: Defer updates to children until needed
- **Range query**: Aggregate information over [L, R] in O(log n)
- **Point/range update**: Modify single element or range efficiently
- **Persistent segment tree**: Maintain multiple versions for time-travel queries

## How to Recognize This Type of Problem

- Range queries (sum, min, max, GCD) with updates
- "Answer Q queries on an array" with modifications
- Dynamic programming optimization (convex hull trick on segment tree)
- Offline query processing with coordinate compression
- 2D range queries (2D segment tree)

## LeetCode Problems

- [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)
- [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
- [699. Falling Squares](https://leetcode.com/problems/falling-squares/)
