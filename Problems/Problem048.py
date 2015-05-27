"""The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000."""

def selfExp(upper):
	a = 1
	#yield a**a
	while a <=upper:
		yield a**a
		a +=1

def expSum(upper):
	return sum([i for i in selfExp(upper)])

def last_Ndigits(N,upper):
	sumVal = expSum(upper)
	stringVal = str(sumVal)
	return stringVal[-N:]

print last_Ndigits(10,1000)