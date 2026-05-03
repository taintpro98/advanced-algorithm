"""
LeetCode 714 - Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Pattern:
State Machine DP
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		pass


sol = Solution()

# Example 1: Output 8
print(sol.maxProfit([1, 3, 2, 8, 4, 9], 2))

# Example 2: Output 6
print(sol.maxProfit([1, 3, 7, 5, 10, 3], 3))
