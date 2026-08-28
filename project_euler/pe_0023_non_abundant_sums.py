"""
Project Euler 23 - Non-Abundant Sums
https://projecteuler.net/problem=23

Pattern:
Divisor Sum, Sieve, Subset Sum
"""
def is_abundant(n: int) -> bool:
	d = 2
	divisors_sum = 1
	while d * d <= n:
		if n % d == 0:
			f = n // d
			if d == f:
				divisors_sum += d
			else:
				divisors_sum += d + f
		d += 1
	return divisors_sum > n

def sum_of_non_abundant_sums_below(limit: int) -> int:
	ans = 1
	abundants_set = set()
	for t in range(2, limit):
		if is_abundant(t):
			abundants_set.add(t)
		isable = False
		for a in abundants_set:
			if t - a in abundants_set:
				isable = True
		if not isable:
			ans += t
	return ans




# Example: limit = 24 -> 276  (24 is the smallest sum of two abundant numbers, so 1..23 all count)
print(sum_of_non_abundant_sums_below(24))

# Answer: limit = 28124  (every integer above 28123 is a sum of two abundant numbers)
print(sum_of_non_abundant_sums_below(28124))
