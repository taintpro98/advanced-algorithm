# Shortest Path Algorithms

## What This Subtopic Is About

Shortest path algorithms find minimum-cost paths in weighted graphs. This pattern includes classic algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall) and their applications to grid-based problems, network routing, and optimization.

## Typical Patterns & Invariants

- **Dijkstra's algorithm**: Single-source shortest path with non-negative weights using priority queue
- **Bellman-Ford**: Handles negative weights, detects negative cycles
- **Floyd-Warshall**: All-pairs shortest paths in O(n³)
- **BFS for unweighted**: O(V+E) for unit-weight graphs
- **A* search**: Heuristic-guided Dijkstra for faster pathfinding

## How to Recognize This Type of Problem

- Finding shortest/minimum-cost path in graph or grid
- Problems with weighted edges or cells
- "Minimum time/cost to reach..."
- Network delay, packet routing scenarios
- Grid traversal with obstacles or varying costs

## LeetCode Problems

- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)
