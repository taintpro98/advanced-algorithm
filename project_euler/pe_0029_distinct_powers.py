"""
Project Euler 29 - Distinct Powers
https://projecteuler.net/problem=29

Pattern:
Set Deduplication, Exponent Arithmetic
"""


def distinct_powers(a_max: int, b_max: int) -> int:
	ans = set()
	for a in range(2, a_max+1):
		for b in range(2, b_max+1):
			ans.add(a**b)
	return len(ans)


# Example: a_max = 5, b_max = 5 -> 15
print(distinct_powers(5, 5))

# Answer: a_max = 100, b_max = 100
print(distinct_powers(100, 100))
