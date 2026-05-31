"""
LeetCode 210 - Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Pattern:
Kahn's Algorithm (BFS Topological Sort)
"""
from typing import List
from collections import deque, defaultdict


class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		if len(prerequisites) == 0:
			return [a for a in range(numCourses)]
		graph = defaultdict(list)
		count = [0] * numCourses # the number of vertices that points to this vertex
		for (a, b) in prerequisites: # b -> a
			count[a] += 1
			graph[b].append(a)
		process = deque()
		for v, c in enumerate(count):
			if c == 0:
				process.append(v)
		ans = []
		while process:
			v = process.popleft()
			ans.append(v)
			for g in graph[v]:
				count[g] -= 1
				if count[g] == 0:
					process.append(g)
		return [] if len(ans) < numCourses else ans

sol = Solution()

# Example 1: Output [0, 1]
print(sol.findOrder(2, [[1, 0]]))

# Example 2: Output [0, 1, 2, 3]
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

# Example 3: Output [] (cycle)
print(sol.findOrder(2, [[1, 0], [0, 1]]))
