N = int(input())
bales = sorted([list(map(int, input().split(" "))) for _ in range(N)])

maxHeight = 0

def recurse(h, i):
    global N, bales, maxHeight
    if i == N:
        if h > maxHeight: maxHeight = h
    else:
        for j in range(i, N):
            if i == 0 or bales[j][0] > bales[i-1][0] and bales[j][1] > bales[i-1][1]:
                recurse(h+1, j+1)
        if h > maxHeight: maxHeight = h

recurse(0, 0)

print(maxHeight)