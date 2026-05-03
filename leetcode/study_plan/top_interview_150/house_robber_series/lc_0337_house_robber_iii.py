"""
LeetCode 337 - House Robber III
https://leetcode.com/problems/house-robber-iii/

Pattern:
State Machine DP (Tree)
"""
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def rob(self, root: Optional[TreeNode]) -> int:
		memo = {}
		def recursive(node: Optional[TreeNode]) -> int:
			if not node:
				return 0
			if node in memo:
				return memo[node]
			ans1 = recursive(node.left) + recursive(node.right)
			ans2 = node.val
			if node.left:
				ans2 += recursive(node.left.left) + recursive(node.left.right)
			if node.right:
				ans2 += recursive(node.right.left) + recursive(node.right.right)
			memo[node] = max(ans1, ans2)
			return memo[node]
		return recursive(root)


sol = Solution()

# Example 1: Output 7
#     3
#    / \
#   2   3
#    \   \
#     3   1
root1 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
print(sol.rob(root1))

# Example 2: Output 9
#     3
#    / \
#   4   5
#  / \   \
# 1   3   1
root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
print(sol.rob(root2))
