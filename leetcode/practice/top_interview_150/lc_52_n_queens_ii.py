"""
LeetCode 52 - N-Queens II
https://leetcode.com/problems/n-queens-ii/

Pattern:
Backtracking

Example 1:
Input: n = 4
Output: 2

Solution 1:                 Solution 2:
. Q . .                     . . Q .
. . . Q                     Q . . .
Q . . .                     . . . Q
. . Q .                     . Q . .

Example 2:
Input: n = 1
Output: 1

Q
"""
from typing import List

class Solution:    
	def dfs(self, x: int, y: int, n: int, ans: List[int], vc: set, dia1: set, dia2: set):
		if x == n-1:
			ans[0] += 1
			return
		vc.add(y)
		dia1.add(x-y)
		dia2.add(x+y)
		for t in range(n):
			if t not in vc and x + 1 - t not in dia1 and x + 1 + t not in dia2:
				self.dfs(x+1, t, n, ans, vc, dia1, dia2)
		vc.remove(y)
		dia1.remove(x-y)
		dia2.remove(x+y)
    
	def totalNQueens(self, n: int) -> int:
		ans = [0]
		vc = set()
		dia1 = set()
		dia2 = set()
		for t in range(n):
			self.dfs(0, t, n, ans, vc, dia1, dia2)
		return ans[0]


def visualize(n: int, expected: int):
    sol = Solution()
    result = sol.totalNQueens(n)
    print(f"Input: n = {n}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"{'PASS' if result == expected else 'FAIL'}")
    print()

visualize(4, 2)
