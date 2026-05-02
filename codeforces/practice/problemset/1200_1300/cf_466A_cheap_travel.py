"""
Codeforces 466A - Cheap Travel
https://codeforces.com/problemset/problem/466/A

Pattern:
Implementation
"""
import sys
from math import gcd
from collections import defaultdict, deque

input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('inf')


def solve():
	n, m, a, b = map(int, input().split())
	if m * a <= b:
		print(n*a)
		return
	nums_buy = n // m
	ans = nums_buy * b
	remain = n - nums_buy * m
	single_buys = remain * a
	ans += min(single_buys, b)
	print(ans)

solve()
