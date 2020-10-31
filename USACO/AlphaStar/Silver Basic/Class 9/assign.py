N, K = map(int, input().split(" "))
grid = [["-"] * (N+1) for _ in range(N+1)]
for _ in range(K):
    t = input().split(" ")
    a, b = int(t[1]), int(t[2])
    if t[0] == "S":
        grid[a][b] = "S"
        grid[b][a] = "S"
    else:
        grid[a][b] = "D"
        grid[b][a] = "D"


C = 0
for i in grid:
    print(*i)

def recurse(comb, i):
    global N, C, grid
    if i == N+1:
        print(comb)
        C += 1
    else:
        possible = {0, 1, 2}
        sames = set()
        for j in range(1, i):
            if grid[i][j] == "S":
                sames.add(j)
            elif grid[i][j] == "D":
                possible.discard(comb[j])
        for j in possible:
            comb[i] = j
            recurse(comb, i+1)
            comb[i] = None

recurse([None]*(N+1), 1)
print(C)
"""
0 = H
1 = J
2 = G

1   2   3   4
_   _   _   _
0   0   0   x   - doesn't work
0   0   1   0   - works
0   0   1   1   - works
0   0   1   2   - works
0   0   2   0   - works
0   0   2   1   - works
0   0   2   2   - works
0   1   x   x   - doesn't work
0   2   x   x   - doesn't work
"""