"""
LeetCode 121 - Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		ans = 0
		a = -prices[0]
		b = 0
		for i in range(1, len(prices)):
			b = max(b, a + prices[i])
			a = max(a, -prices[i])
			ans = max(ans, b)
		return ans


sol = Solution()

# Example 1: Output 5
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

# Example 2: Output 0
print(sol.maxProfit([7, 6, 4, 3, 1]))
