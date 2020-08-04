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

for k, i in enumerate(controlGrid):
    print(k+1, end="|  ")
    for j in i:
        print(j, end="\t")
    print()


pairs = {}

# Step 1: Count num pairs > 50
for i in range(len(controlGrid)):
    for j in range(len(controlGrid)):
        if i != j and controlGrid[i][j] > 50:
            if i+1 in pairs:
                pairs[i+1].append(j+1)
            else:
                pairs[i+1] = [j+1]

# Step 2: Assign additional percentages



print(*pairs.items())