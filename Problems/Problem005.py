"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def fact(x,div):
	for n in range(11,div+1):
		if x%n != 0:
			return False
	return True

def init(div):
	x = 2520
	while not fact(x,div):
		x += 2520
	yield x

for a in init(20):
	print a