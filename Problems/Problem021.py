"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def factors(n):
	factSubList = [[div,n/div] for div in range(1,int(n**0.5)+1) if n%div == 0]
	factList = sorted(reduce(list.__add__,factSubList))
	return factList
	return [n for n in range(1,int(n**0.5)+1)]

def divSum(n):
	return sum(factors(n))-n

def amicable(n):
	divSum_ = divSum(n)
	amic1 = divSum(divSum_)
	amic2 = divSum(amic1)
	# return divSum_, amic1
	return divSum_ == amic2 and n == amic1 and amic1 != amic2

print sum([i for i in range(1,10001) if amicable(i)])

amicables = [1, 6, 28, 220, 284, 496, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 8128]
for i in amicables:
	print amicable(i)