"""
Project Euler 32 - Pandigital Products
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Pattern:
Pandigital Numbers, Brute Force Enumeration, Set Deduplication
"""


def pandigital_products_sum() -> int:
	ans = set()
	def backtrack(size: int, a: int, cur_perm: str, visited: list[bool]):
		nonlocal ans
		if len(cur_perm) == size:
			c = a * int(cur_perm)
			s = str(c)
			if len(s) == 4:
				valid = True
				for char in s:
					if char == '0' or visited[int(char)]:
						valid = False
						break
				if not valid:
					return
				dedup = set()
				for char in s:
					dedup.add(char)
				if len(dedup) < 4:
					return
				ans.add(c)
		for t in range(1, 10):
			if not visited[t]:
				visited[t] = True
				backtrack(size, a, cur_perm + str(t), visited)
				visited[t] = False
	visited = 10 * [False]
	for a in range(2, 9):
		visited[a] = True
		backtrack(4, a, '', visited)
		visited[a] = False
	for x in range(1, 10):
		visited[x] = True
		for y in range(1, 10):
			if x == y:
				continue
			visited[y] = True
			backtrack(3, 10*x + y, '', visited)
			visited[y] = False
		visited[x] = False
	return sum(ans)



# Answer
print(pandigital_products_sum())
