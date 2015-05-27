"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

num2text = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine', 10: 'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen', 20: 'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

def hundreds(n):
	return num2text[n] + ' hundred and'
	#else: return num2text[n] + ' hundred and'

def split(num):
	numStr = str(num)
	lenStr = len(numStr)
	if lenStr>=2:
		if int(numStr[-2]) == 1 or int(numStr[-1]) == 0:# or int(numStr[-1]) == 0:
			numStrList = map(int,numStr[0:-2])
			numStrList.append(int(numStr[-2:]))
			return lenStr,numStrList
		else:
			return lenStr,map(int,numStr)
	elif lenStr ==1:
		return 1, [num]

def convert(n):
	numLen, digits = split(n)
	text = []
	for i,num in enumerate(digits):
		if (num == 0):
			pass
		elif numLen - i == 4:
			text.append('one thousand')
		elif numLen - i == 3:
			text.append(hundreds(num))
		elif (numLen - i == 2 and 0 < num < 10):
			text.append(num2text[num*10])
		else:
			text.append(num2text[num])
	textStr = ' '.join(text)
	if textStr[-3:] == 'and':
		return textStr.replace(' and','')
	else:
		return textStr


def iter_(upper):
	sum_ = 0
	for num in range(1,upper+1):
		print convert(num)
		strLen = len(convert(num).replace(' ',''))
		sum_ += strLen
	return sum_
	#textList = [len(convert(num)) for num in range(1,upper+1)]
	#return sum(textList)
	#return sorted(textList, key = len)

#print convert(125)
print iter_(1000)