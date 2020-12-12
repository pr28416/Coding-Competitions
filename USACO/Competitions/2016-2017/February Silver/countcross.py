class Node:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.north = self.south = self.east = self.west = False
        self.isCow = False
        self.num = 0

with open("countcross.in") as f:
    N, K, R = map(int, f.readline().split(" "))
    grid = [[Node(i, j) for j in range(N)] for i in range(N)]
    barriers = [list(map(lambda x: int(x)-1, f.readline().split(" "))) for _ in range(R)]

    cows = []
    for _ in range(K):
        i, j = map(int, f.readline().split(" "))
        grid[i-1][j-1].isCow = True
        cows.append(grid[i-1][j-1])

    for i in barriers:
        pos1, pos2 = i[:2], i[2:]
        if pos1[0] == pos2[0]:
            if pos1[1] < pos2[1]:
                grid[pos1[0]][pos1[1]].east = True
                grid[pos2[0]][pos2[1]].west = True
            else:
                grid[pos1[0]][pos1[1]].west = True
                grid[pos2[0]][pos2[1]].east = True
        else:
            if pos1[0] < pos2[0]:
                grid[pos1[0]][pos1[1]].south = True
                grid[pos2[0]][pos2[1]].north = True
            else:
                grid[pos1[0]][pos1[1]].north = True
                grid[pos2[0]][pos2[1]].south = True

from queue import Queue

k = 1
for i in range(N):
    for j in range(N):
        if grid[i][j].num != 0: continue
        grid[i][j].num = k
        queue = Queue()
        queue.put_nowait(grid[i][j])
        while not queue.empty():
            item = queue.get_nowait()

            if not item.north and item.r > 0 and grid[item.r-1][item.c].num == 0:
                grid[item.r-1][item.c].num = k
                queue.put_nowait(grid[item.r-1][item.c])

            if not item.south and item.r < N-1 and grid[item.r+1][item.c].num == 0:
                grid[item.r+1][item.c].num = k
                queue.put_nowait(grid[item.r+1][item.c])

            if not item.west and item.c > 0 and grid[item.r][item.c-1].num == 0:
                grid[item.r][item.c-1].num = k
                queue.put_nowait(grid[item.r][item.c-1])

            if not item.east and item.c < N-1 and grid[item.r][item.c+1].num == 0:
                grid[item.r][item.c+1].num = k
                queue.put_nowait(grid[item.r][item.c+1])
        
        k += 1
        
count = 0
for i, c1 in enumerate(cows):
    for j, c2 in enumerate(cows):
        if i == j: continue
        if c1.num != c2.num: count += 1

with open("countcross.out", "w") as f:
    f.write("%s\n" % (count//2))