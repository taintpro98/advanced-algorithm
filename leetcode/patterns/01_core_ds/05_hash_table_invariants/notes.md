# Hash Table Invariants

## What This Subtopic Is About

Hash tables enable O(1) lookup, insertion, and deletion, making them essential for maintaining invariants and tracking state. This pattern focuses on using hash structures to preserve relationships, detect patterns, or optimize lookups in algorithms that would otherwise require nested iterations.

## Typical Patterns & Invariants

- **Complement search**: Store seen elements to find pairs summing to target
- **Frequency counting**: Track element occurrences for duplicate/unique patterns
- **Index mapping**: Map values to indices for quick access
- **State caching**: Memoize computed states to avoid recomputation
- **Set operations**: Quick membership testing and uniqueness guarantees

## How to Recognize This Type of Problem

- Finding pairs, triplets with specific sum/difference
- Detecting duplicates within constraints (k distance, time window)
- Mapping between different representations
- Optimization of lookup-heavy algorithms
- Problems mentioning "seen before" or "already encountered"

## LeetCode Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
