"""
ID: pranav.19
LANG: PYTHON2
TASK: friday
"""
N = 0
with open("friday.in", "r") as f:
	N = int(f.readline())

def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

# Get the number of days
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
startYear = 1900
endYear = 1900+N-1
numDays = -1
for year in range(startYear, endYear+1):
	if isLeapYear(year):
		numDays += 366
	else:
		numDays += 365

marks = [0, 0, 0, 0, 0, 0, 0]
"""
0 - Saturday
1 - Sunday
2 - Monday
3 - Tuesday
4 - Wednesday
5 - Thursday
6 - Friday
"""
current13 = 0 # Saturday
currentYear = 1900
currentMonth = 0 # January

while currentYear <= endYear:
	marks[current13 % 7] += 1
	if isLeapYear(currentYear) and currentMonth == 1:
		current13 += 1
	current13 += monthDays[currentMonth]
	currentMonth += 1

	if currentMonth > 11:
		currentMonth = 0
		currentYear += 1

		
with open("friday.out", "w") as f:
	phrase = ""
	for i in marks:
		phrase += str(i)+" "
	phrase = phrase[0:len(phrase)-1]+"\n"
	f.write(phrase)