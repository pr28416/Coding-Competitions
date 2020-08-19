"""
ID: pranav.19
LANG: PYTHON3
TASK: concom
"""

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

def addController(i, j):
    global controlGrid, doesOwn

    if doesOwn[i][j]: return
    doesOwn[i][j] = 1
    
    for k in range(len(controlGrid)):
        controlGrid[i][k] += controlGrid[j][k]

    for k in range(len(controlGrid)):
        if doesOwn[k][i]:
            addController(k, j)

    for k in range(len(controlGrid)):
        if controlGrid[i][k] > 50:
            addController(i, k)

def addOwner(i, j, p):
    global controlGrid, doesOwn

    for k in range(len(controlGrid)):
        if doesOwn[k][i]:
            controlGrid[k][j] += p

    for k in range(len(controlGrid)):
        if controlGrid[k][j] > 50:
            addController(k, j)

controlGrid = [[0] * 101 for i in range(101)]
doesOwn = [[0] * 101 for i in range(101)]

with open("concom.in") as f:
    N = int(f.readline())

    # controlGrid = [[0] * 101 for i in range(101)]
    # doesOwn = [[0] * 101 for i in range(101)]

    for i in range(len(doesOwn)):
        doesOwn[i][i] = 1

    for i in range(N):
        triplet = tuple(map(int, f.readline().split(" ")))
        print("scanning", *triplet)
        addOwner(*triplet)


printGrid(doesOwn, 3)
with open("concom.out", "w") as f:
    for a in range(len(doesOwn)):
        for b in range(len(doesOwn)):
            if a != b and doesOwn[a][b]:
                # print(f"{a} {b}")
                f.write(f"{a} {b}\n")