# Monotonic Stack

## What This Subtopic Is About

A monotonic stack maintains elements in either strictly increasing or decreasing order. This pattern efficiently solves "next greater/smaller element" problems and range queries where you need to find the nearest element satisfying a comparison condition.

## Typical Patterns & Invariants

- **Monotonic decreasing**: Keep larger elements at bottom, useful for "next greater element"
- **Monotonic increasing**: Keep smaller elements at bottom, useful for "next smaller element"
- **Stack invariant**: Pop elements that violate monotonicity before pushing
- **Index storage**: Often store indices instead of values for position tracking
- **Linear time complexity**: Each element pushed and popped at most once, O(n) total
- **Contribution Technique**: Calculate how many subarrays each element contributes to as min/max by finding left/right boundaries using monotonic stack

## How to Recognize This Type of Problem

- Finding "next greater" or "next smaller" element
- Maximum/minimum in subarrays with specific properties
- Histogram or bar-related problems
- Problems involving visibility or line of sight
- Range queries requiring nearest comparisons

## LeetCode Problems

- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
- [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)
