"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

def leap(year):
	if year%4 != 0: return False
	elif year%100 ==0 and year%400 != 0: return False
	else: return True

def yearDays(year):
	if leap(year): return 366
	else: return 365

def monthDays(year):
	days = [range(1,noMonthDays[M]+1) for M,month in enumerate(noMonthDays)]
	if leap(year):
		days[1].append(29)
	return reduce(list.__add__,days)

def days(yearStart,yearEnd):
	daysInYear = [monthDays(year) for year in range(yearStart,yearEnd+1)]
	#print [range(1,day+1) for day in daysInYear]
	list_ = reduce(list.__add__,daysInYear)
	monthStart = startOfMonth(list_)
	return dayName(monthStart)

def startOfMonth(daysList):
	return [d for d,day in enumerate(daysList) if day ==1]

def dayName(monthStart):
	return sum([1 for d in monthStart if daysofWeek[d] == 'Sun'])

noMonthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
daysofWeek = ['Wed', 'Thu','Fri','Sat','Sun','Mon','Tue',]*5300
def First1901():
	days1900 = yearDays(1900)
	print daysofWeek[days1900]
	
#print First1901()
print days(1901,2000)
#print monthDays(1901)