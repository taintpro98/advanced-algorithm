"""
Project Euler 34 - Digit Factorials
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers below `limit` which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Pattern:
Digit Factorials, Search Bound Derivation, Brute Force
"""
from math import factorial

def sum_of_digit_factorials() -> int:
	upper = 1
	FACTS = {}
	for i in range(10):
		FACTS[i] = factorial(i)
	p = FACTS[9]
	while 10**(upper-1) / upper <= p:
		upper += 1
	upper = 10**upper
	res = 0
	for n in range(10, upper):
		s = str(n)
		ans = n
		for c in s:
			ans -= FACTS[int(c)]
		if ans == 0:
			res += n
	return res


# Example: limit = 1000 -> 145
# print(sum_of_digit_factorials(1000))

# Answer
print(sum_of_digit_factorials())
