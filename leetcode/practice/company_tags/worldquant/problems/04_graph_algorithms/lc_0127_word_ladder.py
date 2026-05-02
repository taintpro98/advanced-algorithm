"""
LeetCode 127 - Word Ladder
https://leetcode.com/problems/word-ladder/

Pattern:
BFS on Implicit Graph
"""
from typing import List


class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		pass


sol = Solution()

# Example 1: Output 5
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

# Example 2: Output 0
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
