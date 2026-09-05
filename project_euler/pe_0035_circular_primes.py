"""
Project Euler 35 - Circular Primes
https://projecteuler.net/problem=35

Pattern:
Sieve of Eratosthenes, Digit Rotation
"""
def get_rotations(n: int) -> list[int]:
	str_n = str(n)
	ans = set()
	for i in range(len(str_n)):
		rotated = str_n[i:] + str_n[:i]
		ans.add(int(rotated))
	return list(ans)

def count_circular_primes_below(limit: int) -> int:
	primes = (limit + 1) * [True]
	primes[0] = primes[1] = False
	for p in range(2, limit + 1):
		if primes[p]:
			t = 2 * p
			while t <= limit:
				primes[t] = False
				t += p
	cnt = 0
	for p in range(len(primes)):
		if primes[p]:
			rotations = get_rotations(p)
			pick = True
			for r in rotations:
				if not primes[r]:
					pick = False
					break
			if pick:
				cnt += len(rotations)
				for r in rotations:
					primes[r] = False
	return cnt


# Example: limit = 100 -> 13  (2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97)
print(count_circular_primes_below(100))

# Answer: limit = 1000000
print(count_circular_primes_below(1000000))
