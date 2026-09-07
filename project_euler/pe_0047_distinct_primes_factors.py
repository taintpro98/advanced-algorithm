"""
Project Euler 47 - Distinct Primes Factors
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?

Pattern:
Sieve of Distinct Prime Factor Counts, Consecutive Run Scan
"""
RANGE = 10000

def first_consecutive_distinct_factors(k: int) -> int:
	primes = []
	while len(primes) < 100 * RANGE:
		primes += [0] * RANGE
		limit = len(primes)
		for p in range(2, limit):
			if primes[p] == 0:
				lower = max(2, (limit - RANGE + p - 1) // p)
				for t in range(lower * p, limit, p):
					primes[t] += 1
		n = max(2, limit - RANGE)
		while n < limit:
			if primes[n] == k and n < limit - k + 1:
				choice = True
				for x in range(1, k):
					if primes[n + x] != k:
						choice = False
				if choice:
					return n
			n += 1
	return -1
		



# Example: k = 3 -> 644
print(first_consecutive_distinct_factors(3))

# Answer
print(first_consecutive_distinct_factors(4))
