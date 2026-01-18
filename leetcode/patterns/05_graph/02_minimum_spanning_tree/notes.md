# Minimum Spanning Tree

## What This Subtopic Is About

Minimum Spanning Tree (MST) algorithms find the subset of edges connecting all vertices with minimum total weight. This pattern uses Kruskal's (sort + union-find) or Prim's (greedy + priority queue) algorithms for network design and clustering problems.

## Typical Patterns & Invariants

- **Kruskal's algorithm**: Sort edges, use union-find to avoid cycles
- **Prim's algorithm**: Grow MST from arbitrary vertex using min heap
- **Cut property**: Minimum-weight edge crossing cut is in MST
- **Cycle property**: Maximum-weight edge in cycle is not in MST
- **Union-Find**: Efficiently detect cycles and merge components

## How to Recognize This Type of Problem

- Connecting all nodes with minimum cost
- Network design problems (roads, cables, pipes)
- "Connect all" or "minimum cost to connect"
- Problems reducible to finding spanning tree
- Clustering or grouping with distance constraints

## LeetCode Problems

- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- [1168. Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)
- [1489. Find Critical and Pseudo-Critical Edges in MST](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
