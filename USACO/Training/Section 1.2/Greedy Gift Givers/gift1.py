"""
ID: pranav.19
LANG: PYTHON2
TASK: gift1
"""
from math import floor

input = []
with open("gift1.in", "r") as f:
	input = f.readlines()

NP = int(input[0])
people = [input[i] for i in range(1, NP+1)]
money = [0 for i in range(NP)]

input = input[NP+1:len(input)]
a = 0
while a < len(input):
	currentPerson = input[a]
	numbers = input[a+1].split(" ")
	totalAmt = int(numbers[0])
	numReceivers = int(numbers[1])

	if numReceivers != 0:

		splitAmt = floor(totalAmt/numReceivers)
		for i in range(0, numReceivers):

			for personIdx in range(0, len(people)):
				if input[a+2+i] == people[personIdx]:
					money[personIdx] += splitAmt
					break

		remainder = totalAmt-(splitAmt*numReceivers)

		for personIdx in range(0, len(people)):
				if currentPerson == people[personIdx]:
					money[personIdx] -= totalAmt
					money[personIdx] += remainder
					break

	a += 2+numReceivers

for i in range(len(people)):
	temp = people[i]
	people[i] = temp[:len(temp)-1]

with open("gift1.out", "w") as f:
	for i in range(len(people)):
		f.write("%s %s" % (people[i], int(money[i]))+"\n")