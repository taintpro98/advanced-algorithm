"""
Project Euler 21 - Amicable Numbers
https://projecteuler.net/problem=21

Pattern:
Divisor Sum, Number Theory
"""
def divisors_sum(n: int) -> int:
	if n <= 1:
		return 1
	d = 1
	ans = 0
	while d * d <= n:
		if n % d == 0:
			f = n // d
			if d == f:
				ans += d
			else:
				ans += d + f
		d += 1
	return ans

def sum_of_amicable_numbers_below(limit: int) -> int:
	ans = 0
	amiset = set()
	for x in range(2, limit):
		if x in amiset:
			continue
		y = divisors_sum(x) - x
		if divisors_sum(y) == x + y:
			amiset.add(x)
			amiset.add(y)
			if x != y:
				ans += x + y
	return ans


# Example: limit = 300 -> 504  (the pair 220, 284)
print(sum_of_amicable_numbers_below(300))

# Answer: limit = 10000
print(sum_of_amicable_numbers_below(10000))
