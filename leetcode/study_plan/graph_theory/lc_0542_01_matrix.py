"""
LeetCode 542 - 01 Matrix
https://leetcode.com/problems/01-matrix/

Pattern:
BFS Multi-Source
"""
from typing import List


class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		pass


sol = Solution()

# Example 1: Output [[0,0,0],[0,1,0],[0,0,0]]
print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))

# Example 2: Output [[0,0,0],[0,1,0],[1,2,1]]
print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
