"""
Project Euler 9 - Special Pythagorean Triplet
https://projecteuler.net/problem=9

Pattern:
Number Theory, Enumeration, Euclid's Formula
"""


def special_pythagorean_triplet(perimeter: int) -> int:
	c = perimeter // 3
	while c < perimeter:
		a = (perimeter - c) // 2
		while a > 0:
			b = perimeter - c - a
			if a*a + b*b == c*c:
				print(a, b, c)
				return a*b*c
			a -= 1
		c += 1

# Example: perimeter = 12 -> 60  (3, 4, 5)
print(special_pythagorean_triplet(12))

# Answer: perimeter = 1000
print(special_pythagorean_triplet(1000))
