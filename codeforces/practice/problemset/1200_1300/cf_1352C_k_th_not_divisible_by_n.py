"""
Codeforces 1352C - K-th Not Divisible by n
https://codeforces.com/problemset/problem/1352/C

Pattern:
Binary Search, Math
"""
import sys
from math import gcd
from collections import defaultdict, deque

input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('inf')


def solve():
	n, k = map(int, input().split())
	c = k // (n-1)
	r = k % (n-1)
	ans = c * n + r
	if r == 0:
		ans -= 1
	print(ans)


T = int(input())
for _ in range(T):
	solve()
