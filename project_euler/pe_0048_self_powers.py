"""
Project Euler 48 - Self Powers
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Pattern:
Modular Exponentiation
"""
MOD = 10**10

def self_power(n: int) -> int:
	ans = 1
	for _ in range(n):
		ans *= n
		ans %= MOD
	return ans

def self_powers(n: int) -> int:
	ans = 0
	for t in range(1, n+1):
		ans += self_power(t)
		ans %= MOD
	return ans


# Example: n = 10 -> 10405071317
print(self_powers(10))

# Answer
print(self_powers(1000))
