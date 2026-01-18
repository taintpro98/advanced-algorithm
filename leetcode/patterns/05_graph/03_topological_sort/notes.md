# Topological Sort

## What This Subtopic Is About

Topological sort produces a linear ordering of vertices in a Directed Acyclic Graph (DAG) where all edges point forward. This pattern is essential for dependency resolution, task scheduling, and build systems.

## Typical Patterns & Invariants

- **Kahn's algorithm (BFS)**: Process vertices with in-degree 0, decrement neighbors
- **DFS-based**: Post-order traversal gives reverse topological order
- **Cycle detection**: Impossible to topologically sort if cycle exists
- **In-degree tracking**: Count incoming edges to identify ready nodes
- **Lexicographic order**: Use priority queue for smallest valid ordering

## How to Recognize This Type of Problem

- Task scheduling with prerequisites
- Course dependencies (CS curriculum classic)
- Build order or compilation dependencies
- "Before/after" relationship constraints
- Detecting cycles in directed graphs

## LeetCode Problems

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
