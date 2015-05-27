"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

import itertools as it

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def split(n):
	digits = [x for x in str(n)]
	return len(digits), digits

def circles(n):
	n_len, n = split(n)
	c = set()
	for i in range(n_len):
		popped = n.pop(0)
		n.append(popped)
		newNum = int(''.join(n))
		c.add(newNum)
	return c

def evenDig(x):
	return any(i in '24680' for i in str(x) if str(x)<1)

def circularValues(x):
	if evenDig(x):
		return None, False
	else:
		circleVals = circles(x)
		return circleVals, all(n in primeSet for n in circleVals)

def circular():
	circleSet = set()
	for x in primeSet:
		circ, is_circular = circularValues(x)
		if is_circular and x not in circleSet:
			circleSet.update(circ)
	return circleSet

limit = 1000000
primeSet = set(rwh_primes1(limit))
print len(circular())
