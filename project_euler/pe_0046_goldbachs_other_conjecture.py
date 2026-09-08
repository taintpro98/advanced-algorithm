"""
Project Euler 46 - Goldbach's Other Conjecture
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 x 1^2
15 = 7 + 2 x 2^2
21 = 3 + 2 x 3^2
25 = 7 + 2 x 3^2
27 = 19 + 2 x 2^2
33 = 31 + 2 x 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

Pattern:
Sieve of Eratosthenes, Perfect Squares, Search
"""
def smallest_goldbach_counterexample(limit: int) -> int:
	eratos = limit * [2] # 00 - 0, 01 - 1, 10 - 2, 11 - 3 (prime or not + goldbach or note)
	for p in range(2, limit):
		if p % 2 == 1 and eratos[p] == 0:
			return p
		if eratos[p] == 2 or eratos[p] == 3:
			for t in range(2*p, limit, p):
				eratos[t] = eratos[t] - 2 if eratos[t] >= 2 else eratos[t]
			if p > 2:
				d = p + 2
				i = 1
				while d < limit:
					eratos[d] = eratos[d] + 1 if eratos[d] % 2 == 0 else eratos[d]
					i += 1
					d = p + 2*i*i
		p += 1
	return -1


# Example: limit = 34 -> -1 (every odd composite below 34 satisfies the conjecture)
print(smallest_goldbach_counterexample(34))

# Answer
print(smallest_goldbach_counterexample(10000))
