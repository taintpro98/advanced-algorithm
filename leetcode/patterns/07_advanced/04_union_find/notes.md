# Union-Find (Disjoint Set Union)

## What This Subtopic Is About

Union-Find efficiently manages disjoint sets with near-constant time union and find operations. This pattern uses path compression and union by rank/size for connectivity queries, MST algorithms, and dynamic connectivity.

## Typical Patterns & Invariants

- **Path compression**: Flatten tree during find operations
- **Union by rank/size**: Attach smaller tree under larger one
- **Amortized O(α(n))**: Inverse Ackermann function, nearly O(1)
- **Connected components**: Track number of disjoint sets
- **Weighted union-find**: Track distances or relationships

## How to Recognize This Type of Problem

- Checking if elements are in same connected component
- Dynamically merging sets or groups
- Detecting cycles in undirected graphs
- Network connectivity problems
- Kruskal's MST algorithm foundation

## LeetCode Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)
