# Knapsack Variants

## What This Subtopic Is About

Knapsack problems involve selecting items with weights and values to optimize an objective under capacity constraints. This pattern extends from basic 0/1 knapsack to unbounded, multi-dimensional, and constraint satisfaction variants.

## Typical Patterns & Invariants

- **0/1 Knapsack**: Each item used at most once, dp[i][w] with i items and capacity w
- **Unbounded Knapsack**: Items can be used unlimited times
- **Multi-dimensional**: Multiple constraints (weight, volume, etc.)
- **Exact sum**: Find if subset sums to exact target
- **Optimization target**: Maximize value or minimize cost

## How to Recognize This Type of Problem

- Selecting items with constraints on total weight/capacity
- Subset sum or partition problems
- "Achieve exactly" or "maximize under constraint"
- Resource allocation with item choices
- Problems reducible to selecting from a set with limits

## LeetCode Problems

- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [494. Target Sum](https://leetcode.com/problems/target-sum/)
