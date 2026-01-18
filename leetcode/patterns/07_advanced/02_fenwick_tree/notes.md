# Fenwick Tree (Binary Indexed Tree)

## What This Subtopic Is About

Fenwick Tree (BIT) provides efficient prefix sum queries and point updates in O(log n) using bit manipulation. This pattern is simpler than segment trees for specific use cases and excels at inversion counting and order statistics.

## Typical Patterns & Invariants

- **Bit manipulation**: Use x & -x to isolate lowest set bit
- **Prefix sum query**: Sum from index 1 to k in O(log n)
- **Point update**: Increment/modify single element in O(log n)
- **Range update**: Combine two BITs for range modifications
- **2D BIT**: Handle 2D prefix sums and updates

## How to Recognize This Type of Problem

- Prefix sum queries with point updates
- Counting inversions in arrays
- Order statistics (rank queries)
- Problems requiring cumulative frequency
- Simpler alternative to segment tree when applicable

## LeetCode Problems

- [308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/)
- [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
