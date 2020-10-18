T = int(input())
for s in range(T):
    N = int(input())
    grid = [None] * N
    for i in range(N):
        grid[i] = list(map(int, input().split(" ")))
    tc = 0
    for j in range(N):
        sc1 = 0
        sc2 = 0
        for i in range(N-j):
            sc1 += grid[i+j][i]
            sc2 += grid[i][i+j]
        if sc1 > tc: tc = sc1
        if sc2 > tc: tc = sc2
    print("Case #%s: %s" % (s+1, tc))