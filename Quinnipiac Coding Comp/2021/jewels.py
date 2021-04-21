from decimal import Decimal
from math import ceil

def find_color_set(colored_set, capacity): #  price, weight, color, price per weight
	print("COLORED_SET BEFORE:", colored_set)
	for gem in colored_set:
		gem.append(gem[0]/gem[1]) # euro per carat
	colored_set.sort(key=lambda x: x[2],reverse=True)
	print("COLORED_SET AFTER:", colored_set)
	# print(colored_set)
	# order on price per weight
	weight = 0
	price = 0
	for i in range(len(colored_set)):
		print(f"Weight: {weight}, Price: {price}")
		if weight + colored_set[i][1] <= capacity:
			print(">We are adding", colored_set[i][0], "as our price")
			price += colored_set[i][0]
			weight += colored_set[i][1]
			print(f"\t> Changed to Weight: {weight}, Price: {price}")
		else:
			ratio = (capacity - weight) / colored_set[i][1]
			print(ratio,ratio * colored_set[i][0])
			price += ratio * colored_set[i][0]
			print("Broke out - price is", price)
			break
	print(f"Returning {price}")
	return price

  # for each color
  # add greedily until capacity
  # return price value

T = int(input())
for _ in range(T):
	M = int(input())
	capacity = int(input())
	categories = [None] * M
	for i in range(M):
		line = input().split(" ")
		categories[i] = [Decimal(line[0]), Decimal(line[1]), line[2].strip("\n")]
	# for i in categories:
	# 	print(i)
	categories.sort(key=lambda x: x[2])
	for i in categories:
		print(i)
	listOfLists = [[categories[0]]]
	for i in range(1, len(categories)):
		if categories[i][2] != listOfLists[-1][0][2]:
			listOfLists.append([])
		listOfLists[-1].append(categories[i])
	total = 0
	for lst in listOfLists:
		total += find_color_set(lst, capacity)
	print(round(total))
	# print(total)


# s = [[1, 2, 'RED'], [3, 4, 'RED']]
# c = 9

# print(find_color_set(s, c))

'''
2
10
5
10 2 RED
8 1.2 WHITE
4 0.5 BLUE
15 3 WHITE
3 0.9 BLUE
20 5 BLUE
6 2 WHITE
20 3 RED
18 4 RED
8 0.4 WHITE
10
7
10 2 RED
8 1.2 WHITE
4 0.5 BLUE
15 3 WHITE
3 0.9 BLUE
20 5 BLUE
6 2 WHITE
20 3 RED
18 4 RED
8 0.4 WHITE


Test case #1
[Decimal('4'), Decimal('0.5'), 'BLUE']
[Decimal('3'), Decimal('0.9'), 'BLUE']
[Decimal('20'), Decimal('5'), 'BLUE']
[Decimal('10'), Decimal('2'), 'RED']
[Decimal('20'), Decimal('3'), 'RED']
[Decimal('18'), Decimal('4'), 'RED']
[Decimal('8'), Decimal('1.2'), 'WHITE']
[Decimal('15'), Decimal('3'), 'WHITE']
[Decimal('6'), Decimal('2'), 'WHITE']
[Decimal('8'), Decimal('0.4'), 'WHITE']

Test case #2
[Decimal('4'), Decimal('0.5'), 'BLUE']
[Decimal('3'), Decimal('0.9'), 'BLUE']
[Decimal('20'), Decimal('5'), 'BLUE']
[Decimal('10'), Decimal('2'), 'RED']
[Decimal('20'), Decimal('3'), 'RED']
[Decimal('18'), Decimal('4'), 'RED']
[Decimal('8'), Decimal('1.2'), 'WHITE']
[Decimal('15'), Decimal('3'), 'WHITE']
[Decimal('6'), Decimal('2'), 'WHITE']
[Decimal('8'), Decimal('0.4'), 'WHITE']
'''