"""
Project Euler 77 - Prime Summations
https://projecteuler.net/problem=77

It is possible to write ten as the sum of sieve in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of sieve in over five
thousand different ways?

Pattern:
Coin Change Counting, Unbounded Knapsack, Sieve of Eratosthenes
"""
def first_prime_summation(ways: int) -> int:
	sieve = [True] * 100
	sieve[0] = sieve[1] = False
	primes = []
	for p in range(2, 100):
		if sieve[p]:
			primes.append(p)
			for t in range(2*p, 100, p):
				sieve[t] = False
	dp = [[0] * (len(primes) + 1) for _ in range(5000)] # dp[x][y] = min value with x ways of y primes
	for i in range(len(primes) + 1):
		dp[0][i] = 1
		dp[1][i] = 0
	for x in range(2, 5000):
		for y in range(1, len(primes) + 1):
			a = x
			while a >= 0:
				dp[x][y] += dp[a][y-1]
				a -= primes[y-1]
			if dp[x][y] > ways:
				return x
	return -1

	


# Example: ways = 4 -> 10
print(first_prime_summation(4))

# Answer
print(first_prime_summation(5000))
