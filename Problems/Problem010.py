"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

def is_prime(n):
	if n > 1:
		if n == 2:
			return True
 		elif n % 2 == 0:
			return False
		for div in range(3,n,2):
			if n%div == 0:
				return False
		return True
	return False

def primeGen(maxVal):
	n = 3
	while n < maxVal:
		if is_prime(n):
			yield n
		n+=2

def primeAdd(maxVal):
	primeList = [prime for prime in primeGen(maxVal)]
	primeList.insert(0,2)
	return sum(primeList)

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

print sum(rwh_primes(2000000))

#print primeAdd(10)
#print len(str(2**500500))