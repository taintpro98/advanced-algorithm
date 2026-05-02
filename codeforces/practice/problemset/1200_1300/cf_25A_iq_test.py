"""
Codeforces 25A - IQ Test
https://codeforces.com/problemset/problem/25/A

Pattern:
Brute Force
"""
import sys
from math import gcd
from collections import defaultdict, deque

input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('inf')


def solve():
	n = int(input())
	nums = list(map(int, input().split()))
	for t in range(2, n+1):
		if nums[t-1] % 2 != nums[t-2] % 2:
			if t > 2:
				print(t)
				return
			else:
				if nums[t-1]%2 == nums[t]%2:
					print(1)
					return
				else:
					print(2)
					return

solve()
