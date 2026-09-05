"""
Project Euler 30 - Digit Fifth Powers
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

	1634 = 1^4 + 6^4 + 3^4 + 4^4
	8208 = 8^4 + 2^4 + 0^4 + 8^4
	9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

Pattern:
Digit Powers, Search Bound Derivation, Brute Force
"""


def digit_power_sum(power: int) -> int:
	upper = 1
	p = 9**power
	while 10**(upper-1) / upper <= p:
		upper += 1
	upper = 10**upper
	res = 0
	for n in range(10, upper):
		s = str(n)
		ans = n
		for c in s:
			ans -= int(c)**power
		if ans == 0:
			res += n
	return res


# Example: power = 4 -> 19316
print(digit_power_sum(4))

# Answer
print(digit_power_sum(5))
