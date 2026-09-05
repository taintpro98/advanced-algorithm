"""
Project Euler 17 - Number Letter Counts
https://projecteuler.net/problem=17

Letters used writing out every number from 1 to `limit` inclusive, ignoring
spaces and hyphens. British usage: 342 is "three hundred and forty-two" (23
letters), 115 is "one hundred and fifteen" (20 letters).

Pattern:
Number to Words, Simulation
"""
LETTERS = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety'
}

def number2letters(n: int) -> str:
	if n in LETTERS:
		return LETTERS[n]
	if n < 100:
		last = n % 10
		first = n - last
		return LETTERS[first] + LETTERS[last]
	if n == 1000:
		return 'onethousand'
	if n % 100 == 0:
		return LETTERS[n//100] + 'hundred'
	last = n % 100
	first = n - last
	return LETTERS[n//100] + 'hundred' + 'and' + number2letters(last)

def count_number_letters(limit: int) -> int:
	ans = 0
	for i in range(1, limit+1):
		letters = number2letters(i)
		ans += len(letters)
	return ans


# Example: limit = 5 -> 19  (one, two, three, four, five)
print(count_number_letters(5))

# Answer: limit = 1000
print(count_number_letters(1000))
