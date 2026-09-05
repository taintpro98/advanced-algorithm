"""
Project Euler 27 - Quadratic Primes
https://projecteuler.net/problem=27

Quadratics of the form n^2 + a*n + b, with |a| < a_bound and |b| <= b_bound.
Return the product a*b of the pair producing the longest run of primes for
consecutive n starting at n = 0.

Pattern:
Primality Testing, Brute Force Search
"""


def quadratic_primes(a_bound: int, b_bound: int) -> int:
	is_primes = [True] * 1001
	for p in range(2, 1001):
		if not is_primes[p]:
			continue
		t = 2 * p
		while t <= 1000:
			is_primes[t] = False
			t += p
   
	def is_prime(p: int) -> bool:
		if p <= 1:
			return False
		if p <= 1000:
			return is_primes[p]
		d = 2
		while d * d <= p:
			if p % d == 0:
				return False
			d += 1
		return True
	max_len = 0
	ans_a = 0
	ans_b = 0
	for b in range(-b_bound, b_bound+1):
		if abs(b) != 2 and is_primes[abs(b)]:
			for a in range(-a_bound + 1, a_bound):
				if a % 2 == 1:
					n = 1
					while is_prime(n*n + a*n + b):
						n += 1
					if n > max_len:
						max_len = n
						ans_a = a
						ans_b = b
	return ans_a * ans_b


# Statement checkpoints: n^2 + n + 41 stays prime for n = 0..39 (40 primes),
# and n^2 - 79n + 1601 stays prime for n = 0..79 (80 primes).

# Example: |a| < 50, |b| <= 50 -> -235  (a = -5, b = 47, a run of 43 primes)
print(quadratic_primes(50, 50))

# Answer: |a| < 1000, |b| <= 1000
print(quadratic_primes(1000, 1000))
