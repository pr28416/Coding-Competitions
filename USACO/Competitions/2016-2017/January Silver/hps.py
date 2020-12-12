with open("hps.in") as f:
    N = int(f.readline())
    sums = [(0, 0, 0)]
    for _ in range(N):
        tmp = f.readline().strip("\n")
        if tmp == "H":
            sums.append((sums[-1][0]+1, sums[-1][1], sums[-1][2]))
        elif tmp == "P":
            sums.append((sums[-1][0], sums[-1][1]+1, sums[-1][2]))
        else:
            sums.append((sums[-1][0], sums[-1][1], sums[-1][2]+1))

fin = 0

for i in range(3):
    for j in range(3):
        if i == j: continue
        for h in range(N+1):
            e = sums[h][i]+sums[-1][j]-sums[h][j]
            if e > fin: fin = e

with open("hps.out", "w") as f:
    f.write("%s\n" % fin)