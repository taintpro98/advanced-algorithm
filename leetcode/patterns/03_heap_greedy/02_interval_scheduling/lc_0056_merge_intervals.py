"""
LeetCode 56 - Merge Intervals
https://leetcode.com/problems/merge-intervals/

Pattern:
Sort and Merge Intervals
"""
from typing import List


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals.sort(key = lambda x: x[0])
		ans = []
		cs, ce = intervals[0]
		for t in range(1, len(intervals)):
			start, end = intervals[t]
			if start <= ce:
				cs = min(cs, start)
				ce = max(ce, end)
			else:
				ans.append([cs,ce])
				cs, ce = start, end
		ans.append([cs,ce])
		return ans


sol = Solution()

# Example 1: Output [[1,6],[8,10],[15,18]]
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))

# Example 2: Output [[1,5]]
print(sol.merge([[1,4],[4,5]]))
