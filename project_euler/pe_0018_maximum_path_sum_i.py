"""
Project Euler 18 - Maximum Path Sum I
https://projecteuler.net/problem=18

Maximum total from top to bottom of the triangle, moving to one of the two
adjacent numbers on the row below at each step.

See: project_euler/pe_0067_maximum_path_sum_ii.py  (same question, 100 rows)

Pattern:
Triangle DP, Bottom-Up Relaxation
"""
from typing import List

EXAMPLE_TRIANGLE: List[List[int]] = [
	[3],
	[7, 4],
	[2, 4, 6],
	[8, 5, 9, 3],
]

TRIANGLE: List[List[int]] = [
	[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20, 4, 82, 47, 65],
	[19, 1, 23, 75, 3, 34],
	[88, 2, 77, 73, 7, 63, 67],
	[99, 65, 4, 28, 6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def max_path_sum(triangle: List[List[int]]) -> int:
	n = len(triangle)
	dp = n * [0]
	dp[0] = triangle[0][0]
	for i in range(1, n):
		for j in range(i, 0, -1):
			dp[j] = max(dp[j], dp[j-1]) + triangle[i][j]
		dp[0] = dp[0] + triangle[i][0]
	ans = dp[0]
	for t in range(1, n):
		if dp[t] > ans:
			ans = dp[t]
	return ans


# Example: EXAMPLE_TRIANGLE -> 23  (3 + 7 + 4 + 9)
print(max_path_sum(EXAMPLE_TRIANGLE))

# Answer: TRIANGLE
print(max_path_sum(TRIANGLE))
