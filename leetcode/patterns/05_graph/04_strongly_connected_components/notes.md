# Strongly Connected Components

## What This Subtopic Is About

Strongly Connected Components (SCCs) are maximal subgraphs where every vertex is reachable from every other vertex. This pattern uses Tarjan's or Kosaraju's algorithms to decompose directed graphs into SCCs for analysis and optimization.

## Typical Patterns & Invariants

- **Tarjan's algorithm**: Single DFS with low-link values and stack
- **Kosaraju's algorithm**: Two DFS passes (original + reversed graph)
- **Condensation graph**: Treat each SCC as single node, resulting DAG
- **Discovery time**: Track when vertex first visited
- **Low-link value**: Earliest discoverable vertex reachable in subtree

## How to Recognize This Type of Problem

- Finding cycles or circular dependencies in directed graphs
- Analyzing reachability in both directions
- Graph decomposition into strongly connected regions
- Problems on directed graphs requiring bidirectional paths
- Identifying "core" or "kernel" subgraphs

## LeetCode Problems

- [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
- [1568. Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)
- [928. Minimize Malware Spread II](https://leetcode.com/problems/minimize-malware-spread-ii/)
