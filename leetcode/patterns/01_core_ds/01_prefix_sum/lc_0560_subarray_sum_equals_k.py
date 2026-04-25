"""
LeetCode 560 - Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Pattern:
Prefix Sum + Hash Map
"""
from typing import List

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		od = {} # the sum that ends at that index
		od[0] = 1
		cur = 0
		ans = 0
		for t in range(len(nums)):
			cur += nums[t]
			if cur - k in od:
				ans += od[cur - k]
			if cur in od:
				od[cur] += 1
			else:
				od[cur] = 1
		return ans


sol = Solution()
nums = [1,2,3]
k = 3
ans = sol.subarraySum(nums, k)
print(ans)