"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

def splitNum(a):
	return [int(dig) for dig in str(a)]

def exp(n):
	upper = upperBound(n)
	l = []
	for a in xrange(2,upper):
		dig = splitNum(a)
		powersList = map(lambda x: x**n,dig)
		powerSum = sum(powersList)
		if a == powerSum:
			l.append(a)
	return sum(l)

def upperBound(power):
	maxPower = 9**power
	maxValLength = len(str(maxPower*len(str(maxPower))))
	return maxValLength*maxPower

print exp(5)

#print upperBound(5)