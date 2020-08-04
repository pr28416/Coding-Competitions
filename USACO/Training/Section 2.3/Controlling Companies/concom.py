N = c = []
with open("concom.in") as f:
    N = int(f.readline())
    for i in range(N):
        c.append(tuple(map(int, f.readline().split(" "))))

controlGrid = [[0] * N for i in range(N)]
# row: owner
# row: company
for i in c:
    controlGrid[i[0]-1][i[1]-1] = i[2]

for i in controlGrid:
    print(i)