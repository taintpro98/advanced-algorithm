"""
Project Euler 49 - Prime Permutations
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

Pattern:
Primality Testing, Digit Permutations, Grouping by Signature
"""
from typing import List
from collections import defaultdict

def prime_permutation_sequences(digits: int) -> List[str]:
	upper = 10**digits + 1
	lower = 10**(digits - 1)
	primes = upper * [True]
	primes[0] = primes[1] = False
	for p in range(2, upper):
		if primes[p]:
			for t in range(2*p, upper, p):
				primes[t] = False
	prime_set = defaultdict(list)
	ans = []
	for p in range(lower, upper):
		if primes[p]:
			key = "".join(sorted(str(p)))
			prime_set[key].append(p)
			if len(prime_set[key]) >= 3:
				for t in range(1, len(prime_set[key]) - 1):
					first = 2*prime_set[key][t] - p
					if first in prime_set[key]:
						ans.append(str(first) + str(prime_set[key][t]) + str(p))
	return ans


# Example: digits = 4 -> ['148748178147', <answer>]
print(prime_permutation_sequences(4))
