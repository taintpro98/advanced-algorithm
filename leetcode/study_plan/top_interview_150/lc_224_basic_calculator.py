"""
LeetCode 224 - Basic Calculator
https://leetcode.com/problems/basic-calculator/

Pattern:
Stack
"""
import re

class Solution:
	def is_int(s: str) -> bool:
		if s[0] == '-':
			return s[1:].isdigit()
		return s.isdigit()

	def calculate(self, s: str) -> int:
		res: list[str] = re.findall(r'\d+|[+\-()]', s.replace(' ', ''))
		tokens: list[str] = []
		idx = 0
		while idx < len(res):
			t = res[idx]
			if t == '-' and (idx == 0 or res[idx-1] == '('):
				tokens += ['0', '-']
			else:
				tokens.append(res[idx])
			idx += 1
		stack = []
		post_fix: list[str] = []
		ops = set(['+', '-'])
		for t in tokens:
			if Solution.is_int(t):
				post_fix.append(t)
			elif t == '(':
				stack.append(t)
			elif t == ')':
				while stack and stack[-1] != '(':
					post_fix.append(stack.pop())
				if stack:
					stack.pop()
			else:
				while stack and stack[-1] in ops:
					post_fix.append(stack.pop())
				stack.append(t)
		while stack:
			post_fix.append(stack.pop())
		# calculate post fix
		for p in post_fix:
			if Solution.is_int(p):
				stack.append(p)
			else:
				if len(stack) == 0:
					return None
				b = int(stack.pop())
				if stack:
					a = int(stack.pop())
				else:
					a = 0
				if p == '+':
					stack.append(a + b)
				else:
					stack.append(a - b)
		return int(stack[-1])

s = "- (3 - (- (4 + 5) ) )"
sol = Solution()
print(sol.calculate(s))
