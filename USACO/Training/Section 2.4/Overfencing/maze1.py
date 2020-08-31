"""
ID: pranav.19
LANG: PYTHON3
TASK: maze1
"""

from queue import deque

nodes = None

class Node:
    def __init__(self, h, w):
        self.h, self.w, self.d = h, w, "X"
        self.neighbors, self.v1, self.didCheck = [], 1, False
        self.v2 = 1
    def __str__(self):
        # return f"(h{self.h}, w{self.w}, d{self.d}, v{self.value})"
        # return f"({self.h}, {self.w})"
        return f"{Color.BOLD}{Color.GREEN}({self.h},{self.w}), {Color.BLUE}v1:{self.v1}, {Color.GREY}v2:{self.v2}{Color.END}"
    def __repr__(self):
        return self.__str__()

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    GREY = '\033[90m'

def test(nodes, h, w, t):
    root = nodes[h][w]
    qu = deque()
    qu.append(root)
    largestVal = 1
    while len(qu) > 0:
        node = qu.popleft()
        # print("pulled node", node)
        node.didCheck = True
        for neighbor in node.neighbors:
            if not neighbor.didCheck:
                # print("adding neighbor", neighbor)
                if t == 0:
                    neighbor.v1 = largestVal = node.v1 + 1
                else:
                    neighbor.v2 = largestVal = node.v2 + 1
                qu.append(neighbor)
                neighbor.didCheck = True
    # print()
    for node in nodes:
        for n in node:
            n.didCheck = False
    return largestVal
    

with open("maze1.in", "r") as f:
    W, H = map(int, f.readline().split(" "))

    nodes = [[Node(i, j) for j in range(W)] for i in range(H)]
    pre = list(map(lambda x: list(x.strip("\n")), f.readlines()))

    # print("PRE:")
    # for i in pre:
    #     print(*i)

    tests = []

    for h in range(H):
        for w in range(W):
            #print(f"\n========\n({h}, {w})\n========\n")
            prePos = (h*2+1, w*2+1)
            
            if pre[prePos[0]][prePos[1]-1] != "|": # Left
                if w == 0: tests.append((h, w)); nodes[h][w].d = "L"; #print("Adding exit L")
                else: nodes[h][w].neighbors.append(nodes[h][w-1]); #print("Adding neighbor L")

            if pre[prePos[0]][prePos[1]+1] != "|": # Right
                if w == W-1: tests.append((h, w)); nodes[h][w].d = "R"; #print("Adding exit R")
                else: nodes[h][w].neighbors.append(nodes[h][w+1]); #print("Adding neighbor R")

            if pre[prePos[0]-1][prePos[1]] != "-": # Up
                if h == 0: tests.append((h, w)); nodes[h][w].d = "U"; #print("Adding exit U")
                else: nodes[h][w].neighbors.append(nodes[h-1][w]); #print("Adding neighbor U")

            if pre[prePos[0]+1][prePos[1]] != "-": # Down
                if h == H-1: tests.append((h, w)); nodes[h][w].d = "D"; #print("Adding exit D")
                else: nodes[h][w].neighbors.append(nodes[h+1][w]); #print("Adding neighbor D")

            # for row in nodes:
            #     for cell in row:
            #         print(f"node: {cell}\n\tneighbors: {cell.neighbors}")

    # print("GRID:")
    # for row in nodes:
    #     print(*row)

    dimensions = []
    i = 0
    for t in tests:
        # print("Opening at:", nodes[t[0]][t[1]])

        dimensions.append(test(nodes, *t, i))
        i += 1

        # for h in nodes:
        #     print(*h)

        # print("\nresetting...")
    # del i, tests, pre
    # def stdev(a, b):
    #     avg = (a+b)/2
    #     s = (a-avg)**2+(b-avg)**2
    #     return (0.5 * s) ** 0.5
    
    # # print()
    # sd_min, maxCell = H*W, (nodes[0][0].v1, nodes[0][0].v2)
    # listOfNodes = []
    # for row in nodes:
    #     print(*row)
        # for cell in row:
        #     listOfNodes.append(cell)

    # print("dimensions:", dimensions)
    grid = [[0] * (max(dimensions)+1) for i in range(max(dimensions)+1)]

    for row in nodes:
        for cell in row:
            grid[cell.v1][cell.v2] = 1
            grid[cell.v2][cell.v1] = 1

    # print("\ngrid:")
    # for row in grid:
    #     print(*row)
    # print("\n")

    maxCell = (0, 0)
    for i in range(len(grid)-1, -1, -1):
        for j in range(i, len(grid)):
            if grid[j][i] == 1:
                maxCell = (j, i)
                break
            else:
                grid[j][i] = 'x'
        else:
            continue
        break


    # print()
    # print(answers)
    # print(f"found: maxCell: {maxCell}, writing: {min(maxCell)}")
    with open("maze1.out", "w") as f:
        f.write(f"{min(maxCell)}\n")