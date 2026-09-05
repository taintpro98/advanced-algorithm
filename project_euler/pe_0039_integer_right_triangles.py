"""
Project Euler 39 - Integer Right Triangles
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides {a, b, c},
there are exactly three solutions for p = 120:

	{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p <= 1000 is the number of solutions maximised?

Pattern:
Pythagorean Triples, Perimeter Bucketing, Counting
"""
from math import gcd

def most_solutions(p_max: int) -> int:
	cnt = [0] * (p_max + 1)
	m = 2
	while 2 * m * (m+1) <= p_max:
		for n in range(1, m):
			if gcd(m, n) != 1:
				continue
			if (m - n) % 2 == 0:
				continue
			p0 = 2*m*(m+n)
			for p in range(p0, p_max+1, p0):
				cnt[p] += 1
		m += 1
	return max(range(p_max + 1), key=lambda p: cnt[p])


# Example: p_max = 120 -> 120
print(most_solutions(120))

# Answer
print(most_solutions(1000))
