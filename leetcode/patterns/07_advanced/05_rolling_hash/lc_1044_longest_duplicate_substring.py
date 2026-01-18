"""
LeetCode 1044 - Longest Duplicate Substring
https://leetcode.com/problems/longest-duplicate-substring/

Pattern:
Rolling Hash with Binary Search
"""
class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.BASE = 131
        self.prefix = []
        self.power = []
    
    def rollHash(self, l: int, r: int) -> int: # [l, r)
        return (self.prefix[r] - self.prefix[l] * self.power[r-l]) % self.MOD
    
    def findDuplicateK(self, s: str, k: int) -> int:
        num_to_str_map = {}
        for t in range(len(s) - k + 1):
            rhash = self.rollHash(t, t+k)
            if rhash in num_to_str_map and s[num_to_str_map[rhash]:num_to_str_map[rhash]+k] == s[t:t+k]:
                return num_to_str_map[rhash]
            num_to_str_map[rhash] = t
        return -1
    
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        self.prefix = [0] * (n+1)
        self.power = [1] * (n+1)
        for t in range(1, n+1):
            self.prefix[t] = self.BASE * self.prefix[t-1] + ord(s[t-1])
            self.prefix[t] %= self.MOD
            self.power[t] = self.power[t-1] * self.BASE % self.MOD
        
        l, r = 1, n-1
        best_start = -1
        best_len = 0
        while l <= r:
            mid = l + (r-l+1) // 2
            start = self.findDuplicateK(s, mid)
            if start != -1:
                best_len = mid
                best_start = start
                l = mid + 1
            else:
                r = mid - 1
        return "" if best_start == -1 else s[best_start:best_start+best_len]
    
s = "aa"
sol = Solution()
ans = sol.longestDupSubstring(s)
print(ans)