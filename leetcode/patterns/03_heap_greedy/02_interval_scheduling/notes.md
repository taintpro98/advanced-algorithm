# Interval Scheduling

## What This Subtopic Is About

Interval scheduling problems involve selecting or merging time intervals to optimize objectives like maximizing non-overlapping meetings or minimizing resources. This pattern combines greedy strategies with sorting and heap-based conflict resolution.

## Typical Patterns & Invariants

- **Sort by end time**: Greedy choice for maximum non-overlapping intervals
- **Sort by start time**: Merge overlapping intervals efficiently
- **Min heap for end times**: Track active intervals for resource allocation
- **Sweep line algorithm**: Process events (start/end) in chronological order
- **Greedy exchange argument**: Prove local optimal choice leads to global optimum

## How to Recognize This Type of Problem

- Meeting rooms or resource allocation problems
- Merging or detecting overlapping intervals
- Scheduling with constraints (non-overlapping, minimum gaps)
- Problems involving time ranges or continuous segments
- Optimization of interval selection

## LeetCode Problems

- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
