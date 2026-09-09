"""
Project Euler 28 - Number Spiral Diagonals
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""


def spiral_diagonals_sum(size: int) -> int:
	ans = 0
	k = r = 0
	a = 1
	upper = size * size 
	while a <= upper:
		ans += a
		if r < 3:
			r += 1	
		else:
			r = 0
			k += 1
		a = (2*k + 1) * (2*k + 1) + 2*r*(k+1)
	return ans


# Example: size = 5 -> 101
print(spiral_diagonals_sum(5))

# Answer
print(spiral_diagonals_sum(1001))
