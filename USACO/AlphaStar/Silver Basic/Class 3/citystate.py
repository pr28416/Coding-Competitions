N = int(input())
places = ["".join([i[:2] for i in input().split(" ")]) for _ in range(N)]
places.sort()

def bs(x, lst, comp):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo+(up-lo)//2
        if comp(x, lst[y]): up=y
        else: lo=y+1
    return lo

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abv = [f"{alpha[i]}{alpha[j]}" for i in range(26) for j in range(26)]
matrix = [[0] * 676 for _ in range(676)]

for place in places:
    rev = place[2:] + place[:2]
    lo, up = bs(rev, places, lambda x, y: x <= y), bs(rev, places, lambda x, y: x < y)
    if lo == up: continue
    i, j = bs(place[:2], abv, lambda x, y: x <= y), bs(place[2:], abv, lambda x, y: x <= y)
    matrix[i][j] += up-lo

s = 0
for i in range(676):
    for j in range(i+1, 676):
        s += matrix[i][j]
print(s)