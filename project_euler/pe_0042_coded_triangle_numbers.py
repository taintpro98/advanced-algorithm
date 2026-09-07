"""
Project Euler 42 - Coded Triangle Numbers
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by t_n = n(n+1)/2;
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a
triangle number then we shall call the word a triangle word.

Using pe_0042_words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

Pattern:
Triangle Numbers, String to Value Mapping, Set Lookup
"""
from pathlib import Path
from typing import List
from math import isqrt

def load_words(filename: str) -> List[str]:
	text = Path(__file__).with_name(filename).read_text()
	return text.replace('"', '').split(',')

def is_triangle(n: int) -> bool:
	x = isqrt(2*n)
	return x*(x+1) == 2*n

def count_triangle_words(words: List[str]) -> int:
	cnt = 0
	for w in words:
		s = 0
		for c in w:
			s += (ord(c.upper()) - ord('A') + 1)
		if is_triangle(s):
			cnt += 1
	return cnt


# Example: ["SKY", "ABC", "A"] -> 3
print(count_triangle_words(["SKY", "ABC", "A"]))

# Answer
print(count_triangle_words(load_words("pe_0042_words.txt")))
