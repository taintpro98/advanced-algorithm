"""
Project Euler 10 - Summation of Primes
https://projecteuler.net/problem=10

Pattern:
Sieve of Eratosthenes, Prime Generation
"""
def is_prime(p: int) -> bool:
    if p <= 1:
        return False
    x = 2
    while x*x <= p:
        if p % x == 0:
            return False
        x += 1
    return True

def sum_of_primes_below(limit: int) -> int:
	sum = 0
	for p in range(limit):
		if is_prime(p):
			sum += p
	return sum


# Example: limit = 10 -> 17  (2 + 3 + 5 + 7)
print(sum_of_primes_below(10))

# Answer: limit = 2000000
print(sum_of_primes_below(2000000))
