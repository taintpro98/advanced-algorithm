"""
Project Euler 57 - Square Root Convergents
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than the denominator?
"""
from math import gcd

def cal(x: int, y: int) -> tuple[int]:
	m = 2*y + x
	n = y + x
	d = gcd(m, n)
	return (m // d, n // d)

def count_longer_numerators(expansions: int) -> int:
	x, y = 3, 2
	n = 1
	cnt = 0
	while n <= expansions:
		if len(str(x)) > len(str(y)):
			cnt += 1
		x, y = cal(x, y)
		n += 1
	return cnt

# Example: expansions = 8 -> 1 (the eighth expansion, 1393/985, is the first)
print(count_longer_numerators(8))

# Answer
print(count_longer_numerators(1000))
