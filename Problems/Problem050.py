"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""
import math
import cProfile
#limit = 1*10**4
limit = 7879
oneMill = 1*10**8
#print limit

def primeGen(n):
	"generates list of primes"
	sieve = [True]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False]*((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def is_prime(x):
	if x > 1:
		if x == 2:
			return True
		if x%2 == 0:
			return False
		for div in xrange(3,int(x**0.5)+1,2):
			if x%div == 0:
				return False
		return True
	return False

def nextSum(i=0,max_len =0,max_sum=0,sums = []):
	if i <= primeLen:
		for n in xrange(0,primeLen-i):
			slice_len = primeLen - n - i
			if slice_len > max_len:
				slice_ = primeList[i:primeLen-n]
				slice_sum = sum(slice_)
				if is_prime(slice_sum) and slice_sum < oneMill: 
					if slice_len> max_len and slice_len> max_len:
						max_sum = slice_sum
						max_len = slice_len
						sums.append((slice_len,slice_sum))
					max_len = slice_len
		nextSum(i+1,max_len,max_sum,sums)
	return max(sums)

primeList = primeGen(limit)
primeLen = len(primeList)
print nextSum()

