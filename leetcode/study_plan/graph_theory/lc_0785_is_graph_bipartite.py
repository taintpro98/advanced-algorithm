"""
LeetCode 785 - Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

Pattern:
BFS / DFS Graph Coloring
"""
from typing import List
from collections import deque

class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		colors = [-1] * len(graph)
		def bfs(node: int) -> bool:
			q = deque()
			q.append(node)
			while q:
				u = q.popleft()
				for v in graph[u]:
					if colors[v] != -1:
						if colors[v] == colors[u]:
							return False
					else:
						colors[v] = 1 - colors[u]
						q.append(v)
			return True
		for t in range(len(graph)):
			if colors[t] == -1:
				colors[t] = 0
				if not bfs(t):
					return False
		return True

sol = Solution()

# Example 1: Output False
print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

# Example 2: Output True
print(sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))

print(sol.isBipartite([[1],[0],[4],[4],[2,3]]))

# Example 3: Output True
print(sol.isBipartite([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))