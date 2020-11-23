N, M = map(int, input().split(" "))
grid = [[i for i in input()] for _ in range(N)]
phrases = []

# Horizontal
for i in range(N):
    for j in range(M-2):
        phrases.append(grid[i][j]+grid[i][j+1]+grid[i][j+2])
        phrases.append(grid[i][j+2]+grid[i][j+1]+grid[i][j])

# Vertical
for j in range(M):
    for i in range(N-2):
        phrases.append(grid[i][j]+grid[i+1][j]+grid[i+2][j])
        phrases.append(grid[i+2][j]+grid[i+1][j]+grid[i][j])

# L-R Diagonal
for i in range(N-2):
    for j in range(M-2):
        phrases.append(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2])
        phrases.append(grid[i+2][j+2]+grid[i+1][j+1]+grid[i][j])

# R-L Diagonal
for i in range(N-2):
    for j in range(2, M):
        phrases.append(grid[i][j]+grid[i+1][j-1]+grid[i+2][j-2])
        phrases.append(grid[i+2][j-2]+grid[i+1][j-1]+grid[i][j])

phrases.sort()
phrases = list(filter(lambda x: (x[0]==x[1] and x[0]!=x[2] or x[1]==x[2] and x[0]!=x[2]) and x not in {"OOM", "MOO"}, phrases))
phrases = list(filter(lambda x: (x[0]==x[1] and x[2] != 'M' and x[:2] != 'OO') or (x[1]==x[2] and x[0] != 'M' and x[1:] != 'OO'), phrases))

maxCount = 0
count = int(len(phrases) > 0)
for i in range(1, len(phrases)):
    if phrases[i] != phrases[i-1]:
        maxCount = max(count, maxCount)
        count = 1
    else:
        count += 1

maxCount = max(count, maxCount)
print(maxCount)