"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def product(trip):
	a,b,c = trip
	return a*b*c

def tripletSum(trip,val):
	a,b,c = trip
	return a + b + c == val

def pyth(trip):
	a,b,c = trip
	return a**2 + b**2 == c**2

def triplets(n,val):
	for a in range(2,n+1):
		for b in range(a+1,n+1):
			c = int((a**2+b**2)**0.5)
			trip = (a,b,c)
			if pyth(trip) and tripletSum(trip,val):
				return product(trip)

print triplets(500,1000)