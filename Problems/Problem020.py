"""n! means n x (n - 1) x ... x 3 x 2 x 1
For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def factorial(upper):
	n,fact= 1,1
	while n <=upper:
		fact = n*fact
		yield fact
		n +=1

def factVal(upper):
	return [n for n in factorial(upper)][-1]

def split(n):
	fact = str(factVal(n))
	digits = [d for d in fact]
	return sum(map(int,digits))

upper = 100000
print split(upper)