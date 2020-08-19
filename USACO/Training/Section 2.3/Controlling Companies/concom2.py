"""
ID: pranav.19
LANG: PYTHON3
TASK: concom
"""

N = c = []
with open("concom.in") as f:
    N = int(f.readline())
    for i in range(N):
        c.append(tuple(map(int, f.readline().split(" "))))

controlGrid = [[0] * 101 for i in range(101)]
# listOfOwners = set()
# listOfNodes = set()
maxCompany = 0
for i in c:
    controlGrid[i[0]][i[1]] = i[2]
    if i[0] > maxCompany: maxCompany = i[0]
    if i[1] > maxCompany: maxCompany = i[1]
    # listOfOwners.add(i[0])
    # listOfNodes.add(i[1])
controlGrid = controlGrid[:maxCompany+1][:maxCompany+1]

def printGrid(controlGrid, a):
    print("================\n \t|  ", end="")
    for i in range(1, a+1):
        print(i, end="\t")
    print("\n \t|  ", end="")
    for i in range(1, a+1):
        print("-", end="\t")
    print()
    for k in range(1, len(controlGrid)):
        if k > a: break
        print(k, end="\t|  ")
        for m in range(1, len(controlGrid[k])):
            if m > a: break
            print(controlGrid[k][m], end="\t")
        print()
    print("================")


pairs = [[] for i in range(101)]
pairs = set()

# Step 1: Count num pairs > 50
for i in range(1, len(controlGrid)):
    for j in range(1, len(controlGrid)):
        if i != j and controlGrid[i][j] > 50:
            pairs.add((i, j))

# Step 2: Assign additional percentages
finalized = set()
checked = set()

while len(pairs) != 0:
    # print("Process these pairs:", *pairs)
    temp = set()
    for pair in pairs:
        if pair[0] == pair[1]: continue
        # Finalize pair
        finalized.add(pair)
        # Factor in company-subsubcompany relationship - iter: 100
        for cell in range(1, len(controlGrid)):
            if pair[0] == cell or (pair[0], cell) in pairs: continue
            if (pair[0], cell) in finalized: continue
            if (pair[0], pair[1], cell) in checked: continue
            if (pair[0], cell) == (1, 18):
                print((pair[0], pair[1], cell))
            # if (pair[0], cell) == (1, 18): continue
                # print("Found (1, 18)\nBefore:")
                printGrid(controlGrid, maxCompany)

            controlGrid[pair[0]][cell] += controlGrid[pair[1]][cell]
            # Check if company now owns subsubcompany
            # if (pair[0], cell) == (1, 18):
                    # print("After:")
                    # printGrid(controlGrid, maxCompany)

            checked.add((pair[0], pair[1], cell))
            if controlGrid[pair[0]][cell] > 50:
                temp.add((pair[0], cell))

    # Fill in new pairs
    pairs = temp
        

# Step 3: Sort finalized
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
    if len(x) <= 1: return x
    return mg(sp(x[:len(x)//2]), sp(x[len(x)//2:]))


finalized = sp(list(finalized))

printGrid(controlGrid, maxCompany)


with open("concom.out", "w") as f:
    for i in finalized:
        print(f"{i[0]} {i[1]}")
        f.write(f"{i[0]} {i[1]}\n")