N = int(input())
moves = [input() for _ in range(N)]

sums = [[0]*3 for _ in range(N)]
kv = {"P":0,"H":1,"S":2}
sums[0][kv[moves[0]]] = 1
for i in range(1, N):
    sums[i][0], sums[i][1], sums[i][2] = sums[i-1][0], sums[i-1][1], sums[i-1][2]
    sums[i][kv[moves[i]]] += 1

maxAmt = 0
for s in range(len(moves)):
    for i in range(3):
        for j in range(3):
            if j == i: continue
            e = sums[s][i] + sums[-1][j]-sums[s][j]
            if e > maxAmt: maxAmt = e
print(maxAmt)