"""
LeetCode 188 - Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		dp = [0] + k * [0] + k * [-prices[0]]
		for i in range(1, len(prices)):
			a = dp.copy()
			for x in range(1, k+1):
				dp[x] = max(dp[x], a[x+k] + prices[i])
			for x in range(k):
				dp[x+k+1] = max(dp[x+k+1], a[x] - prices[i])
		return max(dp[1:k+1] + [0])


sol = Solution()

# Example 1: Output 2
print(sol.maxProfit(2, [2, 4, 1]))

# Example 2: Output 7
print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))
