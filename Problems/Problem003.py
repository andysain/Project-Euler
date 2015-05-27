"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def isprime(x):
	if x > 1:
		if x == 2:
			return True
		if x % 2 == 0:
			return False
		for cur in range(3,int(x**0.5)+1,2):
			if x % cur == 0:
				return False
		return True
	return False
	#return [[y,x/y] for y in range(1,int(x**0.5)) if x%y==0]	

def factors(num):
	factorlist = reduce(list.__add__,[[x,num/x] for x in range(1,int(num**0.5)) if num%(x) ==0])
	return max([fact for fact in factorlist if isprime(fact)])


#print factors(13195)
print factors(600851475143)