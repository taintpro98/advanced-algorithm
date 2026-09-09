"""
Project Euler 53 - Combinatoric Selections
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n! / (r!(n-r)!), where r <= n, n! = n x (n-1) x ... x 3 x 2 x 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater
than one-million?
"""


def count_combinations_above(max_n: int, threshold: int) -> int:
	dp = [0] * (max_n // 2 + 1)
	cnt = 0
	for n in range(0, max_n + 1):
		for k in range(n // 2, -1, -1):
			if k == 0:
				dp[k] = 1
			elif k > (n-1) // 2:
				dp[k] = dp[k-1] + dp[k-1]
			else:
				dp[k] = dp[k] + dp[k-1]
			if dp[k] > threshold:
				cnt += 1 if n % 2 == 0 and k == n//2 else 2
	return cnt


# Example: max_n = 22, threshold = 1000000 -> 0 (no value exceeds one-million until n = 23)
print(count_combinations_above(22, 1000000))

# Answer
print(count_combinations_above(100, 1000000))
