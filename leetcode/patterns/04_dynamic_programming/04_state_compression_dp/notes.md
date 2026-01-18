# State Compression Dynamic Programming

## What This Subtopic Is About

State compression DP uses bitmasks to represent subsets, enabling efficient DP on small sets (typically ≤ 20 elements). This pattern compresses exponential states into manageable representations, solving NP-hard problems optimally for small inputs.

## Typical Patterns & Invariants

- **Bitmask representation**: Use integer bits to represent subset membership
- **State transitions**: Iterate through all subsets or toggle bits
- **DP table**: dp[mask] or dp[i][mask] where mask encodes state
- **Subset enumeration**: Efficiently iterate submasks of a mask
- **Exponential complexity**: O(2ⁿ × n) or O(2ⁿ × n²) typical

## How to Recognize This Type of Problem

- Small constraint (n ≤ 20) hinting at exponential solution
- Selecting subsets with dependencies
- Visiting cities, assigning tasks, covering sets
- State depends on which elements are "used" or "visited"
- NP-hard problems with small input size

## LeetCode Problems

- [691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/)
- [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
- [1178. Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)
