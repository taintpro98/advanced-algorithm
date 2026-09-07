"""
Project Euler 50 - Consecutive Prime Sum
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

Pattern:
Sieve of Eratosthenes, Prefix Sums, Sliding Window
"""

def longest_consecutive_prime_sum(limit: int) -> int:
	primes = [True] * limit
	primes[0] = primes[1] = False
	primes_list = []
	for p in range(2, limit):
		if primes[p]:
			primes_list.append(p)
			for t in range(2*p, limit, p):
				primes[t] = False
	prefix = [2]
	for t in range(1, len(primes_list)):
		prefix.append(prefix[-1] + primes_list[t])
	longest = len(primes_list) - 1
	while longest > 1:
		idx = 0
		primes_sum = prefix[idx + longest] - prefix[idx]
		while primes_sum < limit and not primes[primes_sum] and idx + longest + 1 <= len(primes_list):
			idx += 1
			primes_sum = prefix[idx + longest] - prefix[idx]
		if primes_sum < limit and primes[primes_sum]:
			return primes_sum
		longest -= 1
	return -1


# Example: limit = 100 -> 41
print(longest_consecutive_prime_sum(100))

# Example: limit = 1000 -> 953
print(longest_consecutive_prime_sum(1000))

# Answer
print(longest_consecutive_prime_sum(1000000))
