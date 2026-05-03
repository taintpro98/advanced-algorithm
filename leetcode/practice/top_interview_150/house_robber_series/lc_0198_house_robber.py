"""
LeetCode 198 - House Robber
https://leetcode.com/problems/house-robber/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		a = 0
		b = nums[0]
		for i in range(2, len(nums) + 1):
			tmp = a
			a = b
			b = max(b, tmp + nums[i-1])
		return b


sol = Solution()

# Example 1: Output 4
print(sol.rob([1, 2, 3, 1]))

# Example 2: Output 12
print(sol.rob([2, 7, 9, 3, 1]))
