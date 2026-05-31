"""
LeetCode 802 - Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/
"""
from typing import List


class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		terminals = set()
		for v, l in enumerate(graph): # ":each l is an array
			if len(l) == 0:
				terminals.add(v)
		ans = []
		for v in range(len(graph)):
			print("fuck")
		return ans



sol = Solution()

# Example 1: Output [2, 4, 5, 6]
print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))

# Example 2: Output [4]
print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
