"""
Project Euler 19 - Counting Sundays
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November.
  All the rest have thirty-one, saving February alone,
  which has twenty-eight, rain or shine, and on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

Pattern:
Calendar Arithmetic, Day-of-Week Cycling, Leap Year Rules
"""
def is_leap(year: int) -> bool:
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def count_days(year: int, month: int) -> int:
	if month == 2:
		if is_leap(year):
			return 29
		else:
			return 28
	months = {
		1: 31,
		3: 31,
		4: 30,
		5: 31,
		6: 30,
		7: 31,
		8: 31,
		9: 30,
		10: 31,
		11: 30,
		12: 31
	}
	return months.get(month, 0)

def counting_sundays(start_year: int, end_year: int) -> int:
	cnt = 0
	cur = 0
	for y in range(start_year, end_year+1):
		for m in range(1, 13):
			if y == 1900 and m == 1:
				cur = 1
			else:
				if m > 1:
					cur += count_days(y, m-1)
				else:
					cur += count_days(y, 12)
			if cur % 7 == 0:
				cnt += 1
	return cnt


# Example: Sundays on the 1st during 1900 only
print(counting_sundays(1900, 1900))

# Answer: 1901 to 2000
print(counting_sundays(1901, 2000))
