# Network Flow

## What This Subtopic Is About

Network flow algorithms find maximum flow through a capacity-constrained network from source to sink. This pattern includes Ford-Fulkerson, Edmonds-Karp, and Dinic's algorithms, with applications to matching, assignment, and resource allocation.

## Typical Patterns & Invariants

- **Max-flow min-cut theorem**: Maximum flow equals minimum cut capacity
- **Augmenting paths**: Repeatedly find paths with available capacity
- **Residual graph**: Track remaining capacity and backward edges
- **Ford-Fulkerson**: DFS-based augmenting paths
- **Edmonds-Karp**: BFS-based, O(VE²) complexity

## How to Recognize This Type of Problem

- Maximum throughput or capacity problems
- Resource flow through network with constraints
- "Maximum number of..." with bottlenecks
- Problems reducible to source-sink flow
- Matching problems in general graphs (not just bipartite)

## LeetCode Problems

- [Maximum Flow (custom implementation)](https://leetcode.com/)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/)
- [2403. Minimum Time to Kill All Monsters](https://leetcode.com/problems/minimum-time-to-kill-all-monsters/)
