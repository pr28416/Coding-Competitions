N, M = map(int, input().split(" "))
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.switches = []
        self.isOn = False;
        self.visited = False;

    def isNextTo(self, node):
        if self.x == node.x and abs(self.y - node.y) <= 1:
            return True
        elif self.y == node.y and abs(self.x - node.x) <= 1:
            return True
        else:
            return False

    def __str__(self):
        return f"n({self.x},{self.y})" + ("y" if self.isOn else "n")

    def __repr(self):
        return f"n({self.x},{self.y})" + ("y" if self.isOn else "n")

grid = [[Node(x, y) for x in range(1, N+1)] for y in range(1, N+1)]
# for i in grid:
#     print(*i)

for i in range(M):
    c1, r1, c2, r2 = map(lambda x: int(x)-1, input().split(" "))
    # print(f"{c1}, {r1} going to {c2}, {r2}")
    grid[r1][c1].switches.append(grid[r2][c2])

for i in grid:
    for j in i:
        print(f"{j}, switches:", *j.switches)

# DFS
# def dfs_lightsOn(node):
#     node.isOn = True
#     print("Turned the light on in", node)
#     for switch in node.switches:
#         if not switch.isOn:
#             dfs_lightsOn(switch)

# dfs_lightsOn(grid[0][0])

# rooms = 0
# def dfs_crossRooms(r, c):
#     global rooms, grid, N
#     grid[r][c].visited = True;
#     rooms += 1
#     print("Can access", grid[r][c])
#     # Up
#     if r > 0 and not grid[r-1][c].visited and grid[r-1][c].isOn:
#         dfs_crossRooms(r-1, c)
#     # Down
#     if r < N-1 and not grid[r+1][c].visited and grid[r+1][c].isOn:
#         dfs_crossRooms(r+1, c)
#     # Left
#     if c > 0 and not grid[r][c-1].visited and grid[r][c-1].isOn:
#         dfs_crossRooms(r, c-1)
#     # Right
#     if c < N-1 and not grid[r][c+1].visited and grid[r][c+1].isOn:
#         dfs_crossRooms(r, c+1)

# dfs_crossRooms(0, 0)
lightgrid = [[grid[j][i].isOn for i in range(N)] for j in range(N)]
didTraverse = True
rooms = 0
grid[0][0].isOn = True
def dfs_walk(r, c):
    global grid, didTraverse
    grid[r][c].visited = True
    # Turn on possible light switches
    for switch in grid[r][c].switches:
        switch.isOn = True

    # Go to switching nodes
    # Up
    if r > 0 and not grid[r-1][c].visited and grid[r-1][c].isOn:
        didTraverse = True
        dfs_walk(r-1, c)
    # Down
    if r < N-1 and not grid[r+1][c].visited and grid[r+1][c].isOn:
        didTraverse = True
        dfs_walk(r+1, c)
    # Left
    if c > 0 and not grid[r][c-1].visited and grid[r][c-1].isOn:
        didTraverse = True
        dfs_walk(r, c-1)
    # Right
    if c < N-1 and not grid[r][c+1].visited and grid[r][c+1].isOn:
        didTraverse = True
        dfs_walk(r, c+1)


while didTraverse:
    print("DID TRAVERSE, so doing so again")
    didTraverse = False
    dfs_walk(0, 0)
    temp = [[grid[j][i].isOn for i in range(N)] for j in range(N)]
    if temp == lightgrid:
        break
    lightgrid = temp

def dfs_walk2(r, c):
    global rooms, grid, N
    grid[r][c].visited = True
    print("Currently on", grid[r][c])
    rooms += 1
    # Go to neighbors nodes
    # Up
    if r > 0 and not grid[r-1][c].visited and grid[r-1][c].isOn:
        dfs_walk2(r-1, c)
    # Down
    if r < N-1 and not grid[r+1][c].visited and grid[r+1][c].isOn:
        dfs_walk2(r+1, c)
    # Left
    if c > 0 and not grid[r][c-1].visited and grid[r][c-1].isOn:
        dfs_walk2(r, c-1)
    # Right
    if c < N-1 and not grid[r][c+1].visited and grid[r][c+1].isOn:
        dfs_walk2(r, c+1)

dfs_walk(0, 0)
for g in grid:
    for i in g:
        i.visited = False

for i in grid:
    print(*i)

dfs_walk2(0, 0)
print(rooms)
