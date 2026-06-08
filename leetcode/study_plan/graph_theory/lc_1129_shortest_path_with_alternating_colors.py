"""
LeetCode 1129 - Shortest Path with Alternating Colors
https://leetcode.com/problems/shortest-path-with-alternating-colors/

Pattern:
BFS on State Graph
"""
from typing import List
from collections import deque, defaultdict

class Solution:
	def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
		dist = [-1] * n
		graph = defaultdict(list)
		for (u, v) in redEdges:
			graph[u].append((v, 0))
		for (u, v) in blueEdges:
			graph[u].append((v, 1))
		q = deque([
			(0, 0), (0, 1)
		])
		visited = set([(0, 0), (0, 1)])
		level = 0
		while q:
			for _ in range(len(q)):
				node, prev_edge = q.popleft()
				if dist[node] == -1:
					dist[node] = level
				for v, edge in graph[node]:
					if edge == prev_edge:
						continue
					if (v, edge) in visited:
						continue
					visited.add((v, edge))
					q.append((v, edge))
			level += 1
		return dist


sol = Solution()

# Example 1: Output [0,1,-1]
print(sol.shortestAlternatingPaths(3, [[0,1],[1,2]], []))

# Example 2: Output [0,1,-1]
print(sol.shortestAlternatingPaths(3, [[0,1]], [[2,1]]))

print(sol.shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]]))

print(sol.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))