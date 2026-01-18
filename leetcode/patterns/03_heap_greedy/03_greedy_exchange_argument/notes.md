# Greedy Exchange Argument

## What This Subtopic Is About

Greedy exchange argument is a proof technique and problem-solving approach where you show that swapping any deviation from your greedy choice cannot improve the solution. This pattern is essential for advanced greedy problems requiring rigorous correctness proofs.

## Typical Patterns & Invariants

- **Local optimality**: Make locally optimal choice at each step
- **Exchange argument proof**: Show swapping greedy choice with alternative doesn't improve solution
- **Matroid structure**: Problems with hereditary and exchange properties
- **Optimal substructure**: Greedy choice plus optimal solution to remaining subproblem
- **Sorting heuristic**: Often involves sorting by custom comparator

## How to Recognize This Type of Problem

- Optimization problems where greedy seems to work
- Problems requiring proof of correctness
- Scheduling, assignment, or selection with constraints
- Custom sorting order determines solution quality
- "Arrange" or "reorder" for optimal outcome

## LeetCode Problems

- [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [134. Gas Station](https://leetcode.com/problems/gas-station/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
