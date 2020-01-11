capacities = []
amounts = []

with open("mixmilk.in", "r") as f:
    for i in range(3):
        temp = f.readline().split(" ")
        capacities.append(int(temp[0]))
        amounts.append(int(temp[1]))

for i in range(100):
    a = i % 3
    b = (a+1)%3
    amounts[b] += amounts[a]
    amounts[a] = 0
    if amounts[b] > capacities[b]:
        amounts[a] = amounts[b] - capacities[b]
        amounts[b] = capacities[b]

with open("mixmilk.out", "w") as f:
    for i in amounts:
        f.write("%s\n" % i)