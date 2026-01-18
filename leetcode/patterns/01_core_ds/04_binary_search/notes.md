# Binary Search

## What This Subtopic Is About

Binary search is a divide-and-conquer algorithm that efficiently searches sorted spaces by eliminating half of the search range in each step. Beyond simple array searching, this pattern extends to "binary search on answer" where you search for optimal values in monotonic solution spaces.

## Typical Patterns & Invariants

- **Classic search**: Find target in sorted array with O(log n) complexity
- **First/last occurrence**: Find boundaries of target range using lower_bound/upper_bound
- **Binary search on answer**: Search for minimum/maximum value satisfying a condition
- **Monotonic predicate**: Condition that changes from false to true (or vice versa) exactly once
- **Search space transformation**: Convert problem into "can we achieve X?" then binary search X

## How to Recognize This Type of Problem

- Sorted array or monotonic function
- "Find minimum/maximum value such that..."
- Optimization problems with verifiable conditions
- "Allocate" or "distribute" resources with constraints
- Time/space complexity hints at logarithmic solution

## LeetCode Problems

- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
