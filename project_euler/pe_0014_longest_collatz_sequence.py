"""
Project Euler 14 - Longest Collatz Sequence
https://projecteuler.net/problem=14

Pattern:
Simulation, Memoization
"""
def collatz_chain_length(n: int) -> int:
	if n <= 1:
		return 1
	count = 1
	while n > 1:
		count += 1
		if n % 2 == 0:
			n //= 2
		else:
			n = 3*n + 1
	return count

def longest_collatz_start_under(limit: int) -> int:
	ans = 0
	max_len = 1
	for t in range(1, limit):
		clen = collatz_chain_length(t)
		if clen > max_len:
			max_len = clen
			ans = t
	return ans


# Example: limit = 15 -> 9  (chain of 20 terms)
print(longest_collatz_start_under(15))

# Answer: limit = 1000000
print(longest_collatz_start_under(1000000))
