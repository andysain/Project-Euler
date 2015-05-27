"""Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n**2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""

def euler(n):
	eq = n**2 + n + 41
	if eq < 0: return False
	return is_prime(eq)

def euler2(n):
	eq = n**2 - 79*n + 1601
	if eq < 0: return False
	return is_prime(eq)	

def myEuler(n,a,b):
	eq = n**2 + a*n + b
	if eq < 0: return False
	return is_prime(eq)

def is_prime(n):
	factList = [div for div in range(1,int(n**0.5)+1) if n%div == 0]
	if len(factList) == 1: return True
	else: return False

def primeList():
	primes = []
	n = 20
	factList = [div for div in range(1,int(n**0.5)+1) if n%div == 0]
	return [fact for fact in factList if fact==1]



def passCoeff(bound):
	maxPrimes = []
	count = 0
	for a in xrange(-bound,bound):
		for b in xrange(-bound,bound):
			n = 0
			while myEuler(n,a,b):
				n +=1
				count +=1
			maxPrimes.append((n-1,a,b))
	return max(maxPrimes)
				
bound = 1000
#n,a,b = passCoeff(bound)
#print a*b
print primeList()

