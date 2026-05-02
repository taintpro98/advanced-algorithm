"""
Codeforces 514A - Chewbacca and Number
https://codeforces.com/problemset/problem/514/A

Pattern:
Greedy, Implementation
"""
import sys
from math import gcd
from collections import defaultdict, deque

input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('inf')

def minInvert(t: int):
    return min(t, abs(9-t))

def solve():
	x = int(input())
	ans = 0
	ten = 1
	while x:
		l = x % 10
		l = minInvert(l)
		if x < 10 and l == 0:
			l = 9
		ans += l*ten
		ten *= 10
		x //= 10
	print(ans)

solve()
