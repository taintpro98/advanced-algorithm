"""
LeetCode 1293 – Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

Pattern:
BFS with Extended State (x, y, remaining_eliminations)
"""
from typing import List
from collections import deque

from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        if M == 1 and N == 1:
            return 0
        # best_used[(x,y)] = minimum walls broken used to reach (x,y)
        best_used = {(0, 0): 0}
        q = deque([(0, 0, 0, 0)])  # x, y, used, steps
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y, used, steps = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                new_used = used + grid[nx][ny]
                if new_used > k:
                    continue
                if nx == M - 1 and ny == N - 1:
                    return steps + 1
                if (nx, ny) not in best_used or new_used < best_used[(nx, ny)]:
                    best_used[(nx, ny)] = new_used
                    q.append((nx, ny, new_used, steps + 1))
        return -1

grid = [[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]]
k = 4
sol = Solution()
ans = sol.shortestPath(grid, k)
print(ans)