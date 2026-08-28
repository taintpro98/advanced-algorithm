"""
Project Euler 12 - Highly Divisible Triangular Number
https://projecteuler.net/problem=12

Pattern:
Divisor Counting, Prime Factorization
"""
def count_divisors(n: int) -> int:
	if n == 0 or n == 1:
		return 1
	p = 2
	ans = 1
	while p*p <= n:
		if n % p == 0:
			cnt = 0
			while n % p == 0:
				cnt += 1
				n //= p
			ans *= (cnt + 1)
		p += 1
	if n > 1:
		ans *= 2
	return ans

def first_triangle_number_with_divisors_over(count: int) -> int:
	t = 1
	step = 2
	while count_divisors(t) <= count:
		t += step
		step += 1
	return t



# Example: count = 5 -> 28  (divisors: 1, 2, 4, 7, 14, 28)
print(first_triangle_number_with_divisors_over(5))

# Answer: count = 500
print(first_triangle_number_with_divisors_over(500))
