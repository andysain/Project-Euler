"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?"""

nameFile = open('Problem022_names.txt','r')
nameList = sorted([name.replace('"','').split(',') for name in nameFile][0])
chars = ['None','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	

def namePoints(name):
	return sum([chars.index(letter) for letter in name])

def names(nameList):
	return sum([(i+1)*namePoints(name) for i,name in enumerate(nameList)])
		
print names(nameList)