"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""
import math
import time

def factorial(upper):
	a = 1
	fact = 1
	while a<= upper:
		fact *= a
		yield fact
		a+=1

def split(n):
	return [int(d) for d in str(n)]

def upperLimit(lenFact1):
	"""find the upper limit of factorials
	recusive function that multiplies lenght
	by 9!"""
	fact2 = lenFact1*fact9
	lenfact2 = len(str(fact2))
	maxFact = lenfact2*fact9
	lenMax = len(str(maxFact))
	if lenMax == lenfact2: 
		return maxFact
	else:
		return upperLimit(lenMax)

def factSum(n):
	digits = split(n)
	return sum(map(lambda x: math.factorial(x),digits))

def equality(n):
	return n == factSum(n)

def iterate(upper):
	return [n for n in xrange(3,upper) if equality(n)]
		

fact9 = math.factorial(9)
lenght9fact = len(str(fact9))
upper = upperLimit(lenght9fact)
print sum(iterate(upper))
