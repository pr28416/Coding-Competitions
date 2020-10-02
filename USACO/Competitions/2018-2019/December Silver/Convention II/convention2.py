with open("convention2.in") as f:
    N = int(f.readline())
    cows = [list(map(int, f.readline().split(" "))) for _ in range(N)]
    for i in range(len(cows)):
        cows[i].append(i+1)

cows.sort(key=lambda x: (x[0], x[2]))
for i in cows:
    print(i)