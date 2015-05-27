"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
import itertools
def factors(n):
	"""generate factors"""
	factList = [[div,n/div] for div in xrange(1,int(n**0.5)+1) if n%div ==0]
	sortReduce = reduce(list.__add__,factList)
	return list(set(sortReduce))

def factSum(n):
	return sum(factors(n)) - n

def is_abundant(n):
	if n<12:
		return False
	return factSum(n) > n

upper = 22056
abundants = {i for i in xrange(1,upper+1) if is_abundant(i)}

def is_abundant_sum(n):
	for i in abundants:
		if i > n:
			return False
		if (n-i) in abundants:
			return True
	return False

print sum(x for x in xrange(1,upper+1) if not is_abundant_sum(x))