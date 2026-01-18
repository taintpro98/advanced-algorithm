"""
LeetCode 718 - Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Pattern:
Rolling Hash for Longest Common Substring
"""
from typing import List

class Solution:
    def __init__(self):
        self.BASE = 131
        self.MOD = 10**9+7
        self.prefix1 = []
        self.prefix2 = []
        self.power = []

    def findCommonK(self, nums1: List[int], nums2: List[int], k: int) -> bool:
        num_to_start = {}
        for s in range(len(nums1)-k+1):
            hash1 = (self.prefix1[s+k] - self.prefix1[s] * self.power[k]) % self.MOD
            num_to_start[hash1] = s
        for s in range(len(nums2)-k+1):
            hash2 = (self.prefix2[s+k] - self.prefix2[s] * self.power[k]) % self.MOD
            if hash2 in num_to_start:
                return True
        return False
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1)
        L2 = len(nums2)
        self.prefix1 = (L1+1) * [0]
        self.prefix2 = (L2+1) * [0]
        self.power = (max(L1, L2) + 1) * [1]
        
        for t in range(1, L1+1):
            self.prefix1[t] = (self.prefix1[t-1] * self.BASE + nums1[t-1]) % self.MOD
        for t in range(1, L2+1):
            self.prefix2[t] = (self.prefix2[t-1] * self.BASE + nums2[t-1]) % self.MOD
        for t in range(1, len(self.power)):
            self.power[t] = self.power[t-1] * self.BASE % self.MOD
            
        l, r = 0, min(L1, L2)
        while l < r:
            mid = l + (r-l+1)//2
            if self.findCommonK(nums1, nums2, mid):
                l = mid
            else:
                r = mid - 1
        return l
    
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

sol = Solution()
ans = sol.findLength(nums1, nums2)
print(ans)