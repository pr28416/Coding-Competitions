def bs(x, lst, comp):
    lo, up = 0, len(lst)
    while lo < up:
        y = (up+lo)//2
        if comp(x, lst[y]): up=y
        else: lo=y+1
    return lo

N, K = map(int, input().split(" "))
haybales = sorted([int(input()) for _ in range(N)])

def fireCows(bales, K, r):
    up = 0
    for _ in range(K):
        if up == len(bales): return True
        bombLoc = bales[up]+r
        up = bs(bombLoc+r, bales, lambda x, y: x < y)
    return up == len(bales)

lo, up = 1, 50001
while lo < up:
    r = (up+lo)//2
    if fireCows(haybales, K, r): up=r
    else: lo=r+1
print(lo)