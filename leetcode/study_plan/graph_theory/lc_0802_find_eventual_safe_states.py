"""
LeetCode 802 - Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/

Pattern:
DFS / Cycle Detection
"""
from typing import List


class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		pass


sol = Solution()

# Example 1: Output [2, 4, 5, 6]
print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))

# Example 2: Output [4]
print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
