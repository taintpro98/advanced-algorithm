"""
LeetCode 878 – Nth Magical Number
https://leetcode.com/problems/nth-magical-number/

Pattern:
Number Theory + Binary Search + LCM
"""
# class Solution:
#     def gcd(self, a: int, b: int):
#         while b:
#             a, b = b, a % b
#         return a
            
#     def lcm(self, a: int, b: int) -> int:
#         return a * b // self.gcd(a, b)
    
#     def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
#         MOD = 10**9 + 7
#         lcm = self.lcm(a, b)
#         count_to_lcm = lcm//a + lcm//b - 1
#         print(count_to_lcm)
#         q = n // count_to_lcm
#         r = n % count_to_lcm
#         base = q * lcm
#         if r == 0:
#             return base % MOD
#         t = 1
#         x = base + a
#         y = base + b
#         while t <= r:
#             if x < y:
#                 ans = x % MOD
#                 x += a
#             elif x > y:
#                 ans = y % MOD
#                 y += b
#             else:
#                 ans = x % MOD
#                 x += a
#                 y += b
#             t += 1
#         return ans

class Solution:
    def gcd(self, a: int, b: int):
        while b:
            a, b = b, a % b
        return a
            
    def lcm(self, a: int, b: int) -> int:
        return a * b // self.gcd(a, b)
    
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l, r = min(a, b), n * min(a, b)
        L = self.lcm(a, b)
        while l < r:
            mid = l + (r - l) // 2
            c = (mid // a) + (mid // b) - (mid // L)
            if c < n:
                l = mid + 1
            else:
                r = mid
        return l % MOD
    
n = 5
a = 2
b = 4
sol = Solution()
ans = sol.nthMagicalNumber(n, a, b)
print(ans)