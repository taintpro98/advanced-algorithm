"""
LeetCode 372 - Super Pow
https://leetcode.com/problems/super-pow/

Pattern:
Modular Exponentiation with Large Exponent
"""
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        MOD = 1337
        a %= MOD
        for digit in b:
            ans = pow(ans, 10, MOD)
            ans *= pow(a, digit, MOD)
            ans %= MOD
        return ans
    
a = 2147483647
b = [2,0,0]
sol = Solution()
ans = sol.superPow(a, b)
print(ans)