R, C = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(R)]

sortedPositions = [(i, j) for j in range(C) for i in range(R)]
sortedPositions.sort(reverse=True, key=lambda x: grid[x[0]][x[1]])

for pos in sortedPositions:
    r, c = pos
    up = c > 0 and grid[r][c] == grid[r][c-1]
    down = c < C-1 and grid[r][c] == grid[r][c+1]
    left = r > 0 and grid[r][c] == grid[r-1][c]
    right = r < R-1 and grid[r][c] == grid[r+1][c]
    ul = r > 0 and c > 0 and grid[r][c] == grid[r-1][c-1]
    ur = r > 0 and c < C-1 and grid[r][c] == grid[r-1][c+1]
    dl = r < R-1 and c > 0 and grid[r][c] == grid[r+1][c-1]
    dr = r < R-1 and c < C-1 and grid[r][c] == grid[r+1][c+1]
    if up or down or left or right or ul or ur or dl or dr:
        print(grid[r][c])
        break