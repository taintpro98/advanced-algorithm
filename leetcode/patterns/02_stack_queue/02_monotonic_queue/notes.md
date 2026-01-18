# Monotonic Queue

## What This Subtopic Is About

A monotonic queue (typically implemented with a deque) maintains elements in monotonic order while supporting efficient front and back operations. This pattern is essential for sliding window problems where you need to track maximum or minimum values efficiently.

## Typical Patterns & Invariants

- **Deque structure**: Support removal from both ends
- **Monotonic property**: Maintain increasing or decreasing order
- **Window sliding**: Remove elements outside current window from front
- **Optimal element tracking**: Always keep the best element accessible at front
- **Amortized O(1)**: Each element enqueued and dequeued at most once

## How to Recognize This Type of Problem

- Sliding window with max/min queries
- "Maximum/minimum in every subarray of size k"
- Dynamic range queries with moving boundaries
- Problems combining window sliding with ordering requirements
- Optimization of window-based comparisons

## LeetCode Problems

- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
