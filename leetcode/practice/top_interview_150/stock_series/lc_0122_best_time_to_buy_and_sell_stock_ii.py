"""
LeetCode 122 - Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		a = 0
		b = -prices[0]
		for i in range(1, len(prices)):
			tmp = a
			a = max(a, b + prices[i])
			b = max(b, tmp - prices[i])
		return a


sol = Solution()

# Example 1: Output 7
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

# Example 2: Output 4
print(sol.maxProfit([1, 2, 3, 4, 5]))

# Example 3: Output 0
print(sol.maxProfit([7, 6, 4, 3, 1]))
