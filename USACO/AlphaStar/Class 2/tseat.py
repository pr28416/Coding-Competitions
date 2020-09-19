W, R = map(int, input().split(" "))
grid = [[0] * W for _ in range(R)]
order = [(i, j) for i in range(R) for j in range(W)]
order.sort(key=lambda s: (
    ((s[0]-R+1)**2+(s[1]-W//2)**2)**0.5, # distance between points
    -s[0],
    s[1], # leftmost is given priority
))
for i in range(len(order)):
    grid[order[i][0]][order[i][1]] = i+1
for i in grid:
    print(*i)