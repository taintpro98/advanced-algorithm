# Interval Dynamic Programming

## What This Subtopic Is About

Interval DP solves problems on contiguous ranges by breaking them into smaller subranges. This pattern typically uses a 2D table where dp[i][j] represents the optimal solution for the interval [i, j], building solutions from smaller intervals to larger ones.

## Typical Patterns & Invariants

- **2D DP table**: dp[i][j] = optimal value for range [i, j]
- **Interval length iteration**: Process intervals by increasing length
- **Split point enumeration**: Try all ways to split interval [i, j] at point k
- **Merge cost**: Combine solutions from [i, k] and [k+1, j]
- **Time complexity**: Typically O(n³) with three nested loops

## How to Recognize This Type of Problem

- Optimal way to break/merge a sequence
- Problems involving ranges or subarrays with dependencies
- "Burst", "remove", or "combine" elements optimally
- Matrix chain multiplication variants
- Palindrome-related optimization on substrings

## LeetCode Problems

- [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
- [1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
