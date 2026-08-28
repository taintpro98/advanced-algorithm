"""
Project Euler 16 - Power Digit Sum
https://projecteuler.net/problem=16

Pattern:
Big Integer Arithmetic, Digit Manipulation
"""


def power_digit_sum(exponent: int) -> int:
	exp = 2 ** exponent
	ans = 0
	while exp > 0:
		digit = exp % 10
		ans += digit
		exp //= 10
	return ans


# Example: exponent = 15 -> 26  (2^15 = 32768)
print(power_digit_sum(15))

# Answer: exponent = 1000
print(power_digit_sum(1000))
