"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(x):
	if x > 1:
		if x == 2:
			return True
		elif x%2 == 0:
			return False
		for cur in range(3,x,2):
			if x%cur == 0:
				return False
		return True
	return False

def primeN(nth):
	x = 3
	primes = [2]
	while True and len(primes) < nth-1:
		x += 2 
		if is_prime(x): 
			primes.append(x)
	return x

print primeN(10001)