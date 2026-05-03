"""
LeetCode 213 - House Robber II
https://leetcode.com/problems/house-robber-ii/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def linearRob(self, nums: List[int]) -> int:
		a = 0
		b = nums[0]
		for i in range(2, len(nums) + 1):
			tmp = a
			a = b
			b = max(b, tmp + nums[i-1])
		return b
	
	def rob(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		return max(self.linearRob(nums[:-1]), self.linearRob(nums[1:]))


sol = Solution()

# Example 1: Output 3
print(sol.rob([2, 3, 2]))

# Example 2: Output 4
print(sol.rob([1, 2, 3, 1]))

# Example 3: Output 3
print(sol.rob([1, 2, 3]))
