f = open("homework.in", "r")

N = int(f.readline())
homeworks = list(map(int, f.readline().split(" ")))

f.close()

# print(N, homeworks)

lowest = [None] * (N-1) + [min(homeworks[-2:])]
sums = [None] * (N-1) + [homeworks[-1]]

for i in range(N-2, -1, -1):
    if homeworks[i] <= lowest[i+1]:
        lowest[i] = homeworks[i]
    else:
        lowest[i] = lowest[i+1]
    
    sums[i] = sums[i+1] + homeworks[i]

del lowest[-1]
# print(*lowest)
# print(*sums)

temp = [[0, 0]] * (N-1)

for k in range(1, N-1):
    temp[k] = [k, (sums[k] - lowest[k]) / float(N-k-1)]

del temp[0]

# print(temp)

temp.sort(key=lambda x: x[1], reverse=True)
# print("Look here:")
# for i in temp:
#     print(i)

smallest = [temp[0]]
for i in range(1, len(temp)):
    if temp[i][1] != temp[i-1][1]:
        break
    else:
        smallest.append(temp[i])

smallest.sort(key=lambda x: x[0])

f = open("homework.out", "w")

if len(smallest) == 0:
    f.write("0\n")
else:
    for i in smallest:         
        # print(i)
        f.write("%s\n" % i[0])

f.close()