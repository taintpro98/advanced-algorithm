"""
LeetCode 139 - Word Break
https://leetcode.com/problems/word-break/

Pattern:
String DP
"""
from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		dp = [False] * (len(s) + 1) # dp[i] is the result of string with len i
		dp[0] = True
		for t in range(1, len(s)+1):
			for w in wordDict:
				if t >= len(w) and s[t-len(w):t] == w and dp[t-len(w)]:
					dp[t] = True
					break
		return dp[len(s)]


sol = Solution()

# Example 1: Output True
print(sol.wordBreak("leetcode", ["leet", "code"]))

# Example 2: Output True
print(sol.wordBreak("applepenapple", ["apple", "pen"]))

# Example 3: Output False
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
