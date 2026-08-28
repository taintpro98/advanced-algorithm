"""
Project Euler 7 - 10001st Prime
https://projecteuler.net/problem=7

Pattern:
Prime Generation, Sieve of Eratosthenes
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

def nth_prime(n: int) -> int:
	cnt = 0
	x = 1
	while cnt < n:
		x += 1
		if is_prime(x):
			cnt += 1
	return x

# Example: n = 6 -> 13
print(nth_prime(7))

# Answer: n = 10001
print(nth_prime(10001))
