"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""
from itertools import permutations
import cProfile

digits = "123456789"
#digits = "123"
digList = list(digits)

def pandigital():
	return (list(p) for n in xrange(4,9) for p in permutations(digits,n))
	#return (int(''.join(p)) for n in xrange(1,10) for p in permutations(digits,n))

def factors(n):
	"""wrtie factors if pandigital"""
	nInt = int(n)
	panFactors = []
	print nInt
	for div in xrange(1,int(nInt**0.5)+1):
		if nInt%div ==0:
			x = ''.join(map(str,[nInt,nInt/div,div]))
			if is_pandigital(x):
				panFactors.append([nInt,nInt/div,div])
	return panFactors
	#return [[nInt,nInt/div,div] for div in xrange(1,int(nInt**0.5)+1) if nInt%div ==0 and is_pandigital(''.join(map(str,[nInt,nInt/div,div])))]

def is_pandigital(n):
	"""determines if number is pandigital"""
	nStr = str(n)
	return sorted(nStr) == digList

def panChecker():
	for p in pandigital():
		x = ''.join(p)
		print p
		for n in factors(x): 
			print n	

#print cProfile.run('panChecker()')
print panChecker()