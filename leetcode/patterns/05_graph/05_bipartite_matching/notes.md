# Bipartite Matching

## What This Subtopic Is About

Bipartite matching finds maximum cardinality matching in bipartite graphs where vertices split into two disjoint sets with edges only between sets. This pattern solves assignment problems using augmenting paths or flow algorithms.

## Typical Patterns & Invariants

- **Bipartite detection**: Two-coloring using BFS/DFS
- **Maximum matching**: Hungarian algorithm, Hopcroft-Karp
- **Augmenting paths**: Find paths to increase matching size
- **Hall's theorem**: Characterizes when perfect matching exists
- **Reduction to flow**: Model as max-flow problem with unit capacities

## How to Recognize This Type of Problem

- Assigning items to groups with constraints
- Graph can be split into two independent sets
- Matching or pairing problems
- "No two edges share a vertex" constraint
- Detecting odd-length cycles (bipartite test)

## LeetCode Problems

- [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
- [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)
- [1820. Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/)
