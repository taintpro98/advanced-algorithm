"""
Project Euler 20 - Factorial Digit Sum
https://projecteuler.net/problem=20

Pattern:
Big Integer Arithmetic, Digit Manipulation
"""


def factorial_digit_sum(n: int) -> int:
	factor = 1
	for i in range(1, n+1):
		factor *= i
	ans = 0
	while factor > 0:
		digit = factor % 10
		ans += digit
		factor //= 10
	return ans


# Example: n = 10 -> 27  (10! = 3628800)
print(factorial_digit_sum(10))

# Answer: n = 100
print(factorial_digit_sum(100))
