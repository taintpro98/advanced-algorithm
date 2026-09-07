"""
Project Euler 41 - Pandigital Prime
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

Pattern:
Pandigital Numbers, Primality Testing, Permutations
"""
def is_prime(p: int) -> bool:
	if p <= 1:
		return False
	if p == 2:
		return True
	if p % 2 == 0:
		return False
	d = 3
	while d * d <= p:
		if p % d == 0:
			return False
		d += 2
	return True

def largest_pandigital_prime(max_digits: int) -> int:
	ans = 0
	def backtrack(n: int, cur_perm: str, visited: list[bool]) -> int:
		nonlocal ans
		if ans != 0:
			return ans
		if len(cur_perm) == n:
			p = int(cur_perm)
			if is_prime(p) and p > ans:
				ans = p
				return ans
		for i in range(n, 0, -1):
			if not visited[i]:
				visited[i] = True
				ans = backtrack(n, cur_perm + str(i), visited)
				visited[i] = False
		return ans

	for t in [x for x in [7, 4] if x <= max_digits]:
		cur_perm = ''
		visited = (t+1) * [False]
		ans = backtrack(t, cur_perm, visited)
		if ans != 0:
			return ans
	return ans


# Example: max_digits = 4 -> 4231
print(largest_pandigital_prime(4))

# Answer
print(largest_pandigital_prime(9))
