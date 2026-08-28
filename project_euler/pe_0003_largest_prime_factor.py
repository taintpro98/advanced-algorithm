"""
Project Euler 3 - Largest Prime Factor
https://projecteuler.net/problem=3

Pattern:
Prime Factorization, Trial Division
"""


def largest_prime_factor(n: int) -> int:
	p = 2
	ans = 0
	while p*p <= n:
		if n % p == 0:
			ans = p
			while n % p == 0:
				n //= p
		p += 1
	if n > 1:
		ans = n
	return ans


# Example: n = 13195 -> 29  (prime factors: 5, 7, 13, 29)
print(largest_prime_factor(13195))

# Answer: n = 600851475143
print(largest_prime_factor(600851475143))
