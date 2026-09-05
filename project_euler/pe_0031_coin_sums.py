"""
Project Euler 31 - Coin Sums
https://projecteuler.net/problem=31

UK coins in general circulation (in pence):
1, 2, 5, 10, 20, 50, 100, 200.

Pattern:
Unbounded Knapsack, Counting DP
"""

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sums(target: int) -> int:
	dp = [(target+1) * [0] for _ in range(len(COINS) + 1)]
	for i in range(1, len(COINS) + 1):
		for j in range(target + 1):
			if j == 0:
				dp[i][j] = 1
			elif j < COINS[i-1]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j - COINS[i-1]]
	return dp[8][target]


# Example: target = 5 -> 4  (1+1+1+1+1, 1+1+1+2, 1+2+2, 5)
print(coin_sums(5))

# Answer: target = 200  (£2)
print(coin_sums(200))
