"""
LeetCode 221 - Maximal Square
https://leetcode.com/problems/maximal-square/

Pattern:
Dynamic Programming
"""
from typing import List

class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		M = len(matrix)
		N = len(matrix[0])
		dp = [0] * N
		cur_pre = 0
		ans = 0
		for i in range(M):
			for j in range(N):
				tmp = dp[j]
				if matrix[i][j] == '0':
					dp[j] = 0
				else:
					if j == 0:
						dp[j] = 1
					else:
						dp[j] = 1 + min(dp[j], dp[j-1], cur_pre)
				cur_pre = tmp
				if dp[j] > ans:
					ans = dp[j]
		return ans * ans


def print_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        print(" ".join(row))
    print()


sol = Solution()

matrix1 = [["0","0","1"],["0","1","1"],["1","1","1"]]
print_matrix(matrix1)
print(sol.maximalSquare(matrix1))  # Expected: 4
# dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])