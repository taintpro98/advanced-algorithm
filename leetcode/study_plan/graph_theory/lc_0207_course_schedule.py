"""
LeetCode 207 - Course Schedule
https://leetcode.com/problems/course-schedule/

Pattern:
Topological Sort for Cycle Detection
"""
from typing import List
from collections import deque, defaultdict

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		if len(prerequisites) == 0:
			return True
		graph = defaultdict(list)
		count = [0] * numCourses # the number of vertices that points to this vertex
		for (a, b) in prerequisites: # b -> a
			count[a] += 1
			graph[b].append(a)
		process = deque()
		for v, c in enumerate(count):
			if c == 0:
				process.append(v)
		done = 0
		while process:
			v = process.popleft()
			for g in graph[v]:
				count[g] -= 1
				if count[g] == 0:
					process.append(g)
			done += 1
		return done == numCourses

sol = Solution()

# Example 1: Output True
print(sol.canFinish(2, [[1, 0]]))

# Example 2: Output False
print(sol.canFinish(2, [[1, 0], [0, 1]]))

# Example 3: Output True
print(sol.canFinish(1, []))

# Example 4: Output True
print(sol.canFinish(3, [[1,0],[2,0]]))