"""
Project Euler 36 - Double-base Palindromes
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Pattern:
Palindromes, Base Conversion
"""
def is_palindromic(s: str) -> bool:
	if len(s) <= 1:
		return True
	n = len(s)
	for i in range(0, (n + 1) // 2):
		if s[i] != s[n-1-i]:
			return False
	return True

def double_base_palindromes_sum(limit: int) -> int:
	ans = 0
	t = 1
	while True:
		s = str(t)
		p1 = int(s + s[::-1])
		p2 = int(s + s[:-1][::-1])
		if p1 >= limit and p2 >= limit:
			break
		if p1 < limit and is_palindromic(bin(p1)[2:]):
			ans += p1
		if p2 < limit and is_palindromic(bin(p2)[2:]):
			ans += p2
		t += 1
	return ans


# Answer
print(double_base_palindromes_sum(1000000))
