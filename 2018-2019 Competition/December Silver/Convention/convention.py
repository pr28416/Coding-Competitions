N, M, C = 0, 0, 0
arrivals = []

with open("convention2.in", "r") as f:
    temp = f.readline().split(" ")
    N, M, C = int(temp[0]), int(temp[1]), int(temp[2])
    arrivals = [int(i) for i in f.readline().split(" ")]
    arrivals.sort()

groups = []

while len(arrivals) > 0:
    inc = 0
    temp = []
    while inc < C and len(arrivals) > 0:
        temp.append(arrivals.pop(0))
        inc += 1
    groups.append(temp)

# print(groups)

largest = 0
for group in groups:
    if group[len(group)-1]-group[0] > largest:
        largest = group[len(group)-1]-group[0]

print(largest)

with open("convention.out", "w") as f:
    f.write("%s\n" % largest)