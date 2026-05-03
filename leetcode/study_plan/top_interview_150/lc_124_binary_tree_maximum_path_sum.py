"""
LeetCode 124 - Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Pattern:
DFS / Tree Recursion
"""
from typing import Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		ans = float('-inf')
		def dfs(node: Optional[TreeNode]) -> int: # this max sum of the path from root (no need to leaf)
			nonlocal ans
			if not node:
				return 0
			left = max(0, dfs(node.left))
			right = max(0, dfs(node.right))
			ans = max(ans, node.val + left + right)
			return max(node.val, node.val + dfs(node.left), node.val + dfs(node.right))
		dfs(root)
		return ans

# Test
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxPathSum(root))  # Expected: 42
