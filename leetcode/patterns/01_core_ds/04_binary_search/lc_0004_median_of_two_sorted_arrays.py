"""
LeetCode 4 - Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Pattern:
Binary Search on Partition Point
"""
from typing import List

class Solution:
    def binSearch(self, nums1: List[int], nums2: List[int]): # len(nums1) <= len(nums2)
        S = len(nums1) + len(nums2)
        k = (S + 1) // 2
        l, r = 0, len(nums1)
        left1 = 0
        left2 = k
        while l <= r:
            k1 = l + (r-l)//2
            k2 = k - k1
            if k1 > 0 and k2 < len(nums2) and nums1[k1-1] > nums2[k2]:
                r = k1 - 1
            elif k2 > 0 and k1 < len(nums1) and nums2[k2-1] > nums1[k1]:
                l = k1 + 1
            else:
                left1 = k1
                left2 = k - k1
                break
        lefts = []
        if left1 > 0:
            lefts.append(nums1[left1-1])
        if left2 > 0:
            lefts.append(nums2[left2-1])
        left = max(lefts)
        if S % 2 == 0:
            rights = []
            if left1 < len(nums1):
                rights.append(nums1[left1])
            if left2 < len(nums2):
                rights.append(nums2[left2])
            right = min(rights)
            return (left + right) / 2
        return left
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            return self.binSearch(nums1, nums2)
        return self.binSearch(nums2, nums1) 
        
    
nums1 = [1,3]
nums2 = [2,7]
sol = Solution()
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)