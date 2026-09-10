"""
Project Euler 94 - Almost Equilateral Triangles
https://projecteuler.net/problem=94

It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has an
area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral
side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""
def cal(x: int, y: int) -> tuple[int]:
	return (2*x + 3*y, x + 2*y)

def almost_equilateral_perimeters_sum(max_perimeter: int) -> int:
	x, y = 2, 1
	ans = 0
	p = 0
	while p <= max_perimeter:
		ans += p
		x, y = cal(x, y)
		if x % 3 == 1:
			p = 2*x + 2
		elif x % 3 == 2:
			p = 2*x - 2
	return ans



# Example: max_perimeter = 16 -> 16 (only the 5-5-6 triangle)
print(almost_equilateral_perimeters_sum(16))

# Answer
print(almost_equilateral_perimeters_sum(1000000000))
