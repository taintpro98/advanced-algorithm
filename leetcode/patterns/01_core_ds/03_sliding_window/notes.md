# Sliding Window

## What This Subtopic Is About

Sliding window is an optimization technique that maintains a dynamic window over a sequence, expanding and contracting based on constraints. This pattern transforms nested loops into linear time complexity for subarray/substring problems with specific properties.

## Typical Patterns & Invariants

- **Fixed-size window**: Maintain exactly k elements and slide one position at a time
- **Variable-size window**: Expand right pointer to include elements, contract left when constraint violated
- **Window invariant**: Track property (sum, count, frequency) that must be maintained
- **Two-pointer window**: Left and right boundaries moving independently
- **Optimization target**: Maximize or minimize window size while satisfying constraints

## How to Recognize This Type of Problem

- Subarray or substring with constraints (sum, length, character count)
- "Longest" or "shortest" contiguous sequence problems
- "At most K" or "exactly K" distinct elements
- Finding all subarrays/substrings satisfying a condition
- Problems where brute force involves checking all subarrays

## LeetCode Problems

- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
