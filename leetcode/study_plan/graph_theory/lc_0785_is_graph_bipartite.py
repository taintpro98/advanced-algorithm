"""
LeetCode 785 - Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

Pattern:
BFS / DFS Graph Coloring
"""
from typing import List


class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		pass


sol = Solution()

# Example 1: Output False
print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

# Example 2: Output True
print(sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
