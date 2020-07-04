N, cows, movements = 0, [], []
with open("shuffle.in", "r") as f:
    N = int(f.readline())
    movements = [int(i) for i in f.readline().split(" ")]
    cows = [int(i) for i in f.readline().split(" ")]

for i in range(3):
    temp = [0]*N
    for p in range(len(movements)):
        temp[p] = cows[movements[p]-1]
    cows = temp

with open("shuffle.out", "w") as f:
    for i in cows:
        f.write("%s\n" % i)