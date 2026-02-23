"""
LeetCode 50 - Pow(x, n)
https://leetcode.com/problems/powx-n/

Pattern:
Fast Exponentiation (Binary Exponentiation)

Key Insight:
- x^n = (x^2)^(n/2) if n is even
- x^n = x * (x^2)^(n/2) if n is odd
- Time: O(log n), Space: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        k = n // 2
        r = n % 2
        a = self.myPow(x, k)
        return a * a * self.myPow(x, r)