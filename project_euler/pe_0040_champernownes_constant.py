"""
Project Euler 40 - Champernowne's Constant
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

	0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of:

	d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

Pattern:
Digit Indexing, String Construction
"""
import math 

def cald(index: int) -> int:
	sumdigits = 0
	curdigit = 0
	lower_bound = 0
	while index > sumdigits:
		curdigit += 1
		sumdigits += curdigit*9*10**(curdigit - 1)
	lower_bound = sumdigits - curdigit*9*10**(curdigit - 1)
	curidx = index - lower_bound
	reminder = curidx % curdigit
	if reminder == 0:
		curnumber = curidx // curdigit + 10**(curdigit - 1) - 1
		return int(str(curnumber)[-1])
	curnumber = curidx // curdigit + 10**(curdigit - 1)
	return int(str(curnumber)[reminder - 1])

def champernowne_digit_product(positions: list[int]) -> int:
	return math.prod([cald(x) for x in positions])


# Example: positions = [12] -> 1
print(champernowne_digit_product([12]))

# Answer
print(champernowne_digit_product([1, 10, 100, 1000, 10000, 100000, 1000000]))
