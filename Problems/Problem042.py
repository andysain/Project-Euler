"""The nth term of the sequence of triangle numbers is given by, t(n) = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?"""
import csv

letters = [None,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
wordFile = open('words.txt','r')

def words(inFile):
	reader = csv.reader(inFile)
	for r in reader:
		triangleWords = [word for word in r if points(word) in triList]
	return len(triangleWords)
	
def points(word):
	return sum([letters.index(L) for L in word])

def triangle(n,upper, triList = []):
	tri = n*(n+1)/2
	if tri<upper:
		triList.append(tri)
		triangle(n+1,upper,triList)
	return triList

upper = 364
triList = triangle(1,upper)

print words(wordFile)

