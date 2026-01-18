# Prefix Sum

## What This Subtopic Is About

Prefix sum is a fundamental preprocessing technique that transforms an array into cumulative sums, enabling constant-time range sum queries. This pattern is essential for optimizing problems that involve repeated queries over subarrays or detecting patterns based on cumulative properties.

## Typical Patterns & Invariants

- **Cumulative transformation**: Transform `arr[i]` into `prefix[i] = arr[0] + arr[1] + ... + arr[i]`
- **Range sum formula**: `sum(l, r) = prefix[r] - prefix[l-1]`
- **Hash map tracking**: Store prefix sums in a hash map to detect target differences or patterns
- **Modular arithmetic**: Use modulo operations with prefix sums for divisibility problems
- **2D prefix sum**: Extend to matrices for rectangle sum queries

## How to Recognize This Type of Problem

- Problems asking for subarray sums equal to a target
- Queries about range sums or cumulative properties
- Finding subarrays with specific sum properties
- Problems involving "continuous" or "contiguous" elements
- Optimization of repeated range queries from O(n) to O(1)

## LeetCode Problems

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
