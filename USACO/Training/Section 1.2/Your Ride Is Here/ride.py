"""
ID: pranav.19
LANG: PYTHON2
TASK: ride
"""
from string import ascii_uppercase
alphabet = list(ascii_uppercase)

with open("ride.in", "r") as textfile:
	line1 = textfile.readline()
	line2 = textfile.readline()

product1, product2 = 1, 1

for index, item in enumerate(line1):
	if item != "\n":
		product1 *= alphabet.index(item) + 1

for index, item in enumerate(line2):
	if item != "\n":
		product2 *= alphabet.index(item) + 1

fout = open("ride.out", "w")

if product1 % 47 == product2 % 47:
	fout.write("GO\n")
else:
	fout.write("STAY\n")

fout.close()