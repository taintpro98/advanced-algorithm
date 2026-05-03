"""
LeetCode 202 - Happy Number
https://leetcode.com/problems/happy-number/

Pattern:
Floyd's Cycle Detection (Fast & Slow Pointers)
"""

# class Solution:
#     def getSquaresSum(self, n: int) -> int:
#         ans = 0
#         while n > 0:
#             r = n % 10
#             ans += r*r
#             n //= 10
#         return ans
#     def isHappy(self, n: int) -> bool:
#         t = n
#         exits = set([1])
#         while t not in exits:
#             exits.add(t)
#             t = self.getSquaresSum(t)
#         return t == 1
class Solution:
    def getSquaresSum(self, n: int) -> int:
        ans = 0
        while n > 0:
            r = n % 10
            ans += r*r
            n //= 10
        return ans
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow = fast = n
        while fast != 1:
            slow = self.getSquaresSum(slow)
            fast = self.getSquaresSum(self.getSquaresSum(fast))
            if slow == fast:
                break
        return fast == 1

n = 82
sol = Solution()
print(sol.isHappy(n))  # True