"""
LeetCode 547 - Number of Provinces
https://leetcode.com/problems/number-of-provinces/

Pattern:
Union-Find / DFS Connected Components
"""
from typing import List


class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		pass


sol = Solution()

# Example 1: Output 2
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

# Example 2: Output 3
print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
