"""
Project Euler 22 - Names Scores
https://projecteuler.net/problem=22

Using pe_0022_names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value
for each name, multiply this value by its alphabetical position in the list to obtain
a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a
score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

Pattern:
Sorting, String to Value Mapping, Weighted Sum
"""
from pathlib import Path
from typing import List


def load_names(filename: str) -> List[str]:
	text = Path(__file__).with_name(filename).read_text()
	return text.replace('"', '').split(',')

def char_worth(c: str) -> int:
	return ord(c.upper()) - ord('A') + 1

def worth(name: str) -> int:
	ans = 0
	for n in name:
		ans += char_worth(n)
	return ans

def names_scores(names: List[str]) -> int:
	ans = 0
	names.sort()
	for i, n in enumerate(names):
		score = worth(n) * (i+1)
		ans += score
	return ans

# Example: ["MARY", "PATRICIA", "LINDA"] -> 385
print(names_scores(["MARY", "PATRICIA", "LINDA"]))

# Answer
print(names_scores(load_names("pe_0022_names.txt")))
