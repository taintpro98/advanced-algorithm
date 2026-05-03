"""
LeetCode 140 - Word Break II
https://leetcode.com/problems/word-break-ii/

Pattern:
String DP / Backtracking
"""
from typing import List


class Solution:
	def backtrack(self, s: str, wordDict: List[str], t: int) -> List[str]: # solution of the string with length t
		if t == 0:
			return [""]
		ans = []
		for w in wordDict:
			if len(w) <= t and w == s[t-len(w):t]:
				pre = self.backtrack(s, wordDict, t-len(w))
				ans += [(x + " " + w).strip() for x in pre]
		return ans

	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		return self.backtrack(s, wordDict, len(s))


sol = Solution()

# Example 1: Output ["cat sand dog", "cats and dog"] (any order)
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

#Example 2: Output ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

# Example 3: Output []
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
