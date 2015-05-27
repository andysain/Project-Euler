"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def products(dig):
	numList = range(10**(dig-1),10**dig)
	return max([n1*n2 for n1 in numList for n2 in numList if ispal(n1*n2)])

def ispal(num):
	return str(num) == str(num)[::-1]


print products(3)
#print ispal(9009)