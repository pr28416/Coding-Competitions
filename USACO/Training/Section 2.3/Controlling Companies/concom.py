"""
ID: pranav.19
LANG: PYTHON3
TASK: concom
"""

N = c = []
with open("concom2.in") as f:
    N = int(f.readline())
    for i in range(N):
        c.append(tuple(map(int, f.readline().split(" "))))

controlGrid = [[0] * 101 for i in range(101)]
listOfOwners = set()
listOfNodes = set()
# row: owner
# row: company
for i in c:
    controlGrid[i[0]][i[1]] = i[2]
    listOfOwners.add(i[0])
    listOfNodes.add(i[1])

def printGrid(controlGrid, a):
    print("================")
    for k, i in enumerate(controlGrid):
        if k == 0: continue
        if k > a: break
        print(k+1, end="|  ")
        for m, j in enumerate(i):
            if m == 0: continue
            if m > a: break
            print(j, end="\t")
        print()
    print("================")


pairs = [[] for i in range(101)]

# Step 1: Count num pairs > 50
for i in range(len(controlGrid)):
    for j in range(len(controlGrid)):
        if i != j and controlGrid[i][j] > 50:
            pairs[i].append(j)

# Step 2: Assign additional percentages
finalized = set()

# print("beginning with:")
# for i in range(len(pairs)):
#     if len(pairs[i]) != 0:
#         print(i, pairs[i])
# print("--------")

empty = [[] for i in range(101)]
# rd = 1
while pairs != empty:
    # print("\n\nRound", rd)
    # rd += 1
    # print("AAA...")
    # for i in range(1, len(pairs)):
    for i in listOfOwners:
        # print("\tBBB...", i)
        if len(pairs[i]) == 0: continue
        temp = []
        line = 0
        while len(pairs[i]) > 0:
            line += 1
            e = (i, pairs[i].pop())
            # print("finalized", e)
            finalized.add(e)
            # check what c owns
            # for j in range(1, len(controlGrid)):
            for j in listOfNodes:
                # print("\t\t\tDDD....")
                if j in pairs[i]: continue
                controlGrid[i][j] += controlGrid[e[1]][j]
                if controlGrid[i][j] > 50 and i != j:
                    # print(f"Added {(i, j)}")
                    temp.append(j)
        # print("finalized is now", finalized)
        for t in temp:
            pairs[i].append(t)
    
    # print("Grid became:")
    # printGrid(controlGrid, 5)
def mg(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]: x.append(a.pop(0))
        elif a[0][0] > b[0][0]: x.append(b.pop(0))
        else:
            if a[0][1] < b[0][1]: x.append(a.pop(0))
            else: x.append(b.pop(0))
    while len(a) > 0: x.append(a.pop(0))
    while len(b) > 0: x.append(b.pop(0))
    return x

def sp(x):
    if len(x) == 1: return x
    return mg(sp(x[:len(x)//2]), sp(x[len(x)//2:]))


finalized = sp(list(finalized))

# printGrid(controlGrid, 5)


with open("concom.out", "w") as f:
    for i in finalized:
        print(f"{i[0]} {i[1]}")
        f.write(f"{i[0]} {i[1]}\n")