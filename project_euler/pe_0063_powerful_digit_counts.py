"""
Project Euler 63 - Powerful Digit Counts
https://projecteuler.net/problem=63

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from math import log10

def powerful_digit_counts() -> int:
	cnt = 0
	for n in range(1, 22):
		for m in range(1, 10):
			if log10(m) - 1 + 1/n >= 0:
				cnt += 1
	return cnt


# Answer
print(powerful_digit_counts())
