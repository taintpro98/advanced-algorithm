"""
Project Euler 37 - Truncatable Primes
https://projecteuler.net/problem=37

Sum of the first `count` primes that stay prime when digits are removed both
left to right and right to left. Note: 2, 3, 5 and 7 are not considered
truncatable primes.

Pattern:
Primality Testing, Digit Truncation
"""
def is_prime(p: int) -> bool:
	if p < 2:
		return False
	d = 2
	while d*d<=p:
		if p%d == 0:
			return False
		d += 1
	return True

def is_truncatable_prime(p: int) -> bool:
	if p < 10:
		return False
	s = str(p)
	check = set()
	for i in range(1, len(s)):
		check.add(int(s[:i]))
		check.add(int(s[i:]))
	check.add(p)
	for t in check:
		if not is_prime(t):
			return False
	return True

def sum_of_truncatable_primes(count: int) -> int:
	cnt = 0
	p = 23
	ans = 0
	while cnt < count:
		if is_truncatable_prime(p):
			cnt += 1
			ans += p
		p += 1
	return ans


# Example: count = 2 -> 60  (23 and 37)
# print(sum_of_truncatable_primes(2))

# Answer: count = 11  (there are only eleven)
print(sum_of_truncatable_primes(11))
