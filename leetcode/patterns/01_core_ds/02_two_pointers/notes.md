# Two Pointers

## What This Subtopic Is About

Two pointers is a technique that uses two indices to traverse a data structure, often moving in opposite directions or at different speeds. This pattern reduces time complexity from O(n²) to O(n) for problems involving pairs, subsequences, or partitioning.

## Typical Patterns & Invariants

- **Opposite direction**: Left and right pointers moving towards each other
- **Same direction (slow/fast)**: Floyd's cycle detection, finding duplicates
- **Partition invariant**: Maintaining a property across a division point
- **Sorted array optimization**: Leveraging sorted order to eliminate redundant comparisons
- **In-place modification**: Swapping or rearranging without extra space

## How to Recognize This Type of Problem

- Problems on sorted arrays asking for pairs with specific properties
- "Remove duplicates" or "move elements" in-place
- Palindrome checking or string manipulation
- Finding cycles in linked lists
- Merging or comparing two sequences

## LeetCode Problems

- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [15. 3Sum](https://leetcode.com/problems/3sum/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
