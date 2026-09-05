"""
Project Euler 4 - Largest Palindrome Product
https://projecteuler.net/problem=4

Largest palindrome made from the product of two numbers of `digits` digits.

Pattern:
Palindrome Check, Brute Force Search
"""
def is_palindrome(n: int) -> bool:
	s = str(n)
	return s == s[::-1]

def largest_palindrome_product(digits: int) -> int:
	bound = 10**(digits - 1)
	ans = 1
	for i in range(bound, 10 * bound):
		for j in range(bound, 10 * bound):
			check = i * j
			if is_palindrome(check) and check > ans:
				ans = check
	return ans


# Example: digits = 2 -> 9009  (91 x 99)
print(largest_palindrome_product(2))

# Answer: digits = 3
print(largest_palindrome_product(3))
