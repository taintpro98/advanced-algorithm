"""
Project Euler 76 - Counting Summations
https://projecteuler.net/problem=76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""


def counting_summations(n: int) -> int:
	dp = [[0] * n for _ in range(n + 1)]
	for i in range(n):
		dp[0][i] = 1
	for x in range(1, n + 1):
		for y in range(1, n):
			a = x
			while a >= 0:
				dp[x][y] += dp[a][y-1]
				a -= y
	return dp[n][n-1]

# Example: n = 5 -> 6
print(counting_summations(5))

# Answer
print(counting_summations(100))
