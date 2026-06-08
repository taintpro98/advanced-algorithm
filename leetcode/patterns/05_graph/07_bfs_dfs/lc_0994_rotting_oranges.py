"""
LeetCode 994 - Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

Pattern:
BFS (Multi-source)
"""
from typing import List
from collections import deque

class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		dirs = ((0,1), (1,0), (0,-1), (-1,0))
		R, C = len(grid), len(grid[0])
		q = deque()
		fresh_count = 0
		for x in range(R):
			for y in range(C):
				if grid[x][y] == 2:
					q.append((x, y, 0))
				elif grid[x][y] == 1:
					fresh_count += 1
		if fresh_count == 0:
			return 0
		ans = 0
		while q:
			x, y, d = q.popleft()
			for dx, dy in dirs:
				nx, ny = x + dx, y + dy
				if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
					grid[nx][ny] = 2
					fresh_count -= 1
					dist = d + 1
					q.append((nx, ny, dist))
					ans = max(ans, dist)
		return ans if fresh_count == 0 else -1


sol = Solution()

# Example 1: Output 4
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

# Example 2: Output -1
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

# Example 3: Output 0
print(sol.orangesRotting([[0,2]]))
