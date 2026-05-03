"""
LeetCode 123 - Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		p1 = 0
		p2 = 0
		p3 = -prices[0]
		p4 = -prices[0]

		for i in range(1, len(prices)):
			a1, a2, a3, a4 = p1, p2, p3, p4
			p1 = max(a1, a3 + prices[i])
			p2 = max(a2, a4 + prices[i])
			p3 = max(a3, - prices[i])
			p4 = max(a4, a1 - prices[i])
		return max(0, p1, p2)


sol = Solution()

# Example 1: Output 6
print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))

# Example 2: Output 4
print(sol.maxProfit([1, 2, 3, 4, 5]))

# # Example 3: Output 0
print(sol.maxProfit([7, 6, 4, 3, 1]))
