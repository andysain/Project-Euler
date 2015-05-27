"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

import decimal

def rep(den):
	d = decimal.Decimal(den)
	frac = 1/d
	print d,frac
	if len(str(frac))> 25:
		return is_int(d)
	else:
		return frac

def is_int(n):
	a = 10
	while not (((a-1)/n)*a)%1 == 0:
		print a, (((a-1)/n)*a)
		a *=10
	return a

a = 10000000000000
n = 17.0
print a, a/n, 1/n, (a/n - 1/n)%1

#for i in xrange(1,20):
#	print i,rep(i), 1/decimal.Decimal(i)
