"""
Project Euler 43 - Sub-string Divisibility
https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

d_2 d_3 d_4  = 406 is divisible by 2
d_3 d_4 d_5  = 063 is divisible by 3
d_4 d_5 d_6  = 635 is divisible by 5
d_5 d_6 d_7  = 357 is divisible by 7
d_6 d_7 d_8  = 572 is divisible by 11
d_7 d_8 d_9  = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
PRIMES = [2,3,5,7,11,13,17]
def is_valid(n: int) -> bool:
	s = str(n)
	for t in range(1, 8):
		if int(s[t:t+3]) % PRIMES[t-1] != 0:
			return False
	return True

def substring_divisible_pandigitals_sum() -> int:
	ans = 0
	def backtrack(cur_perm: str, visited: list[bool]):
		nonlocal ans
		if len(cur_perm) == 10:
			n = int(cur_perm)
			if is_valid(n):
				ans += n
			return
		for t in range(0, 10):
			if len(cur_perm) == 0 and t == 0:
				continue
			if not visited[t]:
				visited[t] = True
				backtrack(cur_perm + str(t), visited)
				visited[t] = False
	visited = [False] * 10
	backtrack('', visited)
	return ans


# Answer
print(substring_divisible_pandigitals_sum())
