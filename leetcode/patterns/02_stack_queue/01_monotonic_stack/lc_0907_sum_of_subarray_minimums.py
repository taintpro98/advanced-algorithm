"""
LeetCode 907 - Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Pattern:
Monotonic Stack + Contribution Technique

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
from typing import List

class Solution:
    def countNumArray(self, l: int, r: int, mid: int) -> int:
        if l + 1 > mid or r - 1 < mid:
            return 0
        return (mid - l) * (r - mid)
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        result = 0
        mstk = []
        n = len(arr)
        # l, r are the previous and next smaller
        for (idx, t) in enumerate(arr):
            while mstk and t <= arr[mstk[-1]]:
                top = mstk[-1]
                mstk.pop()
                l = -1
                if mstk:
                    l = mstk[-1]
                result += arr[top] * self.countNumArray(l, idx, top)
                result %= MOD
            mstk.append(idx)
        while mstk:
            top = mstk[-1]
            mstk.pop()
            l = -1
            if mstk:
                l = mstk[-1]
            result += arr[top] * self.countNumArray(l, n, top)
            result %= MOD
        return result
                
arr = [3,3]
sol = Solution()
ans = sol.sumSubarrayMins(arr)
print(ans)
        