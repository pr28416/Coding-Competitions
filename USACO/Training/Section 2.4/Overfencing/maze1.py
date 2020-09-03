"""
ID: pranav.19
LANG: PYTHON3
TASK: maze1
"""

from queue import deque

nodes = None

class Node:
    def __init__(self, h, w):
        self.h, self.w = h, w
        self.neighbors, self.values, self.didCheck = [], [1, 1], [False, False]

with open("maze1.in", "r") as f:
    W, H = map(int, f.readline().split(" "))

    nodes = [[Node(i, j) for j in range(W)] for i in range(H)]
    pre = list(map(lambda x: list(x.strip("\n")), f.readlines()))

    tests = []

    for h in range(H):
        for w in range(W):
            prePos = (h*2+1, w*2+1)
            
            if pre[prePos[0]][prePos[1]-1] != "|": # Left
                if w == 0: tests.append((h, w))
                else: nodes[h][w].neighbors.append(nodes[h][w-1])

            if pre[prePos[0]][prePos[1]+1] != "|": # Right
                if w == W-1: tests.append((h, w))
                else: nodes[h][w].neighbors.append(nodes[h][w+1])

            if pre[prePos[0]-1][prePos[1]] != "-": # Up
                if h == 0: tests.append((h, w))
                else: nodes[h][w].neighbors.append(nodes[h-1][w])

            if pre[prePos[0]+1][prePos[1]] != "-": # Down
                if h == H-1: tests.append((h, w))
                else: nodes[h][w].neighbors.append(nodes[h+1][w])

    del pre

    for test in range(len(tests)):
        root = nodes[tests[test][0]][tests[test][1]]
        qu = deque()
        qu.append(root)
        while len(qu) > 0:
            node = qu.popleft()
            node.didCheck[test] = True
            for neighbor in node.neighbors:
                if not neighbor.didCheck[test]:
                    neighbor.values[test] = node.values[test]+1
                    qu.append(neighbor)
                    neighbor.didCheck[test] = True

    answer = 0
    for h in range(H):
        for w in range(W):
            nodes[h][w] = min(nodes[h][w].values)
            if nodes[h][w] > answer:
                answer = nodes[h][w]

    with open("maze1.out", "w") as f:
        f.write(f"{answer}\n")