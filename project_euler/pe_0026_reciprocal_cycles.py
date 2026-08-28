"""
Project Euler 26 - Reciprocal Cycles
https://projecteuler.net/problem=26

Pattern:
Long Division Simulation, Cycle Detection, Multiplicative Order
"""
def euler_function(n: int) -> int:
	p = 2
	ans = n
	while p*p <= n:
		if n % p == 0:
			ans = ans * (p-1) // p
			while n % p == 0:
				n //= p
		p += 1
	if n > 1:
		ans = ans * (n-1) // n
	return ans

def cycle_length(denominator: int) -> int:
	while denominator % 2 == 0:
		denominator //= 2
	while denominator % 5 == 0:
		denominator //= 5
	if denominator == 1:
		return 0
	euler = euler_function(denominator)
	for t in range(1, denominator + 1):
		if euler % t == 0 and pow(10, t, denominator) == 1:
			return t
	return 0

def longest_recurring_cycle_below(limit: int) -> int:
	ans = 2
	max_len = 0
	for d in range(2, limit):
		cycle = cycle_length(d)
		if cycle > max_len:
			max_len = cycle
			ans = d
	return ans


# Example: limit = 10 -> 7  (1/7 = 0.(142857), a 6-digit cycle)
print(longest_recurring_cycle_below(10))

# Answer: limit = 1000
print(longest_recurring_cycle_below(1000))
