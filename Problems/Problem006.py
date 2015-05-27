"""
The sum of the squares of the first ten natural numbers is,
	1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_sq(n):
	return sum([x**2 for x in range(n+1)])

def sq_sum(n):
	return sum([x for x in range(n+1)])**2

def diff(n):
	#return sum_sq(n)
	return sq_sum(n) - sum_sq(n)

print diff(100)