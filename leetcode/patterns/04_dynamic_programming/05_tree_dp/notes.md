# Tree Dynamic Programming

## What This Subtopic Is About

Tree DP computes optimal solutions on tree structures by solving subproblems on subtrees and combining results. This pattern leverages the recursive nature of trees, typically using post-order traversal to aggregate information from children to parents.

## Typical Patterns & Invariants

- **Post-order traversal**: Solve children before parents
- **DP on subtrees**: dp[node] = optimal value for subtree rooted at node
- **Include/exclude states**: dp[node][0/1] for whether node is selected
- **Rerooting technique**: Compute answer for each node as root in linear time
- **Path decomposition**: Heavy-light or centroid decomposition for advanced queries

## How to Recognize This Type of Problem

- Optimization on tree structures
- Selecting/excluding nodes with constraints
- Maximum/minimum path problems on trees
- Subtree-based aggregation
- Problems mentioning "root", "parent-child", "subtree"

## LeetCode Problems

- [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)
