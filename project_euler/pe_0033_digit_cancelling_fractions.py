"""
Project Euler 33 - Digit Cancelling Fractions
https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

Pattern:
Brute Force Enumeration, Fraction Reduction, GCD
"""
from math import gcd

def is_valid(a: int, b: int) -> int:
	if a % 10 == 0 and b % 10 == 0:
		return -1
	s1 = str(a)
	s2 = str(b)
	if s1[0] == s2[0] or s1[0] == s2[1]:
		return int(s1[0])
	if s1[1] == s2[0] or s1[1] == s2[1]:
		return int(s1[1])
	return -1

def cancel(common: int, ab: int) -> int:
	if (ab-common) % 10 == 0:
		return ab // 10
	if ab // 10 == common:
		return ab % 10
	return -1

def digit_cancelling_denominator() -> int:
	fractions = []
	for a in range(10, 99):
		for b in range(a+1, 100):
			common = is_valid(a, b)
			if common != -1:
				d = gcd(a,b)
				if d == 1:
					continue
				a1, b1 = cancel(common, a), cancel(common, b)
				d1 = gcd(a1, b1)
				if (a // d, b // d) == (a1 // d1, b1 // d1):
					fractions.append((a, b))
	if len(fractions) != 4:
		return -1
	num = den = 1
	for (a, b) in fractions:
		num *= a
		den *= b
	d = gcd(num, den)
	return den // d

# Answer
print(digit_cancelling_denominator())
